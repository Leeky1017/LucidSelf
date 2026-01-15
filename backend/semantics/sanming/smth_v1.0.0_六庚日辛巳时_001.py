"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339479
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
    semantic_id="smth_v1.0.0_六庚日辛巳时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六庚日辛巳时(SemanticEntry):
    """
    - 原文（source_text）：
  六庚日生时辛巳，偏官合刃自身生。为人刚毅妻财损，运到金乡贵禄享。
  庚日辛巳时，阳刃偏官。庚以辛为刃，丙为杀。明辛暗丙，合煞为权。通身旺月，贵；不通，无贵，...
    """
    
    original_text: str = """- 原文（source_text）：
  六庚日生时辛巳，偏官合刃自身生。为人刚毅妻财损，运到金乡贵禄享。
  庚日辛巳时，阳刃偏官。庚以辛为刃，丙为杀。明辛暗丙，合煞为权。通身旺月，贵；不通，无贵，寿考。

- 分字分词释义：
  - **阳刃偏官**：辛金为庚金劫财（阳刃），巳中丙火为偏官（七煞）。
  - **合煞为权**：丙辛合（威制之合），煞刃相合，主掌权。

- **规范化释义（primary_lang_explained）**：
  六庚日出生于辛巳时，辛金劫财（刃）透出，巳中丙火七煞暗藏，丙辛相合，为"煞刃双显、合煞为权"之象。为人刚毅果断，但恐损妻破财（劫财之故）。若生于身旺月，主贵；若身弱，只主长寿（巳为长生），不贵。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Geng Days with Xin-Si Hour":

  - Yang Blade Partial Official—Xin Metal Rob Wealth (blade) reveals; Bing Fire Seven-Killing hidden in Si; Bing-Xin combine making killing become power.
  - Person is resolute and decisive but may damage wife and wealth; if luck reaches Metal land, enjoys noble fortune.
  - If passing body-prosperous month, indicates nobility; without monthly qi, no nobility but longevity (Si is longevity).
  - Key: Blade and Killing combine with affection; strong body transforms killing into authority.

- 核心要点：
  - **长生**：庚生于巳。
  - **合煞**：丙辛合，去煞留官（或化水），但此处多指煞刃有情。
  - **忌冲**：亥冲巳，破合破生。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_069]` `[trigger: 偏官合刃]` `[factor_trigger: pianguan_heren AND zishen_sheng]` `[role: 主干]` 六庚日生时辛巳，偏官合刃自身生。 → 《三命通会》卷九#六庚日辛巳时
  - `[ns_smth_09_070]` `[trigger: 刚毅妻财损]` `[factor_trigger: gangyi_qicai_sun AND yun_dao_jinxiang]` `[role: 主干依赖]` 为人刚毅妻财损，运到金乡贵禄享。 → 《三命通会》卷九#六庚日辛巳时
  - `[ns_smth_09_071]` `[trigger: 通身旺月]` `[factor_trigger: tong_shenwang_yue AND gui]` `[role: 条件分支]` 通身旺月，贵。 → 《三命通会》卷九#六庚日辛巳时
  - `[ns_smth_09_072]` `[trigger: 不通寿考]` `[factor_trigger: butong_shoukao AND wugui]` `[role: 总结]` 不通，无贵，寿考。 → 《三命通会》卷九#六庚日辛巳时"""
    normalized_text_zh: str = """"""
    subject: str = "六庚日辛巳时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_geng', 'bazi_semantic', 'bazi_state_factor_276', 'bazi_semantic', 'bazi_relation_factor_119', 'bazi_semantic', 'bazi_state_factor_277', 'bazi_semantic', 'hour_branch_si', 'bazi_semantic', 'bazi_condition_factor_124', 'bazi_semantic', 'source_ref', 'rel_smth_09_052', 'yangren_pianguan', 'rel_smth_09_053', 'heshi_weiquan', 'rel_smth_09_054', 'tong_shenwang_yue', 'evi_smth_09_052', 'yangren_pianguan', 'rule_yangren_pianguan1', 'evi_smth_09_053', 'heshi_weiquan', 'rule_hesha_weiquan1', 'evi_smth_09_054', 'tong_shenwang_yue', 'rule_tongshenwang_yue1', 'map_smth_09_035', 'map_smth_09_036']
    
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
        l1_anchor="smth_v1.0.0_六庚日辛巳时_001_L1",
    )
    version: str = "1.0.0"
