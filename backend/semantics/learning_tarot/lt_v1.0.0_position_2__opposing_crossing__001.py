"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008938
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
    semantic_id="lt_v1.0.0_position_2__opposing_crossing__001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Position2OpposingCrossing(SemanticEntry):
    """
    **Keywords**: Opposing Factor • Factor for Change • Secondary/Reinforcing Factor

**Position Meaning...
    """
    
    original_text: str = """**Keywords**: Opposing Factor • Factor for Change • Secondary/Reinforcing Factor

**Position Meanings**:
- "That which is crossing you" (traditional)
- Contrary element, source of resistance
- Something out of left field, surprise
- Supporting feature, additional emphasis

**Placement**: Rotate card 90° clockwise, lay on top of Card 1

**Narrative Snippets**:
- `[ns_ltt_155]` `[trigger: position_2]` `[factor_trigger: tarot_celtic_2]` `[role: 主干]` Position 2 = opposing/crossing factor, that which crosses you."""
    normalized_text_zh: str = """"""
    subject: str = "Position 2: Opposing/Crossing Factor (交叉因素)"
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
        l1_anchor="lt_v1.0.0_position_2__opposing_crossing__001_L1",
    )
    version: str = "1.0.0"
