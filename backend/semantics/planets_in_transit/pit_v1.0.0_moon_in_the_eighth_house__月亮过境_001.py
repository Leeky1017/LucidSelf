"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301059
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
    semantic_id="pit_v1.0.0_moon_in_the_eighth_house__月亮过境_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonInTheEighthHouse月亮过境(SemanticEntry):
    """
    **Source Text** (Lines 3708-3724):
> Emotional experiences much more intense than usual. Drawn to in...
    """
    
    original_text: str = """**Source Text** (Lines 3708-3724):
> Emotional experiences much more intense than usual. Drawn to intense or powerful people who have strong effect on you. Through emotional encounters, you experience moods and feelings quite different from your "normal" self. May feel effects like second house (possessiveness) but with added danger of conflict over joint possessions. You may desire something that belongs to someone else or greater control over shared things. Recognize that attachment serves no real purpose and is potential source of trouble.

**English Paraphrase**: Emotional experiences intense. Drawn to powerful people with strong effect. Experience unusual moods through encounters. Second house effects (possessiveness) plus conflict over joint possessions. May desire others' things or control over shared things. Recognize attachment is trouble source.

**Complete Chinese Interpretation**: 情感体验强烈。被有强烈影响的强大人物吸引。通过遭遇体验不寻常的情绪。第二宫效果（占有欲）加上共同财产冲突。可能想要他人的东西或对共享事物的控制。认识到依附是麻烦来源。

**Narrative Snippets**:
- `[ns_pit_m015]` `[trigger: moon_transit_house_8]` `[factor_trigger: astro_transit_moon AND astro_house_8]` `[role: 主干]` Emotional experiences much more intense—drawn to powerful people. Experience unusual moods. → PIT Ch5 Moon-8H
- `[ns_pit_m016]` `[trigger: moon_transit_house_8]` `[factor_trigger: astro_transit_moon AND astro_house_8]` `[role: 条件分支]` Conflict danger over joint possessions. Recognize attachment serves no real purpose. → PIT Ch5 Moon-8H"""
    normalized_text_zh: str = """"""
    subject: str = "Moon in the Eighth House (月亮过境第八宫)"
    factor_refs: list = ['state_emotional_intensity', 'pattern_power_attraction', 'state_attachment_awareness']
    
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
        l1_anchor="pit_v1.0.0_moon_in_the_eighth_house__月亮过境_001_L1",
    )
    version: str = "1.0.0"
