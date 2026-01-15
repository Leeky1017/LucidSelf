"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339616
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
    semantic_id="smth_v1.0.0_六癸日壬子时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六癸日壬子时(SemanticEntry):
    """
    - 原文（source_text）：
  六癸日生时壬子，青云得路最为奇。若无己土冲克破，自有功名显达时。
  癸日壬子时，日禄归时，癸水子上建禄，若年月干支无戊己午未字刑冲破害，三元有倚托，通月气者...
    """
    
    original_text: str = """- 原文（source_text）：
  六癸日生时壬子，青云得路最为奇。若无己土冲克破，自有功名显达时。
  癸日壬子时，日禄归时，癸水子上建禄，若年月干支无戊己午未字刑冲破害，三元有倚托，通月气者，文章秀丽，官职显达；若通木气月，亦贵。如柱透己，有甲合，亦贵。否则，反复。

- 分字分词释义：
  - **青云得路**：即日禄归时格。癸禄在子。
  - **冲克破**：午冲子，未穿子，戊己土克水（官煞混杂）。

- **规范化释义（primary_lang_explained）**：
  六癸日出生于壬子时，为日禄归时格（建禄）。若年月柱中无戊己土克水，无午火冲子，无未土穿子，且日主有倚托（印比），通月气，主文章秀丽，官职显达。若生于木月（食伤），亦贵。若柱中透己土（煞），有甲木（伤官）合之，去煞留官（或合煞），亦贵。否则，成败反复。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Gui Days with Ren-Zi Hour":

  - Blue cloud gains road most wonderful—Day Salary Returns Time pattern; Gui Water establishes Salary at Zi.
  - If no Ji Earth clashing-controlling to break, naturally has achievement fame prominence time.
  - If year-month stems-branches have no Wu-Ji-Wu-Wei punishing-clashing-breaking-harming, three origins have support connecting monthly qi, literary elegant official prominent.
  - Key: Day Salary Returns Time fears Official-Killing filling in or clashing breaking.

- 核心要点：
  - **日禄归时**：癸禄在子。
  - **忌财官**：归禄忌官星填实及财星破禄（午冲子）。
  - **喜食伤**：木运泄秀。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_193]` `[trigger: 青云得路]` `[factor_trigger: qingyun_delu AND zui_wei_qi]` `[role: 主干]` 六癸日生时壬子，青云得路最为奇。 → 《三命通会》卷九#六癸日壬子时
  - `[ns_smth_09_194]` `[trigger: 若无己土]` `[factor_trigger: ruo_wu_jitu AND zi_you_gongming]` `[role: 主干依赖]` 若无己土冲克破，自有功名显达时。 → 《三命通会》卷九#六癸日壬子时
  - `[ns_smth_09_195]` `[trigger: 日禄归时]` `[factor_trigger: rilu_guishi AND wenzhang_xiuli]` `[role: 条件分支]` 日禄归时，若年月无戊己午未字刑冲破害，文章秀丽，官职显达。 → 《三命通会》卷九#六癸日壬子时
  - `[ns_smth_09_196]` `[trigger: 通木气贵]` `[factor_trigger: tong_muqi_gui AND tou_ji_jia_he]` `[role: 总结]` 若通木气月，亦贵。如柱透己，有甲合，亦贵。否则，反复。 → 《三命通会》卷九#六癸日壬子时"""
    normalized_text_zh: str = """"""
    subject: str = "六癸日壬子时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_gui', 'bazi_semantic', 'bazi_state_factor_346', 'bazi_semantic', 'bazi_state_factor_345', 'bazi_semantic', 'bazi_state_factor_308', 'bazi_semantic', 'hour_branch_zi', 'bazi_semantic', 'bazi_condition_wu_ji_wu_wei', 'bazi_semantic', 'source_ref', 'rel_smth_09_145', 'rilu_guishi', 'rel_smth_09_146', 'tong_muqi_youtuo', 'rel_smth_09_147', 'po_lu_xingchong', 'evi_smth_09_145', 'qingyun_delu', 'rule_qingyun_delu_gui_zi1', 'evi_smth_09_146', 'wuwuji_wuwei', 'rule_wuwuji_wuwei1', 'evi_smth_09_147', 'chengbai_fanfu', 'rule_chengbai_fanfu1', 'map_smth_09_097', 'map_smth_09_098']
    
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
        l1_anchor="smth_v1.0.0_六癸日壬子时_001_L1",
    )
    version: str = "1.0.0"
