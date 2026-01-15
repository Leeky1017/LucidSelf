"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.288321
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
    semantic_id="pit_v1.0.0_mars_conjunct_mars__流年火星合本命火星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MarsConjunctMars流年火星合本命火星(SemanticEntry):
    """
    > Mars Return—new two-year energy cycle begins. Initiating energy peak. Good for starting projects. ...
    """
    
    original_text: str = """> Mars Return—new two-year energy cycle begins. Initiating energy peak. Good for starting projects. Assert yourself strongly.

**Narrative Snippets**:
- `[ns_pit_ma033]` `[trigger: transit_mars_conjunct_natal_mars]` `[factor_trigger: astro_transit_mars CONJUNCT natal_mars]` `[role: 主干]` Mars Return—new energy cycle. Good for starting projects. → PIT Ch8 Mars☌Mars"""
    normalized_text_zh: str = """"""
    subject: str = "Mars Conjunct Mars (流年火星合本命火星)"
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
        l1_anchor="pit_v1.0.0_mars_conjunct_mars__流年火星合本命火星_001_L1",
    )
    version: str = "1.0.0"
