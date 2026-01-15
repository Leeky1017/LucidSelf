"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008777
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
    semantic_id="lt_v1.0.0_lesson_7__writing_a_question___001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Lesson7WritingAQuestion(SemanticEntry):
    """
    **Source Text** (Lines 786-908): Writing a Question - Most tarot readings are for a problem or chall...
    """
    
    original_text: str = """**Source Text** (Lines 786-908): Writing a Question - Most tarot readings are for a problem or challenge. The question helps you relate guidance to your situation.

**English Paraphrase**: When writing a tarot question, follow these principles: **Accept Responsibility** (don't deflect to cards), **Keep Options Open** (don't decide answer ahead), **Find Best Level of Detail** (not too vague or detailed), **Focus on Yourself** (you are central character), **Stay Neutral** (open to other views), **Be Positive** (confident tone).

**Complete Chinese Interpretation**: 写塔罗问题时，遵循以下原则：**承担责任**（不要把决定权推给牌）、**保持开放选项**（不要预先决定答案）、**找到最佳细节级别**（不要太模糊或太详细）、**聚焦自己**（你是中心人物）、**保持中立**（对其他观点开放）、**保持积极**（自信的语气）。

**Six Principles for Question Writing**:
1. **Accept Responsibility**: Avoid "Should I..." or Yes/No questions
2. **Keep Options Open**: Don't decide answer ahead of time
3. **Find Best Level of Detail**: Balance between vague and over-detailed
4. **Focus on Yourself**: You are always central character
5. **Stay Neutral**: Open to other points of view
6. **Be Positive**: Confident, not defeatist tone

**Good Question Starters**:
- "Can you give me insight into..."
- "What do I need to understand about..."
- "What is the meaning of..."
- "How can I improve my chances of..."

**Narrative Snippets**:
- `[ns_ltt_134]` `[trigger: question_principles]` `[factor_trigger: tarot_question]` `[role: 主干]` Six principles: Responsibility, Open, Detail, Self-focus, Neutral, Positive. → L801-902
- `[ns_ltt_135]` `[trigger: question_starters]` `[factor_trigger: tarot_question]` `[role: 辅助]` Good starters: "What do I need to understand...", "How can I improve..." → L830-836"""
    normalized_text_zh: str = """"""
    subject: str = "Lesson 7: Writing a Question (问题书写)"
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
        l1_anchor="lt_v1.0.0_lesson_7__writing_a_question___001_L1",
    )
    version: str = "1.0.0"
