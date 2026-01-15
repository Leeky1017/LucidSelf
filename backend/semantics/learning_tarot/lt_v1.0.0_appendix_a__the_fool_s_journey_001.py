"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.009036
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
    semantic_id="lt_v1.0.0_appendix_a__the_fool_s_journey_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class AppendixATheFoolSJourney(SemanticEntry):
    """
    **Summary**: The 22 Major Arcana cards symbolize stages of inner development from earliest awareness...
    """
    
    original_text: str = """**Summary**: The 22 Major Arcana cards symbolize stages of inner development from earliest awareness (Card 0) to integration and fulfillment (Card 21).

**Key Stages**:
- **Fool (0)**: Beginning, innocence, potential
- **Magician (1) & High Priestess (2)**: Discover polarity (action/nonaction, conscious/unconscious)
- **Empress (3) & Emperor (4)**: Nurturing and authority
- **Hierophant (5) & Lovers (6)**: Group beliefs and personal beliefs
- **Chariot (7)**: Mastery and control
- **Strength (8)**: Soft control, patience
- **Hermit (9)**: Inner search
- **Wheel of Fortune (10)**: Cycles, destiny
- **Justice (11)**: Cause and effect
- **Hanged Man (12)**: Surrender, letting go
- **Death (13)**: Transformation
- **Temperance (14)**: Balance, integration
- **Devil (15)**: Bondage, materialism
- **Tower (16)**: Revelation, breakthrough
- **Star (17)**: Hope, inspiration
- **Moon (18)**: Illusion, fears
- **Sun (19)**: Enlightenment, vitality
- **Judgement (20)**: Rebirth, calling
- **World (21)**: Integration, fulfillment

**Narrative Snippets**:
- `[ns_ltt_164]` `[trigger: fools_journey]` `[factor_trigger: tarot_major_arcana]` `[role: 主干]` Major Arcana = stages of inner development from 0 (awareness) to 21 (fulfillment). → Appendix A"""
    normalized_text_zh: str = """"""
    subject: str = "Appendix A: The Fool's Journey (愚者之旅)"
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
        l1_anchor="lt_v1.0.0_appendix_a__the_fool_s_journey_001_L1",
    )
    version: str = "1.0.0"
