# GymBro

原始页面：https://tokensand.com/p/gymbro

所属活动：vastlondon

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
GymBro
Dave Chengabout 5 hours agoContributorJudging locked: Event build
GymBro
Gym Bro is an AI fitness coaching prototype that analyses workout videos, measures joint angles and provides visual form feedback, with VAST video search and W&B tracing.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Gym Bro helps you review your exercise form from a workout video. Upload a set to find a moment worth checking, inspect your joint angles and get feedback with a visual correction.
NVIDIA Cosmos scans the video for a potential form issue. The app refines the timestamp and uses MediaPipe to measure the pose. A coaching model explains the suggested adjustment using those measurements, while an image model shows corrected form. Gym Bro measures the edited pose again to check whether it meets the target.
The "Under the hood" panel shows the analysis steps, provider attempts, timings and fallbacks. Without provider credentials, you can use local pose analysis, rule-based feedback and a target skeleton.
VAST integration searches existing indexed workout footage and plays matching clips. W&B Weave records model-call metadata without sending workout images, prompts or coaching text. CoreWeave GPU hosting is a proposed next step.
The prototype includes a labelled cached synthetic demo, an interactive architecture map and a three-minute walkthrough. Live VAST retrieval and Weave trace verification configuration and access.
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

- [Hackathon](https://tokensand.com/vastlondon)

- [Project gallery](https://tokensand.com/vastlondon/projects)

- [Dave Cheng](https://tokensand.com/u/dave-cheng)

- [View GitHub repository](https://github.com/Aerovity/Gymbro)

- [Visit project website](https://gymbro-gold.vercel.app/)

- [Watch demo video](https://www.youtube.com/watch?v=mzEJK-ebqxo)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/5d92a32f-62f3-4f05-9621-6de7b42d6f16/25cad6ae-1d15-473f-bbb1-f821b45208d0.png)

## 页面结构化补充资料

### Technical architecture

https://github.com/Aerovity/Gymbro/blob/main/ARCHITECTURE.md

### Setup instructions

https://github.com/Aerovity/Gymbro/blob/main/README.md#quick-start

### Lessons learned

Video models and pose estimation do different jobs. The video model finds a moment worth reviewing, while pose estimation supplies the measurements used in the coaching feedback. An edited image still needs checking. Gym Bro measures the corrected pose against a target, but that check covers one measurement. It cannot confirm that every form issue has been fixed. When remote services are unavailable, local pose analysis, rule-based coaching and a target skeleton let the app return partial results. The cached synthetic demo needs a clear label so users know when they are seeing a saved example rather than fresh analysis. Running pose estimation in the browser reduces server work, although per

### Additional screenshots or links

https://github.com/Aerovity/Gymbro/blob/main/docs/screens/results-mobile.png; https://github.com/Aerovity/Gymbro/blob/main/docs/screens/3d-replay-split.png
