"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008296
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
    semantic_id="lt_v1.0.0_two_of_cups__圣杯二_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class TwoOfCups圣杯二(SemanticEntry):
    """
    **Source Text** (Lines 5619-5675): Keywords: Connection • Truce • Attraction

**English Paraphrase**...
    """
    
    original_text: str = """**Source Text** (Lines 5619-5675): Keywords: Connection • Truce • Attraction

**English Paraphrase**: **Two of Cups** represents "connection"—union of two, partnership, mutual attraction, making peace.

**Complete Chinese Interpretation**: **圣杯二**代表"连接"——两者的结合、伙伴关系、相互吸引、和解。

**Core Points**: Two of Cups = connection, truce, attraction; Partnership; Mutual bond

**Narrative Snippets**:
- `[ns_ltt_083]` `[trigger: two_cups]` `[factor_trigger: tarot_two_cups AND tarot_partnership]` `[role: 主干]` Two of Cups shows two people exchanging cups in mutual recognition: the alchemy of genuine connection where each sees and values the other; partnership formed not from need but from appreciation—the foundation of healthy relationship."""
    normalized_text_zh: str = """"""
    subject: str = "Two of Cups (圣杯二)"
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
        l1_anchor="lt_v1.0.0_two_of_cups__圣杯二_001_L1",
    )
    version: str = "1.0.0"
