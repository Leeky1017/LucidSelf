"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339357
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
    semantic_id="smth_v1.0.0_六己日己巳时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六己日己巳时(SemanticEntry):
    """
    - 原文（source_text）：
  六己日生时己巳，金神入火乡。身旺名成，亥卯未为官印，申子辰主财乡。
  己日己巳时，金神入火乡。己以金为子，巳中有庚金长生，丙火建禄，己土专禄。若无破，通月气...
    """
    
    original_text: str = """- 原文（source_text）：
  六己日生时己巳，金神入火乡。身旺名成，亥卯未为官印，申子辰主财乡。
  己日己巳时，金神入火乡。己以金为子，巳中有庚金长生，丙火建禄，己土专禄。若无破，通月气，身旺，富贵；忌刑冲破害。

- 分字分词释义：
  - **金神入火乡**：己巳时，己土坐巳火，巳中藏庚金长生，巳为火地（火乡）。古论“金神”多指乙丑、己巳、癸酉三组干支，金神喜火制，故云“入火乡”。
  - **身旺名成**：日禄归时（己禄在午，巳为帝旺前位，此处指巳为己土旺地，印绶生身），身强。
  - **亥卯未为官印**：亥卯未木局生火（印），木为官，官印相生。
  - **申子辰主财乡**：申子辰水局为财，身旺能任财。

- **规范化释义（primary_lang_explained）**：
  六己日出生于己巳时，为金神入火乡格（或身旺格）。巳中丙火印绶旺，己土得助。若日主身强，无刑冲破害，主富贵名成。若地支见亥卯未木局，为官印相生；见申子辰水局，为财旺生官。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ji Days with Ji-Si Hour":

  - Ji-Si is Metal God entering Fire land; Si contains Geng Metal at longevity and Bing Fire at establishment.
  - If strong body without punishment-clash-break-harm, indicates fame and nobility achieved.
  - If branches form Hai-Mao-Wei Wood bureau, official-seal mutually generate; if Shen-Zi-Chen Water bureau, wealth prospers.
  - Key: Metal God delights in Fire control; strong body can handle wealth and official.

- 核心要点：
  - **金神格**：己巳为金神，喜火炼金，巳本身即为火乡，自带贵气。
  - **日主得禄/旺**：己土坐巳，印生身旺。
  - **喜财官**：身旺喜财官耗泄，忌比劫夺财。

- 详细解说：
  己巳时，火土两旺。若生于冬月（财旺），身强任财，大富；生于春月（官旺），身强任官，大贵。生于夏月，火炎土燥，金神受制太过，宜见水润；生于秋月，食伤泄秀，亦吉。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_021]` `[trigger: 金神入火乡]` `[factor_trigger: jinshen_ruhuoxiang AND shenwang_mingcheng]` `[role: 主干]` 六己日生时己巳，金神入火乡。 → 《三命通会》卷九#六己日己巳时
  - `[ns_smth_09_022]` `[trigger: 身旺名成]` `[factor_trigger: shenwang_mingcheng AND haimaowei_guanyin]` `[role: 主干依赖]` 身旺名成，亥卯未为官印，申子辰主财乡。 → 《三命通会》卷九#六己日己巳时
  - `[ns_smth_09_023]` `[trigger: 无破通月]` `[factor_trigger: wupo_tongyue AND fugui]` `[role: 条件分支]` 若无破，通月气，身旺，富贵。 → 《三命通会》卷九#六己日己巳时
  - `[ns_smth_09_024]` `[trigger: 忌刑冲破害]` `[factor_trigger: ji_xingchong_pohai AND xiong]` `[role: 总结]` 忌刑冲破害。 → 《三命通会》卷九#六己日己巳时"""
    normalized_text_zh: str = """"""
    subject: str = "六己日己巳时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_ji', 'bazi_semantic', 'bazi_state_metal_fire_1', 'bazi_semantic', 'bazi_state_factor_303', 'bazi_semantic', 'bazi_state_factor_260', 'bazi_semantic', 'hour_branch_si', 'bazi_semantic', 'bazi_condition_factor_116', 'bazi_semantic', 'source_ref', 'rel_smth_09_016', 'jinshen_ruhuoxiang', 'rel_smth_09_017', 'shenwang_mingcheng', 'rel_smth_09_018', 'haimaoweimu_ju', 'evi_smth_09_016', 'jinshen_ruhuoxiang', 'rule_jinshen_huoxiang1', 'evi_smth_09_017', 'shenwang_mingcheng', 'rule_shenwang_mingcheng1', 'evi_smth_09_018', 'haimaoweimu_ju', 'rule_haimaoweimu_guanyin1', 'map_smth_09_011', 'map_smth_09_012']
    
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
        l1_anchor="smth_v1.0.0_六己日己巳时_001_L1",
    )
    version: str = "1.0.0"
