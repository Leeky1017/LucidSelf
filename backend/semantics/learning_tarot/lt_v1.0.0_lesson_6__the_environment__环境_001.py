"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008763
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
    semantic_id="lt_v1.0.0_lesson_6__the_environment__环境_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Lesson6TheEnvironment环境(SemanticEntry):
    """
    **Source Text** (Lines 723-785): The environment includes physical setting and internal state. Five ...
    """
    
    original_text: str = """**Source Text** (Lines 723-785): The environment includes physical setting and internal state. Five inner qualities are beneficial: Being Open, Being Calm, Being Focused, Being Alert, Being Respectful.

**English Paraphrase**: The **environment** includes "the physical setting and your internal state." Five inner qualities are beneficial: **Being Open** (receptive, allowing), **Being Calm** (like a peaceful sea), **Being Focused** (strong desire produces direct message), **Being Alert** (all faculties alive), **Being Respectful** (treating cards as valued tool).

**Complete Chinese Interpretation**: **环境**包括"物理环境和你的内在状态。"五种有益的内在品质：**开放**（接受性、允许性）、**平静**（如平静的大海）、**专注**（强烈的愿望产生直接的信息）、**警觉**（所有能力都活跃）、**尊重**（将牌作为有价值的工具对待）。

**Five Inner Qualities**:
1. **Being Open** (开放): Receptive, allowing, willing to receive
2. **Being Calm** (平静): Peaceful sea where ripples of insight can be perceived
3. **Being Focused** (专注): Strong question = direct and powerful message
4. **Being Alert** (警觉): All faculties alive and awake
5. **Being Respectful** (尊重): Treating cards as valued tool

**Narrative Snippets**:
- `[ns_ltt_132]` `[trigger: five_qualities]` `[factor_trigger: tarot_environment]` `[role: 主干]` Five inner qualities: Open, Calm, Focused, Alert, Respectful. → L726-744
- `[ns_ltt_133]` `[trigger: tarot_spot]` `[factor_trigger: tarot_space AND tarot_ritual]` `[role: 辅助]` Designate a consistent physical location for tarot practice: repeated use builds associative energy; the mind shifts into receptive mode upon entering the space, just as sleep comes easier in a bed used only for sleeping."""
    normalized_text_zh: str = """"""
    subject: str = "Lesson 6: The Environment (环境)"
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
        l1_anchor="lt_v1.0.0_lesson_6__the_environment__环境_001_L1",
    )
    version: str = "1.0.0"
