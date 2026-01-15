"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.310075
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
    semantic_id="pit_v1.0.0_jupiter_sextile_mercury__流年木星六_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterSextileMercury流年木星六(SemanticEntry):
    """
    > Favorable for learning, teaching, communicating. Good news possible. Positive negotiations. Travel...
    """
    
    original_text: str = """> Favorable for learning, teaching, communicating. Good news possible. Positive negotiations. Travel and education favored.

**Narrative Snippets**:
- `[ns_pit_ju024]` `[trigger: transit_jupiter_sextile_natal_mercury]` `[factor_trigger: astro_transit_jupiter SEXTILE natal_mercury]` `[role: 主干]` Favorable for learning and communicating. Good news possible. → PIT Ch9 Jupiter⚹Mercury"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter Sextile Mercury (流年木星六合本命水星)"
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
        l1_anchor="pit_v1.0.0_jupiter_sextile_mercury__流年木星六_001_L1",
    )
    version: str = "1.0.0"
