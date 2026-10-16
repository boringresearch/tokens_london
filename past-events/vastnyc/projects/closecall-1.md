# CloseCall

原始页面：https://tokensand.com/p/closecall-1

所属活动：vastnyc

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
CloseCall
Michael7 days agoContributorJudging locked: Event build
CloseCall
CloseCall turns the street video cities already have into measured, clip-linked evidence of near misses (close passes, cars in crosswalks, traffic squeezing work-zone flaggers) so Vision Zero and transportation teams can fix the right streets and prove the fixes worked.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Watch demo videoProject gallery
Demo video
Watch demo video
Project description
CloseCall finds near misses in the street video cities already have. NVIDIA VSS searches the VAST library (3,537 clips, 13 cameras), YOLO11 boxes every car, bike and person and uses their real size to measure gaps in metres, and NVIDIA Cosmos describes each clip so we can flag hazards like a car in the crosswalk. Each clip gets a 0 to 10 danger score, places are ranked as hotspots, and a person approves every finding against its clip.
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

- [Michael](https://tokensand.com/u/michael)

- [View GitHub repository](https://github.com/Sebilopez1/closecall)

- [Watch demo video](https://www.youtube.com/watch?v=mf90AfTFsCw)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/6c319888-d5b9-4bfd-a181-1274d1950bb7/da07b57a-0136-4045-a94c-545e1c01016a.png)

## 页面结构化补充资料

### Technical architecture

A single Python server (standard library only) and a one-page web app, deployed to Kubernetes on the event’s VAST cluster. The server calls the NVIDIA VSS API to search clips and fetch Cosmos descriptions and YOLO11 detections, turns box sizes into gap estimates in metres, scores each clip 0 to 10 and groups clips into hotspots. Findings, review decisions and blind ratings are saved as JSON files; raw video stays in VAST and is streamed through a proxy.

### Setup instructions

On the event build machine: clone github.com/Sebilopez1/closecall, then run bash deploy/deploy.sh. It reads the team’s VSS credentials from /config, stores them in a Kubernetes Secret, and deploys the server and web app. Open the app URL and press Re-scan footage to search and score the cameras. bash deploy/logs.sh shows the logs. Set CLOSECALL_CAMERA to scan a single camera.

### Lessons learned

Cosmos describes, it doesn’t measure: we needed YOLO boxes to get distances, and Cosmos to say what was happening. Using an object’s real size as a ruler works, but single-camera gaps are only good to about ±30-50% until a camera is calibrated. Showing every finding with its clip and logging a human decision made results easy to check. We also dropped an early multi-agent build plan for one simple server we could deploy in a minute.
