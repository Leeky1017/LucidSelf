"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224647
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
    semantic_id="pit_v1.0.0_sun_square_pluto__流年太阳刑本命冥王星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunSquarePluto流年太阳刑本命冥王星(SemanticEntry):
    """
    > Power struggles likely. Confrontations with those who challenge your position or authority. Compul...
    """
    
    original_text: str = """> Power struggles likely. Confrontations with those who challenge your position or authority. Compulsive or obsessive tendencies strong. Be careful of manipulation—by you or of you. Deep psychological issues may surface. Don't force issues—could backfire. Transformation through crisis. Examine your use of power.

**Narrative Snippets**:
- `[ns_pit_119]` `[trigger: transit_sun_square_natal_pluto]` `[factor_trigger: astro_transit_sun SQUARE natal_pluto]` `[role: 主干]` Power struggles likely—confrontations. Compulsive tendencies. Don't force issues. Examine your use of power. → PIT Ch4 Sun□Pluto"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Square Pluto (流年太阳刑本命冥王星)"
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
        l1_anchor="pit_v1.0.0_sun_square_pluto__流年太阳刑本命冥王星_001_L1",
    )
    version: str = "1.0.0"
