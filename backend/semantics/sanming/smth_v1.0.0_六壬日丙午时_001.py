"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339781
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
    semantic_id="smth_v1.0.0_六壬日丙午时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六壬日丙午时(SemanticEntry):
    """
    - 原文（source_text）：
  六壬日生时丙午，聚财之地坐胞胎。月逢金水须富贵，弃命从来是就财。
  壬日丙午时，禄马三奇。壬以己为官，丙丁为财，午上丁己是禄马，壬水受胎，有倚托，通金水月气...
    """
    
    original_text: str = """- 原文（source_text）：
  六壬日生时丙午，聚财之地坐胞胎。月逢金水须富贵，弃命从来是就财。
  壬日丙午时，禄马三奇。壬以己为官，丙丁为财，午上丁己是禄马，壬水受胎，有倚托，通金水月气，就财生旺，主富贵，通火气，亦贵。

- 分字分词释义：
  - **聚财之地**：午为丁火（财）禄地，财旺。
  - **坐胞胎**：壬水在午为胎地。
  - **弃命就财**：若日主无根，满局火土，从财格（或从杀）。

- **规范化释义（primary_lang_explained）**：
  六壬日出生于丙午时，午中藏丁火（正财）、己土（正官），财官双美（禄马三奇）。壬水在午受胎。若日主有金水倚托，身旺任财，主富贵。若生于火月，火土太旺，日主无根，作弃命就财格（从财），亦贵。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ren Days with Bing-Wu Hour":

  - Gathering-Wealth place sits embryo-fetus—Wu is Ding Fire (Wealth) Prosperity place; Ren Water in Wu is Fetal stage.
  - Month encountering Metal-Water must wealthy-noble; abandoning life following becomes wealth.
  - Salary-Horse Three Wonders; Wu above Ding-Ji is Salary-Horse; with support connecting Metal-Water monthly qi, following Wealth generating prosperous, wealthy-noble.
  - Key: Body strong normal pattern; body extremely weak becomes Following-Wealth pattern; both can achieve nobility.

- 核心要点：
  - **财官双美**：丁己同宫。
  - **偏财透干**：丙火透。
  - **从格/正格**：视身强弱定。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_169]` `[trigger: 聚财之地]` `[factor_trigger: jucai_zhidi AND zuo_baotai]` `[role: 主干]` 六壬日生时丙午，聚财之地坐胞胎。 → 《三命通会》卷九#六壬日丙午时
  - `[ns_smth_09_170]` `[trigger: 月逢金水]` `[factor_trigger: yuefeng_jinshui AND xu_fugui]` `[role: 主干依赖]` 月逢金水须富贵，弃命从来是就财。 → 《三命通会》卷九#六壬日丙午时
  - `[ns_smth_09_171]` `[trigger: 禄马三奇]` `[factor_trigger: luma_sanqi AND ding_ji_tonglu]` `[role: 条件分支]` 壬以己为官，丙丁为财，午上丁己是禄马。 → 《三命通会》卷九#六壬日丙午时
  - `[ns_smth_09_172]` `[trigger: 通火气贵]` `[factor_trigger: tong_huoqi_gui AND jiucai_shengwang]` `[role: 总结]` 有倚托，通金水月气，就财生旺，主富贵，通火气，亦贵。 → 《三命通会》卷九#六壬日丙午时"""
    normalized_text_zh: str = """"""
    subject: str = "六壬日丙午时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_ren', 'bazi_semantic', 'bazi_state_factor_337', 'bazi_semantic', 'bazi_relation_factor_135', 'bazi_semantic', 'bazi_state_factor_338', 'bazi_semantic', 'hour_branch_wu', 'bazi_semantic', 'bazi_condition_metal_water_fire', 'bazi_semantic', 'source_ref', 'rel_smth_09_127', 'luma_sanqi', 'rel_smth_09_128', 'tong_jinshui_huoyue', 'rel_smth_09_129', 'qiming_jiucai', 'evi_smth_09_127', 'luma_sanqi', 'rule_luma_sanqi_bingwu1', 'evi_smth_09_128', 'tong_jinshui_huoyue', 'rule_tong_jinshui_fuqui1', 'evi_smth_09_129', 'qiming_jiucai', 'rule_qiming_jiucai1', 'map_smth_09_085', 'map_smth_09_086']
    
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
        l1_anchor="smth_v1.0.0_六壬日丙午时_001_L1",
    )
    version: str = "1.0.0"
