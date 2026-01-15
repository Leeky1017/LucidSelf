"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227445
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
    semantic_id="smth_v1.0.0_五行生克造化大纪_001",
    book_id="sanming",
    engine_id="bazi"
)
class 五行生克造化大纪(SemanticEntry):
    """
    - **原文（source_text）**：
  五行相生相克为造化之大纪，故天之五气（寒暑燥湿风）、地之五行（金木水火土）、形气相感、万物化生。凡干支、运气，以至年月日时之推算，无不本乎此理。

-...
    """
    
    original_text: str = """- **原文（source_text）**：
  五行相生相克为造化之大纪，故天之五气（寒暑燥湿风）、地之五行（金木水火土）、形气相感、万物化生。凡干支、运气，以至年月日时之推算，无不本乎此理。

- 分字分词释义：
  - **五行相生相克**：指水、火、木、金、土之间的生扶与制约关系，是一切推命与推运的基础结构。

- **规范化释义（primary_lang_explained）**：
  五行生克是造化生成的总纲领，天有五气，地有五行，形气相感而万物化生。干支、运气与年月日时的推算，皆以此为根本。

- **完整对等诠释（secondary_lang_full）**：
  This paragraph sets out the Five Elements' mutual generation and control as the grand ordinance of creation. From the Ten Heavenly Stems and Twelve Branches, to the Five Movements and Six Qi, to the cycles of years, months, days and hours, every system of calculation rests on this pattern. In heaven it appears as cold, heat, dryness, dampness and wind; on earth it appears as the tangible forms of Metal, Wood, Water, Fire and Earth. Through the interaction of heavenly Qi and earthly form, the myriad beings come forth.

- **核心要点**：
  - 论命的一切细节（格局、用神、运势）都不得脱离「五行生克」这个总纲；
  - 干支、运气与岁月日时，只是用来刻画五行生克之用的不同视角和刻度。

- **详细解说**：
  本节总结五行生克为造化之大纪：天之五气（寒暑燥湿风）与地之五行（金木水火土）相感而化生万物。干支、运气、年月日时的推算皆以此为本。论命时，格局、用神、运势等一切细节都不能脱离五行生克这个总纲。

- **应用推演（操作顺序）**：
  1) 在搭建任何命理规则体系前，先抽象出一个统一的「五行生克引擎」：所有格局、十神、神煞规则都在其上层运作，而不是各自为政；
  2) 解命时，先用五行生克在全盘上跑一遍：标出谁生谁、谁克谁、谁泄谁、谁制谁，再在此基础上识别格局与用神，而不是直接跳到格局名目；
  3) 推岁运时，以「运来何行、与原局何生克」为纲：先看运对体用主线的生克，再看次要干支与六亲；
  4) 在工程化中，将「五行生克矩阵」做成可配置数据结构，允许在不同学派、不同实践场景中微调权重，但永远不动其"互相制衡"的核心逻辑。

- **反例与边界**：
  - 只记若干名目（从格、化格、专旺格等），却无法解释这些格局背后的五行生克路径，导致遇到稍有变形的命局就失去判断能力；
  - 将某些十神看得过重，而不看其背后所属五行在全局中的位置，导致「有名无实」：名为财官印食，实则五行被制空；
  - 在系统实现中，若只写一堆 if-else 的格局判断，而没有统一的五行生克层，很难扩展或解释复杂反例；
  - 反过来，如果只停留在抽象的五行生克，不愿落实到具体十神与事件类型，也会让系统失去可操作性。

- **小例（示意）**：
  - 为推理引擎设计一个「五行流转视图」：给定命局与岁运，系统先输出水、火、木、金、土之间的生克网络，再在此网络上标注财官印食比劫的位置与强弱，供后续格局与事件判断模块调用，体现本节「造化大纪」的统摄作用。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_039]` `[trigger: 造化大纪]` `[factor_trigger: wuxing_shengke=fundamental]` `[role: 主干]` 五行相生相克为造化之大纪。 → 《三命通会》卷一#论五行生成
  - `[ns_smth_040]` `[trigger: 形气相感]` `[factor_trigger: heaven_earth_interaction=active]` `[role: 主干依赖]` 天之五气、地之五行，形气相感，万物化生。 → 《三命通会》卷一#论五行生成
  - `[ns_smth_775]` `[trigger: 官印禄库格有无]` `[factor_trigger: guanyin_luku_ge_presence]` `[role: 条件分支]` 官印禄库格有无定格局。 → 《三命通会》卷一
  - `[ns_smth_776]` `[trigger: 官印配合]` `[factor_trigger: guanyin_peihe]` `[role: 条件分支]` 官印配合主清贵。 → 《三命通会》卷一
  - `[ns_smth_777]` `[trigger: 官印双全]` `[factor_trigger: guanyin_shuangquan]` `[role: 条件分支]` 官印双全主大贵。 → 《三命通会》卷一
  - `[ns_smth_778]` `[trigger: 官印同位]` `[factor_trigger: guanyin_tongwei]` `[role: 条件分支]` 官印同位主有力。 → 《三命通会》卷一
  - `[ns_smth_779]` `[trigger: 官印相生]` `[factor_trigger: guanyin_xiangsheng]` `[role: 条件分支]` 官印相生主顺遂。 → 《三命通会》卷一
  - `[ns_smth_780]` `[trigger: 官印月时]` `[factor_trigger: guanyin_yueshi]` `[role: 条件分支]` 官印月时定位置。 → 《三命通会》卷一
  - `[ns_smth_781]` `[trigger: 官印运配合]` `[factor_trigger: guanyin_yun_peihe]` `[role: 条件分支]` 官印运配合定时机。 → 《三命通会》卷一
  - `[ns_smth_782]` `[trigger: 官制劫护财]` `[factor_trigger: guanzhi_jie_hu_cai]` `[role: 条件分支]` 官制劫护财主有助。 → 《三命通会》卷一
  - `[ns_smth_783]` `[trigger: 孤独兴衰风险]` `[factor_trigger: gudu_xingshuai_risk]` `[role: 条件分支]` 孤独兴衰有风险。 → 《三命通会》卷一
  - `[ns_smth_784]` `[trigger: 古法依赖]` `[factor_trigger: gufa_yilai]` `[role: 条件分支]` 古法依赖主传统。 → 《三命通会》卷一
  - `[ns_smth_785]` `[trigger: 癸大贵]` `[factor_trigger: gui_dagui]` `[role: 条件分支]` 癸大贵主贵气。 → 《三命通会》卷一
  - `[ns_smth_786]` `[trigger: 癸合戊路径]` `[factor_trigger: gui_he_wu_lujing]` `[role: 条件分支]` 癸合戊路径定合化。 → 《三命通会》卷一
  - `[ns_smth_787]` `[trigger: 癸受挫]` `[factor_trigger: gui_shoucu]` `[role: 条件分支]` 癸受挫主不顺。 → 《三命通会》卷一
  - `[ns_smth_788]` `[trigger: 贵旺身衰]` `[factor_trigger: gui_wang_shenshuai]` `[role: 条件分支]` 贵旺身衰主不担。 → 《三命通会》卷一
  - `[ns_smth_789]` `[trigger: 癸晚年]` `[factor_trigger: gui_wannian]` `[role: 条件分支]` 癸晚年定晚景。 → 《三命通会》卷一
  - `[ns_smth_790]` `[trigger: 癸水己土配置]` `[factor_trigger: gui_water_ji_earth_config]` `[role: 条件分支]` 癸水己土配置定格局。 → 《三命通会》卷一
  - `[ns_smth_791]` `[trigger: 癸异常]` `[factor_trigger: gui_yichang]` `[role: 条件分支]` 癸异常主变化。 → 《三命通会》卷一
  - `[ns_smth_792]` `[trigger: 贵不用]` `[factor_trigger: guibuyong]` `[role: 条件分支]` 贵不用主空贵。 → 《三命通会》卷一
  - `[ns_smth_793]` `[trigger: 贵格财官印]` `[factor_trigger: guige_caiguanyin]` `[role: 条件分支]` 贵格财官印定贵气。 → 《三命通会》卷一
  - `[ns_smth_794]` `[trigger: 贵格配合]` `[factor_trigger: guige_peihe]` `[role: 条件分支]` 贵格配合定格局。 → 《三命通会》卷一
  - `[ns_smth_795]` `[trigger: 贵格异常]` `[factor_trigger: guige_yichang]` `[role: 条件分支]` 贵格异常主变化。 → 《三命通会》卷一
  - `[ns_smth_796]` `[trigger: 贵贱变质]` `[factor_trigger: guijian_bianzhi]` `[role: 条件分支]` 贵贱变质主转换。 → 《三命通会》卷一
  - `[ns_smth_797]` `[trigger: 贵拘成府]` `[factor_trigger: guiju_chengfu]` `[role: 条件分支]` 贵拘成府主有力。 → 《三命通会》卷一
  - `[ns_smth_798]` `[trigger: 归禄格]` `[factor_trigger: guiluge]` `[role: 条件分支]` 归禄格主有禄。 → 《三命通会》卷一
  - `[ns_smth_799]` `[trigger: 贵马学堂]` `[factor_trigger: guima_xuetang]` `[role: 条件分支]` 贵马学堂主聪慧。 → 《三命通会》卷一"""
    normalized_text_zh: str = """"""
    subject: str = "五行生克造化大纪"
    factor_refs: list = ['wuxing_shengke', 'zaohua_daji', 'xingqi_xianggan']
    
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
        l1_anchor="smth_v1.0.0_五行生克造化大纪_001_L1",
    )
    version: str = "1.0.0"
