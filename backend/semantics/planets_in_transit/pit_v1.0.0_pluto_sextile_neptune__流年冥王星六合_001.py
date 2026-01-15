"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.238922
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
    semantic_id="pit_v1.0.0_pluto_sextile_neptune__流年冥王星六合_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class PlutoSextileNeptune流年冥王星六合(SemanticEntry):
    """
    > Constructive spiritual transformation. Good for depth work, healing through compassion. Creative r...
    """
    
    original_text: str = """> Constructive spiritual transformation. Good for depth work, healing through compassion. Creative regeneration.

**Narrative Snippets**:
- `[ns_pit_pl054]` `[trigger: transit_pluto_sextile_natal_neptune]` `[factor_trigger: astro_transit_pluto SEXTILE natal_neptune]` `[role: 主干]` Constructive spiritual transformation. Healing through compassion. → PIT Ch13 Pluto⚹Neptune"""
    normalized_text_zh: str = """"""
    subject: str = "Pluto Sextile Neptune (流年冥王星六合本命海王星)"
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
        l1_anchor="pit_v1.0.0_pluto_sextile_neptune__流年冥王星六合_001_L1",
    )
    version: str = "1.0.0"
