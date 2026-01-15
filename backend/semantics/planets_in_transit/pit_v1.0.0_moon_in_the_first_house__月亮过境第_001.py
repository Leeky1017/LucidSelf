"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.300945
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
    semantic_id="pit_v1.0.0_moon_in_the_first_house__月亮过境第_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonInTheFirstHouse月亮过境第(SemanticEntry):
    """
    **Source Text** (Lines 3569-3584):
> This is a two-day period when personal and subjective considera...
    """
    
    original_text: str = """**Source Text** (Lines 3569-3584):
> This is a two-day period when personal and subjective considerations will override everything else. You feel a great need to belong and relate to friends or loved ones. This need turns on your emotional sensors and makes you very sensitive to the feelings and moods of people around you. You can be very emotionally giving, but also emotionally demanding if you feel inadequate. Be careful not to demand more nurturing than you can give.

**English Paraphrase**: Two-day period of personal, subjective focus. Strong need to belong and relate. Emotional sensors highly active—sensitive to others' feelings. Can be emotionally giving OR astro_demanding. Don't demand more nurturing than you can give. Objectivity difficult now.

**Complete Chinese Interpretation**: 两天的个人主观聚焦期。强烈需要归属和联系。情感感应器高度活跃——对他人感受敏感。可以很情感付出或索求。不要索求超过你能给予的滋养。客观性现在困难。

**Narrative Snippets**:
- `[ns_pit_m001]` `[trigger: moon_transit_house_1]` `[factor_trigger: astro_transit_moon AND astro_house_1]` `[role: 主干]` Two-day period of personal, subjective focus—very sensitive to others' feelings and moods. → PIT Ch5 Moon-1H
- `[ns_pit_m002]` `[trigger: moon_transit_house_1]` `[factor_trigger: astro_transit_moon AND astro_house_1]` `[role: 条件分支]` Can be emotionally giving OR demanding—don't demand more nurturing than you can give. → PIT Ch5 Moon-1H
- `[ns_pit_tm]` `[trigger: transit_moon]` `[factor_trigger: transit_moon]` `[role: 主干]` Transiting Moon moves fastest through zodiac (~2.5 days per sign), triggering brief emotional fluctuations and mood shifts. → PIT Foundation
- `[ns_pit_mn]` `[trigger: moon_needs]` `[factor_trigger: moon_needs]` `[role: 条件分支]` Moon needs represent emotional requirements, security needs, and nurturing patterns—activated when Moon transits sensitive points. → PIT Foundation
- `[ns_pit_mf]` `[trigger: moon_familiar]` `[factor_trigger: moon_familiar]` `[role: 条件分支]` Moon familiar refers to habitual emotional patterns and comfort-seeking behaviors rooted in early conditioning. → PIT Foundation
- `[ns_pit_tp]` `[trigger: transit_planet]` `[factor_trigger: transit_planet]` `[role: 主干]` Transit planet is any planet currently moving through the zodiac, activating natal points and houses it contacts. → PIT Foundation
- `[ns_pit_es]` `[trigger: state_emotional_sensitivity]` `[factor_trigger: state_emotional_sensitivity]` `[role: 效果]` State of heightened emotional sensitivity—increased awareness of and responsiveness to emotional undercurrents. → PIT Foundation
- `[ns_pit_smg]` `[trigger: state_moon_1h_giving]` `[factor_trigger: state_moon_1h_giving]` `[role: 效果]` State of emotional giving when Moon transits 1st house—nurturing outflow when feeling emotionally adequate. → PIT Foundation
- `[ns_pit_smd]` `[trigger: state_moon_1h_demanding]` `[factor_trigger: state_moon_1h_demanding]` `[role: 效果]` State of emotional demanding when Moon transits 1st house—seeking nurturing when feeling inadequate. → PIT Foundation
- `[ns_pit_sar]` `[trigger: state_automatic_reactions]` `[factor_trigger: state_automatic_reactions]` `[role: 效果]` State of automatic emotional reactions triggered by Moon transits activating conditioned patterns. → PIT Foundation"""
    normalized_text_zh: str = """"""
    subject: str = "Moon in the First House (月亮过境第一宫)"
    factor_refs: list = ['transit_moon', 'state_emotional_sensitivity', 'pattern_nurturing_exchange']
    
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
        l1_anchor="pit_v1.0.0_moon_in_the_first_house__月亮过境第_001_L1",
    )
    version: str = "1.0.0"
