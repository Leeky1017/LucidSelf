"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.280752
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
    semantic_id="pit_v1.0.0_mercury_in_the_fifth_house__水星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MercuryInTheFifthHouse水星(SemanticEntry):
    """
    **Source Text** (Lines 5069-5091):
> Good for expressing thoughts and communicating them. Like 1H tr...
    """
    
    original_text: str = """**Source Text** (Lines 5069-5091):
> Good for expressing thoughts and communicating them. Like 1H transit. Use your mind for amusement—reading, writing, games requiring mental agility. Ideas may just be fun to play with. Be careful not to play with people for your own amusement. Mercury is the planet of pranks. May be poor listener. Pursuing mental activities for their own sake can enlarge your mind.

**English Paraphrase**: Good for expressing thoughts. Mind for amusement—reading, writing, games. Ideas fun to play with. Don't play pranks on people. May be poor listener. Mental play enlarges mind.

**Complete Chinese Interpretation**: 适合表达想法。心智用于娱乐——阅读、写作、游戏。想法有趣可以玩。不要对人恶作剧。可能是糟糕的听众。智力游戏扩展思维。

**Narrative Snippets**:
- `[ns_pit_me006]` `[trigger: mercury_transit_house_5]` `[factor_trigger: astro_transit_mercury AND astro_house_5]` `[role: 主干]` Mind for amusement—reading, writing, games. Mercury is planet of pranks. → PIT Ch6 Mercury-5H"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury in the Fifth House (水星过境第五宫)"
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
        l1_anchor="pit_v1.0.0_mercury_in_the_fifth_house__水星_001_L1",
    )
    version: str = "1.0.0"
