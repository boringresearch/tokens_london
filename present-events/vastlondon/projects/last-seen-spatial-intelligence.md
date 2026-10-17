# Last Seen (Spatial Intelligence)

原始页面：https://tokensand.com/p/last-seen-spatial-intelligence

所属活动：vastlondon

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Last Seen (Spatial Intelligence)
Darshan Chhedaabout 5 hours agoContributorJudging locked: Event build
Last Seen (Spatial Intelligence)
When a patient with dementia walks off a ward, CCTV can only say where they were last seen, so LastSeen lets hospital staff describe the person, finds and follows them across every camera, and when they slip out of view, shows where they could be now and where to look first.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Last Seen is a search tool for the first few minutes after someone goes missing inside a building. A member of staff describes the person out loud, and Last Seen searches every camera, shows the people who fit, and asks a quick question when two of them look alike, so the right person gets picked instead of guessed. From there it follows them across cameras on a 3D model of the building. When they walk somewhere no camera covers, it shows how far they could have got, clears the areas the cameras can see are empty, and ranks the cameras and rooms worth checking first, until a camera picks them up again and confirms it is the same person. We built it on NVIDIA’s synthetic hospital footage and used only half of the cameras, keeping the rest hidden so we could check our guesses against where people really were. The footage runs through the VAST DataEngine pipeline into VastDB, which holds the video search index, our tracks and our person index. NVIDIA Cosmos Reason describes each person and checks what it says against two camera views, Cosmos Embed matches descriptions to people, YOLO11 finds people in each frame, and Canary turns speech into the search. Weights & Biases serverless inference runs the agent’s reasoning, Weave traces and scores every step, CoreWeave GPUs serve the models, and we built the whole thing in Cursor.
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
Tokens&

## 公开链接

- [Hackathon](https://tokensand.com/vastlondon)

- [Project gallery](https://tokensand.com/vastlondon/projects)

- [Darshan Chheda](https://tokensand.com/u/darshan-chheda)

- [View GitHub repository](https://github.com/1337Xcode/lastseen)

- [Visit project website](https://team-42-vss.thecosmoslabs.com/app)

- [Watch demo video](https://youtu.be/QlnaMYaLGUs)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/007065e9-6089-4cbe-9f4d-76774dd676b8/1a310b0b-15ca-46a4-9ee7-4bccc6e8fb1a.jpg)

## 页面结构化补充资料

### Technical architecture

The scene is Hospital_000 from NVIDIA’s PhysicalAI SmartSpaces dataset (CC BY 4.0). We trimmed it and uploaded it through the video search upload route, so the VAST DataEngine pipeline segments, captions and embeds it into VastDB like any other footage. A background job runs YOLO11 on each camera, and our tracker uses the camera calibration to place every detected person on the floor plan, then links the same person across cameras and over time. Cosmos Reason builds a person index from two views of each person. When someone is chosen, it works out how they differ from the people who look like them, using measured height and walking speed alongside what it can see. While the target is out of

### Setup instructions

The quickest way to try Last Seen is the live link above, which runs on the event cluster, so there’s nothing to install. To run it yourself, open a terminal on a workshop VM and clone the repo. The bootstrap script installs what the VM is missing and reads the team settings from /config. The fetch-scene command pulls the trimmed hospital scene from the repo’s release, and the deploy command pushes the app to your namespace. The README lists each command with what it expects and what it prints, and the eval command reruns the Weave Evaluation, so you can check our numbers yourself.

### Lessons learned

The first thing we learned is that video search only finds what the captioning prompt asked about. The default captions describe scenes rather than people, so we wrote our own ingest prompt about clothing, what people carry and what they’re doing. After that we treated the prompt as part of the data model, not something you set once and forget. The second was about trust. Cosmos is good at describing people, but a single camera angle can mislead it, so we only kept what two different cameras agreed on. When something failed that check, we dropped it rather than showing it with a warning. Keeping half the cameras hidden did the same job for the search map, because it let us find out where we

### Additional screenshots or links

https://docs.google.com/presentation/d/1hjY9r49PuGCSjW27vuRw-tthc61iyUWd2vosVn-araQ/edit
