"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.281267
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
    semantic_id="pit_v1.0.0_mercury_square_uranus__流年水星刑本命_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MercurySquareUranus流年水星刑本命(SemanticEntry):
    """
    > Mental restlessness and disruption. Scattered thinking. Impulsive communications you may regret. U...
    """
    
    original_text: str = """> Mental restlessness and disruption. Scattered thinking. Impulsive communications you may regret. Unexpected changes in plans.

**Narrative Snippets**:
- `[ns_pit_me052]` `[trigger: transit_mercury_square_natal_uranus]` `[factor_trigger: astro_transit_mercury SQUARE natal_uranus]` `[role: 主干]` Mental restlessness. Scattered thinking. Impulsive communications you may regret. → PIT Ch6 Mercury□Uranus"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury Square Uranus (流年水星刑本命天王星)"
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
        l1_anchor="pit_v1.0.0_mercury_square_uranus__流年水星刑本命_001_L1",
    )
    version: str = "1.0.0"
