"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008383
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
    semantic_id="lt_v1.0.0_ace_of_swords__宝剑王牌_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class AceOfSwords宝剑王牌(SemanticEntry):
    """
    **Source Text** (Lines 6132-6193): Keywords: Mental Force • Truth • Justice • Fortitude

**English P...
    """
    
    original_text: str = """**Source Text** (Lines 6132-6193): Keywords: Mental Force • Truth • Justice • Fortitude

**English Paraphrase**: **Ace of Swords** is "a symbol of possibility in the area of intelligence, reason, justice, truth, clarity, and fortitude."

**Complete Chinese Interpretation**: **宝剑王牌**是"在智慧、理性、正义、真理、清晰和坚毅领域的可能性象征。"

**Core Points**: Ace of Swords = mental force, truth, justice, fortitude; Clarity of thought; Cutting through

**Narrative Snippets**:
- `[ns_ltt_092]` `[trigger: ace_swords]` `[factor_trigger: tarot_ace_swords]` `[role: 主干]` Ace of Swords represents mental clarity and cutting to truth. → L6132-6140"""
    normalized_text_zh: str = """"""
    subject: str = "Ace of Swords (宝剑王牌)"
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
        l1_anchor="lt_v1.0.0_ace_of_swords__宝剑王牌_001_L1",
    )
    version: str = "1.0.0"
