"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.223941
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
    semantic_id="pit_v1.0.0_sun_in_the_twelfth_house__太阳过境_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunInTheTwelfthHouse太阳过境(SemanticEntry):
    """
    **Source Text** (Lines 1958-1988):
> At this time you have to get in touch with your own subconsciou...
    """
    
    original_text: str = """**Source Text** (Lines 1958-1988):
> At this time you have to get in touch with your own subconscious mind, to find out how it directs your life in ways that you aren't aware of. We all broadcast two kinds of signals: what we think we're doing, and unconscious signals revealing what we're really doing.
> 
> Particularly deadly are childhood behavior patterns that have long outlived their usefulness. The only way to handle them is to recognize and experience them with full and detached consciousness.
> 
> Your year is ending. This is a good time to look back and see how well you have managed the art of living. Anything you refuse to face will continue in your unconscious and work against you when you least expect it.

**English Paraphrase**: Get in touch with subconscious—find how it directs life in ways you're unaware. Two signal types: conscious and unconscious. Childhood patterns particularly deadly—handle through detached recognition. Year is ending; evaluate art of living. Refused material continues in unconscious, works against you.

**Complete Chinese Interpretation**: 接触潜意识——发现它如何以你不知道的方式指导生活。两种信号：有意识和无意识。童年模式特别致命——通过超脱的认识来处理。一年正在结束；评估生活艺术。拒绝面对的东西继续存在于无意识中，对你不利。

**Narrative Snippets**:
- `[ns_pit_042]` `[trigger: sun_transit_house_12]` `[factor_trigger: astro_transit_sun AND astro_house_12]` `[role: 主干]` Get in touch with your subconscious mind—find out how it directs your life in ways you aren't aware of. → PIT Ch4 Sun-12H
- `[ns_pit_043]` `[trigger: sun_transit_house_12]` `[factor_trigger: astro_transit_sun AND astro_house_12]` `[role: 主干依赖]` Particularly deadly are childhood behavior patterns that have outlived their usefulness. → PIT Ch4 Sun-12H
- `[ns_pit_044]` `[trigger: sun_transit_house_12]` `[factor_trigger: astro_transit_sun AND astro_house_12]` `[role: 总结]` Anything you refuse to face will continue in your unconscious and work against you when you least expect it. → PIT Ch4 Sun-12H"""
    normalized_text_zh: str = """"""
    subject: str = "Sun in the Twelfth House (太阳过境第十二宫)"
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
        l1_anchor="pit_v1.0.0_sun_in_the_twelfth_house__太阳过境_001_L1",
    )
    version: str = "1.0.0"
