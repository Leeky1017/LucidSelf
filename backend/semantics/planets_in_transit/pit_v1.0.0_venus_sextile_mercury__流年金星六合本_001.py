"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.259226
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
    semantic_id="pit_v1.0.0_venus_sextile_mercury__流年金星六合本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusSextileMercury流年金星六合本(SemanticEntry):
    """
    > Easy expression of affection through words. Good for negotiations about relationships. Social comm...
    """
    
    original_text: str = """> Easy expression of affection through words. Good for negotiations about relationships. Social communications flow.

**Narrative Snippets**:
- `[ns_pit_ve024]` `[trigger: transit_venus_sextile_natal_mercury]` `[factor_trigger: astro_transit_venus SEXTILE natal_mercury]` `[role: 主干]` Easy expression of affection. Good for relationship negotiations. → PIT Ch7 Venus⚹Mercury"""
    normalized_text_zh: str = """"""
    subject: str = "Venus Sextile Mercury (流年金星六合本命水星)"
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
        l1_anchor="pit_v1.0.0_venus_sextile_mercury__流年金星六合本_001_L1",
    )
    version: str = "1.0.0"
