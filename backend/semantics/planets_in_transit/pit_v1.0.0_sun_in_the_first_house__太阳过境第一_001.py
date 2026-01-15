"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.223633
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
    semantic_id="pit_v1.0.0_sun_in_the_first_house__太阳过境第一_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunInTheFirstHouse太阳过境第一(SemanticEntry):
    """
    **Source Text** (Lines 1671-1694):
> At this time of year, for approximately one month, you will be ...
    """
    
    original_text: str = """**Source Text** (Lines 1671-1694):
> At this time of year, for approximately one month, you will be able to recharge yourself, so to speak, for the year to come. You will become more concerned with personal matters and less with the world at large. This period is self-centered in a positive sense in that it is born not of selfishness, but of a real need to look at yourself and find out what you need for further progress.
> 
> Because the Sun is the source of all energy in the horoscope and because the first house is the projection of your personality, this transit indicates a time when you can project yourself with more forcefulness than usual. It is an excellent time for making an impression on others, but you must be careful because you will not be especially sensitive to their needs. This is because of the self-centeredness mentioned above. You are wrapped up primarily in your own concerns and are likely to have a very subjective viewpoint on most matters. For this reason, you may find it difficult to work with others during this transit.
> 
> Under certain conditions this transit may also result in marital problems, but only if there are other, more serious transits. Nevertheless, this is not one of the best times for resolving marital conflicts.
> 
> You have a great need to express yourself now, and it is a valid need. No purpose will be served by denying all your own needs in favor of a misguided concept of duty. There are times, and this is one of them, when your first duty is to yourself, and if you don't fulfill that duty, you will be of little use to anyone else.

**Key Term Analysis**:
- **Recharge**: literal = restore energy / symbolic = solar return to self / context = annual renewal cycle
- **Self-centered (positive)**: literal = focused on self / symbolic = legitimate self-attention / context = not selfishness but necessary introspection
- **First house**: literal = Ascendant house / symbolic = personality projection, physical self / context = how you appear to world
- **Forcefulness**: literal = strength of impact / symbolic = solar vitality amplified / context = enhanced personal projection
- **Subjective viewpoint**: literal = internal perspective / symbolic = ego-centered perception / context = reduced objectivity

**English Paraphrase (Primary Language)**:
When the transiting Sun passes through your first house (approximately one month annually, beginning at your Ascendant), you enter a period of personal renewal and self-focus. This is the solar energy returning to your house of self-identity, creating optimal conditions for recharging your vitality for the coming year. Hand emphasizes this self-centeredness is positive and necessary—not selfish but essential for self-understanding and future progress. The Sun as horoscope's energy source, combined with the first house as personality projection, creates a time of enhanced personal forcefulness. You can make strong impressions on others, but sensitivity to their needs diminishes. Your perspective becomes highly subjective, making collaborative work challenging. Marital tensions may surface if supported by other difficult transits, and this is not ideal for resolving partnership conflicts. The core message: your first duty during this transit is to yourself—fulfill this duty or you cannot serve others effectively.

**Complete Chinese Interpretation (Secondary Language)**:
当流年太阳过境第一宫（每年约一个月，从上升点开始），你进入个人更新和自我聚焦的时期。这是太阳能量回归你的自我认同宫位，为来年的活力充电创造最佳条件。汉德强调这种「自我中心」是正面且必要的——不是自私，而是理解自我和未来进步所必需的。太阳作为星盘的能量源，结合第一宫作为人格投射之宫，创造了增强个人力量感的时期。你能给他人留下强烈印象，但对他人需求的敏感度降低。你的视角变得高度主观，使合作工作变得困难。如果有其他困难行运支持，婚姻紧张可能浮现，这不是解决伴侣冲突的理想时期。核心信息：在此行运期间，你对自己的首要责任是照顾自己——履行这个责任，否则你无法有效服务他人。

**Core Points**:
- Sun in 1st house = annual recharge period lasting ~1 month
- Self-focus is positive necessity, not selfishness
- Sun = energy source + 1H = personality projection → enhanced forcefulness
- Excellent for making impressions on others
- Reduced sensitivity to others' needs during transit
- Highly subjective viewpoint develops
- Collaborative work becomes challenging
- Marital problems possible if supported by other transits
- Not ideal time for resolving partnership conflicts
- Self-care is primary duty—neglecting it renders you useless to others
- This self-duty precedes duty to others

**Detailed Explanation**:
Hand presents the Sun's first house transit as the personal New Year within the annual solar cycle. The Sun's nature as life-giving energy combined with the first house's role as the window of self-expression creates a concentrated period of personal power. The advice to prioritize self during this time reflects Hand's psychological approach to astrology—recognizing that sustainable service to others requires a foundation of self-understanding and self-care. The warning about relationship difficulties stems from the natural tension between 1st house (self) and 7th house (partnership) axes. This transit's timing (one month annually starting from Ascendant) makes it predictable and plannable for personal development work.

**Narrative Snippets**:
- `[ns_pit_001]` `[trigger: sun_transit_house_1]` `[factor_trigger: astro_transit_sun AND astro_house_1]` `[role: 主干]` Sun in the first house creates a period of personal renewal—recharge yourself for the year to come. → PIT Ch4 Sun-1H
- `[ns_pit_002]` `[trigger: sun_transit_house_1]` `[factor_trigger: astro_transit_sun AND astro_house_1]` `[role: 主干依赖]` This self-centeredness is positive, born not of selfishness but of real need to find out what you need for further progress. → PIT Ch4 Sun-1H
- `[ns_pit_003]` `[trigger: sun_transit_house_1]` `[factor_trigger: astro_transit_sun AND astro_house_1]` `[role: 主干依赖]` You can project yourself with more forcefulness than usual—excellent time for making an impression on others. → PIT Ch4 Sun-1H
- `[ns_pit_004]` `[trigger: sun_transit_house_1]` `[factor_trigger: astro_transit_sun AND astro_house_1]` `[role: 条件分支]` You will not be especially sensitive to others' needs; you have a very subjective viewpoint on most matters. → PIT Ch4 Sun-1H
- `[ns_pit_005]` `[trigger: sun_transit_house_1 AND astro_relationship]` `[factor_trigger: astro_transit_sun AND astro_house_1 AND astro_natal_7h_ruler]` `[role: 条件分支]` This transit may result in marital problems if there are other more serious transits—not the best time for resolving marital conflicts. → PIT Ch4 Sun-1H
- `[ns_pit_006]` `[trigger: sun_transit_house_1]` `[factor_trigger: astro_transit_sun AND astro_house_1]` `[role: 总结]` Your first duty is to yourself; if you don't fulfill that duty, you will be of little use to anyone else. → PIT Ch4 Sun-1H
- `[ns_pit_h1]` `[trigger: house_1]` `[factor_trigger: house_1]` `[role: 主干]` First house represents self, personality, physical body, personal initiative and self-projection. → PIT Foundation
- `[ns_pit_ts]` `[trigger: transit_sun]` `[factor_trigger: transit_sun]` `[role: 主干]` Transiting Sun moves through the zodiac approximately 1 degree per day, spending about one month in each house. → PIT Foundation
- `[ns_pit_h7]` `[trigger: house_7]` `[factor_trigger: house_7]` `[role: 条件分支]` Seventh house represents partnerships, marriage, open enemies, and one-to-one relationships—opposite the first house. → PIT Foundation

**Textual Criticism & Variant Analysis**:
- **English**: N/A - Single authoritative source (1976 Para Research edition). Hand's original text is definitive.
- **中文**: 无变体 - 单一权威来源（1976年Para Research版）。汉德原文为定本。"""
    normalized_text_zh: str = """"""
    subject: str = "Sun in the First House (太阳过境第一宫)"
    factor_refs: list = ['transit_sun', 'house_1', 'state_positive_self_focus', 'state_enhanced_projection', 'state_subjective_perception']
    
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
        l1_anchor="pit_v1.0.0_sun_in_the_first_house__太阳过境第一_001_L1",
    )
    version: str = "1.0.0"
