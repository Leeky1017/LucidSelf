"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.259163
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
    semantic_id="pit_v1.0.0_venus_trine_moon__流年金星拱本命月亮_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusTrineMoon流年金星拱本命月亮(SemanticEntry):
    """
    > Excellent for domestic, personal, emotional life. Relationships work better. Warm and friendly to ...
    """
    
    original_text: str = """> Excellent for domestic, personal, emotional life. Relationships work better. Warm and friendly to everyone. Relations with women especially favorable. Sexual relationships supported by increasing love within relationship. Emotions quiet, good for being alone together quietly.

**Narrative Snippets**:
- `[ns_pit_ve021]` `[trigger: transit_venus_trine_natal_moon]` `[factor_trigger: astro_transit_venus TRINE natal_moon]` `[role: 主干]` Excellent for domestic and emotional life. Sexual relationships supported by love. → PIT Ch7 Venus△Moon"""
    normalized_text_zh: str = """"""
    subject: str = "Venus Trine Moon (流年金星拱本命月亮)"
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
        l1_anchor="pit_v1.0.0_venus_trine_moon__流年金星拱本命月亮_001_L1",
    )
    version: str = "1.0.0"
