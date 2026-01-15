"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.272962
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
    semantic_id="pit_v1.0.0_neptune_sextile_mars__流年海王星六合本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneSextileMars流年海王星六合本(SemanticEntry):
    """
    > Inspired action. Good for creative, spiritual activities. Compassionate action. Intuitive timing.
...
    """
    
    original_text: str = """> Inspired action. Good for creative, spiritual activities. Compassionate action. Intuitive timing.

**Narrative Snippets**:
- `[ns_pit_ne034]` `[trigger: transit_neptune_sextile_natal_mars]` `[factor_trigger: astro_transit_neptune SEXTILE natal_mars]` `[role: 主干]` Inspired action. Good for creative and spiritual activities. → PIT Ch12 Neptune⚹Mars"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune Sextile Mars (流年海王星六合本命火星)"
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
        l1_anchor="pit_v1.0.0_neptune_sextile_mars__流年海王星六合本_001_L1",
    )
    version: str = "1.0.0"
