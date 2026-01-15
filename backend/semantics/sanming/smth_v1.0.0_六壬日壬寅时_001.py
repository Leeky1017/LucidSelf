"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339745
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
    semantic_id="smth_v1.0.0_六壬日壬寅时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六壬日壬寅时(SemanticEntry):
    """
    - 原文（source_text）：
  六壬日生时壬寅，水火相逢既济论。水木月通财禄贵，不通无救是常人。
  壬日壬寅时，水火既济。壬用丙为财，甲为食，寅上丙生甲旺，壬水无气，若通水局，有倚托，皆贵...
    """
    
    original_text: str = """- 原文（source_text）：
  六壬日生时壬寅，水火相逢既济论。水木月通财禄贵，不通无救是常人。
  壬日壬寅时，水火既济。壬用丙为财，甲为食，寅上丙生甲旺，壬水无气，若通水局，有倚托，皆贵，不通无救，福薄。壬寅日健旺，主大富，如不通月气，亦贵。

- 分字分词释义：
  - **水火既济**：壬水日主，寅中藏丙火（财），水火相济。
  - **丙生甲旺**：寅为丙火长生，甲木禄地，食神生财有力。
  - **壬水无气**：壬在寅为病地。

- **规范化释义（primary_lang_explained）**：
  六壬日出生于壬寅时，时支寅中甲木食神、丙火偏财皆旺，食神生财。但壬水在寅病地，身弱。若通水局（申子辰）或月令金水，日主有倚托，主富贵。若身弱无救，福薄。若是壬寅日自坐长生（实为病地，但自坐食财），主大富。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ren Days with Ren-Yin Hour":

  - Water-Fire mutual encounter Already-Accomplished theory—Ren Water Day Master; Yin hides Bing Fire (Wealth); Water-Fire mutually aid.
  - Water-Wood month connecting Wealth-Salary noble; not connecting no rescue is ordinary person.
  - Bing born Jia prosperous; if connecting Water bureau with support, all noble; not connecting no rescue, fortune thin.
  - Key: Eating God generates Wealth pattern; body weak needs support; Ren-Yin day greatly wealthy.

- 核心要点：
  - **食神生财**：甲丙同宫。
  - **身弱**：泄气重，喜比印。
  - **水火既济**：财星得地。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_153]` `[trigger: 水火既济]` `[factor_trigger: shuihuo_jiji AND bijian_shicai]` `[role: 主干]` 六壬日生时壬寅，水火相逢既济论。 → 《三命通会》卷九#六壬日壬寅时
  - `[ns_smth_09_154]` `[trigger: 水木月贵]` `[factor_trigger: shuimu_yue_gui AND butong_changren]` `[role: 主干依赖]` 水木月通财禄贵，不通无救是常人。 → 《三命通会》卷九#六壬日壬寅时
  - `[ns_smth_09_155]` `[trigger: 食神生财]` `[factor_trigger: shishen_shengcai AND shenruo_fubao]` `[role: 条件分支]` 壬用丙为财，甲为食，寅上丙生甲旺，壬水无气。 → 《三命通会》卷九#六壬日壬寅时
  - `[ns_smth_09_156]` `[trigger: 有倚托贵]` `[factor_trigger: you_yituo_gui AND renyin_dafu]` `[role: 总结]` 若通水局，有倚托，皆贵。壬寅日健旺，主大富。 → 《三命通会》卷九#六壬日壬寅时"""
    normalized_text_zh: str = """"""
    subject: str = "六壬日壬寅时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_ren', 'bazi_semantic', 'bazi_state_shishen_9', 'bazi_semantic', 'bazi_state_water_fire', 'bazi_semantic', 'bazi_state_factor_331', 'bazi_semantic', 'hour_branch_yin', 'bazi_semantic', 'bazi_condition_water_3', 'bazi_semantic', 'source_ref', 'rel_smth_09_115', 'shishen_shengcai', 'rel_smth_09_116', 'shishen_shengcai', 'rel_smth_09_117', 'tong_shuiju_youtuo', 'evi_smth_09_115', 'shuihuo_jiqi', 'rule_shuihuo_jiqi1', 'evi_smth_09_116', 'shenruo_wujiu', 'rule_shenruo_wujiu1', 'evi_smth_09_117', 'tong_shuiju_youtuo', 'rule_tong_shuiju_youtuo1', 'map_smth_09_077', 'map_smth_09_078']
    
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
        l1_anchor="smth_v1.0.0_六壬日壬寅时_001_L1",
    )
    version: str = "1.0.0"
