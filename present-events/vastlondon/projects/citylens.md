# CityLens

原始页面：https://tokensand.com/p/citylens

所属活动：vastlondon

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
CityLens
Kedar Kodgireabout 5 hours agoContributorJudging locked: Event build
CityLens
CityLens turns a city's traffic cameras into incidents you can trust. Rules find candidates, NVIDIA Cosmos checks each one and says why, and everything lands in VAST next to the video. Operators see only what matters, check street work against permits, and can simply ask the cameras.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Traffic operations centres have hundreds of cameras and a handful of people watching them. Most of what matters, like a car blocking a lane, a pedestrian stepping into traffic, or a lane closed for street work, is never seen. CityLens is a workspace for those operators.
It runs standing rules over every street camera: blocked lanes, pedestrian conflicts, cyclists squeezed by traffic, congestion, work zones and lane closures. Search over the VSS index finds candidates, then Cosmos Reason watches each clip again and gives a yes or no with a reason. So far that's 38 confirmed incidents and 106 false alarms that never reach the operator. Confirmed incidents are written to our own VastDB tables and routed to the team that would act, parking enforcement, safety review, signal timing, or a permit inspection.
Each camera is judged against its own normal using the YOLO counts, with a storyboard of the whole recording. Click a city to see its cameras alongside live 311 requests and the city's permit and road restriction data. Every work zone the cameras confirm is checked against active permits, so the city can spot unpermitted work.
There's also an assistant. It runs on W&B Inference, queries VAST through eight tools, cites clips you can play, and every step is traced in Weave.
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

- [Kedar Kodgire](https://tokensand.com/u/kedar-kodgire)

- [View GitHub repository](https://github.com/Kedar-K/citylens)

- [Visit project website](https://team-4-app.thecosmoslabs.com/app/#overview)

- [Watch demo video](https://drive.google.com/file/d/1Q3ALjIff6_bC6yDOafmHOUlGJ5kxUeBh/view?pli=1)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/44f9007d-ff93-4a4e-aa30-1569a45dee89/9de958bc-27b9-4ac9-9079-bb877d24f92d.jpg)

## 页面结构化补充资料

### Technical architecture

Video ingest is the shared VAST pipeline: clips land in VAST S3, DataEngine segments them, YOLO11 counts objects, Cosmos Reason writes a caption per clip, Cosmos Embed1 makes text and visual vectors, and everything is stored in VastDB. I re-ingested 352 street clips with my own traffic-operations prompt so the captions describe lane position, flow and work zones. CityLens sits on top. A rules engine runs hybrid search per rule and camera, sends each candidate clip back to Cosmos Reason with one pointed question, and writes the verdict and reason to a citylens.incidents table in the same VastDB. Actions (enforcement, safety review, permit inspection, 311) go to citylens.actions. Per-camera ba
