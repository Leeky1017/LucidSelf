"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008717
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
    semantic_id="lt_v1.0.0_queen_of_pentacles__星币王后_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class QueenOfPentacles星币王后(SemanticEntry):
    """
    **Keywords**: Nurturing • Bighearted • Down-to-Earth • Resourceful • Trustworthy

**English Paraphra...
    """
    
    original_text: str = """**Keywords**: Nurturing • Bighearted • Down-to-Earth • Resourceful • Trustworthy

**English Paraphrase**: **Queen of Pentacles** represents mature practical mastery—nurturing, bighearted, down-to-earth, resourceful, trustworthy.

**Complete Chinese Interpretation**: **星币王后**代表成熟的实践掌控——滋养、宽宏大量、脚踏实地、足智多谋、值得信赖。

**Narrative Snippets**:
- `[ns_ltt_126]` `[trigger: queen_pentacles]` `[factor_trigger: tarot_queen_pentacles AND tarot_abundance]` `[role: 主干]` Queen of Pentacles creates abundance through generous nurturing: her garden flourishes because she tends it faithfully; material success as expression of care for physical reality—home, body, earth, and all that requires patient cultivation."""
    normalized_text_zh: str = """"""
    subject: str = "Queen of Pentacles (星币王后)"
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
        l1_anchor="lt_v1.0.0_queen_of_pentacles__星币王后_001_L1",
    )
    version: str = "1.0.0"
