# watcher

原始页面：https://tokensand.com/p/watcher

所属活动：vastnyc

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
watcher
Subhradeep Acharjee7 days agoContributorJudging locked: Event build
watcher
A multi-agent AI copilot that locks onto a vehicle or person in one traffic camera and hands it off, camera to camera, in real time.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Watch demo videoProject gallery
Demo video
Watch demo video
Project description
When a car flees a crash or a person goes missing, operators still click from feed to feed by hand, guessing which camera comes next. The footage exists. What's missing is something that can follow one target across hundreds of feeds without getting tired. We predict where the suspect can go and try to provide insights to police while chasing
Project links
GitHub repository
Demo video
Tools used
Tools used
NVIDIA
CoreWeave (Weights & Biases)
SpaceXAI (Cursor)

## 公开链接

- [Hackathon](https://tokensand.com/vastnyc)

- [Project gallery](https://tokensand.com/vastnyc/projects)

- [Subhradeep Acharjee](https://tokensand.com/u/subhradeep-acharjee)

- [View GitHub repository](https://github.com/Subhradeep246/watcher)

- [Watch demo video](https://youtu.be/k6UQsA6DA-M)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/73138e1f-d5e8-44a6-9a95-2649d49c22a8/34855c80-6f1f-4be4-944d-f51d438bf5d2.webp)

## 页面结构化补充资料

### Technical architecture

How the project works 1. You pick a camera and click an object. The React app shows a map of NYC's 977 traffic cameras. You open one, such as 7 Ave @ 34 St, and click a car. The browser sends the camera frame and your click position to the FastAPI backend. 2. Two AI models lock onto it. The backend sends the same image and prompt to two models at the same time: NVIDIA NIM (Nemotron Omni), the main model. W&B Inference (Gemma 4, running on CoreWeave GPUs), the second opinion. Each returns JSON with the object type, a bounding box, and an appearance signature such as "yellow taxi, roof light". The backend merges the two answers into one lock. If one model fails, as NVIDIA often did with "busy"
