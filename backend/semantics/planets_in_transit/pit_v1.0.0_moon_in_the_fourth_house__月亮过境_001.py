"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301012
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
    semantic_id="pit_v1.0.0_moon_in_the_fourth_house__月亮过境_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonInTheFourthHouse月亮过境(SemanticEntry):
    """
    **Source Text** (Lines 3625-3647):
> Good time to retire to your own private place. You seek comfort...
    """
    
    original_text: str = """**Source Text** (Lines 3625-3647):
> Good time to retire to your own private place. You seek comfort from outside world demands. Good time to go inside yourself and look at attitudes, feelings, emotional orientation. You may become aware of how habits and past conditioning control your life now. You will probably feel emotionally more possessive—strong fear of being alone or alienated makes you hold on tightly. But holding on leads to losing.

**English Paraphrase**: Good time to retire to private space. Seek comfort from outside demands. Look inside—examine attitudes, feelings. May realize how habits/conditioning control you now. Emotionally possessive—fear of being alone makes you hold tight, but this causes loss.

**Complete Chinese Interpretation**: 退回私人空间的好时机。寻求外界要求的慰藉。向内看——检视态度、感受。可能意识到习惯/条件反射如何控制你。情感上占有欲强——害怕独处使你紧握，但这导致失去。

**Narrative Snippets**:
- `[ns_pit_m007]` `[trigger: moon_transit_house_4]` `[factor_trigger: astro_transit_moon AND astro_house_4]` `[role: 主干]` Good time to retire to private space—look inside, examine attitudes and feelings. → PIT Ch5 Moon-4H
- `[ns_pit_m008]` `[trigger: moon_transit_house_4]` `[factor_trigger: astro_transit_moon AND astro_house_4]` `[role: 条件分支]` May realize how past conditioning controls you. Holding on too tight leads to losing. → PIT Ch5 Moon-4H"""
    normalized_text_zh: str = """"""
    subject: str = "Moon in the Fourth House (月亮过境第四宫)"
    factor_refs: list = ['state_private_retreat', 'state_conditioning_awareness', 'pattern_attachment_paradox']
    
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
        l1_anchor="pit_v1.0.0_moon_in_the_fourth_house__月亮过境_001_L1",
    )
    version: str = "1.0.0"
