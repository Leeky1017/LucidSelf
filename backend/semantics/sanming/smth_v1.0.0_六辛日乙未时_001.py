"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339573
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
    semantic_id="smth_v1.0.0_六辛日乙未时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六辛日乙未时(SemanticEntry):
    """
    - 原文（source_text）：
  六辛日生时乙未，火木相成金不畏。月通金气与春荣，财旺生官身自贵。
  辛日乙未时，天财入库。辛以乙为财，未上入库；己为倒食，丁为正鬼；未上有暗丁，己被明乙制伏...
    """
    
    original_text: str = """- 原文（source_text）：
  六辛日生时乙未，火木相成金不畏。月通金气与春荣，财旺生官身自贵。
  辛日乙未时，天财入库。辛以乙为财，未上入库；己为倒食，丁为正鬼；未上有暗丁，己被明乙制伏，不能为害。若通巳酉丑月者，贵，通火，行西运；通金，行南运，俱贵。

- 分字分词释义：
  - **天财入库**：乙木（偏财）坐未（木库），财星入库。
  - **火木相成**：未中丁（火）乙（木）相生。
  - **己被乙制**：未中己土（枭）受乙木克制，不夺食。

- **规范化释义（primary_lang_explained）**：
  六辛日出生于乙未时，偏财乙木入未库，未中财官印俱备（乙丁己）。乙木克制己土枭神，保护食神。若生于金旺之月（身旺），行木火运，或生于木火月，行金运（身旺），皆主贵。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Xin Days with Yi-Wei Hour":

  - Fire-Wood mutual completion Metal not fearful—Yi Wood Indirect Wealth enters Wei treasury; Ding Fire (Official) Yi Wood (Wealth) mutually generate.
  - If monthly qi connects Metal or spring flourishing, Wealth prosperous generates Official body naturally noble.
  - Yi Wood controls Ji Earth (Owl) in Wei, protecting Eating God from being seized.
  - Key: Heavenly Wealth enters treasury; body strong handles Wealth-Official; mixed-qi pattern requires proper channeling.

- 核心要点：
  - **财库**：未为财库，主富。
  - **身旺**：喜身旺任财官。
  - **杂气财官**：未中财官。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_125]` `[trigger: 火木相成]` `[factor_trigger: huomu_xiangcheng AND jin_buwei]` `[role: 主干]` 六辛日生时乙未，火木相成金不畏。 → 《三命通会》卷九#六辛日乙未时
  - `[ns_smth_09_126]` `[trigger: 财旺生官]` `[factor_trigger: caiwang_shengguan AND shen_zigui]` `[role: 主干依赖]` 月通金气与春荣，财旺生官身自贵。 → 《三命通会》卷九#六辛日乙未时
  - `[ns_smth_09_127]` `[trigger: 天财入库]` `[factor_trigger: tiancai_ruku AND yi_bei_yizhi]` `[role: 条件分支]` 辛以乙为财，未上入库；己被明乙制伏，不能为害。 → 《三命通会》卷九#六辛日乙未时
  - `[ns_smth_09_128]` `[trigger: 通月主贵]` `[factor_trigger: tongyue_zhugui AND xi_nan_yun]` `[role: 总结]` 若通巳酉丑月者，贵，通火，行西运；通金，行南运，俱贵。 → 《三命通会》卷九#六辛日乙未时"""
    normalized_text_zh: str = """"""
    subject: str = "六辛日乙未时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_xin', 'bazi_semantic', 'bazi_state_factor_298', 'bazi_semantic', 'bazi_relation_fire_wood_1', 'bazi_semantic', 'bazi_state_factor_299', 'bazi_semantic', 'hour_branch_wei', 'bazi_semantic', 'bazi_condition_metal_wood_1', 'bazi_semantic', 'source_ref', 'rel_smth_09_094', 'tian_cai_ru_ku', 'rel_smth_09_095', 'tian_cai_ru_ku', 'rel_smth_09_096', 'tong_jinmu_qi', 'evi_smth_09_094', 'tian_cai_ru_ku', 'rule_tiancai_ruku1', 'evi_smth_09_095', 'huomu_xiangcheng', 'rule_huomu_xiangcheng1', 'evi_smth_09_096', 'caiwang_shengguan', 'rule_caiwang_shengguan2', 'map_smth_09_063', 'map_smth_09_064']
    
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
        l1_anchor="smth_v1.0.0_六辛日乙未时_001_L1",
    )
    version: str = "1.0.0"
