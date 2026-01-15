"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.288293
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
    semantic_id="pit_v1.0.0_mars_square_venus__流年火星刑本命金星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MarsSquareVenus流年火星刑本命金星(SemanticEntry):
    """
    > Tension between desire and affection. Relationship conflicts. Sexual frustration possible. Good fo...
    """
    
    original_text: str = """> Tension between desire and affection. Relationship conflicts. Sexual frustration possible. Good for seeing what you really want.

**Narrative Snippets**:
- `[ns_pit_ma030]` `[trigger: transit_mars_square_natal_venus]` `[factor_trigger: astro_transit_mars SQUARE natal_venus]` `[role: 主干]` Tension between desire and love. Conflicts possible. → PIT Ch8 Mars□Venus"""
    normalized_text_zh: str = """"""
    subject: str = "Mars Square Venus (流年火星刑本命金星)"
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
        l1_anchor="pit_v1.0.0_mars_square_venus__流年火星刑本命金星_001_L1",
    )
    version: str = "1.0.0"
