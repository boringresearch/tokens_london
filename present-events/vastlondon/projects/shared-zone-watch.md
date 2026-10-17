# Shared Zone Watch

原始页面：https://tokensand.com/p/shared-zone-watch

所属活动：vastlondon

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Shared Zone Watch
Celestino Gianottiabout 4 hours agoContributorJudging locked: Event build
Shared Zone Watch
Shared Zone Watch is an operator board for warehouse safety teams. Humans and robots already share the same aisle — the danger is a few seconds, not the whole take. The app jumps to a 5second risk window when a person enters a forklift or AMR path, so a dispatcher can freeze that aisle without scrub
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Problem
Warehouse CCTV is long. Mixed traffic (people + forklifts/AMRs) is dangerous in an instant. Operators should not scrub full takes.
What we built
Shared Zone Watch sits on the team-44 VAST Video Search archive. We pin three ceiling/eye cameras from the lab corpus and open only the trigger window:
• ceiling_04 — 0:05–0:10 — person steps into the robot path (NEAR MISS)
• ceiling_01 — 0:05–0:10 — human and vehicle in the same corridor (SHARED ZONE / yield)
• eye_00 — 0:00–0:05 — contact already happened (COLLISION)
Play the 5 seconds. Close the rest of the video. Extra search hits for “person too close to a forklift or robot” can appear below the pinned cameras.
How it works
VAST + NVIDIA Cosmos/YOLO already indexed the footage at ingest. We do not re-run models on click. The app authenticates to the team VSS API, resolves those clips, proxies playback, and seeks to the known timestamps. The product is the operational call: yield, stop, or review — not another generic search box.
Stack
VAST AI OS (index, search, stream) · NVIDIA Cosmos / YOLO in the existing pipeline · Cursor on the lab VM · app deployed on the team Kubernetes Ingress at /app (workshop App button). Weights & Biases credentials were available in the environment for agent logic.
Demo line
“Don’t watch the aisle. Watch the second it goes wrong.”
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

- [Celestino Gianotti](https://tokensand.com/u/celestino-gianotti)

- [View GitHub repository](https://github.com/riomoko/vast-london-team44)

- [Visit project website](https://team-44-app.thecosmoslabs.com/app/)

- [Watch demo video](https://wowcele.com/videoha/videoha.mp4)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/835a85f2-e36d-42dd-a051-bb0f63a1699a/d15cb822-f857-4090-b821-2d8274886f65.png)
