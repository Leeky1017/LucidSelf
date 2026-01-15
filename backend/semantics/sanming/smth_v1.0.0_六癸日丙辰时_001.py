"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339653
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
    semantic_id="smth_v1.0.0_六癸日丙辰时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六癸日丙辰时(SemanticEntry):
    """
    - 原文（source_text）：
  六癸日生时丙辰，偏官无气未为贫。若无木气通其局，定是清高福禄人。
  癸日丙辰时，身坐官库，癸用戊己为官，辰上土墓为官库，见丙为财，辰为水局，丙火无气，癸水合...
    """
    
    original_text: str = """- 原文（source_text）：
  六癸日生时丙辰，偏官无气未为贫。若无木气通其局，定是清高福禄人。
  癸日丙辰时，身坐官库，癸用戊己为官，辰上土墓为官库，见丙为财，辰为水局，丙火无气，癸水合局，柱无甲破官损库，主贵。

- 分字分词释义：
  - **身坐官库**：辰为水库，亦为土库（官库）。
  - **偏官无气**：辰中戊土为正官，己土为偏官。此处“偏官无气”可能指辰中己土无力，或指丙火（财）无气生官。
  - **无木气**：忌甲木伤官损库中官星。

- **规范化释义（primary_lang_explained）**：
  六癸日出生于丙辰时，辰为官库（戊土），丙火正财透出。辰亦为水库，助身。若柱中无甲木伤官破损官库，主清高有福禄。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Gui Days with Bing-Chen Hour":

  - Partial Official no qi not yet poverty—body sits on Official treasury; Chen is Earth tomb (Official treasury).
  - If no Wood qi connecting the pattern, definitely a lofty fortune-salary person.
  - Bing Fire Wealth reveals; Chen also Water bureau helping body; if pillars have no Jia breaking Official damaging treasury, noble.
  - Key: Official treasury pattern fears Wounded Officer (Wood) breaking; body-treasury mutually beneficial.

- 核心要点：
  - **财官双美**：丙戊。
  - **官库**：辰。
  - **忌伤官**：甲木。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_209]` `[trigger: 偏官无气]` `[factor_trigger: pianguan_wuqi AND wei_wei_pin]` `[role: 主干]` 六癸日生时丙辰，偏官无气未为贫。 → 《三命通会》卷九#六癸日丙辰时
  - `[ns_smth_09_210]` `[trigger: 若无木气]` `[factor_trigger: ruo_wu_muqi AND qinggao_fulu]` `[role: 主干依赖]` 若无木气通其局，定是清高福禄人。 → 《三命通会》卷九#六癸日丙辰时
  - `[ns_smth_09_211]` `[trigger: 身坐官库]` `[factor_trigger: shenzuo_guanku AND jian_bing_weicai]` `[role: 条件分支]` 身坐官库，癸用戊己为官，辰为土墓为官库，见丙为财。 → 《三命通会》卷九#六癸日丙辰时
  - `[ns_smth_09_212]` `[trigger: 无甲主贵]` `[factor_trigger: wu_jia_zhugui AND guanku_chengxiang]` `[role: 总结]` 柱无甲破官损库，主贵。 → 《三命通会》卷九#六癸日丙辰时"""
    normalized_text_zh: str = """"""
    subject: str = "六癸日丙辰时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_gui', 'bazi_semantic', 'bazi_state_factor_314', 'bazi_semantic', 'bazi_relation_factor_129', 'bazi_semantic', 'bazi_state_factor_315', 'bazi_semantic', 'hour_branch_chen', 'bazi_semantic', 'bazi_condition_jia_wood', 'bazi_semantic', 'source_ref', 'rel_smth_09_157', 'shenzuo_guanku', 'rel_smth_09_158', 'wu_muqi', 'rel_smth_09_159', 'jiamu_poku', 'evi_smth_09_157', 'shenzuo_guanku', 'rule_shenzuo_guanku1', 'evi_smth_09_158', 'qinggao_fulu', 'rule_qinggao_fulu1', 'evi_smth_09_159', 'sungu_jianfu', 'rule_jiamu_poku1', 'map_smth_09_105', 'map_smth_09_106']
    
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
        l1_anchor="smth_v1.0.0_六癸日丙辰时_001_L1",
    )
    version: str = "1.0.0"
