"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224572
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
    semantic_id="pit_v1.0.0_sun_opposition_uranus__流年太阳冲本命_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunOppositionUranus流年太阳冲本命(SemanticEntry):
    """
    > Day of confrontation with the unexpected. Others may upset your plans. Strong desire for freedom m...
    """
    
    original_text: str = """> Day of confrontation with the unexpected. Others may upset your plans. Strong desire for freedom may conflict with obligations. Relationships strained by need for independence. Don't force changes—they may backfire. Electrical/mechanical problems possible. Stay flexible—rigid positions break under this influence.

**Narrative Snippets**:
- `[ns_pit_111]` `[trigger: transit_sun_opposition_natal_uranus]` `[factor_trigger: astro_transit_sun OPPOSITION natal_uranus]` `[role: 主干]` Confrontation with unexpected—others upset plans. Freedom vs obligations. Stay flexible. → PIT Ch4 Sun☍Uranus"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Opposition Uranus (流年太阳冲本命天王星)"
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
        l1_anchor="pit_v1.0.0_sun_opposition_uranus__流年太阳冲本命_001_L1",
    )
    version: str = "1.0.0"
