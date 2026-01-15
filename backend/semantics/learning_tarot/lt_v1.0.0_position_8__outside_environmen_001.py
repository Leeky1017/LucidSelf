"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.009002
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
    semantic_id="lt_v1.0.0_position_8__outside_environmen_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Position8OutsideEnvironmen(SemanticEntry):
    """
    **Keywords**: Outside Environment • Another's Point of View • Another's Expectations

**Position Mea...
    """
    
    original_text: str = """**Keywords**: Outside Environment • Another's Point of View • Another's Expectations

**Position Meanings**:
- External factors, people around you
- How others see you or situation
- Another person's perspective or expectations

**Narrative Snippets**:
- `[ns_ltt_161]` `[trigger: position_8]` `[factor_trigger: tarot_celtic_8 AND tarot_environment]` `[role: 主干]` Position 8 shows the outside environment: how others see you, the context you operate in, forces beyond your control; compare with Position 7 to see the gap between self-perception and external reality."""
    normalized_text_zh: str = """"""
    subject: str = "Position 8: Outside Environment (外部环境)"
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
        l1_anchor="lt_v1.0.0_position_8__outside_environmen_001_L1",
    )
    version: str = "1.0.0"
