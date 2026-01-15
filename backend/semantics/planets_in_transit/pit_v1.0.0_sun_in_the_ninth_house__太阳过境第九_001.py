"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.223878
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
    semantic_id="pit_v1.0.0_sun_in_the_ninth_house__太阳过境第九_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunInTheNinthHouse太阳过境第九(SemanticEntry):
    """
    **Source Text** (Lines 1882-1905):
> During this time you should attempt to broaden your horizons in...
    """
    
    original_text: str = """**Source Text** (Lines 1882-1905):
> During this time you should attempt to broaden your horizons in every way possible — through study, new and unfamiliar experiences, travel or by meeting people from totally different backgrounds.
> 
> This is an extremely favorable time to undertake a new course of study, a new hobby or intellectual discipline. Break out of your everyday mold and get into the broader world. Travel would be a good way to do this.
> 
> This transit may also indicate involvement or concern with the law, and metaphysical, religious and spiritual concerns in general.

**English Paraphrase**: Broaden horizons through study, new experiences, travel, diverse people. Favorable for new study, hobby, intellectual discipline. Break from routine into broader world. Travel excellent. May indicate legal involvement, metaphysical/religious/spiritual concerns.

**Complete Chinese Interpretation**: 通过学习、新体验、旅行、不同背景的人拓宽视野。对新学习、爱好、知识学科有利。打破常规进入更广阔的世界。旅行极好。可能表示法律参与、形而上学/宗教/精神关注。

**Narrative Snippets**:
- `[ns_pit_036]` `[trigger: sun_transit_house_9]` `[factor_trigger: astro_transit_sun AND astro_house_9]` `[role: 主干]` Broaden your horizons in every way—through study, new experiences, travel, or meeting people from different backgrounds. → PIT Ch4 Sun-9H
- `[ns_pit_037]` `[trigger: sun_transit_house_9]` `[factor_trigger: astro_transit_sun AND astro_house_9]` `[role: 主干依赖]` Extremely favorable for new courses of study, hobbies, or intellectual disciplines. Break out of your everyday mold. → PIT Ch4 Sun-9H"""
    normalized_text_zh: str = """"""
    subject: str = "Sun in the Ninth House (太阳过境第九宫)"
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
        l1_anchor="pit_v1.0.0_sun_in_the_ninth_house__太阳过境第九_001_L1",
    )
    version: str = "1.0.0"
