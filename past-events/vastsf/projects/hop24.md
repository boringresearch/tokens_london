# HOP24

原始页面：https://tokensand.com/p/hop24

所属活动：vastsf

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
HOP24
Kaushik Sivakumar14 days agoContributorJudging locked: Event build
HOP24
Hop24 is a game where you guide a chicken across real highway footage, avoiding vehicles detected by AI.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Hop24 turns real highway footage into an arcade game. Players control an animated chicken crossing traffic recorded on Nashville’s I-24 corridor, timing hops between vehicles. The unusual part is that the cars and trucks are not manually created obstacles: before gameplay, YOLO/FastSam detects vehicles in each video frame, recording bounding boxes, labels, confidence scores, and timestamps.
The browser combines video playback with a canvas showing the chicken and game elements. Saved detections drive collision detection, while autopilot uses recent vehicle positions to estimate movement and decide when the chicken should advance, wait, or retreat.
A collision starts a second experience: investigation. Hop24 replays the event, captures evidence, uses an AI-generated video description to build a query such as “white truck,” and searches an archive for related footage from other cameras. Results can be collected into an incident report.
The system uses VAST for storage and processing, VastDB for detections and searchable data, NVIDIA Cosmos Reason for video descriptions, Cosmos Embed1 for representations, and CoreWeave GPUs. Most AI processing happens before gameplay, keeping the interactive experience responsive.
Hop24 demonstrates how detected objects can connect gameplay, video search, and investigation—while making clear that similar vehicles are only candidate sightings and that the chicken collision is fictional.
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

- [Kaushik Sivakumar](https://tokensand.com/u/kaushik-sivakumar)

- [View GitHub repository](https://github.com/vnmoorthy/hop24)

- [Visit project website](https://team-10-app.thecosmoslabs.com/app/)

- [Watch demo video](https://youtu.be/P1DWPBXSxe0)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/50b37b49-9e9f-42ec-9659-3ae18a5b1df6/511d1a1e-a1c5-4459-a32e-f14dbb85bc76.jpg)

## 页面结构化补充资料

### Technical architecture

1. The playground — your browser You watch a real highway video with an animated chicken drawn on top. You press buttons to move it across the road. The page uses HTML and JavaScript, with a canvas—a drawing board inside the browser. The chicken pictures were made in Blender 2. The messenger — a Python server When the game needs a video or information about a truck, it asks a small Python program. That program talks to the video service, called VSS, and brings the answers back. It also keeps the service’s login token away from the browser. 3. The robot helpers — preparing the videos Before you play, a processing line called VAST DataEngine sends videos through three helpers: | Helper | Think
