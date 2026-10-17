# MirrorVerse gives IRL streamers situational awareness: AI agents read live street cameras for crowds, traffic and chaos around them, then a

原始页面：https://tokensand.com/p/mirrorverse

所属活动：vastlondon

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
MirrorVerse gives IRL streamers situational awareness: AI agents read live street cameras for crowds, traffic and chaos around them, then a
Min Thant Kyawabout 5 hours agoContributorJudging locked: Event build
MirrorVerse gives IRL streamers situational awareness: AI agents read live street cameras for crowds, traffic and chaos around them, then a
Mirrorverse gives IRL streamers situational awareness: AI agents read live street cameras for crowds, traffic and chaos around them, then a real-time 3D twin of the city map tests any move before they make it. Know what's around you. Rehearse the future before it happens.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Live map: Streamers see what’s around them as it happens, including traffic, crowds, accidents and closures.
Better calls on the move: They know what’s ahead before they turn the corner, so they can choose where to go and what to avoid.
Fewer surprises: Streamers can spot trouble early, from unsafe areas to crowds forming to stream snipers closing in.
A digital twin of the city: The Mirrorverse is populated with real cars and people from live data. Anything there is the same as IRL, but we can do anything in Mirrorverse with no consequences. For example, streamers can add 50 people outside a shop, block a road or change the route, then see how it’s likely to play out. THEN they make the decision IRL.
Beyond streaming: The same tech works for film shoots, live events, red carpets and celebrity appearances, anywhere crowds and timing matter.
Sky is the limit :)
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
Tokens&

## 公开链接

- [Hackathon](https://tokensand.com/vastlondon)

- [Project gallery](https://tokensand.com/vastlondon/projects)

- [Min Thant Kyaw](https://tokensand.com/u/min-thant-kyaw)

- [View GitHub repository](https://github.com/chocoliticekreem/mirrorverse)

- [Visit project website](https://emfol.vercel.app/)

- [Watch demo video](https://www.loom.com/share/6c4eee8fee63499f905fe8e52996f642)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/e9d80489-c55d-4fbc-a30d-4c11ee31180b/79e5b868-8880-4a96-8ea3-00795cdad1e8.jpg)

## 页面结构化补充资料

### Technical architecture

Mirrorverse runs on VAST's CAMP stack: - C (Coding agent): Cursor on the VAST lab VM over Remote-SSH, using VAST's official skills to deploy and re-ingest. Shared rules for all our coding agents live in AGENTS.md, a Cursor rule and a vast-camp skill. - A (Agent runtime): Our Python agent runs in our team's VAST Kubernetes namespace at /app. - On each POST /app/assess it searches VSS for streamer-safety moments and pulls detections through the VSS tools. - An LLM on W&B then returns a verdict: calm, busy or danger, plus advice and evidence clips. - Each verdict is saved to VastDB. - M (Model services): These run on CoreWeave GPUs. - NVIDIA Cosmos3-Reason (reasoning over clips), Cosmos Embed1

### Setup instructions

- You need Node 20+, and uv (Python 3.12) for the optional services. - Get the code: git clone https://github.com/chocoliticekreem/classroom-47 && cd classroom-47 npm install - Optional: copy apps/stream/.env.example to apps/stream/.env.local and add your W&B keys. Without them the chat uses local templates and there are no Weave traces. - Run it: - npm run dev:stream opens the app at http://localhost:3047. - npm run yolo adds live crowd counts. - npm run predict adds the forecast service. - npm run tunnel gives an HTTPS link for streaming from a phone. - The agent is already deployed on VAST. Check it with curl https://video-lab-team-47.cosmos.vastdata.com/app/health. - We deployed it from

### Lessons learned

- The ingest prompt matters most. The default captions never noted "someone filming or following the camera holder", so search missed that case (7/8 hits). Re-ingesting with our own prompt improved results. Next time we'd write the prompt before ingesting. - Read the official guide first. VAST's deploy template uses different credential names from our agent's code. If they don't match, the agent starts with no credentials. - Cache everything for the demo. Cold GPUs, TfL rate limits and venue Wi-Fi all failed at some point, so the app precomputes and caches. - Public cameras are low-res. TfL JamCams are 352×288 and loop one 10-second clip. We added sharp "virtual live cams" with YOLO tracks c
