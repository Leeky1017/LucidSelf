"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.259185
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
    semantic_id="pit_v1.0.0_venus_opposition_moon__流年金星冲本命_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusOppositionMoon流年金星冲本命(SemanticEntry):
    """
    > Emotional needs in relationships become clear. May see mismatch between what you want and what you...
    """
    
    original_text: str = """> Emotional needs in relationships become clear. May see mismatch between what you want and what you have. Good for understanding relationship dynamics. Others' needs more apparent.

**Narrative Snippets**:
- `[ns_pit_ve022]` `[trigger: transit_venus_opposition_natal_moon]` `[factor_trigger: astro_transit_venus OPPOSITION natal_moon]` `[role: 主干]` Emotional needs clear. See relationship dynamics. Others' needs apparent. → PIT Ch7 Venus☍Moon"""
    normalized_text_zh: str = """"""
    subject: str = "Venus Opposition Moon (流年金星冲本命月亮)"
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
        l1_anchor="pit_v1.0.0_venus_opposition_moon__流年金星冲本命_001_L1",
    )
    version: str = "1.0.0"
