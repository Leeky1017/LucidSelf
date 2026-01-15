"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.207306
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
    semantic_id="pit_v1.0.0_uranus_square_moon__流年天王星刑本命月亮_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusSquareMoon流年天王星刑本命月亮(SemanticEntry):
    """
    > Emotional tension and sudden upsets. Domestic instability. May feel emotionally restless. Women/fa...
    """
    
    original_text: str = """> Emotional tension and sudden upsets. Domestic instability. May feel emotionally restless. Women/family conflicts. Need constructive outlet for restlessness.

**Narrative Snippets**:
- `[ns_pit_ur020]` `[trigger: transit_uranus_square_natal_moon]` `[factor_trigger: astro_transit_uranus SQUARE natal_moon]` `[role: 主干]` Emotional tension. Domestic instability. Need outlet for restlessness. → PIT Ch11 Uranus□Moon"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus Square Moon (流年天王星刑本命月亮)"
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
        l1_anchor="pit_v1.0.0_uranus_square_moon__流年天王星刑本命月亮_001_L1",
    )
    version: str = "1.0.0"
