# momentOS

原始页面：https://tokensand.com/p/momentos

所属活动：vastsf

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
momentOS
Anonymous builder14 days agoJudging locked: Event build
momentOS
MomentOS turns dashcam history into an explainable driving risk score, using video evidence to identify near-misses, attribute cause, and help insurers reward safer drivers.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
MomentOS is a credit-score-like system for driving, built from actual dashcam video history instead of coarse proxies.
For every trip, we use the VAST video pipeline to segment and index footage, then score risky precursors such as hard braking, cut-ins, tailgating, lane drift, pedestrians in path, and low time-to-collision. Cosmos Reason produces structured risk, cause, TTC and cue outputs. Cosmos Embed measures similarity to hazardous driving events, YOLO11 adds object proximity signals, and a W&B-hosted LLM provides an additional risk judgment.
We combine these signals into a per-clip risk score, then aggregate only driver-caused events into a long-term Safe Driving Score. Events caused by other road users are still surfaced, but do not penalize the driver.
The result is not just a number. Every score is backed by the exact video moments, detected cues, cause attribution, and a generated incident report. Drivers can review and contest events, and tier changes require human review.
On the Nexar public test split, our final blend reached 0.754 AP and 0.785 ROC AUC across 667 clips. The demo groups anonymous clips into simulated driver histories and shows how insurers could use this evidence-backed score to qualify safer drivers for discounts and coaching.
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

- [View GitHub repository](https://github.com/RITIK-12/momentOS)

- [Visit project website](http://team-49-vss.thecosmoslabs.com/app)

- [Watch demo video](https://youtu.be/L6RbEeg6T2Q)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/3f640ba8-9539-4c86-b660-1687be588285/cf8b6fca-97b0-4f2d-9b50-e7506362dee5.jpg)
