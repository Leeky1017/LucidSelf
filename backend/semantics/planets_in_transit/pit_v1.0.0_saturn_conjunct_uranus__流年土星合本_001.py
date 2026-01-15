"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.319007
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
    semantic_id="pit_v1.0.0_saturn_conjunct_uranus__流年土星合本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SaturnConjunctUranus流年土星合本(SemanticEntry):
    """
    > Structure meets change. May feel torn between security and freedom. Old structures challenged. Can...
    """
    
    original_text: str = """> Structure meets change. May feel torn between security and freedom. Old structures challenged. Can build something innovative if balance found.

**Narrative Snippets**:
- `[ns_pit_sa048]` `[trigger: transit_saturn_conjunct_natal_uranus]` `[factor_trigger: astro_transit_saturn CONJUNCT natal_uranus]` `[role: 主干]` Structure meets change. Balance security and freedom. → PIT Ch10 Saturn☌Uranus"""
    normalized_text_zh: str = """"""
    subject: str = "Saturn Conjunct Uranus (流年土星合本命天王星)"
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
        l1_anchor="pit_v1.0.0_saturn_conjunct_uranus__流年土星合本_001_L1",
    )
    version: str = "1.0.0"
