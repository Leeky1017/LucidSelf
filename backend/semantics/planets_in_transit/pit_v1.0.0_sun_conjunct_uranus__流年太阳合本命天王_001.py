"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224534
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
    semantic_id="pit_v1.0.0_sun_conjunct_uranus__流年太阳合本命天王_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunConjunctUranus流年太阳合本命天王(SemanticEntry):
    """
    **Source Text** (estimated):
> Day of surprises and unexpected events. Strong urge for freedom and i...
    """
    
    original_text: str = """**Source Text** (estimated):
> Day of surprises and unexpected events. Strong urge for freedom and independence. May feel restless and want to break out of routine. New ideas and insights come suddenly. Good day for original and creative thinking. May clash with those who try to restrict you. Electrical energy high—be careful with machinery. Open to change but don't act rashly.

**English Paraphrase**: Surprises and unexpected events. Strong urge for freedom. Restless, want to break routine. New ideas come suddenly. Good for original thinking. May clash with restrictors. High electrical energy. Open to change but don't act rashly.

**Complete Chinese Interpretation**: 惊喜和意外事件。强烈渴望自由。不安分，想打破常规。新想法突然出现。适合原创思维。可能与限制者冲突。高电能量。对改变开放但不要鲁莽行动。

**Narrative Snippets**:
- `[ns_pit_107]` `[trigger: transit_sun_conjunct_natal_uranus]` `[factor_trigger: astro_transit_sun CONJUNCT natal_uranus]` `[role: 主干]` Day of surprises—strong urge for freedom. New ideas come suddenly. Good for original thinking. → PIT Ch4 Sun☌Uranus"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Conjunct Uranus (流年太阳合本命天王星)"
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
        l1_anchor="pit_v1.0.0_sun_conjunct_uranus__流年太阳合本命天王_001_L1",
    )
    version: str = "1.0.0"
