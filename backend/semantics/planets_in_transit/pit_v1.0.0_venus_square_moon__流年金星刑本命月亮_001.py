"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.259143
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
    semantic_id="pit_v1.0.0_venus_square_moon__流年金星刑本命月亮_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusSquareMoon流年金星刑本命月亮(SemanticEntry):
    """
    > Not difficult, creates amorous mood. Some problems: possessiveness may suffocate partner. Recogniz...
    """
    
    original_text: str = """> Not difficult, creates amorous mood. Some problems: possessiveness may suffocate partner. Recognize relationship needs room to breathe. Possible conflicts with women or mother. Protective love can be positive if not smothering. Possible glandular disturbances.

**Narrative Snippets**:
- `[ns_pit_ve020]` `[trigger: transit_venus_square_natal_moon]` `[factor_trigger: astro_transit_venus SQUARE natal_moon]` `[role: 主干]` Amorous mood but watch possessiveness. Don't smother. → PIT Ch7 Venus□Moon"""
    normalized_text_zh: str = """"""
    subject: str = "Venus Square Moon (流年金星刑本命月亮)"
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
        l1_anchor="pit_v1.0.0_venus_square_moon__流年金星刑本命月亮_001_L1",
    )
    version: str = "1.0.0"
