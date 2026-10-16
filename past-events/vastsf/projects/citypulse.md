# CityPulse

原始页面：https://tokensand.com/p/citypulse

所属活动：vastsf

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
CityPulse
Anonymous builder14 days agoJudging locked: Event build
CityPulse
CityPulse lets you ask a city a natural-language question and receive a grounded 30-second narrated video answer assembled from the most relevant moments in its indexed footage.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
CityPulse turns urban video archives into an interactive visual storytelling agent.
A user asks a question such as “How do pedestrians and vehicles interact at Toronto intersections?” CityPulse searches the indexed Toronto driving footage, surfaces the strongest evidence, selects six complementary shots, writes a grounded narration, and automatically edits them into a 30-second narrated film.
The interface makes the agent’s work visible: source routes illuminate as relevant moments are found, evidence clips appear during retrieval, selected shots are ordered into the final cut, and the resulting film answers the original question.
CityPulse builds directly on the VAST Video Search & Summary stack. VAST DataEngine stores and retrieves the indexed video evidence. NVIDIA Cosmos Embed powers semantic video retrieval, while Cosmos Reason provides scene understanding and descriptions. YOLO11 detections provide object-level evidence for vehicles, pedestrians, cyclists and other road users. Weights & Biases serverless inference on CoreWeave powers the higher-level AI director that selects shots and writes the narration.
The final response is not generated footage: every shot comes from the licensed source archive and remains grounded in retrieved evidence.
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

- [View GitHub repository](https://github.com/flaspa/citypulse)

- [Visit project website](https://team-37-app.thecosmoslabs.com/app/#film=8fc721166b78)

- [Watch demo video](https://youtu.be/7vD0IwavEwQ)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/5dcaf6d7-f4db-4100-98d1-cb4b26a5ca3d/3feafdac-f13b-418d-8538-c58087272dba.png)

## 页面结构化补充资料

### Technical architecture

CityPulse is a retrieval-to-video agent built on the VAST Video Search & Summary stack. 1. A user asks a natural-language question about Toronto. 2. VAST DataEngine searches the indexed urban footage using NVIDIA Cosmos Embed representations and Cosmos Reason scene descriptions. 3. Retrieved segments include timestamps, captions, source metadata, and YOLO11 object detections. 4. A higher-level AI Director, powered by Weights & Biases serverless inference on CoreWeave, selects six complementary evidence shots and writes a grounded narration. 5. Piper generates the voice-over. 6. FFmpeg assembles the selected source clips, narration, and timing into a 30-second MP4. 7. The CityPulse frontend v

### Setup instructions

The hosted demo requires no local setup. Open the deployed CityPulse app and enter a natural-language question about the Toronto footage. For development, the project lives in tools/toronto-director inside the VAST Builders Challenge environment. It uses the credentials and endpoints already provided through the workshop environment variables and the VAST Cursor skills. The application depends on the team's existing VSS index and does not require users to download or ingest external video.

### Lessons learned

The most important lesson was that the quality of a video agent depends heavily on what was captured during ingestion. Semantic search can only retrieve concepts that the video understanding pipeline described and embedded. We also found that latency can become part of the experience rather than something to hide. CityPulse exposes retrieval, evidence selection, object detections, shot selection, and narration as a visible directing process while the final film is being assembled. A second lesson was the value of grounding. Rather than generating synthetic imagery, CityPulse keeps every shot traceable to source footage and uses AI primarily to search, reason, select, narrate, and edit.
