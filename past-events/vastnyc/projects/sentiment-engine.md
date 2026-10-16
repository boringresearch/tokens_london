# Sentiment Engine

原始页面：https://tokensand.com/p/sentiment-engine

所属活动：vastnyc

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Sentiment Engine
Emily Yuan7 days agoContributorJudging locked: Event build
Sentiment Engine
A real-time video agent that pairs on-screen game events with players' facial reactions and makes hours of gameplay searchable in plain language.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Watch demo videoProject gallery
Demo video
Watch demo video
Project description
Sentiment Engine turns gaming reaction videos into searchable, time-indexed intelligence by pairing what happens on screen with how the player reacts.
For any gameplay video, SE finds the moments that matter — the in-game event (the stimulus) and the player's facial expression at that instant (the response) — then lets you search hours of footage in plain language and auto-writes a studio insight brief when something lands.
How it works:
Ingest — yt-dlp pulls the video stream; ffmpeg samples frames.
Game understanding — NVIDIA model captions the on-screen event per window.
Reaction lane — SE locates the creator's webcam corner, crops the player's face at each event, and the VLM reads the facial expression + intensity.
Fusion — events × reaction intensity × cross-video synchrony rank the "notable moments."
Action — NVIDIA model writes a 2-sentence design/marketing brief for the top moment.
Search — plain-language queries return the moment + reaction.
Project links
GitHub repository
Demo video
Tools used
Tools used
VAST Data
CoreWeave (Weights & Biases)
NVIDIA

## 公开链接

- [Hackathon](https://tokensand.com/vastnyc)

- [Project gallery](https://tokensand.com/vastnyc/projects)

- [Emily Yuan](https://tokensand.com/u/emily-yuan)

- [View GitHub repository](https://github.com/createcontinuem/vastai-hackathon-emilyyuan)

- [项目截图](https://opengraph.githubassets.com/1/createcontinuem/vastai-hackathon-emilyyuan)
