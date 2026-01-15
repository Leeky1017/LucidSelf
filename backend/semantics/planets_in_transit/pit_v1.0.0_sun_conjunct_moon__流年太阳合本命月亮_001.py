"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224149
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
    semantic_id="pit_v1.0.0_sun_conjunct_moon__流年太阳合本命月亮_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunConjunctMoon流年太阳合本命月亮(SemanticEntry):
    """
    **Source Text** (Lines 2132-2164):
> This transit brings your personal, domestic and emotional life ...
    """
    
    original_text: str = """**Source Text** (Lines 2132-2164):
> This transit brings your personal, domestic and emotional life to prominence. All the symbolic power of the solar energy is infused into your emotions, bringing them to the surface. You will feel more integrated and at one with yourself than at any other time.
> 
> This transit will bring out all your unconscious attitudes, so take a long look at what comes up today. This is a time of new beginnings in your inner life, a sort of personal "new Moon." Don't pay so much attention to getting ahead; the Moon-ruled areas can actually make or break all your other efforts.

**English Paraphrase**: Personal, domestic, emotional life to prominence. Solar energy infused into emotions, brought to surface. Feel more integrated and at one with yourself. Unconscious attitudes emerge—examine what comes up. New beginnings in inner life, personal "new Moon." Moon-ruled areas make or break other efforts.

**Complete Chinese Interpretation**: 个人、家庭、情感生活变得突出。太阳能量注入情感，浮出表面。感到更整合、与自己合一。无意识态度浮现——检视出现的内容。内在生活的新开始，个人"新月"。月亮主宰的领域决定其他努力的成败。

**Narrative Snippets**:
- `[ns_pit_055]` `[trigger: transit_sun_conjunct_natal_moon]` `[factor_trigger: astro_transit_sun CONJUNCT natal_moon]` `[role: 主干]` Personal, domestic and emotional life to prominence—feel more integrated and at one with yourself. → PIT Ch4 Sun☌Moon
- `[ns_pit_056]` `[trigger: transit_sun_conjunct_natal_moon]` `[factor_trigger: astro_transit_sun CONJUNCT natal_moon]` `[role: 总结]` New beginnings in your inner life, a personal "new Moon." Moon-ruled areas make or break all other efforts. → PIT Ch4 Sun☌Moon"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Conjunct Moon (流年太阳合本命月亮)"
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
        l1_anchor="pit_v1.0.0_sun_conjunct_moon__流年太阳合本命月亮_001_L1",
    )
    version: str = "1.0.0"
