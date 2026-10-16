# 往期视频 Agent 项目观察报告

基于已下载的 74 个仓库 README，最值得优先读的是 **PERJURY、Receipts、Codec Motion、Spore 和 Bountiful**：它们分别把视频理解推进到说法核验、时序记忆、推理成本优化、模型压力测试和商品目录生成。想找现场演示特别好理解的作品，再看 **Hop 24、Shepherd、Understudy 和会躲猫的机器鼠**。

这是一份 README 选题观察，排序依据是想法的区分度、用户与输出是否明确、README 是否讲清证据和边界；不代表获奖排名或实测质量。范围是本地下载快照：扫描了 74 份根目录 README，并补看 9 份项目子目录或补充 README。未审计代码、运行项目、播放视频或验证线上服务。另有 12 个仓库未下载成功，不纳入判断。下文实验数字均为作者在 README 中的自述。

## 1 最值得优先读的五个项目

### 1.1 PERJURY 让每一句关于视频的说法接受核验

**一句话：你说“这个路口有三辆车”，它把句子拆成可检验的断言，再逐条找证据。**

它根据问题选择成本合适的证人：数据库记录、YOLO 检测、既有字幕，或者让 Cosmos 查看多个机位。模型负责提取观察，程序负责最终裁决；证据不足可以明确表示无法证明。README 特别强调，视觉模型收到的是固定、中立的问题，而不是先看到待证明的说法。

我觉得它有趣的地方在于把“视频聊天”变成了一个可检查的裁决流程。演示时可以依次输入一个明显正确、一个明显错误、一个画面无法回答的说法，区别很直观。可以借鉴的是**拆断言、分配证据来源、保留无法判断状态**。

**边界：** README 说原计划的机位数量没有到位，实际只有 3 个机位；要求至少 8 个可用机位的全场景断言会返回无法证明。不能把界面上的多机位陪审团理解成所有机位都已接通。

来源：[本地 README](repos/charliegillet/perjury-vast-builders-challenge/README.md) · [GitHub](https://github.com/charliegillet/perjury-vast-builders-challenge)

### 1.2 Receipts 知道自己的答案什么时候已经过时

**一句话：10:05 出口被挡、10:40 障碍被搬走，它会更新答案，并同时展示新旧证据。**

它把视频转成有时间和来源的结构化事实，以“实体、属性、位置”为键保存。新事实可以取代旧事实，但旧记录仍留在审计链里；录像中断或最后确认时间太久，答案会标记为可能过时。

这是一个很适合 Agent 产品的切口：检索到某个事实，与知道它现在是否仍成立，是两件不同的事。核心时序逻辑用确定性规则和 SQLite，视觉模型只在输入侧提取事实，问题范围也比较容易收窄。

**边界：** README 报告了 25 道合成问题，以及一个真实短片上的 6 道人工标注问题。真实短片实验把同一批人工事实提供给多个系统，主要比较时间处理，不证明视觉提取准确；其中直接观看视频的 Gemini 基线也取得 6/6，不能写成“全面超过大模型”。

来源：[本地 README](repos/HarshShroff/receipts-vast-hack/README.md) · [GitHub](https://github.com/HarshShroff/receipts-vast-hack)

### 1.3 Codec Motion 从视频压缩信息里找便宜的 AI 触发器

**一句话：摄像头编码时已经算过哪些地方在动，先用这些信息决定什么时候值得调用视觉模型。**

它读取 H.264 运动向量和帧大小，对静态画面跳过部分 YOLO 推理；Cosmos 主要在事件发生时运行。视频、检测结果和事件作为不同的 MoQ 轨道传输，消费者可以只订阅轻量事件。

它的区分度来自底层效率：没有再加一个业务看板，而是问“为什么每帧都要付一次 GPU 成本”。README 给出不同场景的对照，也写了没有奏效的区域裁剪实验，值得学它如何讲清优化条件。

**边界：** 作者在白天安静街景上报告检测器耗时节省 75%，但繁忙仓库或公路仍需处理接近全部帧。表中的 100% recall 是相对逐帧检测基线，不是人工标注的真实召回率。移动摄像头、HEVC 和运动噪声也有限制。

来源：[本地 README](repos/kixelated/vast/README.md) · [GitHub](https://github.com/kixelated/vast)

### 1.4 Spore 找到模型盲区 再生成数据去测试它

**一句话：先问视频库缺少什么天气和光照，再造出这些条件，观察 YOLO 和视频推理模型在哪些强度下失效。**

流程包括真实素材覆盖分析、合成变化、模型测量、评估集和训练实验。它把“视频素材库”变成了模型开发工具，而不是只生成检索结果。README 还说把 61 个合成片段送回 VSS，使缺失条件也能被搜索。

最值得学的是它的研究叙事：先证明覆盖缺口，逐步提高干扰强度，再给出失败曲线。和普通稀有场景挖掘相比，它继续追问“找到缺口以后，怎么测试和修复模型”。

**边界：** README 明确披露，小规模合成数据微调并未稳定改善全部测试集，还损伤了干净样本表现；简单 CLAHE 对比度处理在部分指标上更好。因此它更有说服力的定位是**压力测试与评估数据工具**，而不是“合成数据已经修好了模型”。完整流程也依赖事件凭据和数小时计算。

来源：[本地 README](repos/ColemanIsner/SporeLabs-Team16-NYC/README.md) · [GitHub](https://github.com/ColemanIsner/SporeLabs-Team16-NYC)

### 1.5 Bountiful 拍一遍集市 生成可搜索的商品目录

**一句话：用手机走过古董摊、家具街或手工艺市场，之后按描述搜索商品，并跳回它在视频里出现的时刻。**

Cosmos 提取物品、材质、颜色等信息，文本模型把分段观察整理和去重，向量检索负责找到商品对应的视频时刻。它特别适合原本没有在线目录、商品又很独特的商家。

我把它排得靠前，是因为非技术用户也能立刻理解输入、输出和受益人。演示只需要“拍一段 → 生成目录 → 搜到一件东西 → 播放证据”，业务价值和视觉效果都容易讲清。

**边界：** 作者报告 30 秒和 60 秒素材分别得到 20、27 个目录条目，属于两个短例子；没有据此证明大规模商品识别和去重准确率。原素材不随仓库分发；价格区间是模型整理的字段，不能当成商家报价。

来源：[本地 README](repos/MatthewMakesMagic/bountiful-vast/README.md) · [GitHub](https://github.com/MatthewMakesMagic/bountiful-vast)

## 2 同样值得看的七个项目

### 2.1 Shepherd 给小农场的一份鸡舍夜班报告

它把运动摄像头录下的很多鸡舍片段合成少数事件，区分打斗、普通活动和可能的产蛋活动，生成有证据的晨报。README 描述了一次全画面漏掉、局部放大和慢放才看出的暗处打斗。

**有趣之处：** 场景具体、用户真实需求明确；重复片段合并后，输出比“又有东西动了”更有用。它还会检查报告是否虚增数字或修改优先级。

**边界：** 例子只有自家摄像头的 16 段素材；作者披露漏掉了一次啄击。能看到鸡在窝里，不等于看到了鸡蛋。

来源：[README](repos/mahezat/Shepherd/README.md) · [GitHub](https://github.com/mahezat/Shepherd)

### 2.2 Understudy 把专家录像变成实时操作教练

先从专家演示中组织步骤，再看用户摄像头，指出错在哪一步，播放对应专家片段并语音纠正，最后给出过程评分。README 的主现场任务是换帽子，另有杯子金字塔和积木小人。

**有趣之处：** 历史视频变成能指导当前动作的知识库，旧录像和实时反馈之间有直接关系。窄任务的正确、错误、纠正都能现场演出来。

**边界：** README 给出的是几个小任务的原型流程，未展示它对任意复杂技能都有效。真正值得借鉴的是受控任务的步骤检查，而不是“看一次就学会任何工作”。

来源：[README](repos/ToukoUrsin/vast-video-agents-hack/README.md) · [GitHub](https://github.com/ToukoUrsin/vast-video-agents-hack)

### 2.3 Evidence Atlas 给没有 GPS 的行车录像定位

Cosmos 读取街牌、商店名等线索，OpenStreetMap 提供坐标，再用连续行驶时间检查地点是否可能。模型不直接生成经纬度；证据不足的片段可以不上地图。

**有趣之处：** 利用外部地图和速度约束修正模型观察，把一个具体的数据缺失问题做成可复用能力。地图上的每个点都能展开证据链。

**边界：** 作者对不同来源给出不同精度级别；街道或区域级线索不应该伪装成精确位置。它是位置推断原型，README 里的覆盖数量也不是准确率。

来源：[README](repos/antonelli182/evidence-atlas/README.md) · [GitHub](https://github.com/antonelli182/evidence-atlas)

### 2.4 Hop 24 在真实公路录像里玩小鸡过马路

把视频里的 YOLO 框和部分 FastSAM 轮廓变成游戏碰撞几何；小鸡被撞后回放现场，并按车辆描述去其他摄像头检索候选画面。还有一个基于存储检测结果训练的 Q-learning 自动过路策略。

**有趣之处：** 用户先玩，再自然理解视频检测、检索和证据回放。它让一套偏企业的软件能力变成可以上手的互动演示。

**边界：** 撞击是游戏设定；跨摄像头结果是描述相似的候选，不是真实车辆重识别。README 报告策略成功率 40.7% 对规则基线 38.8%，而且是在相同 30 段数据上的对照，不是独立测试。运行时也没有直接调用大模型。

来源：[README](repos/vnmoorthy/hop24/README.md) · [GitHub](https://github.com/vnmoorthy/hop24)

### 2.5 Linger 用街头行为关系回答长椅该放哪里

把公交到站、行人停留、车辆挡路等行为转换为时空事件，用 linkograph 组织关联，再为座椅、照明等公共空间设计提出建议，并说明真实片段支持了哪些可能情景。

**有趣之处：** 多数项目关注事故，它关注日常空间怎样被使用；输出是一个设计决策，而不是一堆告警。

**边界：** README 明确说关联不是因果。离线模式和缓存可用，但演示视频及在线地址仍写着 TBD；不能仅凭 README 判断现场效果。

来源：[README](repos/cassiusp-beep/linger/README.md) · [GitHub](https://github.com/cassiusp-beep/linger)

### 2.6 Sightline 摄像头先看懂环境 再为自己配置任务

先判断摄像头面对仓库、街道还是其他环境，再为相应场景写分析策略和 Cosmos 提示词，扫描候选事件并深入调查。无关的任务会被排除，例如不对不适用的画面强行做行人车辆冲突分析。

**有趣之处：** Agent 的自主性体现在“该关注什么”，而不仅是收到问题以后调用工具。可以学它把环境分类、任务适配和调查过程展示出来。

**边界：** 当前部署是档案回放；距离是图像估计。README 说重新索引队列在活动期间未完成，预览改进不代表索引已经更新。

来源：[README](repos/Soulemane12/sightline/README.md) · [GitHub](https://github.com/Soulemane12/sightline)

### 2.7 RehabNinja 把康复动作做成切水果游戏

患者对着手机做动作，正确重复切水果，特定动作偏差变成炸弹；同一套姿态观察在后台形成临床团队可查看的记录。还配有同伴支持和人工处理升级的界面。

**有趣之处：** 把需要完成的练习和需要采集的测量合到一次互动里，用户得到的是即时游戏反馈。它的产品包装比普通姿态计数器完整。

**边界：** README 明确患者数据是合成的；这是医疗相关原型，游戏演示不能证明临床测量有效性或患者效果。产品同时覆盖患者、同伴和诊所，对一天比赛来说范围较大。

来源：[README](repos/rexbel/Rise/README.md) · [GitHub](https://github.com/rexbel/Rise)

## 3 其他有意思的方向

| 项目 | 有趣的切口 | 阅读时留意 | README |
| --- | --- | --- | --- |
| Every Cat is the Villain | 会躲猫的机器鼠，逃跑录像成为可问答的记忆 | 有硬件、模拟器和云端规划；README 披露部分原型在活动前已写，不宜按纯一天成果估算工作量 | [阅读](repos/robertnowell/every-cat-is-the-villain/README.md) |
| CityPulse | 问城市一个问题，返回六个镜头组成的约 30 秒旁白短片 | 是原片检索和剪辑，重点在“答案是一段视频” | [阅读](repos/flaspa/citypulse/README.md) |
| Raccoon | 用语音找片、看懂、生成改写，再与原片对照 | 生成改写和真实证据要始终区分；依赖的外部服务较多 | [阅读](repos/Gabrielebattimelli/Accident-Scrubber/README.md) |
| FightLens | MMA 动作解释、回放和随比赛变化的胜率显示 | 录像演示含预计算数据；胜率未校准，单个比赛例子不能证明预测准确 | [阅读](repos/maxx1031/fightlens/README.md) |
| Unfold | 骑行视频重建成可探索的 3D 街道，打开风险点背后的画面 | 重建依赖外部服务，几何和停车距离是估计值 | [阅读](repos/Cobeml/unroll-unrest/README.md) |
| EqualEd | 感官过载支持、课堂回看、阅读辅助 | README 有本地运行与托管集成两种描述；未在真实课堂验证，不能概括成整个系统均已离线运行 | [阅读](repos/SashaSkind/EqualEd/README.md) |
| Aloha Circle | 机场里的动作互动仪式，把访客匹配到本地体验 | 当前 README 已加入另一场 hackathon 的网站和 Agent 工作，VAST 项目主要在 kiosk 部分 | [阅读](repos/contingentx/aloha-circle/README.md) |
| Dashi | 站在网约车司机一侧，用录像解释急刹原因、辅助申诉和复盘 | 驾驶员、评分和评论是模拟的，不能理解为已接通平台申诉 | [阅读](repos/vaishnav-16/dashi/README.md) |
| AURAAFIT | 从街景服装观察整理颜色、风格和配件趋势 | README 指应用在 domain 分支；214 次人物出现不是 214 个独立顾客，本地默认分支很小也不代表产品只有几百 token | [阅读](repos/bofrompursuit/vastbuildersteam49/README.md) |
| The Street Talks Back | 把消防栓、自行车道、斑马线拟人化，让街道自己投诉 | 娱乐化界面是亮点；车辆签名和共现不能自动视作可靠身份匹配 | [阅读](repos/sahilpardasani/street-talks-back/README.md) |
| CrossWise | 给配送机器人一个有证据的 GO、WAIT、NO-GO 建议，久等后升级处理 | 回放上的决策支持，没有控制真实机器人过路 | [阅读](repos/sairamveereddy/CROSSWISE/README.md) |
| SafeRoute | 在烟雾、洪水等模拟灾害下重算避难路线 | 街景被放到模拟网格，灾害也是合成效果；不是实际应急导航 | [阅读](repos/koushikvasa/SafeRoute/tools/saferoute/README.md) |
| SecondCall | 用音频锚点、遮罩画面和规则卡复核剑道等运动片段 | 子目录 README 明确实时服务与部署未验证；检索在活动摄取中断时不可用 | [阅读](repos/xkxi/secondcall/tools/secondcall/README.md) |

## 4 同类项目怎样比较

### 4.1 稀有片段挖掘已经有多种版本

Longtail、Edge-Case Miner、Edgecase Finder、Grabbit、Harvest 都围绕“描述场景 → 检索 → 核验 → 导出数据集”。值得看它们各自往后多做了哪一步：

| 项目 | README 中更突出的差异 | 来源 |
| --- | --- | --- |
| ananya-mh/Longtail | 多路检索，按危险和稀有程度排序，覆盖图和版本化数据集 | [README](repos/ananya-mh/Longtail/README.md) |
| chinesepowered/Edge-Case Miner | 扩写多个检索词，视频核验，场景与地点的覆盖缺口 | [README](repos/chinesepowered/hack-vast/README.md) |
| henrihjm/Edgecase Finder | 核验、质量筛选、采集计划；人工批准后重写提示词并重新索引 | [README](repos/henrihjm/edgecase-miner/README.md) |
| Grabbit | 人工确认后才进回归测试集；README 给出 15 次人工复核、9 次确认的具体小样本 | [README](repos/jacobuku/grabbit-mining-co/README.md) |
| Harvest | 用 Cosmos 观察对照 YOLO 检测，整理漏检、误报和类别表缺项 | [README](repos/karanjit-nexovia/harvest/README.md) |
| tossedsalads-scrambledeggs/LongTail | 分摄像头搜索，对字幕和对象做文字判断，再分析检索为何失败 | [README](repos/tossedsalads-scrambledeggs/longtail/README.md) |
| Spore | 从缺口继续做到合成压力测试和修复实验 | [README](repos/ColemanIsner/SporeLabs-Team16-NYC/README.md) |

我的判断：如果只想借鉴一次清楚的小演示，可以读 Grabbit 或 Harvest；如果想找研究性更强的路线，读 Spore。注意“让模型看过实际视频”和“让模型评价已有字幕”是不同的核验强度。

### 4.2 安全看板的亮点通常在证据和后续动作

这批作品里，交通近失、仓库人与叉车、空间占用是反复出现的主题。值得借鉴的具体设计包括：

- **Scribner：** 用绿、黄、红状态和人工拉绳做安灯流程，证据不足时要求人看，不轻易自动恢复绿灯。[README](repos/0-Scribner/Vast-Builders-Challenge-Andon-Factory-Workflow/README.md)
- **Warehouse Ops Copilot：** 先用运动轨迹提候选，再用中立问题、随机对照和多视角减少误报，并检查文字报告里的数字。[项目 README](repos/huixu11/vast-builders-challenge/tools/warehouse-ops/README.md)
- **ViZ Agent：** 从冲突片段走到地点排序和交通工程工单草稿。[README](repos/bhargavchintam/VizAgent/README.md)
- **StreetCast：** 从骑行录像整理出带时间证据的 311 投诉草稿和社区简报，输出贴近使用者工作。[README](repos/muskancellhub/warehouse-guard/README.md)
- **Watchtower：** 保存自然语言告警规则时先跑历史回溯，让用户马上看到“过去会触发多少次”。[项目 README](repos/PriyanshuDangi/vast-challenge/tools/alert-builder/README.md)

这些模式比单纯列出检测框更容易体现产品用途，但不能因为 README 有报告、告警或 webhook 接口，就推断实际下游处置已经发生。

## 5 哪些仓库需要谨慎解读

**根目录还是模板，不等于没有项目。** Warehouse best buddy 的具体说明在 `tools/warehouse-ops/README.md`；OriginX 的子目录介绍 Watchtower；StreetAudit 也有单独 README，且明确当前是 mock 后端。相反，Warehouse Safety Monitor、OmniRoad 等根 README 主要还是通用入门内容，仅据此不足以评价参赛作品。

**当前 README 不一定描述比赛当时状态。** Breadcast 的当前说明是 Gemini 与 Supabase 的多机位直播制作，且写明五手机验证、外网推理与播放仍有待确认；Aloha Circle 当前说明混合了 VAST kiosk 和后续另一场活动的工作。两者可看产品想法，但不能直接当成某次比赛当天的技术清单。

**项目名不一定对应当前内容。** 项目清单里叫 stayin-alive-cpr 的 `yuchia329/crosswatch`，当前 README 讲的是斑马线占用检测和语音警示；LoveCheck 的根 README 则在介绍 VSS 基础设施。报告以下列实际 README 内容为准。

**Mock、回放、预计算与在线运行要分别理解。** SceneTrace 明确赞助商集成尚为 stub；StreetStyle Scout 的浏览器示例是虚构 fixture；Video Gaming Agents 的公开门户加载已打包的成片，不会现场生成新渲染；Sidewalk Pulse 是带证据的静态 MVP，不做可达路线计算。

## 6 对你明天选题最有用的启发

1. **先选择一种用户能拿走的结果。** 商品目录、晨报、核验结论、纠错提示或剪辑成片，都比“能问视频问题”更具体。
2. **让旧录像改变一次当前决策。** Receipts 更新事实、Understudy 对照专家、Sightline 按环境改策略，这些都清楚展示了 Agent 多做的事。
3. **把无法判断和错误例子也做进演示。** PERJURY 的证据不足、Shepherd 的漏检、Spore 的微调失败，都让项目边界更清晰。
4. **按当天条件收窄。** 规则与记忆类通常比机器人硬件、3D 重建、大规模合成训练更容易缩成一天内可展示的流程；这是范围判断，不是对这些仓库的实际开发时间测量。

如果只留一个小时读 README，我会按 **PERJURY → Receipts → Codec Motion → Bountiful → Hop 24** 的顺序；如果你更关注模型研究，就把 **Spore** 放到最前面。

## 7 全部已下载仓库的扫描索引

以下简评只反映 README 能支持的信息。项目名使用参赛清单，说明列以当前 README 为准。

| # | 项目与仓库 | README 简评 |
| ---: | --- | --- |
| 1 | [Scribner](https://github.com/0-Scribner/Vast-Builders-Challenge-Andon-Factory-Workflow) · [README](repos/0-Scribner/Vast-Builders-Challenge-Andon-Factory-Workflow/README.md) | 仓库安灯：人机接近风险、人工复核与红黄绿状态。 |
| 2 | [ADAS Labs](https://github.com/a8nova/ADAS_LABS) · [README](repos/a8nova/ADAS_LABS/README.md) | 用邮箱投递行为区分需要服务的收件箱，生成收集路线。 |
| 3 | [Scenetrace](https://github.com/ad-kat/scenetrace) · [README](repos/ad-kat/scenetrace/README.md) | 视频调查工作台；README 明确当前以 mock 为主，赞助商集成为 stub。 |
| 4 | [LookOut](https://github.com/anagpal18/Vast_Builder_challange) · [README](repos/anagpal18/Vast_Builder_challange/README.md) | 当前 README 名称 ALMOST；轨迹、TTC/PET 冲突分析及时间偏移 what-if，端到端基于模拟数据。 |
| 5 | [Longtail](https://github.com/ananya-mh/Longtail) · [README](repos/ananya-mh/Longtail/README.md) | 稀有场景多路检索、视频核验、危险与稀有程度排序、数据集导出。 |
| 6 | [Warehouse Safety Monitor](https://github.com/ankuagar/vast-builders-challenge) · [README](repos/ankuagar/vast-builders-challenge/README.md) | 根 README 为官方入门模板，缺少项目专属描述。 |
| 7 | [Evidence Atlas](https://github.com/antonelli182/evidence-atlas) · [README](repos/antonelli182/evidence-atlas/README.md) | 读路牌并匹配地图，用行驶连续性过滤不可能的位置。 |
| 8 | [ViZ Agent](https://github.com/bhargavchintam/VizAgent) · [README](repos/bhargavchintam/VizAgent/README.md) | 交通冲突查找、二次核验、地点排序和工程工单草稿。 |
| 9 | [Auraafit](https://github.com/bofrompursuit/vastbuildersteam49) · [README](repos/bofrompursuit/vastbuildersteam49/README.md) | 街景服装与配件分析；README 指应用代码在 domain 分支。 |
| 10 | [Linger](https://github.com/cassiusp-beep/linger) · [README](repos/cassiusp-beep/linger/README.md) | 用行为关系图为座椅、照明等公共空间设计提供建议。 |
| 11 | [Perjury](https://github.com/charliegillet/perjury-vast-builders-challenge) · [README](repos/charliegillet/perjury-vast-builders-challenge/README.md) | 把说法拆成断言，由多类证据及程序作核验裁决。 |
| 12 | [Edge-Case Miner](https://github.com/chinesepowered/hack-vast) · [README](repos/chinesepowered/hack-vast/README.md) | 扩写检索词、视频核验、覆盖缺口与版本化数据集导出。 |
| 13 | [Warehouse Sentinel](https://github.com/Cioran123/warehouse-sentinel) · [README](repos/Cioran123/warehouse-sentinel/README.md) | 多机位仓库安全复核；轨迹提候选、视觉核验、人工事件台账。 |
| 14 | [UnfoldUnrest](https://github.com/Cobeml/unroll-unrest) · [README](repos/Cobeml/unroll-unrest/README.md) | 当前叫 Unfold；骑行画面重建为 3D 街道并链接维护建议证据。 |
| 15 | [Spore](https://github.com/ColemanIsner/SporeLabs-Team16-NYC) · [README](repos/ColemanIsner/SporeLabs-Team16-NYC/README.md) | 找数据覆盖缺口、生成合成变体、压力测试及模型修复实验。 |
| 16 | [Aloha Circle](https://github.com/contingentx/aloha-circle) · [README](repos/contingentx/aloha-circle/README.md) | VAST kiosk 用姿态互动与服装观察匹配本地体验；当前仓库也含另一活动工作。 |
| 17 | [Sentiment Engine](https://github.com/createcontinuem/vastai-hackathon-emilyyuan) · [README](repos/createcontinuem/vastai-hackathon-emilyyuan/README.md) | 融合视频内容与观众反应，找重要时刻并剪片、写简报；有 mock 路径。 |
| 18 | [PharOS](https://github.com/Divyesh-Thirukonda/pharos) · [README](repos/Divyesh-Thirukonda/pharos/README.md) | 曼哈顿地图、事故历史、摄像头和录像审查工作台，区分候选检索与确认观察。 |
| 19 | [Near-Miss Board](https://github.com/donaldc11/eye-watch) · [README](repos/donaldc11/eye-watch/README.md) | 跨摄像头搜索、播放和问答，后端不可用时展示带标识的演示档案。 |
| 20 | [CityPulse](https://github.com/flaspa/citypulse) · [README](repos/flaspa/citypulse/README.md) | 城市问题转成六镜头、约 30 秒的旁白视频答案。 |
| 21 | [Witness desk](https://github.com/freeslugs/witness-desk) · [README](repos/freeslugs/witness-desk/README.md) | 按城市、时间、车型和颜色找候选车辆，人工观看确认后保存案件。 |
| 22 | [Raccoon](https://github.com/Gabrielebattimelli/Accident-Scrubber) · [README](repos/Gabrielebattimelli/Accident-Scrubber/README.md) | 语音检索、视觉理解、生成视频改写与原片对照。 |
| 23 | [StreetStyle Scout](https://github.com/gshost1/streetstyle-scout) · [README](repos/gshost1/streetstyle-scout/README.md) | 可见服装检索和观察保存；浏览器 fixture 与真实后端明确分开。 |
| 24 | [Receipts](https://github.com/HarshShroff/receipts-vast-hack) · [README](repos/HarshShroff/receipts-vast-hack/README.md) | 带时间的事实记忆，更新被新证据取代的答案并标记过时状态。 |
| 25 | [Edgecase Finder](https://github.com/henrihjm/edgecase-miner) · [README](repos/henrihjm/edgecase-miner/README.md) | 核验、质量筛选和导出；可人工批准提示词改写与重新索引。 |
| 26 | [Warehouse best buddy](https://github.com/huixu11/vast-builders-challenge) · [README](repos/huixu11/vast-builders-challenge/tools/warehouse-ops/README.md) | 子 README 为 Warehouse Ops Copilot；安全、闲置和班次报告，含数字核查。 |
| 27 | [Grabbit Mining Co.](https://github.com/jacobuku/grabbit-mining-co) · [README](repos/jacobuku/grabbit-mining-co/README.md) | 危险片段先经人确认再进回归测试集，披露小样本人工复核结果。 |
| 28 | [CrossWatch](https://github.com/jakdemir/vast-builders) · [README](repos/jakdemir/vast-builders/README.md) | 同仓库有 RoadPlay、Link Road、CrossWatch 和 Wind Watch 等应用。 |
| 29 | [Vision Zero Agent](https://github.com/jkfnc/vision-zero-agent-team4) · [README](repos/jkfnc/vision-zero-agent-team4/README.md) | 视频事件触发告警，也报告了公共领域历史影片爆炸检测实验；其他事件未测。 |
| 30 | [Breadcast](https://github.com/joeldsouzax/vast-hackathon) · [README](repos/joeldsouzax/vast-hackathon/README.md) | 当前是 Gemini 与 Supabase 驱动的多机位节目制作；部分跨网络验证待完成。 |
| 31 | [WitnessAI](https://github.com/johaankjis/WitnessAI) · [README](repos/johaankjis/WitnessAI/README.md) | 事故理赔检索台；README 直说原始索引没有标注好的事故素材。 |
| 32 | [Sports Highlighter](https://github.com/jonhpark7966/video-agents-hack) · [README](repos/jonhpark7966/video-agents-hack/README.md) | 当前说明为足球转播式追踪叠加层，README 很短，主要链接计划。 |
| 33 | [Harvest](https://github.com/karanjit-nexovia/harvest) · [README](repos/karanjit-nexovia/harvest/README.md) | 检索并核验训练素材，比较 Cosmos 观察与 YOLO 输出，整理模型缺项和导出数据。 |
| 34 | [Codec Motion](https://github.com/kixelated/vast) · [README](repos/kixelated/vast/README.md) | 借 H.264 运动信息跳过静态画面推理，并按事件调用视觉模型。 |
| 35 | [Video Gaming Agents](https://github.com/klynwuu/tokens-video-agent-hackathon-public) · [README](repos/klynwuu/tokens-video-agent-hackathon-public/README.md) | 公开包是故事编辑门户、录屏与成片；门户加载已保存结果，不重新渲染。 |
| 36 | [Safe Route](https://github.com/koushikvasa/SafeRoute) · [README](repos/koushikvasa/SafeRoute/tools/saferoute/README.md) | 模拟灾害作用于档案街景，再做避险路由；不是实际应急系统。 |
| 37 | [Shepherd](https://github.com/mahezat/Shepherd) · [README](repos/mahezat/Shepherd/README.md) | 鸡舍片段聚合、风险分级和带证据的晨报，含放大及慢放检查。 |
| 38 | [Bountiful](https://github.com/MatthewMakesMagic/bountiful-vast) · [README](repos/MatthewMakesMagic/bountiful-vast/README.md) | 市场走拍视频转成去重的可搜索商品目录，并定位原片时刻。 |
| 39 | [FightLens](https://github.com/maxx1031/fightlens) · [README](repos/maxx1031/fightlens/README.md) | MMA 动作解释和未校准胜率显示，录屏用预计算检测与估计。 |
| 40 | [StreetCast](https://github.com/muskancellhub/warehouse-guard) · [README](repos/muskancellhub/warehouse-guard/README.md) | 骑行视频变成带片段引用的 311 投诉草稿和社区旁白简报。 |
| 41 | [Spatial Video Agent](https://github.com/Paradox07127/Spatial-Video-Agent) · [README](repos/Paradox07127/Spatial-Video-Agent/README.md) | 多摄像头调查工作台，用 3D、地图及测量字段展示断言证据。 |
| 42 | [OriginX](https://github.com/PriyanshuDangi/vast-challenge) · [README](repos/PriyanshuDangi/vast-challenge/tools/alert-builder/README.md) | 子 README 为 Watchtower：自然语言编告警规则，先回溯档案再按片段回放监控。 |
| 43 | [Exhibit A](https://github.com/rajputav/vast_hackathon) · [README](repos/rajputav/vast_hackathon/README.md) | README 主要是初始部署、连通性和简单搜索说明，产品信息不足。 |
| 44 | [RehabNinja](https://github.com/rexbel/Rise) · [README](repos/rexbel/Rise/README.md) | 康复动作游戏、同伴支持和诊所处理界面；患者数据为合成。 |
| 45 | [momentOS](https://github.com/RITIK-12/momentOS) · [README](repos/RITIK-12/momentOS/README.md) | 从驾驶录像生成可解释安全分数，区分风险归因并提供人工争议处理。 |
| 46 | [Every cat is a villain](https://github.com/robertnowell/every-cat-is-the-villain) · [README](repos/robertnowell/every-cat-is-the-villain/README.md) | 机器鼠识猫逃跑，录像成为可问答记忆；包含活动前原型。 |
| 47 | [SideWalkWatcher](https://github.com/Rowan121/sidewalk-pulse) · [README](repos/Rowan121/sidewalk-pulse/README.md) | 当前叫 Sidewalk Pulse；无障碍固定图层叠加临时阻挡证据，静态 MVP。 |
| 48 | [Occlusive Logic](https://github.com/rwezzy/ZoneLogic-Tripwire) · [README](repos/rwezzy/ZoneLogic-Tripwire/README.md) | 当前叫 ZoneLogic；多边形区域、进入/占用/缺席规则和事件复核；内置源为模拟。 |
| 49 | [The Street Talks Back](https://github.com/sahilpardasani/street-talks-back) · [README](repos/sahilpardasani/street-talks-back/README.md) | 街道设施拟人化投诉与访谈，引用字幕证据并可升级为工单。 |
| 50 | [CrossWise](https://github.com/sairamveereddy/CROSSWISE) · [README](repos/sairamveereddy/CROSSWISE/README.md) | 配送机器人过路建议及久等升级，基于档案回放，不控制机器人。 |
| 51 | [EqualEd](https://github.com/SashaSkind/EqualEd) · [README](repos/SashaSkind/EqualEd/README.md) | 感官支持、课堂回看与阅读辅助；阈值未经真实课堂验证。 |
| 52 | [Visual Actions](https://github.com/Sean-Shmulevich/visual-actions-py) · [README](repos/Sean-Shmulevich/visual-actions-py/README.md) | Vim 风格手势语法控制桌面窗口和媒体，记录会话并可用 Cosmos 分析。 |
| 53 | [CloseCall（Sebilopez1）](https://github.com/Sebilopez1/closecall) · [README](repos/Sebilopez1/closecall/README.md) | 交通风险片段、条件允许时估计距离，人工复核并对照盲评。 |
| 54 | [VASTCAM](https://github.com/Sehyeogkim/Video_agent_hackathion_1002) · [README](repos/Sehyeogkim/Video_agent_hackathion_1002/README.md) | 以事前短片预测人与机器碰撞概率，微调决策模型；标签与划分需留意。 |
| 55 | [LoveCheck](https://github.com/Shaibaj01/LoveCheck) · [README](repos/Shaibaj01/LoveCheck/README.md) | 根 README 为 VSS Foundation Stack 部署和架构，缺少 LoveCheck 产品专属介绍。 |
| 56 | [AisleGuard](https://github.com/shaythegay13/mergerisk) · [README](repos/shaythegay13/mergerisk/README.md) | 仓库人车接近调查，使用固定策展历史片段与真实索引元数据。 |
| 57 | [Replay](https://github.com/shuaeb6/replay-safety) · [README](repos/shuaeb6/replay-safety/README.md) | 自然语言安全规则编译、附着摄像头并回放；UI 示例包含人为编写事件。 |
| 58 | [CloseCall（Sidra）](https://github.com/Sidra/closecall-hack) · [README](repos/Sidra/closecall-hack/README.md) | 路口近失记录、模型分诊、证据台账与改造备忘录；仍需工程师复核。 |
| 59 | [Sightline](https://github.com/Soulemane12/sightline) · [README](repos/Soulemane12/sightline/README.md) | 先理解环境，再自动写摄像头分析策略并调查；当前是档案回放。 |
| 60 | [CarWitness 车证](https://github.com/Stephen2077/carwitness) · [README](repos/Stephen2077/carwitness/README.md) | 中英车辆事件搜索、持续规则、证据报告及 AV 场景卡。 |
| 61 | [watcher](https://github.com/Subhradeep246/watcher) · [README](repos/Subhradeep246/watcher/README.md) | 选择公共摄像头，按外观追踪候选并导出有来源和指纹的观察时间线。 |
| 62 | [OmniRoad](https://github.com/ThilakShekharShriyan/vast-builders-challenge) · [README](repos/ThilakShekharShriyan/vast-builders-challenge/README.md) | 根 README 为官方入门模板，缺少作品说明。 |
| 63 | [LongTail](https://github.com/tossedsalads-scrambledeggs/longtail) · [README](repos/tossedsalads-scrambledeggs/longtail/README.md) | 按摄像头找稀有片段，文字模型判断字幕和对象，再解释检索缺口。 |
| 64 | [Understudy](https://github.com/ToukoUrsin/vast-video-agents-hack) · [README](repos/ToukoUrsin/vast-video-agents-hack/README.md) | 从专家录像学习窄任务步骤，看用户操作并给出语音纠正。 |
| 65 | [Drive Recap](https://github.com/tu2090-ops/vast-builders-challenge) · [README](repos/tu2090-ops/vast-builders-challenge/README.md) | 根 README 为官方活动指南，未从项目 README 获得专属功能说明。 |
| 66 | [Dashi](https://github.com/vaishnav-16/dashi) · [README](repos/vaishnav-16/dashi/README.md) | 网约车司机行程复盘、教学和证据申诉；评分及用户资料为模拟。 |
| 67 | [Close-Call Scout](https://github.com/vast-data/vast-builders-challenge) · [README](repos/vast-data/vast-builders-challenge/README.md) | 对应官方 starter 仓库；可学基础设施和活动流程，非独立产品证据。 |
| 68 | [HOP24](https://github.com/vnmoorthy/hop24) · [README](repos/vnmoorthy/hop24/README.md) | 真实交通录像成为过路游戏；检测几何、证据回放、候选车辆搜索和小型 RL。 |
| 69 | [SecondCall](https://github.com/xkxi/secondcall) · [README](repos/xkxi/secondcall/tools/secondcall/README.md) | 运动视频判罚复核、音频锚点和证据；子 README 说明在线服务未验证。 |
| 70 | [Vastly Unspoken](https://github.com/yb235/yb235-vast-builders-challenge-team24-0cbe60d) · [README](repos/yb235/yb235-vast-builders-challenge-team24-0cbe60d/training/README.md) | training README 是 Yield-or-proceed 逻辑回归基线，学 Cosmos 字幕标签，非机器人策略。 |
| 71 | [stayin-alive-cpr](https://github.com/yuchia329/crosswatch) · [README](repos/yuchia329/crosswatch/README.md) | 当前 README 为 Crosswatch：检测斑马线占用、语音警示及事件问答。 |
| 72 | [traffic-police](https://github.com/yugt/traffic-police) · [README](repos/yugt/traffic-police/README.md) | 当前叫 Evidence Review：固定规则卡评估检索证据，人工决定与模型判断分开存储。 |
| 73 | [ghost-nyc](https://github.com/zglyn/Vast-builders-challenge) · [README](repos/zglyn/Vast-builders-challenge/tools/bike-app/README.md) | 子 README 显示 GHOST what-if 展示及 bike/risk/futures 界面；项目说明有限。 |
| 74 | [StreetAudit](https://github.com/zuther77/vast-builder-challenge-hackthon) · [README](repos/zuther77/vast-builder-challenge-hackthon/tools/road-marking-audit/README.md) | 道路标线缺失/磨损审计；子 README 明确当前是 mock，真实适配器仍有待接入。 |
