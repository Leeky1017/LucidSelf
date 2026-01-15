"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.281138
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
    semantic_id="pit_v1.0.0_mercury_trine_jupiter__流年水星拱本命_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MercuryTrineJupiter流年水星拱本命(SemanticEntry):
    """
    > Excellent for learning and teaching. Optimistic outlook. Good for travel, legal, publishing. Commu...
    """
    
    original_text: str = """> Excellent for learning and teaching. Optimistic outlook. Good for travel, legal, publishing. Communications bring opportunities.

**Narrative Snippets**:
- `[ns_pit_me043]` `[trigger: transit_mercury_trine_natal_jupiter]` `[factor_trigger: astro_transit_mercury TRINE natal_jupiter]` `[role: 主干]` Excellent for learning. Optimistic. Communications bring opportunities. → PIT Ch6 Mercury△Jupiter"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury Trine Jupiter (流年水星拱本命木星)"
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
        l1_anchor="pit_v1.0.0_mercury_trine_jupiter__流年水星拱本命_001_L1",
    )
    version: str = "1.0.0"
