"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412540
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
    semantic_id="smth_v1.0.0_红鸾天印与福贵相兼_001",
    book_id="sanming",
    engine_id="bazi"
)
class 红鸾天印与福贵相兼(SemanticEntry):
    """
    - **原文（source_text）**：

  红鸾天印：谓丙食戊而得戊戌，辛食癸而得癸丑，壬甲辰，乙丁未，日时得之，主富贵。

- 分字分词释义：

  - **红鸾**：本为吉曜名，主喜庆、婚...
    """
    
    original_text: str = """- **原文（source_text）**：

  红鸾天印：谓丙食戊而得戊戌，辛食癸而得癸丑，壬甲辰，乙丁未，日时得之，主富贵。

- 分字分词释义：

  - **红鸾**：本为吉曜名，主喜庆、婚姻、人缘之福。
  - **天印**：指印绶得地，有“天授之印”的意味，主凭信、护身与资助。
  - **丙食戊而得戊戌、辛食癸而得癸丑、壬得甲辰、乙得丁未**：分别指丙、辛、壬、乙等日主，其食神落在特定库地（戌、丑、辰、未），兼具食神与印、库之象。

- **规范化释义（primary_lang_explained）**：

  红鸾天印格，是把“喜庆之星”与“印绶之星”合而一谈的一类结构。丙日用戊为食，若日时得戊戌；辛日用癸为食，若得癸丑；壬日得甲辰；乙日得丁未，皆是食神落在库地、兼有印绶之象，象征命主既有福缘、人缘，又有凭信与身份的护持，故主富而且贵。

- 核心要点：

  - 红鸾天印以**食神 + 印绶 + 库地**三者合一为核心。
  - 既主喜庆、人缘，又主凭信、护身，多对应生活中“有人请托、有位可坐”的状态。
  - 忌库地受冲破或印绶被财星过度克制，否则福贵难以成全。

- 详细解说：

  从结构上看，此格体现的是“福、名、位三合一”：

  - 食神代表福气与才情，落在戌、丑、辰、未等库地，则福气有所积累与沉淀；
  - 库中往往兼藏印绶或与印有生合关系，使此等福气得以制度化为“凭信与身份”；
  - 若再行运得宜，多主婚姻顺遂、事业有靠、名分不轻。

  然而，一旦库地被冲开（如戌逢辰冲、丑逢未冲等），或印绶被财星重重克制，则“红鸾”“天印”之吉难以尽展，反可能在婚姻、人际、名誉方面反覆折损。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_117]` `[trigger: 红鸾天印]` `[factor_trigger: hongluan_tianyin AND shishen_ruku]` `[role: 主干]` 红鸾天印者，丙食戊而得戊戌，辛食癸而得癸丑，食神入墓库且印绶同宫。 → 《三命通会》卷六#红鸾天印与福贵相兼
  - `[ns_smth_06_118]` `[trigger: 福名位三合]` `[factor_trigger: fu_ming_wei AND sanheyi]` `[role: 主干依赖]` 红鸾天印体现福、名、位三合一，既主喜庆人缘，又主凭信护身。 → 《三命通会》卷六#红鸾天印与福贵相兼
  - `[ns_smth_06_119]` `[trigger: 库冲印克]` `[factor_trigger: kudi_chongkai OR yinshou_caike]` `[role: 条件分支]` 库地被冲开或印绶被财星克制，则红鸾天印之吉难以尽展。 → 《三命通会》卷六#红鸾天印与福贵相兼
  - `[ns_smth_06_120]` `[trigger: 红鸾结论]` `[factor_trigger: hongluan_tianyin AND wupo]` `[role: 总结]` 得红鸾天印者，多主婚姻顺遂、事业有靠、名分不轻。 → 《三命通会》卷六#红鸾天印与福贵相兼

- **校勘与字词辨析（双语）**：

  - 原文未细分"红鸾"与"天印"的星曜渊源，本稿仅按常见象义分别理解为“喜庆”与“印绶”。
  - “主富贵”一句，在本稿中具体化为“人缘较佳、身份有凭、物质与名誉皆不落下风”。
  - 各例中具体干支组合，本稿不再逐一推命，只作结构示范。
  - **English**：
    - Example charts are not individually analyzed; only structural demonstration is provided."""
    normalized_text_zh: str = """"""
    subject: str = "红鸾天印与福贵相兼"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_26', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_degree_11', 'bazi_semantic', 'bazi_state_strength_5', 'bazi_semantic', 'bazi_condition_factor_168', 'bazi_semantic', 'bazi_condition_factor_169', 'bazi_semantic', 'source_ref', 'rel_smth_06_085', 'hongluan_tianyin_presence', 'rel_smth_06_086', 'kudi_wengu', 'rel_smth_06_087', 'kudi_chong_risk', 'evi_smth_06_085', 'hongluan_tianyin_presence', 'rule_hongluan', 'evi_smth_06_086', 'kudi_wengu', 'rule_fugui_hl', 'evi_smth_06_087', 'kudi_chong_risk', 'rule_chongku', 'map_smth_06_057', 'map_smth_06_058']
    
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
        l1_anchor="smth_v1.0.0_红鸾天印与福贵相兼_001_L1",
    )
    version: str = "1.0.0"
