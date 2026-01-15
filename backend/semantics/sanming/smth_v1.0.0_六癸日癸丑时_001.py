"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339625
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
    semantic_id="smth_v1.0.0_六癸日癸丑时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六癸日癸丑时(SemanticEntry):
    """
    - 原文（source_text）：
  六癸日生时癸丑，支中暗鬼有刑伤。月通身旺防妻损，丑巳遥合贵异常。
  癸日癸丑时，支得隐鬼。癸以己为偏官，丑中有暗己得位，癸以丁为妻，丑中丁火无气，若通身旺比...
    """
    
    original_text: str = """- 原文（source_text）：
  六癸日生时癸丑，支中暗鬼有刑伤。月通身旺防妻损，丑巳遥合贵异常。
  癸日癸丑时，支得隐鬼。癸以己为偏官，丑中有暗己得位，癸以丁为妻，丑中丁火无气，若通身旺比肩之月，防损妻财。柱丑寅多，以寅刑巳，丑合巳，刑出巳中丙戊为财官，须干头无戊己字，大贵。忌巳未卯破格。

- 分字分词释义：
  - **支中暗鬼**：丑中藏己土（七煞/偏官），故云暗鬼。
  - **丑巳遥合**：丑与巳拱合（巳酉丑），或丑刑巳（寅刑巳？原文作“寅刑巳，丑合巳”）。古法有“丑遥巳禄”格，但那是辛丑日。此处癸丑日，丑中无辛（辛入墓），癸以戊为官，丑遥巳中戊土，故贵。
  - **刑伤**：丑中己土克癸水。

- **规范化释义（primary_lang_explained）**：
  六癸日出生于癸丑时，丑中暗藏己土七煞，克身。且丑中丁火（财）无气。若生于身旺比劫月，防克妻破财。若柱中丑寅多，通过寅刑巳、丑合巳，刑合出巳中丙火（财）戊土（官），且天干不透戊己填实，主大贵。忌见巳（填实）、未（冲丑）、卯（阻碍）破格。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Gui Days with Gui-Chou Hour":

  - Branch-inside dark ghost has punishment injury—Chou hides Ji Earth Seven-Killing attacking body.
  - If month connects body-prosperous, guard against wife loss; Chou-Si remote combine brings extraordinary nobility.
  - If pillar has many Chou-Yin, using Yin punishing Si, Chou combining Si, punishing out Bing-Wu (Wealth-Official) in Si, needs stems without Wu-Ji, great nobility.
  - Key: Remote combine pattern requires no filling in; dark killing needs body strong to handle.

- 核心要点：
  - **遥合格**：丑遥巳中财官。
  - **暗煞**：丑中己土。
  - **拱禄**：癸丑与癸亥拱子禄。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_197]` `[trigger: 支中暗鬼]` `[factor_trigger: zhizhong_angui AND you_xingshang]` `[role: 主干]` 六癸日生时癸丑，支中暗鬼有刑伤。 → 《三命通会》卷九#六癸日癸丑时
  - `[ns_smth_09_198]` `[trigger: 身旺防妻损]` `[factor_trigger: shenwang_fang_qisun AND chou_si_yaohe]` `[role: 主干依赖]` 月通身旺防妻损，丑巳遥合贵异常。 → 《三命通会》卷九#六癸日癸丑时
  - `[ns_smth_09_199]` `[trigger: 遥合财官]` `[factor_trigger: yaohe_caiguan AND xingchu_bing_wu]` `[role: 条件分支]` 柱丑寅多，以寅刑巳，丑合巳，刑出巳中丙戊为财官。 → 《三命通会》卷九#六癸日癸丑时
  - `[ns_smth_09_200]` `[trigger: 干头无戊己]` `[factor_trigger: gantou_wu_wuji AND dagui]` `[role: 总结]` 须干头无戊己字，大贵。忌巳未卯破格。 → 《三命通会》卷九#六癸日癸丑时"""
    normalized_text_zh: str = """"""
    subject: str = "六癸日癸丑时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_gui', 'bazi_semantic', 'bazi_state_factor_309', 'bazi_semantic', 'bazi_relation_chou_si', 'bazi_semantic', 'bazi_state_factor_310', 'bazi_semantic', 'hour_branch_chou', 'bazi_semantic', 'bazi_condition_chou_yin_wu_ji', 'bazi_semantic', 'source_ref', 'rel_smth_09_148', 'chou_si_yaohe', 'rel_smth_09_149', 'yaohe_caiguan', 'rel_smth_09_150', 'zhizhong_angui', 'evi_smth_09_148', 'chou_si_yaohe', 'rule_chou_si_yaohe1', 'evi_smth_09_149', 'gui_dagui', 'rule_wuwuji_dagui1', 'evi_smth_09_150', 'xingshang_qicai', 'rule_shenwang_fangqi1', 'map_smth_09_099', 'map_smth_09_100']
    
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
        l1_anchor="smth_v1.0.0_六癸日癸丑时_001_L1",
    )
    version: str = "1.0.0"
