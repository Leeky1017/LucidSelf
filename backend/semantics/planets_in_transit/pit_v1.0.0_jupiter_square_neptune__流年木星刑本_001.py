"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.310482
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
    semantic_id="pit_v1.0.0_jupiter_square_neptune__流年木星刑本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterSquareNeptune流年木星刑本(SemanticEntry):
    """
    > May be unrealistic or deceived. Spiritual or financial confusion. Avoid important commitments. Che...
    """
    
    original_text: str = """> May be unrealistic or deceived. Spiritual or financial confusion. Avoid important commitments. Check facts and motives.

**Narrative Snippets**:
- `[ns_pit_ju055]` `[trigger: transit_jupiter_square_natal_neptune]` `[factor_trigger: astro_transit_jupiter SQUARE natal_neptune]` `[role: 主干]` May be unrealistic. Avoid important commitments. → PIT Ch9 Jupiter□Neptune"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter Square Neptune (流年木星刑本命海王星)"
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
        l1_anchor="pit_v1.0.0_jupiter_square_neptune__流年木星刑本_001_L1",
    )
    version: str = "1.0.0"
