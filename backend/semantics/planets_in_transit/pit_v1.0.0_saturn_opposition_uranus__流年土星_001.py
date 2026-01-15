"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.319083
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
    semantic_id="pit_v1.0.0_saturn_opposition_uranus__流年土星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SaturnOppositionUranus流年土星(SemanticEntry):
    """
    > Others bring change that challenges your structure. Sudden disruptions from outside. Balance stabi...
    """
    
    original_text: str = """> Others bring change that challenges your structure. Sudden disruptions from outside. Balance stability and change needed.

**Narrative Snippets**:
- `[ns_pit_sa052]` `[trigger: transit_saturn_opposition_natal_uranus]` `[factor_trigger: astro_transit_saturn OPPOSITION natal_uranus]` `[role: 主干]` Others bring challenging change. Balance stability and change. → PIT Ch10 Saturn☍Uranus"""
    normalized_text_zh: str = """"""
    subject: str = "Saturn Opposition Uranus (流年土星冲本命天王星)"
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
        l1_anchor="pit_v1.0.0_saturn_opposition_uranus__流年土星_001_L1",
    )
    version: str = "1.0.0"
