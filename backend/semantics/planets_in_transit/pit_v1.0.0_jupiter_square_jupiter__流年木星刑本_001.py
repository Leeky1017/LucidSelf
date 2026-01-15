"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.310282
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
    semantic_id="pit_v1.0.0_jupiter_square_jupiter__流年木星刑本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterSquareJupiter流年木星刑本(SemanticEntry):
    """
    > Growth patterns tested. May have overexpanded. Time to consolidate. Check if beliefs still serve y...
    """
    
    original_text: str = """> Growth patterns tested. May have overexpanded. Time to consolidate. Check if beliefs still serve you.

**Narrative Snippets**:
- `[ns_pit_ju040]` `[trigger: transit_jupiter_square_natal_jupiter]` `[factor_trigger: astro_transit_jupiter SQUARE natal_jupiter]` `[role: 主干]` Growth patterns tested. Time to consolidate. → PIT Ch9 Jupiter□Jupiter"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter Square Jupiter (流年木星刑本命木星)"
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
        l1_anchor="pit_v1.0.0_jupiter_square_jupiter__流年木星刑本_001_L1",
    )
    version: str = "1.0.0"
