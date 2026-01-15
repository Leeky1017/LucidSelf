"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008522
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
    semantic_id="lt_v1.0.0_five_of_pentacles__星币五_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class FiveOfPentacles星币五(SemanticEntry):
    """
    **Source Text** (Lines 6940-6996): Keywords: Hard Times • Ill Health • Rejection

**English Paraphra...
    """
    
    original_text: str = """**Source Text** (Lines 6940-6996): Keywords: Hard Times • Ill Health • Rejection

**English Paraphrase**: **Five of Pentacles** represents "hard times"—poverty, ill health, rejection, feeling left out in the cold.

**Complete Chinese Interpretation**: **星币五**代表"艰难时期"——贫穷、健康不佳、被拒绝、感到被遗弃在寒冷中。

**Core Points**: Five of Pentacles = hard times, ill health, rejection; Material difficulty; Feeling excluded

**Narrative Snippets**:
- `[ns_ltt_106]` `[trigger: five_pentacles]` `[factor_trigger: tarot_five_pentacles]` `[role: 主干]` Five of Pentacles represents hard times and material difficulty. → L6940-6950"""
    normalized_text_zh: str = """"""
    subject: str = "Five of Pentacles (星币五)"
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
        l1_anchor="lt_v1.0.0_five_of_pentacles__星币五_001_L1",
    )
    version: str = "1.0.0"
