"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412681
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
    semantic_id="smth_v1.0.0_弃命从财与极端相从格_001",
    book_id="sanming",
    engine_id="bazi"
)
class 弃命从财与极端相从格(SemanticEntry):
    """
    - **原文（source_text）**：

  弃命从财：《独步》云：弃命从财，须要会财，若逢根气，命损无猜。假如丁生酉月，柱多庚辛，日干无气，只得弃命相从，运入北方财官旺地，乃为入格，南行灾。古...
    """
    
    original_text: str = """- **原文（source_text）**：

  弃命从财：《独步》云：弃命从财，须要会财，若逢根气，命损无猜。假如丁生酉月，柱多庚辛，日干无气，只得弃命相从，运入北方财官旺地，乃为入格，南行灾。古歌云：日干无气满盘财，弃命相从是福胎，运旺财官皆福贵，如逢根助反为灾。

- 分字分词释义：

  - **弃命从财**：日主极弱、几近无气，而财星极旺，结构上“舍身而从财气”。
  - **须要会财，若逢根气，命损无猜**：从财之格必须财气成局，会合有情；若日主再得根气，则破从为不从，反致灾。
  - **丁生酉月，柱多庚辛，日干无气**：以丁火生于酉月、金多火绝为例，说明从财的典型情形。

- **规范化释义（primary_lang_explained）**：

  弃命从财，是一种极端的相从格：日主几乎完全失去自立之气，只能“随财而行”。若能真从，则反而可在财旺之岁运中得福——例如投身商业体系、资本系统、财务结构中，成为财势的一部分；若半从不从、时有根气，则既无自立之力，又反受财势所压，易起大祸。

- 核心要点：

  - 弃命从财格只适用于**极端日弱、财极旺且成局**的命式，绝不可泛用。
  - 一旦立从，就忌再有比劫、印绶来扶身，反而破格成灾。
  - 运程宜往财旺之乡，顺势而为；逆行身旺之地，常有大挫折。

- 详细解说：

  从现代视角看，可以把“弃命从财”理解为一种“完全卷入大体系”的人生轨迹：

  - 个人不再以“自我主导”作为主要路径，而是顺应某种庞大财务、组织或制度结构；
  - 若结构本身健康，则个体因之得福；若结构本身多凶险，则个体很难全身而退。

  判断是否真从，需详看：

  - 日主是否真无根、无印、无帮；
  - 财气是否一边倒、会局成势；
  - 岁运是否继续推财而不反向扶身。

- **校勘与字词辨析（双语）**：

  - 原文“命损无猜”“是福胎”等语，本稿在白话中仅以“格成则福、破从则祸”解释，不做宿命化的夸张断语。
  - **English**：
    - Avoids fatalistic exaggerations in interpretation.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_129]` `[trigger: 弃命从财]` `[factor_trigger: rigan_wuqi AND manpan_cai]` `[role: 主干]` 弃命从财，须要会财，若逢根气，命损无猜。 → 《三命通会》卷六#弃命从财
  - `[ns_smth_06_130]` `[trigger: 日干无气]` `[factor_trigger: rigan_wuqi AND qiming_xiangcong]` `[role: 主干依赖]` 日干无气满盘财，弃命相从是福胎。 → 《三命通会》卷六#弃命从财
  - `[ns_smth_06_131]` `[trigger: 逢根反灸]` `[factor_trigger: feng_genqi AND fan_weizai]` `[role: 条件分支]` 如逢根助反为灸。从财格最忌岁运扶身。 → 《三命通会》卷六#弃命从财
  - `[ns_smth_06_132]` `[trigger: 运旺财官]` `[factor_trigger: yun_wang_caiguan AND fugui]` `[role: 总结]` 运旺财官皆福贵，南行灾。 → 《三命通会》卷六#弃命从财"""
    normalized_text_zh: str = """"""
    subject: str = "弃命从财与极端相从格"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_34', 'bazi_semantic', 'bazi_structure_degree', 'bazi_semantic', 'bazi_state_degree_22', 'bazi_semantic', 'bazi_state_factor_25', 'bazi_semantic', 'bazi_condition_day_master_1', 'bazi_semantic', 'bazi_condition_factor_192', 'bazi_semantic', 'source_ref', 'rel_smth_06_124', 'qiming_congcai_presence', 'rel_smth_06_125', 'caiqi_huiju', 'rel_smth_06_126', 'rizhu_fenggen_risk', 'evi_smth_06_124', 'qiming_congcai_presence', 'rule_congcai', 'evi_smth_06_125', 'suiyun_tuicai', 'rule_tuicai', 'evi_smth_06_126', 'rizhu_fenggen_risk', 'rule_pocong', 'map_smth_06_083', 'map_smth_06_084']
    
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
        l1_anchor="smth_v1.0.0_弃命从财与极端相从格_001_L1",
    )
    version: str = "1.0.0"
