# SixthSense

原始页面：https://tokensand.com/p/sixthsense

所属活动：vastlondon

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
SixthSense
Dinesh Sunnyabout 5 hours agoContributorJudging locked: Event build
SixthSense
SixthSense watches London bus camera footage, warns about close calls, and checks the next clip to see if it was right.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
The problem: London has 25,000 bus drivers, and TfL's goal is that no one is killed on or by a London bus by 2030. Buses already carry cameras, but the footage is usually only pulled after something goes wrong. Nobody has time to watch it all, so the near misses that come before a crash, and the patterns behind them, go unseen. Safety teams often learn about a risky junction or habit only after someone is hurt.
SixthSense helps London bus safety team see which buses had a close call and what to do about it.The live map shows every London bus from TfL open data, but only draws the buses that need a look, in order of risk.
For each camera clip, SixthSense:
- searches VastDB for 8 kinds of bus hazard, like a cyclist on the nearside or a pedestrian stepping out
- checks with YOLO11 boxes for annotations, object recognition that road users are really getting closer, and drops false alarms
- asks NVIDIA Cosmos3-Reason on CoreWeave what happens next, why, and what the driver should do
- watches the next clip and scores its own prediction with a model on W&B inference, with every step traced in Weave
Note: bus positions are live TfL data. The camera clips are the hackathon footage, standing in for bus cameras.
Project links
GitHub repository
Project website
Demo video
Tools used
Tools used
VAST Data
CoreWeave (Weights & Biases)
NVIDIA
SpaceXAI (Cursor)

## 公开链接

- [Hackathon](https://tokensand.com/vastlondon)

- [Project gallery](https://tokensand.com/vastlondon/projects)

- [Dinesh Sunny](https://tokensand.com/u/dinesh-sunny)

- [View GitHub repository](https://github.com/Dinesh-Sunny/sixthsense)

- [Visit project website](https://team-43-app.thecosmoslabs.com/app/)

- [Watch demo video](https://www.loom.com/share/5caed2bab4ca4b3998251edcdcf84b53)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/f611c780-0fc7-462a-bbdc-902008e6e636/5a3e9dc7-43fd-44ac-be8f-a81428d654ff.png)

## 页面结构化补充资料

### Technical architecture

Backend: Python and FastAPI. Search uses VSS over VastDB. YOLO11 boxes and a ByteTrack tracker measure the gap between road users. Cosmos3-Reason returns the prediction as JSON. A model on W&B inference checks the prediction against the next clip. Results are saved in VastDB tables, and every model call is traced in Weave. Live map: the backend reads TfL bus data about once a minute and sends it to the browser with Socket.IO. Frontend: Next.js with Mapbox GL, exported as static files and served by FastAPI. Deploy: a second Kubernetes deployment that we switch to when ready, with a one-command rollback.

### Setup instructions

Full steps are in the README under Run it. In short: run scripts/release.sh, then on the lab VM run deploy.sh with the commit it prints. Inside the pod, sixthsense probe checks every service and sixthsense run --mode bus --limit 10 runs the agent.

### Lessons learned

Checking each prediction against the next clip gave us a real accuracy number on the day, with no manual labelling. A cheap box check before the expensive model call removed false alarms early. Showing only the buses that need attention made the map easy to read.

### Additional screenshots or links

https://wandb.ai/vastdata/team-43/weave; https://team-43-app.thecosmoslabs.com/app/dashboard/
