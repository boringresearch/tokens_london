# Evidence Atlas

原始页面：https://tokensand.com/p/evidence-atlas

所属活动：vastsf

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Evidence Atlas
André Antonelli14 days agoContributorJudging locked: Event build
Evidence Atlas
Evidence Atlas puts GPS-less dashcam footage on the map using only what the camera saw. Cosmos Reason reads the signs, OpenStreetMap supplies the coordinates, and a route-continuity check rejects impossible matches. Every pin shows its evidence.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Dashcam and fleet archives often have no GPS. VAST VSS finds clips by meaning, but its location filter only says "Toronto". Evidence Atlas answers where.
- Cosmos Reason re-watched all 1,080 indexed Toronto clips and read 3,658 street signs and business names.
- Names are matched in OpenStreetMap, never model-guessed coordinates. Two corner signs that meet give a verified intersection (~60 m), a unique venue gives a landmark (~150 m), and guide signs give an area.
- Drives are continuous, so a route check rejects matches the car couldn't have reached. For example, an "Art Gallery of Ontario" banner read 5 s after the ROM, 1.6 km away, is rejected. 86 clips are placed, 18 are rejected, and 831 are left off the map rather than guessed.
- Every pin opens an evidence chain: the video, what was read, the OpenStreetMap match, what agrees or conflicts, and where the index caption disagrees.
For whom: six built-in use cases, each with its own report written from saved evidence only by Llama 3.3 70B on W&B Inference: ad and retail site scouting, insurance and fleet incident location, roadwork audits, curb and delivery management, cycling and pedestrian safety, and newsroom footage verification. Places, not people: nothing identifies faces or licence plates.
Project links
GitHub repository
Project website
Demo video
Tools used
Tools used
VAST Data
CoreWeave
SpaceX
NVIDIA
Weights & Biases

## 公开链接

- [Hackathon](https://tokensand.com/vastsf)

- [Project gallery](https://tokensand.com/vastsf/projects)

- [André Antonelli](https://tokensand.com/u/andr-antonelli)

- [View GitHub repository](https://github.com/antonelli182/evidence-atlas)

- [Visit project website](http://video-lab-team-48.cosmos.vastdata.com/app/)

- [Watch demo video](https://github.com/antonelli182/evidence-atlas/blob/main/DEMO.md)

- [项目截图](https://opengraph.githubassets.com/1/antonelli182/evidence-atlas)

## 页面结构化补充资料

### Technical architecture

VAST VSS (search, ingest, VastDB, S3 clip storage) -> NVIDIA Cosmos Reason re-watches each clip and reads street signs and business names -> names matched in OpenStreetMap via Overpass (never model coordinates): two meeting corner signs = verified intersection (~60 m), unique venue = landmark (~150 m), guide signs = area -> route-continuity check rejects matches the car could not have reached -> Flask API + vanilla JS/Leaflet map on the team-48 Kubernetes namespace. Llama 3.3 70B on W&B Inference writes use-case reports from saved evidence only. Search falls back to keyword matching over the re-watched archive when Cosmos-Embed1 is unavailable.

### Setup instructions

See README.md: pip install -r requirements.txt; build_atlas.py builds the atlas from VSS + Cosmos Reason + OSM; deploy.sh deploys main.py/pipeline.py/index.html to Kubernetes (needs COSMOS_URL and VSS credentials from the environment).

### Lessons learned

Location needs evidence, not guesses: the model reads signs well but its coordinates are unreliable, so OSM supplies positions and the route check catches impossible matches. Leaving 831 clips unplaced is better than guessing. Shared GPU endpoints flap, so the app needs a graceful fallback.
