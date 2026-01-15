"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.288676
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
    semantic_id="pit_v1.0.0_mars_opposition_pluto__流年火星冲本命_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MarsOppositionPluto流年火星冲本命(SemanticEntry):
    """
    > Others confront your power. Power struggles. May feel controlled. Transform through confrontation ...
    """
    
    original_text: str = """> Others confront your power. Power struggles. May feel controlled. Transform through confrontation with others.

**Narrative Snippets**:
- `[ns_pit_ma062]` `[trigger: transit_mars_opposition_natal_pluto]` `[factor_trigger: astro_transit_mars OPPOSITION natal_pluto]` `[role: 主干]` Power struggles with others. Transform through confrontation. → PIT Ch8 Mars☍Pluto"""
    normalized_text_zh: str = """"""
    subject: str = "Mars Opposition Pluto (流年火星冲本命冥王星)"
    factor_refs: list = ['transit_mars', 'state_energy_surge', 'state_assertive_action', 'state_conflict_potential']
    
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
        l1_anchor="pit_v1.0.0_mars_opposition_pluto__流年火星冲本命_001_L1",
    )
    version: str = "1.0.0"
