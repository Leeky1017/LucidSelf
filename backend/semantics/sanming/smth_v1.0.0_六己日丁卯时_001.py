"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339335
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
    semantic_id="smth_v1.0.0_六己日丁卯时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六己日丁卯时(SemanticEntry):
    """
    - 原文（source_text）：
  六己日生时丁卯，己土卯上见煞星。丁火偏印不伏煞，骨肉离乡路旁行。
  己日丁卯时，己以甲为官，乙为煞，卯上明乙暗甲。丁为偏印，不能化煞。己卯，病神。若身强，年...
    """
    
    original_text: str = """- 原文（source_text）：
  六己日生时丁卯，己土卯上见煞星。丁火偏印不伏煞，骨肉离乡路旁行。
  己日丁卯时，己以甲为官，乙为煞，卯上明乙暗甲。丁为偏印，不能化煞。己卯，病神。若身强，年月有制伏，不犯刑破，贵；身弱，辛苦、无寸土。

- 分字分词释义：
  - **煞星**：卯为乙木禄旺之地，乙木为己土七煞，故云“卯上见煞星”。虽卯中亦藏甲木（中气），但乙木（本气）为主。
  - **丁火偏印不伏煞**：丁火为己土偏印（枭神），虽然印能化煞，但丁火阴柔，化煞之力不如丙火正印有力（原文观点），且卯木生丁火，更助火势，若无水润局，恐燥土不生金，难制煞。
  - **病神**：己长生在酉，沐浴申，病在卯（寄生十二宫），故己卯为自坐病地。

- **规范化释义（primary_lang_explained）**：
  六己日出生于丁卯时，卯木七煞当权。丁火透出为偏印，但偏印化煞护身之力不足（或指丁火生身但不制煞，反泄木气生燥土）。若日主身强，年月有食神伤官制煞，且无刑冲破坏，可为贵命。若身弱无助，七煞攻身，主骨肉分离、离乡背井、辛苦劳碌、贫无立锥之地。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ji Days with Ding-Mao Hour":

  - Mao Wood Seven-Killing is in prosperity position; Ding Fire Partial Seal reveals but cannot fully transform killing.
  - If Day Master is strong with controlling factors (Eating God/Hurting Official) in year-month pillars and no punishment-clash, indicates nobility.
  - If body is weak without support, Seven-Killing attacks self—indicates separation from kin, leaving hometown, hardship and poverty.
  - Key: Partial Seal's limited power to transform killing; strong body with control is essential.

- 核心要点：
  - **时上七煞格**：卯为七煞禄地，煞重。
  - **偏印化煞**：丁卯为煞印相生，但己土坐卯病地，需身旺方吉。
  - **身弱为忌**：身弱煞旺，无制化，主贫贱刑伤。

- 详细解说：
  此格关键在于“煞重身轻”。卯为日主之病地，七煞之旺地，若无其他帮扶，日主难以胜任。丁火虽能化煞生身，但属阴火，力较柔。若年月见水生木，煞更旺；见金制煞，或火土帮身，方有转机。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_013]` `[trigger: 卯上见煞]` `[factor_trigger: mao_shang_jian_sha AND sha_xing]` `[role: 主干]` 六己日生时丁卯，己土卯上见煞星。 → 《三命通会》卷九#六己日丁卯时
  - `[ns_smth_09_014]` `[trigger: 偏印不伏煞]` `[factor_trigger: pianyin_bufusha AND gurou_lixiang]` `[role: 主干依赖]` 丁火偏印不伏煞，骨肉离乡路旁行。 → 《三命通会》卷九#六己日丁卯时
  - `[ns_smth_09_015]` `[trigger: 身强有制]` `[factor_trigger: shenqiang_youzhi AND gui]` `[role: 条件分支]` 若身强，年月有制伏，不犯刑破，贵。 → 《三命通会》卷九#六己日丁卯时
  - `[ns_smth_09_016]` `[trigger: 身弱辛苦]` `[factor_trigger: shenruo_xinku AND wucuntu]` `[role: 总结]` 身弱，辛苦、无寸土。 → 《三命通会》卷九#六己日丁卯时"""
    normalized_text_zh: str = """"""
    subject: str = "六己日丁卯时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_ji', 'bazi_semantic', 'bazi_state_factor_256', 'bazi_semantic', 'bazi_relation_pianyin', 'bazi_semantic', 'bazi_state_factor_257', 'bazi_semantic', 'hour_branch_mao', 'bazi_semantic', 'bazi_condition_factor_112', 'bazi_semantic', 'source_ref', 'rel_smth_09_010', 'shaxing_dangquan', 'rel_smth_09_011', 'pianyin_huasha', 'rel_smth_09_012', 'shenruo_wuzhu', 'evi_smth_09_010', 'shaxing_dangquan', 'rule_shaxing1', 'evi_smth_09_011', 'pianyin_huasha', 'rule_pianyin_huasha1', 'evi_smth_09_012', 'shenruo_wuzhu', 'rule_guroulixiang1', 'map_smth_09_007', 'map_smth_09_008']
    
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
        l1_anchor="smth_v1.0.0_六己日丁卯时_001_L1",
    )
    version: str = "1.0.0"
