# Behind

原始页面：https://tokensand.com/p/behind

所属活动：vastlondon

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Behind
Ali Najafzadehabout 4 hours agoContributorJudging locked: Event build
Behind
"Behind" coaches a cyclist or a driver on one real clip: the street goes dark, a spotlight finds the hazard they should act on, and a voice tells them to wait, hold their line, or let the car through.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Behind is a short lesson for cyclists and drivers, taken from footage they could have been in.
You press Watch. A New York rider's view, or a San Francisco intersection, plays with nothing drawn on it. When it ends, the street goes black and one light stays on the thing that should change the next move: a person standing in front of a parked mail truck, a truck filling the lane, a rider ahead while a car closes on the right, people in a crosswalk, a car coming through from the right. A voice gives the advice in one line: wait, stay stopped, hold your line, or let it through.
A cyclist can replay the moment they would have squeezed a parked truck or swung out in the dark, and hear the move before they need it. A driver can do the same at a crossing: stay put until the stripes are empty, and do not take a gap that is already closing.
The clips and detection tracks come from VAST: video in VAST S3, indexed by VAST DataEngine into VastDB. Behind only reads that archive. NVIDIA Cosmos Reason and Cosmos Embed, on CoreWeave GPUs, wrote and embedded the descriptions. YOLO, on those same NVIDIA GPUs, is what the coach watches: the boxes pick the frame, the spotlight, and the sentence. We built Behind in Cursor with SpaceXAI. Weights & Biases serverless inference, from CoreWeave, is there for a written coaching note. The film takes its spoken line from the YOLO tracks, so the voice and the spotlight show the same thing.
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

- [Hackathon](https://tokensand.com/vastlondon)

- [Project gallery](https://tokensand.com/vastlondon/projects)

- [Ali Najafzadeh](https://tokensand.com/u/ali-najafzadeh)

- [View GitHub repository](https://github.com/ShawnAlisson/behind)

- [Visit project website](https://team-19-app.thecosmoslabs.com/app/)

- [Watch demo video](https://youtu.be/kfymIvd5KdY)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/2bfd4e45-0162-436e-8633-d7740628e163/7f79bbb7-a849-4ae6-90c7-68d75d0cf65c.webp)
