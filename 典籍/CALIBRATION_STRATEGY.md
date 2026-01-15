# 典籍精校策略总览（CALIBRATION_STRATEGY）

本文件定义 LucidSelf「典籍精校」的**执行策略**与**优先级**：用一张张“精校卡”直接产出可被推理引擎消费的资产（因子 / 规则草案 / 叙事素材 / 跨体系映射 / 术语对齐），并在 26 本典籍之间编织可互证、可复用的网络。

---

## 0. 统一产出与落盘位置（强约束）

- **书籍目录保持纯净**：每本典籍目录只保留 `原文/`（以及必要的原始备份，如 `source_backup/`），不保留任何精校产出或中间文件。
- **精校产出统一落盘**：全部写入 `典籍/calibrated/`：
  - `cards/`：精校卡（每条原文/最小语义单元一张卡）
  - `factors/`：按书汇总的因子清单（可由卡聚合生成）
  - `rules/`：按书汇总的规则草案（可由卡聚合生成）
  - `narratives/`：按书汇总的叙事素材库（可由卡聚合生成）
  - `mappings/`：跨体系映射表（可由卡聚合生成）
  - `glossary/`：术语对齐表（可由卡聚合生成）

---

## 1. 26 本典籍策略总表（W0 角色 / Phase / 产出重点）

> `book_abbr` 用于 `card_id / rule_id_draft / narrative_id` 的统一前缀（全小写、无空格）。

| book_abbr | 书名 | 语言 | 领域 | WorldGrid-W0 角色 | 预估条目数量（卡） | 精校优先级 | 关键产出说明 |
|---|---|---|---|---|---:|---|---|
| zpzq | 子平真诠 | 中 | 命理（八字） | 主干 | 200–350 | Phase 1 | 用神/格局/喜忌/行运的“规则骨架”，高密度规则草案与术语对齐 |
| smth | 三命通会 | 中 | 命理（八字） | 主干 | 900–1500 | Phase 1 | 五行/干支/神煞/岁运等“大全型补证”，大量可互证规则与例证叙事片段 |
| dts | 滴天髓（阐微/辑要） | 中 | 命理（八字） | 主干 | 250–450 | Phase 1 | 五行气势/体用/旺衰等“中立标签来源”，适合抽象语义与跨体系映射 |
| mlxj | 梦林玄解 | 中 | 梦学 | 主干 | 800–1400 | Phase 1 | 梦象 → 语义标签 → 叙事素材的主干字典；梦占/梦禳/梦原/梦征分层落盘 |
| inner_sky | The Inner Sky | 英 | 占星 | 主干 | 500–900 | Phase 1 | 现代心理占星的“解释框架”，重点产出可触发叙事素材与规则草案 |
| tetr | Tetrabiblos | 英 | 占星 | 主干 | 700–1100 | Phase 1 | 占星基础概念（行星/宫位/相位/气质）与预测原则，建立跨书术语基线 |
| astro_houses | The Astrological Houses | 英 | 占星 | 主干 | 200–350 | Phase 1 | 12 宫语义主干：宫位→生命领域映射；强绑定中立标签与 narrative 复用 |
| planets_transit | Planets in Transit | 英 | 占星 | 主干 | 900–1400 | Phase 1 | 行运触发网络：`temporal` 因子 + 规则草案 + 叙事素材（强可执行前置） |
| interp_dreams | The Interpretation of Dreams | 英 | 梦学 | 主干 | 1200–2000 | Phase 1 | 梦的机制/梦工作/愿望满足：抽象因子与心理维度规则（高价值共通标签） |
| jung_archetypes | The Archetypes and the Collective Unconscious | 英 | 心理学 | 主干 | 900–1400 | Phase 1 | 原型/情结/个体化：梦学与叙事层的“心理语义底座”与术语对齐 |
| dreams_visions | The Dreams & Visions Symbol Dictionary | 英 | 梦学 | 主干 | 1000–1600 | Phase 1 | 梦象词典（宗教语境明显）：优先抽取可中性化的梦象→语义标签映射 |
| qtbj | 穷通宝鉴 | 中 | 命理（八字） | 补充 | 350–650 | Phase 2 | 月令/季节-天干组合的细粒度规则库，强化 `temporal/season` 因子网络 |
| yhzp | 渊海子平 | 中 | 命理（八字） | 补充 | 800–1400 | Phase 2 | 十神/六亲/疾病/岁运等条目化断法，适合批量规则草案化与冲突矩阵素材 |
| zgjm | 周公解梦类 | 中 | 梦学 | 补充 | 600–900 | Phase 2 | 高频生活梦象补全，与梦林玄解互证；叙事素材可直连 Playbook |
| yijing | 周易及传 | 中 | 义理/象数 | 补充 | 500–900 | Phase 2 | 卦象→处境→决策语义标签库（不做硬占断），为中立标签与叙事素材供能 |
| jzyh | 记纂渊海 | 中 | 类书/背景 | 补充 | 800–1200 | Phase 2 | 天文/岁时/灾异/性行人伦等“语义背景库”，为梦象与心理标签提供语料 |
| christian_astro | Christian Astrology (vol.1&2) | 英 | 占星 | 补充 | 500–900 | Phase 2 | 传统技法与判读口径（宫位/行星/尊贵/推断考虑），补齐规则表达多样性 |
| astro_personality | Astrology of Personality | 英 | 占星 | 补充 | 900–1400 | Phase 2 | 占星×心理学解释框架，强化 neutral_tags 与 psych 因子映射密度 |
| llewellyn_dreams | Llewellyn’s Complete Dictionary of Dreams | 英 | 梦学 | 补充 | 800–1200 | Phase 2 | 通用梦象词典：快速加密 dream 因子覆盖面（以中立标签去宗教化） |
| zwds | 紫微斗数全书 | 中 | 命理（扩展） | 扩展 | 400–700 | Phase 3 | 星曜/宫位象征体系（扩展网络密度），优先抽“中立语义”而非专门排盘细节 |
| waite_key | Waite Pictorial Key to the Tarot | 英 | 塔罗 | 扩展 | 300–600 | Phase 3 | 大小阿卡那语义与占断句库：高复用叙事素材 + tarot→psych 映射 |
| pictorial_key | The Pictorial Key to the Tarot | 英 | 塔罗 | 扩展 | 300–600 | Phase 3 | 当前仓库可与 `waite_key` 视为同源版本（如后续补齐文本再拆分） |
| thoth | The Book of Thoth | 英 | 塔罗 | 扩展 | 600–1000 | Phase 3 | Thoth 牌义与对应体系（元素/行星/黄道等），为 tarot↔astro↔psych 提供桥梁 |
| 78_degrees | 78 Degrees of Wisdom | 英 | 塔罗 | 扩展 | 200–400 | Phase 3 | 结构化旅程叙事（原型序列）：用于 Playbook 生成的“主干叙事骨架” |
| learning_tarot | Learning the Tarot | 英 | 塔罗 | 扩展 | 400–700 | Phase 3 | 解读方法与常用牌阵语义：抽“触发条件 + 叙事句”而非教学流程文本 |
| jung_collected | The Collected Works of C.G. Jung | 英 | 心理学 | 扩展 | 3000–6000 | Phase 3 | 超大体量：以“核心概念/原型/机制”抽取为主，按主题分批推进 |

---

## 2. 每本书的精校粒度指南（P0–P3）

说明：
- **P0**：核心条目，全量精校（卡内 A–F 全部产出）。
- **P1**：主干条目，标准精校（卡内 A–F 全部产出；允许减少映射数量但不为空）。
- **P2**：背景条目，简化精校（规则草案可少；叙事素材与术语对齐仍需覆盖关键点）。
- **P3**：参考条目，仅保留原文索引（只做 A 段 `card_id/source_anchor/source_text/priority`；其余段可留空）。

### 2.1 中文典籍（命理）

#### 子平真诠（zpzq）
- P0：一．论十干十二支；二、论阴阳生克；三、论阴阳生死；八、论用神（含九～十六）；二十五～二十八（行运/喜忌）。
- P1：三十一～四十六（正官/财/印绶/食神/偏官/伤官/阳刃/建禄月劫及取运）。
- P2：十七、墓库刑冲；十八～二十四（四吉神/四凶神/六亲中的妻子等）与四十七、杂格。
- P3：序与附录性引文（仅索引）。

#### 三命通会（smth）
- P0：卷一（五行生成/生克/干支源流/纳音总论与取象/六十甲子性质吉凶）；卷二（天干阴阳生死/四时节气/旺相休囚死/大运小运太岁岁运/六合三合刑害冲击）；卷三（禄马/天乙贵人/三奇/天月德/学堂词馆/空亡羊刃/诸神煞总论）；卷四（十干坐支兼得月时及行运吉凶；十二月支得日干吉凶）。
- P1：后续卷中与“格局/用神/喜忌/运程/命例（可复用的结构化例证）”直接相关章节（按目录标题含这些关键词全量）。
- P2：冷门神煞细碎条、重复引文与大段文辞性铺陈（以能否抽出稳定因子/规则为准）。
- P3：序跋、版本说明与纯索引段落。

#### 滴天髓（dts）
- P0：通天论；天干论（甲～癸）；地支论；形象论；方局论；格局论；从化论（真/假）；岁运论；体用论；衰旺论；中和论；寒暖论；月令论。
- P1：精神论/刚柔论/顺逆论/源流论/通隔论/清浊论/真假论/隐显论/众寡论/奋郁论/恩怨论/顺反论/战合论/君臣论/母子论/才德论/性情论。
- P2：疾病论/六亲论/出身论/地位论/贵贱贫富吉凶寿夭论等应用段（只要能落为因子与触发叙事即可）。
- P3：提要、说明性材料。

#### 穷通宝鉴（qtbj）
- P0：五行总论；十干分论（甲～癸）及“四季/三春三夏三秋三冬”分段（按目录全量）。
- P1：论木/论火/论土/论金/论水（抽象规则与季节/气候因子）。
- P2：重复性解说段（仅保留能抽新因子/新规则者）。
- P3：版本说明与索引段。

#### 渊海子平（yhzp）
- P0：论日为主；论月令；论大运；论太岁吉凶/征太岁；十神主干（伤官/食神/正财/正官/七杀/印绶/倒食/劫财/阳刃等）。
- P1：六亲总篇及父母/兄弟/妻妾/子息；疾病/性情；女命总诀与女命富贵贫贱篇。
- P2：赋/歌/口诀类（喜忌篇、心镜歌、妖祥赋等）——以能否抽规则与叙事素材为准。
- P3：纯堆叠条目、低复用材料（仅索引）。

### 2.2 中文典籍（梦学 / 义理 / 类书）

#### 梦林玄解（mlxj）
- P0：梦占（卷一～卷二十六）：优先天象部、地理部、人物部、形貌部、政事部、栋宇部、服饰/饮食/飞走等高频梦象门类。
- P1：梦禳（卷二十七～卷二十八）：以“趋避/化解”的条件触发句为主，转写为规则草案与叙事素材（避免宗教化措辞，改用中立标签）。
- P2：梦原（卷二十九）：提炼“梦的机制/心性/情志”因子与中立标签映射。
- P3：梦征（卷三十～卷三十四）：以历史梦例作为索引与证据库（只保留锚点与最小引用）。

#### 周公解梦类（zgjm）
- P0：身体面目齿发；夫妻产孕交欢；哀乐病死歌唱；被害斗伤打骂；捕禁刑罚狱具；饮食酒肉瓜菜；门户井灶厨厕；道路桥梁市集；龙蛇禽兽等类。
- P1：天地日月星辰；地理山石树木；宫室屋宇仓库；金银珠玉绢帛；田园五榖耕种等。
- P2：器物细分类目（镜环钗钏、梳篦、卤簿等）与低频条。
- P3：诗序与杂项说明。

#### 周易及传（yijing）
- P0：乾、坤及其彖/象/文言；十翼中与“处境—抉择—德性—风险”直接相关的段落（如系辞要点、象传要点）。
- P1：其余卦的卦辞/爻辞（按卦序；每爻可视为独立卡的原文单元）。
- P2：注疏性的延展解释（如王弼注中可抽出稳定语义者）。
- P3：序跋、版本材料与纯训诂段。

#### 记纂渊海（jzyh）
- P0：天道/天文相关门类；岁时节令；灾异/祥瑞；性行/人伦议论（为梦学与心理学提供中立语义背景）。
- P1：地理山川与郡县门类（只抽可复用的“地域—象征—风险/资源”语义）。
- P2：物类门（草木虫鱼器物）中可复用的“象征性定义”条。
- P3：堆叠引文与纯文采段（仅索引）。

### 2.3 西方典籍（占星）

#### The Inner Sky（inner_sky）
- P0：Part Two（Signs/Planets/Houses）；Part Three（Interpretation I/II/III：组合解释方法）。
- P1：Part One（Why Bother?/Symbolic Language/What Exactly Is a Birthchart?）。
- P2：Chapter 11–12（偏哲学/散文性章节，保留可抽中立标签者）。
- P3：致谢、版权与纯出版信息。

#### Tetrabiblos（tetr）
- P0：Book I（基础概念：行星、星座性质、相位与尊贵等）；Book III（Nativities 核心：Ascendant、寿命、体质、心性等）；Book IV（Wealth/Rank 等关键结论域）。
- P1：Book II（地理/气候/日月食等更偏“世界事件/环境”部分，按可复用程度抽取）。
- P2：重复性论证与过长引文（以可否落为因子/规则为准）。
- P3：序言、译者说明与纯索引。

#### The Astrological Houses（astro_houses）
- P0：`THE FIRST HOUSE` ～ `THE TWELFTH HOUSE`（12 宫核心语义与人生领域映射）。
- P1：WHY HOUSES? 与方法论/历史论述（只抽可复用概念与中立标签）。
- P2：技术史/术语争鸣的长段讨论（以复用为准）。
- P3：图片说明、版权等。

#### Planets in Transit（planets_transit）
- P0：Chapter 1–2（Interpreting/Timing Transits）；各行星章节（Sun–Pluto）。
- P1：Case Study（用于叙事与证据链，但不必全量拆卡）。
- P2：前言与出版说明。
- P3：Index。

#### Christian Astrology (vol.1&2)（christian_astro）
- P0：Book 1（基础：行星/星座/宫位/尊贵/术语/判断前置 Considerations）。
- P1：Book 2（Questions/Horary）：只抽“可迁移的判断结构”（如如何选用 significator/阻断条件/置信度口径）。
- P2：大量案例与重复问类（按可复用规则密度抽取）。
- P3：诗序、致谢等。

#### Astrology of Personality（astro_personality）
- P0：Second Section（Dial of Houses / Signs / Planets / Aspects / Progressions / Transits / Interpretation）。
- P1：First Section（占星与现代思想/分析心理学的对齐框架）。
- P2：Epilogue（个体化与文明的宏观段，抽中立标签即可）。
- P3：Prologue 与纯参考。

### 2.4 西方典籍（梦学 / 心理学）

#### The Interpretation of Dreams（interp_dreams）
- P0：Ch. II–VII（方法/愿望满足/扭曲/材料来源/梦工作/梦的心理学）。
- P1：Ch. I（文献综述，只抽核心分歧与术语基线）。
- P2：索引与附录性材料（按需）。
- P3：Literary Index / Index（仅索引）。

#### The Dreams & Visions Symbol Dictionary（dreams_visions）
- P0：A–Z 梦象条目（逐条拆卡：梦象→中立语义标签→叙事素材）。
- P1：Chapter 01（Dream interpretation steps / How to use this book：抽为通用规则与因子）。
- P2：宗教化前言/告诫段（只抽中立可复用句）。
- P3：版权与出版信息。

#### Llewellyn’s Complete Dictionary of Dreams（llewellyn_dreams）
- P0：The Dream Dictionary（A–Z 条目，全量拆卡）。
- P1：Introduction（抽“解释方法/符号语言”中立规则）。
- P2：出版信息。
- P3：无关索引段落（仅索引）。

#### The Archetypes and the Collective Unconscious（jung_archetypes）
- P0：Concept of the Collective Unconscious；Archetypes/Anima；Mother Archetype；Rebirth；（以及书内其他核心原型论述，按 TOC 主标题逐段拆卡）。
- P1：Translator/Editorial note（只抽术语与定义差异）。
- P2：长段引文式案例（以能否抽“原型—情结—表现/触发”为准）。
- P3：插图目录与纯索引。

#### The Collected Works of C.G. Jung（jung_collected）
- P0：优先抽“概念定义/机制/原型簇/个体化过程”相关段落（按卷与主题分批推进，先覆盖与梦学/占星叙事强相关主题）。
- P1：与 P0 概念直接互证的案例段（只保留可复用句与锚点）。
- P2：纯历史/书信/出版说明。
- P3：全量索引与目录保留索引即可。

### 2.5 西方典籍（塔罗）

#### Waite Pictorial Key to the Tarot（waite_key）
- P0：Part II（Trumps Major inner symbolism）；Part III（Divinatory meanings：Greater/Lesser Arcana）。
- P1：Part I（历史与总论，用于术语基线与映射）。
- P2：附加牌义与方法章节（按复用密度抽取）。
- P3：Bibliography/出版信息。

#### The Pictorial Key to the Tarot（pictorial_key）
- P0–P3：与 `waite_key` 同口径；若未来补齐独立文本再细分章节级策略。

#### The Book of Thoth（thoth）
- P0：Part II（Atu/Trumps）；Part III（Court Cards）；Part IV（Small Cards）；Appendix B（Correspondences：跨体系映射高价值）。
- P1：Part One（Theory of the Tarot）。
- P2：Invocation/Mnemonics 与附录中重复段（按复用密度抽取）。
- P3：纯出版信息与外链残留行（仅索引）。

#### 78 Degrees of Wisdom（78_degrees）
- P0：Chapter 3–6（Trumps as archetype journey / sequences）。
- P1：Chapter 1–2（读牌结构与概览）。
- P2：Bibliography。
- P3：出版信息。

#### Learning the Tarot（learning_tarot）
- P0：Part 2（Principles of Interpretation：单卡/牌对/逆位/叙事化）。
- P1：Part 1（Major/Minor Arcana 概念框架与牌阵基础）。
- P2：Exercises（只抽可复用“练习→规则”语句）。
- P3：出版信息。

---

## 3. 跨典籍网络编织策略（因子 / 规则 / 叙事 / 术语）

### 3.1 因子网络如何互联

- **以 `neutral_tags` 为主干**：先用中立标签把不同体系挂在同一“语义节点”下，再回落到各引擎因子。
- **五行↔元素/性质对齐（示例方向）**：
  - 八字五行（木火土金水）与占星四元素（Fire/Earth/Air/Water）不做硬等价；以 `Resource_Conflict / Growth_Pressure / Emotional_Tension / Authority_Challenge` 等标签做桥接。
- **梦象↔原型↔叙事触发**：
  - 梦象词典（梦林/周公/西方词典）先抽 `dream_*` 因子，再映射到 Jung 原型因子与中立标签，实现中西梦学互证。
- **宫位/领域对齐**：
  - 占星 12 宫 → 人生领域（事业/财富/关系/健康/心理/运势）可作为 `rule_conclusion` 的落点维度；再与八字常用领域标签对齐。

### 3.2 规则网络如何互补

- **同一中立标签下允许多规则并存**：中式命理与西式占星/梦学规则不强行统一表达式；以 `conclusion_dimension + neutral_tags` 进行对齐与冲突管理。
- **时间机制对齐**：
  - 八字的大运/流年 与 占星的 transit（行运）在因子层统一归入 `temporal`，规则草案里通过 `rule_condition` 描述其时间层触发方式。
- **置信度口径统一**：
  - 高：原文直陈 if-then；中：原文隐含但可单段推出；低：需要跨段/跨书推断（但仍必须给 evidence_quote）。

### 3.3 叙事素材如何复用

- **复用单位是 `neutral_tags + trigger_expr`**：相同语义标签的叙事句可跨书复用，只需替换语言与意象强度。
- **中文/英文互译只做“术语对齐 + 叙事改写”**：不做全文对译；重点保证触发条件与语义标签一致。

### 3.4 术语对齐如何稳定

- **术语粒度**：稳定技术概念（短语级），避免单字碎片。
- **定义本土化**：中文不直译英文腔；英文不拼音堆砌；优先写可被系统复用的“定义句”。

---

## 4. 精校执行顺序建议（Phase 1/2/3）

### Phase 1（WorldGrid-W0 阻塞项 / 主干骨架）

- 八字：子平真诠（zpzq）→ 滴天髓（dts）→ 三命通会（smth）
- 梦学（中文）：梦林玄解（mlxj）
- 占星（西方）：The Inner Sky（inner_sky）→ Tetrabiblos（tetr）→ The Astrological Houses（astro_houses）→ Planets in Transit（planets_transit）
- 梦学/心理（西方）：The Interpretation of Dreams（interp_dreams）→ The Archetypes and the Collective Unconscious（jung_archetypes）→ The Dreams & Visions Symbol Dictionary（dreams_visions）

### Phase 2（补充典籍：提升网络密度与互证路径）

- 八字补强：穷通宝鉴（qtbj）→ 渊海子平（yhzp）
- 梦学补强：周公解梦类（zgjm）→ Llewellyn’s Complete Dictionary of Dreams（llewellyn_dreams）
- 世界观/背景：周易及传（yijing）→ 记纂渊海（jzyh）
- 占星补强：Christian Astrology（christian_astro）→ Astrology of Personality（astro_personality）

### Phase 3（扩展典籍：加深与拓宽）

- 紫微斗数全书（zwds）
- 塔罗：Waite Key（waite_key / pictorial_key）→ Book of Thoth（thoth）→ 78 Degrees（78_degrees）→ Learning the Tarot（learning_tarot）
- Jung 全集（jung_collected）

