# Linger

原始页面：https://tokensand.com/p/linger

所属活动：vastsf

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Linger
cassiusp14 days agoContributorJudging locked: Event build
Linger
Linger is a video agent that scans every street camera in the VAST library, finds where people stop and wait, and recommends design changes like seating or lighting, each backed by the real clips it came from.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Where should the bench go? Designers answer that by watching a plaza for weeks or scrubbing hours of footage, like William Whyte did. Most streets never get that attention, so seating, lighting and bus stop decisions get guessed. Linger is video agent that does this observation at scale. It scans ever camera in the VAST video library, ranks the places where people stop, wait and gather (linger), and lets a planner explore one: where people stop by day and night, what tends to happen next (a bus arrives, then a group forms where it stopped), and three plausible futures, like seating or lighting, each citing the real clips behind it. We re-ingested the footage with a behavior-only prompt, so NVIDIA Cosmos3-Reason never records faces, identity, or clothing. YOLO11 detects people and vehicles on CoreWeave GPUs. The agent reasons with W&B Inference, traces every step in Weave, and a Weave evaluation checks it never cites a missing clip or claims cause.
Built for planners, transit agencies and campuses: weeks of observation in an afternoon, backed by evidence anyone can watch.
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

- [Hackathon](https://tokensand.com/vastsf)

- [Project gallery](https://tokensand.com/vastsf/projects)

- [cassiusp](https://tokensand.com/u/cassiusp)

- [View GitHub repository](https://github.com/cassiusp-beep/linger)

- [Visit project website](https://team-19-app.thecosmoslabs.com/app/)

- [Watch demo video](https://www.loom.com/share/cfc181ab678443ecaae29bd244edd402)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/05434e3c-234a-4d25-9ee4-662f96fc3a2c/24f183ae-7aba-4411-889d-18ad0fe1221a.png)

## 页面结构化补充资料

### Technical architecture

Footage in VAST, re-ingested with our behavior only prompt Cosmos3-Reason, Embed1 and YOLO11 run on CoreWeave GPUs Agent turns clips into events and links them W&B Inference proposes futures; code verifies every cited clip Weave traces every step and evaluates the agent

### Setup instructions

git clone [link] cd linger && make set up make cache-rules make Deve, then open localhost:XXXX/app Add W&B keys to .env for LLM mode

### Lessons learned

The ingest prompt decides what can ever be search. Our first evaluation caught the agent over claiming. We tightened prompts and verify each citation in code. Rules-based fallbacks mean the demo never broke. Describing only behavior meant faces were never stored.

### Additional screenshots or links

https://wandb.ai/vastdata/team-19/weave
