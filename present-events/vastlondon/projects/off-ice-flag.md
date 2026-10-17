# Off-ice Flag

原始页面：https://tokensand.com/p/off-ice-flag

所属活动：vastlondon

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Off-ice Flag
Bekarys Rakhymbekabout 4 hours agoContributorJudging locked: Event build
Off-ice Flag
A video agent for hockey trainers that watches a full game and flags every hit as Come off, Watch or Play on, from the signs visible on camera, so a trainer reviews a few minutes of clips instead of the whole game.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Off-ice Flag turns a full hockey game into a short review tape. Every time players make body contact, a card appears with four yes/no signs (head or neck involved, slow to rise, left the ice, favoring a limb), the caption that justified them, a one-sentence why, and a decision: Come off pauses the replay, Watch and Play on keep playing. It never names an injury or rates severity; it only reports what is visible, and a trainer makes the call.
How it works: the game is split losslessly into parts under the upload cap and uploaded to VAST with our ingest prompt. The VAST DataEngine pipeline segments each part into ~5 s clips, NVIDIA Cosmos captions each clip (steered to describe body contact and the four signs), and YOLO detections and embeddings land in VastDB. Our app polls VAST, sends each caption to Weights & Biases serverless inference for strict JSON signs plus a quote copied from the caption, applies a fixed Python decision rule (the model never picks the word), and asks W&B for a why sentence that Python checks for the quote and against medical wording. Cards appear while the game is still indexing.
Trainers can search footage in plain words (VAST hybrid search), ask questions (cached answers, VAST agent ask, or a VAST recap), and jump straight to the clip.
Project links
GitHub repository
Project website
Demo video
Tools used
Tools used
VAST Data
Claude Code Router
SpaceXAI (Cursor)
CoreWeave (Weights & Biases)
NVIDIA

## 公开链接

- [Hackathon](https://tokensand.com/vastlondon)

- [Project gallery](https://tokensand.com/vastlondon/projects)

- [Bekarys Rakhymbek](https://tokensand.com/u/bekarys-rakhymbek)

- [View GitHub repository](https://github.com/yousuf-shahzad/team-45-vast-builders-challenge-2026)

- [Visit project website](https://team-45-app.thecosmoslabs.com/app/)

- [Watch demo video](https://drive.google.com/file/d/1ZngGSX3xevVUwMvFFnby-CnAku_KL1QI/view?usp=sharing)

- [项目截图](https://opengraph.githubassets.com/1/yousuf-shahzad/team-45-vast-builders-challenge-2026)

## 页面结构化补充资料

### Technical architecture

One FastAPI app (Python 3.12) on our team's Kubernetes namespace, served at /app with no Docker build: public python:3.12-slim image, code in ConfigMaps. - vss_client.py: every VAST call. Login, lossless split + upload, segments, stream proxy (the VAST token never reaches the browser), stored YOLO labels, hybrid search, agent ask, synthesize, re-ingest. - decision.py: every W&B call. Caption -> {contact, 4 signs, evidence_quote} at temperature 0, validated in Python; the Come off / Watch / Play on rule; why sentences checked for the quote, the decision word, no contradicting decision, and no medical wording. - questions.py: background tape builder. Polls VAST every 15 s, processes segments i

### Setup instructions

1. git clone the repo; cd tools/off-ice-flag; pip install -r requirements.txt 2. Without VAST: python main.py and open http://localhost:8080 (sample cards). python test_offline.py runs the offline tests. 3. On the workshop VM: python vss_client.py split game.mp4, then python vss_client.py upload game_part_*.mp4 4. python decision.py check runs tricky captions (goalie save, bench, real hits) through the live model. 5. Deploy: commands at the top of tools/off-ice-flag/deploy/off-ice-flag.yaml. Open workshop.thecosmoslabs.com, click App, then Split game > Load videos and tick the parts.

### Lessons learned

- The ingest prompt decides everything: if Cosmos is not asked about body contact, no later step can find it. Our first prompt let a goalie dropping for a save and players sitting on the bench read as "slow to rise", so we defined contact strictly (one player hitting another) and listed what is not contact. - Let the model extract facts, not make the call. W&B returns yes/no signs plus a quote copied from the caption; a fixed Python rule picks the decision, so every card can be traced and tested. - A 100 MB HTTP upload cap meant a full game could not go up in one piece. Splitting by stream copy kept full quality; the app stitches the parts back onto one clock. - Long videos index slowly on s
