# Visual Actions

原始页面：https://tokensand.com/p/visual-actions

所属活动：vastnyc

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Visual Actions
jirubin1597 days agoContributorJudging locked: Event build
Visual Actions
It's a menu bar app that controls the desktop with gestures, using modes the way Vim does. You raise an open palm to "arm" it, then make a command gesture:
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Watch demo videoProject gallery
Demo video
Watch demo video
Project description
1. Perception: MediaPipe Hand Landmarker reads 21 hand landmarks from each OpenCV webcam frame. We turn them into a 65-number feature vector. 2. Classification: A scikit-learn logistic regression, trained on public HaGRIDv2 landmarks plus synthetic and calibration data, labels each frame. A hold timer weighted by confidence keeps random hand movement from firing commands. 3. Action: PyObjC calls macOS directly (Quartz events, the Accessibility API, overlays). It sends keystrokes, moves windows with its own snapping, and draws on-screen feedback. 4. Self-improvement loop (the hackathon part): Every gesture event is logged. The intent pipeline goes segments → video clips → Cosmos Reason → JEV check → tagger → review → export: - Cosmos Reason (the shared NIM, cosmos3-nano-reasoner) watches each clip and judges what the user meant to do: a real command, a misfire, or a missed gesture. - A JEV pass (over OpenRouter) cross-checks Cosmos's verdict. - An LLM tagger with escalation to a stronger model settles disagreements and writes corrected labels. - The corrected labels go back into retraining.
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

- [jirubin159](https://tokensand.com/u/jirubin159)

- [View GitHub repository](https://github.com/Sean-Shmulevich/visual-actions-py)

- [Watch demo video](https://drive.google.com/drive/folders/1QpFn7WUFdx4jvCCexYyh21Bcf1epylca?usp=drive_link)

- [项目截图](https://opengraph.githubassets.com/1/Sean-Shmulevich/visual-actions-py)
