# 往期仓库代码 Token 统计

使用本地 tiktoken 的 `o200k_base` 编码器，对每个源码文件分别分词后求和。没有调用模型 API，也没有执行下载的项目代码。

## 统计口径

- 完全跳过 `.git`，不读取 Git 历史或元数据。
- 只计算支持的源码扩展名及 Dockerfile、Makefile 等构建脚本；包含源文件中的注释、字符串和空白。
- Notebook 只计算 code cells，排除输出、Markdown 和 Notebook 元数据。
- 排除依赖目录、Python 虚拟环境（包括自定义名称）、缓存、常见构建目录及明显的压缩/打包/生成文件。
- 排除 Markdown/README、JSON/YAML/TOML 配置、锁文件、数据集、图片、音视频和其他二进制文件。
- 这是本地当前版本全部符合规则的代码量；可能包含测试、重复代码和随项目复制的基础模板，不等于作者原创代码量。未被规则识别的第三方或生成代码仍可能计入。
- token 数是所选编码器的实际计数；其他模型的 tokenizer 可能不同。拼接文件名、提示词和工具包装会额外增加上下文 token。
- 额外排除已识别的纯 JSON 赋值型 JavaScript 数据文件、slides.html 等演示文稿；移除源码内嵌 data URL 的 Base64 媒体载荷，保留其余代码。代码字节数和行数均按处理后的文本统计。
- 下载失败的仓库标记为不可统计，不能当成零代码。

## 汇总

- 已统计：**74 个仓库**；另有 **12 个未下载成功**。
- 代码文件：**2,679**；代码行数：**475,171**。
- 代码 UTF-8 文本大小：**21.44 MiB**。
- 合计：**6,154,699 tokens（6.155M）**。
- 每仓库平均：**83,172 tokens**；中位数：**53,528 tokens**。
- 读取/解析失败文件：**0**（详见 JSON 的 errors）。

[仓库 CSV](code-token-counts.csv) · [逐文件明细](code-token-files.csv) · [完整规则及 JSON](code-token-counts.json)

## 各仓库（按 token 数降序）

| 仓库 | 项目 | 代码文件 | 代码行数 | Token |
| --- | --- | ---: | ---: | ---: |
| [Paradox07127/Spatial-Video-Agent](https://github.com/Paradox07127/Spatial-Video-Agent) | Spatial Video Agent | 270 | 48,339 | **721,150** |
| [joeldsouzax/vast-hackathon](https://github.com/joeldsouzax/vast-hackathon) | Breadcast | 95 | 22,218 | **325,673** |
| [Shaibaj01/LoveCheck](https://github.com/Shaibaj01/LoveCheck) | LoveCheck | 201 | 37,715 | **304,061** |
| [Sean-Shmulevich/visual-actions-py](https://github.com/Sean-Shmulevich/visual-actions-py) | Visual Actions | 145 | 24,033 | **289,418** |
| [rexbel/Rise](https://github.com/rexbel/Rise) | RehabNinja | 211 | 23,658 | **263,200** |
| [charliegillet/perjury-vast-builders-challenge](https://github.com/charliegillet/perjury-vast-builders-challenge) | Perjury | 77 | 18,046 | **262,701** |
| [ColemanIsner/SporeLabs-Team16-NYC](https://github.com/ColemanIsner/SporeLabs-Team16-NYC) | Spore | 61 | 11,492 | **162,562** |
| [contingentx/aloha-circle](https://github.com/contingentx/aloha-circle) | Aloha Circle | 91 | 15,578 | **162,401** |
| [Soulemane12/sightline](https://github.com/Soulemane12/sightline) | Sightline | 38 | 13,043 | **156,652** |
| [anagpal18/Vast_Builder_challange](https://github.com/anagpal18/Vast_Builder_challange) | LookOut | 78 | 10,441 | **141,476** |
| [zglyn/Vast-builders-challenge](https://github.com/zglyn/Vast-builders-challenge) | ghost-nyc | 33 | 11,784 | **139,069** |
| [huixu11/vast-builders-challenge](https://github.com/huixu11/vast-builders-challenge) | Warehouse best buddy | 29 | 8,513 | **131,417** |
| [Cioran123/warehouse-sentinel](https://github.com/Cioran123/warehouse-sentinel) | Warehouse Sentinel | 108 | 12,396 | **131,317** |
| [maxx1031/fightlens](https://github.com/maxx1031/fightlens) | FightLens | 38 | 8,583 | **125,277** |
| [johaankjis/WitnessAI](https://github.com/johaankjis/WitnessAI) | Witness — AI-Powered Video Evidence Intelligence | 106 | 11,558 | **118,306** |
| [HarshShroff/receipts-vast-hack](https://github.com/HarshShroff/receipts-vast-hack) | Receipts | 44 | 9,210 | **114,394** |
| [SashaSkind/EqualEd](https://github.com/SashaSkind/EqualEd) | EqualEd | 27 | 6,863 | **107,532** |
| [Cobeml/unroll-unrest](https://github.com/Cobeml/unroll-unrest) | UnfoldUnrest | 43 | 5,550 | **98,198** |
| [ToukoUrsin/vast-video-agents-hack](https://github.com/ToukoUrsin/vast-video-agents-hack) | Understudy | 50 | 7,621 | **89,964** |
| [rwezzy/ZoneLogic-Tripwire](https://github.com/rwezzy/ZoneLogic-Tripwire) | Occlusive Logic | 44 | 5,904 | **88,598** |
| [0-Scribner/Vast-Builders-Challenge-Andon-Factory-Workflow](https://github.com/0-Scribner/Vast-Builders-Challenge-Andon-Factory-Workflow) | Scribner | 50 | 8,788 | **88,063** |
| [yuchia329/crosswatch](https://github.com/yuchia329/crosswatch) | stayin-alive-cpr | 4 | 1,967 | **87,422** |
| [xkxi/secondcall](https://github.com/xkxi/secondcall) | SecondCall | 43 | 4,923 | **84,441** |
| [Divyesh-Thirukonda/pharos](https://github.com/Divyesh-Thirukonda/pharos) | PharOS | 26 | 3,760 | **74,731** |
| [shuaeb6/replay-safety](https://github.com/shuaeb6/replay-safety) | Replay | 32 | 5,153 | **73,136** |
| [PriyanshuDangi/vast-challenge](https://github.com/PriyanshuDangi/vast-challenge) | OriginX | 19 | 8,282 | **72,796** |
| [jonhpark7966/video-agents-hack](https://github.com/jonhpark7966/video-agents-hack) | Sports Highlighter | 20 | 5,885 | **69,841** |
| [Sidra/closecall-hack](https://github.com/Sidra/closecall-hack) | CloseCall | 59 | 4,586 | **68,840** |
| [chinesepowered/hack-vast](https://github.com/chinesepowered/hack-vast) | Edge-Case Miner | 12 | 4,995 | **68,186** |
| [muskancellhub/warehouse-guard](https://github.com/muskancellhub/warehouse-guard) | StreetCast | 11 | 4,066 | **65,552** |
| [Gabrielebattimelli/Accident-Scrubber](https://github.com/Gabrielebattimelli/Accident-Scrubber) | Raccoon | 47 | 5,575 | **63,780** |
| [bhargavchintam/VizAgent](https://github.com/bhargavchintam/VizAgent) | Group 20 (ViZ Agent) | 19 | 4,778 | **61,331** |
| [MatthewMakesMagic/bountiful-vast](https://github.com/MatthewMakesMagic/bountiful-vast) | Bountiful | 15 | 3,488 | **61,314** |
| [jakdemir/vast-builders](https://github.com/jakdemir/vast-builders) | CrossWatch | 28 | 5,415 | **59,362** |
| [gshost1/streetstyle-scout](https://github.com/gshost1/streetstyle-scout) | StreetStyle Scout | 24 | 5,110 | **58,066** |
| [mahezat/Shepherd](https://github.com/mahezat/Shepherd) | Shepherd | 25 | 3,284 | **56,037** |
| [henrihjm/edgecase-miner](https://github.com/henrihjm/edgecase-miner) | Edgecase Finder | 22 | 3,956 | **55,137** |
| [Subhradeep246/watcher](https://github.com/Subhradeep246/watcher) | watcher | 39 | 6,195 | **51,918** |
| [vnmoorthy/hop24](https://github.com/vnmoorthy/hop24) | HOP24 | 8 | 2,639 | **51,566** |
| [sairamveereddy/CROSSWISE](https://github.com/sairamveereddy/CROSSWISE) | CrossWise | 14 | 2,694 | **47,996** |
| [karanjit-nexovia/harvest](https://github.com/karanjit-nexovia/harvest) | Harvest | 14 | 2,785 | **47,368** |
| [jkfnc/vision-zero-agent-team4](https://github.com/jkfnc/vision-zero-agent-team4) | Vision Zero Agent | 20 | 2,811 | **47,150** |
| [flaspa/citypulse](https://github.com/flaspa/citypulse) | CityPulse | 14 | 3,276 | **46,385** |
| [yb235/yb235-vast-builders-challenge-team24-0cbe60d](https://github.com/yb235/yb235-vast-builders-challenge-team24-0cbe60d) | Vastly Unspoken | 5 | 3,519 | **43,591** |
| [sahilpardasani/street-talks-back](https://github.com/sahilpardasani/street-talks-back) | The Street Talks Back | 11 | 2,777 | **41,969** |
| [antonelli182/evidence-atlas](https://github.com/antonelli182/evidence-atlas) | Evidence Atlas | 5 | 2,601 | **39,963** |
| [robertnowell/every-cat-is-the-villain](https://github.com/robertnowell/every-cat-is-the-villain) | Every cat is a villain in its own story | 22 | 2,178 | **39,790** |
| [klynwuu/tokens-video-agent-hackathon-public](https://github.com/klynwuu/tokens-video-agent-hackathon-public) | 🎮Video G(ame it) Agent — Your Footage, Now in Story Mode - Team 23 | 20 | 1,010 | **38,942** |
| [Sebilopez1/closecall](https://github.com/Sebilopez1/closecall) | CloseCall | 8 | 2,552 | **38,757** |
| [koushikvasa/SafeRoute](https://github.com/koushikvasa/SafeRoute) | Safe Route | 14 | 2,750 | **36,601** |
| [zuther77/vast-builder-challenge-hackthon](https://github.com/zuther77/vast-builder-challenge-hackthon) | StreetAudit | 12 | 3,861 | **36,319** |
| [cassiusp-beep/linger](https://github.com/cassiusp-beep/linger) | Linger | 22 | 2,472 | **35,362** |
| [ananya-mh/Longtail](https://github.com/ananya-mh/Longtail) | Longtail | 10 | 2,257 | **34,876** |
| [RITIK-12/momentOS](https://github.com/RITIK-12/momentOS) | momentOS | 16 | 2,157 | **34,630** |
| [rajputav/vast_hackathon](https://github.com/rajputav/vast_hackathon) | Exhibit A | 7 | 2,534 | **31,169** |
| [vaishnav-16/dashi](https://github.com/vaishnav-16/dashi) | Dashi | 10 | 2,207 | **31,122** |
| [ankuagar/vast-builders-challenge](https://github.com/ankuagar/vast-builders-challenge) | Warehouse Safety Monitor | 3 | 2,203 | **30,715** |
| [tu2090-ops/vast-builders-challenge](https://github.com/tu2090-ops/vast-builders-challenge) | Drive Recap | 17 | 3,181 | **27,264** |
| [freeslugs/witness-desk](https://github.com/freeslugs/witness-desk) | Witness desk | 29 | 2,780 | **26,135** |
| [Stephen2077/carwitness](https://github.com/Stephen2077/carwitness) | CarWitness 车证 | 5 | 1,860 | **24,686** |
| [kixelated/vast](https://github.com/kixelated/vast) | Codec Motion | 20 | 1,738 | **22,855** |
| [Sehyeogkim/Video_agent_hackathion_1002](https://github.com/Sehyeogkim/Video_agent_hackathion_1002) | VASTCAM | 11 | 2,257 | **21,034** |
| [shaythegay13/mergerisk](https://github.com/shaythegay13/mergerisk) | AisleGuard | 8 | 1,996 | **20,269** |
| [donaldc11/eye-watch](https://github.com/donaldc11/eye-watch) | Near-Miss Board | 8 | 1,460 | **16,141** |
| [ad-kat/scenetrace](https://github.com/ad-kat/scenetrace) | Scenetrace | 24 | 1,936 | **14,526** |
| [jacobuku/grabbit-mining-co](https://github.com/jacobuku/grabbit-mining-co) | Grabbit Mining Co. | 4 | 998 | **14,231** |
| [yugt/traffic-police](https://github.com/yugt/traffic-police) | traffic-police | 4 | 1,036 | **13,114** |
| [a8nova/ADAS_LABS](https://github.com/a8nova/ADAS_LABS) | ADAS Labs - Carrier Route Optimization | 2 | 1,137 | **13,085** |
| [createcontinuem/vastai-hackathon-emilyyuan](https://github.com/createcontinuem/vastai-hackathon-emilyyuan) | Sentiment Engine | 15 | 1,136 | **12,047** |
| [tossedsalads-scrambledeggs/longtail](https://github.com/tossedsalads-scrambledeggs/longtail) | LongTail | 4 | 809 | **8,827** |
| [Rowan121/sidewalk-pulse](https://github.com/Rowan121/sidewalk-pulse) | SideWalkWatcher | 3 | 54 | **6,861** |
| [vast-data/vast-builders-challenge](https://github.com/vast-data/vast-builders-challenge) | Close-Call Scout | 3 | 512 | **3,889** |
| [ThilakShekharShriyan/vast-builders-challenge](https://github.com/ThilakShekharShriyan/vast-builders-challenge) | OmniRoad | 2 | 218 | **1,772** |
| [bofrompursuit/vastbuildersteam49](https://github.com/bofrompursuit/vastbuildersteam49) | Auraafit | 1 | 29 | **373** |

## 无法统计的仓库

| 仓库 | 原因 |
| --- | --- |
| [angu10/invoice-video-agent](https://github.com/angu10/invoice-video-agent) | 未下载成功 |
| [Ghatage/freezeframe](https://github.com/Ghatage/freezeframe) | 未下载成功 |
| [jamie-roberts-dev/wahz](https://github.com/jamie-roberts-dev/wahz) | 未下载成功 |
| [JohnYangSam/vast-builders-challenge](https://github.com/JohnYangSam/vast-builders-challenge) | 未下载成功 |
| [labcc/robo-obs](https://github.com/labcc/robo-obs) | 未下载成功 |
| [manvendersingh21/WORLDSTATE](https://github.com/manvendersingh21/WORLDSTATE) | 未下载成功 |
| [meneramandarin/fountain](https://github.com/meneramandarin/fountain) | 未下载成功 |
| [publu/matcha-vast](https://github.com/publu/matcha-vast) | 未下载成功 |
| [raj978/vast-builders-challenge](https://github.com/raj978/vast-builders-challenge) | 未下载成功 |
| [TurpoFIN/unitproof](https://github.com/TurpoFIN/unitproof) | 未下载成功 |
| [Vontarius-Ventures/WorldCompiler](https://github.com/Vontarius-Ventures/WorldCompiler) | 未下载成功 |
| [wilsonwongxyz/vast-builders-challenge](https://github.com/wilsonwongxyz/vast-builders-challenge) | 未下载成功 |

## 复算

在安装了 `tiktoken` 的 Python 环境运行：

```sh
python scripts/count_repo_code_tokens.py
```
