# Perjury

原始页面：https://tokensand.com/p/perjury

所属活动：vastsf

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Perjury
Anonymous builder14 days agoJudging locked: Event build
Perjury
Perjury is a fact-checker for traffic video: you say or type a claim about the footage, and it splits the sentence into atomic claims, checks each one, and rules each SUPPORTED, CONTRADICTED, or "the pixels can't tell" with the evidence shown.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
PERJURYEvery claim about the footage takes the stand.
Say or type a sentence about a traffic video. PERJURY splits it into atomic claims and sends each one to the cheapest witness that can settle it. Each claim is ruled SUPPORTED, CONTRADICTED or "the pixels can't tell", with the evidence. The Cosmos jurors never see the claim, and code computes the verdict, not an LLM. It is a verify(claim) tool for any person or agent that has to sign off on what footage shows.
How it uses the stack:VastDB: the records witness. Pushdown queries settle classes, counts and metadata across every segment before any GPU call.
S3: keyframes and 4K evidence crops.
DataEngine + VSS: reads the ingest pipeline's output, and evidence reels go back in via videos/upload. The stock agent is the A/B baseline.
Cosmos3 Reasoner: jurors answer fixed questions on keyframe grids and put a box around each "yes".
Cosmos-Embed1: picks the most claim-like moment per camera.
YOLO11: its detections feed the records, and a zoom check must confirm every Cosmos "yes".
Canary-1B: speech-to-text for spoken claims.
Nemotron on W&B Inference: splits sentences into claims and labels captions.
Weave: traces every verdict, logs 👍/👎 feedback, and runs the 47-claim bench.
CoreWeave: GPU host. Each verdict shows its GPU-seconds.
K8s + FastAPI: live at /app.
Cursor: ships a perjury-verify skill.
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

- [View GitHub repository](https://github.com/charliegillet/perjury-vast-builders-challenge)

- [Visit project website](https://team-41-vss.thecosmoslabs.com/app/)

- [Watch demo video](https://drive.google.com/drive/folders/1efAnu0wfKoiQxP4-wBif5wVuTBabe5G0?usp=sharing)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/82ea98cd-fde7-48be-9221-b2b715942d79/7c1c30d9-a7d4-4bd8-afd6-e852442a123d.png)
