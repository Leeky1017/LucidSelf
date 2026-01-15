"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.259347
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
    semantic_id="pit_v1.0.0_venus_square_venus__流年金星刑本命金星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusSquareVenus流年金星刑本命金星(SemanticEntry):
    """
    > Minor relationship or value tensions. May feel unfulfilled. Good for seeing relationship adjustmen...
    """
    
    original_text: str = """> Minor relationship or value tensions. May feel unfulfilled. Good for seeing relationship adjustments needed.

**Narrative Snippets**:
- `[ns_pit_ve030]` `[trigger: transit_venus_square_natal_venus]` `[factor_trigger: astro_transit_venus SQUARE natal_venus]` `[role: 主干]` Minor relationship tensions. See adjustments needed. → PIT Ch7 Venus□Venus"""
    normalized_text_zh: str = """"""
    subject: str = "Venus Square Venus (流年金星刑本命金星)"
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
        l1_anchor="pit_v1.0.0_venus_square_venus__流年金星刑本命金星_001_L1",
    )
    version: str = "1.0.0"
