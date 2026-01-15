"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.223921
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
    semantic_id="pit_v1.0.0_sun_in_the_eleventh_house__太阳过_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunInTheEleventhHouse太阳过(SemanticEntry):
    """
    **Source Text** (Lines 1937-1957):
> At this time your attention is turned toward the groups you bel...
    """
    
    original_text: str = """**Source Text** (Lines 1937-1957):
> At this time your attention is turned toward the groups you belong to, their values and ideals and your relationship to those values. Friendships and other relationships are important; you are examining the role they play in your life.
> 
> It is usually best to work and cooperate with other people now. Socialize extensively and study the people you associate with, for they are a reflection of yourself.
> 
> Your idealism is aroused—personal rather than abstract idealism. It is your recognition of what you want your life to be, so follow that ideal.

**English Paraphrase**: Attention to groups, their values and ideals, your relationship to them. Friendships important now. Best to cooperate with others. Associates reflect yourself. Personal idealism aroused—what you want life to be.

**Complete Chinese Interpretation**: 关注群体、它们的价值观和理想、你与它们的关系。友谊现在很重要。最好与他人合作。同伴反映你自己。个人理想主义被唤醒——你想要生活成为什么。

**Narrative Snippets**:
- `[ns_pit_040]` `[trigger: sun_transit_house_11]` `[factor_trigger: astro_transit_sun AND astro_house_11]` `[role: 主干]` Attention turns to groups you belong to, their values and ideals, and your relationship to them. → PIT Ch4 Sun-11H
- `[ns_pit_041]` `[trigger: sun_transit_house_11]` `[factor_trigger: astro_transit_sun AND astro_house_11]` `[role: 总结]` Your personal idealism is aroused—your recognition of what you want your life to be. Follow that ideal. → PIT Ch4 Sun-11H"""
    normalized_text_zh: str = """"""
    subject: str = "Sun in the Eleventh House (太阳过境第十一宫)"
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
        l1_anchor="pit_v1.0.0_sun_in_the_eleventh_house__太阳过_001_L1",
    )
    version: str = "1.0.0"
