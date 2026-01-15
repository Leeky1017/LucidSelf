"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008740
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
    semantic_id="lt_v1.0.0_lesson_4__the_spread__牌阵_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Lesson4TheSpread牌阵(SemanticEntry):
    """
    **Source Text** (Lines 610-645): A spread is a preset pattern for laying out the tarot cards. It def...
    """
    
    original_text: str = """**Source Text** (Lines 610-645): A spread is a preset pattern for laying out the tarot cards. It defines how many cards to use, where each one goes, and what each one means.

**English Paraphrase**: A **spread** is "a template guiding the placement of the cards so they can shed light on a given topic." The most important feature is that "each position has a unique meaning that colors the interpretation of whatever card falls in that spot."

**Complete Chinese Interpretation**: **牌阵**是"引导牌卡放置的模板，使它们能够照亮给定的主题。"最重要的特点是"每个位置都有独特的含义，这会给落在该位置的任何牌的解读染上颜色。"

**Key Concepts**:
- **Position meaning** (位置含义): Colors interpretation of card
- **Celtic Cross**: Most popular spread, strong energy built up over years
- **Spread size**: 6-15 cards is optimal range

**Narrative Snippets**:
- `[ns_ltt_128]` `[trigger: spread_position]` `[factor_trigger: tarot_spread]` `[role: 主干]` Each position has unique meaning that colors card interpretation. → L616-618
- `[ns_ltt_129]` `[trigger: celtic_cross]` `[factor_trigger: tarot_celtic_cross]` `[role: 主干]` Celtic Cross is most popular spread with strong accumulated energy. → L638-642"""
    normalized_text_zh: str = """"""
    subject: str = "Lesson 4: The Spread (牌阵)"
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
        book_id="learning_tarot",
        chapter="",
        l1_anchor="lt_v1.0.0_lesson_4__the_spread__牌阵_001_L1",
    )
    version: str = "1.0.0"
