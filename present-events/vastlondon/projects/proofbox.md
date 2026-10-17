# ProofBox

原始页面：https://tokensand.com/p/proofbox

所属活动：vastlondon

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
ProofBox
tokydokyabout 5 hours agoContributorJudging locked: Event build
ProofBox
ProofBox turns packing-station video into dispute evidence. An overhead camera ties each parcel to its order via QR, YOLO tracks every item going in, Cosmos Reason verifies each one, and sellers get a per-item packed / not-packed verdict linked to the exact clip.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Visit project websiteWatch demo videoProject gallery
Demo video
Watch demo video
Project description
The problem: “item missing” claims are one of the costliest headaches in e-commerce, and sellers often lose them by default because they can’t prove what went into the box.
What ProofBox does: an overhead camera records every mailer as it is packed. The QR label on the parcel is detected and the frame is linked to the order. YOLO tracks each item placed inside, and NVIDIA Cosmos Reason watches the clip to confirm what each item is and that it actually went in. Every verdict, timestamp and clip reference is stored in VastDB on the VAST AI OS.
When a claim lands: the seller asks in plain text or by voice (“was the charger in order 4821?”) and a W&B-hosted agent returns a per-item verdict, packed or not packed, with the exact clip as evidence, ready to attach to the marketplace or payment dispute.
Built on: VAST S3 + DataEngine + VastDB for ingest and the evidence store, NVIDIA Cosmos Reason and Cosmos Embed for reasoning and semantic search over packing footage, YOLO on CoreWeave GPUs for detection and tracking, Weights & Biases Inference for the agent, built in Cursor.
Supply chain potential: the same pattern works at every handoff. Add cameras at pick, pack, carrier handover and returns, and each order gets a video-verified chain of custody. That gives 3PLs and brands proof for mis-pick and shrinkage disputes, carrier liability and insurance claims, plus searchable warehouse footage (“every order where an item was swapped after pick”).
Project links
GitHub repository
Project website
Demo video
Tools used
Tools used
VAST Data
NVIDIA
SpaceXAI (Cursor)

## 公开链接

- [Hackathon](https://tokensand.com/vastlondon)

- [Project gallery](https://tokensand.com/vastlondon/projects)

- [tokydoky](https://tokensand.com/u/tokydoky)

- [View GitHub repository](https://github.com/lmarkmann/proofbox)

- [Visit project website](https://proofbox.luis-markmann.workers.dev/)

- [Watch demo video](https://youtu.be/UgSbvmjAwKs)

- [项目截图](https://auth.tokensand.app/storage/v1/object/public/project-screenshots/4e858a3a-0df8-4cdf-b669-3278cc78217c/5899d050-4eef-4f3d-b666-ba095b5145a9.png)

## 页面结构化补充资料

### Setup instructions

We can provide the label printer to plug in and test the whole operation end to end exactly as seen in the demo
