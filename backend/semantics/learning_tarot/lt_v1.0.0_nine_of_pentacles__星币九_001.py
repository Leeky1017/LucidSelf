"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008560
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
    semantic_id="lt_v1.0.0_nine_of_pentacles__星币九_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class NineOfPentacles星币九(SemanticEntry):
    """
    **Source Text** (Lines 7168-7224): Keywords: Discipline • Self-Reliance • Refinement

**English Para...
    """
    
    original_text: str = """**Source Text** (Lines 7168-7224): Keywords: Discipline • Self-Reliance • Refinement

**English Paraphrase**: **Nine of Pentacles** represents "self-reliance"—independence, refinement, enjoying the fruits of your labor.

**Complete Chinese Interpretation**: **星币九**代表"自力更生"——独立、精致、享受你劳动的成果。

**Core Points**: Nine of Pentacles = discipline, self-reliance, refinement; Independence; Enjoying success

**Narrative Snippets**:
- `[ns_ltt_110]` `[trigger: nine_pentacles]` `[factor_trigger: tarot_nine_pentacles]` `[role: 主干]` Nine of Pentacles represents self-reliance and enjoying success. → L7168-7175"""
    normalized_text_zh: str = """"""
    subject: str = "Nine of Pentacles (星币九)"
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
        l1_anchor="lt_v1.0.0_nine_of_pentacles__星币九_001_L1",
    )
    version: str = "1.0.0"
