"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.009096
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
    semantic_id="lt_v1.0.0_jill_s_first_reading__january__001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class JillSFirstReadingJanuary(SemanticEntry):
    """
    **Context**: Open Reading for Jill, an adoptee seeking information about her birth parents.

**Key C...
    """
    
    original_text: str = """**Context**: Open Reading for Jill, an adoptee seeking information about her birth parents.

**Key Cards**:
- **Position 3 (Root Cause)**: Three of Swords - HEARTBREAK and LONELINESS of separation
- **Position 1**: Page of Pentacles - Focus on PRACTICAL matters for legal case
- **Position 2**: Knight of Cups - UNREALISTIC dreams, OVERLY ROMANTIC hopes
- **Position 4**: Queen of Cups - The "dream mother" Jill hopes to find
- **Position 7**: King of Swords - Jill as agent of HONESTY and JUSTICE
- **Position 8**: Knight of Pentacles - Others see Jill as TOO OBSESSED
- **Position 9**: Five of Cups - Key lesson about LOSS
- **Position 10**: The Magician - POWER awaiting when she realizes her goal

**Interpretation Insights**:
- Many court cards suggest need for balance
- Cups/Pentacles pair (Cards 1-2) = fantasy vs. reality conflict
- Five of Cups as key: transmuting emotional loss is central lesson
- Magician as only major arcana = extra dimension of power possible

**Narrative Snippets**:
- `[ns_ltt_168]` `[trigger: jill_reading_1]` `[factor_trigger: tarot_sample_reading]` `[role: 主干]` Jill's first reading shows balance needed between fantasy (Cups) and reality (Pentacles)."""
    normalized_text_zh: str = """"""
    subject: str = "Jill's First Reading (January 1990)"
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
        l1_anchor="lt_v1.0.0_jill_s_first_reading__january__001_L1",
    )
    version: str = "1.0.0"
