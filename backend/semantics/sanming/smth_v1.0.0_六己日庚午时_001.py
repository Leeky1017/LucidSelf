"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339367
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
    semantic_id="smth_v1.0.0_六己日庚午时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六己日庚午时(SemanticEntry):
    """
    - 原文（source_text）：
  六己日生时庚午，日禄归时格。庚金伤官，午上无气，己土归禄于午，明官暗禄。若年月无乙木破禄，无刑冲破害，贵。
  己日庚午时，日禄归时。己土见庚为伤官，午上庚金...
    """
    
    original_text: str = """- 原文（source_text）：
  六己日生时庚午，日禄归时格。庚金伤官，午上无气，己土归禄于午，明官暗禄。若年月无乙木破禄，无刑冲破害，贵。
  己日庚午时，日禄归时。己土见庚为伤官，午上庚金败地（沐浴），无气；己禄在午。若不通月气，亦主清贵；通月气，富贵。

- 分字分词释义：
  - **日禄归时**：己禄在午，时支为午，故名日禄归时（归禄格）。
  - **伤官无气**：庚金在午火之地处于败地（沐浴），受火克，伤官无力。
  - **明官暗禄**：原文“明官暗禄”恐有误，庚为伤官，非官；午为禄，非暗（时支本气）。可能指午中藏丁己，丁为印，己为比。或指庚金（伤官）虽然透出，但无气，不伤正官（若有）。实则应为“伤官泄秀”或“归禄”。
  - **乙木破禄**：乙木为七煞，克己土，或指乙木生午火太旺（木生火），或指乙庚合绊（伤官合煞）。此处“破禄”多指刑冲（子冲午）。

- **规范化释义（primary_lang_explained）**：
  六己日出生于庚午时，为日禄归时格。天干透出庚金伤官，但庚在午地无气（受克）。己土在时支午得禄。若年月柱无乙木七煞克身（或破禄），且地支无子冲午、丑穿午等刑冲，主贵。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ji Days with Geng-Wu Hour":

  - Day Fortune Returns to Hour pattern; Ji's fortune is at Wu; Geng Metal Hurting Official at Wu is in bathing position (powerless).
  - If year-month pillars have no Yi Wood breaking fortune and no punishment-clash, indicates nobility.
  - Even without monthly qi, still indicates refined nobility; with monthly qi, both riches and nobility.
  - Key: Fortune returns to hour indicates late prosperity; Hurting Official powerless does not harm nobility.

- 核心要点：
  - **归禄格**：己禄在午，主晚年福寿，归禄喜财，忌官（归禄格一般忌官星填实，但己土喜甲己合，情况稍异）。
  - **伤官坐死绝**：庚金无力，不伤贵气。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_025]` `[trigger: 日禄归时]` `[factor_trigger: rilu_guishi AND shangguan_wuqi]` `[role: 主干]` 六己日生时庚午，日禄归时格。 → 《三命通会》卷九#六己日庚午时
  - `[ns_smth_09_026]` `[trigger: 伤官无气]` `[factor_trigger: shangguan_wuqi AND bu_po_lu]` `[role: 主干依赖]` 庚金伤官，午上无气。 → 《三命通会》卷九#六己日庚午时
  - `[ns_smth_09_027]` `[trigger: 无刑冲破害]` `[factor_trigger: wu_xingchong_pohai AND gui]` `[role: 条件分支]` 若年月无乙木破禄，无刑冲破害，贵。 → 《三命通会》卷九#六己日庚午时
  - `[ns_smth_09_028]` `[trigger: 不通亦贵]` `[factor_trigger: butong_yigui AND tongyueqi_fugui]` `[role: 总结]` 若不通月气，亦主清贵；通月气，富贵。 → 《三命通会》卷九#六己日庚午时"""
    normalized_text_zh: str = """"""
    subject: str = "六己日庚午时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_ji', 'bazi_semantic', 'bazi_state_factor_345', 'bazi_semantic', 'bazi_relation_shangguan_8', 'bazi_semantic', 'bazi_state_factor_262', 'bazi_semantic', 'hour_branch_wu', 'bazi_semantic', 'bazi_condition_factor_115', 'bazi_semantic', 'source_ref', 'rel_smth_09_019', 'rilu_guishi', 'rel_smth_09_020', 'shangguan_wuqi', 'rel_smth_09_021', 'xingchong_polu', 'evi_smth_09_019', 'rilu_guishi', 'rule_rilu_guishi1', 'evi_smth_09_020', 'shangguan_wuqi', 'rule_shangguan_wuqi1', 'evi_smth_09_021', 'xingchong_polu', 'rule_wuxingchong_gui1', 'map_smth_09_013', 'map_smth_09_014']
    
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
        l1_anchor="smth_v1.0.0_六己日庚午时_001_L1",
    )
    version: str = "1.0.0"
