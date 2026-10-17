# RAIght way

原始页面：https://tokensand.com/p/raight-way

所属活动：vastlondon

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
RAIght way
Afthab Shirazabout 5 hours agoContributorJudging locked: Event build
RAIght way
We tell cleanup crews where to go without ever needing to search themselves.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Cities have countless examples of infrastructure damage: potholes, graffiti, broken signs and so on. In order to figure out what to fix, councils must drive and search for issues manually, costing money and time. England and Wales spend £4.4 billion annually on these kind of issues, with £240 million purely due to finding out late.
With the rise of autonomous vehicles, streets are already being recorded at scale. Our product uses NVIDIA Cosmos (running on W&B Inference) to search hours of this data for damage, pinpoint where using the provided GPS data, use Nemotron to score them and decide which crews should be dispatched, then we use NVIDIA cuopt to find the optimal pathway for crews to perform maintenance. Our entire stack is built on Vast infrastructure.
Project links
GitHub repository
Project website
Demo video
Tools used
Tools used
VAST Data
CoreWeave (Weights & Biases)
NVIDIA
SpaceXAI (Cursor)

## 公开链接

- [Hackathon](https://tokensand.com/vastlondon)

- [Project gallery](https://tokensand.com/vastlondon/projects)

- [Afthab Shiraz](https://tokensand.com/u/afthab-shiraz)

- [View GitHub repository](https://github.com/Harrishayy/raightway)

- [Visit project website](https://raightway.vercel.app/review)

- [Watch demo video](https://www.youtube.com/watch?v=5s7CWI68txM)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/8201f9ba-d3fe-46b2-bc22-bd0303928cf7/15555602-ba92-4cec-8173-6bc993b17550.jpg)

## 页面结构化补充资料

### Technical architecture

We use NVIDIA Cosmos to extract moments in the footage where damage is found. We then use nemotron to score damage and categorise it, which is used to decide which type of crews need to be dispatched. We feed the GPS locations of the damages for each category into NVIDIA cuopt, which computes the optimal route between the points. This allows the crews to perform maintenance as efficiently as possible.

### Lessons learned

Understood how to use cosmos, and the benefits of Vast.
