"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008811
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
    semantic_id="lt_v1.0.0_lesson_10__the_open_reading__开_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Lesson10TheOpenReading开(SemanticEntry):
    """
    **Source Text** (Lines 1148-1186): The Open Reading - request for guidance not tied to particular pr...
    """
    
    original_text: str = """**Source Text** (Lines 1148-1186): The Open Reading - request for guidance not tied to particular problem. No question written.

**English Paraphrase**: **Open Reading** is "a request for guidance that is not tied to a particular problem. You don't write a question." It offers "a higher level of guidance that embraces the larger patterns." Best for special occasions: birthdays, anniversaries, thresholds of new phases.

**Complete Chinese Interpretation**: **开放解读**是"不与特定问题挂钩的指导请求。你不写问题。"它提供"更高层次的指导，包含更大的模式。"最适合特殊场合：生日、周年纪念、新阶段的门槛。

**When to Use Open Reading**:
- Birthdays, anniversaries, ceremonial days
- Equinoxes, first days (new job, trip)
- Thresholds of new phases (birth of child, move to new house)
- Unknown expanse opening before you

**Narrative Snippets**:
- `[ns_ltt_139]` `[trigger: open_reading]` `[factor_trigger: tarot_open_reading]` `[role: 主干]` Open Reading offers higher guidance embracing larger patterns. → L1150-1159"""
    normalized_text_zh: str = """"""
    subject: str = "Lesson 10: The Open Reading (开放解读)"
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
        l1_anchor="lt_v1.0.0_lesson_10__the_open_reading__开_001_L1",
    )
    version: str = "1.0.0"
