# Codec Motion

原始页面：https://tokensand.com/p/codec-motion

所属活动：vastsf

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Codec Motion
Luke Curley14 days agoContributorJudging locked: Event build
Codec Motion
Avoid expensive inference by utilizing built-in codec motion vectors
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
A lot of video footage is surprisingly static, and running a full interference sweep on unchanging frames is a waste of precious GPUs. We're optimizing the pipeline by using codec motion vectors, used for video codec compression, to crudely detect motion for free. This is a simple heuristic that gates a full YOLO run on the entire frame, saving up to 70% for low motion scenes, but could easily be extended to specific regions of the video and more expensive models. Everything uses my open source real-time media transport (moq.dev) allowing the AI model to only run on demand, saving even more money for rarely monitored security footage.
YOLO is running on my desktop PC at home so I can process individual frames. It's connected to my global CDN (moq.pro) which it uses to both fetch the camera footage and publish the AI detection results (as a track). The web player subscribes to tracks on demand based on the camera selected and options. We emulate live footage using VAST's sample videos slowly tricked over the network (ffmpeg -re) and everything is real-time. Object detections and motion vectors (extracted by the desktop) trail the footage by at least 2 frames (plus RTT) because we intentionally don't synchronize the sources. Real-time latency is critical for some use-cases, like drones, so we felt it would make a more honest demo.
Project links
GitHub repository
Project website
Demo video
Tools used
Tools used
CoreWeave (Weights & Biases)
NVIDIA
SpaceXAI (Cursor)

## 公开链接

- [Hackathon](https://tokensand.com/vastsf)

- [Project gallery](https://tokensand.com/vastsf/projects)

- [Luke Curley](https://tokensand.com/u/luke-curley)

- [View GitHub repository](https://github.com/kixelated/vast)

- [Visit project website](https://codec-motion.kixelated.workers.dev/)

- [Watch demo video](https://youtu.be/5-2Lw2rGEUY)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/4eb34811-74d2-4ae4-9486-e9cebc561be0/faff3418-2192-42f5-a0b2-177095ebf6eb.png)
