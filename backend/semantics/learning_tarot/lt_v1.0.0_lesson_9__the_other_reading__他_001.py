"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008800
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
    semantic_id="lt_v1.0.0_lesson_9__the_other_reading__他_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Lesson9TheOtherReading他(SemanticEntry):
    """
    **Source Text** (Lines 1099-1147): The Other Reading - centered on another person or subject. About ...
    """
    
    original_text: str = """**Source Text** (Lines 1099-1147): The Other Reading - centered on another person or subject. About someone, not for them.

**English Paraphrase**: **Other Reading** is "centered on another person or subject" and is "about someone, not for him or her." Before doing one, ask three test questions: Do I feel strong emotions? Do I have vested interest? Do I desire particular outcome? If yes to any, do reading for yourself instead.

**Complete Chinese Interpretation**: **他人解读**是"以另一个人或主题为中心"，是"关于某人，而不是为某人。"在做之前，问三个测试问题：我是否有强烈情绪？我是否有既得利益？我是否渴望特定结果？如果任何一个是肯定的，就为自己做解读。

**Three Test Questions**:
1. Do I feel strong emotions about this person/situation?
2. Do I have a vested interest in this situation?
3. Do I desire a particular outcome?

If YES to any → Do reading centered on yourself instead

**Narrative Snippets**:
- `[ns_ltt_138]` `[trigger: other_reading]` `[factor_trigger: tarot_other_reading]` `[role: 主干]` Other Reading is about someone, not for them. Test with 3 questions. → L1099-1127"""
    normalized_text_zh: str = """"""
    subject: str = "Lesson 9: The Other Reading (他人解读)"
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
        l1_anchor="lt_v1.0.0_lesson_9__the_other_reading__他_001_L1",
    )
    version: str = "1.0.0"
