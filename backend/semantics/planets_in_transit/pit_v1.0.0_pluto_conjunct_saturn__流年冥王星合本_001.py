"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.238660
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
    semantic_id="pit_v1.0.0_pluto_conjunct_saturn__流年冥王星合本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class PlutoConjunctSaturn流年冥王星合本(SemanticEntry):
    """
    > Power meets structure. Deep transformation of life structures. May feel compelled to change fundam...
    """
    
    original_text: str = """> Power meets structure. Deep transformation of life structures. May feel compelled to change fundamentally. Powerful but slow transformation.

**Narrative Snippets**:
- `[ns_pit_pl043]` `[trigger: transit_pluto_conjunct_natal_saturn]` `[factor_trigger: astro_transit_pluto CONJUNCT natal_saturn]` `[role: 主干]` Power meets structure. Deep transformation. Fundamental change. → PIT Ch13 Pluto☌Saturn"""
    normalized_text_zh: str = """"""
    subject: str = "Pluto Conjunct Saturn (流年冥王星合本命土星)"
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
        l1_anchor="pit_v1.0.0_pluto_conjunct_saturn__流年冥王星合本_001_L1",
    )
    version: str = "1.0.0"
