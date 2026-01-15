"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.207358
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
    semantic_id="pit_v1.0.0_uranus_conjunct_mercury__流年天王星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusConjunctMercury流年天王星(SemanticEntry):
    """
    > Sudden new ideas and insights. Mental excitement. May be restless, scattered. Good for innovation....
    """
    
    original_text: str = """> Sudden new ideas and insights. Mental excitement. May be restless, scattered. Good for innovation. Communication surprises. New ways of thinking.

**Narrative Snippets**:
- `[ns_pit_ur023]` `[trigger: transit_uranus_conjunct_natal_mercury]` `[factor_trigger: astro_transit_uranus CONJUNCT natal_mercury]` `[role: 主干]` Sudden new ideas. Mental excitement. Good for innovation. → PIT Ch11 Uranus☌Mercury"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus Conjunct Mercury (流年天王星合本命水星)"
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
        l1_anchor="pit_v1.0.0_uranus_conjunct_mercury__流年天王星_001_L1",
    )
    version: str = "1.0.0"
