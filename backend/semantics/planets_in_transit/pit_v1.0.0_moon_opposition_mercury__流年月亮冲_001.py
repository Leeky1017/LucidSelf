"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301258
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
    semantic_id="pit_v1.0.0_moon_opposition_mercury__流年月亮冲_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonOppositionMercury流年月亮冲(SemanticEntry):
    """
    > Mind and emotions at cross-purposes. May say things you don't mean or can't express what you feel....
    """
    
    original_text: str = """> Mind and emotions at cross-purposes. May say things you don't mean or can't express what you feel. Others' words may trigger emotional reactions. Good for seeing how you communicate emotionally.

**Narrative Snippets**:
- `[ns_pit_m040]` `[trigger: transit_moon_opposition_natal_mercury]` `[factor_trigger: astro_transit_moon OPPOSITION natal_mercury]` `[role: 主干]` Mind and emotions at cross-purposes—may say things you don't mean. Others' words trigger reactions. → PIT Ch5 Moon☍Mercury"""
    normalized_text_zh: str = """"""
    subject: str = "Moon Opposition Mercury (流年月亮冲本命水星)"
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
        l1_anchor="pit_v1.0.0_moon_opposition_mercury__流年月亮冲_001_L1",
    )
    version: str = "1.0.0"
