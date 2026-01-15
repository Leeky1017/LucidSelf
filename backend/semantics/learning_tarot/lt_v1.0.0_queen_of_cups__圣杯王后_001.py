"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008643
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
    semantic_id="lt_v1.0.0_queen_of_cups__圣杯王后_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class QueenOfCups圣杯王后(SemanticEntry):
    """
    **Keywords**: Loving • Tenderhearted • Intuitive • Psychic • Spiritual

**English Paraphrase**: **Qu...
    """
    
    original_text: str = """**Keywords**: Loving • Tenderhearted • Intuitive • Psychic • Spiritual

**English Paraphrase**: **Queen of Cups** represents mature emotional mastery—loving, tenderhearted, intuitive, psychic, spiritual.

**Complete Chinese Interpretation**: **圣杯王后**代表成熟的情感掌控——有爱、温柔、直觉、通灵、灵性。

**Narrative Snippets**:
- `[ns_ltt_118]` `[trigger: queen_cups]` `[factor_trigger: tarot_queen_cups AND tarot_psychic]` `[role: 主干]` Queen of Cups holds the covered cup of the unconscious with reverence: she senses what words cannot express, reads the emotional undercurrents others miss; her mastery is receptive rather than active—knowing when to absorb and when to reflect back."""
    normalized_text_zh: str = """"""
    subject: str = "Queen of Cups (圣杯王后)"
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
        l1_anchor="lt_v1.0.0_queen_of_cups__圣杯王后_001_L1",
    )
    version: str = "1.0.0"
