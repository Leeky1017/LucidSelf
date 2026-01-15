"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.009119
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
    semantic_id="lt_v1.0.0_jill_s_third_reading__november_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class JillSThirdReadingNovember(SemanticEntry):
    """
    **Context**: Question Reading after rejection - Jill's father slammed door in her face; mother moved...
    """
    
    original_text: str = """**Context**: Question Reading after rejection - Jill's father slammed door in her face; mother moved in with father.

**Question**: "How will my relationship with my birth mother and birth father develop in the future?"

**Key Cards**:
- **Position 3**: Eight of Swords - RESTRICTION now basis of situation
- **Position 5**: Nine of Wands - Warning to be DEFENSIVE now conscious attitude
- **Position 4**: Four of Wands - CELEBRATION moving into past
- **Position 7**: Ten of Pentacles - Jill longs for SECURE, ORDERLY family
- **Position 8**: The Devil - Parents locked in OBSESSIVE RELATIONSHIP, BONDAGE
- **Position 1**: Eight of Wands - CONCLUSION likely, QUICK ACTION needed
- **Position 6**: Death - Major ENDING approaching
- **Position 10**: The Empress - MOTHERING archetype as resolution
- **Position 9**: Page of Pentacles - Lesson about TRUST and ABILITY TO ACT

**Four Repeat Cards**:
1. Eight of Swords: Position 6 (reading 1) → Position 3 (restriction now foundational)
2. Nine of Wands: Position 9 (reading 2) → Position 5 (warning now conscious)
3. Four of Wands: Position 6 (reading 2) → Position 4 (celebration fading)
4. Page of Pentacles: Position 1 (reading 1) → Position 9 (lesson reinforced)

**Critical Insight**: "No single Cups card" - lessons of love taking form of challenges

**Narrative Snippets**:
- `[ns_ltt_170]` `[trigger: jill_reading_3]` `[factor_trigger: tarot_sample_reading]` `[role: 主干]` Jill's third reading: four repeat cards track energy evolution; no Cups = love lessons through challenges."""
    normalized_text_zh: str = """"""
    subject: str = "Jill's Third Reading (November 1990)"
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
        l1_anchor="lt_v1.0.0_jill_s_third_reading__november_001_L1",
    )
    version: str = "1.0.0"
