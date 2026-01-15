"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008484
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
    semantic_id="lt_v1.0.0_ace_of_pentacles__星币王牌_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class AceOfPentacles星币王牌(SemanticEntry):
    """
    **Source Text** (Lines 6707-6768): Keywords: Material Force • Prosperity • Practicality • Trust

**E...
    """
    
    original_text: str = """**Source Text** (Lines 6707-6768): Keywords: Material Force • Prosperity • Practicality • Trust

**English Paraphrase**: **Ace of Pentacles** is "a symbol of possibility in the area of prosperity, abundance, trust, security, and groundedness."

**Complete Chinese Interpretation**: **星币王牌**是"在繁荣、富足、信任、安全和踏实领域的可能性象征。"

**Core Points**: Ace of Pentacles = material force, prosperity, practicality, trust; New material opportunity; Grounded beginning

**Narrative Snippets**:
- `[ns_ltt_102]` `[trigger: ace_pentacles]` `[factor_trigger: tarot_ace_pentacles]` `[role: 主干]` Ace of Pentacles represents material opportunity and prosperity. → L6707-6715"""
    normalized_text_zh: str = """"""
    subject: str = "Ace of Pentacles (星币王牌)"
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
        l1_anchor="lt_v1.0.0_ace_of_pentacles__星币王牌_001_L1",
    )
    version: str = "1.0.0"
