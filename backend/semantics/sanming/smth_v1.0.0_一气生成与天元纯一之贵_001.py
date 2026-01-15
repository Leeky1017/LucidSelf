"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412954
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
    semantic_id="smth_v1.0.0_一气生成与天元纯一之贵_001",
    book_id="sanming",
    engine_id="bazi"
)
class 一气生成与天元纯一之贵(SemanticEntry):
    """
    - **原文（source_text）**：

  天元一气，乃四壬寅，四辛卯，四庚辰，四己巳，四戊午，四丁未，四丙申，四乙酉，四甲戌，四癸亥是也。四柱干支一气，中间亦有轻重贵贱，须细别之。壬寅、辛卯...
    """
    
    original_text: str = """- **原文（source_text）**：

  天元一气，乃四壬寅，四辛卯，四庚辰，四己巳，四戊午，四丁未，四丙申，四乙酉，四甲戌，四癸亥是也。四柱干支一气，中间亦有轻重贵贱，须细别之。壬寅、辛卯、甲戌富贵双全；己巳亦贵；戊午、丁未刃旺性强，虽贵亦多凶险，克妻，不善终；庚辰贵而风流，名重利轻；乙酉多伤残；癸亥多贫薄；丙申生北方亦可取贵，岁运如遇刑冲破夺，必生灾祸。大要推其支内有无财官印食，入格有无伤损，天干有无得令，上下干支财官印食可化不可化，可从不可从，定其轻重贵贱。又曰：四干纯一不杂，为天元一气，不可以比肩论，须详其支神有无生化，有无刑克，带财官印合格，岁运不背，必当大贵，冲刑克制亦凶，不可执定一气皆以贵言。如甲子、甲戌、甲寅、甲子之类，又名凤凰干格。果正郎：壬辰、壬子、壬寅、壬寅，壬自绝于寅，是为驳杂，故止正郎。又曰：四支纯一不杂，为地物相之一，名芝兰并秀格，须看干元是支福聚祸聚，如是福聚合格，多居两府之贵，如甲寅、丙寅、庚寅、戊寅之类，又名凤凰支格。诗曰：天元一气定尊荣，不杂天干一字清，非可比肩争竞论，生来富贵至公卿。又：天元一字水为源，生在秋冬妙莫言，大吉土神逢一位，少年仕路必高迁。又：天元一字土为基，四季生时更是奇，申酉二支加入局，聪明俊秀异常儿。又：天元一字木为根，传送登明显福元，四柱官星如得地，功名利禄好争先。又：天元一字若逢金，时日魁罡福气深，羊刃逢冲并带贵，平生得遇贵人钦。又：天元一字火融融，大吉功曹时日中，冲起财官为发用，平生富贵福兴隆。

- 分字分词释义：

  - **天元一气**：四柱干支同属一气（同一五行或同一干），上下纯一不杂，气势高度集中。
  - **四壬寅、四辛卯……四癸亥**：列举干支同字、四柱一气的典型组合。
  - **四干纯一 / 四支纯一**：天干或地支四位皆同，可成“凤凰干格”或“凤凰支格”。
  - **中间亦有轻重贵贱，须细别之**：即便同属一气，不同组合在贵贱上仍有差别，不可一概而论。
  - **不可执定一气皆以贵言**：提醒不能因“一气”之名而忽略全局财官印食、刑冲化合等具体结构。

- **规范化释义（primary_lang_explained）**：

  一气生成格，讨论的是四柱干支在同一五行、同一干支上高度纯一的格局。经典以四壬寅、四辛卯、四庚辰等为例，说明当天干或地支四位皆同，便如“天元一气”，气势极其集中，容易形成鲜明而强烈的人生命格——要么极贵，要么其代价与偏颇亦极大。

  原文对不同组合的评语不尽相同：有“富贵双全”者，有“贵而凶险、克妻不善终”者，有“名重利轻”“多伤残”“多贫薄”者，提示即使同为一气，也需结合支中所藏之财官印食、是否得令、是否被刑冲破合等多重因素，才能判断轻重贵贱。

- 核心要点：

  - 一气生成的关键不在于“全同”本身，而在于**同中有用、同中有化**。
  - 天干、地支纯一时，更需细看支藏、格局与岁运，不能简单判为“必贵”。
  - 适宜时，一气格可成“凤凰干格”“凤凰支格”，多主清贵显达；失衡时，则易走向性格偏执、际遇极端。

- 详细解说：

  一气格可视作“四位纯全”的另一种极端形式：能量高度集中，变化空间相对收窄。其优点在于：人生主题鲜明、力量集中、行动决断；其隐忧在于：缺乏弹性、难以转圜，一旦岁运与原局发生强烈冲突，容易出现大起大落甚至“成败一线间”的局面。

  判断一气格时，可从以下路径入手：

  1. 明确此“一气”究竟偏向哪一五行、哪一干支（如木、火、土、金、水）；

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_225]` `[trigger: 一气生成]` `[factor_trigger: yiqi_shengcheng AND sizhuchunyi]` `[role: 主干]` 天元一气，乃四壬寅、四辛卯、四庚辰等是也。 → 《三命通会》卷六#一气生成
  - `[ns_smth_06_226]` `[trigger: 天元纯一]` `[factor_trigger: tianyuan_chunyi AND bukebijianlun]` `[role: 主干依赖]` 四干纯一不杂，为天元一气，不可以比肩论。 → 《三命通会》卷六#一气生成
  - `[ns_smth_06_227]` `[trigger: 轻重贵贱]` `[factor_trigger: yiqi_qingzhong AND xibiezhi]` `[role: 条件分支]` 中间亦有轻重贵贱，须细别之。 → 《三命通会》卷六#一气生成
  - `[ns_smth_06_228]` `[trigger: 富贵公卿]` `[factor_trigger: yiqi_zunrong AND fugui_gongqing]` `[role: 总结]` 天元一气定尊荣，生来富贵至公卿。 → 《三命通会》卷六#一气生成"""
    normalized_text_zh: str = """"""
    subject: str = "一气生成与天元纯一之贵"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_84', 'bazi_semantic', 'bazi_condition_factor_219', 'bazi_semantic', 'bazi_state_factor_349', 'bazi_semantic', 'source_ref', 'rel_smth_06_196', 'yiqishengcheng_presence', 'rel_smth_06_197', 'tongzhong_youyong', 'rel_smth_06_198', 'chuner_wuyong', 'evi_smth_06_196', 'yiqishengcheng_presence', 'rule_yiqishengcheng', 'evi_smth_06_197', 'tongzhong_youyong', 'rule_youyong', 'evi_smth_06_198', 'chuner_wuyong', 'rule_pianku', 'map_smth_06_131', 'map_smth_06_132']
    
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
        l1_anchor="smth_v1.0.0_一气生成与天元纯一之贵_001_L1",
    )
    version: str = "1.0.0"
