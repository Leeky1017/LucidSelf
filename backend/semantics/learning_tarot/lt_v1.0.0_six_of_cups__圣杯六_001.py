"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008336
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
    semantic_id="lt_v1.0.0_six_of_cups__圣杯六_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class SixOfCups圣杯六(SemanticEntry):
    """
    **Source Text** (Lines 5847-5903): Keywords: Good Will • Innocence • Childhood

**English Paraphrase...
    """
    
    original_text: str = """**Source Text** (Lines 5847-5903): Keywords: Good Will • Innocence • Childhood

**English Paraphrase**: **Six of Cups** represents "nostalgia and innocence"—childhood memories, good will, simple pleasures, sharing.

**Complete Chinese Interpretation**: **圣杯六**代表"怀旧和纯真"——童年记忆、善意、简单的快乐、分享。

**Core Points**: Six of Cups = good will, innocence, childhood; Nostalgia; Simple joys

**Narrative Snippets**:
- `[ns_ltt_087]` `[trigger: six_cups]` `[factor_trigger: tarot_six_cups AND tarot_memory]` `[role: 主干]` Six of Cups evokes childhood's emotional simplicity: the larger figure offering a cup to the smaller recalls innocent generosity before calculation entered relationships; nostalgia can heal or trap depending on whether memory inspires or replaces present living."""
    normalized_text_zh: str = """"""
    subject: str = "Six of Cups (圣杯六)"
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
        l1_anchor="lt_v1.0.0_six_of_cups__圣杯六_001_L1",
    )
    version: str = "1.0.0"
