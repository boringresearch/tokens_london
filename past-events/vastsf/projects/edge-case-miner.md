# Edge-Case Miner

原始页面：https://tokensand.com/p/edge-case-miner

所属活动：vastsf

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Edge-Case Miner
Anonymous builder14 days agoJudging locked: Event build
Edge-Case Miner
Find the rare edge-case clips AV and robotics teams need for training: describe a scenario in plain English, search every camera in a VAST video archive, let NVIDIA Cosmos3-Reason watch each candidate, and export a verified, versioned dataset.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Edge-Case Miner
Find the rare edge-case clips AV and robotics teams need for training: describe a scenario in plain English, search every camera in a VAST video archive, let NVIDIA Cosmos3-Reason watch each candidate, and export a verified, versioned dataset.
How it works
Describe the edge case in plain English, or pick one of 10 taxonomy scenarios.Expand. Qwen 3.8 on W&B Inference rewrites it as 4 caption-style search queries.Search. The scenario and its queries run concurrently against VSS hybrid search (Cosmos-Embed1 text + visual vectors in VastDB) across every camera. Hits are merged (best similarity, which queries found them) and shown with their YOLO11 object counts.Verify. Cosmos3-Reason watches each candidate: the app pulls the 5 s segment, shrinks it to 480p / 8 fps H.264 and asks for a strict JSON verdict {match, confidence, why}. If Cosmos is unavailable, DeepSeek V4 on W&B Inference judges the ingest caption instead (labelled "caption"). Verdicts are cached.Grow from good hits. "More like this" searches with a clip's caption; before/after steps to the neighbouring segments of the same video.Coverage. A scenario × location grid. Cells with no verified match are GAPs (red): the edge cases to go collect or simulate.Export. The verified set becomes a manifest (S3 URI, timestamps, camera, location, label, verdict, reason) and a versioned W&B Artifact. Every step is traced in W&B Weave.
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

- [View GitHub repository](https://github.com/chinesepowered/hack-vast)

- [Visit project website](https://team-47-app.thecosmoslabs.com/app/#mine)

- [Watch demo video](https://www.youtube.com/watch?v=6olWa6bTzIg)

- [项目截图](https://i.ytimg.com/vi/6olWa6bTzIg/hqdefault.jpg)
