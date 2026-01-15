"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.318776
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
    semantic_id="pit_v1.0.0_saturn_conjunct_jupiter__流年土星合_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SaturnConjunctJupiter流年土星合(SemanticEntry):
    """
    > Expansion meets structure. Can build something lasting. Measured, realistic growth. Consolidate ga...
    """
    
    original_text: str = """> Expansion meets structure. Can build something lasting. Measured, realistic growth. Consolidate gains. Balance optimism with caution.

**Narrative Snippets**:
- `[ns_pit_sa038]` `[trigger: transit_saturn_conjunct_natal_jupiter]` `[factor_trigger: astro_transit_saturn CONJUNCT natal_jupiter]` `[role: 主干]` Expansion meets structure. Build something lasting. → PIT Ch10 Saturn☌Jupiter"""
    normalized_text_zh: str = """"""
    subject: str = "Saturn Conjunct Jupiter (流年土星合本命木星)"
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
        l1_anchor="pit_v1.0.0_saturn_conjunct_jupiter__流年土星合_001_L1",
    )
    version: str = "1.0.0"
