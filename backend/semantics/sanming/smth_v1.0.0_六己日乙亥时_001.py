"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339418
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
    semantic_id="smth_v1.0.0_六己日乙亥时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六己日乙亥时(SemanticEntry):
    """
    - 原文（source_text）：
  六己日生时乙亥，煞官得地木滋荣。不通月气平常论，运入东方极显荣。
  己日乙亥时，煞官得地。己用甲为官，乙为煞，壬为财。亥上壬水旺，甲木长生，乙木死，己土绝。...
    """
    
    original_text: str = """- 原文（source_text）：
  六己日生时乙亥，煞官得地木滋荣。不通月气平常论，运入东方极显荣。
  己日乙亥时，煞官得地。己用甲为官，乙为煞，壬为财。亥上壬水旺，甲木长生，乙木死，己土绝。若通月气，贵；不通，平常。

- 分字分词释义：
  - **煞官得地**：亥为甲木（官）长生之地，乙木（煞）虽死，但亥中壬水生木，木气滋荣。
  - **运入东方**：东方木运（寅卯辰），助起官煞。

- **规范化释义（primary_lang_explained）**：
  六己日出生于乙亥时，乙木七煞透出，坐亥水长生之地（甲木长生），财官煞皆得地利。若日主通月气身旺，主贵。若不通月气身弱，则平常。若大运流向东方木地，官煞得助，身若能任，极显荣。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ji Days with Yi-Hai Hour":

  - Yi Wood Seven-Killing reveals; Hai is where Jia Wood (Official) is at longevity—"killing-official gaining ground, wood nourished gloriously."
  - Without passing monthly qi, ordinary assessment; if luck enters Eastern Wood direction, extremely glorious.
  - If passing monthly qi with strong body, indicates nobility; otherwise ordinary.
  - Key: Water generates Wood creating prosperous killing-official; body must be strong enough to handle.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_045]` `[trigger: 煞官得地]` `[factor_trigger: shaguan_dedi AND mu_zirong]` `[role: 主干]` 六己日生时乙亥，煞官得地木滋荣。 → 《三命通会》卷九#六己日乙亥时
  - `[ns_smth_09_046]` `[trigger: 不通平常]` `[factor_trigger: butong_pingchang AND yun_ru_dongfang]` `[role: 主干依赖]` 不通月气平常论，运入东方极显荣。 → 《三命通会》卷九#六己日乙亥时
  - `[ns_smth_09_047]` `[trigger: 通月身旺]` `[factor_trigger: tongyue_shenwang AND gui]` `[role: 条件分支]` 若通月气，贵。 → 《三命通会》卷九#六己日乙亥时
  - `[ns_smth_09_048]` `[trigger: 身弱不通]` `[factor_trigger: shenruo_butong AND pingchang]` `[role: 总结]` 不通，平常。 → 《三命通会》卷九#六己日乙亥时"""
    normalized_text_zh: str = """"""
    subject: str = "六己日乙亥时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_ji', 'bazi_semantic', 'bazi_state_factor_268', 'bazi_semantic', 'bazi_relation_water_wood', 'bazi_semantic', 'bazi_state_factor_269', 'bazi_semantic', 'hour_branch_hai', 'bazi_semantic', 'bazi_condition_factor_120', 'bazi_semantic', 'source_ref', 'rel_smth_09_034', 'shaguan_dedi', 'rel_smth_09_035', 'shenchu_juedi', 'rel_smth_09_036', 'yun_ru_dongfang', 'evi_smth_09_034', 'shaguan_dedi', 'rule_shaguan_dedi1', 'evi_smth_09_035', 'shenchu_juedi', 'rule_butong_pingchang1', 'evi_smth_09_036', 'yun_ru_dongfang', 'rule_dongfang_xianrong1', 'map_smth_09_023', 'map_smth_09_024']
    
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
        l1_anchor="smth_v1.0.0_六己日乙亥时_001_L1",
    )
    version: str = "1.0.0"
