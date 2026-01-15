"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339527
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
    semantic_id="smth_v1.0.0_六辛日庚寅时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六辛日庚寅时(SemanticEntry):
    """
    - 原文（source_text）：
  六辛日生时庚寅，财旺生官遇贵神。金木局中通月气，必为荣贵富豪人。
  辛日庚寅时，贵人财官。辛以寅为天乙贵，丙火为官，甲木为财，寅上丙、甲旺，若通金木月气或通...
    """
    
    original_text: str = """- 原文（source_text）：
  六辛日生时庚寅，财旺生官遇贵神。金木局中通月气，必为荣贵富豪人。
  辛日庚寅时，贵人财官。辛以寅为天乙贵，丙火为官，甲木为财，寅上丙、甲旺，若通金木月气或通运，主富贵显达。

- 分字分词释义：
  - **贵神**：寅为辛金天乙贵人。
  - **财旺生官**：寅中甲木（财）生丙火（官），财官双美。
  - **金木局**：金局助身，木局助财。

- **规范化释义（primary_lang_explained）**：
  六辛日出生于庚寅时，寅为天乙贵人，内藏甲木正财、丙火正官，财官印（寅中戊）俱全且旺。若通金气（身旺）或木气（财旺），主富贵显达。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Xin Days with Geng-Yin Hour":

  - Wealth prosperous generates Official encountering Noble Spirit—Yin is Xin's Heavenly Noble; Jia Wood Wealth and Bing Fire Official both prosperous at Yin.
  - If Metal-Wood bureau connects monthly qi, definitely a glorious noble wealthy person.
  - Geng Metal Rob Wealth helps body; Yin contains complete Wealth-Official-Seal, pattern auspicious.
  - Key: Heavenly Noble at hour with Wealth-Official prosperous; body strong can handle riches nobility.

- 核心要点：
  - **财官双美**：寅为财官长生/禄地。
  - **天乙贵人**：辛贵在寅。
  - **身旺**：财官旺需身旺任之。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_105]` `[trigger: 财旺生官]` `[factor_trigger: caiwang_shengguan AND yu_guishen]` `[role: 主干]` 六辛日生时庚寅，财旺生官遇贵神。 → 《三命通会》卷九#六辛日庚寅时
  - `[ns_smth_09_106]` `[trigger: 通金木月气]` `[factor_trigger: tong_jinmu_yueqi AND fuhao_ren]` `[role: 主干依赖]` 金木局中通月气，必为荣贵富豪人。 → 《三命通会》卷九#六辛日庚寅时
  - `[ns_smth_09_107]` `[trigger: 通运亦贵]` `[factor_trigger: tongyun_yigui AND fugui_xianda]` `[role: 条件分支]` 若通金木月气或通运，主富贵显达。 → 《三命通会》卷九#六辛日庚寅时
  - `[ns_smth_09_108]` `[trigger: 贵人财官]` `[factor_trigger: guiren_caiguan AND tianyigui]` `[role: 总结]` 寅为天乙贵，丙火为官，甲木为财。 → 《三命通会》卷九#六辛日庚寅时"""
    normalized_text_zh: str = """"""
    subject: str = "六辛日庚寅时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_xin', 'bazi_semantic', 'bazi_state_factor_299', 'bazi_semantic', 'bazi_state_yi', 'bazi_semantic', 'bazi_state_factor_291', 'bazi_semantic', 'hour_branch_yin', 'bazi_semantic', 'bazi_condition_metal_wood', 'bazi_semantic', 'source_ref', 'rel_smth_09_079', 'caiwang_shengguan', 'rel_smth_09_080', 'caiwang_shengguan', 'rel_smth_09_081', 'tong_jinmu_yueqi', 'evi_smth_09_079', 'caiwang_shengguan', 'rule_caiwang_guishen1', 'evi_smth_09_080', 'tong_jinmu_yueqi', 'rule_jinmu_tongqi1', 'evi_smth_09_081', 'fuhao_xianda', 'rule_fuhao_xianda1', 'map_smth_09_053', 'map_smth_09_054']
    
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
        l1_anchor="smth_v1.0.0_六辛日庚寅时_001_L1",
    )
    version: str = "1.0.0"
