# Drive Loop

原始页面：https://tokensand.com/p/drive-loop

所属活动：vastlondon

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Drive Loop
Andrei Lahunouabout 5 hours agoContributorJudging locked: Event build
Drive Loop
Drive Loop is a self-training data engine for self-driving teams: it keeps fleet camera video on VAST, finds risky moments with NVIDIA models, lets engineers check who was right, the driver or the model, and packages each moment for simulator training.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Self-driving fleets record petabytes of video, and the rare dangerous moments are what the next model must learn from. Drive Loop finds them, checks them and turns them into training data.
How it works: we use the Toronto dashcam footage already stored in the VAST VSS archive (clips in S3 on VAST, detections and search vectors in VastDB). Stored YOLO11 boxes give 558 candidates where a person is in the car's lane, out of 1,080 clips. NVIDIA Cosmos3-Reason watches each closest clip and says where the person is and what the car should do. NVIDIA Nemotron VL, served by W&B Inference, double-checks the frame and removes cyclists and duplicates: 20 events, 8 of 8 correct when checked by eye. Optical flow measures what the driver really did, so each event gets a 0-100 danger score and a driver-versus-model verdict.
Engineers review events in a web app: clip with a perception overlay, speed chart synced to the video, and a "who was right?" label that becomes training data. Anyone can write a new detector in plain words, test it on one clip on the shared NVIDIA GPU in about 5 seconds, then run it over the footage. Each event becomes a scenario package for NVIDIA Cosmos Transfer or Omniverse; the simulator studio previews up to 1,080 variants (rain, snow, night, a child). Sending to a simulator is a demo.
The app runs on CoreWeave Kubernetes, judge calls are traced in W&B Weave, and we built on the event's Cursor agent skills.
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

- [Andrei Lahunou](https://tokensand.com/u/andrei-lahunou)

- [View GitHub repository](https://github.com/vast-team-33/vaast-team-33-project)

- [Visit project website](https://team-33-app.thecosmoslabs.com/app)

- [Watch demo video](https://youtu.be/cKueRONRbL0)

- [项目截图](https://i.ytimg.com/vi/cKueRONRbL0/hqdefault.jpg)
