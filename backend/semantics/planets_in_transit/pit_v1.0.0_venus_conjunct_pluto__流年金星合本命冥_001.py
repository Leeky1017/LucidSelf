"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.259968
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
    semantic_id="pit_v1.0.0_venus_conjunct_pluto__流年金星合本命冥_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusConjunctPluto流年金星合本命冥(SemanticEntry):
    """
    > Intense, transformative love. Deep feelings surface. May feel obsessive. Power dynamics in relatio...
    """
    
    original_text: str = """> Intense, transformative love. Deep feelings surface. May feel obsessive. Power dynamics in relationships. Profound connections.

**Narrative Snippets**:
- `[ns_pit_ve058]` `[trigger: transit_venus_conjunct_natal_pluto]` `[factor_trigger: astro_transit_venus CONJUNCT natal_pluto]` `[role: 主干]` Intense transformative love. Deep feelings. Power dynamics. → PIT Ch7 Venus☌Pluto"""
    normalized_text_zh: str = """"""
    subject: str = "Venus Conjunct Pluto (流年金星合本命冥王星)"
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
        l1_anchor="pit_v1.0.0_venus_conjunct_pluto__流年金星合本命冥_001_L1",
    )
    version: str = "1.0.0"
