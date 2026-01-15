"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.272807
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
    semantic_id="pit_v1.0.0_neptune_trine_moon__流年海王星拱本命月亮_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneTrineMoon流年海王星拱本命月亮(SemanticEntry):
    """
    > Beautiful emotional and intuitive flow. Compassion natural. Good for family, creativity, spiritual...
    """
    
    original_text: str = """> Beautiful emotional and intuitive flow. Compassion natural. Good for family, creativity, spiritual matters. Psychic abilities enhanced.

**Narrative Snippets**:
- `[ns_pit_ne021]` `[trigger: transit_neptune_trine_natal_moon]` `[factor_trigger: astro_transit_neptune TRINE natal_moon]` `[role: 主干]` Beautiful emotional flow. Compassion natural. Psychic enhanced. → PIT Ch12 Neptune△Moon"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune Trine Moon (流年海王星拱本命月亮)"
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
        l1_anchor="pit_v1.0.0_neptune_trine_moon__流年海王星拱本命月亮_001_L1",
    )
    version: str = "1.0.0"
