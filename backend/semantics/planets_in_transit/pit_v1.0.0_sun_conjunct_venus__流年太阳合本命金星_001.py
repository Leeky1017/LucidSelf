"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224261
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
    semantic_id="pit_v1.0.0_sun_conjunct_venus__流年太阳合本命金星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunConjunctVenus流年太阳合本命金星(SemanticEntry):
    """
    **Source Text** (Lines 2418-2443):
> Central issue: self-expression through creativity and relations...
    """
    
    original_text: str = """**Source Text** (Lines 2418-2443):
> Central issue: self-expression through creativity and relationships. You want attention from those you love; willing to give love in return. May bring new love interest. Good time to socialize, make new contacts and friendships—you attract people through warmth and friendliness. Venus may bring money as well as friends—favorable for financial activities, but watch extravagance and self-indulgence. Try to surround yourself with beauty and art.

**English Paraphrase**: Self-expression through creativity and relationships. Seek attention from loved ones, give love in return. May bring new love. Good for socializing and new contacts. Attract through warmth. Venus may bring money—favorable for finance but avoid extravagance. Surround yourself with beauty.

**Complete Chinese Interpretation**: 通过创造力和关系的自我表达。寻求所爱之人的关注，回报以爱。可能带来新恋情。适合社交和新接触。通过热情吸引人。金星可能带来金钱——对财务有利但避免挥霍。用美围绕自己。

**Narrative Snippets**:
- `[ns_pit_073]` `[trigger: transit_sun_conjunct_natal_venus]` `[factor_trigger: astro_transit_sun CONJUNCT natal_venus]` `[role: 主干]` Self-expression through creativity and relationships—attract people through warmth, may bring new love interest. → PIT Ch4 Sun☌Venus
- `[ns_pit_074]` `[trigger: transit_sun_conjunct_natal_venus]` `[factor_trigger: astro_transit_sun CONJUNCT natal_venus]` `[role: 条件分支]` Venus may bring money—favorable for finance but avoid extravagance and self-indulgence. → PIT Ch4 Sun☌Venus"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Conjunct Venus (流年太阳合本命金星)"
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
        l1_anchor="pit_v1.0.0_sun_conjunct_venus__流年太阳合本命金星_001_L1",
    )
    version: str = "1.0.0"
