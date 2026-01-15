"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.009129
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
    semantic_id="lt_v1.0.0_lessons_from_jill_s_tale_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class LessonsFromJillSTale(SemanticEntry):
    """
    **Summary**: Three readings over one year demonstrate how tarot reflects life developments.

**Key L...
    """
    
    original_text: str = """**Summary**: Three readings over one year demonstrate how tarot reflects life developments.

**Key Lessons**:
1. **Repeat cards** show enduring energies and their evolution
2. **Position shifts** reveal how issues move between conscious/unconscious
3. **Court card abundance** signals need for balance
4. **Missing suits** can be as significant as present ones
5. **Major arcana cards** carry extra weight in interpretation
6. **Card pairs** (especially Cups/Pentacles) reveal core conflicts

**Interpretation Techniques Demonstrated**:
- Tracking cards across multiple readings
- Noticing position changes of repeat cards
- Identifying dominant and absent suit energies
- Recognizing archetypal patterns (dream mother → actual mother)
- Reading relationship dynamics through court card combinations

**Narrative Snippets**:
- `[ns_ltt_171]` `[trigger: jill_lessons]` `[factor_trigger: tarot_interpretation]` `[role: 主干]` Jill's tale teaches: track repeat cards, note position shifts, absent suits are significant."""
    normalized_text_zh: str = """"""
    subject: str = "Lessons from Jill's Tale"
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
        l1_anchor="lt_v1.0.0_lessons_from_jill_s_tale_001_L1",
    )
    version: str = "1.0.0"
