"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301593
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
    semantic_id="pit_v1.0.0_moon_conjunct_pluto__流年月亮合本命冥王_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonConjunctPluto流年月亮合本命冥王(SemanticEntry):
    """
    > Intense emotional experiences. Deep feelings surface. May feel compulsive or obsessive. Power dyna...
    """
    
    original_text: str = """> Intense emotional experiences. Deep feelings surface. May feel compulsive or obsessive. Power dynamics in relationships become clear. Good for psychological insight. Transformation.

**Narrative Snippets**:
- `[ns_pit_m071]` `[trigger: transit_moon_conjunct_natal_pluto]` `[factor_trigger: astro_transit_moon CONJUNCT natal_pluto]` `[role: 主干]` Intense emotional experiences—deep feelings surface. Good for psychological insight. → PIT Ch5 Moon☌Pluto"""
    normalized_text_zh: str = """"""
    subject: str = "Moon Conjunct Pluto (流年月亮合本命冥王星)"
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
        l1_anchor="pit_v1.0.0_moon_conjunct_pluto__流年月亮合本命冥王_001_L1",
    )
    version: str = "1.0.0"
