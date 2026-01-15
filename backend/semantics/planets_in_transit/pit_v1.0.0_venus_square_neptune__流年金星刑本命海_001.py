"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.259911
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
    semantic_id="pit_v1.0.0_venus_square_neptune__流年金星刑本命海_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusSquareNeptune流年金星刑本命海(SemanticEntry):
    """
    > Confusion in love. May be deceived or self-deceiving. Romantic illusions. Avoid important decision...
    """
    
    original_text: str = """> Confusion in love. May be deceived or self-deceiving. Romantic illusions. Avoid important decisions. Not good for commitments.

**Narrative Snippets**:
- `[ns_pit_ve055]` `[trigger: transit_venus_square_natal_neptune]` `[factor_trigger: astro_transit_venus SQUARE natal_neptune]` `[role: 主干]` Confusion in love. May be deceived. Avoid important decisions. → PIT Ch7 Venus□Neptune"""
    normalized_text_zh: str = """"""
    subject: str = "Venus Square Neptune (流年金星刑本命海王星)"
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
        l1_anchor="pit_v1.0.0_venus_square_neptune__流年金星刑本命海_001_L1",
    )
    version: str = "1.0.0"
