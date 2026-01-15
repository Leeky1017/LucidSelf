"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.288429
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
    semantic_id="pit_v1.0.0_mars_sextile_jupiter__流年火星六合本命_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MarsSextileJupiter流年火星六合本命(SemanticEntry):
    """
    > Favorable for action. Opportunities through initiative. Good for travel, legal, education. Confide...
    """
    
    original_text: str = """> Favorable for action. Opportunities through initiative. Good for travel, legal, education. Confidence and optimism.

**Narrative Snippets**:
- `[ns_pit_ma039]` `[trigger: transit_mars_sextile_natal_jupiter]` `[factor_trigger: astro_transit_mars SEXTILE natal_jupiter]` `[role: 主干]` Favorable for action. Opportunities through initiative. → PIT Ch8 Mars⚹Jupiter"""
    normalized_text_zh: str = """"""
    subject: str = "Mars Sextile Jupiter (流年火星六合本命木星)"
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
        l1_anchor="pit_v1.0.0_mars_sextile_jupiter__流年火星六合本命_001_L1",
    )
    version: str = "1.0.0"
