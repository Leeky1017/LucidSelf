"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.318634
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
    semantic_id="pit_v1.0.0_saturn_conjunct_mercury__流年土星合_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SaturnConjunctMercury流年土星合(SemanticEntry):
    """
    > Serious, disciplined thinking. Good for detailed planning. May feel mentally heavy or pessimistic....
    """
    
    original_text: str = """> Serious, disciplined thinking. Good for detailed planning. May feel mentally heavy or pessimistic. Good for practical decisions and contracts.

**Narrative Snippets**:
- `[ns_pit_sa023]` `[trigger: transit_saturn_conjunct_natal_mercury]` `[factor_trigger: astro_transit_saturn CONJUNCT natal_mercury]` `[role: 主干]` Serious disciplined thinking. Good for detailed planning. → PIT Ch10 Saturn☌Mercury"""
    normalized_text_zh: str = """"""
    subject: str = "Saturn Conjunct Mercury (流年土星合本命水星)"
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
        l1_anchor="pit_v1.0.0_saturn_conjunct_mercury__流年土星合_001_L1",
    )
    version: str = "1.0.0"
