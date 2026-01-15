"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339564
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
    semantic_id="smth_v1.0.0_六辛日甲午时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六辛日甲午时(SemanticEntry):
    """
    - 原文（source_text）：
  六辛日逢甲午时，暗鬼枭神真可畏。若无倚托反劳生，莫道六辛逢马贵。
  辛日甲午时，鬼旺身衰。辛用丁为鬼，己为倒食，甲为财。甲午木死则神无气，丁己健旺，虽见午为...
    """
    
    original_text: str = """- 原文（source_text）：
  六辛日逢甲午时，暗鬼枭神真可畏。若无倚托反劳生，莫道六辛逢马贵。
  辛日甲午时，鬼旺身衰。辛用丁为鬼，己为倒食，甲为财。甲午木死则神无气，丁己健旺，虽见午为天乙贵，平生反复；纵通旺气，亦贵不永。若生火土月，西方运，贵。

- 分字分词释义：
  - **暗鬼枭神**：午中丁火（七煞/鬼）、己土（枭神/倒食）。
  - **鬼旺身衰**：午为火旺之地，辛金受克（病地）。
  - **马贵**：午为辛金贵人，甲为财（马）。

- **规范化释义（primary_lang_explained）**：
  六辛日出生于甲午时，午中丁火七煞和己土枭神健旺，辛金受克泄，身衰。甲木财星在午为死地。虽然午是天乙贵人，但煞旺攻身，平生多反复，富贵不长久。若生于火土月（印旺），且行西方金运帮身，方贵。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Xin Days with Jia-Wu Hour":

  - Dark ghost owl spirit truly fearsome—Wu hides Ding Fire Seven-Killing and Ji Earth Partial Seal both prosperous attacking body.
  - If no support instead toils for life; don't say Six Xin meeting Horse (Wu) is noble.
  - Although Wu is Heavenly Noble, ghost prosperous body declining, life full of reversals; even if connecting prosperous qi, nobility not lasting.
  - Key: Killing heavy body light requires Seal-Parallel support; born Fire-Earth month traveling West luck then noble.

- 核心要点：
  - **煞重身轻**：午火克金。
  - **枭神夺食**：己土夺癸。
  - **身旺为急**：需印比帮身。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_121]` `[trigger: 暗鬼枭神]` `[factor_trigger: angui_xiaoshen AND zhen_kewei]` `[role: 主干]` 六辛日逢甲午时，暗鬼枭神真可畏。 → 《三命通会》卷九#六辛日甲午时
  - `[ns_smth_09_122]` `[trigger: 无倚托劳生]` `[factor_trigger: wu_yituo_laosheng AND modao_magui]` `[role: 主干依赖]` 若无倚托反劳生，莫道六辛逢马贵。 → 《三命通会》卷九#六辛日甲午时
  - `[ns_smth_09_123]` `[trigger: 鬼旺身衰]` `[factor_trigger: guiwang_shenshuai AND fugu_buyong]` `[role: 条件分支]` 鬼旺身衰，虽见午为天乙贵，平生反复。 → 《三命通会》卷九#六辛日甲午时
  - `[ns_smth_09_124]` `[trigger: 火土月西运]` `[factor_trigger: huotu_yue_xiyun AND gui]` `[role: 总结]` 若生火土月，西方运，贵。 → 《三命通会》卷九#六辛日甲午时"""
    normalized_text_zh: str = """"""
    subject: str = "六辛日甲午时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_xin', 'bazi_semantic', 'bazi_state_factor_296', 'bazi_semantic', 'bazi_state_factor_319', 'bazi_semantic', 'bazi_state_factor_297', 'bazi_semantic', 'hour_branch_wu', 'bazi_semantic', 'bazi_condition_fire_earth_1', 'bazi_semantic', 'source_ref', 'rel_smth_09_091', 'an_gui_xiaoshen', 'rel_smth_09_092', 'gui_wang_shenshuai', 'rel_smth_09_093', 'huotu_yue_xiyun', 'evi_smth_09_091', 'an_gui_xiaoshen', 'rule_angui_xiaoshen1', 'evi_smth_09_092', 'gui_wang_shenshuai', 'rule_wuyitu_laosheng1', 'evi_smth_09_093', 'huotu_yue_xiyun', 'rule_huotu_xiyun1', 'map_smth_09_061', 'map_smth_09_062']
    
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
        l1_anchor="smth_v1.0.0_六辛日甲午时_001_L1",
    )
    version: str = "1.0.0"
