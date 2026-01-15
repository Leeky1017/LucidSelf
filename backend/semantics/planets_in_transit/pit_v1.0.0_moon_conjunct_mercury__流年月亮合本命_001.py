"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301221
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
    semantic_id="pit_v1.0.0_moon_conjunct_mercury__流年月亮合本命_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonConjunctMercury流年月亮合本命(SemanticEntry):
    """
    > Mind and emotions unite. Communications have emotional depth. Good for expressing feelings verball...
    """
    
    original_text: str = """> Mind and emotions unite. Communications have emotional depth. Good for expressing feelings verbally. May be more subjective in thinking. Good for discussions about personal matters, writing, learning.

**Narrative Snippets**:
- `[ns_pit_m036]` `[trigger: transit_moon_conjunct_natal_mercury]` `[factor_trigger: astro_transit_moon CONJUNCT natal_mercury]` `[role: 主干]` Mind and emotions unite—communications have emotional depth. Good for expressing feelings verbally. → PIT Ch5 Moon☌Mercury"""
    normalized_text_zh: str = """"""
    subject: str = "Moon Conjunct Mercury (流年月亮合本命水星)"
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
        l1_anchor="pit_v1.0.0_moon_conjunct_mercury__流年月亮合本命_001_L1",
    )
    version: str = "1.0.0"
