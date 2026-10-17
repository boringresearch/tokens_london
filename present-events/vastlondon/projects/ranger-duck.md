# Ranger Duck

原始页面：https://tokensand.com/p/ranger-duck

所属活动：vastlondon

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Ranger Duck
iverson930gabout 4 hours agoContributorJudging locked: Event build
Ranger Duck
Ranger Duck is a robot prototype built with Pollen Robotics’ simulator and MuJoCo physics engine, using real animal videos to train AI agents to respond naturally, interact with animals, observe wildlife over time, and engage with pets while tracking their activities.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
What We BuiltMicroDuck uses real-world animal videos to guide a simulated robot’s responses, combining video search, playback, agent-driven actions, and physics simulation. We ingested three Hugging Face datasets totaling X minutes of video.
Why It MattersRobot training needs diverse interaction data. MicroDuck explores using animal videos as behavioral references for embodied AI. Potential applications include long-term, close-range wildlife observation and pet companionship.
How It WorksEncounter Mode: Retrieve an interaction video, use one animal’s behavior as the situation and the other’s as a response reference, then execute MicroDuck’s closest supported action.Loop Mode: Turn each completed action into the next search prompt and repeat.The agent harness coordinates retrieval, interpretation, action selection, and execution feedback, using existing pretrained movement policies to explore future training workflows.
TechnologySimulation: Pollen Robotics’ MicroDuck simulator, MuJoCo WebAssembly physics, Three.js rendering, and ONNX Runtime Web movement policies.Agent and evaluation: Codex with MCP search tools; Weights & Biases for tracing and evaluation.Video infrastructure: VSS, VastDB, and S3 for searchable clips, captions, metadata, detections, and playback; VAST DataEngine with Cosmos3-Reason, YOLO11, and Cosmos Embed1 for descriptions, detections, and embeddings.Application: React and TypeScript frontend with a Python FastAPI backend.
Project links
GitHub repository
Project website
Demo video
Tools used
Tools used
VAST Data
CoreWeave (Weights & Biases)
NVIDIA

## 公开链接

- [Hackathon](https://tokensand.com/vastlondon)

- [Project gallery](https://tokensand.com/vastlondon/projects)

- [iverson930g](https://tokensand.com/u/iverson930g)

- [View GitHub repository](https://github.com/CoralLeiCN/rtv-hack)

- [Watch demo video](https://youtu.be/dHBOVm6pdes)

- [项目截图](https://i.ytimg.com/vi/dHBOVm6pdes/hqdefault.jpg)
