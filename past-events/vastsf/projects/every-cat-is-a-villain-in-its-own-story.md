# Every cat is a villain in its own story

原始页面：https://tokensand.com/p/every-cat-is-a-villain-in-its-own-story

所属活动：vastsf

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Every cat is a villain in its own story
Robert Nowell14 days agoContributorJudging locked: Event build
Every cat is a villain in its own story
A robot mouse that runs away from cats, loves hot dogs, and can answer questions about its own footage
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
A small robot mouse with a camera which is rightfully terrified of cats. It patrols the room. When NVIDIA Cosmos Reason (cosmos3-nano-reasoner, served on CoreWeave GPUs) sees a cat in the live feed, the car panics: red lights, a 540 degree spin and a sprint away, with a panic clip on the dashboard. When Cosmos sees a hot dog, the car flashes green, and approaches.
Every 5-second clip the robot records goes into the event's VAST AI OS video pipeline, where DataEngine runs YOLO11, Cosmos captions and Cosmos-Embed1 into VastDB (756 clips so far). So the robot can answer plain-language questions about its own life: "when did the cat get closest, and did I get away?" comes back with an answer and the matching clips.
A Llama 3.3 70B planner on WandB Inference narrates what the robot is doing. Reflexes (steering, a 25 cm wall check, a disconnect watchdog) run on the laptop and never wait on the cloud; YOLO11 is the offline fallback detector.
For anyone with a pet camera, a security feed or a robot: video that can be searched and acted on instead of sitting unwatched.
Project links
GitHub repository
Project website
Demo video
Tools used
Tools used
VAST Data
CoreWeave (Weights & Biases)
NVIDIA
SpaceXAI (Cursor)

## 公开链接

- [Hackathon](https://tokensand.com/vastsf)

- [Project gallery](https://tokensand.com/vastsf/projects)

- [Robert Nowell](https://tokensand.com/u/robert-nowell)

- [View GitHub repository](https://github.com/robertnowell/every-cat-is-the-villain)

- [Visit project website](https://schemes-science-presentation-morris.trycloudflare.com/)

- [Watch demo video](https://www.loom.com/share/a7c97be0f1694a5db438275071cc5074)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/a2bfe859-22a1-4f12-b7b1-b0ad4c301545/778de4e5-c90e-4802-b5ef-a2dcf538580c.png)

## 页面结构化补充资料

### Technical architecture

Camera (ESP32 MJPEG) -> laptop. Fast loop on the laptop: frame -> reflex policy -> drive commands over the Elegoo's 9600-baud link (change-only + 10 Hz keepalive), ultrasonic wall check, watchdog stops the car on stale video or lost link. Every ~3 s: frame -> NVIDIA Cosmos Reason (cosmos3-nano-reasoner on the event's CoreWeave GPU endpoint) -> JSON verdict: cat visible/side, open floor, boxed in, hot dog. Cosmos alone decides the panic; YOLO11 only when offline. Planner: Llama 3.3 70B on W&B Inference turns recent events + verdict into a narrated mode. Memory: recorder cuts 5 s clips -> relay on the event VM uploads to the VAST video pipeline (/api/v1/videos/upload with a cat-and-escape prom

### Setup instructions

Hardware: Elegoo Smart Robot Car V4 with camera, a MacBook, a plush cat. python3 -m venv .venv && .venv/bin/pip install ultralytics opencv-python numpy torch transformers pillow openai requests fastapi uvicorn weave Simulator, no car: ./demo.sh then open http://localhost:8000 and click Start. Real car: join the car's ELEGOO Wi-Fi, run preflight.py (9-step first-hookup check), then ./run_car.sh. Event stack: COSMOS_BASE / COSMOS_MODEL from the team config, WANDB_API_KEY, and vm_relay.py running on the event VM for VAST. Tests: .venv/bin/python -m pytest -q tests

### Lessons learned

Prompt wording decides the vision model's answer. Telling Cosmos the robot "must run away from a cat" made it say "cornered, cat approaching" on 15 of 15 frames, 11 with no cat. A neutral prompt that describes first, then answers, scored 10/12 on cat and 10/11 on cornered against hand-labelled frames. Let the big model confirm before acting: YOLO alone gave about 60 false panics on the real car; with Cosmos confirming, one real panic was confirmed and a false alarm rejected. A 9600-baud serial link is about 960 bytes a second, so the car only gets drive commands when they change, plus a keepalive. Keep the cloud out of the reflex loop: seconds of model latency are fine for judgement and memo
