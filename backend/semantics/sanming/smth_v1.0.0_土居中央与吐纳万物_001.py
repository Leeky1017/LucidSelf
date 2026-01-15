"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227491
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
    semantic_id="smth_v1.0.0_土居中央与吐纳万物_001",
    book_id="sanming",
    engine_id="bazi"
)
class 土居中央与吐纳万物(SemanticEntry):
    """
    - **原文（source_text）**：
  土主于中央，兼位西南，应于长夏。土之为言吐也，含吐万物，将生者出，将死者归，为万物家。故长于夏末，火所生也。土或胜水，水乃反土，自然之义也。

- 分...
    """
    
    original_text: str = """- **原文（source_text）**：
  土主于中央，兼位西南，应于长夏。土之为言吐也，含吐万物，将生者出，将死者归，为万物家。故长于夏末，火所生也。土或胜水，水乃反土，自然之义也。

- 分字分词释义：
  - **吐**：含吐、出纳之意，主承载、生养与归藏。
  - **万物家**：一切生长与死亡都系于土，故为万物之所归。

- **规范化释义（primary_lang_explained）**：
  土居中央，又兼管西南之地，对应长夏。土能含纳而又能吐出，将欲生者推出地面，将将死者收归其内，因此为「万物之家」。土得火气而长于夏末，有时能制服水，而水有时也能反制于土，这是自然之常理。

- **完整对等诠释（secondary_lang_full）**：

  Earth occupies the center and also governs the south‑west, corresponding to late summer. Its key action is to hold and to release: it receives all things into itself, brings those about to be born up to the surface, and takes back what is dying, thus becoming the "home of all beings". Fed by Fire, Earth is strongest at the end of summer. Sometimes it overcomes Water; at other times Water undermines Earth—this mutual checking is part of the natural order. In destiny reading, Earth stands for platform, environment, trustworthiness and balance. It is the field on which the other elements act. One must therefore pay close attention to how Earth and Water balance each other, for that balance describes whether a life has a solid, nourishing ground or faces either stagnation and heaviness on one side, or erosion and instability on the other.

- **核心要点**：
  - 命局之土，多主承载、信实、中和，也关系到环境基础、资源与稳定度；
  - 土与水的制化是命局中「环境 vs. 流动」的关键平衡点，不能一味偏重其一。

- **详细解说**：
  本节阐述土的中央属性与吐纳机能。土居中央，兼管西南，对应长夏。土能含纳而又能吐出，将欲生者推出地面，将将死者收归其内，因此为「万物之家」。土得火气而长于夏末，有时能制服水，而水有时也能反制于土。论命时，土厚而有火生、有木疏、有水润，则为承载与平台；土浊滞或太弱，则难以安顿其他行。在职业与事件分析中，土主「环境与平台」，对应基础设施、制度结构、组织架构等。

- **应用推演（操作顺序）**：
  1) 在命局结构中，把土视作「环境与平台」：先判断其厚薄、洁浊，再判断其他行能否在其上安顿；
  2) 分析职业与生活选择时，土象多与土地、建筑、资源、管理平台、基础设施相关，也与「可信度与稳定性」挂钩；
  3) 推岁运时，行土运往往意味着「平台/环境」的变化或重构：有时是稳定、有时是沉重，需结合原局水火金木之态来定；
  4) 在系统设计中，将制度结构、组织架构、基础设施等抽象为土象，用来解释「为何同一个人在不同组织中的表现大相径庭」。

- **反例与边界**：
  - 简单以「土多」等同于「老实、稳定」，而不看土是否浊滞、死重，忽略「顽固、迟钝、压抑」的一面；
  - 将土象一概视为低级、不灵动，而忘记厚土是万物之基，缺土则水火皆难以安顿；
  - 在工程实现中，如果只建模个体行为而不建模「环境/平台」这一层（土），系统很难解释同一命局在不同环境中的巨大差异；
  - 反过来，将一切问题归咎于「环境不好」，完全忽略个体在水木火金等方面的主动调适能力，也违背本节所强调的互动关系。

- **小例（示意）**：
  - 某命局土厚而水木适中，在大公司稳步发展远优于频繁跳槽创业；系统可据此在职业策略建议中强调「平台型发展」而非「频繁破土」；
  - 在城市或企业命盘分析中，把基础设施建设、制度梳理、文化沉淀等阶段标记为「土运期」，用以解释为何该阶段「显得沉闷但为后续发展蓄势」。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_051]` `[trigger: 土主中央]` `[factor_trigger: position=center AND wuxing=earth]` `[role: 主干]` 土主于中央，兼位西南，应于长夏。土之为言吐也，含吐万物。 → 《三命通会》卷一#论五行生成
  - `[ns_smth_052]` `[trigger: 火生土]` `[factor_trigger: wuxing_shengke=fire_generates_earth]` `[role: 主干依赖]` 故长于夏末，火所生也。土或胜水，水乃反土，自然之义也。 → 《三命通会》卷一#论五行生成
  - `[ns_smth_900]` `[trigger: 空煞破败]` `[factor_trigger: kong_sha_pobai]` `[role: 条件分支]` 空煞破败主不利。 → 《三命通会》卷一
  - `[ns_smth_901]` `[trigger: 库冲条件]` `[factor_trigger: ku_chong_tiaojian]` `[role: 条件分支]` 库冲条件定激活。 → 《三命通会》卷一
  - `[ns_smth_902]` `[trigger: 库墓开闭]` `[factor_trigger: kumu_kaibi]` `[role: 条件分支]` 库墓开闭定变化。 → 《三命通会》卷一
  - `[ns_smth_903]` `[trigger: 库墓转化]` `[factor_trigger: kumu_zhuanhua]` `[role: 条件分支]` 库墓转化主变质。 → 《三命通会》卷一
  - `[ns_smth_904]` `[trigger: 枯涸风险]` `[factor_trigger: kuhe_risk]` `[role: 条件分支]` 枯涸有风险。 → 《三命通会》卷一
  - `[ns_smth_905]` `[trigger: 狂风暴雨风险]` `[factor_trigger: kuangfeng_baoyu_risk]` `[role: 条件分支]` 狂风暴雨有风险。 → 《三命通会》卷一
  - `[ns_smth_906]` `[trigger: 苦业虚耗]` `[factor_trigger: kuye_xuhao]` `[role: 条件分支]` 苦业虚耗主不利。 → 《三命通会》卷一
  - `[ns_smth_907]` `[trigger: 地支层次]` `[factor_trigger: layer_earthly_branch]` `[role: 条件分支]` 地支层次定位置。 → 《三命通会》卷一
  - `[ns_smth_908]` `[trigger: 天干层次]` `[factor_trigger: layer_heavenly_stem]` `[role: 条件分支]` 天干层次定位置。 → 《三命通会》卷一
  - `[ns_smth_909]` `[trigger: 雷霆格]` `[factor_trigger: leiting_ge]` `[role: 条件分支]` 雷霆格主格局。 → 《三命通会》卷一
  - `[ns_smth_910]` `[trigger: 类象表意]` `[factor_trigger: leixiang_biaoyi]` `[role: 条件分支]` 类象表意定含义。 → 《三命通会》卷一
  - `[ns_smth_911]` `[trigger: 理化分]` `[factor_trigger: lihua_fen]` `[role: 条件分支]` 理化分定方法。 → 《三命通会》卷一
  - `[ns_smth_912]` `[trigger: 连珠格]` `[factor_trigger: lianzhu_ge]` `[role: 条件分支]` 连珠格主格局。 → 《三命通会》卷一
  - `[ns_smth_913]` `[trigger: 两神成象]` `[factor_trigger: liangshen_chengxiang]` `[role: 条件分支]` 两神成象主格局。 → 《三命通会》卷一
  - `[ns_smth_914]` `[trigger: 临财风险]` `[factor_trigger: lincai_risk]` `[role: 条件分支]` 临财有风险。 → 《三命通会》卷一
  - `[ns_smth_915]` `[trigger: 临官帝旺]` `[factor_trigger: linguan_diwang]` `[role: 条件分支]` 临官帝旺主旺盛。 → 《三命通会》卷一
  - `[ns_smth_916]` `[trigger: 凌乱失序风险]` `[factor_trigger: lingluan_shixu_risk]` `[role: 条件分支]` 凌乱失序有风险。 → 《三命通会》卷一
  - `[ns_smth_917]` `[trigger: 临机应变]` `[factor_trigger: linji_yingbian]` `[role: 条件分支]` 临机应变主灵活。 → 《三命通会》卷一
  - `[ns_smth_918]` `[trigger: 临劫财]` `[factor_trigger: linjiecai]` `[role: 条件分支]` 临劫财主竞争。 → 《三命通会》卷一
  - `[ns_smth_919]` `[trigger: 临流行运]` `[factor_trigger: linliu_xingyun]` `[role: 条件分支]` 临流行运定时机。 → 《三命通会》卷一
  - `[ns_smth_920]` `[trigger: 临禄地时]` `[factor_trigger: linlu_dishi]` `[role: 条件分支]` 临禄地时主有力。 → 《三命通会》卷一
  - `[ns_smth_921]` `[trigger: 龙德贵人]` `[factor_trigger: longde_guiren]` `[role: 条件分支]` 龙德贵人主有贵。 → 《三命通会》卷一
  - `[ns_smth_922]` `[trigger: 龙虎配合]` `[factor_trigger: longhu_peihe]` `[role: 条件分支]` 龙虎配合主有力。 → 《三命通会》卷一
  - `[ns_smth_923]` `[trigger: 禄财官配置]` `[factor_trigger: lu_cai_guan_peizhi]` `[role: 条件分支]` 禄财官配置定格局。 → 《三命通会》卷一
  - `[ns_smth_924]` `[trigger: 六害风险]` `[factor_trigger: liuhai_risk]` `[role: 条件分支]` 六害有风险。 → 《三命通会》卷一"""
    normalized_text_zh: str = """"""
    subject: str = "土居中央与吐纳万物"
    factor_refs: list = ['earth', 'intake_output', 'home_of_all', 'late_summer']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_土居中央与吐纳万物_001_L1",
    )
    version: str = "1.0.0"
