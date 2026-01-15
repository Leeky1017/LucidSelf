"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008503
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
    semantic_id="lt_v1.0.0_three_of_pentacles__星币三_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class ThreeOfPentacles星币三(SemanticEntry):
    """
    **Source Text** (Lines 6826-6882): Keywords: Teamwork • Planning • Competence

**English Paraphrase*...
    """
    
    original_text: str = """**Source Text** (Lines 6826-6882): Keywords: Teamwork • Planning • Competence

**English Paraphrase**: **Three of Pentacles** represents "competent work"—teamwork, skilled craftsmanship, planning, collaboration.

**Complete Chinese Interpretation**: **星币三**代表"胜任的工作"——团队合作、熟练的工艺、规划、协作。

**Core Points**: Three of Pentacles = teamwork, planning, competence; Skilled work; Collaboration

**Narrative Snippets**:
- `[ns_ltt_104]` `[trigger: three_pentacles]` `[factor_trigger: tarot_three_pentacles]` `[role: 主干]` Three of Pentacles represents teamwork and competent planning. → L6826-6835"""
    normalized_text_zh: str = """"""
    subject: str = "Three of Pentacles (星币三)"
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
        l1_anchor="lt_v1.0.0_three_of_pentacles__星币三_001_L1",
    )
    version: str = "1.0.0"
