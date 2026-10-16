# Vision Zero Agent

原始页面：https://tokensand.com/p/vision-zero-agent-1

所属活动：vastnyc

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Vision Zero Agent
jayakumaronline7 days agoContributorJudging locked: Event build
Vision Zero Agent
Real-time alerts for news desks facing hours of raw footage: NVIDIA Cosmos checks every 5 s segment as it arrives for the event you describe (explosions: 51 of 56 found), and the same agent flags close calls on street and warehouse cameras.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
A news desk gets hours of raw footage from remote cameras in conflict zones and disaster areas, two or three hours per feed. Somewhere inside are the five seconds that matter. Nobody can watch every feed live.
Vision Zero Agent watches for them. It cuts each incoming feed into 5 s segments and sends each one to NVIDIA Cosmos Reason on CoreWeave GPUs as it arrives. When Cosmos sees the event, the agent saves the clip and alerts the desk: a pop-up and chime on the page, a desktop notification, and an email or webhook. The event is just a prompt: we built and measured it on explosions, and the same trigger can watch for fires, floods, building collapses or crowd surges.
Measured on public-domain Wikimedia Commons war films: 51 of 56 explosions found in 222 hand-checked clips (91% recall, 85% precision). On three films it had never seen, every blast raised a live alert, with 0 false alarms in 36 segments. Known limits: it misses the first flash before the cloud forms, and confuses parachutes with bombs.
The same agent protects people on everyday cameras. Across 3,500+ street and warehouse clips stored and searched on VAST, it flags cars cutting close to pedestrians and cyclists, and workers in the path of forklifts and robots (8/10 and 6/6 agree with human review). Reviewers confirm alerts, plain-English watch rules search the archive (gpt-oss-120b on W&B Inference), and one click writes an incident report. Every call is traced in W&B Weave. Built in one day with Cursor.
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

- [Hackathon](https://tokensand.com/vastnyc)

- [Project gallery](https://tokensand.com/vastnyc/projects)

- [jayakumaronline](https://tokensand.com/u/jayakumaronline)

- [View GitHub repository](https://github.com/jkfnc/vision-zero-agent-team4)

- [Visit project website](https://team-4-app.thecosmoslabs.com/app/war)

- [Watch demo video](https://github.com/jkfnc/vision-zero-agent/releases/download/v1.0-demo/vision_zero_demo.mp4)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/e98a2cf4-a1b4-4271-b2f2-5de81aae55a5/44646d8b-0c17-477f-8d4c-fcf255f9c449.png)
