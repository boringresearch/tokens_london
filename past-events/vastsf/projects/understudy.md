# Understudy

原始页面：https://tokensand.com/p/understudy

所属活动：vastsf

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Understudy
Touko Ursin14 days agoContributorJudging locked: Event build
Understudy
Understudy turns video nobody watches into a live coach. It learns a task from expert recordings, then watches a new person on camera, corrects mistakes out loud with the expert clip for that step, and scores the attempt.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Inspiration: Companies record how their best people work, and almost nobody watches it. New hires still learn by shadowing, and mistakes get caught late. We wanted that unwatched video to coach the next person live.
How each sponsor is used:
- VAST Data (VAST AI OS): stores the 2,352-clip archive and our own recorded takes in S3. We segmented, captioned, embedded and inserted our takes into the team VastDB ourselves (2,409 rows). VAST semantic search powers "Ask the archive".
- NVIDIA Cosmos Reason: live scene reading about once a second during coaching, plus clip captions and task recognition.
- NVIDIA Cosmos Embed: vectors for the archive map, task recognition and search.
- CoreWeave: GPUs serving all the Cosmos and YOLO models.
- Weights & Biases: serverless inference. Llama 3.3 70B writes the score feedback and names the map clusters, DeepSeek V4 Flash is the fallback judge, and Weave traces every live check.
- Cursor / SpaceXAI: Used for creating the project
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

- [Touko Ursin](https://tokensand.com/u/touko-ursin)

- [View GitHub repository](https://github.com/ToukoUrsin/vast-video-agents-hack)

- [Visit project website](https://hints-modules-jvc-suspension.trycloudflare.com)

- [Watch demo video](https://drive.google.com/file/d/1FTKoPFUKaKgEr-alHf8hGr9LpdgJuH9I/view?usp=sharing)

- [项目截图](https://opengraph.githubassets.com/1/ToukoUrsin/vast-video-agents-hack)

## 页面结构化补充资料

### Technical architecture

How we built it: - Archive: VAST AI OS stores the archive. We built our own ingest into VastDB for our recorded takes (segment, caption with Cosmos Reason, embed with Cosmos Embed). - Live loop: the browser sends two frames about once a second. Cosmos Reason on CoreWeave GPUs turns each into a structured scene report, we keep only what both frames agree on, and per-step checks track progress and trigger spoken corrections with the expert clip. - Feedback and stack: W&B inference (Llama 3.3 70B) writes the feedback and names the map clusters; Weave traces every check. The app is React and FastAPI.
