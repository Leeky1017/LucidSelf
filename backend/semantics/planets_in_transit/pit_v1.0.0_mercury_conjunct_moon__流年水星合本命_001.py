"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.280901
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
    semantic_id="pit_v1.0.0_mercury_conjunct_moon__流年水星合本命_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MercuryConjunctMoon流年水星合本命(SemanticEntry):
    """
    > Mind and emotions work together. Can express feelings clearly. Subjective thinking—good for person...
    """
    
    original_text: str = """> Mind and emotions work together. Can express feelings clearly. Subjective thinking—good for personal matters. Conversations emotionally meaningful. Good for discussions with women or about domestic matters.

**Narrative Snippets**:
- `[ns_pit_me020]` `[trigger: transit_mercury_conjunct_natal_moon]` `[factor_trigger: astro_transit_mercury CONJUNCT natal_moon]` `[role: 主干]` Mind and emotions together. Express feelings clearly. Good for domestic discussions. → PIT Ch6 Mercury☌Moon"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury Conjunct Moon (流年水星合本命月亮)"
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
        l1_anchor="pit_v1.0.0_mercury_conjunct_moon__流年水星合本命_001_L1",
    )
    version: str = "1.0.0"
