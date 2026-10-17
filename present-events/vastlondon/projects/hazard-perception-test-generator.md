# Hazard perception test generator

原始页面：https://tokensand.com/p/hazard-perception-test-generator

所属活动：vastlondon

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Hazard perception test generator
sami.alsindiabout 4 hours agoContributorJudging locked: Event build
Hazard perception test generator
Generates hazard perception tests, for any industry, based on their CCTV footage
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Watch demo videoProject gallery
Demo video
Watch demo video
Project description
Hazard perception — solution architecture
Second Team 41 product on the shared lab App button. Card 1 is Video Recutter (tools/idea-upscaler/SEED.md). This document is card 3.
The test plays one indexed clip, records when the tester marks a hazard, then boxes one object from the YOLO sidecar and scores the reaction. It does not generate video and it does not call Cosmos Reason to judge the answer.
Purpose
A short hazard-perception test over the archive that is already indexed for Team 41.
Three modes pick the camera world:
Mode	What the tester is	Clip the search keeps
Driving	A driver in street traffic	capture_type streets, then traffic. Warehouse rows and nyc_bike_gopro-1 are dropped.
Forklift driver	A driver in a warehouse aisle	location warehouse3, camera_id sdg_warehouse_cam-2, capture_type warehouse
Warehouse walk	A person on foot in that aisle	The same warehouse filter
The first pass plays the clip and can prime the sidecar. The hazard is chosen when the second pass starts. One hazard is boxed. The score is a local table, 0 to 5, for Slow down, Brake, Wait, Steer away, or Continue.
User flow
Open the workshop lab page and click App. The launcher is /app/. The third card, Hazard perception, opens /app/hazard/.
Code is in tools/hazard-perception/main.py
Project links
GitHub repository
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

- [sami.alsindi](https://tokensand.com/u/sami-alsindi)

- [View GitHub repository](https://github.com/OnkarBhattacharya/Team41-project-1.13)

- [Watch demo video](https://drive.google.com/file/d/130Dzi3vnWtRMI-QUp9L1zE258axZJCZ7/view?usp=sharing)

- [项目截图](https://opengraph.githubassets.com/1/OnkarBhattacharya/Team41-project-1.13)
