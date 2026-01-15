"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.272777
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
    semantic_id="pit_v1.0.0_neptune_conjunct_moon__流年海王星合本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneConjunctMoon流年海王星合本(SemanticEntry):
    """
    > Emotional sensitivity heightened. May feel vulnerable, confused emotionally. Psychic impressions i...
    """
    
    original_text: str = """> Emotional sensitivity heightened. May feel vulnerable, confused emotionally. Psychic impressions increase. Domestic life may be confusing. Compassion for family. Possible deception in emotions.

**Narrative Snippets**:
- `[ns_pit_ne018]` `[trigger: transit_neptune_conjunct_natal_moon]` `[factor_trigger: astro_transit_neptune CONJUNCT natal_moon]` `[role: 主干]` Emotional sensitivity heightened. May feel vulnerable. Psychic impressions. Domestic confusion. → PIT Ch12 Neptune☌Moon"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune Conjunct Moon (流年海王星合本命月亮)"
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
        l1_anchor="pit_v1.0.0_neptune_conjunct_moon__流年海王星合本_001_L1",
    )
    version: str = "1.0.0"
