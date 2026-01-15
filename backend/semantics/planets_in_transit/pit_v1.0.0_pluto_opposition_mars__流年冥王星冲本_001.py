"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.238552
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
    semantic_id="pit_v1.0.0_pluto_opposition_mars__流年冥王星冲本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class PlutoOppositionMars流年冥王星冲本(SemanticEntry):
    """
    > Others confront your power. Power struggles. May feel controlled. Transform through confrontation ...
    """
    
    original_text: str = """> Others confront your power. Power struggles. May feel controlled. Transform through confrontation with others' actions.

**Narrative Snippets**:
- `[ns_pit_pl037]` `[trigger: transit_pluto_opposition_natal_mars]` `[factor_trigger: astro_transit_pluto OPPOSITION natal_mars]` `[role: 主干]` Others confront power. Power struggles. → PIT Ch13 Pluto☍Mars"""
    normalized_text_zh: str = """"""
    subject: str = "Pluto Opposition Mars (流年冥王星冲本命火星)"
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
        l1_anchor="pit_v1.0.0_pluto_opposition_mars__流年冥王星冲本_001_L1",
    )
    version: str = "1.0.0"
