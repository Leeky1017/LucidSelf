"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008824
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
    semantic_id="lt_v1.0.0_lesson_11__interpreting_a_sing_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Lesson11InterpretingASing(SemanticEntry):
    """
    **Source Text** (Lines 1206-1274): Four sources of meaning for interpreting a single card.

**Englis...
    """
    
    original_text: str = """**Source Text** (Lines 1206-1274): Four sources of meaning for interpreting a single card.

**English Paraphrase**: Four sources of meaning for a single card: (1) Your **unique response** based on background, personality, state of mind; (2) **Conventional meanings** built up over years; (3) **Position meanings** in the spread; (4) Your **question or life circumstances** as framework. The **"Aha" reaction** signals you're on the right track.

**Complete Chinese Interpretation**: 单牌解读的四个含义来源：(1) 你基于背景、个性、心理状态的**独特反应**；(2) 多年积累的**传统含义**；(3) 牌阵中的**位置含义**；(4) 作为框架的你的**问题或生活环境**。**"Aha"反应**表明你走在正确的轨道上。

**Four Sources of Card Meaning**:
1. **Unique Response**: Your background, personality, state of mind
2. **Conventional Meanings**: Built up over years, vary with teachers
3. **Position Meanings**: Based on spread position
4. **Question/Life Circumstances**: Framework and boundaries

**The "Aha" Reaction**: "When one meaning hits you with particular force, you know you're on the right track."

**Narrative Snippets**:
- `[ns_ltt_140]` `[trigger: four_sources]` `[factor_trigger: tarot_interpretation]` `[role: 主干]` Four sources: unique response, convention, position, question. → L1211-1223
- `[ns_ltt_141]` `[trigger: aha_reaction]` `[factor_trigger: tarot_intuition AND tarot_confirmation]` `[role: 主干依赖]` The 'aha' reaction—sudden recognition, physical sensation of rightness—signals that conscious interpretation has connected with deeper knowing; this felt sense is the primary confirmation mechanism in intuitive reading."""
    normalized_text_zh: str = """"""
    subject: str = "Lesson 11: Interpreting a Single Card (单牌解读)"
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
        l1_anchor="lt_v1.0.0_lesson_11__interpreting_a_sing_001_L1",
    )
    version: str = "1.0.0"
