# EqualEd

原始页面：https://tokensand.com/p/equaled

所属活动：vastsf

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
EqualEd
Alexander Skinderev14 days agoContributorJudging locked: Event build
EqualEd
EqualEd is a classroom video agent for neurodivergent students: it sees sensory overload coming for an autistic student and starts calming sound before the noise, rewinds what a student with ADHD missed, and alerts the teacher only when they need to step in.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Watch demo videoProject gallery
Demo video
Watch demo video
Project description
One laptop camera watches the class. On the laptop, YOLO11-pose, YOLOE and YAMNet track the student and spot loud things by name (a blender, a drill) before they make a sound, plus crowding, someone rushing in or someone staying too close. As risk rises, calming sound fades into the student's AirPods early and the teacher's phone gets an alert with the right IEP accommodation. Covering ears or rocking triggers an overload alert.
NVIDIA Cosmos3-Reason on CoreWeave GPUs reads the last few seconds of video and says what is about to get overwhelming. Canary-1B transcribes the lecture, so a student with ADHD can ask "what did I miss?" about the minutes they looked away; Llama 3.3 70B on W&B Inference answers. Weave traces every model call.
On VAST, we scored all 2,352 clips in our archive for sensory load from the Cosmos captions and YOLO11 counts (771 high, 566 calm) and built a sensory map: the SF street cameras are the most overwhelming (76% high load), the neighborhood camera the calmest (97% calm). Our VM app adds a Cosmos risk timeline over archive video, VAST search with clip streaming, re-ingest with our sensory prompt, and W&B summaries of the calmest places and times.
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

- [Hackathon](https://tokensand.com/vastsf)

- [Project gallery](https://tokensand.com/vastsf/projects)

- [Alexander Skinderev](https://tokensand.com/u/alexander-skinderev)

- [View GitHub repository](https://github.com/SashaSkind/EqualEd)

- [Watch demo video](https://youtu.be/6Duq39aC22Q)

- [项目截图](https://i.ytimg.com/vi/6Duq39aC22Q/hqdefault.jpg)
