"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.272858
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
    semantic_id="pit_v1.0.0_neptune_trine_mercury__流年海王星拱本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneTrineMercury流年海王星拱本(SemanticEntry):
    """
    > Excellent for intuitive, creative, spiritual thinking. Communication flows beautifully. Good for p...
    """
    
    original_text: str = """> Excellent for intuitive, creative, spiritual thinking. Communication flows beautifully. Good for poetry, music, art.

**Narrative Snippets**:
- `[ns_pit_ne026]` `[trigger: transit_neptune_trine_natal_mercury]` `[factor_trigger: astro_transit_neptune TRINE natal_mercury]` `[role: 主干]` Excellent for intuitive/creative thinking. Communication flows. → PIT Ch12 Neptune△Mercury"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune Trine Mercury (流年海王星拱本命水星)"
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
        l1_anchor="pit_v1.0.0_neptune_trine_mercury__流年海王星拱本_001_L1",
    )
    version: str = "1.0.0"
