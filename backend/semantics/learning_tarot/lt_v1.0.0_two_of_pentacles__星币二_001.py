"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008493
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
    semantic_id="lt_v1.0.0_two_of_pentacles__星币二_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class TwoOfPentacles星币二(SemanticEntry):
    """
    **Source Text** (Lines 6769-6825): Keywords: Juggling • Flexibility • Fun

**English Paraphrase**: *...
    """
    
    original_text: str = """**Source Text** (Lines 6769-6825): Keywords: Juggling • Flexibility • Fun

**English Paraphrase**: **Two of Pentacles** represents "juggling"—balancing multiple priorities, flexibility, keeping things in motion with fun.

**Complete Chinese Interpretation**: **星币二**代表"兼顾"——平衡多个优先事项、灵活性、有趣地保持事物运转。

**Core Points**: Two of Pentacles = juggling, flexibility, fun; Balancing act; Adaptability

**Narrative Snippets**:
- `[ns_ltt_103]` `[trigger: two_pentacles]` `[factor_trigger: tarot_two_pentacles]` `[role: 主干]` Two of Pentacles represents juggling and flexibility. → L6769-6780"""
    normalized_text_zh: str = """"""
    subject: str = "Two of Pentacles (星币二)"
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
        l1_anchor="lt_v1.0.0_two_of_pentacles__星币二_001_L1",
    )
    version: str = "1.0.0"
