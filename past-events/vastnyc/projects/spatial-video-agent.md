# Spatial Video Agent

原始页面：https://tokensand.com/p/spatial-video-agent

所属活动：vastnyc

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Spatial Video Agent
Leon7 days agoContributorJudging locked: Event build
Spatial Video Agent
Spatial Video Agent lets safety and incident investigators ask one plain question across every camera and get the exact moments back, with distances in meters where the camera geometry supports it
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Spatial Video Agent answers one plain-English question across every camera in the corpus: 3,537 clips from warehouses, a Toronto dashcam, and New York and San Francisco street corners. For each hit, it runs tracking and geometry at query time and returns an answer card grouped by evidence level. Where a camera has calibration or GPS, the card shows the person-to-vehicle distance in meters with an uncertainty. Where it has neither, the agent abstains and says “no geometry”. Video and detections live in VAST S3, and captions and Cosmos embeddings are read live from VastDB on every query. NVIDIA Cosmos 3 Reason and Cosmos-Embed1 run on CoreWeave GPUs. Our FastAPI app runs on the CoreWeave cluster. W&B Weave traces every agent step. Every number comes from CV and geometry, not from the model.
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

- [Leon](https://tokensand.com/u/leon)

- [View GitHub repository](https://github.com/Paradox07127/Spatial-Video-Agent)

- [Visit project website](https://team-38-app.thecosmoslabs.com/app/)

- [Watch demo video](https://drive.google.com/file/d/1uOYmZHRu4deunYWyKfyeApz7GT5tzkxi/view)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/a2c90a72-8d13-4431-99c1-a2ff737a47e7/e248ed74-0589-43d0-9012-457f8c8ef34d.png)
