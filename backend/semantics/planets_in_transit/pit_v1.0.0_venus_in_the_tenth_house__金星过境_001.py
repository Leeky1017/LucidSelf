"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.258838
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
    semantic_id="pit_v1.0.0_venus_in_the_tenth_house__金星过境_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusInTheTenthHouse金星过境(SemanticEntry):
    """
    **Source Text** (Lines 6981-6998):
> Creates favorable circumstances in business/professional life. ...
    """
    
    original_text: str = """**Source Text** (Lines 6981-6998):
> Creates favorable circumstances in business/professional life. Attracts persons and circumstances that facilitate work. People in authority favorably inclined. Relationships run smoothly. May involve in artistic matters—design, layout, redecorating, public relations. New love would be with older person or "guide figure." Be careful of mercenary motives.

**English Paraphrase**: Favorable for business/career. Attracts helpful people. Good with authorities. May do artistic work. New love with guide figure. Avoid mercenary motives.

**Complete Chinese Interpretation**: 对事业/职业有利。吸引有帮助的人。与权威人士关系好。可能做艺术工作。与导师型人物的新恋情。避免唯利是图的动机。

**Narrative Snippets**:
- `[ns_pit_ve010]` `[trigger: venus_transit_house_10]` `[factor_trigger: astro_transit_venus AND astro_house_10]` `[role: 主干]` Favorable for career. Good with authorities. May do artistic work professionally. → PIT Ch7 Venus-10H"""
    normalized_text_zh: str = """"""
    subject: str = "Venus in the Tenth House (金星过境第十宫)"
    factor_refs: list = []
    
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
        book_id="planets_in_transit",
        chapter="",
        l1_anchor="pit_v1.0.0_venus_in_the_tenth_house__金星过境_001_L1",
    )
    version: str = "1.0.0"
