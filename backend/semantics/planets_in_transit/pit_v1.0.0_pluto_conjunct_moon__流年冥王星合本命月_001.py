"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.238199
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
    semantic_id="pit_v1.0.0_pluto_conjunct_moon__流年冥王星合本命月_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class PlutoConjunctMoon流年冥王星合本命月(SemanticEntry):
    """
    > Intense emotional transformation. Deep psychological patterns surface. May feel emotionally compel...
    """
    
    original_text: str = """> Intense emotional transformation. Deep psychological patterns surface. May feel emotionally compelled. Women/family issues intense. Domestic upheaval possible.

**Narrative Snippets**:
- `[ns_pit_pl018]` `[trigger: transit_pluto_conjunct_natal_moon]` `[factor_trigger: astro_transit_pluto CONJUNCT natal_moon]` `[role: 主干]` Intense emotional transformation. Deep patterns surface. Domestic upheaval possible. → PIT Ch13 Pluto☌Moon"""
    normalized_text_zh: str = """"""
    subject: str = "Pluto Conjunct Moon (流年冥王星合本命月亮)"
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
        l1_anchor="pit_v1.0.0_pluto_conjunct_moon__流年冥王星合本命月_001_L1",
    )
    version: str = "1.0.0"
