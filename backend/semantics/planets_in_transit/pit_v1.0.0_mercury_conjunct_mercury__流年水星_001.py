"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.280955
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
    semantic_id="pit_v1.0.0_mercury_conjunct_mercury__流年水星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MercuryConjunctMercury流年水星(SemanticEntry):
    """
    > Mercury Return—mental cycle renewal. Communications intensified. Mind particularly clear for your ...
    """
    
    original_text: str = """> Mercury Return—mental cycle renewal. Communications intensified. Mind particularly clear for your natural way of thinking. Good for planning and decisions.

**Narrative Snippets**:
- `[ns_pit_me025]` `[trigger: transit_mercury_conjunct_natal_mercury]` `[factor_trigger: astro_transit_mercury CONJUNCT natal_mercury]` `[role: 主干]` Mercury Return—mental renewal. Communications intensified. Mind clear. → PIT Ch6 Mercury☌Mercury"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury Conjunct Mercury (流年水星合本命水星)"
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
        l1_anchor="pit_v1.0.0_mercury_conjunct_mercury__流年水星_001_L1",
    )
    version: str = "1.0.0"
