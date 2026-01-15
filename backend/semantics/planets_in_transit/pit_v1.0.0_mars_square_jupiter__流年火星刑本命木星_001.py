"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.288438
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
    semantic_id="pit_v1.0.0_mars_square_jupiter__流年火星刑本命木星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MarsSquareJupiter流年火星刑本命木星(SemanticEntry):
    """
    > May overreach. Actions exceed realistic limits. Check overconfidence. Legal or ethical issues poss...
    """
    
    original_text: str = """> May overreach. Actions exceed realistic limits. Check overconfidence. Legal or ethical issues possible.

**Narrative Snippets**:
- `[ns_pit_ma040]` `[trigger: transit_mars_square_natal_jupiter]` `[factor_trigger: astro_transit_mars SQUARE natal_jupiter]` `[role: 主干]` May overreach. Check overconfidence. → PIT Ch8 Mars□Jupiter"""
    normalized_text_zh: str = """"""
    subject: str = "Mars Square Jupiter (流年火星刑本命木星)"
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
        l1_anchor="pit_v1.0.0_mars_square_jupiter__流年火星刑本命木星_001_L1",
    )
    version: str = "1.0.0"
