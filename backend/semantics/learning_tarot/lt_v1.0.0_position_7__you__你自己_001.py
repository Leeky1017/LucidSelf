"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008992
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
    semantic_id="lt_v1.0.0_position_7__you__你自己_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Position7You你自己(SemanticEntry):
    """
    **Keywords**: You as You Are • You as You Could Be • You as You Present Yourself

**Position Meaning...
    """
    
    original_text: str = """**Keywords**: You as You Are • You as You Could Be • You as You Present Yourself

**Position Meanings**:
- How you see yourself in this situation
- Aspect of yourself relevant to question
- How you are presenting yourself to others

**Narrative Snippets**:
- `[ns_ltt_160]` `[trigger: position_7]` `[factor_trigger: tarot_celtic_7 AND tarot_self]` `[role: 主干]` Position 7 reflects who you are being: your self-image, the face you present, the role you've assumed in this situation; compare with Position 1 to see if you're aligned with reality or playing a part."""
    normalized_text_zh: str = """"""
    subject: str = "Position 7: You (你自己)"
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
        l1_anchor="lt_v1.0.0_position_7__you__你自己_001_L1",
    )
    version: str = "1.0.0"
