"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008752
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
    semantic_id="lt_v1.0.0_lesson_5__the_daily_reading__日_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Lesson5TheDailyReading日(SemanticEntry):
    """
    **Source Text** (Lines 646-722): The Daily Reading - select a single card that becomes your theme fo...
    """
    
    original_text: str = """**Source Text** (Lines 646-722): The Daily Reading - select a single card that becomes your theme for the day. Purpose is to heighten awareness of one approach to life for a single twenty-four-hour period.

**English Paraphrase**: In **Daily Reading**, you "select a single card that becomes your theme for the day." The purpose is to "heighten your awareness of one approach to life for a single twenty-four-hour period" and to "learn the tarot without strain or tedium."

**Complete Chinese Interpretation**: 在**日常解读**中，你"选择一张牌作为当天的主题。"目的是"提高你对一种生活方式的认识，持续24小时"，并"在没有压力或乏味的情况下学习塔罗牌。"

**Key Concepts**:
- **Theme card** (主题牌): Single card for the day
- **Journal** (日记): Track selections with color coding
- **Color system**: Wands=Red, Cups=Blue, Swords=Yellow, Pentacles=Green, Major=Purple

**Daily Reading Procedure**:
1. Shuffle deck once or twice
2. Hold deck face down, cover with other hand
3. Pause to become calm and centered
4. Ask Inner Guide for guidance
5. Place deck face down, cut to left, restack
6. Turn over top card as card of the day
7. Return card, shuffle once or twice

**Narrative Snippets**:
- `[ns_ltt_130]` `[trigger: daily_reading]` `[factor_trigger: tarot_daily_reading]` `[role: 主干]` Daily Reading heightens awareness of one approach for 24 hours. → L648-651
- `[ns_ltt_131]` `[trigger: color_coding]` `[factor_trigger: tarot_journal]` `[role: 辅助]` Color coding: Wands=Red(Fire), Cups=Blue(Water), Swords=Yellow(Air), Pentacles=Green(Earth), Major=Purple. → L702-708"""
    normalized_text_zh: str = """"""
    subject: str = "Lesson 5: The Daily Reading (日常解读)"
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
        l1_anchor="lt_v1.0.0_lesson_5__the_daily_reading__日_001_L1",
    )
    version: str = "1.0.0"
