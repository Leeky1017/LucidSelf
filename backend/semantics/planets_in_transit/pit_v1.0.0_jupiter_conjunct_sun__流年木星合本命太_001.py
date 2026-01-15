"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.309921
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
    semantic_id="pit_v1.0.0_jupiter_conjunct_sun__流年木星合本命太_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterConjunctSun流年木星合本命太(SemanticEntry):
    """
    > One of most marvelous transits. At least feel good—optimistic, healthy. Beginning of new twelve-ye...
    """
    
    original_text: str = """> One of most marvelous transits. At least feel good—optimistic, healthy. Beginning of new twelve-year cycle. Initiate new projects, expand activities. May escape narrowing circumstances. Good for study, going back to school. Meet people who expose you to new aspects. Freedom increases. Pitfalls: overreach, extravagance. Don't overinvest. Feeling of well-being closer to truth than usual gloom.

**Narrative Snippets**:
- `[ns_pit_ju013]` `[trigger: transit_jupiter_conjunct_natal_sun]` `[factor_trigger: astro_transit_jupiter CONJUNCT natal_sun]` `[role: 主干]` New 12-year cycle. Expand activities. Good for study. Watch overreach. → PIT Ch9 Jupiter☌Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter Conjunct Sun (流年木星合本命太阳)"
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
        l1_anchor="pit_v1.0.0_jupiter_conjunct_sun__流年木星合本命太_001_L1",
    )
    version: str = "1.0.0"
