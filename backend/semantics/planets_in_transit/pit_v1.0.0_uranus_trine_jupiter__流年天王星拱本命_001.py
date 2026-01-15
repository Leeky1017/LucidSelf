"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.208007
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
    semantic_id="pit_v1.0.0_uranus_trine_jupiter__流年天王星拱本命_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusTrineJupiter流年天王星拱本命(SemanticEntry):
    """
    > Excellent for freedom and expansion. Breakthroughs come easily. Progressive opportunities. Excitin...
    """
    
    original_text: str = """> Excellent for freedom and expansion. Breakthroughs come easily. Progressive opportunities. Exciting growth.

**Narrative Snippets**:
- `[ns_pit_ur041]` `[trigger: transit_uranus_trine_natal_jupiter]` `[factor_trigger: astro_transit_uranus TRINE natal_jupiter]` `[role: 主干]` Excellent for freedom and expansion. Breakthroughs easy. → PIT Ch11 Uranus△Jupiter"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus Trine Jupiter (流年天王星拱本命木星)"
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
        l1_anchor="pit_v1.0.0_uranus_trine_jupiter__流年天王星拱本命_001_L1",
    )
    version: str = "1.0.0"
