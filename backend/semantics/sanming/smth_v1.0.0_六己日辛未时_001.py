"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339378
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
    semantic_id="smth_v1.0.0_六己日辛未时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六己日辛未时(SemanticEntry):
    """
    - 原文（source_text）：
  六己日生时辛未，食神坐库透天干。不逢刑害无冲破，富贵荣华福寿全。
  己日辛未时，食神助身。己以辛为食，未中藏乙为煞，己土建旺，未为羊刃。若通月气，身旺，贵；...
    """
    
    original_text: str = """- 原文（source_text）：
  六己日生时辛未，食神坐库透天干。不逢刑害无冲破，富贵荣华福寿全。
  己日辛未时，食神助身。己以辛为食，未中藏乙为煞，己土建旺，未为羊刃。若通月气，身旺，贵；不通，富。

- 分字分词释义：
  - **食神坐库**：辛金食神透干，未为木库（煞库），此处未也藏丁己，非金库。古文“坐库”有时指通根余气，未中无金。此处可能指辛金坐未（燥土脆金），或指未中乙木七煞入库。
  - **羊刃**：己土帝旺在巳，未为冠带（一说己土随丁火，未为冠带；随戊土，未为衰）。通常己土无明显羊刃，或以未为刃（阴干刃）。
  - **食神助身**：食神泄秀，非助身（印比助身）。意指食神吐秀为福。

- **规范化释义（primary_lang_explained）**：
  六己日出生于辛未时，辛金食神透出。未中藏乙木七煞和丁火偏印。若无刑冲破害，主富贵福寿。若通月气身旺，更贵。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ji Days with Xin-Wei Hour":

  - Xin Metal Eating God reveals; Wei contains Yi Wood Seven-Killing and Ding Fire Partial Seal.
  - Without punishment-harm-clash-break, indicates riches nobility blessings longevity complete.
  - If passing monthly qi with strong body, even more noble; without monthly qi, still wealthy.
  - Key: Eating God draining brilliance brings fortune; killing hidden in treasury poses no harm.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_029]` `[trigger: 食神坐库]` `[factor_trigger: shishen_zuoku AND tou_tiangan]` `[role: 主干]` 六己日生时辛未，食神坐库透天干。 → 《三命通会》卷九#六己日辛未时
  - `[ns_smth_09_030]` `[trigger: 无刑害冲破]` `[factor_trigger: wu_xinghai_chongpo AND fugui_fushou]` `[role: 主干依赖]` 不逢刑害无冲破，富贵荣华福寿全。 → 《三命通会》卷九#六己日辛未时
  - `[ns_smth_09_031]` `[trigger: 通月身旺]` `[factor_trigger: tongyue_shenwang AND gui]` `[role: 条件分支]` 若通月气，身旺，贵。 → 《三命通会》卷九#六己日辛未时
  - `[ns_smth_09_032]` `[trigger: 不通亦富]` `[factor_trigger: butong_yifu AND shishen_tushou]` `[role: 总结]` 不通，富。 → 《三命通会》卷九#六己日辛未时"""
    normalized_text_zh: str = """"""
    subject: str = "六己日辛未时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_ji', 'bazi_semantic', 'bazi_state_shishen_tougan', 'bazi_semantic', 'bazi_relation_factor_113', 'bazi_semantic', 'bazi_state_factor_313', 'bazi_semantic', 'hour_branch_wei', 'bazi_semantic', 'bazi_condition_factor_116', 'bazi_semantic', 'source_ref', 'rel_smth_09_022', 'shishen_tougan', 'rel_smth_09_023', 'sha_ruku', 'rel_smth_09_024', 'shenwang_tongyueqi', 'evi_smth_09_022', 'shishen_tougan', 'rule_shishen_tougan1', 'evi_smth_09_023', 'sha_ruku', 'rule_wupoxinghai1', 'evi_smth_09_024', 'fushou_shuangquan', 'rule_fushou_shuangquan1', 'map_smth_09_015', 'map_smth_09_016']
    
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
        l1_anchor="smth_v1.0.0_六己日辛未时_001_L1",
    )
    version: str = "1.0.0"
