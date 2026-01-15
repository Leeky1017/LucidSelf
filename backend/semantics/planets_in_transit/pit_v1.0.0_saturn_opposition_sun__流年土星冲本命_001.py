"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.318575
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
    semantic_id="pit_v1.0.0_saturn_opposition_sun__流年土星冲本命_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SaturnOppositionSun流年土星冲本命(SemanticEntry):
    """
    > Others test and challenge you. May face opposition from authorities. Time to see what you've built...
    """
    
    original_text: str = """> Others test and challenge you. May face opposition from authorities. Time to see what you've built. Relationships show where you need work. May feel low vitality. New beginnings through confrontation.

**Narrative Snippets**:
- `[ns_pit_sa017]` `[trigger: transit_saturn_opposition_natal_sun]` `[factor_trigger: astro_transit_saturn OPPOSITION natal_sun]` `[role: 主干]` Others test and challenge. See what you've built. New beginnings through confrontation. → PIT Ch10 Saturn☍Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Saturn Opposition Sun (流年土星冲本命太阳)"
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
        l1_anchor="pit_v1.0.0_saturn_opposition_sun__流年土星冲本命_001_L1",
    )
    version: str = "1.0.0"
