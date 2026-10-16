# PharOS

原始页面：https://tokensand.com/p/pharos

所属活动：vastnyc

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
PharOS
Viktor Radev7 days agoContributorJudging locked: Event build
PharOS
PharOS turns NYC’s traffic cameras into an early-warning system for city safety teams, spotting near misses and risky behavior at intersections so dangerous corners can be fixed before the next crash.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
NYC DOT’s traffic cameras watch the city’s most dangerous corners but record nothing, so every near miss is lost. PharOS is a 3D map of Manhattan with a heatmap of injury crashes from the last 12 months of NYC Open Data, and every node is a real DOT camera. Open an intersection to see its camera image, crash history, reported causes, crashes by hour, and next steps. For continuous video, PharOS monitors live 511NY feeds and returns a verdict on each 8-second clip in about 14 seconds. Plain-English search finds matching moments in recorded footage.
How we used the stack:
VAST AI OS: The workshop’s VAST pipeline had already indexed recorded New York footage into VastDB. PharOS queries it with hybrid semantic search and streams matching clips for seekable playback.
NVIDIA: On each live clip, YOLO11 boxes every car, person and bike across 32 frames, while Cosmos Reason reads the same video and describes what happened. Neither can claim motion from a single frame.
CoreWeave: Its GPUs serve the NVIDIA models, which return results in under 3 seconds.
Weights & Biases: W&B Inference runs Llama 3.3 70B. It turns each clip’s findings into a structured verdict, turns questions into search plans, and writes next steps linked to official guidance.
Next: live video at every DOT camera, and a citywide ranking of intersections by near misses for planners.
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

- [Viktor Radev](https://tokensand.com/u/viktor-radev)

- [View GitHub repository](https://github.com/Divyesh-Thirukonda/pharos)

- [Visit project website](https://team-12-app.thecosmoslabs.com/app/)

- [Watch demo video](https://drive.google.com/file/d/14WIy1vDYRlM_E19bL_HJT2OjzpmpMbDv/view?usp=sharing)

- [项目截图](https://opengraph.githubassets.com/1/Divyesh-Thirukonda/pharos)

## 页面结构化补充资料

### Technical architecture

Every thirty seconds, our backend captures eight seconds of live video at four frames a second. NVIDIA runs two models on that exact clip in parallel. YOLO11 boxes every car, person and bike across all 32 frames, and Cosmos Reason watches the clip and describes what actually happened. Both are served on CoreWeave GPUs and come back in under three seconds. Weights & Biases Inference runs Llama 3.3 70B, which checks those findings against our evidence rules and writes a structured verdict. It also turns plain-English questions into search plans. Those searches run on VAST's video search, which finds and streams matching clips from recorded New York footage.

### Lessons learned

The hardest lesson was that an AI model will confidently describe a near miss it can’t actually see. Early on, Cosmos labeled a single frame a conflict, so we added a rule that any motion claim needs evidence across several frames. Data access shaped the product more than models did. NYC DOT’s cameras only give still images, so we had to find continuous 511NY video feeds. A packaged FFmpeg also crashed on those streams until we switched decoders. We learned to keep three things separate: a search result is a candidate, a crash count is history, and only a verdict on real footage is an observation. Finally, splitting into parallel builds and merging later cost time. Agreeing on one shared con
