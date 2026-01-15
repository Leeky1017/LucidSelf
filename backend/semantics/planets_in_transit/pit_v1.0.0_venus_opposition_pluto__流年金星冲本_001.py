"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.260047
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
    semantic_id="pit_v1.0.0_venus_opposition_pluto__流年金星冲本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusOppositionPluto流年金星冲本(SemanticEntry):
    """
    > Others reveal power dynamics in love. May feel controlled or try to control. Good for seeing relat...
    """
    
    original_text: str = """> Others reveal power dynamics in love. May feel controlled or try to control. Good for seeing relationship transformation needs.

**Narrative Snippets**:
- `[ns_pit_ve062]` `[trigger: transit_venus_opposition_natal_pluto]` `[factor_trigger: astro_transit_venus OPPOSITION natal_pluto]` `[role: 主干]` Others reveal power dynamics. See transformation needs. → PIT Ch7 Venus☍Pluto"""
    normalized_text_zh: str = """"""
    subject: str = "Venus Opposition Pluto (流年金星冲本命冥王星)"
    factor_refs: list = ['transit_venus', 'state_love_attraction', 'state_social_harmony', 'state_value_appreciation']
    
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
        l1_anchor="pit_v1.0.0_venus_opposition_pluto__流年金星冲本_001_L1",
    )
    version: str = "1.0.0"
