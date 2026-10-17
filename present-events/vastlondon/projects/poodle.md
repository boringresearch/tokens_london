# Poodle

原始页面：https://tokensand.com/p/poodle

所属活动：vastlondon

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Poodle
Devansh Kariaabout 4 hours agoContributorJudging locked: Event build
Poodle
Poodle is a claims desk for car insurers that watches the dashcam video of a crash, checks the driver's story against what the camera saw, works out what the policy pays, and hands anything it isn't sure about to a human.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Poodle helps car insurance handlers decide claims from video. A handler opens a claim and sees the real dashcam clip with YOLO boxes on the cars, a timeline of what happened, and the driver's statement checked line by line: supported, contradicted or unverifiable. They can ask the footage questions, and every answer cites a finding or says "Not visible". The recommendation shows what's covered and what to pay, with the policy clause or Highway Code rule behind each reason. Every file gets a SHA-256 hash, and it all prints as a one-page evidence pack.
How it decides: code owns the rules, dates and money. TypeSafe Jev answers closed questions (what happened, who was at fault, fraud risk) with a confidence score. Under 50% sure, Poodle refers the claim to a person and says why.
It also watches London. It polls about 800 TfL traffic cameras and sends each new still to Jev with 12 image questions in one call. Code turns the answers into an incident library with stills, 10-second clips and review buttons, and logs road conditions per camera every few minutes. All of London costs about $0.50 an hour.
Tools: YOLO11s finds vehicles in claim footage and live stills. We built it in Cursor and Claude Code, which shared one taskboard. Cosmos Reason (video Q&A), W&B Inference (answers) and VastDB (event store) are wired in and switch on with credentials. We had none on build day, so the demo uses recorded answers and a local event log.
Project links
GitHub repository
Project website
Demo video
Tools used
Tools used
VAST Data
SpaceXAI (Cursor)
NVIDIA

## 公开链接

- [Hackathon](https://tokensand.com/vastlondon)

- [Project gallery](https://tokensand.com/vastlondon/projects)

- [Devansh Karia](https://tokensand.com/u/devansh-karia)

- [View GitHub repository](https://github.com/devanshkaria88/vast-real-time)

- [Watch demo video](https://www.loom.com/share/9294e305159a450ab3c8e182c716213c)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/7d244bf5-c991-4194-9d62-72c1113bbdbb/cabdf128-e8ec-49a3-ab83-6bfcc9cdc996.jpg)
