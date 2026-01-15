"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339469
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
    semantic_id="smth_v1.0.0_六庚日庚辰时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六庚日庚辰时(SemanticEntry):
    """
    - 原文（source_text）：
  六庚日生时庚辰，金火秋生气象纯。若有魁罡包贵贱，财官喜忌六官分。
  庚日庚辰时，金水清白。六庚之中，庚戌庚辰为魁罡，怕见财官刑冲；不见，主为人粗豪暴勇而贵，...
    """
    
    original_text: str = """- 原文（source_text）：
  六庚日生时庚辰，金火秋生气象纯。若有魁罡包贵贱，财官喜忌六官分。
  庚日庚辰时，金水清白。六庚之中，庚戌庚辰为魁罡，怕见财官刑冲；不见，主为人粗豪暴勇而贵，见则祸患百出。庚子、庚寅、庚午、庚申，喜见财官。生秋月，为人秀丽，不贵则富。若身不化，得甲乙丁透出，生火木分野，亦作财官论。喜月气通运者，吉。

- 分字分词释义：
  - **金火秋生**：生于秋月（金旺），又有火炼金，气象纯粹。
  - **魁罡**：庚辰、庚戌日为魁罡日，不论财官，只论身强煞旺。
  - **井栏叉格**：庚申、庚子、庚辰日，地支申子辰全，天干透三庚，为井栏叉格。

- **规范化释义（primary_lang_explained）**：
  六庚日出生于庚辰时，若生于秋月，金旺有火，气象纯正。若是庚辰、庚戌日，为魁罡格，忌见财官刑冲，不见财官主掌权贵（武职），见则祸患。若是其他庚日（子、寅、午、申），喜见财官。若地支成申子辰水局，为井栏叉格，忌见寅午戌火局。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Geng Days with Geng-Chen Hour":

  - Metal-Fire autumn-born atmosphere pure; Metal and Water clear and white.
  - If Kui-Gang (Geng-Chen or Geng-Xu day), fears Wealth-Official punishment-clash; without them indicates rough-heroic-brave nobility; with them disasters abound.
  - Other Geng days (Zi, Yin, Wu, Shen) delight in Wealth-Official; autumn-born indicates elegant beauty, if not noble then wealthy.
  - Key: Distinguish Kui-Gang pattern from regular; or Well-Railing Fork pattern if Shen-Zi-Chen complete.

- 核心要点：
  - **魁罡格**：庚辰日庚辰时，重魁罡，忌财官。
  - **井栏叉**：润下，喜东方运。
  - **比劫帮身**：庚辰时，印比帮身，身强。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_065]` `[trigger: 金火秋生]` `[factor_trigger: jinhuo_qiusheng AND qixiang_chun]` `[role: 主干]` 六庚日生时庚辰，金火秋生气象纯。 → 《三命通会》卷九#六庚日庚辰时
  - `[ns_smth_09_066]` `[trigger: 魁罡贵贱]` `[factor_trigger: kuigang_guijian AND caiguan_xiji]` `[role: 主干依赖]` 若有魁罡包贵贱，财官喜忌六官分。 → 《三命通会》卷九#六庚日庚辰时
  - `[ns_smth_09_067]` `[trigger: 魁罡忌财官]` `[factor_trigger: kuigang_ji_caiguan AND cuhaobao_gui]` `[role: 条件分支]` 庚戌庚辰为魁罡，怕见财官刑冲；不见，主粗豪暴勇而贵。 → 《三命通会》卷九#六庚日庚辰时
  - `[ns_smth_09_068]` `[trigger: 喜见财官]` `[factor_trigger: xi_jian_caiguan AND xiuli_fugui]` `[role: 总结]` 庚子、庚寅、庚午、庚申，喜见财官。生秋月，为人秀丽，不贵则富。 → 《三命通会》卷九#六庚日庚辰时"""
    normalized_text_zh: str = """"""
    subject: str = "六庚日庚辰时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_geng', 'bazi_semantic', 'bazi_state_factor_275', 'bazi_semantic', 'bazi_relation_factor_118', 'bazi_semantic', 'bazi_state_metal_water_2', 'bazi_semantic', 'hour_branch_chen', 'bazi_semantic', 'bazi_condition_factor_123', 'bazi_semantic', 'source_ref', 'rel_smth_09_049', 'kuigang_ge', 'rel_smth_09_050', 'jinglancha_ge', 'rel_smth_09_051', 'qiusheng_wucaiguan', 'evi_smth_09_049', 'jinsui_qingbai', 'rule_jinqiu_qixiang1', 'evi_smth_09_050', 'kuigang_ge', 'rule_kuigang_bao1', 'evi_smth_09_051', 'qiusheng_wucaiguan', 'rule_caiguan_xiji1', 'map_smth_09_033', 'map_smth_09_034']
    
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
        l1_anchor="smth_v1.0.0_六庚日庚辰时_001_L1",
    )
    version: str = "1.0.0"
