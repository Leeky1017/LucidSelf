"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008402
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
    semantic_id="lt_v1.0.0_three_of_swords__宝剑三_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class ThreeOfSwords宝剑三(SemanticEntry):
    """
    **Source Text** (Lines 6251-6307): Keywords: Heartbreak • Loneliness • Betrayal

**English Paraphras...
    """
    
    original_text: str = """**Source Text** (Lines 6251-6307): Keywords: Heartbreak • Loneliness • Betrayal

**English Paraphrase**: **Three of Swords** represents "heartbreak"—sorrow, loneliness, betrayal, painful separation.

**Complete Chinese Interpretation**: **宝剑三**代表"心碎"——悲伤、孤独、背叛、痛苦的分离。

**Core Points**: Three of Swords = heartbreak, loneliness, betrayal; Sorrow; Painful truth

**Narrative Snippets**:
- `[ns_ltt_094]` `[trigger: three_swords]` `[factor_trigger: tarot_three_swords]` `[role: 主干]` Three of Swords represents heartbreak and painful truth. → L6251-6260"""
    normalized_text_zh: str = """"""
    subject: str = "Three of Swords (宝剑三)"
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
        l1_anchor="lt_v1.0.0_three_of_swords__宝剑三_001_L1",
    )
    version: str = "1.0.0"
