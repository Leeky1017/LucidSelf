"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.755870
Version: 1.0.0

对照 Requirements 6.4 - 带 @SemanticRegistry.register 装饰器的 Python 模块
"""

from backend.semantics.core.base import SemanticEntry, SemanticRegistry, NarrativeSnippetExtended
from backend.core.contracts import (
    SnippetRole,
    SourceMetadata,
    ConfigRelation,
    EvidenceChainEntry,
    RelationType,
    EffectDirection,
    ConfidenceLevel,
)


@SemanticRegistry.register(
    semantic_id="zw_v1.0.0_论诸星同位垣各司所宜分别富贵贫贱夭寿_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 论诸星同位垣各司所宜分别富贵贫贱夭寿(SemanticEntry):
    """
    - 分字分词释义：

  - **诸星同位垣**：多颗星曜同在一宫的组合关系，决定该宫吉凶倾向。
  - **各司所宜**：每颗星曜有其“适宜位置”与“适宜同伴”，脱离这些条件则福祸转向。
  - *...
    """
    
    original_text: str = """- 分字分词释义：

  - **诸星同位垣**：多颗星曜同在一宫的组合关系，决定该宫吉凶倾向。
  - **各司所宜**：每颗星曜有其“适宜位置”与“适宜同伴”，脱离这些条件则福祸转向。
  - **庙旺平陷**：星曜在宫垣中的强弱状态，庙旺则力量充沛，陷地则力量受限。
  - **富贵贫贱夭寿**：人生物质与寿命层级的综合评估标签。
  - **紫府得辅彼同垣**：尊星得辅佐星三方拱照，可成就一品之贵，是富贵格局典型。
  - **四杀与空劫**：羊陀火铃、地劫天空等高破坏性星曜，同宫或三方时易带来破坏与流失。
  - **朝斗格**：紫微尊星居子午，科权禄三方拱照，为“仰面朝斗”贵格。
  - **星曜底层字典**：本条可视为星曜判断的基础语义库，为后续格局分析提供素材。

- 原文（断句）（节要）：

  论诸星同位垣，各司所宜分别富贵贫贱夭寿。

  紫微：庙寅午丑未，旺申亥卯巳，平子无陷……紫微居午无刑忌，甲丁巳命至公卿，加刑忌平常，刑乃擎羊也。紫微居子午，科权禄照最为奇，为仰面朝斗格。紫微卯酉劫空四杀，多为脱俗之僧……紫府得辅弼同垣，及三方拱照嘉会，终身富贵；紫破辰戌，君臣不义；紫微贪狼为至淫。

  天府：庙子丑寅未，旺午酉辰戌地，卯巳申亥无陷……府相梁同，君臣庆会；天府禄存昌曲，巨万之资；府居戌宫无杀凑者，甲巳人腰金又且富。

  其后依次论天相、天梁、天同、天机、太阳、太阴、文昌、文曲、武曲、贪狼、廉贞、巨门、七杀、破军、擎羊、陀罗、火星、铃星、魁钺、左辅右弼、禄存、天马、科权禄、劫空、天伤等，分别说明：各星在庙旺、平、陷诸宫时的贵贱祸福；与四杀、空劫、科权禄、辅弼、日月等星同垣或三方会合时的格局高低；以及在命宫、身宫、财帛、官禄、福德、迁移、妻宫、奴仆、疾厄等不同宫位的倾向与应象。末尾以「五卷终」收束，表示卷五以此作为诸星论断的总汇与总结。

- 规范化释义（primary_lang_explained）：

  本条是整卷中篇幅最长、结构最密的部分，可以理解为一部「星曜位置与组合说明书」。它不再逐条讲行限或岁限，而是按星曜分类，从紫微、天府起，依次说明每颗星在不同宫垣与组合下，对富贵、贫贱、夭寿等结局的结构性影响。文本中大量运用格局名（如仰面朝斗、紫府朝垣、七杀朝斗等）、比喻与历史人物（如安禄山、赵高、贾谊、孙膑、颜回等）来举例说明星曜组合的典型结果。

  另一方面，本条也强调「同一颗星在不同位置与组合下，性质会有巨大差异」：如紫微与天府得辅弼、左右、科权禄拱照，可以成就一品之贵；同一紫微若与破军、贪狼、羊陀、四杀同会，则可能表现为奸邪、淫佚、凶恶胥吏等；七杀入庙且得吉曜朝拱，可以成为有权威的将星；七杀陷地又逢羊铃白虎，则成为极高的生死风险指标；文昌文曲在庙旺并得左右禄存，主聪慧高第；若陷地逢四杀空劫，则美名短暂而早夭。整体而言，这一大段的价值不在于死背每句歌诀，而在于掌握：星曜有其「适宜位置」与「适宜同伴」，脱离这些条件则福祸转向。

- 完整对等诠释（secondary_lang_full）：

  This closing section reads like a handbook of how each major star behaves in
  different places and company. Starting with Ziwei and Tianfu and moving
  through Tianxiang, Tianliang, Tiantong, Tianji, the Sun and Moon, the
  scholarly pair Wen Chang and Wen Qu, martial stars like Wuqu and Tanlang,
  harsh stars such as Qisha and Pojun, and supportive or disruptive stars like
  Qingyang, Tuoluo, Mars, Bell, Zuo Fu, You Bi, Kui, Yue, Lucun, Tianma and the
  robbing voids, it catalogues how dignity, house placement and combinations
  tilt a life toward wealth and rank, ordinary struggle, poverty, danger or
  early death.

  For modern work its value lies less in memorising every line and more in
  extracting principles. A star must be read through four lenses: its intrinsic
  nature, whether it is dignified or fallen in a given house, which houses it
  occupies (Life, Wealth, Career, Fortune, Travel, etc.), and which allies or
  enemies it meets in the same or triadic houses. Benefic supports such as
  assistants, literary stars and salary–power combinations can transform sharp
  or harsh stars into engines of achievement; concentrated killers and voids can
  pull even noble stars down into scandal, hardship or risk. Treated as a
  structured library of patterns rather than literal prophecies, this chapter
  becomes a rich source of features and heuristics for any serious Ziwei
  practice or system design.

<!-- L2_BEGIN -->

- 核心要点：

  - **主题**：系统归纳各主要星曜在不同宫垣与组合下，对富贵、贫贱、夭寿等结局的结构性影响.
  - **自然属性**：
    - 象征：
      - 紫微、天府等尊星象征统摄、权柄与中枢；七杀、破军等象征极端、破荡与转折；文昌、文曲象征才学与声名；四杀与空劫象征破坏与流失.
      - 辅弼、左右、魁钺、科权禄等象征支持系统与资源加持.
    - 特性：
      - 强调「位置 + 组合」的重要性，同一颗星在不同宫位、不同同伴下表现截然不同.
      - 既给出富贵清显的高度格局，也点出贫贱夭折、流离浪荡的极端用例.
    - 元素：各主星与辅星、庙旺平陷状态、命身财官福迁等宫位、四杀空劫、日月、科权禄、禄马等.
  - **功能象义**：
    - 作为星曜判断的「底层字典」，为后续一切格局与用神分析提供基础语义.
    - 帮助从星曜结构推断人格特质、职业类型、财富模式、感情结构、寿命风险等大方向.
    - 为现代因子化设计提供直接素材，可提炼为「星 × 宫 × 组合 → 倾向结果」的规则库.
  - **必要条件**：
    - 已排出命盘并能标定各星在十二宫中的位置与庙旺平陷状态.
    - 能识别同宫与三方四正星群，区分吉曜、凶曜与中性星.
  - **增强条件**：
    - 结合行运层（大限、小限、太岁），在特定年份放大某些结构性倾向.
    - 参考大量案例，对文本中极端描述做强度校准与语义现代化处理.
  - **失效条件**：
    - 只背歌诀、不看整体盘面与现实处境，将潜在可能误读为必然命运.
    - 将单一星曜简单贴上「吉星」「凶星」标签，而忽略组合与落宫对其性质的重塑作用.

- **L2-术语对齐（Term Glossary·六列）**：

  | 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
  |---------|---------|---------|---------|-----------|--------|
  | 庙旺平陷 | Dignified Average Fallen | 星曜在宫垣中强弱状态 | Strength debility star given house | state_miaowangpingxian | existing |
  | 四杀与空劫 | Four Killers Void-Robbers | 羊陀火铃劫空高破坏性星曜 | Highly disruptive Qingyang Tuoluo | group_sishakongjie | existing |
  | 朝斗格 | Facing-Dipper Pattern | 紫微尊星三方科权禄贵格 | Noble principal stars Pole benefic | pattern_chaodou | new_candidate |
  | 夹命/夹财 | Flanking Life Wealth | 日月左右命财宫夹拱结构 | Key stars flank Life Wealth | pattern_jiamingcai | new_candidate |
  | 富贵贫贱夭寿 | Wealth Rank Poverty Longevity | 人生物质寿命层级总体标签 | Global wealth rank lifespan outcomes | result_fuguipinjian | new_candidate |

<!-- L2.5_BEGIN -->
#### L2.5 桥接层

**因子关系层**：

| 关系ID | 关系类型 | 因子A | 因子B | 关系性质 | 条件约束 | 效果方向 | source_ref |
|-------|---------|-------|-------|---------|---------|---------|-----------|
| rel_xingwei_001 | base | state_miaowangpingxian | result_fuguipinjian | 庙陷影响 | 星曜落宫 | 能量基线 | 《论诸星同位垣》 |
| rel_xingwei_002 | risk | group_sishakongjie | result_fuguipinjian | 四杀空劫 | 同宫三方 | 破坏流失 | 《论诸星同位垣》 |
| rel_xingwei_003 | pattern | pattern_chaodou | result_fuguipinjian | 朝斗贵格 | 科权禄会 | 一品之贵 | 《论诸星同位垣》 |

**推理溯源层**：

| 证据ID | 原文锚点 | 涉及因子 | 推理步骤 | 结论方向 | 置信度 | 可生成规则 | 目标规则ID |
|-------|---------|---------|---------|---------|-------|----------|-----------|
| evi_xingwei_001 | "紫府得辅彼同垣及三方拱照嘉会终身富贵" | pattern_chaodou | 紫府辅彼→终身富贵 | 贵格形成 | 高 | ✅ | rule_xingwei_zifu |
| evi_xingwei_002 | "文昌文曲若陷地逢四杀空劫则美名短暂而早夭" | group_sishakongjie | 陷地+四杀→早夭 | 风险指标 | 高 | ✅ | rule_xingwei_changqu |

**跨体系概念映射层**：

| 概念ID | 共通语义 | 八字对应 | 占星对应 | 梦学对应 | 心理学对应 | 备注 |
|-------|---------|---------|---------|---------|-----------|------|
| concept_star_library | 星曜字典 | 十神象义 | 行星象征 | - | 原型系统 | 星曜底层 |
| concept_life_outcome | 人生层级 | 格局高低 | 宫位影响 | - | 生涯结果 | 富贵贫贱夭寿 |
<!-- L2.5_END -->

<!-- L2_END -->

<!-- FACTOR_BEGIN -->

- 语义因子提取（因子层·八列表）：

  | 因子类型 | 因子标签（人话） | 因子ID | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
  |----------|-----------------|--------|----------|----------|----------|-----------|------|
  | 结构类 | 关键星曜庙旺平陷状态 | state_xingmiaopingxian | existing | 命盘结构 | 庙/旺/平/陷 | ziwei_rule_engine | 星曜能量基线 |
  | 结构类 | 星曜落入关键宫位 | pos_xingluogong | existing | 命盘结构 | 命身/财/官/福/迁 | ziwei_rule_engine | 影响生活领域 |
  | 条件类 | 吉凶曜组合强度 | level_jixiongzuhe | existing | 组合条件 | 强吉/中/弱/强凶 | ziwei_rule_engine | 同宫三方评估 |
  | 条件类 | 是否形成特定格局 | flag_geju | existing | 格局标签 | 成格/类格/破格/无 | ziwei_rule_engine | 典型组合标记 |
  | 结果类 | 人生层级与风险轮廓 | result_renshengcengji | existing | 结果评估 | 上富/中起落/劳碌/贫贱/夭折 | ziwei_rule_engine | 综合结构评估 |

<!-- FACTOR_END -->

- 完整对等诠释（secondary_lang_full）：

  This closing section reads like a handbook of how each major star behaves in
  different places and company. Starting with Ziwei and Tianfu and moving
  through Tianxiang, Tianliang, Tiantong, Tianji, the Sun and Moon, the
  scholarly pair Wen Chang and Wen Qu, martial stars like Wuqu and Tanlang,
  harsh stars such as Qisha and Pojun, and supportive or disruptive stars like
  Qingyang, Tuoluo, Mars, Bell, Zuo Fu, You Bi, Kui, Yue, Lucun, Tianma and the
  robbing voids, it catalogues how dignity, house placement and combinations
  tilt a life toward wealth and rank, ordinary struggle, poverty, danger or
  early death.

  For modern work its value lies less in memorising every line and more in
  extracting principles. A star must be read through four lenses: its intrinsic
  nature, whether it is dignified or fallen in a given house, which houses it
  occupies (Life, Wealth, Career, Fortune, Travel, etc.), and which allies or
  enemies it meets in the same or triadic houses. Benefic supports such as
  assistants, literary stars and salary–power combinations can transform sharp
  or harsh stars into engines of achievement; concentrated killers and voids can
  pull even noble stars down into scandal, hardship or risk. Treated as a
  structured library of patterns rather than literal prophecies, this chapter
  becomes a rich source of features and heuristics for any serious Ziwei
  practice or system design."""
    normalized_text_zh: str = """"""
    subject: str = "论诸星同位垣各司所宜分别富贵贫贱夭寿"
    factor_refs: list = ['state_miaowangpingxian', 'group_sishakongjie', 'pattern_chaodou', 'pattern_jiamingcai', 'result_fuguipinjian', 'source_ref', 'rel_xingwei_001', 'state_miaowangpingxian', 'rel_xingwei_002', 'group_sishakongjie', 'rel_xingwei_003', 'pattern_chaodou', 'evi_xingwei_001', 'pattern_chaodou', 'rule_xingwei_zifu', 'evi_xingwei_002', 'group_sishakongjie', 'rule_xingwei_changqu', 'concept_star_library', 'concept_life_outcome']
    
    # 叙事素材（包含 trigger_human）
    narrative_snippets: list = [

    ]
    
    # L2.5 因子关系
    related_semantics: list = [

    ]
    
    # L2.5 证据链
    evidence_refs: list = [

    ]
    
    metadata: SourceMetadata = SourceMetadata(
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_论诸星同位垣各司所宜分别富贵贫贱夭寿_001_L1",
    )
    version: str = "1.0.0"
