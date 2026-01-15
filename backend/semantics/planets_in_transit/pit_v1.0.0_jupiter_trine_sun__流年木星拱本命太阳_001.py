"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.309956
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
    semantic_id="pit_v1.0.0_jupiter_trine_sun__流年木星拱本命太阳_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterTrineSun流年木星拱本命太阳(SemanticEntry):
    """
    > Excellent for expansion and growth. Opportunities flow easily. Good health and optimism. Success i...
    """
    
    original_text: str = """> Excellent for expansion and growth. Opportunities flow easily. Good health and optimism. Success in ventures. Good for travel, education, legal matters. Others help you.

**Narrative Snippets**:
- `[ns_pit_ju016]` `[trigger: transit_jupiter_trine_natal_sun]` `[factor_trigger: astro_transit_jupiter TRINE natal_sun]` `[role: 主干]` Excellent for expansion. Opportunities flow. Success in ventures. → PIT Ch9 Jupiter△Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter Trine Sun (流年木星拱本命太阳)"
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
        l1_anchor="pit_v1.0.0_jupiter_trine_sun__流年木星拱本命太阳_001_L1",
    )
    version: str = "1.0.0"
