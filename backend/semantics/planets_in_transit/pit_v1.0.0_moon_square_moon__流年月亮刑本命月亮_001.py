"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301191
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
    semantic_id="pit_v1.0.0_moon_square_moon__流年月亮刑本命月亮_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonSquareMoon流年月亮刑本命月亮(SemanticEntry):
    """
    > Emotional tension and challenge. Habitual emotional patterns are tested. May feel irritable or at ...
    """
    
    original_text: str = """> Emotional tension and challenge. Habitual emotional patterns are tested. May feel irritable or at odds with yourself. Old habits vs new needs. Women or family members may be challenging.

**Narrative Snippets**:
- `[ns_pit_m033]` `[trigger: transit_moon_square_natal_moon]` `[factor_trigger: astro_transit_moon SQUARE natal_moon]` `[role: 主干]` Emotional tension—habitual patterns tested. May feel irritable. Old habits vs new needs. → PIT Ch5 Moon□Moon"""
    normalized_text_zh: str = """"""
    subject: str = "Moon Square Moon (流年月亮刑本命月亮)"
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
        l1_anchor="pit_v1.0.0_moon_square_moon__流年月亮刑本命月亮_001_L1",
    )
    version: str = "1.0.0"
