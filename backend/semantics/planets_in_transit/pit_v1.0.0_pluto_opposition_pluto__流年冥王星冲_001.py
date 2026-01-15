"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.239109
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
    semantic_id="pit_v1.0.0_pluto_opposition_pluto__流年冥王星冲_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class PlutoOppositionPluto流年冥王星冲(SemanticEntry):
    """
    > Major generational confrontation with transformation (~82-124 depending on birth year). Face ultim...
    """
    
    original_text: str = """> Major generational confrontation with transformation (~82-124 depending on birth year). Face ultimate power/death themes. Rarely experienced.

**Narrative Snippets**:
- `[ns_pit_pl062]` `[trigger: transit_pluto_opposition_natal_pluto]` `[factor_trigger: astro_transit_pluto OPPOSITION natal_pluto]` `[role: 主干]` Major confrontation with transformation. Face ultimate themes. Rarely experienced. → PIT Ch13 Pluto☍Pluto"""
    normalized_text_zh: str = """"""
    subject: str = "Pluto Opposition Pluto (流年冥王星冲本命冥王星)"
    factor_refs: list = ['transit_pluto', 'cycle_pluto_square', 'state_transformation', 'pattern_power_dynamics']
    
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
        l1_anchor="pit_v1.0.0_pluto_opposition_pluto__流年冥王星冲_001_L1",
    )
    version: str = "1.0.0"
