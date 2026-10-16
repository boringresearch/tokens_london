# Real-Time Video Agents Hack — London 参赛资料

源码下载：[仓库索引](past-events/repos/README.md)（已下载 74 个；12 个公开访问失败，详见索引）。

整理日期：2026-10-16。汇总主办方邮件、实际访问的 Hack Page、Luma 活动页、VAST 官方开发仓库及相关官方文档。时间均为伦敦当地时间 **BST（UTC+1）**。

> 最重要的事：10 月 17 日 08:30 开门，带实体政府照片证件、电脑和充电器；构建环境限最先到场的 100 人。**项目提交截止为 16:30**，需要代码仓库和演示视频。提前注册 Cosmos Community、Cursor、Weights & Biases。

另见：[往期评审标准与争取获奖策略](JUDGING_AND_WINNING_STRATEGY.md)，包含官方标准、5 个往期项目分析、选题与演示建议。

往期完整资料：[旧金山 45 项 + 纽约 41 项项目归档](past-events/README.md)，包含全部 86 项公开详情、技术说明、代码与演示链接。

## 目录

1. [活动与到场](#1-活动与到场)
2. [流程与截止时间](#2-流程与截止时间)
3. [参赛规则、提交与评审](#3-参赛规则提交与评审)
4. [奖品与开发额度](#4-奖品与开发额度)
5. [账号与环境接入](#5-账号与环境接入)
6. [技术架构与开发能力](#6-技术架构与开发能力)
7. [视频数据与选题](#7-视频数据与选题)
8. [开发顺序与故障处理](#8-开发顺序与故障处理)
9. [准备与提交清单](#9-准备与提交清单)
10. [链接导航与访问结果](#10-链接导航与访问结果)
11. [信息差异与待确认事项](#11-信息差异与待确认事项)
12. [本地资料归档](#12-本地资料归档)

## 1. 活动与到场

| 项目 | 信息 |
| --- | --- |
| 名称 | Real-Time Video Agents Hack - LDN / VAST Builders Challenge |
| 日期 | 2026 年 10 月 17 日，星期六 |
| 地点 | **Halkin, 1–2 Paris Garden, London SE1 8ND, United Kingdom** |
| 开门 | 08:30，提供早餐 |
| 主办/合作 | tokens&、VAST Data，以及 NVIDIA、SpaceXAI（Cursor）、CoreWeave、Weights & Biases |
| 资格 | 18 岁及以上；必须出示实体政府签发的带照片证件 |
| 不接受的证件 | 学生证、电子证件；邮件注明无例外 |
| 团队 | 推荐 2 人，最多 4 人；邮件允许单人参与，可通过 Discord 或 Luma guest list 找队友 |
| 环境名额 | 邮件说明仅最先到场的 100 位参与者获得构建环境；其他人仍可参加交流 |
| 报名 | Luma 需申请并由主办方批准；本次未验证你的个人批准/票券状态 |
| 拍摄 | 现场拍照及录像，参加即同意影像可能用于社交媒体和宣传 |
| 联系主办方 | 可直接回复你收到的活动邮件 |

来源：[Luma](https://luma.com/vastlondon)、[Hack Page](https://tokensand.com/vastlondon)及用户提供的通知邮件。地图短链接已确认指向 Halkin；Google Maps 随后显示 Cookie 同意页。

## 2. 流程与截止时间

| 时间（BST） | 安排 |
| --- | --- |
| 08:30 | 开门、早餐 |
| 09:00 | 开场主题演讲 |
| 09:30 | 开始开发；项目提交入口开放 |
| 12:30 | 午餐 |
| **16:30** | **项目提交截止，同时开始 Demos** |
| 18:30 | 闭幕、颁奖 |

开发窗口约 7 小时，包含午餐。建议在 16:00 前准备好可访问的仓库与演示视频，给上传和提交留时间；这是准备建议，不是官方另设的截止时间。

**时间冲突：** 官方 GitHub 开发指南写“submissions will start around 4:30pm”，但伦敦 Hack Page 明确显示 09:30 开放、16:30 截止。本整理按伦敦专属提交页准备，不能等到 16:30 才开始上传。

来源：[Hack Page](https://tokensand.com/vastlondon)、[官方开发指南](https://github.com/vast-data/vast-builders-challenge)。

## 3. 参赛规则、提交与评审

### 3.1 要做什么

开发一个能理解视频并完成具体任务的应用或 Agent，例如搜索片段、回答问题、识别事件、根据结果执行动作。目标是在当天完成一个可运行的原型。Hack Page 要求项目在活动期间开发，每队提交一个项目，最多 4 人。

### 3.2 提交材料

| 材料 | 页面要求 |
| --- | --- |
| GitHub 仓库 | 评审能够访问；页面没有明确要求必须公开 |
| 演示视频 | 简短，并提供可分享的链接；未写明时长上限 |
| 项目介绍 | 说明做了什么、用了什么工具 |
| 团队信息 | 队员姓名和联系邮箱 |
| 可选补充 | 可运行的网站、项目截图 |

- [提交项目](https://tokensand.com/vastlondon/submit)：已访问，跳转登录页。支持 Google 登录或邮箱一次性验证码。登录后字段、附件限制和实际开放状态未验证。
- [项目展示页](https://tokensand.com/vastlondon/projects)：已访问，本次未提取到项目列表；不能据此判断是否已有提交。
- 登录页说明：新建 builder profile 默认公开，可在 Profile 中改为私密。

### 3.3 评审

VAST 系列活动介绍列出三个维度：**创意、技术实现、实际应用价值**。未找到伦敦场的评分权重、打分表、平分处理规则或演示时长。开发指南提到首轮评审会逐队了解项目。

Luma 列出的讲者与评审：

| 身份 | 姓名及页面职位 |
| --- | --- |
| 讲者、评审 | Brian Verkley — Director, AI Data Platform @ VAST Data |
| 评审 | Abubakr Karali — Senior Solutions Architect @ NVIDIA |
| 评审 | Ram B. — Sr. Developer Advocate @ VAST Data |
| 评审 | Junaid Butt — AI Solutions Engineer @ Weights & Biases |

来源：[Hack Page](https://tokensand.com/vastlondon)、[Luma](https://luma.com/vastlondon)、[VAST 系列活动介绍](https://www.vastdata.com/blog/lets-build-introducing-the-vast-builders-challenge)。

## 4. 奖品与开发额度

### 4.1 比赛奖品

| 奖项      | 已确认信息                                                |
| ------- | ---------------------------------------------------- |
| 第一名     | NVIDIA DGX Spark™                                    |
| 第二名     | Hugging Face Microduck                               |
| 其他列出的奖品 | Luma 写有 Cursor Credits 和 Cash Gift Cards；没有注明金额或对应名次 |
| 分配      | Hack Page 写明两支队伍获得总奖项；credits 和 gift cards 在队员之间分配   |
|         |                                                      |

硬件是否每人一份、其他赞助商是否设独立奖、金额与领取条件，公开页面未明确。

### 4.2 Cursor 开发额度

1. 使用与活动报名一致的邮箱注册 Cursor，建议个人邮箱。
2. 官方开发指南说完成签到的注册者会获得额度；邮件强调应在活动前完成账号注册。
3. 在 [Cursor Usage](https://cursor.com/dashboard/usage) 检查，指南说请求应显示为 `Free`。
4. 没到账或需要追加，用 [Cursor Credits Request](https://forms.gle/AVta9RRTmfdeUNX26)。
5. 表单已打开：必填姓名、个人邮箱、申请原因（未收到 / 需要追加）；团队为选填。未代填或提交。
6. 官方建议 Cursor Agent 模型使用 `Auto` 节省 token；未公布额度金额、有效期或是否覆盖所有模型。

### 4.3 W&B / CoreWeave 推理额度

提前创建 W&B 账号。邮件说明活动开始时提供 serverless inference，需要追加额度时联系现场 Weights & Biases by CoreWeave 团队，以账号邮箱处理。团队云端环境按指南预置 `WANDB_API_KEY`、`WANDB_TEAM`、`WANDB_PROJECT`；本次没有进入你的环境验证。

[原推理文档](https://docs.wandb.ai/inference)现跳转 [CoreWeave Inference 文档](https://docs.coreweave.com/inference)，浏览器已成功读取。文档提供 OpenAI 兼容接口，当前示例 base URL 为 `https://api.inference.wandb.ai/v1`，模型选择与可用配额以现场环境为准。试用入口为 [Forge Inference](https://forge.coreweave.com/inference)。

来源：[官方开发指南](https://github.com/vast-data/vast-builders-challenge)、[额度表单](https://forms.gle/AVta9RRTmfdeUNX26)、[推理文档](https://docs.coreweave.com/inference)、主办方邮件。

## 5. 账号与环境接入

### 5.1 需要的账号

| 账号 | 用途 | 入口 |
| --- | --- | --- |
| VAST Cosmos Community | 访问活动基础设施、发帖求助 | [社区](https://community.vastdata.com/) |
| Cursor | AI 编程、SSH 远程开发、活动额度 | [官网](https://cursor.com/) |
| Weights & Biases | 应用推理及开发工具 | [官网](https://wandb.ai/site/) |
| tokens& | 提交项目 | [提交入口](https://tokensand.com/vastlondon/submit) |
| GitHub | 托管评审可访问的代码 | 提交材料要求 |
| Discord | 找队友、联系参与者和赞助方 | [邀请](https://discord.gg/rPBMhMzRU) |

**名称区分：** Cosmos Community 是 VAST 社区；NVIDIA Cosmos 是视频理解等模型技术，两者不是同一个注册入口。

### 5.2 最新接入流程

1. 注册 Cosmos Community，阅读 [Start here](https://community.vastdata.com/t/vast-builders-challenge-start-here/2102)。
2. 从 [Workshop 接入说明](https://community.vastdata.com/t/about-the-workshop-category-and-access/1969) 进入 [实验环境](https://workshop.thecosmoslabs.com)。本次访问停在 Cloudflare Access 邮箱验证码登录页。
3. 先组队并坐在一起，按主办方分配选择正确队号。指南截图提示队号只能选一次。团队共享 pipeline、索引及凭据。
4. 按实验页面指导配置 SSH，先从终端连通。
5. 在本机 Cursor 开新窗口，选择 **Connect via SSH**，选择实验页面给出的 `bc-<username>` 主机。
6. 打开远程 `vast-builders-challenge` 文件夹。仓库、文件、执行命令和凭据都在 VM 上。
7. 在实验页面打开 **Video Search & Summary**，检查 Search、Explore、Dashboard 三个页面。
8. 可在 Cursor 使用官方提供的 `/build-day-quickstart`，按步骤熟悉环境。

### 5.3 SSH 公钥说明

[10 月 16 日发布的官方 SSH 帖](https://community.vastdata.com/t/generate-public-key-for-cursor-ssh-access/2133) 要求在 Cursor 连接前生成公钥，将公钥粘贴到实验页的 `Option 1 - Key`。帖子使用 ed25519，文件名为 `~/.ssh/id_ed25519_cursor`，macOS 使用 `pbcopy` 复制 `.pub` 文件内容。

本次仅整理说明，没有生成或修改本机密钥。实际主机、用户名、SSH 配置按登录后的实验页操作。

### 5.4 本地要准备什么

带电脑和充电器，官方优先建议个人电脑，避免公司 VPN/IT 限制。**“无需本地设置”应理解为不必自己部署模型与数据平台；最新指南仍需要本机 Cursor 和 SSH 接入准备。**

来源：[官方开发指南](https://github.com/vast-data/vast-builders-challenge)、[准备指南](https://github.com/vast-data/vast-builders-challenge/blob/main/BEFORE_YOU_BUILD.md)、上述社区帖子。

## 6. 技术架构与开发能力

### 6.1 平台负责什么

VAST AI OS 提供视频存储、处理流水线和索引；模型运行在 CoreWeave GPU 上。团队在这些能力之上开发自己的应用、Agent 或仪表盘。

```text
主办方已完成：原始视频 → 切片 → 检测 / 描述 / 向量化 → VastDB 索引
你主要使用：  搜索 / 问答 / 视频读取 → 应用逻辑 → 展示或行动
需要新描述：  已有片段 → 重新检测 / 描述 / 向量化 → 更新索引
```

### 6.2 活动架构文档列出的模型

| 模型 | 用途 | 环境变量 |
| --- | --- | --- |
| Cosmos3-Reason | 描述视频、视频推理 | `COSMOS3_REASON_URL` |
| YOLO11（yolo11s） | 目标检测、类别、边界框 | `YOLO_URL` |
| Cosmos Embed1 | 文本/视觉 embedding，混合搜索 | `COSMOS_EMBED1_URL` |
| Canary-1B | 语音识别、语音翻译；当前 VSS 流水线未接入，需要自行集成 | `CANARY_1B_URL` |

这些是活动仓库所列环境，不代表 NVIDIA 通用文档中的每项能力都已为本场部署。每个模型有独立主机和端口，不要互相推导地址。

### 6.3 常用 Skills

| Skill | 能做什么 |
| --- | --- |
| `retrieval/search` | 按自然语言及筛选条件搜索片段 |
| `retrieval/agent-qa` | 基于视频证据回答问题 |
| `retrieval/videos` | 浏览视频、播放片段、查看描述和检测、总结视频 |
| `retrieval/dashboard` | 查看索引数量与处理状态 |
| `retrieval/suggest-prompts` | 获取搜索建议和近期事件 |
| `retrieval/list-metadata` | 查询实际可用的摄像头、地点、scenario 等值 |
| `ingest/reingest-videos` | 对已索引视频用新提示词重新处理 |
| `ingest/reingest-chunk` | 只重新处理一个 chunk |
| `vastdb-read` | 直接查看数据库内容 |
| `/deploy-app-no-registry` | 在团队 Kubernetes 环境部署应用 |
| `/ask-cosmos` | 生成故障求助说明，由你复制发布到社区 |

Skills 位于官方仓库 `.cursor/skills/`，读取 VM 环境变量。其余变量见本地 [config.example](sources/vast-builders-challenge/config.example)，该文件只有占位符，不需要填入后自行部署。

### 6.4 开发限制与关键注意点

- 使用自己团队的 namespace、bucket、账号和 UI，不访问其他团队资源。
- 模型、数据库和流水线已部署，活动指南要求不要重建 DataEngine 函数或重新部署流水线。
- 参赛环境主要支持对已有、已切片的视频进行 **re-ingest**；架构文档明确说本次挑战不上传新的 chunks、不运行 Segmenter。
- 最新指南明确要求不要导入 YouTube 等互联网视频；提供的视频源已针对授权筛选。
- 大批量 re-ingest 由团队 1–2 人统一负责，避免队员同时重复处理长视频。
- 修改提示词后，必须等待片段重新描述、检测、embedding 和写入索引完成；API 接受请求不等于已可搜索。
- 先查看已有描述是否包含你要的信息，缺失时才重新处理。搜索为空也应检查认证、索引健康和筛选值，不能直接认定素材中不存在该事件。

来源：[开发指南](https://github.com/vast-data/vast-builders-challenge)、[架构参考](https://github.com/vast-data/vast-builders-challenge/blob/main/ARCHITECTURE_REFERENCE.md)。

## 7. 视频数据与选题

以下为官方架构参考列出的数据，不保证你分配到的伦敦团队索引全部已就绪。以实际 Explore / Dashboard 为准，尤其 SF 数据在文档中仍标为待导入。

| 数据组 | 地点 / camera_id | 文档规模 | 可做的方向 |
| --- | --- | --- | --- |
| 高速公路多摄像头 I-24 | `nashville` / `i24_cam-1` | 约 51 个片段 | 变道、拥堵、车辆交互 |
| PIE 行车视频 | `toronto` / `pie_cam-3` | 6 组长视频 | 路口转弯、行人与车辆、道路安全 |
| 社区街道 | `neighborhood` / `neighborhood_cam-1` | 2 天合并视频 | 停车、临停、车辆经过 |
| 旧金山街道 | `san_francisco` / `sf_streets_cam-1` 至 `4` | 4 个摄像头，待导入 | 多摄像头街道活动 |
| 仓库 SDG RGB | `warehouse3` / `sdg_warehouse_cam-2` | 约 178 个短片段 | 叉车接近行人、通道占用 |
| 室内 Smart Spaces | `indoor` / `smartspace_cam-1` | 约 102 个片段 | 人流、通道、设施运营 |

主要筛选字段包括 `camera_id`、`capture_type`、`location`，以及检测的物体类别。数据表中的 Category 是演示分组，不是同名过滤字段。

官方建议先从 Highway Traffic（Pack A）或 Warehouse Safety（Pack C）开始。可先用 `truck changing lanes` 或 `forklift near a person in an aisle` 这类具体描述验证检索，再做界面和后续动作。跨场景搜索可以围绕“人接近移动中的车辆”，但应先确认各数据组已索引。

可选分析 scenario 包括 `surveillance`、`traffic`、`live_driving`、`retail`、`warehouse`、`egocentric`、`sports`、`nhl`、`general`；以 `list-metadata` 实际返回为准。

来源：[架构参考：Video corpus](https://github.com/vast-data/vast-builders-challenge/blob/main/ARCHITECTURE_REFERENCE.md#video-corpus-already-indexed)。

## 8. 开发顺序与故障处理

建议按官方流程完成一个小循环：

1. 检查索引中已有的视频，选一个具体场景。
2. 搜索一个事件，播放返回片段，确认时间戳和画面确实对应。
3. 对同一视频提问，观察带证据的回答。
4. 如果描述缺少关键细节，用少量片段尝试自定义 prompt 的 re-ingest。
5. 等待索引完成，再运行同样搜索并检查结果。
6. 在已有 API 上构建应用，部署后从实验页 **App** 按钮查看。
7. 准备演示视频、仓库和说明，16:30 前提交。

**出问题时：** 官方建议先更新 VM 上预置仓库，再让 Cursor 检查环境健康。搜索为空时检查登录、pipeline 与索引是否匹配、过滤条件是否真实存在。需要求助可运行 `/ask-cosmos` 生成说明，然后到 [Workshop 分区](https://community.vastdata.com/c/workshop/27) 新建主题，写明队号、目标、报错和已尝试的方法，不要直接回复接入说明帖。

参考：[Build Day Guide](https://github.com/vast-data/vast-builders-challenge)、[Workshop 求助说明](https://community.vastdata.com/t/about-the-workshop-category-and-access/1969)。

## 9. 准备与提交清单

### 今天准备

- [ ] 确认 Luma 报名批准/票券。
- [ ] 准备实体政府照片证件、电脑、充电器。
- [ ] 注册 Cosmos Community、Cursor、W&B；Cursor 邮箱与报名一致。
- [ ] 在本机准备好 Cursor，读完 SSH 公钥说明。
- [ ] 加 Discord 找队友，最多 4 人，商定一个具体问题。
- [ ] 阅读官方准备指南及开发指南，保存本地 PDF。
- [ ] 确保可登录 GitHub、tokens&，有分享演示视频的方式。

### 到场后

- [ ] 08:30 左右到场并签到，留意前 100 人的环境名额。
- [ ] 按分配选择正确队号，连通 SSH 和 Video Search & Summary。
- [ ] 确认 Cursor 额度；未收到就填写补领表单。
- [ ] 查看实际可用数据、模型和推理额度。
- [ ] 团队指定 1–2 人负责大批量 re-ingest。
- [ ] 确认评分规则、演示时长、16:30 截止及提交要求。

### 提交前

- [ ] 项目可运行，演示结果能回到具体视频片段核验。
- [ ] 仓库评审可访问，项目说明写清问题、工具和运行方式。
- [ ] 演示视频可分享，链接权限正常。
- [ ] 队员姓名、邮箱完整，可选网站和截图准备好。
- [ ] 在提交页面完成提交，并确认成功状态。

## 10. 链接导航与访问结果

### 10.1 邮件及活动核心入口

| 资源 | 解析后的入口 | 本次结果 |
| --- | --- | --- |
| 活动页 | [Luma](https://luma.com/vastlondon) | 已读取公开活动信息；个人票券未验证 |
| Hack Page | [tokensand.com/vastlondon](https://tokensand.com/vastlondon) | 浏览器成功读取规则、奖项、提交要求及链接 |
| Discord | [discord.gg/rPBMhMzRU](https://discord.gg/rPBMhMzRU) | 短链接解析成功；页面提示打开 Discord，未读取频道内容或加入服务器 |
| Cosmos Community | [community.vastdata.com](https://community.vastdata.com/) | 公开首页及接入/SSH 帖可读 |
| Cursor | [cursor.com](https://cursor.com/) | 官网可读；未登录个人账号 |
| W&B | [wandb.ai/site](https://wandb.ai/site/) | 官网可读；未登录个人账号 |
| 地图 | [邮件地点链接](https://luma.link/q1R2KHGAhj) | 指向 Halkin 的 Google Maps，停在 Cookie 同意页 |
| 项目提交 | [Submit](https://tokensand.com/vastlondon/submit) | 需 Google 或邮箱验证码登录 |
| 项目列表 | [Projects](https://tokensand.com/vastlondon/projects) | 页面未提取到有效项目列表 |
| 云端实验环境 | [Workshop](https://workshop.thecosmoslabs.com) | Cloudflare Access 邮箱验证码登录 |
| Cursor 补领/追加 | [表单](https://forms.gle/AVta9RRTmfdeUNX26) | 已查看字段，未提交 |

原始短链接对应关系：Hack Page `vy4oXPaEZh`；Discord `21zITYgniZ`；Cosmos `4gkItoDDoj`；Cursor `GmmlfgFzwq`；W&B `lcqeNzQsSy`。均为 `https://luma.link/` 下的链接。

### 10.2 先读这些官方资料

| 资料 | 用途 |
| --- | --- |
| [官方开发仓库 / 当天指南](https://github.com/vast-data/vast-builders-challenge) | 接入、Skills、开发、部署、提交与排错 |
| [Before You Build](https://github.com/vast-data/vast-builders-challenge/blob/main/BEFORE_YOU_BUILD.md) | 账号和电脑准备、选题 |
| [Architecture Reference](https://github.com/vast-data/vast-builders-challenge/blob/main/ARCHITECTURE_REFERENCE.md) | 模型、数据流水线、视频组、示例查询 |
| [Community Start Here](https://community.vastdata.com/t/vast-builders-challenge-start-here/2102) | 注册社区及接入导航 |
| [Workshop Access](https://community.vastdata.com/t/about-the-workshop-category-and-access/1969) | 环境入口、接入 PDF、求助方式 |
| [SSH 公钥说明](https://community.vastdata.com/t/generate-public-key-for-cursor-ssh-access/2133) | 本地 Cursor 连接前准备 |
| [VAST 系列活动介绍](https://www.vastdata.com/blog/lets-build-introducing-the-vast-builders-challenge) | 活动背景、系列评审维度 |

### 10.3 技术扩展资料

这些页面已访问或尝试访问。通用产品文档用于查背景和接口，活动环境操作优先以专属仓库为准。

| 资料 | 内容 / 访问结果 |
| --- | --- |
| [VAST AI OS](https://www.vastdata.com/platform/ai-os) | 可读；存储、数据库、DataEngine 等平台组成 |
| [VAST 视频搜索示例](https://www.vastdata.com/blog/unlock-video-intelligence-build-real-time-video-search-and-ai-summary) | 可读；参考架构与视频搜索应用背景，属于较早的通用教程 |
| [NVIDIA VSS 文档](https://docs.nvidia.com/vss/latest/) | 可读；视频搜索、总结、实时分析和 Agent 参考架构 |
| [NVIDIA Cosmos](https://www.nvidia.com/en-us/ai/cosmos/) | 可读；Cosmos 技术介绍 |
| [Ultralytics YOLO11](https://docs.ultralytics.com/models/yolo11) | 可读；检测模型说明 |
| [CoreWeave](https://coreweave.com/) | 可读；GPU 云平台介绍 |
| [Serverless Inference](https://docs.coreweave.com/inference) | 浏览器可读；W&B 原文档重定向至此，OpenAI 兼容 API |
| [W&B Weave](https://wandb.ai/site/weave/) | 可读；Agent 可观测性和评估相关工具 |
| [ARIA](https://www.coreweave.com/products/coreweave-forge/aria) | 可读；Hack Page 原 ARIA 链接重定向至此 |
| [Hack Page 视频概览](https://drive.google.com/file/d/1qUrT0QaBGS6mXxHTEG2vnLM2pT1KY4RD/view?usp=sharing) | 已尝试访问，未取得视频内容，未观看或转录 |
| [准备指南中的另一个概览视频](https://drive.google.com/file/d/1kMiMJCX-4YDmtw8RuRYKg8Pv76dKcC4C/view?usp=sharing) | 官方仓库给出的另一个文件；未观看，不能认定与上一个相同 |

## 11. 信息差异与待确认事项

| 问题 | 不同来源 / 当前处理 |
| --- | --- |
| 提交时间 | GitHub 写 16:30 左右开始 submissions；伦敦 Hack Page 写 16:30 截止。按更早的截止要求准备，现场确认 |
| 本地设置 | 邮件说无需本地 setup；最新指南要求本机 Cursor + SSH。云端平台无需部署，但客户端接入仍要准备 |
| 自带视频 | 系列博客允许带个人素材；当前活动指南禁止导入互联网视频，架构参考限定已有片段 re-ingest。任何新素材接入先向现场确认 |
| 数据可用性 | 架构参考列 6 组，README 正文只概括部分来源，SF 标待导入。按团队实际索引选题 |
| 组队 | 邮件允许单人；Hack Page 推荐至少 2 人、最多 4 人。这是推荐，不把它解读为已禁止单人 |
| 注册截止 | Luma 同时出现 10 月 15 日和活动前一周两种措辞；个人报名是否批准仍需查看票券 |
| 奖项 | Hack Page 明确第一、二名；Luma 另列 credits / gift cards，未给金额和名次映射 |
| 评分与演示 | 已找到系列评审维度，未找到伦敦场权重、演示时长和打分表 |
| 额度及后续使用 | 未公布 Cursor / W&B 金额、过期日、活动后 VM 或应用保留时长 |
| 提交细节 | 登录后的完整表单、是否可以修改、视频时长和文件上限未验证 |
| 其他规则 | 预先写代码的边界、外部服务使用条件、知识产权及是否必须使用每个赞助工具，已访问页面未明确列全 |

## 12. 本地资料归档

主要信息集中在本 README，另保留来源快照便于核查：

- [Hack Page 正文和链接](sources/hack-page.json)
- [Cursor 额度表单正文](sources/credits.json)
- [推理文档正文](sources/inference.json)
- [官方开发指南原文](sources/vast-builders-challenge/README.md)
- [准备指南原文](sources/vast-builders-challenge/BEFORE_YOU_BUILD.md)
- [架构参考原文](sources/vast-builders-challenge/ARCHITECTURE_REFERENCE.md)
- [环境变量占位示例](sources/vast-builders-challenge/config.example)
- [准备指南 PDF](sources/vast-builders-challenge/docs/BEFORE_YOU_BUILD.pdf)
- [开发指南 PDF](sources/vast-builders-challenge/docs/BUILD_DAY.pdf)
- [架构参考 PDF](sources/vast-builders-challenge/docs/ARCHITECTURE_REFERENCE.pdf)
- [基础设施接入 PDF](sources/vast-builders-challenge/docs/BUILDERS-CHALLENGE-INFRA-ONBOARDING.pdf)

PDF 为官方原文件下载，未逐页核对与最新 Markdown 是否一致。旧 `BUILD_DAY.md` 现在仅指向官方 README，阅读当天指南应优先看 README。来源快照是抓取时的页面内容，不是持续同步的数据。

本次已读取公开信息及登录前页面，没有注册账号、加入社区/Discord、提交表单或访问私人实验环境。邮件退订、追踪像素和通用社交/商店页不属于参赛资料整理范围。
