# Haystack

原始页面：https://tokensand.com/p/haystack

所属活动：vastlondon

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Haystack
Awab Ibrahimabout 5 hours agoContributorJudging locked: Event build
Haystack
Haystack is a real-time video agent that hunts through hours of dashcam footage for the rare, dangerous moments self-driving cars fail on, lets a human confirm them, and exports them as a ready-to-train dataset for autonomous-vehicle teams.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Self-driving cars don't crash on the boring 99% of driving. They crash on the weird 1%: a pedestrian hidden by a turning bus, a horse-drawn carriage, a school bus with its stop sign out. Those moments are buried in hours of normal footage and finding them by hand is slow and expensive. Haystack finds them for you.
How it works:
1. Understand: dashcam video is stored on VAST Data (S3 + VastDB). NVIDIA's VSS Blueprint uses Cosmos-Reason2 to describe every 5-second clip and Cosmos-Embed1 to make it searchable. YOLO11 boxes people and vehicles and measures motion.
2. Search: type a plain-English question ("cyclist running a red light") or switch on the Live agent, which scans camera by camera, invents new hunts and flags edge cases as it finds them.
3. Judge: an LLM on Weights & Biases Inference scores each clip for rarity, danger and training value and explains why. Every call is traced in W&B Weave.
4. Human check: one key press (Y/N) confirms or rejects each find. This measures the judge's accuracy, and rejected clips never reach the dataset.
5. Act: export a labelled dataset (clips, boxes, COCO labels, train/val split) logged as a versioned W&B artifact.
Built in Cursor, running on CoreWeave GPUs.
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

- [Hackathon](https://tokensand.com/vastlondon)

- [Project gallery](https://tokensand.com/vastlondon/projects)

- [Awab Ibrahim](https://tokensand.com/u/awab-ibrahim)

- [View GitHub repository](https://github.com/Baladog05/VideoHack)

- [Visit project website](https://team-39-app.thecosmoslabs.com/app/)

- [Watch demo video](https://drive.google.com/file/d/1uQ_YRtFwZDw2LEAQBwqLzokvoZecBu1B/view)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/c5ae53b0-1d5f-4364-baf7-66bea1dd4874/4d25f477-d00f-4855-af8a-e78246d81bcd.png)
