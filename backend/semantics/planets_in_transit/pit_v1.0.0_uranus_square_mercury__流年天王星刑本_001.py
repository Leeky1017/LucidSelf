"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.207392
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
    semantic_id="pit_v1.0.0_uranus_square_mercury__流年天王星刑本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusSquareMercury流年天王星刑本(SemanticEntry):
    """
    > Mental tension and restlessness. Scattered thinking. Communication disruptions. Good for seeing ri...
    """
    
    original_text: str = """> Mental tension and restlessness. Scattered thinking. Communication disruptions. Good for seeing rigid thinking patterns. Be careful with important decisions.

**Narrative Snippets**:
- `[ns_pit_ur025]` `[trigger: transit_uranus_square_natal_mercury]` `[factor_trigger: astro_transit_uranus SQUARE natal_mercury]` `[role: 主干]` Mental tension. Scattered. Communication disruptions. Careful with decisions. → PIT Ch11 Uranus□Mercury"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus Square Mercury (流年天王星刑本命水星)"
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
        l1_anchor="pit_v1.0.0_uranus_square_mercury__流年天王星刑本_001_L1",
    )
    version: str = "1.0.0"
