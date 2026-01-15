"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.300986
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
    semantic_id="pit_v1.0.0_moon_in_the_second_house__月亮过境_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonInTheSecondHouse月亮过境(SemanticEntry):
    """
    **Source Text** (Lines 3585-3605):
> You emotionally identify with your possessions or whatever you ...
    """
    
    original_text: str = """**Source Text** (Lines 3585-3605):
> You emotionally identify with your possessions or whatever you value. This can lead to strong attachment and possessiveness. You may unconsciously identify with your value system so that every challenge feels like a challenge to yourself. You probably feel best when surrounded by familiar objects that hold memories from your past. Traditionally a bad time to spend money—attitudes toward possessions are conditioned by unconscious drives.

**English Paraphrase**: Emotionally identify with possessions and values. Strong attachment, possessiveness. Challenges to values feel personal. Prefer familiar objects with memories. Bad time to spend money—unconscious drives influence decisions.

**Complete Chinese Interpretation**: 情感上与财产和价值观认同。强烈依附，占有欲。对价值观的挑战感觉像人身攻击。喜欢带有记忆的熟悉物品。不是花钱的好时候——无意识驱动影响决定。

**Narrative Snippets**:
- `[ns_pit_m003]` `[trigger: moon_transit_house_2]` `[factor_trigger: astro_transit_moon AND astro_house_2]` `[role: 主干]` Emotionally identify with possessions—strong attachment, every challenge to values feels personal. → PIT Ch5 Moon-2H
- `[ns_pit_m004]` `[trigger: moon_transit_house_2]` `[factor_trigger: astro_transit_moon AND astro_house_2]` `[role: 条件分支]` Bad time to spend money—unconscious drives condition purchasing decisions. → PIT Ch5 Moon-2H"""
    normalized_text_zh: str = """"""
    subject: str = "Moon in the Second House (月亮过境第二宫)"
    factor_refs: list = ['state_value_identity_fusion', 'state_possession_attachment', 'pattern_unconscious_spending']
    
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
        l1_anchor="pit_v1.0.0_moon_in_the_second_house__月亮过境_001_L1",
    )
    version: str = "1.0.0"
