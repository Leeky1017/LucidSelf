"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224666
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
    semantic_id="pit_v1.0.0_sun_opposition_pluto__流年太阳冲本命冥_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunOppositionPluto流年太阳冲本命冥(SemanticEntry):
    """
    > Critical confrontation with power—yours or others'. What you've been building faces ultimate test....
    """
    
    original_text: str = """> Critical confrontation with power—yours or others'. What you've been building faces ultimate test. Power struggles reach climax. Hidden enemies or agendas may be revealed. Psychological transformation through crisis. Don't manipulate—will backfire. Surrender ego attachment to outcomes. Death/rebirth theme—something must end for new to begin.

**Narrative Snippets**:
- `[ns_pit_121]` `[trigger: transit_sun_opposition_natal_pluto]` `[factor_trigger: astro_transit_sun OPPOSITION natal_pluto]` `[role: 主干]` Critical confrontation with power—ultimate test. Power struggles climax. Transformation through crisis. → PIT Ch4 Sun☍Pluto
- `[ns_pit_122]` `[trigger: transit_sun_opposition_natal_pluto]` `[factor_trigger: astro_transit_sun OPPOSITION natal_pluto]` `[role: 总结]` Don't manipulate—will backfire. Death/rebirth theme—something must end for new to begin. → PIT Ch4 Sun☍Pluto"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Opposition Pluto (流年太阳冲本命冥王星)"
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
        l1_anchor="pit_v1.0.0_sun_opposition_pluto__流年太阳冲本命冥_001_L1",
    )
    version: str = "1.0.0"
