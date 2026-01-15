"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.207250
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
    semantic_id="pit_v1.0.0_uranus_opposition_sun__流年天王星冲本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusOppositionSun流年天王星冲本(SemanticEntry):
    """
    > Others bring disruption and change. May feel others trying to upset your identity. Good for seeing...
    """
    
    original_text: str = """> Others bring disruption and change. May feel others trying to upset your identity. Good for seeing where you need more freedom. Relationships may be volatile.

**Narrative Snippets**:
- `[ns_pit_ur017]` `[trigger: transit_uranus_opposition_natal_sun]` `[factor_trigger: astro_transit_uranus OPPOSITION natal_sun]` `[role: 主干]` Others bring disruption. See freedom needs. Relationships volatile. → PIT Ch11 Uranus☍Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus Opposition Sun (流年天王星冲本命太阳)"
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
        l1_anchor="pit_v1.0.0_uranus_opposition_sun__流年天王星冲本_001_L1",
    )
    version: str = "1.0.0"
