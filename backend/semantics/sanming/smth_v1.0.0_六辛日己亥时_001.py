"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339608
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
    semantic_id="smth_v1.0.0_六辛日己亥时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六辛日己亥时(SemanticEntry):
    """
    - 原文（source_text）：
  六辛日生时己亥，背禄剥官反破伤。如作飞天禄马贵，失时无合空忙忙。
  辛日己亥时，飞禄合局。辛以丙为官，亥上有旺壬伤，故官无气；如再得亥月或亥日，以亥冲出巳中...
    """
    
    original_text: str = """- 原文（source_text）：
  六辛日生时己亥，背禄剥官反破伤。如作飞天禄马贵，失时无合空忙忙。
  辛日己亥时，飞禄合局。辛以丙为官，亥上有旺壬伤，故官无气；如再得亥月或亥日，以亥冲出巳中丙火为官星。若是辛酉、辛丑合局，贵；其余辛无合。不通月气，无倚托，贫下；有倚托，吉。

- 分字分词释义：
  - **背禄剥官**：亥中壬水伤官旺，伤克丙火官星，故名背禄（背离官禄）。
  - **飞天禄马**：辛亥日亥时（或多亥），亥冲巳，巳中丙戊为辛之官印，为飞天禄马格。

- **规范化释义（primary_lang_explained）**：
  六辛日出生于己亥时，壬水伤官健旺，克制丙火官星，正官无气，甚至破格。但若生于亥月亥日，地支亥多，冲出巳中丙火官星，为飞天禄马格，主贵。若非飞天格，又无倚托，伤官见官，主贫下忙碌。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Xin Days with Ji-Hai Hour":

  - Back-Salary peel-Official instead breaks harms—Hai contains Ren Water Wounded Officer prosperous attacking Bing Fire Official.
  - If making Flying-Heaven Salary-Horse noble pattern, losing timing without combine empty busy-busy.
  - Hai clashes Si, Si contains Bing-Wu (Official-Seal) for Xin; if Xin-You or Xin-Chou combining bureau, noble; others no combine.
  - Key: Flying Heaven pattern requires multiple Hai clashing Si; otherwise Wounded Officer sees Official indicates poverty struggle.

- 核心要点：
  - **伤官格**：壬水旺，忌见官。
  - **飞天禄马**：亥冲巳，虚邀官星。
  - **枭印**：己土透，制伤。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_141]` `[trigger: 背禄剥官]` `[factor_trigger: beilu_boguan AND fan_poshang]` `[role: 主干]` 六辛日生时己亥，背禄剥官反破伤。 → 《三命通会》卷九#六辛日己亥时
  - `[ns_smth_09_142]` `[trigger: 飞天禄马]` `[factor_trigger: feitian_luma AND shishi_wuhe]` `[role: 主干依赖]` 如作飞天禄马贵，失时无合空忙忙。 → 《三命通会》卷九#六辛日己亥时
  - `[ns_smth_09_143]` `[trigger: 亥冲巳]` `[factor_trigger: hai_chong_si AND yu_guanxing]` `[role: 条件分支]` 以亥冲出巳中丙火为官星。 → 《三命通会》卷九#六辛日己亥时
  - `[ns_smth_09_144]` `[trigger: 合局为贵]` `[factor_trigger: heju_weigui AND xinyou_xinchou]` `[role: 总结]` 若是辛酉、辛丑合局，贵；其余辛无合。 → 《三命通会》卷九#六辛日己亥时"""
    normalized_text_zh: str = """"""
    subject: str = "六辛日己亥时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_xin', 'bazi_semantic', 'bazi_state_factor_305', 'bazi_semantic', 'bazi_relation_factor_126', 'bazi_semantic', 'bazi_state_factor_306', 'bazi_semantic', 'hour_branch_hai', 'bazi_semantic', 'bazi_condition_hai_si', 'bazi_semantic', 'source_ref', 'rel_smth_09_106', 'beilu_boguan', 'rel_smth_09_107', 'beilu_boguan', 'rel_smth_09_108', 'feitian_luma', 'evi_smth_09_106', 'beilu_boguan', 'rule_beilu_boguan1', 'evi_smth_09_107', 'kong_mangmang', 'rule_kongmangmang1', 'evi_smth_09_108', 'feitian_luma', 'rule_feitian_luma1', 'map_smth_09_071', 'map_smth_09_072']
    
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
        l1_anchor="smth_v1.0.0_六辛日己亥时_001_L1",
    )
    version: str = "1.0.0"
