"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.237853
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
    semantic_id="pit_v1.0.0_pluto_in_the_first_house__冥王星过_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class PlutoInTheFirstHouse冥王星过(SemanticEntry):
    """
    **Source Text** (Lines 18771-18794):
> Gradually reshape many aspects of personality. Get in touch w...
    """
    
    original_text: str = """**Source Text** (Lines 18771-18794):
> Gradually reshape many aspects of personality. Get in touch with forces that shaped you. Gain greater control over unconscious drives—subconsciously directed urges, compulsions, irrational impulses. Greater control over how you project personality—relationships more rewarding. But challenges en route. Energies rising to control everything—could make relationships difficult. Chance to be positive or negative force for change. Negative if don't understand yourself—vehicle for blind, irrational ego forces, infantile primitive urges. If understand yourself well, complete rebirth of energy and effectiveness. Fortunately, driven to seek inner dimensions of life—attracted to mysteries and hidden aspects. May lead to astrology, yoga, occult whose purpose is total regeneration of self.

**English Paraphrase**: Reshape personality. Gain control over unconscious drives. Can be positive or negative force for change. If understand self, complete rebirth. Driven to inner dimensions—mysteries, occult, yoga, astrology for self-regeneration.

**Complete Chinese Interpretation**: 重塑人格。获得对无意识驱动的控制。可以成为积极或消极的变革力量。如果理解自我，完全重生。被驱动到内在维度——神秘、神秘学、瑜伽、占星学用于自我重生。

**Narrative Snippets**:
- `[ns_pit_pl001]` `[trigger: pluto_transit_house_1]` `[factor_trigger: astro_house_1 AND astro_identity_transformation]` `[role: 主干]` Reshape personality. Control unconscious drives. Complete rebirth if understand self. → PIT Ch13 Pluto-1H"""
    normalized_text_zh: str = """"""
    subject: str = "Pluto in the First House (冥王星过境第一宫)"
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
        book_id="planets_in_transit",
        chapter="",
        l1_anchor="pit_v1.0.0_pluto_in_the_first_house__冥王星过_001_L1",
    )
    version: str = "1.0.0"
