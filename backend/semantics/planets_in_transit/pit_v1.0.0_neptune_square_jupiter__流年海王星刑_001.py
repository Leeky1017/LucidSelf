"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.273019
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
    semantic_id="pit_v1.0.0_neptune_square_jupiter__流年海王星刑_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneSquareJupiter流年海王星刑(SemanticEntry):
    """
    > May be unrealistic or deceived. Spiritual or financial confusion. Avoid important commitments. Che...
    """
    
    original_text: str = """> May be unrealistic or deceived. Spiritual or financial confusion. Avoid important commitments. Check facts and motives.

**Narrative Snippets**:
- `[ns_pit_ne040]` `[trigger: transit_neptune_square_natal_jupiter]` `[factor_trigger: astro_transit_neptune SQUARE natal_jupiter]` `[role: 主干]` May be unrealistic. Avoid important commitments. → PIT Ch12 Neptune□Jupiter"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune Square Jupiter (流年海王星刑本命木星)"
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
        l1_anchor="pit_v1.0.0_neptune_square_jupiter__流年海王星刑_001_L1",
    )
    version: str = "1.0.0"
