"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.223726
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
    semantic_id="pit_v1.0.0_sun_in_the_third_house__太阳过境第三_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunInTheThirdHouse太阳过境第三(SemanticEntry):
    """
    **Source Text** (Lines 1719-1743):
> The Sun in this house turns your attention toward your immediat...
    """
    
    original_text: str = """**Source Text** (Lines 1719-1743):
> The Sun in this house turns your attention toward your immediate surroundings and increases your interaction with friends, neighbors, relatives and business associates — the people you deal with every day. It is a good time to look at how you handle these casual relationships that are so important for your life. Often we develop unfortunate little habits in communicating with these people, which undermine our effectiveness and our ability to communicate with them. In fact, clear communication should be one of the goals of this period. With the Sun in this house there is a temptation to pour out energy and take none in. But try to avoid this. Instead of always being the active agent in communication, be the passive one, too — in other words, listen!
> 
> This is also a time of year when the tempo of your life accelerates. There is more activity, more moving around and even a sense of restlessness that can be assuaged only by getting out and doing something new and different. You might take up the study of a subject that you have never encountered before, or you might take a series of short trips.
> 
> This is an especially good time to tell someone clearly how you feel about some subject. If others have been confused as to what you are doing or thinking in some area, you should be able now to communicate your real thoughts and intentions. Don't leave people in the dark about yourself. Your mental processes should be relatively clear now, and you can use this ability to get through to others.

**Key Term Analysis**:
- **Third house**: literal = house of siblings/communication / symbolic = immediate environment, daily exchanges / context = Mercury's natural house
- **Immediate surroundings**: literal = nearby environment / symbolic = daily life sphere / context = regular contacts
- **Communication habits**: literal = patterns of exchange / symbolic = relational effectiveness / context = often unconscious patterns
- **Listen**: literal = receive information / symbolic = balance active/passive / context = counter Sun's outpouring tendency
- **Tempo accelerates**: literal = faster pace / symbolic = Mercury-like restlessness / context = increased mental activity
- **Short trips**: literal = nearby travel / symbolic = mental stimulation through movement / context = 3H traditional meaning

**English Paraphrase (Primary Language)**:
The Sun's transit through your third house turns attention to your immediate environment—daily interactions with neighbors, relatives, friends, and business associates. This period illuminates how you handle these seemingly casual but vital relationships. Hand notes we often develop unconscious communication habits that undermine our effectiveness. Clear communication should be a primary goal. The Sun's nature creates temptation to pour out energy without receiving—Hand advises balancing this by listening, not just speaking. Life's tempo accelerates during this transit, bringing restlessness that demands new activities or short trips for satisfaction. Mental stimulation through study of unfamiliar subjects also fits this period. This is excellent timing for clear self-expression—communicate your real thoughts and intentions, especially where others have been confused about your position. Mental clarity is enhanced, supporting effective communication.

**Complete Chinese Interpretation (Secondary Language)**:
太阳过境第三宫将注意力转向你的直接环境——与邻居、亲戚、朋友和商业伙伴的日常互动。这个时期照亮你如何处理这些看似随意但至关重要的关系。汉德指出我们常发展出削弱沟通效果的无意识交流习惯。清晰沟通应是主要目标。太阳的本质造成只输出能量不接收的倾向——汉德建议通过倾听来平衡，不只是说话。此行运期间生活节奏加快，带来不安分感，需要新活动或短途旅行来满足。学习不熟悉的科目进行心智刺激也适合这个时期。这是清晰自我表达的绝佳时机——传达你真实的想法和意图，尤其是在他人对你的立场感到困惑的领域。心智清晰度增强，支持有效沟通。

**Core Points**:
- Third house = immediate surroundings, daily contacts, communication
- Focus on casual but important relationships: neighbors, relatives, associates
- Examine communication habits that may undermine effectiveness
- Clear communication is primary goal of this period
- Sun temptation: pour out energy without receiving
- Counter-advice: listen, don't just speak
- Life tempo accelerates, restlessness increases
- New activities, study, or short trips satisfy restlessness
- Excellent time for clear self-expression
- Communicate real thoughts where confusion existed
- Mental clarity enhanced during transit

**Detailed Explanation**:
Hand's treatment of the third house transit emphasizes the dual nature of communication—both transmitting and receiving. The Sun's active, outpouring nature can unbalance communication toward one-way transmission. The advice to listen reflects understanding that third house effectiveness requires receptivity. The accelerated tempo and restlessness reflect Mercury's (natural 3H ruler) qualities being energized by the Sun. Short trips and new studies both satisfy the house's need for mental stimulation and variety.

**Narrative Snippets**:
- `[ns_pit_012]` `[trigger: sun_transit_house_3]` `[factor_trigger: astro_transit_sun AND astro_house_3]` `[role: 主干]` Sun in the third house turns attention toward immediate surroundings and increases interaction with daily contacts. → PIT Ch4 Sun-3H
- `[ns_pit_013]` `[trigger: sun_transit_house_3]` `[factor_trigger: astro_transit_sun AND astro_house_3]` `[role: 主干依赖]` We often develop unfortunate communication habits—clear communication should be one of the goals of this period. → PIT Ch4 Sun-3H
- `[ns_pit_014]` `[trigger: sun_transit_house_3]` `[factor_trigger: astro_transit_sun AND astro_house_3]` `[role: 条件分支]` With Sun here there is temptation to pour out energy and take none in—instead of always being active, listen! → PIT Ch4 Sun-3H
- `[ns_pit_015]` `[trigger: sun_transit_house_3]` `[factor_trigger: astro_transit_sun AND astro_house_3]` `[role: 主干依赖]` The tempo of life accelerates; restlessness can be assuaged only by getting out and doing something new. → PIT Ch4 Sun-3H
- `[ns_pit_016]` `[trigger: sun_transit_house_3]` `[factor_trigger: astro_transit_sun AND astro_house_3]` `[role: 总结]` Your mental processes should be relatively clear now—use this ability to communicate your real thoughts and get through to others. → PIT Ch4 Sun-3H

**Textual Criticism & Variant Analysis**:
- **English**: N/A - Single authoritative source.
- **中文**: 无变体。"""
    normalized_text_zh: str = """"""
    subject: str = "Sun in the Third House (太阳过境第三宫)"
    factor_refs: list = ['house_3', 'concept_immediate_environment', 'psych_communication_patterns', 'state_mental_clarity']
    
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
        l1_anchor="pit_v1.0.0_sun_in_the_third_house__太阳过境第三_001_L1",
    )
    version: str = "1.0.0"
