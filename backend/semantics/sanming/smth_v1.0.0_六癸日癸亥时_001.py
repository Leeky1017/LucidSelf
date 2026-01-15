"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339717
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
    semantic_id="smth_v1.0.0_六癸日癸亥时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六癸日癸亥时(SemanticEntry):
    """
    - 原文（source_text）：
  六癸日生时癸亥，禄马飞天临旺神。不见官星兼惹绊，必为贵格异常人。
  癸日癸亥时，禄马飞天格，癸水亥健旺，癸用戊为官，丙为财，亥中丙戊俱绝，癸无财官，却亥去冲...
    """
    
    original_text: str = """- 原文（source_text）：
  六癸日生时癸亥，禄马飞天临旺神。不见官星兼惹绊，必为贵格异常人。
  癸日癸亥时，禄马飞天格，癸水亥健旺，癸用戊为官，丙为财，亥中丙戊俱绝，癸无财官，却亥去冲出巳中丙戊，飞来就癸为财官，柱无戊己惹绊及官星破禄，若见庚辛，清白而秀，为人智慧，贵为方面。

- 分字分词释义：
  - **禄马飞天**：即飞天禄马格。亥冲巳，巳中丙戊为癸之财官。
  - **旺神**：亥为癸水帝旺。
  - **惹绊**：填实（巳）或合住（寅）。

- **规范化释义（primary_lang_explained）**：
  六癸日出生于癸亥时，日时皆水，亥水帝旺，冲出对宫巳中丙戊财官，为飞天禄马格。若柱中无戊己官煞填实，无巳火填实，无寅木合亥（羁绊），主大贵。若见庚辛印绶，金白水清，主智慧清秀。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Gui Days with Gui-Hai Hour":

  - Salary-Horse Flying-Sky approaching prosperous spirit—Hai clashes Si, Si contains Bing-Wu (Wealth-Official) for Gui.
  - Not seeing Official star together with provoke-entangle, must be noble pattern extraordinary person.
  - Gui Water Hai healthy prosperous; Hai clashes out Si's Bing-Wu flying to Gui as Wealth-Official; if no Wu-Ji entanglement or Official breaking Salary, if seeing Geng-Xin, Metal-white Water-clear elegant.
  - Key: Flying Heaven pattern requires no filling in; Metal-Water pure indicates wisdom and elegance.

- 核心要点：
  - **飞天禄马**：亥冲巳。
  - **日禄归时**：癸禄在子（此处非归禄，乃帝旺）。
  - **金水清白**：喜印。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_209]` `[trigger: 禄马飞天]` `[factor_trigger: luma_feitian AND hai_chong_si]` `[role: 主干]` 六癸日生时癸亥，禄马飞天临旺神。 → 《三命通会》卷九#六癸日癸亥时
  - `[ns_smth_09_210]` `[trigger: 不见官星]` `[factor_trigger: bujian_guanxing AND bu_jian_rebang]` `[role: 主干依赖]` 不见官星兼惹绊，必为贵格异常人。 → 《三命通会》卷九#六癸日癸亥时
  - `[ns_smth_09_211]` `[trigger: 戊己填实]` `[factor_trigger: wujifen_shi AND tianshi_rebang]` `[role: 条件分支]` 柱无戊己惹绊及官星破禄，若见庚辛，清白而秀，为人智慧，贵为方面。 → 《三命通会》卷九#六癸日癸亥时
  - `[ns_smth_09_212]` `[trigger: 金水清白]` `[factor_trigger: jinshui_qingbai AND zhifu_yiren]` `[role: 总结]` 金水清白，主智慧清秀。 → 《三命通会》卷九#六癸日癸亥时"""
    normalized_text_zh: str = """"""
    subject: str = "六癸日癸亥时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_gui', 'bazi_semantic', 'bazi_state_factor_326', 'bazi_semantic', 'bazi_state_metal_water_2', 'bazi_semantic', 'bazi_state_factor_327', 'bazi_semantic', 'hour_branch_hai', 'bazi_semantic', 'bazi_condition_wu_ji_si_yin', 'bazi_semantic', 'source_ref', 'rel_smth_09_178', 'luma_feitian', 'rel_smth_09_179', 'bujian_guanxing_rebang', 'rel_smth_09_180', 'tianshi_rebang', 'evi_smth_09_178', 'luma_feitian', 'rule_luma_feitian1', 'evi_smth_09_179', 'guige_yichang', 'rule_guige_yichang1', 'evi_smth_09_180', 'jinshui_qingbai', 'rule_jinshui_qingbai1', 'map_smth_09_119', 'map_smth_09_120']
    
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
        l1_anchor="smth_v1.0.0_六癸日癸亥时_001_L1",
    )
    version: str = "1.0.0"
