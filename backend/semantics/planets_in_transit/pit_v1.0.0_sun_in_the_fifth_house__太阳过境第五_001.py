"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.223781
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
    semantic_id="pit_v1.0.0_sun_in_the_fifth_house__太阳过境第五_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunInTheFifthHouse太阳过境第五(SemanticEntry):
    """
    **Source Text** (Lines 1767-1793):
> According to tradition, the Sun is happiest in the fifth house....
    """
    
    original_text: str = """**Source Text** (Lines 1767-1793):
> According to tradition, the Sun is happiest in the fifth house. With the Sun here, you feel most free to express yourself and to be yourself. Your primary drive is to do what you want and as much as possible to set your own priorities. You are not especially interested in dominating others, although you may be capable of it at this time, but you will vigorously oppose anyone who tries to prevent you from doing what you want to do.
> 
> The fifth house is often described as the house of amusement and recreation. Therefore you have a strong drive to get out and have a good time, and there is no reason why you shouldn't, as long as you make some effort to meet your daily obligations and restrictions. But the free-spirited drive of the fifth-house Sun may not want to do this, which can be a problem.
> 
> You may have great concern with children now, although this does not mean that you will have problems with them. It only means that your emotional involvement is great. If you have children, this is a good time to examine your relationship with them.
> 
> Your attitude toward your relationships is much lighter at this time, almost as if you saw your relationships as a stage upon which you can perform. At any rate, you favor more than usual the relationships that are fun. This same drive may lead you to a new love relationship with the opposite sex.
> 
> But don't get so wrapped up in yourself and your enjoyments that you forget to examine yourself. This is the time to be yourself, but it also is the time to become conscious of who you are.

**Key Term Analysis**:
- **Fifth house**: literal = Leo's natural house / symbolic = creativity, joy, self-expression / context = Sun's home
- **Sun happiest**: literal = dignity by joy / symbolic = natural expression / context = Sun rules 5H naturally
- **Free to express yourself**: literal = uninhibited expression / symbolic = authentic self-manifestation / context = creative freedom
- **Amusement and recreation**: literal = fun activities / symbolic = pleasure principle / context = 5H traditional meaning
- **Children**: literal = offspring / symbolic = creative products / context = 5H rulership
- **Relationships as stage**: literal = theatrical view / symbolic = performance/display mode / context = Leo influence

**English Paraphrase (Primary Language)**:
The Sun transiting the fifth house is traditionally considered the Sun's happiest placement. You feel most free to express yourself and be yourself authentically. Your primary drive is doing what you want and setting your own priorities. While capable of dominating others, that's not your interest—but you'll vigorously oppose anyone preventing your self-expression. The fifth house governs amusement and recreation, creating strong drive for enjoyment (balanced against daily obligations, though the free-spirited Sun here may resist this). Children become emotionally important during this transit—an excellent time to examine parent-child relationships. Your relationship attitude lightens, viewing relationships almost as a performance stage, favoring fun connections. This may lead to new romantic relationships. Hand's warning: don't become so wrapped up in enjoyment that you forget self-examination. This is time to BE yourself AND astro_become CONSCIOUS of who you are.

**Complete Chinese Interpretation (Secondary Language)**:
太阳过境第五宫传统上被认为是太阳最快乐的位置。你感到最自由地表达自己和做真实的自己。你的主要驱动力是做你想做的事和设定自己的优先事项。虽然有能力支配他人，但那不是你的兴趣——但你会强烈反对任何阻止你自我表达的人。第五宫主管娱乐和休闲，创造强烈的享乐驱动（需与日常义务平衡，尽管这里自由奔放的太阳可能会抗拒）。孩子在此行运期间变得情感上重要——审视亲子关系的绝佳时机。你对关系的态度变得轻松，几乎把关系视为表演舞台，偏好有趣的连接。这可能导致新的浪漫关系。汉德的警告：不要过于沉浸在享乐中而忘记自我检视。这是做自己的时候，也是意识到自己是谁的时候。

**Core Points**:
- Fifth house = Sun's happiest placement traditionally
- Feel most free to express and be yourself
- Primary drive: do what you want, set own priorities
- Capable of domination but not interested in it
- Vigorously oppose those preventing self-expression
- Strong drive for amusement and recreation
- May conflict with daily obligations
- Children become emotionally important
- Good time to examine parent-child relationships
- Relationships viewed lighter, almost theatrical
- Favor fun relationships, possible new romance
- Warning: don't neglect self-examination in enjoyment
- Be yourself AND astro_become conscious of who you are

**Narrative Snippets**:
- `[ns_pit_021]` `[trigger: sun_transit_house_5]` `[factor_trigger: astro_transit_sun AND astro_house_5]` `[role: 主干]` Sun is happiest in the fifth house—you feel most free to express yourself and be yourself. → PIT Ch4 Sun-5H
- `[ns_pit_022]` `[trigger: sun_transit_house_5]` `[factor_trigger: astro_transit_sun AND astro_house_5]` `[role: 主干依赖]` You will vigorously oppose anyone who tries to prevent you from doing what you want to do. → PIT Ch4 Sun-5H
- `[ns_pit_023]` `[trigger: sun_transit_house_5]` `[factor_trigger: astro_transit_sun AND astro_house_5]` `[role: 条件分支]` You have strong drive for amusement and recreation, but the free-spirited fifth-house Sun may not want to meet daily obligations. → PIT Ch4 Sun-5H
- `[ns_pit_024]` `[trigger: sun_transit_house_5 AND astro_children]` `[factor_trigger: astro_transit_sun AND astro_house_5 AND astro_children]` `[role: 条件分支]` Great concern with children now—good time to examine your relationship with them. → PIT Ch4 Sun-5H
- `[ns_pit_025]` `[trigger: sun_transit_house_5]` `[factor_trigger: astro_transit_sun AND astro_house_5]` `[role: 总结]` This is the time to be yourself, but also the time to become conscious of who you are. → PIT Ch4 Sun-5H
- `[ns_pit_h5]` `[trigger: house_5]` `[factor_trigger: house_5]` `[role: 主干]` Fifth house represents creativity, children, romance, joy, self-expression—Sun's natural domain of playful vitality. → PIT Foundation
- `[ns_pit_sun]` `[trigger: sun]` `[factor_trigger: sun]` `[role: 主干]` The Sun represents core identity, vitality, ego, will, life-force and conscious self-expression in the chart. → PIT Foundation

**Textual Criticism**: N/A - Single authoritative source."""
    normalized_text_zh: str = """"""
    subject: str = "Sun in the Fifth House (太阳过境第五宫)"
    factor_refs: list = ['house_5', 'state_sun_joy_dignity', 'state_free_expression']
    
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
        l1_anchor="pit_v1.0.0_sun_in_the_fifth_house__太阳过境第五_001_L1",
    )
    version: str = "1.0.0"
