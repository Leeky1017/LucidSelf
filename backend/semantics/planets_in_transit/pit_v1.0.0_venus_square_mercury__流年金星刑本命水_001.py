"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.259247
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
    semantic_id="pit_v1.0.0_venus_square_mercury__流年金星刑本命水_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusSquareMercury流年金星刑本命水(SemanticEntry):
    """
    > Minor difficulties expressing feelings. Social communications may be awkward. Not best time for im...
    """
    
    original_text: str = """> Minor difficulties expressing feelings. Social communications may be awkward. Not best time for important relationship discussions.

**Narrative Snippets**:
- `[ns_pit_ve025]` `[trigger: transit_venus_square_natal_mercury]` `[factor_trigger: astro_transit_venus SQUARE natal_mercury]` `[role: 主干]` Minor difficulties expressing feelings. Social communications awkward. → PIT Ch7 Venus□Mercury"""
    normalized_text_zh: str = """"""
    subject: str = "Venus Square Mercury (流年金星刑本命水星)"
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
        l1_anchor="pit_v1.0.0_venus_square_mercury__流年金星刑本命水_001_L1",
    )
    version: str = "1.0.0"
