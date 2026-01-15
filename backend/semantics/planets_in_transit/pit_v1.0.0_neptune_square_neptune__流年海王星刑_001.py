"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.273186
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
    semantic_id="pit_v1.0.0_neptune_square_neptune__流年海王星刑_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneSquareNeptune流年海王星刑(SemanticEntry):
    """
    > Spiritual crisis and questioning (~41-42 and ~123 years). Dreams and ideals tested. Disillusionmen...
    """
    
    original_text: str = """> Spiritual crisis and questioning (~41-42 and ~123 years). Dreams and ideals tested. Disillusionment possible but leads to deeper understanding.

**Narrative Snippets**:
- `[ns_pit_ne055]` `[trigger: transit_neptune_square_natal_neptune]` `[factor_trigger: astro_transit_neptune SQUARE natal_neptune]` `[role: 主干]` Spiritual crisis (~41-42). Dreams tested. Disillusionment possible. → PIT Ch12 Neptune□Neptune"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune Square Neptune (流年海王星刑本命海王星)"
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
        l1_anchor="pit_v1.0.0_neptune_square_neptune__流年海王星刑_001_L1",
    )
    version: str = "1.0.0"
