"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.223835
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
    semantic_id="pit_v1.0.0_sun_in_the_seventh_house__太阳过境_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunInTheSeventhHouse太阳过境(SemanticEntry):
    """
    **Source Text** (Lines 1822-1852):
> At this time of year you should learn more about yourself throu...
    """
    
    original_text: str = """**Source Text** (Lines 1822-1852):
> At this time of year you should learn more about yourself through intimate one-to-one encounters with others. You will form working units with other people for various purposes, and through these units you will understand more about the effects that you have upon others.
> 
> One of the most important such relationship is marriage. If you are married, use this time to examine your relationship with your spouse and to discover what needs this relationship does and does not fill in your life.
> 
> This is not a time of the year when you should try to go it alone in any type of activity. You should try to work with someone else, or at least seek out the opinion of another person in an advisory capacity.
> 
> Sometimes the one-to-one encounter may take the form of a conflict. Conflict can be creative, because it forces you to examine your own position more thoroughly. You and your opponent form a pair, just as you and a partner do.

**English Paraphrase**: Learn about yourself through one-to-one encounters. Form working units with others; examine your effects on them. Marriage is the primary such relationship—examine what needs it fills and how well you fill your spouse's needs. NOT a time to go it alone—collaborate, seek advisory opinions. Conflict can be creative—forces self-examination. Opponent and partner both form pairs with you.

**Complete Chinese Interpretation**: 通过一对一接触了解自己。与他人形成工作单位；检验你对他们的影响。婚姻是最重要的此类关系——检验它满足的需求以及你满足配偶需求的程度。不是独自行动的时期——合作，寻求咨询。冲突可以是创造性的——迫使自我检视。对手和伙伴都与你形成配对。

**Narrative Snippets**:
- `[ns_pit_031]` `[trigger: sun_transit_house_7]` `[factor_trigger: astro_transit_sun AND astro_house_7]` `[role: 主干]` Learn more about yourself through intimate one-to-one encounters with others. → PIT Ch4 Sun-7H
- `[ns_pit_032]` `[trigger: sun_transit_house_7]` `[factor_trigger: astro_transit_sun AND astro_house_7]` `[role: 条件分支]` This is not a time to go it alone—work with someone else, seek advisory opinions. → PIT Ch4 Sun-7H
- `[ns_pit_033]` `[trigger: sun_transit_house_7]` `[factor_trigger: astro_transit_sun AND astro_house_7]` `[role: 总结]` Conflict can be creative—you and your opponent form a pair, just as you and a partner do. → PIT Ch4 Sun-7H"""
    normalized_text_zh: str = """"""
    subject: str = "Sun in the Seventh House (太阳过境第七宫)"
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
        l1_anchor="pit_v1.0.0_sun_in_the_seventh_house__太阳过境_001_L1",
    )
    version: str = "1.0.0"
