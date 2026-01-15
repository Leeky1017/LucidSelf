"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.272972
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
    semantic_id="pit_v1.0.0_neptune_square_mars__流年海王星刑本命火_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneSquareMars流年海王星刑本命火(SemanticEntry):
    """
    > Actions confused or undermined. Deception possible. Energy low or misdirected. Avoid important com...
    """
    
    original_text: str = """> Actions confused or undermined. Deception possible. Energy low or misdirected. Avoid important commitments.

**Narrative Snippets**:
- `[ns_pit_ne035]` `[trigger: transit_neptune_square_natal_mars]` `[factor_trigger: astro_transit_neptune SQUARE natal_mars]` `[role: 主干]` Actions confused. Deception possible. Avoid important commitments. → PIT Ch12 Neptune□Mars"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune Square Mars (流年海王星刑本命火星)"
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
        l1_anchor="pit_v1.0.0_neptune_square_mars__流年海王星刑本命火_001_L1",
    )
    version: str = "1.0.0"
