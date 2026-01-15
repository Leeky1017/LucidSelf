"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339388
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
    semantic_id="smth_v1.0.0_六己日壬申时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六己日壬申时(SemanticEntry):
    """
    - 原文（source_text）：
  六己日生时壬申，水旺金重福不轻。月在春冬须显贵，柱无财印亦知名。
  己日壬申时，财官双美。己以壬为财，甲为官，申上壬水长生，甲木绝地。若通月气，身旺，贵；不...
    """
    
    original_text: str = """- 原文（source_text）：
  六己日生时壬申，水旺金重福不轻。月在春冬须显贵，柱无财印亦知名。
  己日壬申时，财官双美。己以壬为财，甲为官，申上壬水长生，甲木绝地。若通月气，身旺，贵；不通，富。

- 分字分词释义：
  - **水旺金重**：壬水（财）长生在申，申金（伤官）得禄，金水相生，财旺伤官旺。
  - **财官双美**：虽甲木官星在申绝地，但壬水财旺能生官（财旺自然生官）。或指申中藏庚壬戊，财局。

- **规范化释义（primary_lang_explained）**：
  六己日出生于壬申时，金水两旺（伤官生财）。若生于春冬（官旺或财旺），主贵。若柱中无财印（指其他干支），亦可知名。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ji Days with Ren-Shen Hour":

  - Water prosperous Metal heavy—blessings not light; Ren Water Wealth at Shen is at longevity; Shen Metal generates Water.
  - If born in spring or winter months, definitely displays nobility; even without wealth-seal in pillars, still achieves fame.
  - If passing monthly qi with strong body, indicates nobility; without monthly qi, indicates wealth.
  - Key: Hurting Official generating Wealth pattern; Metal-Water mutual generation creates endless wealth source.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_033]` `[trigger: 水旺金重]` `[factor_trigger: shuiwang_jinzhong AND fu_buqing]` `[role: 主干]` 六己日生时壬申，水旺金重福不轻。 → 《三命通会》卷九#六己日壬申时
  - `[ns_smth_09_034]` `[trigger: 春冬显贵]` `[factor_trigger: chundong_xiangui AND yue_xiang]` `[role: 主干依赖]` 月在春冬须显贵，柱无财印亦知名。 → 《三命通会》卷九#六己日壬申时
  - `[ns_smth_09_035]` `[trigger: 通月身旺]` `[factor_trigger: tongyue_shenwang AND gui]` `[role: 条件分支]` 若通月气，身旺，贵。 → 《三命通会》卷九#六己日壬申时
  - `[ns_smth_09_036]` `[trigger: 不通亦富]` `[factor_trigger: butong_yifu AND caiguan_shuangmei]` `[role: 总结]` 不通，富。 → 《三命通会》卷九#六己日壬申时"""
    normalized_text_zh: str = """"""
    subject: str = "六己日壬申时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_ji', 'bazi_semantic', 'bazi_state_water_metal', 'bazi_semantic', 'bazi_state_shangguan_8', 'bazi_semantic', 'bazi_state_factor_264', 'bazi_semantic', 'hour_branch_shen', 'bazi_semantic', 'bazi_condition_factor_117', 'bazi_semantic', 'source_ref', 'rel_smth_09_025', 'shuiwang_jinzhong', 'rel_smth_09_026', 'shangguan_shengcai', 'rel_smth_09_027', 'chundong_yue', 'evi_smth_09_025', 'shuiwang_jinzhong', 'rule_shuiwang_jinzhong1', 'evi_smth_09_026', 'chundong_yue', 'rule_chundong_xiangui1', 'evi_smth_09_027', 'caiguan_shuangmei', 'rule_wucaiyin_zhiming1', 'map_smth_09_017', 'map_smth_09_018']
    
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
        l1_anchor="smth_v1.0.0_六己日壬申时_001_L1",
    )
    version: str = "1.0.0"
