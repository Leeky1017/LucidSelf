"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.260008
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
    semantic_id="pit_v1.0.0_venus_square_pluto__流年金星刑本命冥王星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusSquarePluto流年金星刑本命冥王星(SemanticEntry):
    """
    > Power struggles in love. Jealousy and possessiveness. Compulsive attractions. Good for seeing mani...
    """
    
    original_text: str = """> Power struggles in love. Jealousy and possessiveness. Compulsive attractions. Good for seeing manipulation patterns.

**Narrative Snippets**:
- `[ns_pit_ve060]` `[trigger: transit_venus_square_natal_pluto]` `[factor_trigger: astro_transit_venus SQUARE natal_pluto]` `[role: 主干]` Power struggles in love. Jealousy. See manipulation patterns. → PIT Ch7 Venus□Pluto"""
    normalized_text_zh: str = """"""
    subject: str = "Venus Square Pluto (流年金星刑本命冥王星)"
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
        l1_anchor="pit_v1.0.0_venus_square_pluto__流年金星刑本命冥王星_001_L1",
    )
    version: str = "1.0.0"
