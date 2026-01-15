"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.223754
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
    semantic_id="pit_v1.0.0_sun_in_the_fourth_house__太阳过境第_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunInTheFourthHouse太阳过境第(SemanticEntry):
    """
    **Source Text** (Lines 1744-1766):
> At this time of year you focus your concerns upon your most int...
    """
    
    original_text: str = """**Source Text** (Lines 1744-1766):
> At this time of year you focus your concerns upon your most intimate personal life and the people who affect it most, your family and parents. You will want to be in familiar surroundings now and feel that you have some kind of center or place where you can build a solid base for your activities. For most people this means a home.
> 
> Although you should continue to live up to the demands of the outer world, because your personal life is interdependent with it, you should focus most of your attention inward. Not only inward to your personal life, but also inward in a psychological sense. Even more than the Sun's transit through the first house, this is a time of subjective consciousness, of feeling exactly where you are with respect to the world and getting in touch with your own deepest levels. If necessary, go off by yourself and spend time in contemplation or meditation.
> 
> Events that occurred in the past may come back to you now through memories and through consequences of those events that continue to affect you now. It is often wise to find out what effects your past, your upbringing and the experience of your family have had upon you. You may want to call in another person, perhaps even a professional counselor, to help you examine the role of the past in your present life. You may find that the past has generated behavior patterns that are completely inappropriate for your life now.

**Key Term Analysis**:
- **Fourth house**: literal = IC house / symbolic = roots, home, family, inner foundation / context = psychological base
- **Intimate personal life**: literal = private sphere / symbolic = emotional foundation / context = family, home base
- **Subjective consciousness**: literal = inner awareness / symbolic = deepest self-connection / context = more than 1H transit
- **Contemplation/meditation**: literal = quiet reflection / symbolic = inner journey / context = accessing deep levels
- **Past effects**: literal = historical influences / symbolic = psychological conditioning / context = family patterns still active

**English Paraphrase (Primary Language)**:
The Sun's fourth house transit focuses attention on your most intimate personal life—family, parents, and home. You seek familiar surroundings and a solid base for activities. While outer world demands continue, your primary focus should turn inward—not just to personal life but psychologically to your deepest levels. Hand emphasizes this as even more subjectively focused than the first house transit—a time to feel your exact position in the world and connect with innermost self. Contemplation or meditation may be needed. Past events resurface through memories and ongoing consequences. This is optimal timing to examine how your past, upbringing, and family experience have shaped current patterns. Professional counseling may help examine the past's role in present life. You may discover behavior patterns from the past that are now completely inappropriate.

**Complete Chinese Interpretation (Secondary Language)**:
太阳过境第四宫将注意力聚焦于你最私密的个人生活——家庭、父母和家。你寻求熟悉的环境和稳固的活动基础。虽然外部世界的要求持续存在，但你的主要焦点应该转向内在——不仅是个人生活，而是心理上转向最深层次。汉德强调这比第一宫行运更具主观聚焦性——是感受你在世界中确切位置并连接最内在自我的时期。可能需要沉思或冥想。过去事件通过记忆和持续后果重新浮现。这是审视过去、成长经历和家庭经验如何塑造当前模式的最佳时机。专业咨询可能有助于检验过去在当前生活中的角色。你可能发现来自过去的行为模式现在已完全不适用。

**Core Points**:
- Fourth house = intimate personal life, family, parents, home
- Seek familiar surroundings and solid base for activities
- Focus inward: personal life AND astro_psychological deepest levels
- More subjectively focused than 1st house transit
- Time to feel exact position in world
- Connect with innermost self through contemplation/meditation
- Past events resurface through memories and consequences
- Examine how past, upbringing, family shaped current patterns
- Professional counseling may assist past examination
- May discover inappropriate behavior patterns from past

**Narrative Snippets**:
- `[ns_pit_017]` `[trigger: sun_transit_house_4]` `[factor_trigger: astro_transit_sun AND astro_house_4]` `[role: 主干]` At this time you focus upon your most intimate personal life—family, parents, and the need for a solid base. → PIT Ch4 Sun-4H
- `[ns_pit_018]` `[trigger: sun_transit_house_4]` `[factor_trigger: astro_transit_sun AND astro_house_4]` `[role: 主干依赖]` Even more than the first house transit, this is a time of subjective consciousness—getting in touch with your deepest levels. → PIT Ch4 Sun-4H
- `[ns_pit_019]` `[trigger: sun_transit_house_4]` `[factor_trigger: astro_transit_sun AND astro_house_4]` `[role: 条件分支]` Events from the past may come back through memories and through consequences that continue to affect you now. → PIT Ch4 Sun-4H
- `[ns_pit_020]` `[trigger: sun_transit_house_4]` `[factor_trigger: astro_transit_sun AND astro_house_4]` `[role: 总结]` You may find that the past has generated behavior patterns that are completely inappropriate for your life now. → PIT Ch4 Sun-4H

**Textual Criticism**: N/A - Single authoritative source."""
    normalized_text_zh: str = """"""
    subject: str = "Sun in the Fourth House (太阳过境第四宫)"
    factor_refs: list = ['house_4', 'state_subjective_consciousness', 'psych_past_patterns']
    
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
        l1_anchor="pit_v1.0.0_sun_in_the_fourth_house__太阳过境第_001_L1",
    )
    version: str = "1.0.0"
