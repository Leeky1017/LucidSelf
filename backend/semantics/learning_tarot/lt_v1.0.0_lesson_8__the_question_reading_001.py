"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008789
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
    semantic_id="lt_v1.0.0_lesson_8__the_question_reading_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Lesson8TheQuestionReading(SemanticEntry):
    """
    **Source Text** (Lines 909-1098): The Question Reading - Full procedure for exploring a personal que...
    """
    
    original_text: str = """**Source Text** (Lines 909-1098): The Question Reading - Full procedure for exploring a personal question. Procedure is important - same steps help center yourself.

**English Paraphrase**: The **Question Reading** follows a complete procedure: **Setting the Mood** (conducive environment, relax, still mind), **Asking Your Question** (hold cards, opening statement, ask question exactly as written), **Shuffling** (concentrate on question), **Cutting** (3-pile cut, regroup), **Laying Out Cards**, **Responding** (pay attention to reactions), **Analyzing** (review positions), **Creating the Story** (pull everything together), **Writing Summary Statement**, **Finishing Up** (clear deck, express gratitude).

**Complete Chinese Interpretation**: **问题解读**遵循完整流程：**设置情绪**（有利环境、放松、静心）、**提出问题**（握住牌、开场陈述、完全按书面提问）、**洗牌**（专注于问题）、**切牌**（三堆切牌、重组）、**铺牌**、**回应**（注意反应）、**分析**（审查位置）、**创建故事**（整合一切）、**写总结陈述**、**结束**（清理牌组、表达感谢）。

**Complete Reading Procedure**:
1. **Setting the Mood**: Relax, still mind, 30-40 min minimum
2. **Asking Your Question**: Hold cards, opening statement, say question exactly
3. **Shuffling**: Concentrate on overall intent
4. **Cutting**: 3-pile cut to left, regroup quickly
5. **Laying Out Cards**: Follow spread pattern
6. **Responding**: Pay attention to reactions, jot notes
7. **Analyzing**: Review each position, look for relationships
8. **Creating the Story**: Pull together spontaneously, speak out loud
9. **Summary Statement**: Distill main theme in 1-2 sentences
10. **Finishing Up**: Write down cards, clear deck, express gratitude

**Narrative Snippets**:
- `[ns_ltt_136]` `[trigger: reading_procedure]` `[factor_trigger: tarot_reading]` `[role: 主干]` Complete 10-step reading procedure from mood to gratitude. → L909-1098
- `[ns_ltt_137]` `[trigger: story_creation]` `[factor_trigger: tarot_story]` `[role: 主干依赖]` Creating the story - speak spontaneously, let it arise freely. → L1019-1034"""
    normalized_text_zh: str = """"""
    subject: str = "Lesson 8: The Question Reading (问题解读)"
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
        l1_anchor="lt_v1.0.0_lesson_8__the_question_reading_001_L1",
    )
    version: str = "1.0.0"
