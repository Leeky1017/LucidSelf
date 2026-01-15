"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008958
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
    semantic_id="lt_v1.0.0_position_4__past__过去_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Position4Past过去(SemanticEntry):
    """
    **Keywords**: Past • Receding Influence • Quality to Let Go

**Position Meanings**:
- Something movi...
    """
    
    original_text: str = """**Keywords**: Past • Receding Influence • Quality to Let Go

**Position Meanings**:
- Something moving away, already experienced
- To be released, resolved factor
- Childhood or past life (karmic) influence

**Narrative Snippets**:
- `[ns_ltt_157]` `[trigger: position_4]` `[factor_trigger: tarot_celtic_4 AND tarot_past]` `[role: 主干]` Position 4 shows what is passing away: the receding influence, completed phase, or quality whose time has ended; this card indicates what to release rather than cling to—its energy is moving out of your life."""
    normalized_text_zh: str = """"""
    subject: str = "Position 4: Past (过去)"
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
        l1_anchor="lt_v1.0.0_position_4__past__过去_001_L1",
    )
    version: str = "1.0.0"
