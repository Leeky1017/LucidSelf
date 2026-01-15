"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.009060
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
    semantic_id="lt_v1.0.0_appendix_c__suit_pair_meanings_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class AppendixCSuitPairMeanings(SemanticEntry):
    """
    **Summary**: When two suits appear together, they create dynamic tensions.

**Wands/Cups**: Outer/In...
    """
    
    original_text: str = """**Summary**: When two suits appear together, they create dynamic tensions.

**Wands/Cups**: Outer/Inner, Aggressive/Passive, Actions/Feelings
**Wands/Swords**: Hot/Cool, Charisma/Authority, Inspiration/Analysis
**Wands/Pentacles**: New/Old, Risk/Security, Fast/Slow
**Cups/Swords**: Feelings/Thoughts, Heart/Head, Emotion/Logic
**Cups/Pentacles**: Spirit/Matter, Fantasy/Reality, Romantic/Practical
**Swords/Pentacles**: Theory/Practice, Ideas/Implementation, Perfection/Compromise

**Narrative Snippets**:
- `[ns_ltt_166]` `[trigger: suit_pairs]` `[factor_trigger: tarot_suit_pairs]` `[role: 主干]` Suit pairs create dynamic tensions: Wands/Cups = outer/inner, etc. → Appendix C"""
    normalized_text_zh: str = """"""
    subject: str = "Appendix C: Suit Pair Meanings (花色配对含义)"
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
        l1_anchor="lt_v1.0.0_appendix_c__suit_pair_meanings_001_L1",
    )
    version: str = "1.0.0"
