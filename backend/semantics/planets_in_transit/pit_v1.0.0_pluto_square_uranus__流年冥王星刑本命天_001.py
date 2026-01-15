"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.238859
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
    semantic_id="pit_v1.0.0_pluto_square_uranus__流年冥王星刑本命天_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class PlutoSquareUranus流年冥王星刑本命天(SemanticEntry):
    """
    > Power struggles around change. May feel compelled to transform or resist violently. Channel carefu...
    """
    
    original_text: str = """> Power struggles around change. May feel compelled to transform or resist violently. Channel carefully—can be destructive or liberating.

**Narrative Snippets**:
- `[ns_pit_pl050]` `[trigger: transit_pluto_square_natal_uranus]` `[factor_trigger: astro_transit_pluto SQUARE natal_uranus]` `[role: 主干]` Power struggles around change. Channel carefully. → PIT Ch13 Pluto□Uranus"""
    normalized_text_zh: str = """"""
    subject: str = "Pluto Square Uranus (流年冥王星刑本命天王星)"
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
        l1_anchor="pit_v1.0.0_pluto_square_uranus__流年冥王星刑本命天_001_L1",
    )
    version: str = "1.0.0"
