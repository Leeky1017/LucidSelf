"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.310188
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
    semantic_id="pit_v1.0.0_jupiter_sextile_mars__流年木星六合本命_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterSextileMars流年木星六合本命(SemanticEntry):
    """
    > Favorable for action. Opportunities through initiative. Good for sports, competition, ventures. Co...
    """
    
    original_text: str = """> Favorable for action. Opportunities through initiative. Good for sports, competition, ventures. Confidence and optimism.

**Narrative Snippets**:
- `[ns_pit_ju034]` `[trigger: transit_jupiter_sextile_natal_mars]` `[factor_trigger: astro_transit_jupiter SEXTILE natal_mars]` `[role: 主干]` Favorable for action. Opportunities through initiative. → PIT Ch9 Jupiter⚹Mars"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter Sextile Mars (流年木星六合本命火星)"
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
        l1_anchor="pit_v1.0.0_jupiter_sextile_mars__流年木星六合本命_001_L1",
    )
    version: str = "1.0.0"
