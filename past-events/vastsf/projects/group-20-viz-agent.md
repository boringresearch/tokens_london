# Group 20 (ViZ Agent)

原始页面：https://tokensand.com/p/group-20-viz-agent

所属活动：vastsf

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Group 20 (ViZ Agent)
Bindu Bhargava Reddy Chintam14 days agoBuilderJudging locked: Event build
Group 20 (ViZ Agent)
ViZ Agent finds pedestrian–vehicle conflicts in street and dashcam video, double-checks each one with three AI checks, and turns the verified ones into ranked hotspots and a drafted work order for city traffic engineers.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
The problem. San Francisco pledged Vision Zero in 2014, yet the first half of 2026 saw 100 fatal or severe crashes, more than the 92 in 2014. The city's new Street Safety Act asks for quarterly progress dashboards. Street cameras already record the close calls, but nobody has time to watch them.
What it does. ViZ Agent searches video indexed on VAST (NVIDIA VSS retrieval) for four kinds of pedestrian–vehicle conflict across a Toronto dashcam and four San Francisco street cameras. Each candidate must pass three independent checks: YOLO detections, the Cosmos Reason caption verdict, and a Nemotron grader on W&B Inference. Cosmos Reason can take a second look and explain what physically happened. Verified clips are ranked into hotspots, and the agent drafts an Open311 work order with an FHWA proven safety countermeasure picked from the conflict's cause.
For whom. City traffic engineers and Vision Zero teams. In our live run, 60 candidate clips became 4 verified conflicts, so an engineer reviews 4 clips, not 60.
Human in the loop. An engineer approves or rejects each clip with one click. Those labels measure the agent's precision and are published to W&B Weave as a dataset and an evaluation. Every search, check and model call is traced in Weave, and nothing is sent without sign-off. The whole sweep is also packaged as an Agent Skill.
Project links
GitHub repository
Project website
Demo video
Tools used
Tools used
FastAPI-MCP
Claude Code Router
VAST Data
SpaceXAI (Cursor)
CoreWeave (Weights & Biases)
NVIDIA
YOLO11
Kubernetes
HeyGen HyperFrames

## 公开链接

- [Hackathon](https://tokensand.com/vastsf)

- [Project gallery](https://tokensand.com/vastsf/projects)

- [Bindu Bhargava Reddy Chintam](https://tokensand.com/u/bindu-bhargava-reddy-chintam)

- [View GitHub repository](https://github.com/bhargavchintam/VizAgent)

- [Visit project website](https://team-20-app.thecosmoslabs.com/app/)

- [Watch demo video](https://drive.google.com/drive/folders/19vCEtQ9mrKITst7B5-MmhrQgFAvw8g74?usp=sharing)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/e68c2892-c640-40a3-ad64-87b9c51378f0/820a16e3-dee4-47ab-a5b4-6e1aab1925a7.png)
