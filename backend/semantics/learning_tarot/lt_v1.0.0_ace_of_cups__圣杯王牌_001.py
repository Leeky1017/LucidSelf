"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008286
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
    semantic_id="lt_v1.0.0_ace_of_cups__圣杯王牌_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class AceOfCups圣杯王牌(SemanticEntry):
    """
    **Source Text** (Lines 5557-5618): Keywords: Emotional Force • Intuition • Intimacy • Love

**Englis...
    """
    
    original_text: str = """**Source Text** (Lines 5557-5618): Keywords: Emotional Force • Intuition • Intimacy • Love

**English Paraphrase**: **Ace of Cups** is "a symbol of possibility in the area of deep feelings, intimacy, attunement, compassion, and love."

**Complete Chinese Interpretation**: **圣杯王牌**是"在深层感情、亲密、协调、同情和爱的领域的可能性象征。"

**Core Points**: Ace of Cups = emotional force, intuition, intimacy, love; New emotional beginning; Heart opening

**Narrative Snippets**:
- `[ns_ltt_082]` `[trigger: ace_cups]` `[factor_trigger: tarot_ace_cups]` `[role: 主干]` Ace of Cups represents possibility in area of deep feelings and love. → L5557-5565"""
    normalized_text_zh: str = """"""
    subject: str = "Ace of Cups (圣杯王牌)"
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
        l1_anchor="lt_v1.0.0_ace_of_cups__圣杯王牌_001_L1",
    )
    version: str = "1.0.0"
