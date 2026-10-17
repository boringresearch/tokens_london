# LiveGuard

原始页面：https://tokensand.com/p/liveguard

所属活动：vastlondon

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
LiveGuard
Karim Bakkaliabout 4 hours agoContributorJudging locked: Event build
LiveGuard
LiveGuard turns every high-stakes video call into a verified one, quietly, in the background, before a deepfake can talk anyone into a transfer.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Watch demo videoProject gallery
Demo video
Watch demo video
Project description
What we built
LiveGuard checks, during a live video call, whether the person on screen is a real human, before a finance approver releases a payment. It runs as a small floating dot over Meet or Zoom. The caller is never asked to do anything. The agent watches, decides, stays quiet on a pass, and leaves a red banner up on a fail.
How it works
Watch. The browser records the caller's video tile, from a screen share of the call or a webcam, in back-to-back 8-second windows.
Measure, with YOLO. YOLO pose finds the caller (the largest person in the window, ignoring your own self-view) and checks four things:
1.Is there one clear face?
2.Are there no sudden jumps between frames (cuts or glitches)?
3.Does the head show natural micro-movement? A held-up photo moves as one rigid piece.
4.Are the frames changing at all, or is the feed frozen?
It also marks the hard moments, a head turn or a hand near the face, because that's where face-swap deepfakes break.
Judge, with Cosmos. NVIDIA Cosmos sees five frames, hard moments first, each labelled with what YOLO measured. It judges whether the person looks physically real, and names any artefact with its frame number.Decide each window.
1.FAIL if Cosmos found an artefact or the feed is frozen.
2.INCONCLUSIVE if there was no clear face or no natural movement.
3.Otherwise PASS: "strong" if a hard moment was judged clean, "basic" if the caller stayed still.
Project links
GitHub repository
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

- [Karim Bakkali](https://tokensand.com/u/karim-bakkali)

- [View GitHub repository](https://github.com/sid184/liveness-agent-hack)

- [Watch demo video](https://www.loom.com/share/dce5d28dd8b84dc6aa19e437db75f676)

- [项目截图](https://opengraph.githubassets.com/1/sid184/liveness-agent-hack)
