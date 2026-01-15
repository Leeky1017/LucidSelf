"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008392
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
    semantic_id="lt_v1.0.0_two_of_swords__宝剑二_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class TwoOfSwords宝剑二(SemanticEntry):
    """
    **Source Text** (Lines 6194-6250): Keywords: Blocked Emotions • Avoidance • Stalemate

**English Par...
    """
    
    original_text: str = """**Source Text** (Lines 6194-6250): Keywords: Blocked Emotions • Avoidance • Stalemate

**English Paraphrase**: **Two of Swords** represents "blocked emotions"—refusing to see, avoidance, stalemate, being at an impasse.

**Complete Chinese Interpretation**: **宝剑二**代表"被阻塞的情感"——拒绝看到、回避、僵局、陷入僵局。

**Core Points**: Two of Swords = blocked emotions, avoidance, stalemate; Denial; Impasse

**Narrative Snippets**:
- `[ns_ltt_093]` `[trigger: two_swords]` `[factor_trigger: tarot_two_swords AND tarot_denial]` `[role: 主干]` Two of Swords shows the blindfolded figure holding crossed swords: refusing to see or choose, maintaining tense stalemate through willful denial; the temporary peace of avoidance that prevents both conflict and resolution."""
    normalized_text_zh: str = """"""
    subject: str = "Two of Swords (宝剑二)"
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
        l1_anchor="lt_v1.0.0_two_of_swords__宝剑二_001_L1",
    )
    version: str = "1.0.0"
