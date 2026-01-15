"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.280846
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
    semantic_id="pit_v1.0.0_mercury_conjunct_sun__流年水星合本命太_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MercuryConjunctSun流年水星合本命太(SemanticEntry):
    """
    > Must express yourself and thinking in every possible way. Mind clearer, more alert and mentally sh...
    """
    
    original_text: str = """> Must express yourself and thinking in every possible way. Mind clearer, more alert and mentally sharp. Very conscious of your purpose. Be careful not to put so much energy into communicating that you don't receive. Express with vigor, make impression. Day crowded with communications. May feel restless, eager to travel. Learn more quickly than at almost any other time.

**Narrative Snippets**:
- `[ns_pit_me015]` `[trigger: transit_mercury_conjunct_natal_sun]` `[factor_trigger: astro_transit_mercury CONJUNCT natal_sun]` `[role: 主干]` Mind clearer, more alert. Express with vigor. Day crowded with communications. → PIT Ch6 Mercury☌Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury Conjunct Sun (流年水星合本命太阳)"
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
        l1_anchor="pit_v1.0.0_mercury_conjunct_sun__流年水星合本命太_001_L1",
    )
    version: str = "1.0.0"
