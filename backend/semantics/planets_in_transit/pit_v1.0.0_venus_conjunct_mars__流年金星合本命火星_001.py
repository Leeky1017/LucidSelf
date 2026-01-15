"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.259405
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
    semantic_id="pit_v1.0.0_venus_conjunct_mars__流年金星合本命火星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusConjunctMars流年金星合本命火星(SemanticEntry):
    """
    > Sexual energy heightened. Passionate feelings. Good for romance and physical expression. May be im...
    """
    
    original_text: str = """> Sexual energy heightened. Passionate feelings. Good for romance and physical expression. May be impulsive in love.

**Narrative Snippets**:
- `[ns_pit_ve033]` `[trigger: transit_venus_conjunct_natal_mars]` `[factor_trigger: astro_transit_venus CONJUNCT natal_mars]` `[role: 主干]` Sexual energy heightened. Passionate. Good for romance. → PIT Ch7 Venus☌Mars"""
    normalized_text_zh: str = """"""
    subject: str = "Venus Conjunct Mars (流年金星合本命火星)"
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
        l1_anchor="pit_v1.0.0_venus_conjunct_mars__流年金星合本命火星_001_L1",
    )
    version: str = "1.0.0"
