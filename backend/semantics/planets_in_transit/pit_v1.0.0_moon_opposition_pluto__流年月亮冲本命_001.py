"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301629
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
    semantic_id="pit_v1.0.0_moon_opposition_pluto__流年月亮冲本命_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonOppositionPluto流年月亮冲本命(SemanticEntry):
    """
    > Confrontations reveal power dynamics. Others may try to control emotionally. Deep feelings surface...
    """
    
    original_text: str = """> Confrontations reveal power dynamics. Others may try to control emotionally. Deep feelings surface through relationships. Time to see your own manipulation patterns. Transformation through crisis.

**Narrative Snippets**:
- `[ns_pit_m075]` `[trigger: transit_moon_opposition_natal_pluto]` `[factor_trigger: astro_transit_moon OPPOSITION natal_pluto]` `[role: 主干]` Confrontations reveal power dynamics. See your manipulation patterns. Transformation through crisis. → PIT Ch5 Moon☍Pluto"""
    normalized_text_zh: str = """"""
    subject: str = "Moon Opposition Pluto (流年月亮冲本命冥王星)"
    factor_refs: list = ['aspect_moon_sun', 'aspect_moon_moon', 'aspect_moon_mercury', 'aspect_moon_venus', 'aspect_moon_mars', 'aspect_moon_jupiter', 'aspect_moon_saturn', 'aspect_moon_uranus', 'aspect_moon_neptune', 'aspect_moon_pluto']
    
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
        l1_anchor="pit_v1.0.0_moon_opposition_pluto__流年月亮冲本命_001_L1",
    )
    version: str = "1.0.0"
