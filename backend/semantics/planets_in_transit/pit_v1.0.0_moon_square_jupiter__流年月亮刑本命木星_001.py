"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301416
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
    semantic_id="pit_v1.0.0_moon_square_jupiter__流年月亮刑本命木星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonSquareJupiter流年月亮刑本命木星(SemanticEntry):
    """
    > Emotional excess possible. May overreact, overindulge, or expect too much. Restlessness and dissat...
    """
    
    original_text: str = """> Emotional excess possible. May overreact, overindulge, or expect too much. Restlessness and dissatisfaction. Need for more than usual. Check unrealistic expectations. Don't overcommit.

**Narrative Snippets**:
- `[ns_pit_m053]` `[trigger: transit_moon_square_natal_jupiter]` `[factor_trigger: astro_transit_moon SQUARE natal_jupiter]` `[role: 主干]` Emotional excess possible—may overreact or expect too much. Check unrealistic expectations. → PIT Ch5 Moon□Jupiter"""
    normalized_text_zh: str = """"""
    subject: str = "Moon Square Jupiter (流年月亮刑本命木星)"
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
        l1_anchor="pit_v1.0.0_moon_square_jupiter__流年月亮刑本命木星_001_L1",
    )
    version: str = "1.0.0"
