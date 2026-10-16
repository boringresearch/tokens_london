# Grabbit Mining Co.

原始页面：https://tokensand.com/p/grabbit-mining-co

所属活动：vastsf

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Grabbit Mining Co.
Jacob14 days agoContributorJudging locked: Event build
Grabbit Mining Co.
Describe a dangerous moment in one sentence; Grabbit digs through pre-indexed warehouse and road footage and hands you a verified, exportable test set of edge cases for robotics/AV policy evaluation. AI proposes, a human decides.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Robotics and AV teams own thousands of hours of footage nobody watched. Grabbit Mining Co. turns one sentence ("forklift within 2 m of a worker in an aisle") into a human-verified test set of edge cases.
How it works (every step runs on the sponsor stack):
01 Expand — W&B Inference rewrites the sentence into 3 query variants (traced in Weave).
02 Search — Cosmos Embed vectors in VastDB over 2,352 segments indexed by VAST DataEngine; all cameras, deduped, top 12.
03 Evidence — Cosmos Reason captions + YOLO11 detections from the VSS pipeline on CoreWeave GPUs. We re-ingested 8 warehouse chunks with a custom RISK prompt (distance to forklift, walkway, running) because the default captions lacked those facts.
04 Severity — W&B Inference returns strict JSON {is_match, severity 1-5, tags, rationale}; median 402 ms per clip.
05 Review — a human presses Confirm or Reject on the page. Grabbit can't reach its own button; that's the safety feature.
06 Act — export test set (JSONL) for policy eval.
Key finding: the only severity-5 clip for the forklift query sat at search rank 9, and at rank 7 for person-vs-vehicle. Similarity search alone would have buried both. You can't just search; you have to mine.
Today's run: 3 queries, 36 hits, 17 flagged, 15 human-reviewed, 60% confirmed, 9 in the test set.
Built in Cursor with its VAST skills. The page is a static replay of today's run so nothing breaks on stage; the pipeline is live on the VM (mine.py).
Project links
GitHub repository
Project website
Demo video
Tools used
Tools used
VAST Data
CoreWeave (Weights & Biases)
NVIDIA
SpaceXAI (Cursor)

## 公开链接

- [Hackathon](https://tokensand.com/vastsf)

- [Project gallery](https://tokensand.com/vastsf/projects)

- [Jacob](https://tokensand.com/u/jacob)

- [View GitHub repository](https://github.com/jacobuku/grabbit-mining-co)

- [Visit project website](https://jacobuku.github.io/grabbit-mining-co)

- [Watch demo video](https://www.youtube.com/watch?v=RhVQOEq7XWk)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/91cbf2a4-e727-400f-97ca-848ddaccea5a/10278d16-9ec8-4427-a556-66beabeb0e2f.png)

## 页面结构化补充资料

### Technical architecture

VM (Cursor + VAST skills): mine.py → W&B Inference expand → VastDB vector search (Cosmos Embed, 256-d) → retrieval/videos for Cosmos Reason caption + YOLO11 detections → W&B Inference severity JSON (Weave-traced) → results.json + thumbs/. Frontend: static GitHub Pages reading results.json; human review stored client-side; eval_report.py computes precision and exports the test set.

### Setup instructions

Replay: open https://jacobuku.github.io/grabbit-mining-co — no setup. Re-run: on the VAST builders VM, clone the repo, python3 -m venv --without-pip .venv && pip install weave openai, set WANDB_* env vars, python mine.py → writes results.json; python thumbs.py; python eval_report.py. Full steps in README.

### Lessons learned

Default captions don't carry the facts you need (distance, walkway, running) — re-ingest with a task-specific prompt. The best edge case was search rank 9: rank by LLM severity, not similarity. Keep the demo static and honestly labeled; the VM session drops every 30 min.
