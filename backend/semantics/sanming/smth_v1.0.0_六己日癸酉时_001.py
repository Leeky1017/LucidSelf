"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339398
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
    semantic_id="smth_v1.0.0_六己日癸酉时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六己日癸酉时(SemanticEntry):
    """
    - 原文（source_text）：
  六己日生时癸酉，偏财长生食神旺。若无破害富贵多，教化人间显名望。
  己日癸酉时，食神生财。己以癸为财，辛为食。酉上癸水病，辛金旺。若通月气，身旺，贵；不通，...
    """
    
    original_text: str = """- 原文（source_text）：
  六己日生时癸酉，偏财长生食神旺。若无破害富贵多，教化人间显名望。
  己日癸酉时，食神生财。己以癸为财，辛为食。酉上癸水病，辛金旺。若通月气，身旺，贵；不通，富。

- 分字分词释义：
  - **偏财长生**：原文“偏财长生”恐误，癸水长生在卯，酉为病地。但酉金生癸水，金白水清，财源不断。
  - **食神旺**：酉为辛金禄地，食神极旺。

- **规范化释义（primary_lang_explained）**：
  六己日出生于癸酉时，食神辛金当令，生偏财癸水。若无刑冲破害，主富贵双全，且能在人间教化众生，名望显赫（食神主名声、技艺）。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ji Days with Gui-You Hour":

  - Eating God Xin Metal at You is at fortune position (extremely prosperous); generates Gui Water Indirect Wealth.
  - Without break-harm, indicates abundant riches and nobility, able to educate and influence the world with great fame.
  - If passing monthly qi with strong body, indicates nobility; without monthly qi, indicates wealth.
  - Key: Eating God generating Wealth pattern; prosperous food-god brings fame and fortune together.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_037]` `[trigger: 偏财长生]` `[factor_trigger: piancai_changsheng AND shishen_wang]` `[role: 主干]` 六己日生时癸酉，偏财长生食神旺。 → 《三命通会》卷九#六己日癸酉时
  - `[ns_smth_09_038]` `[trigger: 无破害富贵]` `[factor_trigger: wu_pohai_fugui AND jiaohua_renjian]` `[role: 主干依赖]` 若无破害富贵多，教化人间显名望。 → 《三命通会》卷九#六己日癸酉时
  - `[ns_smth_09_039]` `[trigger: 通月身旺]` `[factor_trigger: tongyue_shenwang AND gui]` `[role: 条件分支]` 若通月气，身旺，贵。 → 《三命通会》卷九#六己日癸酉时
  - `[ns_smth_09_040]` `[trigger: 不通亦富]` `[factor_trigger: butong_yifu AND shishen_shengcai]` `[role: 总结]` 不通，富。 → 《三命通会》卷九#六己日癸酉时"""
    normalized_text_zh: str = """"""
    subject: str = "六己日癸酉时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_ji', 'bazi_semantic', 'bazi_state_shishen_7', 'bazi_semantic', 'bazi_state_shishen_9', 'bazi_semantic', 'bazi_state_factor_265', 'bazi_semantic', 'hour_branch_you', 'bazi_semantic', 'bazi_condition_factor_118', 'bazi_semantic', 'source_ref', 'rel_smth_09_028', 'shishen_wang', 'rel_smth_09_029', 'shishen_shengcai', 'rel_smth_09_030', 'wupohai', 'evi_smth_09_028', 'shishen_wang', 'rule_shishen_wang1', 'evi_smth_09_029', 'wupohai', 'rule_wupohai_fugui1', 'evi_smth_09_030', 'jiaohua_renjian', 'rule_jiaohua_mingwang1', 'map_smth_09_019', 'map_smth_09_020']
    
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
        l1_anchor="smth_v1.0.0_六己日癸酉时_001_L1",
    )
    version: str = "1.0.0"
