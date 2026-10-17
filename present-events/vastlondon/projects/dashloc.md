# DashLoc

原始页面：https://tokensand.com/p/dashloc

所属活动：vastlondon

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
DashLoc
__about 4 hours agoContributorJudging locked: Event build
DashLoc
Helps reconstruct a journey from pure dashcam footage, for law enforcement, claim auditing and personal logging
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
What we built: GeoTrace works out where a dashcam clip was recorded from the video alone, with no GPS and no metadata. It reconstructs six 15-minute Toronto trips on a map, to a median of 10 m when we hide a sign and predict where the car was. It can also check a claim, such as “was this recorded at X?”: a made-up location came back 557 km off. We also built TripScore, which gives each trip an explainable driving-risk score from the same footage.How it works: Cosmos3-Reason reads street signs, business names, tram tracks, motion and turns from every 5-second segment. An anchor-chain solver then matches the sign reads to the OpenStreetMap road network and rejects misreads that don’t fit the distance and timing. Optical flow measures turns independently, and a second model re-checks each sign from the clip’s frames. An independent business-name check agrees for 38 of 73 names within 300 m. The app is deployed on the team cluster.Sponsor tech:NVIDIA: Cosmos3-Reason powers the sign and motion reading, plus the fault review in TripScore. YOLO11 detections drive TripScore’s tracking, and Nemotron-3.5-Super-VL-120B is the second opinion.CoreWeave and Weights & Biases: the Cosmos and YOLO endpoints run on the CoreWeave GPUs, and we called Nemotron through W&B Serverless Inference.VAST Data: we built on the pre-ingested index, S3 segments and detection sidecars through the VSS API, and deployed to the team cluster with the challenge’s skill.
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

- [__](https://tokensand.com/u/dev-3)

- [View GitHub repository](https://github.com/CXFG01/geotrace)

- [Visit project website](https://team-16-app.thecosmoslabs.com/app/)

- [Watch demo video](https://youtu.be/7zTHF3lm5ZU)

- [项目截图](https://i.ytimg.com/vi/7zTHF3lm5ZU/hqdefault.jpg)
