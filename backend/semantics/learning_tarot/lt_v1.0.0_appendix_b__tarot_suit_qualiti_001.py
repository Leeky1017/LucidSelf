"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.009049
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
    semantic_id="lt_v1.0.0_appendix_b__tarot_suit_qualiti_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class AppendixBTarotSuitQualiti(SemanticEntry):
    """
    **Summary**: Each suit has positive and negative expressions.

**Wands (Fire)**: 
- Positive: advent...
    """
    
    original_text: str = """**Summary**: Each suit has positive and negative expressions.

**Wands (Fire)**: 
- Positive: adventurous, bold, confident, creative, energetic, passionate
- Negative: rash, impulsive, restless, hot-tempered, overconfident

**Cups (Water)**:
- Positive: loving, caring, intuitive, gentle, compassionate, spiritual
- Negative: moody, oversensitive, escapist, melancholic, passive

**Swords (Air)**:
- Positive: honest, analytical, logical, just, clear-headed, ethical
- Negative: cold, critical, detached, judgmental, overbearing

**Pentacles (Earth)**:
- Positive: practical, reliable, hardworking, loyal, resourceful, steady
- Negative: stubborn, materialistic, inflexible, overcautious, pessimistic

**Narrative Snippets**:
- `[ns_ltt_165]` `[trigger: suit_qualities]` `[factor_trigger: tarot_suits AND tarot_polarity]` `[role: 主干]` Each suit contains both light and shadow: Wands can be creative or destructive, Cups nurturing or drowning, Swords clarifying or cutting, Pentacles stable or stagnant—context and surrounding cards determine which pole manifests."""
    normalized_text_zh: str = """"""
    subject: str = "Appendix B: Tarot Suit Qualities (花色品质)"
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
        l1_anchor="lt_v1.0.0_appendix_b__tarot_suit_qualiti_001_L1",
    )
    version: str = "1.0.0"
