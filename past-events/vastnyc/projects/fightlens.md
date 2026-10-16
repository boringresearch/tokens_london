# FightLens

原始页面：https://tokensand.com/p/fightlens

所属活动：vastnyc

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
FightLens
Wanning He7 days agoContributorJudging locked: Event build
FightLens
FightLens helps boxing and MMA viewers understand fast exchanges through AI-powered action tracking, contextual explanations, and evolving win-probability estimates in one viewing interface.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Watch demo videoProject gallery
Demo video
Watch demo video
Project description
FightLens is an app that helps viewers understand what is happening in boxing and MMA, and why the balance of a fight is changing. It brings fighter tracking, exchange analysis, and win-probability estimates into one interface, with corresponding video moments viewers can revisit to inspect the evidence.
Our event-driven pipeline separates fast action detection, contextual video understanding, and decision updates. YOLO acts as an always-on sentinel, tracking fighters and flagging potential attacks. When an exchange is detected, NVIDIA Cosmos receives a clip with context before and after the trigger to interpret the action and generate an explanation. This design aims to reduce redundant video-model calls without missing brief exchanges.
VAST Data organizes video features, real-time events, and related data into shared context for prediction. The Jev architecture with clef-flash supports rapid updates to the estimated advantage. Each exchange, explanation, and probability update is linked so viewers can follow the reasoning.
The displayed probabilities are prototype estimates, not yet validated or calibrated. Next, we plan to use historical fight videos to evaluate and improve the workflow, measuring end-to-end latency and prediction quality separately. Our team combines boxing experience, AI research, and product development to make combat sports easier to follow.
Project links
GitHub repository
Demo video
Tools used
Tools used
VAST Data
NVIDIA
SpaceXAI (Cursor)

## 公开链接

- [Hackathon](https://tokensand.com/vastnyc)

- [Project gallery](https://tokensand.com/vastnyc/projects)

- [Wanning He](https://tokensand.com/u/wanning-he)

- [View GitHub repository](https://github.com/maxx1031/fightlens)

- [Watch demo video](https://www.loom.com/share/86c7dbac0dcb41af84bbbed72caa1acc)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/929bb8cb-2375-4b64-a925-89e77b1fc56c/02c5b33d-2bae-47b0-bd34-90a6a207b341.png)

## 页面结构化补充资料

### Technical architecture

Video stream → YOLO fighter tracking and potential-attack detection → event-triggered clips with pre/post-action context → NVIDIA Cosmos exchange analysis and captions → Jev / clef-flash decision updates → viewer-facing explanations and win-probability estimates. VAST Data provides shared context across video features, events, and related data. The two-branch design keeps lightweight detection running continuously while invoking video understanding around relevant exchanges. Latency and prediction quality will be evaluated separately; probability calibration remains future work.
