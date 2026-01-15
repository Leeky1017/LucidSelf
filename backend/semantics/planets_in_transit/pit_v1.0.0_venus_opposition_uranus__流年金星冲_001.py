"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.259852
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
    semantic_id="pit_v1.0.0_venus_opposition_uranus__流年金星冲_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusOppositionUranus流年金星冲(SemanticEntry):
    """
    > Others disrupt love equilibrium. Sudden relationship changes. Good for seeing where you need more ...
    """
    
    original_text: str = """> Others disrupt love equilibrium. Sudden relationship changes. Good for seeing where you need more freedom or stability.

**Narrative Snippets**:
- `[ns_pit_ve052]` `[trigger: transit_venus_opposition_natal_uranus]` `[factor_trigger: astro_transit_venus OPPOSITION natal_uranus]` `[role: 主干]` Others disrupt love. Sudden changes. See freedom/stability needs. → PIT Ch7 Venus☍Uranus"""
    normalized_text_zh: str = """"""
    subject: str = "Venus Opposition Uranus (流年金星冲本命天王星)"
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
        l1_anchor="pit_v1.0.0_venus_opposition_uranus__流年金星冲_001_L1",
    )
    version: str = "1.0.0"
