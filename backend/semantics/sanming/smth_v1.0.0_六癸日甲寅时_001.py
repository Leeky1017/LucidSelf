"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339633
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
    semantic_id="smth_v1.0.0_六癸日甲寅时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六癸日甲寅时(SemanticEntry):
    """
    - 原文（source_text）：
  六癸日生时甲寅，刃复官禄减精神。柱中无有庚申字，刑合财官是贵人。
  癸日甲寅时，刑合财官，癸以丙为财，戊为官，寅刑出巳中丙戊为财官，若柱无官煞及刑冲破害损格...
    """
    
    original_text: str = """- 原文（source_text）：
  六癸日生时甲寅，刃复官禄减精神。柱中无有庚申字，刑合财官是贵人。
  癸日甲寅时，刑合财官，癸以丙为财，戊为官，寅刑出巳中丙戊为财官，若柱无官煞及刑冲破害损格，贵；有庚申戊己字，无制伏，不贵。

- 分字分词释义：
  - **刑合财官**：寅刑巳（巳为丙戊禄），刑出财官。
  - **刃复官禄**：原文“刃复”恐误，可能指“刑出”。或指寅中甲木伤官（刃？甲木非癸刃）克官。
  - **庚申字**：庚申冲寅，破刑合之局。

- **规范化释义（primary_lang_explained）**：
  六癸日出生于甲寅时，名为刑合财官格。寅木刑出巳中丙火（财）戊土（官）。若柱中无官煞（戊己）填实，无庚申冲寅，无刑冲破害，主贵。若有庚申戊己，格局受损，不贵。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Gui Days with Jia-Yin Hour":

  - Blade repeats Official Salary reduces spirit—(text questionable) possibly refers to punishing out pattern.
  - If pillars have no Geng-Shen characters, punishment-combining Wealth-Official becomes noble person.
  - Yin punishes Si, punishing out Bing-Wu (Wealth-Official) in Si; if no Official-Killing or punishment-clash-break-harm damaging pattern, noble.
  - Key: Punishment-combine pattern requires no filling in (Wu-Ji) and no Shen clashing Yin.

- 核心要点：
  - **刑合格**：寅刑巳。
  - **伤官生财**：甲生丙。
  - **忌冲**：忌申冲寅。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_201]` `[trigger: 刃复官禄]` `[factor_trigger: ren_fu_guanlu AND jian_jingshen]` `[role: 主干]` 六癸日生时甲寅，刃复官禄减精神。 → 《三命通会》卷九#六癸日甲寅时
  - `[ns_smth_09_202]` `[trigger: 柱中无庚申]` `[factor_trigger: zhuzhong_wu_gengshen AND xinghe_guiren]` `[role: 主干依赖]` 柱中无有庚申字，刑合财官是贵人。 → 《三命通会》卷九#六癸日甲寅时
  - `[ns_smth_09_203]` `[trigger: 寅刑巳]` `[factor_trigger: yin_xing_si AND xingchu_caiguan]` `[role: 条件分支]` 癸以丙为财，戊为官，寅刑出巳中丙戊为财官。 → 《三命通会》卷九#六癸日甲寅时
  - `[ns_smth_09_204]` `[trigger: 无官煞刑冲]` `[factor_trigger: wu_guansha_xingchong AND gui]` `[role: 总结]` 若柱无官煞及刑冲破害损格，贵；有庚申戊己字，无制伏，不贵。 → 《三命通会》卷九#六癸日甲寅时"""
    normalized_text_zh: str = """"""
    subject: str = "六癸日甲寅时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_gui', 'bazi_semantic', 'bazi_state_factor_311', 'bazi_semantic', 'bazi_state_shangguan_8', 'bazi_semantic', 'bazi_state_factor_312', 'bazi_semantic', 'hour_branch_yin', 'bazi_semantic', 'bazi_condition_geng_shen_wu_ji', 'bazi_semantic', 'source_ref', 'rel_smth_09_151', 'xinghe_caiguan', 'rel_smth_09_152', 'wu_gengshen_wuji', 'rel_smth_09_153', 'gengshen_chongyin', 'evi_smth_09_151', 'xinghe_caiguan', 'rule_xinghe_caiguan1', 'evi_smth_09_152', 'wu_gengshen_wuji', 'rule_wu_gengshen1', 'evi_smth_09_153', 'poge_bugui', 'rule_gengshen_poge1', 'map_smth_09_101', 'map_smth_09_102']
    
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
        l1_anchor="smth_v1.0.0_六癸日甲寅时_001_L1",
    )
    version: str = "1.0.0"
