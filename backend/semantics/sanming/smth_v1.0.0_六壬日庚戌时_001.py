"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339815
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
    semantic_id="smth_v1.0.0_六壬日庚戌时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六壬日庚戌时(SemanticEntry):
    """
    - 原文（source_text）：
  六壬日生时庚戌，身临财库却为鬼。明庚暗戌相刑克，财禄生平聚散多。
  壬日庚戌时，枭临财库，壬以丙丁为财，库于戌，庚为倒食，戊偏官，若通火木月气，有倚托者，贵...
    """
    
    original_text: str = """- 原文（source_text）：
  六壬日生时庚戌，身临财库却为鬼。明庚暗戌相刑克，财禄生平聚散多。
  壬日庚戌时，枭临财库，壬以丙丁为财，库于戌，庚为倒食，戊偏官，若通火木月气，有倚托者，贵；不通，财帛聚散。

- 分字分词释义：
  - **枭临财库**：庚（枭）透干，戌为火库（财库）。
  - **身临财库却为鬼**：戌中藏戊土七煞（鬼），壬水坐煞库。
  - **相刑克**：庚金泄戊土，或庚金克木（食伤），戌中丁火克庚金？原文意指格局驳杂，财库中有鬼。

- **规范化释义（primary_lang_explained）**：
  六壬日出生于庚戌时，庚金枭神透出，坐戌财库。戌中藏丁（财）、戊（煞）、辛（印）。若通火木月气（财食旺），有倚托，主贵。若不通，财帛多聚散。戌为财库，亦为煞库，故云“身临财库却为鬼”。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ren Days with Geng-Xu Hour":

  - Body approaches Wealth treasury yet becomes Ghost—Xu is Fire treasury (Wealth) but hides Wu Earth Seven-Killing (Ghost).
  - Bright Geng dark Xu mutually punish-attack; Wealth-Salary lifetime gather-scatter much.
  - Owl approaches Wealth treasury; if connecting Fire-Wood monthly qi with support, noble; not connecting, Wealth gather-scatter.
  - Key: Wealth treasury pattern complicated by hidden Killing; needs monthly qi support for stability.

- 核心要点：
  - **财煞同宫**：戌中丁戊。
  - **印绶化煞**：庚化戊。
  - **财库**：戌为财库。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_185]` `[trigger: 身临财库]` `[factor_trigger: shenlin_caiku AND que_wei_gui]` `[role: 主干]` 六壬日生时庚戌，身临财库却为鬼。 → 《三命通会》卷九#六壬日庚戌时
  - `[ns_smth_09_186]` `[trigger: 明庚暗戌]` `[factor_trigger: minggeng_anxu AND xiang_xingke]` `[role: 主干依赖]` 明庚暗戌相刑克，财禄生平聚散多。 → 《三命通会》卷九#六壬日庚戌时
  - `[ns_smth_09_187]` `[trigger: 枭临财库]` `[factor_trigger: xiao_lin_caiku AND caisha_tongcang]` `[role: 条件分支]` 枭临财库，戌为火库，庚为倒食，戊偏官。 → 《三命通会》卷九#六壬日庚戌时
  - `[ns_smth_09_188]` `[trigger: 通火木贵]` `[factor_trigger: tong_huomu_gui AND butong_jusan]` `[role: 总结]` 若通火木月气，有倚托者，贵；不通，财帛聚散。 → 《三命通会》卷九#六壬日庚戌时"""
    normalized_text_zh: str = """"""
    subject: str = "六壬日庚戌时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_ren', 'bazi_semantic', 'bazi_state_factor_343', 'bazi_semantic', 'bazi_relation_factor_137', 'bazi_semantic', 'bazi_state_factor_344', 'bazi_semantic', 'hour_branch_xu', 'bazi_semantic', 'bazi_condition_fire_wood_1', 'bazi_semantic', 'source_ref', 'rel_smth_09_139', 'xiao_lin_caiku', 'rel_smth_09_140', 'tong_huomu_yueqi', 'rel_smth_09_141', 'caiku_fuzai', 'evi_smth_09_139', 'caiku_fuzai', 'rule_caiku_fuzai1', 'evi_smth_09_140', 'tong_huomu_yueqi', 'rule_tong_huomu_yueqi_gengxu1', 'evi_smth_09_141', 'caibo_jusan', 'rule_caibo_jusan1', 'map_smth_09_093', 'map_smth_09_094']
    
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
        l1_anchor="smth_v1.0.0_六壬日庚戌时_001_L1",
    )
    version: str = "1.0.0"
