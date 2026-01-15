"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.009108
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
    semantic_id="lt_v1.0.0_jill_s_second_reading__june_19_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class JillSSecondReadingJune19(SemanticEntry):
    """
    **Context**: Other Reading after dramatic events - Jill found both birth parents, and they rekindled...
    """
    
    original_text: str = """**Context**: Other Reading after dramatic events - Jill found both birth parents, and they rekindled their romance.

**Key Cards**:
- **Position 1**: Page of Swords - Face CHALLENGE with FORTITUDE and CLARITY
- **Position 2**: Four of Swords - EXAMINE ACTIONS AND tarot_MOTIVATIONS, nurture still center
- **Position 5**: Queen of Cups - Dream mother now in conscious mind
- **Position 3**: Five of Cups - LOSS now lodged in unconscious
- **Position 4**: Three of Pentacles - TEAMWORK may become thing of past
- **Position 7**: The Lovers - Jill wants to forge bonds of LOVE
- **Position 8**: The Moon - Environment of FEAR and ILLUSION
- **Position 10**: Five of Pentacles - Possible REJECTION ahead
- **Position 9**: Nine of Wands - Be DEFENSIVE, prepare for worst

**Interpretation Insights**:
- Links to first reading: Five of Cups moved from position 9 to position 3
- Major arcana in positions 7-8 carry extra weight
- Lovers vs. Moon = Jill's hopes vs. unclear environment
- No willful deceit, just lack of clarity

**Narrative Snippets**:
- `[ns_ltt_169]` `[trigger: jill_reading_2]` `[factor_trigger: tarot_sample_reading]` `[role: 主干]` Jill's second reading shows repeat cards tracking energy shifts; Five of Cups moved deeper."""
    normalized_text_zh: str = """"""
    subject: str = "Jill's Second Reading (June 1990)"
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
        l1_anchor="lt_v1.0.0_jill_s_second_reading__june_19_001_L1",
    )
    version: str = "1.0.0"
