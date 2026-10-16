# WORLDSTATE

原始页面：https://tokensand.com/p/worldstate

所属活动：vastsf

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
WORLDSTATE
Manvender Raparia14 days agoBuilderJudging locked: Event build
WORLDSTATE
WORLDSTATE learns how physical processes should unfold from repeated video, detects when reality deviates, explains failures with NVIDIA Cosmos, and remembers them so future incidents are recognized instantly. Built for robotics, manufacturing, and warehouse operations.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
WORLDSTATE turns video from passive footage into operational memory.
Instead of only detecting objects or describing individual frames, WORLDSTATE watches repeated executions of a physical process and learns the normal sequence of states and transitions without manually labeling each step.
In our robot pick-and-place demo, WORLDSTATE learns the normal process: approach, grasp, lift, carry, descend, and place. When an object unexpectedly shifts sideways, the system detects the exact moment reality diverges from what it learned — at 1.904 seconds — and flags it as a novel failure.
NVIDIA Cosmos then explains what physically happened in natural language, while YOLO tracks the objects involved.
The operator can click Remember This Failure, adding the event to WORLDSTATE's memory. When a different run later fails in the same way, it is immediately recognized as a known failure instead of an unknown anomaly.
WORLDSTATE also includes searchable event memory and a 3D digital twin for visualizing failures and simulated recovery paths.
We additionally integrated our team's real VAST warehouse corpus: 40 clips with Cosmos Reason captions and YOLO11 detections that can be searched directly from the WORLDSTATE interface.
The goal is simple: give robots, factories, and warehouses a video agent that learns what should happen — and remembers when reality breaks.
Project links
GitHub repository
Project website
Demo video
Tools used
Tools used
SpaceXAI (Cursor)
CoreWeave (Weights & Biases)
NVIDIA
VAST Data

## 公开链接

- [Hackathon](https://tokensand.com/vastsf)

- [Project gallery](https://tokensand.com/vastsf/projects)

- [Manvender Raparia](https://tokensand.com/u/manvender-raparia)

- [View GitHub repository](https://github.com/manvendersingh21/WORLDSTATE)

- [Visit project website](https://calgary-postings-shoot-genealogy.trycloudflare.com/)

- [Watch demo video](https://drive.google.com/file/d/1MxdXFtnHElIPD97XFaFAEU25sdmKVw7L/view?usp=sharing)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/5d3dd4f4-6689-49b7-8902-6044d9997e9b/58646065-6425-4f61-8afd-eb05a5219e2b.png)

## 页面结构化补充资料

### Technical architecture

https://calgary-postings-shoot-genealogy.trycloudflare.com/static/architecture.html WORLDSTATE uses YOLO for object perception and tracking, a learned state-transition graph to model the normal physical process, trajectory and embedding-based anomaly signals to detect divergence, NVIDIA Cosmos for natural-language reasoning over what physically went wrong, and persistent event memory for semantic search and recognizing previously seen failure patterns. The frontend also includes a 3D digital twin for visualizing the robot state, divergence point, and simulated recovery.

### Setup instructions

Clone the public GitHub repository, install the Python dependencies, configure required API/environment variables in .env, then start the WORLDSTATE backend and web interface. The demo can run with the included robot dataset, and the VAST corpus page can additionally load exported VAST VSS footage and metadata.
