"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.310256
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
    semantic_id="pit_v1.0.0_jupiter_conjunct_jupiter__流年木星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterConjunctJupiter流年木星(SemanticEntry):
    """
    > Jupiter Return (~12 years). New cycle of growth and expansion begins. Opportunities for advancemen...
    """
    
    original_text: str = """> Jupiter Return (~12 years). New cycle of growth and expansion begins. Opportunities for advancement. Review life direction. What do you want to grow into?

**Narrative Snippets**:
- `[ns_pit_ju038]` `[trigger: transit_jupiter_conjunct_natal_jupiter]` `[factor_trigger: astro_transit_jupiter CONJUNCT natal_jupiter]` `[role: 主干]` Jupiter Return. New growth cycle. Review life direction. → PIT Ch9 Jupiter☌Jupiter"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter Conjunct Jupiter (流年木星合本命木星)"
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
        l1_anchor="pit_v1.0.0_jupiter_conjunct_jupiter__流年木星_001_L1",
    )
    version: str = "1.0.0"
