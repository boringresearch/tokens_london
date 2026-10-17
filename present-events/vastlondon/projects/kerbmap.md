# KerbMap

原始页面：https://tokensand.com/p/kerbmap

所属活动：vastlondon

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
KerbMap
Parthasarathy Ramanujamabout 5 hours agoContributorJudging locked: Event build
KerbMap
Kerb Map turns the dashcam footage drivers already record into a live map of free kerb parking, processed on VAST with NVIDIA Cosmos, where every space shows the frame and reasoning behind it.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Drivers circle for parking because nobody knows where the free kerb is. Cities still count it by hand.
Kerb Map fixes that with footage that already exists. Connect a dashcam once and its clips sync to VAST storage. VAST DataEngine runs YOLO11, NVIDIA Cosmos Reason and Cosmos Embed1. Our kerb analysis finds parked cars and gaps and applies street rules such as junctions, driveways and crossings. It asks Cosmos only about gaps the rules can’t settle, which means 270x fewer Cosmos calls than captioning every segment. Each stretch of kerb gets a receipt in VastDB: free, occupied, not a space or can’t tell, plus when it was seen, the evidence frame and the decision trail.
In the mobile app, “Find parking” shows the nearest free spaces, and drivers confirm or correct them with 👍/👎.
Live now: 11,081 receipts in VastDB, from the organisers’ Toronto dashcam drives and street cameras.
Checked against people: 120 dashcam labels and 100 street-camera labels. Street camera agreement is 45 of 51 on held-out spots.
Built with: VAST AI OS (S3, DataEngine, VastDB), NVIDIA Cosmos and Nemotron, CoreWeave GPUs, W&B Serverless Inference and Weave, and Cursor agents.
Who pays: city kerbside teams and parking operators get kerb data without manual surveys. Dashcam owners get cloud backup and a parking finder.
List of tools used: VAST AI OS, NVIDIA, CoreWeave, W&B and Cursor
Project links
GitHub repository
Project website
Demo video
Tools used
Tools used
VAST Data
SpaceXAI (Cursor)
NVIDIA

## 公开链接

- [Hackathon](https://tokensand.com/vastlondon)

- [Project gallery](https://tokensand.com/vastlondon/projects)

- [Parthasarathy Ramanujam](https://tokensand.com/u/parthasarathy-ramanujam)

- [View GitHub repository](https://github.com/samarth-ar10/Kerb_Map)

- [Visit project website](https://team-5-app.thecosmoslabs.com/app/index.html)

- [Watch demo video](https://vimeo.com/1236839389?share=copy&fl=sv&fe=ci)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/4c74a97d-0c35-4381-b83f-04b58a7e19a9/c7b9da8c-b711-473e-85d0-c5874275a618.webp)
