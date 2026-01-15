"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301071
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
    semantic_id="pit_v1.0.0_moon_in_the_ninth_house__月亮过境第_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonInTheNinthHouse月亮过境第(SemanticEntry):
    """
    **Source Text** (Lines 3727-3744):
> Strong urge to get away from daily routine, not entirely consci...
    """
    
    original_text: str = """**Source Text** (Lines 3727-3744):
> Strong urge to get away from daily routine, not entirely conscious of reasons. It's a mood, a restlessness hard to pin down. Contradiction: Moon clings to familiar while ninth house takes you away. Travel beneficial if break isn't too radical—you're not interested in getting totally away, just bored with everyday life. Study or mental journeys may be more useful—remain in familiar surroundings while exposed to revolutionary and liberating ideas. May meet new friends from foreign countries or different backgrounds.

**English Paraphrase**: Strong urge to escape routine—restlessness hard to explain. Contradiction: Moon wants familiar, 9H takes away. Travel okay if not too radical—just bored, not seeking total escape. Study/mental journeys better—familiar surroundings with new ideas. May meet foreign or different friends.

**Complete Chinese Interpretation**: 强烈想逃离常规——难以解释的不安。矛盾：月亮要熟悉，第九宫带走。旅行可以如果不太激进——只是无聊，不寻求完全逃离。学习/心智旅程更好——熟悉环境中接触新想法。可能遇到外国或不同的朋友。

**Narrative Snippets**:
- `[ns_pit_m017]` `[trigger: moon_transit_house_9]` `[factor_trigger: astro_transit_moon AND astro_house_9]` `[role: 主干]` Strong urge to escape routine—restlessness hard to pin down. Contradiction between Moon's needs and 9H. → PIT Ch5 Moon-9H
- `[ns_pit_m018]` `[trigger: moon_transit_house_9]` `[factor_trigger: astro_transit_moon AND astro_house_9]` `[role: 条件分支]` Study or mental journeys better than travel—familiar surroundings with liberating ideas. → PIT Ch5 Moon-9H"""
    normalized_text_zh: str = """"""
    subject: str = "Moon in the Ninth House (月亮过境第九宫)"
    factor_refs: list = ['state_restless_escape', 'pattern_familiar_foreign', 'pattern_mental_journey']
    
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
        l1_anchor="pit_v1.0.0_moon_in_the_ninth_house__月亮过境第_001_L1",
    )
    version: str = "1.0.0"
