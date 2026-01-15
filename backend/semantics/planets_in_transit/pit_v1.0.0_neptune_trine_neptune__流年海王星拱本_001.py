"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.273195
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
    semantic_id="pit_v1.0.0_neptune_trine_neptune__流年海王星拱本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneTrineNeptune流年海王星拱本(SemanticEntry):
    """
    > Spiritual harmony (~55-56 and ~110 years). Dreams and ideals flow easily. Compassion and creativit...
    """
    
    original_text: str = """> Spiritual harmony (~55-56 and ~110 years). Dreams and ideals flow easily. Compassion and creativity enhanced.

**Narrative Snippets**:
- `[ns_pit_ne056]` `[trigger: transit_neptune_trine_natal_neptune]` `[factor_trigger: astro_transit_neptune TRINE natal_neptune]` `[role: 主干]` Spiritual harmony (~55-56). Dreams and ideals flow easily. → PIT Ch12 Neptune△Neptune"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune Trine Neptune (流年海王星拱本命海王星)"
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
        l1_anchor="pit_v1.0.0_neptune_trine_neptune__流年海王星拱本_001_L1",
    )
    version: str = "1.0.0"
