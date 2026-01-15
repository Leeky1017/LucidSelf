"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.318813
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
    semantic_id="pit_v1.0.0_saturn_opposition_jupiter__流年土_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SaturnOppositionJupiter流年土(SemanticEntry):
    """
    > Others may restrict or test your growth. Authority challenges expansion. Good for seeing where you...
    """
    
    original_text: str = """> Others may restrict or test your growth. Authority challenges expansion. Good for seeing where you need more or less structure.

**Narrative Snippets**:
- `[ns_pit_sa042]` `[trigger: transit_saturn_opposition_natal_jupiter]` `[factor_trigger: astro_transit_saturn OPPOSITION natal_jupiter]` `[role: 主干]` Others restrict or test. See structure needs. → PIT Ch10 Saturn☍Jupiter"""
    normalized_text_zh: str = """"""
    subject: str = "Saturn Opposition Jupiter (流年土星冲本命木星)"
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
        l1_anchor="pit_v1.0.0_saturn_opposition_jupiter__流年土_001_L1",
    )
    version: str = "1.0.0"
