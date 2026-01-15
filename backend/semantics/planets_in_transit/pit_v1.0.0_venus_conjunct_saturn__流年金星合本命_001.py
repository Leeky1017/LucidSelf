"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.259599
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
    semantic_id="pit_v1.0.0_venus_conjunct_saturn__流年金星合本命_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusConjunctSaturn流年金星合本命(SemanticEntry):
    """
    > Love meets reality. Serious about relationships. May feel lonely or restricted. Good for commitmen...
    """
    
    original_text: str = """> Love meets reality. Serious about relationships. May feel lonely or restricted. Good for commitments if ready. Practical approach to love.

**Narrative Snippets**:
- `[ns_pit_ve043]` `[trigger: transit_venus_conjunct_natal_saturn]` `[factor_trigger: astro_transit_venus CONJUNCT natal_saturn]` `[role: 主干]` Love meets reality. Serious about relationships. Good for commitments. → PIT Ch7 Venus☌Saturn"""
    normalized_text_zh: str = """"""
    subject: str = "Venus Conjunct Saturn (流年金星合本命土星)"
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
        l1_anchor="pit_v1.0.0_venus_conjunct_saturn__流年金星合本命_001_L1",
    )
    version: str = "1.0.0"
