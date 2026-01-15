"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339663
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
    semantic_id="smth_v1.0.0_六癸日丁巳时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六癸日丁巳时(SemanticEntry):
    """
    - 原文（source_text）：
  六癸日生时丁巳，贵地逢财遇暗官。有托就看财禄盛，无依必定福偏残。
  癸日丁巳时，癸合财官，癸用丙为财，戊为官，庚为印，巳为天乙贵人。巳上庚金长生，丙戊建禄，...
    """
    
    original_text: str = """- 原文（source_text）：
  六癸日生时丁巳，贵地逢财遇暗官。有托就看财禄盛，无依必定福偏残。
  癸日丁巳时，癸合财官，癸用丙为财，戊为官，庚为印，巳为天乙贵人。巳上庚金长生，丙戊建禄，癸水受胎，若有倚托，通水气月，贵，不通水气，平常。时逢三奇，大抵发于晚年。

- 分字分词释义：
  - **贵地**：巳为癸水天乙贵人。
  - **暗官**：巳中藏戊土正官。
  - **财禄盛**：丁火透，巳中丙火得禄，财旺。
  - **三奇**：财官印（丙戊庚）俱全于巳。

- **规范化释义（primary_lang_explained）**：
  六癸日出生于丁巳时，丁火偏财透出，巳中藏丙财、戊官、庚印，财官印三奇俱全，且皆旺（禄/长生）。巳又是天乙贵人。若日主有倚托（身旺），通水气，主大贵。若身弱无依，福气偏残（富屋贫人）。此格多发于晚年。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Gui Days with Ding-Si Hour":

  - Noble place encountering Wealth meets dark Official—Si is Gui's Heavenly Noble; Si hides Bing-Wu-Geng (Wealth-Official-Seal).
  - With support see Wealth-Salary flourishing; without reliance definitely fortune partially incomplete.
  - Si contains Three Wonders (Wealth-Official-Seal); Geng Metal at Long Life; Bing-Wu at Prosperity; if with support connecting Water qi month, noble.
  - Key: Three Wonders complete requires body strong to handle; mostly develops in later years.

- 核心要点：
  - **财官印三奇**：巳中全。
  - **天乙贵人**：巳。
  - **身弱**：癸绝于巳，胎于巳，身弱。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_213]` `[trigger: 贵地逢财]` `[factor_trigger: guidi_fengcai AND yu_anguan]` `[role: 主干]` 六癸日生时丁巳，贵地逢财遇暗官。 → 《三命通会》卷九#六癸日丁巳时
  - `[ns_smth_09_214]` `[trigger: 有托财禄盛]` `[factor_trigger: youtuo_cailu_sheng AND wuyi_fu_piancan]` `[role: 主干依赖]` 有托就看财禄盛，无依必定福偏残。 → 《三命通会》卷九#六癸日丁巳时
  - `[ns_smth_09_215]` `[trigger: 三奇全备]` `[factor_trigger: sanqi_quanbei AND wannian_fa]` `[role: 条件分支]` 巳为天乙贵人，藏丙戊庚（财官印），三奇全备，大抵发于晚年。 → 《三命通会》卷九#六癸日丁巳时
  - `[ns_smth_09_216]` `[trigger: 通水气贵]` `[factor_trigger: tong_shuiqi_gui AND shenruo_pincan]` `[role: 总结]` 若有倚托，通水气月，贵，不通水气，平常。 → 《三命通会》卷九#六癸日丁巳时"""
    normalized_text_zh: str = """"""
    subject: str = "六癸日丁巳时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_gui', 'bazi_semantic', 'bazi_state_factor_316', 'bazi_semantic', 'bazi_state_yi', 'bazi_semantic', 'bazi_state_factor_317', 'bazi_semantic', 'hour_branch_si', 'bazi_semantic', 'bazi_condition_water_1', 'bazi_semantic', 'source_ref', 'rel_smth_09_160', 'caiguanyin_sanqi', 'rel_smth_09_161', 'tong_shuiqi_youtuo', 'rel_smth_09_162', 'shenruo_wuyi', 'evi_smth_09_160', 'tianyi_guiren', 'rule_guidi_caiguan1', 'evi_smth_09_161', 'gui_wannian', 'rule_youtuo_wannian1', 'evi_smth_09_162', 'fu_piancan', 'rule_wuyi_piancan1', 'map_smth_09_107', 'map_smth_09_108']
    
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
        l1_anchor="smth_v1.0.0_六癸日丁巳时_001_L1",
    )
    version: str = "1.0.0"
