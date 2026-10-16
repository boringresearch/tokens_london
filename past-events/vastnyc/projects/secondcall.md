# SecondCall

原始页面：https://tokensand.com/p/secondcall

所属活动：vastnyc

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
SecondCall
Chloe Liang7 days agoContributorJudging locked: Event build
SecondCall
SecondCall turns the sports videos sitting in your camera roll into an instant, judge-blind second opinion: it hears and sees the decisive moment, checks it against the rulebook, and shows players and referees the evidence behind each call, starting with kendo.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Problem. In sports with judges, calls happen in a split second and people argue about them all the time. Friends and parents film every game, but those videos just sit in our camera rolls. We started with kendo because we both do it: a point only counts if the shout, the strike and the stomp all land in the same quarter-second.
What it does. Drop in a match video and SecondCall judges each strike: POINT, NO POINT or CAN'T TELL, with how sure it is and the proof. It also catches penalties (hansoku) and points the referees might have missed.
How it works. First it listens: the stomp and the shinai crack tell us exactly when the strike happened, and NVIDIA Canary hears which target was called. YOLO11 zooms in on the two players and blocks out the referees, then NVIDIA Cosmos looks at the frames around that moment. A rule card turns all that into a verdict, W&B Inference explains it in plain words, and Weave tracks every step. The app never sees the referees' flags, so it can't be swayed by them. Rulings live in VastDB, matches are searchable in VAST Video Search & Summary, and it all runs on CoreWeave GPUs.
Beyond kendo. Every sport is just a new rule card, so it works for judo, fencing, pickleball line calls, or any sport where calls get argued.
What we learned. Plain 5-second clips kept missing the strike. Listening for the moment first, then showing Cosmos close-up frames, fixed it.
Limits. It's a second opinion, not a replacement for referees. Built with Cursor.
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

- [Chloe Liang](https://tokensand.com/u/chloe-liang)

- [View GitHub repository](https://github.com/xkxi/secondcall)

- [Visit project website](https://team-30-app.thecosmoslabs.com/app/)

- [Watch demo video](https://www.youtube.com/watch?v=6eMjYFXXdVg)

- [项目截图](https://i.ytimg.com/vi/6eMjYFXXdVg/hqdefault.jpg)
