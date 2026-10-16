# CrossWise

原始页面：https://tokensand.com/p/crosswise

所属活动：vastnyc

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
CrossWise
SAIRAM KUMAR REDDY7 days agoContributorJudging locked: Event build
CrossWise
CrossWise is a crossing copilot for sidewalk delivery robots that watches street video and decides GO, WAIT or NO-GO every 0.2 seconds, so robots stop getting stuck at crosswalks.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Watch demo videoProject gallery
Demo video
Watch demo video
Project description
Problem. Delivery robots get stuck at crosswalks: they spin in place, miss the walk phase, or start into traffic.
What it does. CrossWise watches street video and decides GO, WAIT or NO-GO every 0.2 seconds, with the evidence drawn on the video. When a robot would wait too long, it escalates to a reroute or a remote operator. A scorecard ranks 7 crossings by difficulty for route planning.
How it works. Vehicles are tracked from the YOLO11 boxes VAST stores for every frame, with camera-shake removal and 1.5-second path prediction. The pedestrian signal is read from pixels. A vision model on W&B Inference finds cones, barriers and the free path. Unclear evidence forces WAIT. NVIDIA Cosmos Reason captions and Cosmos Embed search, on CoreWeave GPUs, found the crossing footage in the VAST archive. Decisions are stored in VastDB and model calls are traced in W&B Weave.
What we learned. Our first version had an LLM judge 5-second captions. It confused the car light with the pedestrian signal and parked cars with traffic. We rebuilt the core as frame-level perception and measured both on 5 clips: starts against DON'T WALK fell from 3 to 0, crossings rose from 6 to 8, and time from WALK to rolling dropped from 3.4 s to 1.0 s.
Limits. Decision support on recorded footage; it does not control a robot. Built end to end with Cursor.
Project links
GitHub repository
Demo video
Tools used
Tools used
VAST Data
SpaceXAI (Cursor)
CoreWeave (Weights & Biases)
NVIDIA

## 公开链接

- [Hackathon](https://tokensand.com/vastnyc)

- [Project gallery](https://tokensand.com/vastnyc/projects)

- [SAIRAM KUMAR REDDY](https://tokensand.com/u/sairam-kumar-reddy)

- [View GitHub repository](https://github.com/sairamveereddy/CROSSWISE)

- [Watch demo video](https://www.loom.com/share/d082290e4ba744e1bbc27cb5b92a51ac)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/7cffea34-6d53-4d67-b76c-378b7b441d0c/9055d604-9cb3-4d59-bf23-247f74da6035.png)
