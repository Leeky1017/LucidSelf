"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.208510
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
    semantic_id="pit_v1.0.0_uranus_opposition_pluto__流年天王星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusOppositionPluto流年天王星(SemanticEntry):
    """
    > Others wield transformative power. Power struggles over freedom. Good for seeing where you need to...
    """
    
    original_text: str = """> Others wield transformative power. Power struggles over freedom. Good for seeing where you need to transform or be transformed.

**Narrative Snippets**:
- `[ns_pit_ur062]` `[trigger: transit_uranus_opposition_natal_pluto]` `[factor_trigger: astro_transit_uranus OPPOSITION natal_pluto]` `[role: 主干]` Others wield transformative power. Power struggles over freedom. → PIT Ch11 Uranus☍Pluto"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus Opposition Pluto (流年天王星冲本命冥王星)"
    factor_refs: list = ['transit_uranus', 'cycle_uranus_opposition', 'state_liberation', 'state_disruption']
    
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
        l1_anchor="pit_v1.0.0_uranus_opposition_pluto__流年天王星_001_L1",
    )
    version: str = "1.0.0"
