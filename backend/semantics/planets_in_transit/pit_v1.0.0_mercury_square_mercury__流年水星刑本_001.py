"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.280974
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
    semantic_id="pit_v1.0.0_mercury_square_mercury__流年水星刑本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MercurySquareMercury流年水星刑本(SemanticEntry):
    """
    > Mental tension and challenges. Thinking tested. May have communication difficulties. Good for iden...
    """
    
    original_text: str = """> Mental tension and challenges. Thinking tested. May have communication difficulties. Good for identifying mental blind spots.

**Narrative Snippets**:
- `[ns_pit_me027]` `[trigger: transit_mercury_square_natal_mercury]` `[factor_trigger: astro_transit_mercury SQUARE natal_mercury]` `[role: 主干]` Mental tension. Thinking tested. Identify mental blind spots. → PIT Ch6 Mercury□Mercury"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury Square Mercury (流年水星刑本命水星)"
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
        l1_anchor="pit_v1.0.0_mercury_square_mercury__流年水星刑本_001_L1",
    )
    version: str = "1.0.0"
