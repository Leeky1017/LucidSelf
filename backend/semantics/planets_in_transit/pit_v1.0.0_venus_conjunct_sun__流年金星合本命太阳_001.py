"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.258904
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
    semantic_id="pit_v1.0.0_venus_conjunct_sun__流年金星合本命太阳_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusConjunctSun流年金星合本命太阳(SemanticEntry):
    """
    > Day for creativity or love. Want to express yourself with someone else. Feel affectionate and soci...
    """
    
    original_text: str = """> Day for creativity or love. Want to express yourself with someone else. Feel affectionate and sociable. Physical health excellent. Good day to please yourself. Good for entertaining or going out. May be quite popular—magnetism attracts others. Creative activities favored.

**Narrative Snippets**:
- `[ns_pit_ve013]` `[trigger: transit_venus_conjunct_natal_sun]` `[factor_trigger: astro_transit_venus CONJUNCT natal_sun]` `[role: 主干]` Day for creativity or love. Feel affectionate and sociable. Magnetism attracts others. → PIT Ch7 Venus☌Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Venus Conjunct Sun (流年金星合本命太阳)"
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
        l1_anchor="pit_v1.0.0_venus_conjunct_sun__流年金星合本命太阳_001_L1",
    )
    version: str = "1.0.0"
