# My Day

原始页面：https://tokensand.com/p/my-day

所属活动：vastlondon

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
My Day
F Labout 4 hours agoContributorJudging locked: Event build
My Day
My Day is a dignity-first personal memory journal for older adults living alone or with early memory loss . It turns short video clips into a searchable timeline to answer daily reassurance questions with exact video proof , while giving users total control over what they share with family.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Watch demo videoProject gallery
Demo video
Watch demo video
Project description
My Day is a dignity-first personal episodic memory agent designed for older adults living independently or experiencing early memory changes. The application transforms short daily video clips into a searchable timeline, allowing users to ask natural language questions—such as "Has Sarah visited today?" or "Where are my keys?"—and receive calm, grounded answers backed by direct video clip proof. Built on a tech stack featuring VAST AI OS vector search, NVIDIA Cosmos video understanding, CoreWeave GPU compute, and Weights & Biases agent logic, the system strictly prevents hallucinated memories by safely abstaining whenever an event wasn't filmed. Crucially, all video logs remain 100% private until the user explicitly chooses to share specific clips with family carers, replacing intrusive 24/7 room surveillance with dignity, individual control, and peace of mind.
Project links
GitHub repository
Demo video
Tools used
Tools used
VAST Data
CoreWeave (Weights & Biases)
SpaceXAI (Cursor)
NVIDIA
cosmos
yolo

## 公开链接

- [Hackathon](https://tokensand.com/vastlondon)

- [Project gallery](https://tokensand.com/vastlondon/projects)

- [F L](https://tokensand.com/u/f-l)

- [View GitHub repository](https://github.com/prkshverma09/MyDay)

- [Watch demo video](https://drive.google.com/file/d/1iUt5Vm5HHno_0LuV2LAaVudNWVy6jbl5/view?usp=drive_link)

- [项目截图](https://opengraph.githubassets.com/1/prkshverma09/MyDay)

## 页面结构化补充资料

### Technical architecture

Video is cut into 10-second chunks. Each chunk is described by NVIDIA Cosmos Reason, with YOLO11 object detections (people, objects, positions) fused into a single text record per chunk. Extraction into memory: a Weights & Biases serverless LLM (Llama-3.3-70B-Instruct) reads each chunk's text and extracts structured core memories, filed into two stores: general memory (the routine record of the day) and key moments (visitors and conversations, appliances switched on or off, tracked objects like keys and glasses put down, front door events, anything unusual), with a derived last-seen store for tracked objects. Entries are embedded with NVIDIA Cosmos Embed1 and stored in VastDB (schema reminis

### Additional screenshots or links

https://docs.google.com/presentation/d/1cqZhUYgyfwJOmw_nbeTbinuCZhI873_R/edit?usp=sharing&ouid=113897071480899113174&rtpof=true&sd=true
