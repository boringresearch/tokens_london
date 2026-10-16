#!/usr/bin/env python3
"""Count source tokens offline; never inspect .git or execute downloaded code.

Run with a Python environment containing tiktoken.
"""
import csv
import datetime
import json
import os
import re
from collections import Counter
from pathlib import Path

import tiktoken

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "past-events"
EXTENSIONS = set(""".py .pyi .pyx .pxd .pxi .js .jsx .mjs .cjs .ts .tsx .mts .cts
.html .htm .css .scss .sass .less .vue .svelte .astro .go .rs .c .h .cc .cpp
.cxx .hpp .cs .java .kt .kts .swift .m .mm .rb .php .pl .pm .lua .r .R
.jl .scala .ex .exs .erl .hrl .clj .cljs .cljc .dart .sh .bash .zsh .fish
.ps1 .bat .cmd .sql .graphql .gql .proto .tf .hcl .cmake .gradle .groovy
.sln .fs .fsx .vb .sol .s .asm .cu .cuh .awk .sed .ipynb .jinja .jinja2
.j2 .ejs .hbs .handlebars .mustache .pug .prisma""".lower().split())
SPECIAL = {"dockerfile", "containerfile", "makefile", "gnumakefile", "cmakelists.txt", "justfile", "rakefile", "gemfile", "jenkinsfile"}
EXCLUDED_DIRS = {
    ".git", ".hg", ".svn", "node_modules", "bower_components", "vendor", "_vendor",
    "third_party", "third-party", "site-packages", "dist-packages", ".venv", "venv",
    "env", ".env", "__pycache__", ".next", ".nuxt", ".output", ".svelte-kit",
    "dist", "build", "out", "target", "coverage", "htmlcov", ".tox", ".nox",
    ".cache", ".mypy_cache", ".pytest_cache", ".ruff_cache", ".turbo", ".parcel-cache",
    ".ipynb_checkpoints", "pods", "carthage", "storybook-static",
}
GENERATED = re.compile(r"(?:\.min\.|\.bundle\.|\.generated\.|_pb2(?:_grpc)?\.py$|\.pb\.(?:go|cc|h)$|\.g\.cs$|(?:^|/)(?:assets|static)/(?:index|main|chunk|vendor)[-.][A-Za-z0-9_-]{6,}\.(?:js|css)$)")
VENDORED_NAMES = {"leaflet.js", "leaflet.css", "jquery.js", "bootstrap.js", "bootstrap.css", "hls.js", "plotly.js", "d3.js"}
PRESENTATION_NAMES = {"slides.html", "slide.html", "presentation.html", "pitch.html"}
INLINE_BASE64 = re.compile(r"(data:[A-Za-z0-9.+/-]+(?:;[A-Za-z0-9=.+-]+)*;base64,)[A-Za-z0-9+/=]+")
JSON_ASSIGNMENT = re.compile(r"\s*(?:(?:const|let|var)\s+[A-Za-z_$][\w$]*\s*=|window\.[A-Za-z_$][\w$]*\s*=|export\s+default)\s*")


def is_data_only_js(text):
    remaining = text
    found = False
    while remaining.strip():
        match = JSON_ASSIGNMENT.match(remaining)
        if not match:
            return False
        try:
            obj, end = json.JSONDecoder().raw_decode(remaining[match.end():])
        except ValueError:
            return False
        if not isinstance(obj, (dict, list)):
            return False
        remaining = remaining[match.end()+end:].lstrip()
        if remaining.startswith(";"):
            remaining = remaining[1:]
        found = True
    return found


def sources(repo, skips):
    for directory, dirs, files in os.walk(repo, followlinks=False):
        # A custom-named Python virtualenv is also a dependency tree.
        if "pyvenv.cfg" in files:
            skips["virtualenv_directory"] += 1
            dirs[:] = []
            continue
        keep = []
        for name in sorted(dirs):
            path = Path(directory) / name
            if name.lower() in EXCLUDED_DIRS or path.is_symlink():
                skips["excluded_directory"] += 1
            else:
                keep.append(name)
        dirs[:] = keep
        for name in sorted(files):
            path = Path(directory) / name
            if path.is_symlink():
                skips["symlink"] += 1
                continue
            lower = name.lower()
            if path.suffix.lower() not in EXTENSIONS and lower not in SPECIAL and not lower.startswith("dockerfile."):
                skips["non_source_file"] += 1
                continue
            relative = path.relative_to(repo).as_posix()
            if GENERATED.search(relative) or lower in VENDORED_NAMES or lower in PRESENTATION_NAMES:
                skips["obvious_generated_or_vendored_file"] += 1
                continue
            yield path, relative


def code_text(path):
    raw = path.read_bytes()
    if b"\x00" in raw:
        raise ValueError("binary content")
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        text = raw.decode("latin-1")
    if path.suffix.lower() == ".ipynb":
        notebook = json.loads(text)
        chunks = []
        for cell in notebook.get("cells", []):
            if cell.get("cell_type") == "code":
                source = cell.get("source", [])
                chunks.append(source if isinstance(source, str) else "".join(source))
        text = "\n\n".join(chunks)
    if path.suffix.lower() in {".js", ".mjs", ".cjs"} and is_data_only_js(text):
        return None
    return INLINE_BASE64.sub(r"\1", text)


def main():
    enc = tiktoken.get_encoding("o200k_base")
    manifest = json.loads((OUT / "repos/manifest.json").read_text())
    rows, file_rows, errors = [], [], []
    for item in sorted(manifest["results"], key=lambda x: x["url"].lower()):
        row = {
            "repo": item["url"].removeprefix("https://github.com/"),
            "projects": " / ".join(p["title"] for p in item["projects"]),
            "url": item["url"], "path": item["path"], "download_status": item["status"],
            "code_files": 0, "code_bytes": 0, "code_lines": 0, "tokens": None,
        }
        if item["status"] == "downloaded":
            row["tokens"] = 0
            skips = Counter()
            for path, relative in sources(ROOT / item["path"], skips):
                try:
                    text = code_text(path)
                    if text is None:
                        skips["data_only_javascript"] += 1
                        continue
                    tokens = len(enc.encode(text, disallowed_special=()))
                except Exception as exc:
                    errors.append({"repo": row["repo"], "file": relative, "error": str(exc)})
                    continue
                size = len(text.encode("utf-8"))
                lines = len(text.splitlines())
                row["code_files"] += 1
                row["code_bytes"] += size
                row["code_lines"] += lines
                row["tokens"] += tokens
                file_rows.append({"repo": row["repo"], "file": relative, "code_bytes": size, "code_lines": lines, "tokens": tokens})
            row["skipped"] = dict(skips)
        rows.append(row)
        print(f"{row['repo']}: {row['tokens'] if row['tokens'] is not None else 'unavailable'}", flush=True)
    good = sorted((r for r in rows if r["tokens"] is not None), key=lambda r: r["tokens"], reverse=True)
    total = sum(r["tokens"] for r in good)
    summary = {"downloaded_repos": len(good), "unavailable_repos": len(rows)-len(good), "code_files": sum(r["code_files"] for r in good), "code_bytes": sum(r["code_bytes"] for r in good), "code_lines": sum(r["code_lines"] for r in good), "tokens": total}
    data = {"created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "encoding": "o200k_base", "summary": summary, "source_extensions": sorted(EXTENSIONS), "special_filenames": sorted(SPECIAL), "excluded_directories": sorted(EXCLUDED_DIRS), "generated_path_regex": GENERATED.pattern, "excluded_vendored_filenames": sorted(VENDORED_NAMES), "excluded_presentation_filenames": sorted(PRESENTATION_NAMES), "inline_base64_payloads_removed": True, "data_only_json_assignment_javascript_excluded": True, "results": rows, "errors": errors}
    (OUT / "code-token-counts.json").write_text(json.dumps(data, ensure_ascii=False, indent=2)+"\n")
    columns = [k for k in rows[0] if k != "skipped"]
    for filename, entries, fields in [("code-token-counts.csv", sorted(rows, key=lambda r: (r["tokens"] is None, -(r["tokens"] or 0))), columns), ("code-token-files.csv", sorted(file_rows, key=lambda r: -r["tokens"]), ["repo", "file", "code_bytes", "code_lines", "tokens"])]:
        with (OUT / filename).open("w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(entries)
    median = (good[len(good)//2-1]["tokens"] + good[len(good)//2]["tokens"])/2 if len(good)%2 == 0 else good[len(good)//2]["tokens"]
    lines = ["# 往期仓库代码 Token 统计", "", "使用本地 tiktoken 的 `o200k_base` 编码器，对每个源码文件分别分词后求和。没有调用模型 API，也没有执行下载的项目代码。", "", "## 统计口径", "", "- 完全跳过 `.git`，不读取 Git 历史或元数据。", "- 只计算支持的源码扩展名及 Dockerfile、Makefile 等构建脚本；包含源文件中的注释、字符串和空白。", "- Notebook 只计算 code cells，排除输出、Markdown 和 Notebook 元数据。", "- 排除依赖目录、Python 虚拟环境（包括自定义名称）、缓存、常见构建目录及明显的压缩/打包/生成文件。", "- 排除 Markdown/README、JSON/YAML/TOML 配置、锁文件、数据集、图片、音视频和其他二进制文件。", "- 这是本地当前版本全部符合规则的代码量；可能包含测试、重复代码和随项目复制的基础模板，不等于作者原创代码量。未被规则识别的第三方或生成代码仍可能计入。", "- token 数是所选编码器的实际计数；其他模型的 tokenizer 可能不同。拼接文件名、提示词和工具包装会额外增加上下文 token。", "- 下载失败的仓库标记为不可统计，不能当成零代码。", "", "## 汇总", "", f"- 已统计：**{len(good)} 个仓库**；另有 **{len(rows)-len(good)} 个未下载成功**。", f"- 代码文件：**{summary['code_files']:,}**；代码行数：**{summary['code_lines']:,}**。", f"- 代码 UTF-8 文本大小：**{summary['code_bytes']/1024/1024:.2f} MiB**。", f"- 合计：**{total:,} tokens（{total/1e6:.3f}M）**。", f"- 每仓库平均：**{total/len(good):,.0f} tokens**；中位数：**{median:,.0f} tokens**。", f"- 读取/解析失败文件：**{len(errors)}**（详见 JSON 的 errors）。", "", "[仓库 CSV](code-token-counts.csv) · [逐文件明细](code-token-files.csv) · [完整规则及 JSON](code-token-counts.json)", "", "## 各仓库（按 token 数降序）", "", "| 仓库 | 项目 | 代码文件 | 代码行数 | Token |", "| --- | --- | ---: | ---: | ---: |"]
    for r in good:
        lines.append(f"| [{r['repo']}]({r['url']}) | {r['projects'].replace('|', '／')} | {r['code_files']:,} | {r['code_lines']:,} | **{r['tokens']:,}** |")
    lines += ["", "## 无法统计的仓库", "", "| 仓库 | 原因 |", "| --- | --- |"]
    for r in rows:
        if r["tokens"] is None:
            lines.append(f"| [{r['repo']}]({r['url']}) | 未下载成功 |")
    lines += ["", "## 复算", "", "在安装了 `tiktoken` 的 Python 环境运行：", "", "```sh", "python scripts/count_repo_code_tokens.py", "```", ""]
    lines.insert(13, "- 额外排除已识别的纯 JSON 赋值型 JavaScript 数据文件、slides.html 等演示文稿；移除源码内嵌 data URL 的 Base64 媒体载荷，保留其余代码。代码字节数和行数均按处理后的文本统计。")
    (OUT / "CODE-TOKENS.md").write_text("\n".join(lines))
    print(json.dumps(summary, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
