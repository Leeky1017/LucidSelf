"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.223962
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
    semantic_id="pit_v1.0.0_sun_conjunct_sun__流年太阳合本命太阳_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunConjunctSun流年太阳合本命太阳(SemanticEntry):
    """
    **Source Text** (Lines 1989-2013):
> Today is your real birthday, even though it may be a day or two...
    """
    
    original_text: str = """**Source Text** (Lines 1989-2013):
> Today is your real birthday, even though it may be a day or two different from your calendar birthday. This is the date when the Sun returns to the position it was in when you were born, completing a full circuit around the ecliptic.
> 
> As would seem appropriate with this transit, today is a day of new beginnings. A new year in your own personal calendar has begun, and the influences you feel today will affect the entire year to come. Many astrologers find that the chart cast for the exact minute and second that the Sun returns to its birth position provides a significant forecast for the year ahead.
> 
> The energies you feel today may not be very dynamic, but you do feel as though you ought to be the center of attention in some way. Whatever you do or begin today will bear the stamp of your individuality more than anything else.

**English Paraphrase**: Your real birthday—Sun returns to birth position. Day of new beginnings; new personal year begins. Today's influences affect the entire year. Solar Return chart provides year forecast. You feel you should be center of attention. Whatever begun today bears your individuality's stamp.

**Complete Chinese Interpretation**: 你的真正生日——太阳返回出生位置。新开始的日子；新的个人年开始。今天的影响影响整年。太阳返照盘提供年度预测。你感觉应该成为关注中心。今天开始的任何事都带有你个性的印记。

**Narrative Snippets**:
- `[ns_pit_045]` `[trigger: transit_sun_conjunct_natal_sun]` `[factor_trigger: astro_transit_sun CONJUNCT natal_sun]` `[role: 主干]` Today is your real birthday—the Sun returns to its birth position. A day of new beginnings. → PIT Ch4 Sun☌Sun
- `[ns_pit_046]` `[trigger: transit_sun_conjunct_natal_sun]` `[factor_trigger: astro_transit_sun CONJUNCT natal_sun]` `[role: 主干依赖]` The influences you feel today will affect the entire year to come. Solar Return chart provides forecast. → PIT Ch4 Sun☌Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Conjunct Sun (流年太阳合本命太阳)"
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
        l1_anchor="pit_v1.0.0_sun_conjunct_sun__流年太阳合本命太阳_001_L1",
    )
    version: str = "1.0.0"
