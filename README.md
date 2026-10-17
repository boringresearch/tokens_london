# Real-Time Video Agents Hack — London Guide

Source downloads: [project archive index](past-events/repos/README.md) (74 repositories downloaded; 12 were not publicly accessible; see the index).

Prepared 16 October 2026. This guide brings together the organiser’s email, the event Hack Page, Luma event page, VAST’s official developer repository, and related official documentation. Times are London local time, **BST (UTC+1)**.

> **Key details:** Doors open at 08:30 on 17 October. Bring physical, government-issued photo ID, a computer, and a charger. Build environments are limited to the first 100 attendees. **Project submissions are due at 16:30** and require a code repository and demo video. Register for Cosmos Community, Cursor, and Weights & Biases in advance.

Also see [Past judging criteria and how to build a strong entry](JUDGING_AND_WINNING_STRATEGY.md), with official criteria, analysis of five previous projects, and advice on project selection and demos.

[Past project archive](past-events/README.md): 45 San Francisco projects and 41 New York projects, with all 86 public descriptions, technical details, source code, and demo links.

## Contents

1. [Event and arrival](#1-event-and-arrival)
2. [Schedule and deadlines](#2-schedule-and-deadlines)
3. [Rules, submission, and judging](#3-rules-submission-and-judging)
4. [Prizes and development credits](#4-prizes-and-development-credits)
5. [Accounts and environment access](#5-accounts-and-environment-access)
6. [Architecture and development capabilities](#6-architecture-and-development-capabilities)
7. [Video data and project ideas](#7-video-data-and-project-ideas)
8. [Development workflow and troubleshooting](#8-development-workflow-and-troubleshooting)
9. [Preparation and submission checklists](#9-preparation-and-submission-checklists)
10. [Links and access results](#10-links-and-access-results)
11. [Differences between sources and open questions](#11-differences-between-sources-and-open-questions)
12. [Local reference archive](#12-local-reference-archive)

## 1. Event and arrival

| Item | Details |
| --- | --- |
| Event | Real-Time Video Agents Hack - LDN / VAST Builders Challenge |
| Date | Saturday, 17 October 2026 |
| Venue | **Halkin, 1–2 Paris Garden, London SE1 8ND, United Kingdom** |
| Doors | 08:30; breakfast provided |
| Organisers and partners | tokens&, VAST Data, NVIDIA, SpaceXAI (Cursor), CoreWeave, and Weights & Biases |
| Eligibility | Age 18+; physical, government-issued photo ID required |
| Not accepted | Student cards and digital ID; the email says there are no exceptions |
| Teams | Two people recommended, up to four. The email allows solo participation; Discord or the Luma guest list can help find teammates |
| Environment capacity | The email says build environments go to the first 100 attendees. Others may still attend and network |
| Registration | Luma applications require organiser approval. Your personal approval or ticket was not verified as part of this research |
| Photography | Attendees may be photographed or filmed for social media and promotional use |
| Contact | Reply to the event email to contact the organisers |

Sources: [Luma](https://luma.com/vastlondon), [Hack Page](https://tokensand.com/vastlondon), and the email supplied by the user. The map short link was confirmed to point to Halkin; Google Maps then displayed a cookie consent page.

## 2. Schedule and deadlines

| Time (BST) | Schedule |
| --- | --- |
| 08:30 | Doors open; breakfast |
| 09:00 | Opening keynote |
| 09:30 | Building starts; project submission opens |
| 12:30 | Lunch |
| **16:30** | **Submission deadline; demos begin** |
| 18:30 | Closing and awards |

The build window is about seven hours including lunch. Have an accessible repository and demo video ready by 16:00 to leave time for upload and submission. This is a preparation recommendation, not a separate official deadline.

**Conflicting times:** The official GitHub build guide says submissions will start “around 4:30pm”, while the London Hack Page says submissions open at 09:30 and close at 16:30. This guide follows the London-specific page: do not wait until 16:30 to begin uploading.

Sources: [Hack Page](https://tokensand.com/vastlondon), [official build guide](https://github.com/vast-data/vast-builders-challenge).

## 3. Rules, submission, and judging

### 3.1 What to build

Build an application or agent that understands video and completes a concrete task: for example, search for clips, answer questions, identify events, or take action based on results. Aim for a working prototype by the end of the day. The Hack Page says projects must be developed during the event; each team submits one project and may have up to four members.

### 3.2 Submission materials

| Material | Page requirements |
| --- | --- |
| GitHub repository | Accessible to judges; the page does not explicitly require it to be public |
| Demo video | Short and shared by link; no maximum duration stated |
| Project description | Explain what it does and which tools it uses |
| Team details | Team members’ names and contact email addresses |
| Optional | Working website and project screenshots |

- [Submit a project](https://tokensand.com/vastlondon/submit): the page was visited and redirected to sign-in. It supports Google sign-in or an email one-time code. The fields, attachment limits, and whether submissions are currently open were not verified after sign-in.
- [Project listing](https://tokensand.com/vastlondon/projects): no project list was extracted during this visit; this does not establish whether submissions exist.
- The sign-in page says new builder profiles are public by default; they can be made private in Profile.

### 3.3 Judging

The VAST event series lists three judging dimensions: **creativity, technical execution, and real-world impact**. No London-specific weighting, scorecard, tie-break rule, or demo duration was found. The build guide says the first judging round involves meeting each team.

Speakers and judges listed on Luma:

| Role | Name and listed position |
| --- | --- |
| Speaker and judge | Brian Verkley — Director, AI Data Platform @ VAST Data |
| Judge | Abubakr Karali — Senior Solutions Architect @ NVIDIA |
| Judge | Ram B. — Sr. Developer Advocate @ VAST Data |
| Judge | Junaid Butt — AI Solutions Engineer @ Weights & Biases |

Sources: [Hack Page](https://tokensand.com/vastlondon), [Luma](https://luma.com/vastlondon), [VAST Builders Challenge announcement](https://www.vastdata.com/blog/lets-build-introducing-the-vast-builders-challenge).

## 4. Prizes and development credits

### 4.1 Competition prizes

| Prize | Confirmed information |
| --- | --- |
| First place | NVIDIA DGX Spark™ |
| Second place | Hugging Face Microduck |
| Other listed prizes | Luma lists Cursor Credits and Cash Gift Cards, without amounts or a mapping to placements |
| Allocation | The Hack Page says two teams receive the overall prizes; credits and gift cards are shared among team members |

The public pages do not clarify whether hardware is awarded to each person, whether other sponsors offer separate prizes, or the amounts and redemption conditions.

### 4.2 Cursor credits

1. Register for Cursor using the email address used for event registration; a personal email is recommended.
2. The official build guide says registered attendees who check in will receive credits. The event email stresses registering before the event.
3. Check [Cursor Usage](https://cursor.com/dashboard/usage); the guide says the request should appear as `Free`.
4. If credits do not arrive or you need more, use the [Cursor Credits Request form](https://forms.gle/AVta9RRTmfdeUNX26).
5. The form was opened and requires a name, personal email, and reason (not received / need more); team is optional. It was not filled in or submitted on your behalf.
6. The guide recommends setting the Cursor Agent model to `Auto` to save tokens. Credit amount, expiry, and model coverage are not published.

### 4.3 W&B / CoreWeave inference credits

Create a W&B account in advance. The email says serverless inference will be available from the start of the event. For more credits, contact the Weights & Biases by CoreWeave team on site; they will use the email associated with your account. The team cloud environment is expected to have `WANDB_API_KEY`, `WANDB_TEAM`, and `WANDB_PROJECT` preconfigured; this was not verified inside your environment.

The [original inference documentation](https://docs.wandb.ai/inference) now redirects to [CoreWeave Inference documentation](https://docs.coreweave.com/inference), which was readable in a browser. It documents an OpenAI-compatible API; the current example base URL is `https://api.inference.wandb.ai/v1`. Model selection and available quota depend on the event environment. The trial entry point is [Forge Inference](https://forge.coreweave.com/inference).

Sources: [official build guide](https://github.com/vast-data/vast-builders-challenge), [credits form](https://forms.gle/AVta9RRTmfdeUNX26), [inference documentation](https://docs.coreweave.com/inference), and organiser email.

## 5. Accounts and environment access

### 5.1 Accounts to prepare

| Account | Purpose | Link |
| --- | --- | --- |
| VAST Cosmos Community | Access event infrastructure and ask for help | [Community](https://community.vastdata.com/) |
| Cursor | AI-assisted coding, remote SSH development, event credits | [Website](https://cursor.com/) |
| Weights & Biases | Inference and development tools | [Website](https://wandb.ai/site/) |
| tokens& | Submit the project | [Submission page](https://tokensand.com/vastlondon/submit) |
| GitHub | Host code that judges can access | Required for submission |
| Discord | Find teammates and contact attendees or sponsors | [Invite](https://discord.gg/rPBMhMzRU) |

**Name distinction:** Cosmos Community is the VAST community. NVIDIA Cosmos is model technology for video understanding, among other uses. They are not the same registration portal.

### 5.2 Current access workflow

1. Register for Cosmos Community and read [Start here](https://community.vastdata.com/t/vast-builders-challenge-start-here/2102).
2. Follow [Workshop access instructions](https://community.vastdata.com/t/about-the-workshop-category-and-access/1969) to the [lab environment](https://workshop.thecosmoslabs.com). During this research, access stopped at a Cloudflare Access email-code sign-in page.
3. Form your team and sit together. Select the team number assigned by the organisers; the guide screenshot warns that the team number can only be selected once. Teams share pipelines, indexes, and credentials.
4. Configure SSH as described by the lab page and verify the connection from a terminal first.
5. Open a new Cursor window on your computer, select **Connect via SSH**, and select the `bc-<username>` host shown by the lab page.
6. Open the remote `vast-builders-challenge` folder. The repository, files, commands, and credentials are on the VM.
7. Open **Video Search & Summary** from the lab page and check its Search, Explore, and Dashboard pages.
8. In Cursor, you can use the provided `/build-day-quickstart` to get familiar with the environment.

### 5.3 SSH public key

The [official SSH post published 16 October](https://community.vastdata.com/t/generate-public-key-for-cursor-ssh-access/2133) says to generate a public key before connecting with Cursor, then paste it into `Option 1 - Key` on the lab page. It uses ed25519 and the filename `~/.ssh/id_ed25519_cursor`; on macOS, `pbcopy` can copy the `.pub` file contents.

This guide only documents the instructions; it did not generate or modify a local key. Follow the lab page for the actual hostname, username, and SSH configuration after signing in.

### 5.4 Local preparation

Bring a computer and charger. The organisers recommend a personal computer to avoid corporate VPN or IT restrictions. “No local setup required” means you do not need to deploy the models or data platform yourself; the latest guide still calls for local Cursor and SSH preparation.

Sources: [official build guide](https://github.com/vast-data/vast-builders-challenge), [preparation guide](https://github.com/vast-data/vast-builders-challenge/blob/main/BEFORE_YOU_BUILD.md), and the community post above.

## 6. Architecture and development capabilities

### 6.1 What the platform provides

VAST AI OS provides video storage, processing pipelines, and indexing; models run on CoreWeave GPUs. Teams build their own application, agent, or dashboard on top of these capabilities.

```text
Already done:       raw video → chunks → detection / captions / embeddings → VastDB index
Your main workflow: search / Q&A / video access → application logic → display or action
For new captions:   existing chunks → re-detection / captions / embeddings → index update
```

### 6.2 Models listed in the event architecture guide

| Model | Purpose | Environment variable |
| --- | --- | --- |
| Cosmos3-Reason | Video captions and video reasoning | `COSMOS3_REASON_URL` |
| YOLO11 (`yolo11s`) | Object detection, classes, and bounding boxes | `YOLO_URL` |
| Cosmos Embed1 | Text/visual embeddings and hybrid search | `COSMOS_EMBED1_URL` |
| Canary-1B | Speech recognition and translation; not integrated into the current VSS pipeline, so it requires your own integration | `CANARY_1B_URL` |

These are the services listed by the event repository; this does not mean every capability in the general NVIDIA documentation is deployed for this event. Each model has its own host and port; do not infer one service’s address from another.

### 6.3 Useful skills

| Skill | Use |
| --- | --- |
| `retrieval/search` | Search clips with natural language and filters |
| `retrieval/agent-qa` | Answer questions using video evidence |
| `retrieval/videos` | Browse videos, play clips, inspect captions and detections, and summarise video |
| `retrieval/dashboard` | View index counts and processing status |
| `retrieval/suggest-prompts` | Get search suggestions and recent events |
| `retrieval/list-metadata` | Find available cameras, locations, scenarios, and other values |
| `ingest/reingest-videos` | Reprocess indexed videos with a new prompt |
| `ingest/reingest-chunk` | Reprocess a single chunk |
| `vastdb-read` | Read database contents directly |
| `/deploy-app-no-registry` | Deploy an application in the team Kubernetes environment |
| `/ask-cosmos` | Generate a troubleshooting request for you to copy to the community |

Skills are in `.cursor/skills/` in the official repository and read environment variables from the VM. Other variables are listed in the local [config.example](sources/vast-builders-challenge/config.example); it contains placeholders only and does not need to be filled in to deploy the platform yourself.

### 6.4 Development limits and important notes

- Use your own team’s namespace, bucket, account, and UI. Do not access other teams’ resources.
- Models, databases, and pipelines are already deployed. The event guide says not to recreate DataEngine functions or redeploy pipelines.
- The event environment is mainly for **re-ingesting** existing, chunked videos. The architecture guide says the challenge does not include uploading new chunks or running the Segmenter.
- The latest guide says not to import internet videos such as YouTube; the provided video sources have been screened for authorization.
- Assign one or two team members to handle bulk re-ingestion to avoid processing long videos repeatedly.
- After changing a prompt, wait for captions, detections, embeddings, and index writes to finish. An accepted API request does not mean the results are searchable yet.
- First check whether existing captions include the details you need. Reprocess only if they do not. Empty search results may indicate authentication, index health, or filter problems; they do not prove an event is absent from the footage.

Sources: [official build guide](https://github.com/vast-data/vast-builders-challenge), [architecture reference](https://github.com/vast-data/vast-builders-challenge/blob/main/ARCHITECTURE_REFERENCE.md).

## 7. Video data and project ideas

The datasets below are listed in the official architecture reference; this does not guarantee that every dataset is ready in your London team’s index. Check the actual Explore and Dashboard pages. The San Francisco data is still marked as awaiting import in the document.

| Dataset | Location / `camera_id` | Documented size | Possible direction |
| --- | --- | --- | --- |
| Multi-camera I-24 highway | `nashville` / `i24_cam-1` | About 51 clips | Lane changes, congestion, vehicle interactions |
| PIE driving videos | `toronto` / `pie_cam-3` | 6 groups of long videos | Intersection turns, pedestrians and vehicles, road safety |
| Neighbourhood streets | `neighborhood` / `neighborhood_cam-1` | Two days of merged video | Parking, stopping, passing vehicles |
| San Francisco streets | `san_francisco` / `sf_streets_cam-1` through `4` | 4 cameras; pending import | Multi-camera street activity |
| Warehouse SDG RGB | `warehouse3` / `sdg_warehouse_cam-2` | About 178 short clips | Forklifts approaching pedestrians, blocked aisles |
| Indoor Smart Spaces | `indoor` / `smartspace_cam-1` | About 102 clips | Foot traffic, passageways, facility operations |

Common filter fields include `camera_id`, `capture_type`, and `location`, as well as detected object classes. “Category” in the table is a demo grouping, not necessarily a filter field with that name.

The official recommendation is to start with Highway Traffic (Pack A) or Warehouse Safety (Pack C). Validate retrieval with a concrete query such as `truck changing lanes` or `forklift near a person in an aisle`, then build the interface and follow-on action. A cross-scenario idea could focus on “a person near a moving vehicle,” but first confirm the relevant datasets are indexed.

Optional analysis scenarios include `surveillance`, `traffic`, `live_driving`, `retail`, `warehouse`, `egocentric`, `sports`, `nhl`, and `general`; use the actual values returned by `list-metadata`.

Source: [Architecture reference: video corpus](https://github.com/vast-data/vast-builders-challenge/blob/main/ARCHITECTURE_REFERENCE.md#video-corpus-already-indexed).

## 8. Development workflow and troubleshooting

A small end-to-end loop based on the official workflow:

1. Inspect videos already in the index and choose a concrete scenario.
2. Search for an event, play a returned clip, and confirm the timestamp and footage match.
3. Ask a question about the same video and inspect the evidence-backed answer.
4. If captions lack an important detail, try custom-prompt re-ingestion on a small number of clips.
5. Wait for indexing to finish, then repeat the same search and inspect the results.
6. Build an application using the existing APIs. After deployment, open it with the **App** button on the lab page.
7. Prepare the demo video, repository, and description, then submit before 16:30.

**If something fails:** The official guide recommends updating the preinstalled repository on the VM first, then asking Cursor to inspect environment health. For empty search results, check sign-in, whether the pipeline and index match, and whether the filter values exist. To ask for help, run `/ask-cosmos` to prepare a report, then create a topic in the [Workshop category](https://community.vastdata.com/c/workshop/27). Include your team number, goal, error, and attempted fixes; do not reply directly to the access-instructions topic.

References: [Build Day Guide](https://github.com/vast-data/vast-builders-challenge), [Workshop help instructions](https://community.vastdata.com/t/about-the-workshop-category-and-access/1969).

## 9. Preparation and submission checklists

### Prepare in advance

- [ ] Confirm Luma registration approval and ticket.
- [ ] Bring physical government-issued photo ID, a computer, and a charger.
- [ ] Register for Cosmos Community, Cursor, and W&B; use the same email for Cursor as for event registration.
- [ ] Prepare Cursor on your computer and read the SSH public key instructions.
- [ ] Join Discord to find teammates; teams can have up to four people. Agree on a concrete problem.
- [ ] Read the official preparation and build guides; save the local PDF copies.
- [ ] Confirm you can access GitHub and tokens&, and have a way to share the demo video.

### After arriving

- [ ] Arrive around 08:30 and check in; note the 100-person environment limit.
- [ ] Select the assigned team number and connect to SSH and Video Search & Summary.
- [ ] Check Cursor credits; use the request form if they are missing.
- [ ] Check which datasets, models, and inference credits are actually available.
- [ ] Assign one or two team members to bulk re-ingestion.
- [ ] Confirm judging rules, demo duration, the 16:30 deadline, and submission requirements.

### Before submitting

- [ ] The project runs, and demo results can be verified against the specific video clips.
- [ ] Judges can access the repository; the project description explains the problem, tools, and run instructions.
- [ ] The demo video is shareable and link permissions work.
- [ ] Team names and emails are complete; prepare an optional website and screenshots if available.
- [ ] Submit through the project page and confirm the submission succeeded.

## 10. Links and access results

### 10.1 Email and event links

| Resource | Resolved link | Result during research |
| --- | --- | --- |
| Event page | [Luma](https://luma.com/vastlondon) | Public event information read; personal ticket not verified |
| Hack Page | [tokensand.com/vastlondon](https://tokensand.com/vastlondon) | Rules, prizes, submission requirements, and links read in browser |
| Discord | [discord.gg/rPBMhMzRU](https://discord.gg/rPBMhMzRU) | Short link resolved; page prompted to open Discord; channels not read and server not joined |
| Cosmos Community | [community.vastdata.com](https://community.vastdata.com/) | Public home page and access/SSH posts readable |
| Cursor | [cursor.com](https://cursor.com/) | Website readable; no personal account sign-in |
| W&B | [wandb.ai/site](https://wandb.ai/site/) | Website readable; no personal account sign-in |
| Map | [Location link from email](https://luma.link/q1R2KHGAhj) | Points to Halkin in Google Maps; stopped at cookie consent |
| Project submission | [Submit](https://tokensand.com/vastlondon/submit) | Google or email-code sign-in required |
| Project list | [Projects](https://tokensand.com/vastlondon/projects) | No usable project list extracted |
| Cloud lab environment | [Workshop](https://workshop.thecosmoslabs.com) | Cloudflare Access email-code sign-in |
| Cursor credits request | [Form](https://forms.gle/AVta9RRTmfdeUNX26) | Fields reviewed; not submitted |

Original short links: Hack Page `vy4oXPaEZh`; Discord `21zITYgniZ`; Cosmos `4gkItoDDoj`; Cursor `GmmlfgFzwq`; W&B `lcqeNzQsSy`. Each is under `https://luma.link/`.

### 10.2 Official references to read first

| Resource | Purpose |
| --- | --- |
| [Official developer repository / build-day guide](https://github.com/vast-data/vast-builders-challenge) | Access, skills, development, deployment, submission, and troubleshooting |
| [Before You Build](https://github.com/vast-data/vast-builders-challenge/blob/main/BEFORE_YOU_BUILD.md) | Account and computer preparation; choosing a project |
| [Architecture Reference](https://github.com/vast-data/vast-builders-challenge/blob/main/ARCHITECTURE_REFERENCE.md) | Models, data pipeline, video groups, and sample queries |
| [Community Start Here](https://community.vastdata.com/t/vast-builders-challenge-start-here/2102) | Community registration and access navigation |
| [Workshop Access](https://community.vastdata.com/t/about-the-workshop-category-and-access/1969) | Environment link, access PDF, and help process |
| [SSH public key instructions](https://community.vastdata.com/t/generate-public-key-for-cursor-ssh-access/2133) | Local setup before connecting with Cursor |
| [VAST Builders Challenge announcement](https://www.vastdata.com/blog/lets-build-introducing-the-vast-builders-challenge) | Event background and series judging dimensions |

### 10.3 Further technical references

These pages were visited or access was attempted. General product documentation is background information; use the event-specific repository for environment procedures.

| Resource | Content / access result |
| --- | --- |
| [VAST AI OS](https://www.vastdata.com/platform/ai-os) | Readable; platform components including storage, database, and DataEngine |
| [VAST video search example](https://www.vastdata.com/blog/unlock-video-intelligence-build-real-time-video-search-and-ai-summary) | Readable; reference architecture and video search app background; an older general tutorial |
| [NVIDIA VSS documentation](https://docs.nvidia.com/vss/latest/) | Readable; reference architecture for video search, summarisation, real-time analysis, and agents |
| [NVIDIA Cosmos](https://www.nvidia.com/en-us/ai/cosmos/) | Readable; overview of Cosmos technology |
| [Ultralytics YOLO11](https://docs.ultralytics.com/models/yolo11) | Readable; detection model information |
| [CoreWeave](https://coreweave.com/) | Readable; GPU cloud platform overview |
| [Serverless Inference](https://docs.coreweave.com/inference) | Readable in browser; W&B URL redirects here; OpenAI-compatible API |
| [W&B Weave](https://wandb.ai/site/weave/) | Readable; agent observability and evaluation tools |
| [ARIA](https://www.coreweave.com/products/coreweave-forge/aria) | Hack Page link redirects here |
| [Hack Page overview video](https://drive.google.com/file/d/1qUrT0QaBGS6mXxHTEG2vnLM2pT1KY4RD/view?usp=sharing) | Access attempted; video content not obtained, watched, or transcribed |
| [Another overview video in the prep guide](https://drive.google.com/file/d/1kMiMJCX-4YDmtw8RuRYKg8Pv76dKcC4C/view?usp=sharing) | A separate file linked by the official repository; not watched, so it cannot be assumed to be the same video |

## 11. Differences between sources and open questions

| Question | Source differences / current handling |
| --- | --- |
| Submission time | GitHub says submissions start around 16:30; the London Hack Page says 16:30 is the deadline. Prepare for the earlier deadline and confirm on site |
| Local setup | Email says no local setup; latest guide requires local Cursor and SSH. The cloud platform needs no self-deployment, but client access still needs preparation |
| Bring your own video | Series blog permits personal material; the current event guide prohibits importing internet video, and the architecture guide limits work to re-ingesting existing clips. Ask the on-site team before adding any new material |
| Data availability | Architecture reference lists six groups; San Francisco is marked as pending import. Choose based on the actual team index |
| Team size | Email permits solo entries; Hack Page recommends at least two and allows up to four. This is a recommendation, not evidence that solo participation is prohibited |
| Registration deadline | Luma contains both 15 October and “one week before the event” wording; check your ticket to confirm whether your application was approved |
| Prizes | Hack Page specifies first and second place; Luma also lists credits and gift cards without amounts or placement mapping |
| Judging and demos | Series judging dimensions are available; London weights, demo duration, and scorecard were not found |
| Credits and later access | Cursor/W&B amounts, expiry, and how long the VM or applications remain available after the event are unpublished |
| Submission details | The full form after sign-in, editing options, video duration, and file-size limits were not verified |
| Other rules | The pages visited do not fully specify limits on pre-written code, external services, intellectual property, or whether every sponsor tool must be used |

## 12. Local reference archive

The main information is in this README. Source snapshots are also retained for verification:

- [Hack Page text and links](sources/hack-page.json)
- [Cursor credits form text](sources/credits.json)
- [Inference documentation text](sources/inference.json)
- [Official developer guide](sources/vast-builders-challenge/README.md)
- [Preparation guide](sources/vast-builders-challenge/BEFORE_YOU_BUILD.md)
- [Architecture reference](sources/vast-builders-challenge/ARCHITECTURE_REFERENCE.md)
- [Environment variable placeholder example](sources/vast-builders-challenge/config.example)
- [Preparation guide PDF](sources/vast-builders-challenge/docs/BEFORE_YOU_BUILD.pdf)
- [Build guide PDF](sources/vast-builders-challenge/docs/BUILD_DAY.pdf)
- [Architecture reference PDF](sources/vast-builders-challenge/docs/ARCHITECTURE_REFERENCE.pdf)
- [Infrastructure onboarding PDF](sources/vast-builders-challenge/docs/BUILDERS-CHALLENGE-INFRA-ONBOARDING.pdf)

The PDFs are original files downloaded from the official source and were not checked page by page against the latest Markdown. The old `BUILD_DAY.md` now points to the official README; use that README for the day-of guide. Source snapshots reflect pages at the time of capture and are not continuously updated.

This research covered public information and pre-login pages only. No accounts were registered, no community or Discord was joined, no forms were submitted, and no private lab environment was accessed. Email unsubscribe links, tracking pixels, and generic social or store pages were outside the scope of this event guide.
