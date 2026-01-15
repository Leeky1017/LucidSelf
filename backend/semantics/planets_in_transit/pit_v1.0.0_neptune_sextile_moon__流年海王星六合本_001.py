"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.272787
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
    semantic_id="pit_v1.0.0_neptune_sextile_moon__流年海王星六合本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneSextileMoon流年海王星六合本(SemanticEntry):
    """
    > Pleasant emotional sensitivity. Intuition and compassion flow. Good for creative and domestic matt...
    """
    
    original_text: str = """> Pleasant emotional sensitivity. Intuition and compassion flow. Good for creative and domestic matters. Psychic awareness enhanced.

**Narrative Snippets**:
- `[ns_pit_ne019]` `[trigger: transit_neptune_sextile_natal_moon]` `[factor_trigger: astro_transit_neptune SEXTILE natal_moon]` `[role: 主干]` Pleasant emotional sensitivity. Intuition flows. Good for creative/domestic. → PIT Ch12 Neptune⚹Moon"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune Sextile Moon (流年海王星六合本命月亮)"
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
        l1_anchor="pit_v1.0.0_neptune_sextile_moon__流年海王星六合本_001_L1",
    )
    version: str = "1.0.0"
