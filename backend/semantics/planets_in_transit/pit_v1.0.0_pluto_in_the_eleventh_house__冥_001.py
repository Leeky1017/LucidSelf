"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.238075
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
    semantic_id="pit_v1.0.0_pluto_in_the_eleventh_house__冥_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class PlutoInTheEleventhHouse冥(SemanticEntry):
    """
    **Source Text** (Lines 19074-19104):
> Great changes in long-range goals and hopes for future. Kinds...
    """
    
    original_text: str = """**Source Text** (Lines 19074-19104):
> Great changes in long-range goals and hopes for future. Kinds of people as friends will change. Activities once enjoyed may no longer appeal. Many goals once pursued not worth pursuing. Ideals will change—reflected in people you associate with and groups you identify with. Looking for quite different kind of friendship—not just people you feel at ease with, but intense encounters emotionally and otherwise. Some not pleasant—seeking to confront new dimensions of self through them. Friendships now have purpose in individual development, not casual encounters. One friendship in particular may change your life—you may meet someone affecting you so strongly entire course of life is changed. But that's what you've been seeking. Avoid associating just because powerful and persuasive. Desire for intense experiences shouldn't lead to friends guiding life into wrong paths. Danger of unconscious compulsions taking over. But equally possible to meet someone who can really act as guide and teacher. May become associated with group wanting to reform society. Avoid ruthless persons—with Plutonian energies could be dangerous. If present interest in positive reform sincere, may find others with same aims. Shallow old friendships may end, new ones formed. Doesn't matter as long as fulfill fundamental purposes: transformation through friendships and regeneration of goals.

**English Paraphrase**: Goals and friendships transform. Seek intense, purposeful friendships. One friendship may change your life. Avoid just following powerful people. May join reform movements. Shallow friendships end, new purposeful ones form.

**Complete Chinese Interpretation**: 目标和友谊转变。寻求强烈、有目的的友谊。一段友谊可能改变你的生活。避免只是追随有权势的人。可能加入改革运动。肤浅的友谊结束，新的有目的的形成。

**Narrative Snippets**:
- `[ns_pit_pl011]` `[trigger: pluto_transit_house_11]` `[factor_trigger: astro_transit_pluto AND astro_house_11]` `[role: 主干]` Goals and friendships transform. Seek meaningful connections. One friendship may change life. → PIT Ch13 Pluto-11H"""
    normalized_text_zh: str = """"""
    subject: str = "Pluto in the Eleventh House (冥王星过境第十一宫)"
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
        l1_anchor="pit_v1.0.0_pluto_in_the_eleventh_house__冥_001_L1",
    )
    version: str = "1.0.0"
