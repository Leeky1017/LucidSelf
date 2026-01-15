"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.009137
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
    semantic_id="lt_v1.0.0_exercise_categories_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class ExerciseCategories(SemanticEntry):
    """
    **Source Text** (Lines 2009-2300): Section II contains exercises for each lesson. Exercises are opti...
    """
    
    original_text: str = """**Source Text** (Lines 2009-2300): Section II contains exercises for each lesson. Exercises are optional but reinforce concepts.

**Exercise Types by Lesson**:

**Lesson 1 Exercises**:
- "What Do I Believe?" - rate belief 0-100%
- "Getting to Know a Card" - study card details
- "Answers from Nowhere" - library/bookstore intuition exercise
- "You Can Get What You Need" - $5 bill intention exercise

**Lesson 2-3 Exercises**:
- Study Major Arcana cards in section 4
- Read Fool's Journey (Appendix A)
- Suit Qualities exercises - match word pairs to suits

**Lesson 4-6 Exercises**:
- Celtic Cross Spread practice
- Design your own 3-card spread
- Create your tarot reading space
- Quest for a Symbol - find personal tarot symbol

**Lesson 7-10 Exercises**:
- Write practice questions
- Do full Question Reading
- Do Other Reading about news event
- Test self-involvement with 3 questions

**Lesson 11-19 Exercises**:
- Interpret single cards
- Compare Major/Minor weight
- Study Aces as portals
- Court card personality exercises
- Card pair identification
- Position pair analysis
- Reversed card practice
- Story creation practice

**Narrative Snippets**:
- `[ns_ltt_172]` `[trigger: exercises]` `[factor_trigger: tarot_practice]` `[role: 主干]` Exercises reinforce each lesson: belief assessment, card study, spread practice, interpretation."""
    normalized_text_zh: str = """"""
    subject: str = "Exercise Categories"
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
        l1_anchor="lt_v1.0.0_exercise_categories_001_L1",
    )
    version: str = "1.0.0"
