# Witness desk

原始页面：https://tokensand.com/p/witness-desk

所属活动：vastnyc

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Witness desk
freeslugs7 days agoContributorJudging locked: Event build
Witness desk
Witness desk searches every camera in New York or San Francisco for one vehicle by color, body type, and time, then lets you mark the clip and keep a still.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Witness desk is for someone who saw a vehicle and needs the footage. They choose the city, an optional time, the body type, and the color. The desk searches the indexed archive and lays the closest clips out as a network. The lit node plays in place. Yes keeps a still with the case. No clears that clip and moves to the next.
The search uses the stored clip descriptions from the video stack. The desk shows those captions and does not invent events they do not contain. Plates and make or model are not in this index, so the form does not ask for them. Stolen and hit-and-run are marks a person sets after watching a clip. They are not part of the query.
CoreWeave hosts the video models inside that search stack. It shows the captions those models already wrote. Cases stay in the browser, and the live site needs no login.
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

- [freeslugs](https://tokensand.com/u/freeslugs)

- [View GitHub repository](https://github.com/freeslugs/witness-desk)

- [Visit project website](https://witness-desk.vercel.app)

- [Watch demo video](https://youtu.be/0zOSVs855MU)

- [项目截图](https://i.ytimg.com/vi/0zOSVs855MU/hqdefault.jpg)

## 页面结构化补充资料

### Technical architecture

The Next.js app on Vercel calls the VAST video search API from server routes, so the API token never reaches the browser. Search sends a color and vehicle query, a city metadata filter, and either the whole archive or a time window in that city's timezone. Playback is proxied through the app. The interface turns the returned clips into a node network. Cases and stills stay in the browser.

### Setup instructions

The repository is public at https://github.com/freeslugs/witness-desk and the live site is https://witness-desk.vercel.app. To run it locally, set VSS_BACKEND, VSS_USERNAME, and VSS_PASSWORD, then run npm install and npm run dev. Do not commit those credentials.

### Lessons learned

A specific vehicle question fits this footage better than a free-text hunt. Color, body type, city, and an optional time window are what the captions can answer. A tight hour can return no clips even when the rest of that day has matches. Showing the stored caption, instead of asking another model to retell the clip, keeps the person looking at the actual footage.
