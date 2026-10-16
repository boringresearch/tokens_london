# Warehouse best buddy

原始页面：https://tokensand.com/p/warehouse-best-buddy

所属活动：vastnyc

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Warehouse best buddy
Hui Xu7 days agoContributorJudging locked: Event build
Warehouse best buddy
A real-time video agent for warehouse safety and operations. It watches every camera through the VSS stack on VAST, catches near misses between workers and forklifts, finds idle labor and idle machines, prices the idle time per shift, and answers questions with cited clips.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
For warehouse safety managers and operations leads: the cameras already record every shift, but nobody has time to watch them.
Real time: every 30 s the agent checks what VSS has indexed, analyzes new footage once it is fully indexed, and the app updates within seconds.
Safety you can trust: motion tracks from the YOLO detections propose candidate near misses, NVIDIA Cosmos Reason checks that exact time window and image region, and the camera views vote. Asked directly, Cosmos called 168 of 180 clips a near miss, so the agent never relies on that question. With verification, 0 of 12 random control moments were flagged and all 3 drill near misses were caught.
Operations: idle labor, idle machines, congestion and underused zones, with recommendations tied to the evidence and an idle-cost estimate with editable assumptions (about $859 recoverable per shift, about $215k a year at the defaults).
Ask and report: plain-English questions answered by NVIDIA Nemotron-3-Ultra on W&B Inference, grounded in the analyzer's facts and VSS search, citing alerts and clips. Every number in the shift report is checked against the data.
Results go back to VastDB (alerts, flags, per-segment metrics), keyed by each segment's S3 URI, so they join with the VSS captions and embeddings.
Built with NVIDIA Cosmos Reason and Nemotron, VAST S3, DataEngine and VastDB, CoreWeave GPUs, W&B Inference and Cursor, on 60 videos from 33 camera views.
Project links
GitHub repository
Project website
Demo video
Tools used
Tools used
VAST Data
SpaceXAI (Cursor)
CoreWeave (Weights & Biases)
NVIDIA

## 公开链接

- [Hackathon](https://tokensand.com/vastnyc)

- [Project gallery](https://tokensand.com/vastnyc/projects)

- [Hui Xu](https://tokensand.com/u/hui-xu)

- [View GitHub repository](https://github.com/huixu11/vast-builders-challenge)

- [Visit project website](https://team-35-app.thecosmoslabs.com/app/)

- [Watch demo video](https://drive.google.com/file/d/1zSuZP9rVg4PIwspxM0VGJDs68Z3D1KwZ/view?usp=sharing)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/a9c52792-8432-4c13-b949-9ef4a0ce5246/3c858060-2a90-4b00-9b1c-38b6574d14a6.png)
