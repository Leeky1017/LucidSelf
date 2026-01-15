"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008926
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
    semantic_id="lt_v1.0.0_position_1__heart_of_the_matte_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Position1HeartOfTheMatte(SemanticEntry):
    """
    **Keywords**: Heart of the Matter • Present Environment (Outer/Inner) • Primary Factor

**Position M...
    """
    
    original_text: str = """**Keywords**: Heart of the Matter • Present Environment (Outer/Inner) • Primary Factor

**Position Meanings**:
- Central issue, major concern, basic worry
- Surrounding circumstances, immediate problem
- Internal factors, emotional state
- Most important element, dominant characteristic

**Narrative Snippets**:
- `[ns_ltt_154]` `[trigger: position_1]` `[factor_trigger: tarot_celtic_1 AND tarot_core]` `[role: 主干]` Position 1 represents the heart of the matter: the central issue around which all other factors orbit; this card is the reading's nucleus—other positions illuminate, qualify, or challenge what it reveals."""
    normalized_text_zh: str = """"""
    subject: str = "Position 1: Heart of the Matter (核心问题)"
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
        l1_anchor="lt_v1.0.0_position_1__heart_of_the_matte_001_L1",
    )
    version: str = "1.0.0"
