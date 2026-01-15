"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.273141
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
    semantic_id="pit_v1.0.0_neptune_square_uranus__流年海王星刑本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneSquareUranus流年海王星刑本(SemanticEntry):
    """
    > Tension between dreams and change. Confusion about freedom. May feel lost between ideals and reali...
    """
    
    original_text: str = """> Tension between dreams and change. Confusion about freedom. May feel lost between ideals and reality.

**Narrative Snippets**:
- `[ns_pit_ne050]` `[trigger: transit_neptune_square_natal_uranus]` `[factor_trigger: astro_transit_neptune SQUARE natal_uranus]` `[role: 主干]` Tension dreams vs change. Confusion about freedom. → PIT Ch12 Neptune□Uranus"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune Square Uranus (流年海王星刑本命天王星)"
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
        l1_anchor="pit_v1.0.0_neptune_square_uranus__流年海王星刑本_001_L1",
    )
    version: str = "1.0.0"
