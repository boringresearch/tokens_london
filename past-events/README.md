# 往期活动完整公开资料归档

源码下载：[仓库索引](repos/README.md)（已下载 74 个；12 个公开访问失败，详见索引）。

抓取日期：2026-10-16。来源：tokensand.com 官方活动页面和公开项目详情。

本归档包含活动说明、两场完整项目列表、每项详情正文、页面结构化技术/运行/经验说明，以及代码仓库和演示链接。项目内容为作者自述，未复现，也不是获奖名单。

网页保存为 HTML，便于核对原文；离线阅读请优先使用 Markdown，原始动态网页不保证离线交互正常。视频和图片未批量下载，链接已保留；源码下载结果见上方仓库索引。


## 从 GitHub 下载资料与全部可用源码

本仓库把 74 个已下载的项目源码保存为 Git 子模块，并固定到 `repos/manifest.json` 记录的 commit。活动原文、项目详情和索引直接保存在本仓库中。

```bash
git clone --recurse-submodules https://github.com/boringresearch/tokens_london.git
```

如果已经普通克隆：

```bash
git submodule update --init --recursive
```

子模块未来能否下载取决于原作者仓库是否继续公开。12 个公开访问失败的项目仅保留页面资料和失败记录。Git LFS 大文件需要另行安装 Git LFS 并拉取。

## 抓取结果

共 86 条参赛项目记录，成功 86，失败 0。详见 [manifest.json](manifest.json)。


## 旧金山 · 2026-10-02

共 45 项。[活动原文](vastsf/event.txt) · [完整列表数据](vastsf/project-list.json)

| 项目 | 简介 |
| --- | --- |
| [Aloha Circle](vastsf/projects/aloha-circle.md) | Aloha Circle turns arriving on Maui into meeting Maui — travelers scan a QR at baggage claim, share a playful aloha ritual with an AR guide, and get matched with a real local to enjoy a donated island experience together, all while supporting Maui causes. |
| [Vastly Unspoken](vastsf/projects/vastly-unspoken.md) | Yield or proceed use Cosmos reason to label warehouse footage indexed on Vast to train a tiny CPU model |
| [Property Studio](vastsf/projects/property-studio.md) | Property Studio turns real estate listings into attention-grabbing video scripts backed by photo analysis, property research, and transparent financial models. |
| [SideWalkWatcher](vastsf/projects/sidewalkwatcher.md) | This is a project that uses real time video to detect obstacles on sideawalks for disabled people. Generally, systems that do this track permanent obstacles, but this is for temporary ones. |
| [Group 20 (ViZ Agent)](vastsf/projects/group-20-viz-agent.md) | ViZ Agent finds pedestrian–vehicle conflicts in street and dashcam video, double-checks each one with three AI checks, and turns the verified ones into ranked hotspots and a drafted work order for city traffic engineers. |
| [Praxis - Find my Car](vastsf/projects/praxis-find-my-car.md) | Praxis — Find my Car is a video agent for people who lose a car in dense street parking or residential blocks. Instead of scrubbing hours of camera footage, you ask in natural language. |
| [OriginX](vastsf/projects/originx.md) | OriginX lets site safety leads write safety rules in plain English and watches the video archive for them, raising scored incidents with written reports. |
| [Evidence Atlas](vastsf/projects/evidence-atlas.md) | Evidence Atlas puts GPS-less dashcam footage on the map using only what the camera saw. Cosmos Reason reads the signs, OpenStreetMap supplies the coordinates, and a route-continuity check rejects impossible matches. Every pin shows its evidence. |
| [stayin-alive-cpr](vastsf/projects/stayin-alive-cpr.md) | We changed our project to a crosswalk block detector that speak out the warning to driver who stopped on crosswalk. |
| [Grabbit Mining Co.](vastsf/projects/grabbit-mining-co.md) | Describe a dangerous moment in one sentence; Grabbit digs through pre-indexed warehouse and road footage and hands you a verified, exportable test set of edge cases for robotics/AV policy evaluation. AI proposes, a human decides. |
| [Near-Miss Board](vastsf/projects/near-miss-board.md) | Near-Miss Board lets traffic safety teams search hours of multi-camera highway footage in plain English to find vehicles in near-miss close calls. |
| [Harvest](vastsf/projects/harvest.md) | turns a plain language request into a clean versioned training dataset |
| [Warehouse Safety Monitor](vastsf/projects/warehouse-safety-monitor.md) | Warehouse Safety Monitor watches warehouse camera footage and gives shift leads a ranked queue of near misses, blocked aisles,   crowding and unsafe behavior, with measured distances, hotspot heatmaps and an end-of-shift report. |
| [StreetStyle Scout](vastsf/projects/streetstyle-scout.md) | StreetStyle Scout searches street footage for visible clothing and colors, then shows matching frames and video clips so you can verify the results. |
| [Perjury](vastsf/projects/perjury.md) | Perjury is a fact-checker for traffic video: you say or type a claim about the footage, and it splits the sentence into atomic claims, checks each one, and rules each SUPPORTED, CONTRADICTED, or "the pixels can't tell" with the evidence shown. |
| [Scribner](vastsf/projects/scribner.md) | Integrating Andon with Vision Training to Develop Safe Workflows |
| [VASTCAM](vastsf/projects/vastcam.md) | VAST CAM uses VAST AI OS to build targeted video datasets for training camera-specific models that predict warehouse collisions before impact. |
| [traffic-police](vastsf/projects/traffic-police.md) | A reviewer searches indexed footage in plain language and gets ranked evidence cards linked to the source interval. |
| [WORLDSTATE](vastsf/projects/worldstate.md) | WORLDSTATE learns how physical processes should unfold from repeated video, detects when reality deviates, explains failures with NVIDIA Cosmos, and remembers them so future incidents are recognized instantly. Built for robotics, manufacturing, and warehouse operations. |
| [momentOS](vastsf/projects/momentos.md) | MomentOS turns dashcam history into an explainable driving risk score, using video evidence to identify near-misses, attribute cause, and help insurers reward safer drivers. |
| [Understudy](vastsf/projects/understudy.md) | Understudy turns video nobody watches into a live coach. It learns a task from expert recordings, then watches a new person on camera, corrects mistakes out loud with the expert clip for that step, and scores the attempt. |
| [Warehouse Sentinel](vastsf/projects/warehouse-sentinel.md) | Eyes on the Floor is a video agent that watches a warehouse's existing cameras, flags OSHA hazards like blocked exits and people in forklift lanes the moment they appear, and alerts the floor lead in seconds, so hazards get fixed before an injury, a complaint or an inspection. |
| [CityPulse](vastsf/projects/citypulse.md) | CityPulse lets you ask a city a natural-language question and receive a grounded 30-second narrated video answer assembled from the most relevant moments in its indexed footage. |
| [EqualEd](vastsf/projects/equaled.md) | EqualEd is a classroom video agent for neurodivergent students: it sees sensory overload coming for an autistic student and starts calming sound before the noise, rewinds what a student with ADHD missed, and alerts the teacher only when they need to step in. |
| [Dashi](vastsf/projects/dashi.md) | A video agent for rideshare drivers: coaching from their dashcam clips, evidence for unfair ratings. |
| [FreezeFrame](vastsf/projects/freezeframe.md) | Video aided gaussian splat style 3D reconstruction of any incident from any video for insurance claims |
| [HOP24](vastsf/projects/hop24.md) | Hop24 is a game where you guide a chicken across real highway footage, avoiding vehicles detected by AI. |
| [Second Wind](vastsf/projects/second-wind.md) | Give your legacy app a second life — add an agent, not a rewrite. It learns an ERP workflow from one screen recording, then creates real invoices in the live   app using only what it can see on screen, and hands the keyboard back whenever it is unsure. |
| [LongTail](vastsf/projects/longtail-1.md) | LongTail finds the rare, risky moments hidden in hours of unwatched traffic and warehouse video, double-checks each with an AI, and shows what the archive can't see, for self-driving and robotics teams that need edge cases to test on. |
| [Raccoon](vastsf/projects/raccoon.md) | Video Scrubbing Tool |
| [UnitProof](vastsf/projects/unitproof.md) | An AI inspector that verifies a property's condition from a phone walkthrough video, for landlords, renters and property managers. |
| [Edgecase Finder](vastsf/projects/edgecase-finder.md) | Edge-Case Miner turns a plain-English request like "forklift passing close to a person" into a verified, labelled video training dataset by searching an indexed archive, having Cosmos Reason watch and confirm each clip, scoring quality, and reporting what footage you still need to collect. |
| [Codec Motion](vastsf/projects/codec-motion.md) | Avoid expensive inference by utilizing built-in codec motion vectors |
| [ADAS Labs - Carrier Route Optimization](vastsf/projects/adas-labs-carrier-route-optimization.md) | Route Optimization for USPS Mail box service pickups |
| [test](vastsf/projects/test.md) | testi |
| [Linger](vastsf/projects/linger.md) | Linger is a video agent that scans every street camera in the VAST library, finds where people stop and wait, and recommends design changes like seating or lighting, each backed by the real clips it came from. |
| [OmniRoad](vastsf/projects/omniroad.md) | RoadMind enables autonomous vehicles to **detect road hazards, share them with nearby vehicles in real time, coordinate safer responses, and build a searchable city-wide memory for infrastructure management.** |
| [LookOut](vastsf/projects/lookout.md) | LookOut finds the crashes that almost happened. It sweeps street-camera footage, measures every close call, verifies it on video, simulates the crash that nearly was, and recommends FHWA-proven fixes, each backed by the clips that prove it. |
| [MATCHA: Multimodal Annotation, Task Curation & Human Assessment](vastsf/projects/matcha-multimodal-annotation-task-curation-human-assessment.md) | MATCHA helps researchers turn video archives into datasets for training and evaluation |
| [LoveCheck](vastsf/projects/lovecheck.md) | Check on your loved ones in case of risky situations and be notified in case of an emergency |
| [Longtail](vastsf/projects/longtail.md) | Longtail is a video agent that lets self-driving and robotics teams describe a rare, dangerous scenario in plain English and get back Cosmos-verified clips, ranked by danger and rarity, plus a training-ready JSON with clip IDs and start/end times. |
| [Sports Highlighter](vastsf/projects/sports.md) | Hype Agent turns raw soccer footage into a broadcast-style highlight: it understands the play frame by frame, then edits, re-watches and improves its own cut in a loop. |
| [Every cat is a villain in its own story](vastsf/projects/every-cat-is-a-villain-in-its-own-story.md) | A robot mouse that runs away from cats, loves hot dogs, and can answer questions about its own footage |
| [CloseCall](vastsf/projects/closecall.md) | A flight recorder for intersections. CloseCall turns traffic-camera video into a ledger of near-misses, with the clips, a plain-language search and a fix memo, so a city can make the case for a redesign before the crash instead of after it. |
| [Edge-Case Miner](vastsf/projects/edge-case-miner.md) | Find the rare edge-case clips AV and robotics teams need for training: describe a scenario in plain English, search every camera in a VAST video archive, let NVIDIA Cosmos3-Reason watch each candidate, and export a verified, versioned dataset. |

## 纽约 · 2026-10-09

共 41 项。[活动原文](vastnyc/event.txt) · [完整列表数据](vastnyc/project-list.json)

| 项目 | 简介 |
| --- | --- |
| [Bountiful](vastnyc/projects/bountiful.md) | Turn every market in to a shop |
| [Sentiment Engine](vastnyc/projects/sentiment-engine.md) | A real-time video agent that pairs on-screen game events with players' facial reactions and makes hours of gameplay searchable in plain language. |
| [Vision Zero Agent](vastnyc/projects/vision-zero-agent-1.md) | Real-time alerts for news desks facing hours of raw footage: NVIDIA Cosmos checks every 5 s segment as it arrives for the event you describe (explosions: 51 of 56 found), and the same agent flags close calls on street and warehouse cameras. |
| [RehabNinja](vastnyc/projects/rehabninja.md) | AI enabled rehab game |
| [StreetAudit](vastnyc/projects/streetaudit.md) | Finds which streets need repainting of road markings |
| [Scenetrace](vastnyc/projects/scenetrace.md) | SceneTrace is an AI-powered video safety investigation platform that helps cyclists, road safety teams, and urban planners identify potential near-misses, investigate contributing factors, and generate evidence-backed accident prevention recommendations from real-world footage. |
| [wahz](vastnyc/projects/wahz.md) | wahz is a musical performance and teaching agent. |
| [AisleGuard](vastnyc/projects/aisleguard.md) | AisleGuard is an autonomous warehouse safety agent that detects worker–forklift proximity risks, searches historical video for similar incidents, and triggers alerts when recurring hazards emerge. |
| [Visual Actions](vastnyc/projects/visual-actions.md) | It's a menu bar app that controls the desktop with gestures, using modes the way Vim does. You raise an open palm to "arm" it, then make a command gesture: |
| [Sightline](vastnyc/projects/sightline.md) | Self-configuring video agents that understand any feed, decide what matters, and automatically monitor, investigate, and mark important moments. |
| [Exhibit A](vastnyc/projects/exhibit-a.md) | Put a claim about your video archive on trial: one agent prosecutes with search, another cross-examines every exhibit against physical evidence, a judge rules, and the tape itself takes the stand. Nothing counts until it survives. |
| [Replay](vastnyc/projects/replay.md) | Replay helps find violations across video, no matter how small |
| [Receipts](vastnyc/projects/receipts.md) | The real-time video agent that remembers what happened |
| [ghost-nyc](vastnyc/projects/ghost-nyc.md) | Safety for cyclist |
| [PharOS](vastnyc/projects/pharos.md) | PharOS turns NYC’s traffic cameras into an early-warning system for city safety teams, spotting near misses and risky behavior at intersections so dangerous corners can be fixed before the next crash. |
| [Shepherd](vastnyc/projects/shepherd.md) | A watchdog for livestock |
| [FightLens](vastnyc/projects/fightlens.md) | FightLens helps boxing and MMA viewers understand fast exchanges through AI-powered action tracking, contextual explanations, and evolving win-probability estimates in one viewing interface. |
| [watcher](vastnyc/projects/watcher.md) | A multi-agent AI copilot that locks onto a vehicle or person in one traffic camera and hands it off, camera to camera, in real time. |
| [CarWitness 车证](vastnyc/projects/carwitness.md) | CarWitness (车证) is "Ctrl+F for street cameras": search vehicle events across cameras in English or Chinese and get cited, bilingual incident reports. |
| [Spatial Video Agent](vastnyc/projects/spatial-video-agent.md) | Spatial Video Agent lets safety and incident investigators ask one plain question across every camera and get the exact moments back, with distances in meters where the camera geometry supports it |
| [StreetCast](vastnyc/projects/streetcast.md) | StreetCast turns New York street video into cited, ready-to-file 311 reports. A rider's footage becomes every blocked bike lane, trash pile and obstruction, with the clip and the truck's fleet number, never a plate. A newsroom picks a block and gets a narrated segment where every line cites a clip. |
| [Safe Route](vastnyc/projects/safe-route.md) | SafeRoute uses AI to analyze archived street-camera footage and recommend routes around simulated hazards in an interactive evacuation drill |
| [World Compiler](vastnyc/projects/world-compiler.md) | An application that uses a relay from smart glass such as Meta Raybans to capture real time video, label it, build a semantic searchable map + digital twin. |
| [Witness — AI-Powered Video Evidence Intelligence](vastnyc/projects/witness-ai-powered-video-evidence-intelligence.md) | Witness helps accident investigators and claims reviewers evaluate conflicting statements against timestamped video evidence using VAST DataEngine, NVIDIA Cosmos, and YOLO11, with human oversight. |
| [CloseCall](vastnyc/projects/closecall-1.md) | CloseCall turns the street video cities already have into measured, clip-linked evidence of near misses (close passes, cars in crosswalks, traffic squeezing work-zone flaggers) so Vision Zero and transportation teams can fix the right streets and prove the fixes worked. |
| [Occlusive Logic](vastnyc/projects/occlusive-logic.md) | Occlusive Logic transforms video object detections into user-programmable spatial rules, enabling anyone to monitor defined areas and generate evidence-backed alerts without retraining AI models. |
| [Drive Recap](vastnyc/projects/drive-recap.md) | A trip report card for your drive; awareness score, a clip for each moment, and search; for a teen driver’s parent or anyone who wants to improve. |
| [SecondCall](vastnyc/projects/secondcall.md) | SecondCall turns the sports videos sitting in your camera roll into an instant, judge-blind second opinion: it hears and sees the decisive moment, checks it against the rulebook, and shows players and referees the evidence behind each call, starting with kendo. |
| [Witness desk](vastnyc/projects/witness-desk.md) | Witness desk searches every camera in New York or San Francisco for one vehicle by color, body type, and time, then lets you mark the clip and keep a still. |
| [The Street Talks Back](vastnyc/projects/the-street-talks-back.md) | We take street camera images of vehicles and see how compatible they are as a dating pair (tinder for vehicles) |
| [Close-Call Scout](vastnyc/projects/close-call-scout.md) | ingests video to find dangerous streets or bike paths with broken asphalt, or potholes. allows the users to check a confidence score and report it to the mayor. |
| [CrossWatch](vastnyc/projects/crosswatch.md) | CrossWatch detects faulty pedestrian and car movement |
| [UnfoldUnrest](vastnyc/projects/unrollunrest.md) | UnfoldUnrest turns everyday bike footage into a street safety audit: it finds crossings where hedges, planters or parked cars hide people about to cross from an approaching rider, says what to change, and backs every finding with the frames and a traced AI check. |
| [Warehouse best buddy](vastnyc/projects/warehouse-best-buddy.md) | A real-time video agent for warehouse safety and operations. It watches every camera through the VSS stack on VAST, catches near misses between workers and forklifts, finds idle labor and idle machines, prices the idle time per shift, and answers questions with cited clips. |
| [Spore](vastnyc/projects/spore.md) | Spore helps video model operators find gaps in their evaluation data, grow synthetic data to cover those conditions, and build new evals and benchmarks for training improved models. |
| [Auraafit](vastnyc/projects/auraafit.md) | AURAAFIT turns street-camera video into outfit analytics a merchandiser can act on: what people wear and carry, with a VAST clip and a W&B Weave trace behind every label, and without guessing who anyone is. |
| [Nostradamus](vastnyc/projects/nostradamus.md) | Prediction markets on the next five seconds of video |
| [BLACKBOX](vastnyc/projects/blackbox.md) | A robot-fleet black box that replays a drive in Rerun with tracks, closeness, time to contact, and Cosmos event times. |
| [CrossWise](vastnyc/projects/crosswise.md) | CrossWise is a crossing copilot for sidewalk delivery robots that watches street video and decides GO, WAIT or NO-GO every 0.2 seconds, so robots stop getting stuck at crosswalks. |
| [Breadcast](vastnyc/projects/breadcast.md) | Professional live broadcasting production house using AI |
| [🎮Video G(ame it) Agent — Your Footage, Now in Story Mode - Team 23](vastnyc/projects/video-g-ame-it-agent-your-footage-now-in-story-mode-team-23.md) | Load your footage like cartridges, and play your story like games🍄 |

## 更新方式

在项目根目录运行 `python3 scripts/archive_past_events.py` 会更新活动列表、下载缺失的项目页，并重新解析已有网页缓存。生成结果会覆盖对应归档文件。
完整原文和机器可读数据保留于各活动目录；本次未登录任何账号或访问参赛团队的私人运行环境。
