"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008603
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
    semantic_id="lt_v1.0.0_queen_of_wands__权杖王后_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class QueenOfWands权杖王后(SemanticEntry):
    """
    **Keywords**: Attractive • Wholehearted • Energetic • Cheerful • Self-Assured

**English Paraphrase*...
    """
    
    original_text: str = """**Keywords**: Attractive • Wholehearted • Energetic • Cheerful • Self-Assured

**English Paraphrase**: **Queen of Wands** represents mature creative mastery—attractive, wholehearted, energetic, cheerful, self-assured.

**Complete Chinese Interpretation**: **权杖王后**代表成熟的创造性掌控——有魅力、全心全意、精力充沛、开朗、自信。

**Narrative Snippets**:
- `[ns_ltt_114]` `[trigger: queen_wands]` `[factor_trigger: tarot_queen_wands AND tarot_mastery]` `[role: 主干]` Queen of Wands wields creative fire with mature skill: she inspires without consuming, leads without dominating; her warmth draws others in while her self-possession maintains healthy boundaries—passion refined by experience."""
    normalized_text_zh: str = """"""
    subject: str = "Queen of Wands (权杖王后)"
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
        l1_anchor="lt_v1.0.0_queen_of_wands__权杖王后_001_L1",
    )
    version: str = "1.0.0"
