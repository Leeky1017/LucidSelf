"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301349
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
    semantic_id="pit_v1.0.0_moon_opposition_mars__流年月亮冲本命火_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonOppositionMars流年月亮冲本命火(SemanticEntry):
    """
    > Confrontational feelings. May clash with others, especially women. Emotions run high. Need to bala...
    """
    
    original_text: str = """> Confrontational feelings. May clash with others, especially women. Emotions run high. Need to balance assertion with sensitivity. Others may seem aggressive. Channel energy carefully.

**Narrative Snippets**:
- `[ns_pit_m050]` `[trigger: transit_moon_opposition_natal_mars]` `[factor_trigger: astro_transit_moon OPPOSITION natal_mars]` `[role: 主干]` Confrontational feelings—may clash with others. Emotions run high. Balance assertion with sensitivity. → PIT Ch5 Moon☍Mars"""
    normalized_text_zh: str = """"""
    subject: str = "Moon Opposition Mars (流年月亮冲本命火星)"
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
        l1_anchor="pit_v1.0.0_moon_opposition_mars__流年月亮冲本命火_001_L1",
    )
    version: str = "1.0.0"
