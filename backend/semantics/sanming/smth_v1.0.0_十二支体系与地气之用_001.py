"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227586
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
    semantic_id="smth_v1.0.0_十二支体系与地气之用_001",
    book_id="sanming",
    engine_id="bazi"
)
class 十二支体系与地气之用(SemanticEntry):
    """
    - **原文（source_text）**：
  夫清阳为天，五行彰而十干立；浊阴为地，八方定而十二支分。运移气迁，岁岁而盈虚应纪；上升下降，物物而变化可期。所以支干配合，共臻妙用矣。

- 分字分词...
    """
    
    original_text: str = """- **原文（source_text）**：
  夫清阳为天，五行彰而十干立；浊阴为地，八方定而十二支分。运移气迁，岁岁而盈虚应纪；上升下降，物物而变化可期。所以支干配合，共臻妙用矣。

- 分字分词释义：
  - **清阳为天、浊阴为地**：以清扬之气为天，以沉浊之气为地，干主天、支主地。
  - **八方定而十二支分**：以方位与节令划分十二支，各有定位。
  - **支干配合，共臻妙用**：干支合用，才能完整刻画时空与气机。

- **规范化释义（primary_lang_explained）**：
  本段总说十二支之立：十干偏重天道、五行德性，十二支偏重地气、方位与节令。清阳上腾成天，浊阴下凝成地，于是十干、十二支各司其职，随运移气迁而记录岁岁盈虚。只有干支相配，才能真正表达出时间、空间与气机三者的交织。

- **完整对等诠释（secondary_lang_full）**：

  This opening explanation of the Twelve Earthly Branches states that while the Ten Heavenly Stems emphasise heaven’s movement and elemental virtue, the Branches emphasise earth’s Qi, directions and seasonal phases. Clear, rising Yang becomes heaven and is expressed through the stems; turbid, settling Yin becomes earth and is articulated through the twelve positions around the compass. As fate and Qi shift, these signs record the yearly waxing and waning of fullness and depletion. Only when stems and branches are used together do we get a complete picture of time, place and Qi: the stems supplying overarching principles from above, the branches specifying ground conditions, environments and concrete situations in which those principles are played out."""
    normalized_text_zh: str = """"""
    subject: str = "十二支体系与地气之用"
    factor_refs: list = ['source_ref']
    
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
        l1_anchor="smth_v1.0.0_十二支体系与地气之用_001_L1",
    )
    version: str = "1.0.0"
