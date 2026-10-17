# Event Triage

原始页面：https://tokensand.com/p/event-triage

所属活动：vastlondon

说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。

## 页面正文

Hackathon
Project gallery
Event Triage
dgbose888about 4 hours agoContributorJudging locked: Event build
Event Triage
ET desk video agent watches the last 60 seconds of a trader's screen, fixes the problem on the spot where it's possible and safe to do, otherwise routes it to a support team via Slack channel.
Review the project
Start with the source code, then open the demo or video if available.
View GitHub repository
Watch demo videoProject gallery
Demo video
Watch demo video
Project description
ET Phone Desk turns screen recordings into resolved incidents. When a trader hits a hotkey, the last 60 seconds of their screen is ingested into the VAST AI OS, which indexes every clip for semantic search, so a growing archive of past incidents and their fixes becomes searchable in natural language. NVIDIA Cosmos reasons over the clip to identify the application, the steps taken, the error code and the exact moment of failure, with OCR picking up on-screen text. Weights & Biases–hosted LLMs then decide what to do: deterministic rules map known error codes to a team, a priority and a safe fix playbook, the LLM handles only ambiguous cases, and an independent verifier agent double-checks every decision. For eligible issues, the agent runs an allowlisted, reversible fix and confirms it worked with a health check before marking it resolved. Critical issues are routed to the owning team in Slack immediately, with the clip, the diagnosis and everything already tried. Guardrails keep it safe on a trading desk: on-screen text is treated as untrusted, the agent never touches orders or positions, and per-clip cost and time budgets apply. W&B Weave traces every step and scores routing and resolution accuracy against our labelled clips, all running on CoreWeave GPUs and built with Cursor and Claude Code.
Project links
GitHub repository
Demo video
Tools used
Tools used
Grok Build
NVIDIA
SpaceXAI (Cursor)
CoreWeave (Weights & Biases)

## 公开链接

- [Hackathon](https://tokensand.com/vastlondon)

- [Project gallery](https://tokensand.com/vastlondon/projects)

- [dgbose888](https://tokensand.com/u/dgbose888)

- [View GitHub repository](https://github.com/saneeshmorais16/Event-Triage)

- [Watch demo video](https://www.loom.com/share/27d839e2d97949289596fc1f85f26627)

- [项目截图](https://opengraph.githubassets.com/1/saneeshmorais16/Event-Triage)
