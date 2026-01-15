"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.207914
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
    semantic_id="pit_v1.0.0_uranus_conjunct_jupiter__流年天王星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusConjunctJupiter流年天王星(SemanticEntry):
    """
    > Sudden expansion and breakthroughs. Exciting opportunities. Freedom and growth combine. May be res...
    """
    
    original_text: str = """> Sudden expansion and breakthroughs. Exciting opportunities. Freedom and growth combine. May be restless for change. Innovation favored.

**Narrative Snippets**:
- `[ns_pit_ur038]` `[trigger: transit_uranus_conjunct_natal_jupiter]` `[factor_trigger: astro_transit_uranus CONJUNCT natal_jupiter]` `[role: 主干]` Sudden expansion. Exciting opportunities. Freedom and growth. → PIT Ch11 Uranus☌Jupiter"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus Conjunct Jupiter (流年天王星合本命木星)"
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
        l1_anchor="pit_v1.0.0_uranus_conjunct_jupiter__流年天王星_001_L1",
    )
    version: str = "1.0.0"
