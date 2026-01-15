"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412723
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
    semantic_id="smth_v1.0.0_时逢生印与晚年荫助_001",
    book_id="sanming",
    engine_id="bazi"
)
class 时逢生印与晚年荫助(SemanticEntry):
    """
    - **原文（source_text）**：

  时逢生印：如甲日子时，取子中癸水为印，资助日主。其人足智多谋，安享食禄。年月上要见辛官生印，运行西北，官印乃为贵命。若柱逢戊己土重，更有午字冲破，运...
    """
    
    original_text: str = """- **原文（source_text）**：

  时逢生印：如甲日子时，取子中癸水为印，资助日主。其人足智多谋，安享食禄。年月上要见辛官生印，运行西北，官印乃为贵命。若柱逢戊己土重，更有午字冲破，运历东南，官印衰绝，百事无成，公吏肆市人也。

- 分字分词释义：

  - **时逢生印**：时支落在印星之地，如甲日子时，子中癸水为甲之印。
  - **足智多谋，安享食禄**：印在时，多主晚年仍得智谋与资源扶持，能安享俸禄。
  - **官印相生**：辛官生癸印，形成官印相生之局，为贵命的重要标志之一。

- **规范化释义（primary_lang_explained）**：

  时逢生印，强调“晚年仍有印绶之气相扶”：

  - 在中晚年阶段，仍能保持学习与适应能力；
  - 容易得到制度、单位、长辈或子女的支持；
  - 若再有官印相生，则主仕途或专业生涯在后半程仍有提升空间。

- 核心要点：

  - 时逢生印，是印绶格中的一个加分点，偏重后半生与子息相关的荫助。
  - 喜官印相生、忌重土冲破、水火相战。

- 详细解说：

  在现代职业路径中，此类配置常见于：

  - 退休前后仍有返聘、顾问、讲学机会的人；
  - 因专业权威与人格信用，在晚年仍被机构与社会所需要。

  若命局印弱、又被财伤之，则需警惕在晚年阶段“资格被废、信誉受损”的风险，行运上宜避财乡、少入争名夺利之局。

- **校勘与字词辨析（双语）**：

  - 原文以“公吏肆市人”等语形容破格之象，本稿在白话中仅作“失去体制内位置、流于平常”理解，不作身份歧视。
  - **English**：
    - Modern interpretation avoids status-based discrimination.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_145]` `[trigger: 时逢生印]` `[factor_trigger: shizhu_yinxing AND wannian_yinzhu]` `[role: 主干]` 时逢生印，如甲日子时，取子中癸水为印，资助日主。 → 《三命通会》卷六#时逢生印
  - `[ns_smth_06_146]` `[trigger: 足智多谋]` `[factor_trigger: zuzhi_duomou AND anxiang_shilu]` `[role: 主干依赖]` 其人足智多谋，安享食禄。 → 《三命通会》卷六#时逢生印
  - `[ns_smth_06_147]` `[trigger: 官印贵命]` `[factor_trigger: guan_shengyin AND xibei_guanyin]` `[role: 条件分支]` 年月上要见辛官生印，运行西北，官印乃为贵命。 → 《三命通会》卷六#时逢生印
  - `[ns_smth_06_148]` `[trigger: 土重冲破]` `[factor_trigger: wuji_tuzhong AND wu_chongpo]` `[role: 总结]` 若柱逢戊己土重，更有午字冲破，百事无成。 → 《三命通会》卷六#时逢生印"""
    normalized_text_zh: str = """"""
    subject: str = "时逢生印与晚年荫助"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_38', 'bazi_semantic', 'bazi_structure_hour_pillar_combo', 'bazi_semantic', 'bazi_state_degree_26', 'bazi_semantic', 'bazi_state_factor_28', 'bazi_semantic', 'bazi_condition_earth_3', 'bazi_semantic', 'bazi_condition_factor_199', 'bazi_semantic', 'source_ref', 'rel_smth_06_136', 'shifeng_shengyin_presence', 'rel_smth_06_137', 'guanyin_peihe', 'rel_smth_06_138', 'caitu_poyin_risk', 'evi_smth_06_136', 'shifeng_shengyin_presence', 'rule_shiyin', 'evi_smth_06_137', 'guanyin_peihe', 'rule_guanshengyin', 'evi_smth_06_138', 'yuncheng_fangxiang_risk', 'rule_yuncheng', 'map_smth_06_091', 'map_smth_06_092']
    
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
        l1_anchor="smth_v1.0.0_时逢生印与晚年荫助_001_L1",
    )
    version: str = "1.0.0"
