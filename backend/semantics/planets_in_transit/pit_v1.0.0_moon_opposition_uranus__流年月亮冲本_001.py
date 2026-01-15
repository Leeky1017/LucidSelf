"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301536
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
    semantic_id="pit_v1.0.0_moon_opposition_uranus__流年月亮冲本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonOppositionUranus流年月亮冲本(SemanticEntry):
    """
    > Others may disrupt your emotional equilibrium. Sudden changes in relationships. Need for freedom m...
    """
    
    original_text: str = """> Others may disrupt your emotional equilibrium. Sudden changes in relationships. Need for freedom may conflict with need for security. Expect the unexpected from others.

**Narrative Snippets**:
- `[ns_pit_m065]` `[trigger: transit_moon_opposition_natal_uranus]` `[factor_trigger: astro_transit_moon OPPOSITION natal_uranus]` `[role: 主干]` Others may disrupt emotional equilibrium. Freedom vs security conflict. → PIT Ch5 Moon☍Uranus"""
    normalized_text_zh: str = """"""
    subject: str = "Moon Opposition Uranus (流年月亮冲本命天王星)"
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
        l1_anchor="pit_v1.0.0_moon_opposition_uranus__流年月亮冲本_001_L1",
    )
    version: str = "1.0.0"
