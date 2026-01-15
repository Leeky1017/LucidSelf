"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.288549
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
    semantic_id="pit_v1.0.0_mars_opposition_uranus__流年火星冲本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MarsOppositionUranus流年火星冲本(SemanticEntry):
    """
    > Others disrupt your actions. Sudden conflicts. Need for freedom clashes. Accidents possible. Chann...
    """
    
    original_text: str = """> Others disrupt your actions. Sudden conflicts. Need for freedom clashes. Accidents possible. Channel rebellious energy.

**Narrative Snippets**:
- `[ns_pit_ma052]` `[trigger: transit_mars_opposition_natal_uranus]` `[factor_trigger: astro_transit_mars OPPOSITION natal_uranus]` `[role: 主干]` Others disrupt. Sudden conflicts. Channel rebellious energy. → PIT Ch8 Mars☍Uranus"""
    normalized_text_zh: str = """"""
    subject: str = "Mars Opposition Uranus (流年火星冲本命天王星)"
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
        l1_anchor="pit_v1.0.0_mars_opposition_uranus__流年火星冲本_001_L1",
    )
    version: str = "1.0.0"
