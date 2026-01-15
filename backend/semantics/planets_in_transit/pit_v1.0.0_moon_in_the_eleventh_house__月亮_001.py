"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301096
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
    semantic_id="pit_v1.0.0_moon_in_the_eleventh_house__月亮_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonInTheEleventhHouse月亮(SemanticEntry):
    """
    **Source Text** (Lines 3763-3784):
> Emotional contact with friends very important. If you or friend...
    """
    
    original_text: str = """**Source Text** (Lines 3763-3784):
> Emotional contact with friends very important. If you or friend has something personal to say at deeper emotional level, this is good time. Contact with friends much deeper than usual. May bring female friends into prominence. You feel more protective and supportive, or attract someone who gives you needed emotional support. If not conscious, may become possessive of friends, restrict their freedom from insecurity, become jealous when friend pays attention to someone else. Examine overall life goals—make sure they're real expression of yourself, not product of obsolete emotional attitudes.

**English Paraphrase**: Emotional contact with friends very important. Good time for deep personal sharing. Female friends prominent. Feel protective/supportive or attract supporter. Risk: possessiveness, jealousy, restricting friends' freedom. Examine life goals—are they real or obsolete emotional products?

**Complete Chinese Interpretation**: 与朋友的情感接触非常重要。深入个人分享的好时机。女性朋友突出。感到保护/支持或吸引支持者。风险：占有欲、嫉妒、限制朋友自由。检视人生目标——是真实的还是过时情感产物？

**Narrative Snippets**:
- `[ns_pit_m021]` `[trigger: moon_transit_house_11]` `[factor_trigger: astro_transit_moon AND astro_house_11]` `[role: 主干]` Emotional contact with friends very important—deeper than usual. Female friends prominent. → PIT Ch5 Moon-11H
- `[ns_pit_m022]` `[trigger: moon_transit_house_11]` `[factor_trigger: astro_transit_moon AND astro_house_11]` `[role: 条件分支]` Risk: possessiveness and jealousy with friends. Examine life goals—are they real or obsolete? → PIT Ch5 Moon-11H"""
    normalized_text_zh: str = """"""
    subject: str = "Moon in the Eleventh House (月亮过境第十一宫)"
    factor_refs: list = ['state_friendship_depth', 'state_friend_possessive', 'concept_goal_authenticity']
    
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
        l1_anchor="pit_v1.0.0_moon_in_the_eleventh_house__月亮_001_L1",
    )
    version: str = "1.0.0"
