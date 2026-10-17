# warehouse-safety-agent

原始页面：https://tokensand.com/p/warehouse-safety-agent

所属活动：vastlondon

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
warehouse-safety-agent
Prithviraj Deccaabout 4 hours agoContributorJudging locked: Event build
warehouse-safety-agent
It gives a plant supervisor a live queue of unsafe warehouse clips — walkway, forklift load, open panels, missing vests — with the video, a reason, and a person assigned to investigate each one.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Plant safety is a supervisor console for a warehouse floor. It turns camera clips into a queue of incidents: someone off the marked walkway, a forklift carrying three or more blocks, an open machine panel, or a worker at a machine without a high-vis vest. Each case shows the clip, why it was flagged, a coaching action, and who is assigned to investigate it.
A clip is ingested into the team video archive. The app searches that archive and builds an overview: how many incidents were flagged in the selected period, how many still need an owner, how many are under investigation, and how they split across severe, high, medium, and low.
VAST is the system of record. Its video index stores the segments and finds moments by meaning. Playback streams those segments. When a supervisor assigns a case, the owner and status are saved in a VAST database table, so the assignment remains after a restart.
Cosmos watches each clip and writes the caption on the case. The ingest prompt asks for literal facts: on or off the green path, the load count, whether a panel cover is open, and whether the person at the machine is wearing a vest. Safety rules read that caption.
Weights & Biases classifies the same caption when a rule is unsure. The app calls the W&B inference API with Llama 3.1 8B and asks for one safety class. A confident rule still wins, and the case says whether W&B agreed.
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

- [Prithviraj Decca](https://tokensand.com/u/prithviraj-decca)

- [View GitHub repository](https://github.com/prithvirajdecca-spec/warehouse-safety-agent)

- [Visit project website](https://team-9-app.thecosmoslabs.com/app/)

- [Watch demo video](https://drive.google.com/file/d/1QsLy7_VjGsxYOiwVpLtLmXNAie5NgaCJ/view?usp=sharing)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/175ac175-92de-45b9-9ff2-ffbb087fa049/4d6fce89-278e-420d-913a-51958281f297.png)
