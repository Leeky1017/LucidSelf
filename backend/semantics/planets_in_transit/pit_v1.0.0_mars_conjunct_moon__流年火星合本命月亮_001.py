"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.288145
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
    semantic_id="pit_v1.0.0_mars_conjunct_moon__流年火星合本命月亮_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MarsConjunctMoon流年火星合本命月亮(SemanticEntry):
    """
    > Emotional intensity. May feel irritable or touchy. React strongly to perceived slights. Sexual fee...
    """
    
    original_text: str = """> Emotional intensity. May feel irritable or touchy. React strongly to perceived slights. Sexual feelings heightened. Good for clearing emotional air. Physical activity helps.

**Narrative Snippets**:
- `[ns_pit_ma018]` `[trigger: transit_mars_conjunct_natal_moon]` `[factor_trigger: astro_transit_mars CONJUNCT natal_moon]` `[role: 主干]` Emotional intensity. Irritable. Sexual feelings heightened. Clear emotional air. → PIT Ch8 Mars☌Moon"""
    normalized_text_zh: str = """"""
    subject: str = "Mars Conjunct Moon (流年火星合本命月亮)"
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
        l1_anchor="pit_v1.0.0_mars_conjunct_moon__流年火星合本命月亮_001_L1",
    )
    version: str = "1.0.0"
