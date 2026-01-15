"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.281157
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
    semantic_id="pit_v1.0.0_mercury_conjunct_saturn__流年水星合_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MercuryConjunctSaturn流年水星合(SemanticEntry):
    """
    > Serious, disciplined thinking. Good for detailed planning. May feel mentally heavy or pessimistic....
    """
    
    original_text: str = """> Serious, disciplined thinking. Good for detailed planning. May feel mentally heavy or pessimistic. Good for practical decisions.

**Narrative Snippets**:
- `[ns_pit_me045]` `[trigger: transit_mercury_conjunct_natal_saturn]` `[factor_trigger: astro_transit_mercury CONJUNCT natal_saturn]` `[role: 主干]` Serious disciplined thinking. Good for detailed planning. May feel mentally heavy. → PIT Ch6 Mercury☌Saturn"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury Conjunct Saturn (流年水星合本命土星)"
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
        l1_anchor="pit_v1.0.0_mercury_conjunct_saturn__流年水星合_001_L1",
    )
    version: str = "1.0.0"
