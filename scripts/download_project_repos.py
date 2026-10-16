#!/usr/bin/env python3
"""Download public submitted repositories without running project code."""
import concurrent.futures,datetime,json,os,subprocess,time
from pathlib import Path
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'past-events'/'repos'

def download(item):
    url,projects=item;bits=urlparse(url).path.strip('/').removesuffix('.git').split('/')
    owner,repo=bits[:2];path=DEST/owner/repo;path.parent.mkdir(parents=True,exist_ok=True)
    result={'url':url,'path':str(path.relative_to(ROOT)),'projects':projects}
    env=os.environ.copy();env.update(GIT_TERMINAL_PROMPT='0',GIT_LFS_SKIP_SMUDGE='1')
    try:
        if not (path/'.git').exists():
            p=subprocess.run(['git','-c','credential.helper=','clone','--depth','1','--',url,str(path)],env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=240)
            if p.returncode:result.update(status='failed',error=p.stderr[-1800:]);return result
        sha=subprocess.check_output(['git','-C',str(path),'rev-parse','HEAD'],text=True).strip()
        branch=subprocess.check_output(['git','-C',str(path),'branch','--show-current'],text=True).strip()
        result.update(status='downloaded',commit=sha,branch=branch)
    except subprocess.TimeoutExpired:result.update(status='failed',error='Clone timed out after 240 seconds')
    except Exception as e:result.update(status='failed',error=str(e))
    return result

def main():
    DEST.mkdir(exist_ok=True);repos={}
    for file in (ROOT/'past-events').glob('*/project-list.json'):
        for p in json.loads(file.read_text()):
            url=(p.get('repoUrl') or '').rstrip('/').removesuffix('.git')
            if url:repos.setdefault(url,[]).append({'event':file.parent.name,'title':p['title'],'slug':p['slug']})
    results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        futures=[pool.submit(download,x) for x in repos.items()]
        for f in concurrent.futures.as_completed(futures):
            r=f.result();results.append(r)
            (DEST/'manifest.json').write_text(json.dumps({'updated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'total':len(repos),'results':results},ensure_ascii=False,indent=2))
            print(f"{len(results)}/{len(repos)} {r['status']} {r['url']}",flush=True)
    results.sort(key=lambda r:r['url'].lower());ok=sum(r['status']=='downloaded' for r in results)
    lines=['# 往期项目源码仓库',f'下载日期：2026-10-16。共 {len(repos)} 个仓库：成功 {ok}，失败 {len(repos)-ok}。','使用公开 HTTPS 链接，默认分支浅克隆（`--depth 1`）。记录实际 commit，便于核查；这不是比赛当天版本，仓库可能在赛后更新。未安装依赖或执行项目代码。Git LFS 大文件保留指针，子模块未递归下载。','机器可读结果：[manifest.json](manifest.json)。','## 仓库索引','| 项目 | 仓库 / 本地源码 | 状态 |','| --- | --- | --- |']
    for r in results:
        names='、'.join(p['title'] for p in r['projects']).replace('|','／');rel=Path(r['path']).relative_to('past-events/repos')
        link=f"[源码目录]({rel.as_posix()}/)" if r['status']=='downloaded' else '未下载'
        lines.append(f"| {names} | [GitHub]({r['url']}) · {link} | {r['status']} |")
    failures=[r for r in results if r['status']!='downloaded']
    if failures:
        lines.extend(['','## 下载失败','认证失败或 Repository not found 可能表示私有、删除、链接错误或访问受限，不能仅凭错误判断具体原因。'])
        for r in failures:lines.extend(['',f"### {r['url']}",'```text',r['error'],'```'])
    (DEST/'README.md').write_text('\n\n'.join(lines[:5])+'\n\n'+'\n'.join(lines[5:])+'\n')
    print(f'COMPLETE downloaded={ok} failed={len(repos)-ok}',flush=True)
if __name__=='__main__':main()
