# CloseCall

原始页面：https://tokensand.com/p/closecall

所属活动：vastsf

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
CloseCall
Anonymous builder14 days agoJudging locked: Event build
CloseCall
A flight recorder for intersections. CloseCall turns traffic-camera video into a ledger of near-misses, with the clips, a plain-language search and a fix memo, so a city can make the case for a redesign before the crash instead of after it.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
For city traffic engineers. Today an intersection only "counts" as dangerous once someone is hurt, because crash reports are the only evidence a council accepts. Meanwhile, the cameras already record every close call, and nobody watches them.
What CloseCall does:
Track: Ultralytics YOLO26 tracks every road user. Post-encroachment time (PET) under 4 s flags a conflict, and a physics filter keeps only real crossing paths. Detected heads and plates are pixelated before any model sees a frame.
Triage: each candidate becomes an 8-frame storyboard, and three open models (Qwen, MiniMax, Gemma) on W&B Inference on CoreWeave vote; two of three must agree. Every vote is traced in W&B Weave.
Search: NVIDIA Nemotron embeddings let the engineer search in plain words ("turning car cutting across a pedestrian"). Identity questions are refused.
Act: NVIDIA Nemotron-3.5 Lightning drafts a fix memo in which every claim cites a clip id, and a council-packet CSV export (built with Cursor) goes to the meeting.
Play: "Spot the Near-Miss", a 10-round game: you vs the 3-model vote vs the label.
Measured, not claimed: from 141 s of footage, 1,165 raw flags → 51 candidates → 12 clips to review. The vote caught 3 of 4 labelled near-misses across all 51 events, and 1 of 2 on held-out events (blind, pre-registered labels; every step is in the repo). A VAST VSS client is built behind a storage adapter, ready to connect.
Project links
GitHub repository
Project website
Demo video
Tools used
Tools used
NVIDIA
CoreWeave (Weights & Biases)
SpaceXAI (Cursor)
VAST Data
Ultralytics YOLO26

## 公开链接

- [Hackathon](https://tokensand.com/vastsf)

- [Project gallery](https://tokensand.com/vastsf/projects)

- [View GitHub repository](https://github.com/Sidra/closecall-hack)

- [Visit project website](https://closecall-sidras-projects-db6870c6.vercel.app)

- [Watch demo video](https://bit.ly/sidra-demo)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/d643f8b0-1ad1-48a9-9bf9-b085037b9da0/d9b545ca-e156-4c43-81c9-e8ca095a72eb.jpg)

## 页面结构化补充资料

### Technical architecture

Two-stage triage. Stage 1 (cheap, local): Ultralytics YOLO26 + ByteTrack tracks road users; post-encroachment time (PET < 4 s) plus a physics filter turns 1,165 raw flags into 51 crossing-path events, and heads and plates are pixelated before any model call. Stage 2 (models): each event becomes an 8-frame storyboard, and Qwen3.6-35B, MiniMax-M3 and Gemma-4-31B on W&B Inference (CoreWeave) vote 2-of-3. Search: NVIDIA nemotron-3-embed. Memo: NVIDIA Nemotron-3.5 Lightning on W&B. Every call is traced in W&B Weave. Next.js UI (demo, ledger, evals, game). A storage adapter with a VAST VSS client (search, stream, re-ingest).

### Setup instructions

Python pipeline: pip install -r requirements.txt, set NVIDIA_API_KEY and WANDB_API_KEY (see .env.example), then python -m pipeline.candidates_run → python -m pipeline.verify_v3 → python -m pipeline.publish. Web: cd web && pnpm i && pnpm dev, then open http://localhost:3502/demo. With no keys it runs on the pre-cached run. Re-scoring the eval: the README section "Inputs → outputs → evaluation".

### Lessons learned

Cheap geometry first, models second: PET cut 1,165 flags to 51 before any model call. A 3-model vote on zoomed storyboards beat a single video model on the same clips (v1 0/4 → v3 3/4). Pre-registering the scoring rule and the labels before each run kept every number honest.

### Additional screenshots or links

https://closecall-sidras-projects-db6870c6.vercel.app/play; https://closecall-sidras-projects-db6870c6.vercel.app/evals
