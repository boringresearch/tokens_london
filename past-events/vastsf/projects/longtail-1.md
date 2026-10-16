# LongTail

原始页面：https://tokensand.com/p/longtail-1

所属活动：vastsf

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
LongTail
Anonymous builder14 days agoJudging locked: Event build
LongTail
LongTail finds the rare, risky moments hidden in hours of unwatched traffic and warehouse video, double-checks each with an AI, and shows what the archive can't see, for self-driving and robotics teams that need edge cases to test on.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
You describe a scenario in plain words (e.g. "person close to a moving vehicle"). LongTail searches every camera separately in the VAST/VSS archive (Cosmos3-Reason descriptions, Cosmos Embed1 vectors, YOLO11 detections), then sends each hit to NVIDIA Nemotron 3.5 Lightning on W&B Inference for a yes/no/unsure verdict with a reason. The page shows verdicts live, plays confirmed clips and saves them as a test set. After each run, a second W&B call reads the rejection reasons, explains what the archive's descriptions fail to capture, and suggests a better Cosmos ingest prompt. Example: 22 search hits -> 1 confirmed (a person running toward a moving forklift); the descriptions never state distance between people and moving vehicles. Built solo with the Cursor Agent CLI and the event skills, deployed on CoreWeave Kubernetes; Weave traces verdicts from the CLI. Limits: verdicts use text descriptions, not pixels; borderline verdicts can change between runs; runs take 1-3 minutes.
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

- [Hackathon](https://tokensand.com/vastsf)

- [Project gallery](https://tokensand.com/vastsf/projects)

- [View GitHub repository](https://github.com/tossedsalads-scrambledeggs/longtail)

- [Visit project website](https://team-1-app.thecosmoslabs.com/app/longtail)

- [Watch demo video](https://drive.google.com/file/d/1c2Dz7NSTe87VxszNfwL_e2hDl681zXvR/view?usp=sharing)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/7be67221-eedb-40d8-8c68-3cbff56cc752/52f38497-4e5f-4364-8f64-8775dfc926d5.png)
