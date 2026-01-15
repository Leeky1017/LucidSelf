"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.009014
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
    semantic_id="lt_v1.0.0_position_9__guidance_hopes___f_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Position9GuidanceHopesF(SemanticEntry):
    """
    **Keywords**: Guidance • Key Factor • Hopes and Fears • Overlooked Factor

**Position Meanings**:
- ...
    """
    
    original_text: str = """**Keywords**: Guidance • Key Factor • Hopes and Fears • Overlooked Factor

**Position Meanings**:
- Traditional: hopes and fears
- Guidance card, way to proceed
- Key person, problem, or obstacle
- Element of surprise, overlooked factor

**Narrative Snippets**:
- `[ns_ltt_162]` `[trigger: position_9]` `[factor_trigger: tarot_celtic_9 AND tarot_guidance]` `[role: 主干]` Position 9 is the wildcard: sometimes hopes and fears, sometimes guidance, sometimes the overlooked factor that changes everything; this position requires intuition to interpret because its role shifts reading by reading."""
    normalized_text_zh: str = """"""
    subject: str = "Position 9: Guidance/Hopes & Fears (指导/希望与恐惧)"
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
        l1_anchor="lt_v1.0.0_position_9__guidance_hopes___f_001_L1",
    )
    version: str = "1.0.0"
