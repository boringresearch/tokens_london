# Dashi

原始页面：https://tokensand.com/p/dashi

所属活动：vastsf

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Dashi
vaishnav.ajai.th14 days agoContributorJudging locked: Event build
Dashi
A video agent for rideshare drivers: coaching from their dashcam clips, evidence for unfair ratings.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Riders rate from the back seat and can't see why a driver stopped; telematics knows the car braked, not that a pedestrian stepped out. Dashi reviews each trip's dashcam footage and finds the moments that matter. Proactive side: kudos cards and lesson cards built from the driver's own clips, posted without being asked. Ask side: the driver says "Help me improve my rating" and Dashi finds the 3-star trip, plays the clip where they yielded to a pedestrian, and offers to send the evidence for a rating review. Footage questions in plain English ("show me pedestrians crossing in front of me") run a live VAST hybrid search. For a coachable moment (turning while a pedestrian was still crossing) Dashi shows a better way from a fixed playbook and writes an Ideal replay prompt for a Cosmos Predict/Transfer-style model to render the same scene driven safely. Every verdict quotes the camera caption word for word. Eval on 12 labelled clips: verdict 12/12, scenario 10/12, 0 false alarms; groundedness of summaries 3/7 (our weak spot). Footage is the pie_cam-3 Toronto research dashcam; ratings, routes and driver are simulated. No telemetry, so no speed or braking claims.
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

- [vaishnav.ajai.th](https://tokensand.com/u/vaishnav-ajai-th)

- [View GitHub repository](https://github.com/vaishnav-16/dashi)

- [Visit project website](http://video-lab-team-7.cosmos.vastdata.com/app/)

- [Watch demo video](https://youtu.be/zkmvhn2HwhY)

- [项目截图](https://i.ytimg.com/vi/zkmvhn2HwhY/hqdefault.jpg)

## 页面结构化补充资料

### Technical architecture

Dashcam video (pie_cam-3) runs through the pre-built VAST DataEngine pipeline: YOLO11 detections, NVIDIA Cosmos Reason captions (with our custom ingest prompt so captions describe what the driver's own car does), Cosmos Embed vectors, stored in VastDB. Dashi: discover.py searches each playbook scenario with VAST hybrid search and prunes the playbook. app/core.py runs a 5-stage review per trip: gather segments, classify captions with an LLM on W&B Inference (DeepSeek V4 Flash), validate (evidence quote must be an exact substring of the caption, confidence >= 0.6), merge segments into moments, coach from the playbook, write an Ideal replay prompt, score the trip. app/analyze.py writes moments.

### Setup instructions

python3 -m venv .venv && .venv/bin/pip install fastapi uvicorn requests openai weave. Set INGRESS_URL, USERNAME, PASSWORD (VSS), WANDB_API_KEY, WANDB_TEAM, WANDB_PROJECT. cd app; ../.venv/bin/python ../discover.py; ../.venv/bin/python analyze.py --chunks ../candidates.txt --out ../work/candidates_review.json; ../.venv/bin/python analyze.py --assign ../work/candidates_review.json --trips trips.json; ../.venv/bin/python analyze.py --trips trips.json --out moments.json; ../.venv/bin/python ../eval/run_eval.py. Run locally: DASHI_LOCAL=1 PORT=8090 ../.venv/bin/python main.py. Deploy: deploy/deploy.sh. Full steps in README.md.

### Lessons learned

The ingest prompt decides what you can find. Default captions describe the scene well but rarely say what the camera car itself does, so in 22 scanned chunks only one coachable moment existed, and it came from a chunk re-ingested with our custom prompt (captions saying the car yields went from 0/6 to 3/6 segments). Similarity scores alone (0.3-0.4) can't tell good hits from bad; checking captions with negated sentences removed did. Forcing the LLM's evidence quote to be an exact substring of the caption made the output trustworthy, and the eval showed the one-line summaries are still the weak spot (3/7 fully grounded). POST /search rejects llm_top_n 0 with HTTP 422, and search latency varied

### Additional screenshots or links

https://raw.githubusercontent.com/vaishnav-16/dashi/main/docs/dashi-demo.mp4; https://wandb.ai/vastdata/team-7/weave
