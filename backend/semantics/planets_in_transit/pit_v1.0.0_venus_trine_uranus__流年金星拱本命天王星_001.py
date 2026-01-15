"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.259832
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
    semantic_id="pit_v1.0.0_venus_trine_uranus__流年金星拱本命天王星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusTrineUranus流年金星拱本命天王星(SemanticEntry):
    """
    > Exciting but harmonious love experiences. Pleasant surprises. Creative inspiration. Freedom in rel...
    """
    
    original_text: str = """> Exciting but harmonious love experiences. Pleasant surprises. Creative inspiration. Freedom in relationships.

**Narrative Snippets**:
- `[ns_pit_ve051]` `[trigger: transit_venus_trine_natal_uranus]` `[factor_trigger: astro_transit_venus TRINE natal_uranus]` `[role: 主干]` Exciting harmonious love. Pleasant surprises. Creative inspiration. → PIT Ch7 Venus△Uranus"""
    normalized_text_zh: str = """"""
    subject: str = "Venus Trine Uranus (流年金星拱本命天王星)"
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
        l1_anchor="pit_v1.0.0_venus_trine_uranus__流年金星拱本命天王星_001_L1",
    )
    version: str = "1.0.0"
