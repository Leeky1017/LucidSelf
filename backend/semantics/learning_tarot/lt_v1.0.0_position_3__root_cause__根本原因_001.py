"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008948
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
    semantic_id="lt_v1.0.0_position_3__root_cause__根本原因_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Position3RootCause根本原因(SemanticEntry):
    """
    **Keywords**: Root Cause • Unconscious Influence • Deeper Meaning

**Position Meanings**:
- "That wh...
    """
    
    original_text: str = """**Keywords**: Root Cause • Unconscious Influence • Deeper Meaning

**Position Meanings**:
- "That which is beneath you" (traditional)
- Source of problem, basis of situation
- Unrecognized motivations, unacknowledged goals
- Most basic impulses, driving needs

**Narrative Snippets**:
- `[ns_ltt_156]` `[trigger: position_3]` `[factor_trigger: tarot_celtic_3 AND tarot_unconscious]` `[role: 主干]` Position 3 reveals what lies beneath: the root cause, unconscious influence, or foundation you may not consciously recognize; this card often holds the key insight because it shows what you cannot or will not see."""
    normalized_text_zh: str = """"""
    subject: str = "Position 3: Root Cause (根本原因)"
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
        l1_anchor="lt_v1.0.0_position_3__root_cause__根本原因_001_L1",
    )
    version: str = "1.0.0"
