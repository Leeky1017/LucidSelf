"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008412
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
    semantic_id="lt_v1.0.0_four_of_swords__宝剑四_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class FourOfSwords宝剑四(SemanticEntry):
    """
    **Source Text** (Lines 6308-6364): Keywords: Rest • Contemplation • Quiet Preparation

**English Par...
    """
    
    original_text: str = """**Source Text** (Lines 6308-6364): Keywords: Rest • Contemplation • Quiet Preparation

**English Paraphrase**: **Four of Swords** represents "rest"—recuperation, contemplation, withdrawing to recover, quiet preparation.

**Complete Chinese Interpretation**: **宝剑四**代表"休息"——恢复、沉思、退隐恢复、安静的准备。

**Core Points**: Four of Swords = rest, contemplation, quiet preparation; Recovery; Strategic pause

**Narrative Snippets**:
- `[ns_ltt_095]` `[trigger: four_swords]` `[factor_trigger: tarot_four_swords AND tarot_rest]` `[role: 主干]` Four of Swords depicts the knight in repose within the sanctuary: necessary withdrawal from mental battle to recover strength; not defeat but strategic retreat—the mind requires periods of stillness to integrate what combat has taught."""
    normalized_text_zh: str = """"""
    subject: str = "Four of Swords (宝剑四)"
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
        l1_anchor="lt_v1.0.0_four_of_swords__宝剑四_001_L1",
    )
    version: str = "1.0.0"
