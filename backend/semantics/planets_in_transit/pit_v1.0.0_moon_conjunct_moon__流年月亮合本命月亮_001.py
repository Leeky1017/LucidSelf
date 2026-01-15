"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301173
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
    semantic_id="pit_v1.0.0_moon_conjunct_moon__流年月亮合本命月亮_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonConjunctMoon流年月亮合本命月亮(SemanticEntry):
    """
    > Lunar Return—emotional cycle renewal. A new emotional month begins. Your feelings are heightened a...
    """
    
    original_text: str = """> Lunar Return—emotional cycle renewal. A new emotional month begins. Your feelings are heightened and you're more sensitive than usual. Good time to reflect on emotional patterns. What you feel now sets the tone for the month ahead.

**Narrative Snippets**:
- `[ns_pit_m031]` `[trigger: transit_moon_conjunct_natal_moon]` `[factor_trigger: astro_transit_moon CONJUNCT natal_moon]` `[role: 主干]` Lunar Return—emotional renewal. Feelings heightened. Sets emotional tone for month ahead. → PIT Ch5 Moon☌Moon"""
    normalized_text_zh: str = """"""
    subject: str = "Moon Conjunct Moon (流年月亮合本命月亮)"
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
        l1_anchor="pit_v1.0.0_moon_conjunct_moon__流年月亮合本命月亮_001_L1",
    )
    version: str = "1.0.0"
