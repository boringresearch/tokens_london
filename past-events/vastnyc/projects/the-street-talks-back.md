# The Street Talks Back

原始页面：https://tokensand.com/p/the-street-talks-back

所属活动：vastnyc

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
The Street Talks Back
Frank Yu7 days agoContributorJudging locked: Event build
The Street Talks Back
We take street camera images of vehicles and see how compatible they are as a dating pair (tinder for vehicles)
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Watch demo videoProject gallery
Demo video
Watch demo video
Project description
This is a dating app for vehicles. We take street camera footage, detct and track the vehicles in it and give each one profile built from it how it behaves. Compatibility is computed on the video not just narrated by a LLM. We score things on what the footage shows: speed and driving lanes, times of day etc. The LLM explains the score instead of inventing it so every claim traces back to a clip
Ingest: Street footage is loaded and indexed so it can be searched and streamed by timestamp
Track: YOLO detects and tracks vehicles frame to frame, producing a track history for each one (path, speed, dwell time, proximity to others).
Understand: Cosmos describes each vehicle’s behavior and its interactions with other vehicles (“yields to cyclists,” “idles at the curb”).
Profile: An LLM turns the track data and Cosmos descriptions into a bio, a nickname, and personality traits
Match: A scoring function compares track features for each pair of vehicles. Pairs that shared a clip or camera are candidates
Explain and chat: An LLM writes the compatibility breakdown and a “first date,” and vehicle personas chat with their matches and accept or reject based on their profiles
VAST  We read indexed data, stream the clips and persists complaints and tickets Nvidia - Cosmos reasons captions aree the evidence. YOLO waks the judge cosmos embed runs search and interview
Cursor The whole project was built using it
Weight Biases gpt-oss-20b judges the clip. Llama writes it.
Project links
GitHub repository
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

- [Frank Yu](https://tokensand.com/u/frank-yu)

- [View GitHub repository](https://github.com/sahilpardasani/street-talks-back)

- [Watch demo video](https://www.youtube.com/watch?v=Yj9kGJWgtws)

- [项目截图](https://i.ytimg.com/vi/Yj9kGJWgtws/hqdefault.jpg)
