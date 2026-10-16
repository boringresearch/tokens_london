# StreetCast

原始页面：https://tokensand.com/p/streetcast

所属活动：vastnyc

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
StreetCast
Muskan Dhingra7 days agoContributorJudging locked: Event build
StreetCast
StreetCast turns New York street video into cited, ready-to-file 311 reports. A rider's footage becomes every blocked bike lane, trash pile and obstruction, with the clip and the truck's fleet number, never a plate. A newsroom picks a block and gets a narrated segment where every line cites a clip.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Watch demo videoProject gallery
Demo video
Watch demo video
Project description
StreetCast turns hours of street video into a cited record of what's blocking New York's streets, and helps people act on it.
For riders (Ride report): a delivery cyclist records her ride. StreetCast replays it and every problem lands as a field note: blocked bike lanes, double parking, trash, obstructions, graffiti, construction. Each one comes with a drafted 311 complaint: category, street, what happened, the company and fleet number, and a link to the exact clip. It also shows how much time she lost and what caused it. Fleet numbers, never license plates: accountability for companies, privacy for people.
For newsrooms (Your Block): a producer picks a neighborhood, a time of day and a travel mode. StreetCast runs six searches across the footage and builds a one-minute narrated segment. Every sentence cites the clip and time range it came from. No clip, no sentence.
Eval: claims are checked against the clips they cite, and we report the grounding rate.
How it works: VAST stores, indexes and searches the footage in VastDB. NVIDIA Cosmos Reason describes every clip, Cosmos Embed powers the search, and YOLO11 detects objects. An LLM on W&B Inference turns those descriptions into structured events and scripts, with every call traced in Weave. Built with Cursor.
Rider files it. The city sees it. The newsroom airs it.
Project links
GitHub repository
Demo video
Tools used
Tools used
VAST Data
SpaceXAI (Cursor)
CoreWeave (Weights & Biases)
NVIDIA

## 公开链接

- [Hackathon](https://tokensand.com/vastnyc)

- [Project gallery](https://tokensand.com/vastnyc/projects)

- [Muskan Dhingra](https://tokensand.com/u/muskan-dhingra)

- [View GitHub repository](https://github.com/muskancellhub/warehouse-guard)

- [Watch demo video](https://drive.google.com/file/d/156wwIljYWjdDvhwNSgVmOHJR6izyNyIN/view?usp=sharing)

- [项目截图](https://opengraph.githubassets.com/1/muskancellhub/warehouse-guard)
