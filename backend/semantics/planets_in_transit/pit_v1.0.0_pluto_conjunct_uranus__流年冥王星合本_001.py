"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.238826
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
    semantic_id="pit_v1.0.0_pluto_conjunct_uranus__流年冥王星合本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class PlutoConjunctUranus流年冥王星合本(SemanticEntry):
    """
    > Revolutionary transformation. Deep change that can't be resisted. Old structures overthrown. Gener...
    """
    
    original_text: str = """> Revolutionary transformation. Deep change that can't be resisted. Old structures overthrown. Generational transit with personal impact.

**Narrative Snippets**:
- `[ns_pit_pl048]` `[trigger: transit_pluto_conjunct_natal_uranus]` `[factor_trigger: astro_transit_pluto CONJUNCT natal_uranus]` `[role: 主干]` Revolutionary transformation. Old structures overthrown. → PIT Ch13 Pluto☌Uranus"""
    normalized_text_zh: str = """"""
    subject: str = "Pluto Conjunct Uranus (流年冥王星合本命天王星)"
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
        l1_anchor="pit_v1.0.0_pluto_conjunct_uranus__流年冥王星合本_001_L1",
    )
    version: str = "1.0.0"
