# Disaster Response & Humanitarian Logistics Analyzer

原始页面：https://tokensand.com/p/disaster-response-humanitarian-logistics-analyzer

所属活动：vastlondon

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Disaster Response & Humanitarian Logistics Analyzer
Andrii Drokabout 5 hours agoContributorJudging locked: Event build
Disaster Response & Humanitarian Logistics Analyzer
A video processing agent designed for aid missions, analyzing raw footage from the ground to assess supply line efficiency, structural damage, and resource distribution.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
YOLO identifies delivery vehicles, civilian crowds, or roadblocks. NVIDIA Cosmos interprets the overall scene safety or the urgency of the structural damage. Semantic search allows aid coordinators to query massive, chaotic video logs for specific logistical needs.
Project links
GitHub repository
Project website
Demo video
Tools used
Tools used
VAST Data
SpaceXAI (Cursor)
NVIDIA
CoreWeave (Weights & Biases)

## 公开链接

- [Hackathon](https://tokensand.com/vastlondon)

- [Project gallery](https://tokensand.com/vastlondon/projects)

- [Andrii Drok](https://tokensand.com/u/andrii-drok-1)

- [View GitHub repository](https://github.com/drokandrii/disasteranalyzer)

- [Visit project website](https://team-3-app.thecosmoslabs.com/app/)

- [Watch demo video](https://drive.google.com/drive/folders/1LRXonnrSFLPw2vg98wnafhqyDaXvXqlJ?usp=sharing)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/4a4ee323-d71b-4478-9b20-539d72232121/7e46f758-781c-4c00-aefb-75dd969194a4.jpg)

## 页面结构化补充资料

### Technical architecture

YOLO identifies delivery vehicles, civilian crowds, or roadblocks. NVIDIA Cosmos interprets the overall scene safety or the urgency of structural damage. Cosmos Embed1 indexes segments into VastDB. Semantic search allows aid coordinators to query video logs for specific logistical needs via a Flask-based Mission Ops UI. The app uses VSS APIs to surface insights and Weights & Biases LLMs to synthesize operational briefs based on targeted video segments.

### Setup instructions

Clone the repository: git clone https://github.com/drokandrii/disasteranalyzer Navigate to the tools/disaster-logistics/ directory. Ensure your Kubernetes environment is configured with the necessary secrets (VSS_URL, VSS_USERNAME, VSS_PASSWORD) either via a Secret or /config/ .config. Deploy the Flask app to the /app path using the provided K8s manifests. The app resolves FOCAL_VIDEO (20261017_131332_3cc5783a.mp4) on startup and locks all searches and agent actions to this ground-truth asset.

### Lessons learned

Strict Scoping is Essential: Hard-locking the application architecture to a single source of truth (FOCAL_VIDEO) at the API layer prevented cross-corpus contamination and kept the UI strictly mission-focused. Specialized Prompting: Using a highly specific, logistics-focused prompt (max 800 characters) during the re-ingestion phase with Cosmos3-Reason was the key to transforming generic visual descriptions into actionable, structured data (e.g., identifying "smoke near road" or "vehicle convoy"). Unified Infrastructure: Leveraging VAST’s AI OS data layer alongside NVIDIA Cosmos models enabled us to build a production-ready, highly searchable video API in a single day bypassing the need to sti

### Additional screenshots or links

https://drive.google.com/file/d/1Cu-NbC3u2jeNJlXC941j6-KGl5r_eQN0/view?usp=sharing; https://drive.google.com/file/d/1qiNvt_3MP241X0IXsKahlHWRiVG53jq3/view?usp=sharing
