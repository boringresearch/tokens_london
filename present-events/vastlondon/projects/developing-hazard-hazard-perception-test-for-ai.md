# Developing Hazard - Hazard perception test for AI

原始页面：https://tokensand.com/p/developing-hazard-hazard-perception-test-for-ai

所属活动：vastlondon

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Developing Hazard - Hazard perception test for AI
Moses Manabout 4 hours agoContributorJudging locked: Event build
Developing Hazard - Hazard perception test for AI
An AI agent that sits the UK DVSA hazard perception test on real dashcam footage from the VAST index, scored the way a learner driver is, with a public leaderboard against baselines.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Developing Hazard puts an AI through the hazard perception part of the UK driving theory test. It streams PIE dashcam clips from the VAST index and clicks when it spots a developing hazard. Each click is scored with the official DVSA rules: up to 5 points per hazard, more for spotting it earlier, and zero for clicking non-stop.
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

- [Moses Man](https://tokensand.com/u/moses-man)

- [View GitHub repository](https://github.com/mosesman831/developing-hazard)

- [Visit project website](https://team-36-app.thecosmoslabs.com/app/)

- [Watch demo video](https://youtu.be/8WZGNIqaB28)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/b7a7d6e3-6185-4ec6-9181-838c2b634425/04283ff2-91ca-478d-b55b-2bd06b3295e9.png)

## 页面结构化补充资料

### Technical architecture

PIE dashcam clips sit in the VAST index. The VAST pipeline runs YOLO, Cosmos Reason and Cosmos Embed and stores what they find. Our agent reads those stored detections and captions frame by frame at 5 fps, and an LLM on W&B serverless inference decides when a hazard begins. The DVSA scorer marks every click. Runs are traced in Weave and saved as JSON, and the leaderboard is built from a frozen test set. The app ships as a snapshot under 1 MB, deployed on the VAST workshop pod.

### Setup instructions

Clone the repo onto a VAST Builders VM, copy config.example to .env, add your VSS and WANDB keys, run pytest tests, then deploy with /deploy-app-no-registry.

### Lessons learned

Three Cursor agents worked in parallel, each with its own spec, and a gate checked every PR. That kept main green across 40+ PRs. The hard part was the human work, not the code: a second labelling pass got blocked by a bug, so we froze the test set with one labeller and said so openly. Size limits on the deploy pod forced a snapshot budget early on.
