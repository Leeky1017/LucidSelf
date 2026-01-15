"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.238373
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
    semantic_id="pit_v1.0.0_pluto_opposition_mercury__流年冥王_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class PlutoOppositionMercury流年冥王(SemanticEntry):
    """
    > Others challenge your thinking powerfully. Mental power struggles. May feel mentally controlled. T...
    """
    
    original_text: str = """> Others challenge your thinking powerfully. Mental power struggles. May feel mentally controlled. Transform through confrontation of ideas.

**Narrative Snippets**:
- `[ns_pit_pl027]` `[trigger: transit_pluto_opposition_natal_mercury]` `[factor_trigger: astro_transit_pluto OPPOSITION natal_mercury]` `[role: 主干]` Others challenge thinking. Mental power struggles. → PIT Ch13 Pluto☍Mercury"""
    normalized_text_zh: str = """"""
    subject: str = "Pluto Opposition Mercury (流年冥王星冲本命水星)"
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
        l1_anchor="pit_v1.0.0_pluto_opposition_mercury__流年冥王_001_L1",
    )
    version: str = "1.0.0"
