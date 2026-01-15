"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008903
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
    semantic_id="lt_v1.0.0_lesson_18__creating_the_story__001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Lesson18CreatingTheStory(SemanticEntry):
    """
    **Source Text** (Lines 1019-1034, 59): Creating the Story - pull everything together spontaneously. ...
    """
    
    original_text: str = """**Source Text** (Lines 1019-1034, 59): Creating the Story - pull everything together spontaneously. Speak out loud. Story gathers strength and power as it is spoken.

**English Paraphrase**: **Creating the Story** means pulling everything together spontaneously. "Let that analytical approach go. Your story will be more authentic if it arises freely from within." Speak out loud—"Your story will gather strength and power as it is spoken." If you ramble, "simply pause, regroup, and start again."

**Complete Chinese Interpretation**: **创建故事**意味着自发地整合一切。"放下分析方法。如果你的故事从内心自由涌现，它会更加真实。"大声说出来——"你的故事在被讲述时会积聚力量和能量。"如果你跑题了，"只需暂停，重新组织，再开始。"

**Story Creation Method**:
1. Let analytical approach go
2. Story arises freely from within
3. Speak out loud (writing too slow, thinking too vague)
4. If rambling, pause, regroup, start again
5. May want to tape and play back

**Summary Statement**: Distill main theme in 1-2 sentences

**Narrative Snippets**:
- `[ns_ltt_152]` `[trigger: story_creation]` `[factor_trigger: tarot_story]` `[role: 主干]` Story gathers strength when spoken aloud, arises freely from within. → L1026-1034"""
    normalized_text_zh: str = """"""
    subject: str = "Lesson 18: Creating the Story (创建故事)"
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
        l1_anchor="lt_v1.0.0_lesson_18__creating_the_story__001_L1",
    )
    version: str = "1.0.0"
