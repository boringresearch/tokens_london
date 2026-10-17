# Corner Scout

原始页面：https://tokensand.com/p/corner-scout

所属活动：vastlondon

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Corner Scout
Igor Pejicabout 5 hours agoContributorJudging locked: Event build
Corner Scout
CornerScout transforms street footage into retail location intelligence, helping businesses discover high-potential locations and uncover opportunities that traditional data misses.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Google Maps shows you where stores are; CornerScout helps you discover where your next store should be.
Choosing the right retail location is one of the most important decisions a business can make. Yet traditional site selection relies on static demographics, expensive surveys, and incomplete estimates of foot traffic.
CornerScout introduces a new source of intelligence: what is actually happening on the street.
By transforming real-world street footage into actionable insights, CornerScout helps entrepreneurs, retail chains, and enterprise expansion teams identify promising locations based on observed activity, neighbourhood characteristics, and potential customer audiences.
Instead of just showing where people live or where businesses already exist, CornerScout reveals how neighbourhoods actually function.
How it works:
1. VASTData holds city neighborhood public footage indexed. CornerScout reads that index.
2. NVIDIA captioned those segments with Cosmos. The returned rows report nvidia/cosmos3-nano-reasoner. Those captions are the segment grid, and they drive the city report.
3. CoreWeave (Weights & Biases) looks at the pictures. Gemma4 W&B Inference counts and caches people, cars, cyclists, and dogs in those 180 frames.
When you name a business, a text model on the same API picks the customer audiences
4. Cursor was used to speed-up development of the platform
Project links
GitHub repository
Project website
Demo video
Tools used
Tools used
VAST Data
Vercel
SpaceXAI (Cursor)
CoreWeave (Weights & Biases)
NVIDIA
ffmpeg
gemma4B

## 公开链接

- [Hackathon](https://tokensand.com/vastlondon)

- [Project gallery](https://tokensand.com/vastlondon/projects)

- [Igor Pejic](https://tokensand.com/u/igor-pejic)

- [View GitHub repository](https://github.com/Kakoedlinnoeslovo/highlight-agent-hack)

- [Visit project website](https://corner-scout-rouge.vercel.app)

- [Watch demo video](https://drive.google.com/file/d/16EcsmFyZSnfkOk260PKlY3QeWZpNEWwv/view?usp=drive_link)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/49e5cbbf-7541-494f-b6b4-9c065624968a/fafc8955-ac6d-415f-8f79-051200eed0ab.jpg)

## 页面结构化补充资料

### Technical architecture

Python 3.11 Node.js 24 HTML, CSS, JavaScript Gradio Pydantic FFmpeg Vercel VAST NVIDIA Cosmos W&B Inference W&B Weave Gemma 4

### Lessons learned

Pre-processing videos is super helpful for real-time user searches which allows for very customized and unique search queries. Returned real videos ground the reality and provide confidence to the end-users.

### Additional screenshots or links

https://github.com/Kakoedlinnoeslovo/highlight-agent-hack/blob/1211e30349fdc283240b45865419c4bc1c5d3bb9/docs/assets/business-report-bike-shop.png?raw=true; https://github.com/Kakoedlinnoeslovo/highlight-agent-hack/blob/1211e30349fdc283240b45865419c4bc1c5d3bb9/docs/assets/corner-scout-dog-grooming.png?raw=true
