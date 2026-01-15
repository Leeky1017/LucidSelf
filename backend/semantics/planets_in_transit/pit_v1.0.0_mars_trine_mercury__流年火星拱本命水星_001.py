"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.288255
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
    semantic_id="pit_v1.0.0_mars_trine_mercury__流年火星拱本命水星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MarsTrineMercury流年火星拱本命水星(SemanticEntry):
    """
    > Excellent for decisive thinking and communication. Good for advocacy, negotiations. Mental energy ...
    """
    
    original_text: str = """> Excellent for decisive thinking and communication. Good for advocacy, negotiations. Mental energy for action.

**Narrative Snippets**:
- `[ns_pit_ma026]` `[trigger: transit_mars_trine_natal_mercury]` `[factor_trigger: astro_transit_mars TRINE natal_mercury]` `[role: 主干]` Excellent for decisive thinking. Good for advocacy and negotiations. → PIT Ch8 Mars△Mercury"""
    normalized_text_zh: str = """"""
    subject: str = "Mars Trine Mercury (流年火星拱本命水星)"
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
        l1_anchor="pit_v1.0.0_mars_trine_mercury__流年火星拱本命水星_001_L1",
    )
    version: str = "1.0.0"
