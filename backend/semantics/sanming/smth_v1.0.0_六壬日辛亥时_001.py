"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339823
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
    semantic_id="smth_v1.0.0_六壬日辛亥时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六壬日辛亥时(SemanticEntry):
    """
    - 原文（source_text）：
  六壬日逢辛亥时，印禄相随最是奇。财官不见无冲破，得路青云报尔知。
  壬日辛亥时，日禄居时，无克破，有倚托，柱中不见财官，富贵显达；行东运，大贵；若通气，减福...
    """
    
    original_text: str = """- 原文（source_text）：
  六壬日逢辛亥时，印禄相随最是奇。财官不见无冲破，得路青云报尔知。
  壬日辛亥时，日禄居时，无克破，有倚托，柱中不见财官，富贵显达；行东运，大贵；若通气，减福；南方运，不贵巨富。

- 分字分词释义：
  - **印禄相随**：辛金正印透干，亥为壬水日禄。
  - **得路青云**：指日禄归时格，青云直上。

- **规范化释义（primary_lang_explained）**：
  六壬日出生于辛亥时，正印透出，日禄归时，格局奇特。若柱中不见财官（忌财坏印、官星填实），且无刑冲破害，主青云得路，富贵显达。行东方木运（食伤），大贵。若通气（指通财官气？或身太旺），减福。行南方火运（财），不贵则巨富。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ren Days with Xin-Hai Hour":

  - Seal-禄 follow-each-other most is marvelous—Xin Metal Direct Seal reveals; Hai is Ren Water's Day Salary.
  - Wealth-Official not seen no clash-break, gain-road blue-cloud report you know.
  - Day Salary residing time, no attacking-breaking with support, pillars not seeing Wealth-Official, wealthy-noble prominent; traveling East luck, great nobility; traveling South luck, not noble then huge wealth.
  - Key: Day Salary Return to Hour pattern; fears Wealth damaging Seal and filling in; East Wood luck draining elegant most auspicious.

- 核心要点：
  - **日禄归时**：壬禄在亥。
  - **印绶护禄**：辛生壬。
  - **喜食伤**：喜东方运泄秀。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_189]` `[trigger: 印禄相随]` `[factor_trigger: yinlu_xiangsui AND zui_shi_qi]` `[role: 主干]` 六壬日逢辛亥时，印禄相随最是奇。 → 《三命通会》卷九#六壬日辛亥时
  - `[ns_smth_09_190]` `[trigger: 财官不见]` `[factor_trigger: caiguan_bujian AND wu_chongpo]` `[role: 主干依赖]` 财官不见无冲破，得路青云报尔知。 → 《三命通会》卷九#六壬日辛亥时
  - `[ns_smth_09_191]` `[trigger: 日禄居时]` `[factor_trigger: rilu_jushi AND wu_kepo]` `[role: 条件分支]` 日禄居时，无克破，有倚托，柱中不见财官，富贵显达。 → 《三命通会》卷九#六壬日辛亥时
  - `[ns_smth_09_192]` `[trigger: 东运大贵]` `[factor_trigger: dongyun_dagui AND nanyun_jufu]` `[role: 总结]` 行东运，大贵；若通气，减福；南方运，不贵巨富。 → 《三命通会》卷九#六壬日辛亥时"""
    normalized_text_zh: str = """"""
    subject: str = "六壬日辛亥时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_ren', 'bazi_semantic', 'bazi_state_factor_345', 'bazi_semantic', 'bazi_relation_factor_138', 'bazi_semantic', 'bazi_state_factor_346', 'bazi_semantic', 'hour_branch_hai', 'bazi_semantic', 'bazi_condition_factor_134', 'bazi_semantic', 'source_ref', 'rel_smth_09_142', 'riluguishi', 'rel_smth_09_143', 'bujian_caiguan_wu_chongpo', 'rel_smth_09_144', 'jian_caiguan_tongqi', 'evi_smth_09_142', 'yinlu_xiangsui', 'rule_yinlu_xiangsui1', 'evi_smth_09_143', 'bujian_caiguan_wu_chongpo', 'rule_riluguishi_qingyun1', 'evi_smth_09_144', 'jian_caiguan_tongqi', 'rule_dongnan_yun_qingyun1', 'map_smth_09_095', 'map_smth_09_096']
    
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
        l1_anchor="smth_v1.0.0_六壬日辛亥时_001_L1",
    )
    version: str = "1.0.0"
