# Occlusive Logic

原始页面：https://tokensand.com/p/occlusive-logic

所属活动：vastnyc

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Occlusive Logic
Tinkamanyire “Kama” Rwezahura7 days agoContributorJudging locked: Event build
Occlusive Logic
Occlusive Logic transforms video object detections into user-programmable spatial rules, enabling anyone to monitor defined areas and generate evidence-backed alerts without retraining AI models.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Watch demo videoProject gallery
Demo video
Watch demo video
Project description
Traditional computer vision systems can identify objects but understanding when their presence is relevant often requires some custom programming for each application. Occlusive Logic bridges that gap by allowing users to turn existing video detections into configurable, actionable rules. Users select a video source, draw a polygonal zone directly over the footage, choose the object classes, and configure confitions such as entering an area, remaining there for a specified duration, or being absent. A custom Python rules engine evaluates the object positions, confidence thresholds, the tracking informations and temporal conditions to determine when a rule has been satisfied.
When triggered, the system creates a time stamped incident ticket with visual evidence. Users can inspect, revisit, and resolve incidents through a web dashboard.
The application integrates with VAST's video infrastructure and uses YOLO detection metadata from VAST provided footage. It is built with Python, FastAPI, Javascript, SQLite, and a custom geometry and temporal state engine. Additional simulations demonstrate potential applications in accessibility focused occlusion monitoring and in proper waste management.
Computer Engineering foundation: Occlusive logic treats camera detections as virtual sensor signals and applies programmable spatial and sequential logic to produce an event. This lays a foundation for future boolean rule composition and edge hardware deployment.
Project links
GitHub repository
Demo video
Tools used
Tools used
VAST Data
SpaceXAI (Cursor)
NVIDIA

## 公开链接

- [Hackathon](https://tokensand.com/vastnyc)

- [Project gallery](https://tokensand.com/vastnyc/projects)

- [Tinkamanyire “Kama” Rwezahura](https://tokensand.com/u/tinkamanyire-kama-rwezahura)

- [View GitHub repository](https://github.com/rwezzy/ZoneLogic-Tripwire)

- [Watch demo video](https://drive.google.com/file/d/1dYFiHLgiRSEsVjfKq8R5c1eSTFDQ_gkH/view?usp=sharing)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/05facd52-7683-4007-9b26-680b6df289cc/3e94464e-c152-4055-b7a1-4f68af53dff6.png)

## 页面结构化补充资料

### Technical architecture

Occlusive Logic uses a modular video-processing architecture: 1. Perception: YOLO object detections and bounding boxes retrieved alongside VAST-hosted video clips. 2. Spatial processing: User-defined polygonal zones with configurable object-position matching and confidence thresholds. 3. Temporal rule engine: A Python stateful evaluator supporting entry detection, dwell thresholds, absence conditions, object tracking, and event cooldowns. 4. Incident management: FastAPI and SQLite store timestamped incidents, visual evidence, and resolution status. 5. Interface: JavaScript-based dashboard for video playback, zone drawing, rule configuration, and incident review. The perception layer is separ

### Setup instructions

Source code: https://github.com/rwezzy/ZoneLogic-Tripwire Clone the repository, install the Python dependencies listed in requirements.txt, and run the application using the instructions in README.md. The application includes built-in simulation scenarios that work without external credentials. For VAST footage, configure the required VAST service credentials in the environment and use the VAST video catalog within the application. The VAST integration depends on access to the event infrastructure.

### Lessons learned

One of the biggest challenges was translating object detections into meaningful events. Detecting a person or vehicle is not enough; the system must determine where an object is, how long it remains there, and whether a rule has actually been violated. I learned the importance of separating perception from decision-making, handling imperfect tracking data, and testing spatial and temporal logic against real video detections rather than relying exclusively on simulations. The project also revealed a promising connection to digital design: object detections can function as virtual sensor signals, opening the possibility of combining them through Boolean logic and sequential state machines. I d
