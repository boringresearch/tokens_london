# Auraafit

原始页面：https://tokensand.com/p/auraafit

所属活动：vastnyc

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Auraafit
Tarun Theegela7 days agoContributorJudging locked: Event build
Auraafit
AURAAFIT turns street-camera video into outfit analytics a merchandiser can act on: what people wear and carry, with a VAST clip and a W&B Weave trace behind every label, and without guessing who anyone is.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Stores count foot traffic, but they can't see what the street is wearing. AURAAFIT reads outfits from video.
It starts from event footage indexed in VAST VSS (612 clips, 13 cameras). NVIDIA YOLO11 finds and tracks each person, and W&B Inference vision (Gemma 4) labels what they wear and carry: top, bottom, outer layer, bags. Every labelling call is traced in W&B Weave. Requiring a real garment type in our prompt took typed labels from 49 to 213 out of 214. NVIDIA Cosmos3-Reason adds a scene caption for each 5-second piece.
The app at auraafit.tech replays recorded street cameras from San Francisco and New York with the labels on the boxes. Buyers can search the labels ("backpack"), and each match links to its clip and timestamp in VAST. A dashboard rolls up 214 person-sightings into colour mix, style mix and carried items, with CSV export. A merchandising agent reads only the totals and drafts store actions, such as putting carry accessories near the entrance because 32% of sightings carry a backpack.
Privacy by design: a guard filter keeps clothing and carried items only. Age, gender, race and faces are never inferred, and nothing is tracked across cameras. Counts are sightings, not unique people.
Built for retailers, landlords and business districts deciding what to stock or lease on a block. Next step: a consenting storefront camera, over repeated days.
Project links
GitHub repository
Project website
Demo video
Tools used
Tools used
VAST Data
Claude Code Router
NVIDIA
SpaceXAI (Cursor)
CoreWeave (Weights & Biases)

## 公开链接

- [Hackathon](https://tokensand.com/vastnyc)

- [Project gallery](https://tokensand.com/vastnyc/projects)

- [Tarun Theegela](https://tokensand.com/u/tarun-theegela)

- [View GitHub repository](https://github.com/bofrompursuit/vastbuildersteam49)

- [Visit project website](https://auraafit.tech)

- [Watch demo video](https://youtu.be/zCnlGEaNM_c)

- [项目截图](https://i.ytimg.com/vi/zCnlGEaNM_c/hqdefault.jpg)
