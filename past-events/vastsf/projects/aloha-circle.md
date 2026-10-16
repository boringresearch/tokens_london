# Aloha Circle

原始页面：https://tokensand.com/p/aloha-circle

所属活动：vastsf

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Aloha Circle
seth14 days agoNewcomerJudging locked: Event build
Aloha Circle
Aloha Circle turns arriving on Maui into meeting Maui — travelers scan a QR at baggage claim, share a playful aloha ritual with an AR guide, and get matched with a real local to enjoy a donated island experience together, all while supporting Maui causes.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
Aloha Circle turns a Maui vacation into a relationship with Maui. From the moment visitors land at Kahului Airport, a QR banner at baggage claim starts their aloha with a donation to a live local cause; at the physical Aloha Circle kiosk, keiki and adults complete the Breath of Aloha — a camera-tracked ritual (honi ihu forehead hold, eyes, ears, nose, heart) guided by Kanaloa, a lifelike water-spirit avatar — then spin the Wheel of Aloha to win a sponsor-donated experience and meet the Maui local whose style best matches theirs, claimed instantly by QR or email. Behind it, the Aloha Agent continuously ingests a Maui Needs Index of local causes and recomputes matches between travelers, locals, nonprofits, and donated experiences, so every visit ends in a real action: money to a cause, and a traveler and a local actually meeting.
Sponsors are first-class citizens: local businesses donate the experiences on the wheel (helicopter tours, dinners, excursions), get brand placement in the kiosk and on aloha-circle.com, and a sponsor VLM even reads visitor brand/style signals to drive the match. On the tech side the build is sponsored/powered by VAST Data (S3 + VSS video search), NVIDIA (Cosmos Reason / Cosmos Embed NIMs), W&B Inference by CoreWeave, Roboflow (RF-DETR), and Masky avatars — built across the Agent Harness Hackathon (TrueForge × Qodo × Bright Data) and the VAST Builders Challenge.
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

- [seth](https://tokensand.com/u/seth)

- [View GitHub repository](https://github.com/contingentx/aloha-circle)

- [Visit project website](https://aloha-circle.com/)

- [Watch demo video](https://aloha-circle.com/about)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/50911edc-c6d4-4b77-bcae-f4d4d4847256/92e759dc-eb80-49ef-a96d-1435fff675dc.jpg)

## 页面结构化补充资料

### Technical architecture

Website (aloha-circle.com): Vite + React static site on S3 + CloudFront/ACM/Route53, GitHub Actions OIDC deploys (dev → dev.aloha-circle.com, production → aloha-circle.com); donations backend on AWS Lambda + API Gateway. Mobile app: Expo / React Native. Agent harness: Node API + continuous Maui Needs Index ingest + deterministic matcher, exposed over MCP; a TrueForge workflow recomputes matches in a Daytona sandbox and gates any persistent action behind a one-use human-approval capability. Kiosk: Electron app with MoveNet / RF-DETR (Roboflow) pose tracking for gesture-advanced ritual stages and the grab-and-pull wheel spin; Kanaloa rendered via Masky; a VLM on W&B Inference by CoreWeave (Gem

### Setup instructions

run the electron app within /kioskapp of the github to start the experience the visitor at maui airport will have

### Lessons learned

so many, hard to remember. main thing is how to describe gestures to one-shot prompts =]
