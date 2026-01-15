"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224582
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
    semantic_id="pit_v1.0.0_sun_conjunct_neptune__流年太阳合本命海_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunConjunctNeptune流年太阳合本命海(SemanticEntry):
    """
    > Day of heightened sensitivity and imagination. May feel dreamy, unfocused. Intuition and psychic s...
    """
    
    original_text: str = """> Day of heightened sensitivity and imagination. May feel dreamy, unfocused. Intuition and psychic sensitivity increased. Good for creative and artistic work. Spiritual pursuits favored. Avoid deception—others may mislead you or you may deceive yourself. Not good day for practical decisions requiring clarity. Compassion for others heightened.

**Narrative Snippets**:
- `[ns_pit_112]` `[trigger: transit_sun_conjunct_natal_neptune]` `[factor_trigger: astro_transit_sun CONJUNCT natal_neptune]` `[role: 主干]` Heightened sensitivity and imagination—dreamy, unfocused. Good for creative/artistic work. Avoid deception. → PIT Ch4 Sun☌Neptune"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Conjunct Neptune (流年太阳合本命海王星)"
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
        l1_anchor="pit_v1.0.0_sun_conjunct_neptune__流年太阳合本命海_001_L1",
    )
    version: str = "1.0.0"
