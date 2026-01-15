"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.318604
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
    semantic_id="pit_v1.0.0_saturn_square_moon__流年土星刑本命月亮_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SaturnSquareMoon流年土星刑本命月亮(SemanticEntry):
    """
    > Emotional frustration and blocks. May feel unappreciated, lonely. Domestic difficulties. Mother or...
    """
    
    original_text: str = """> Emotional frustration and blocks. May feel unappreciated, lonely. Domestic difficulties. Mother or women challenging. Don't dwell on negatives.

**Narrative Snippets**:
- `[ns_pit_sa020]` `[trigger: transit_saturn_square_natal_moon]` `[factor_trigger: astro_transit_saturn SQUARE natal_moon]` `[role: 主干]` Emotional frustration. Domestic difficulties. Don't dwell on negatives. → PIT Ch10 Saturn□Moon"""
    normalized_text_zh: str = """"""
    subject: str = "Saturn Square Moon (流年土星刑本命月亮)"
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
        l1_anchor="pit_v1.0.0_saturn_square_moon__流年土星刑本命月亮_001_L1",
    )
    version: str = "1.0.0"
