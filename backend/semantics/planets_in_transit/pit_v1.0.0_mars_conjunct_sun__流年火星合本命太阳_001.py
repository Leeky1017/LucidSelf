"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.288095
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
    semantic_id="pit_v1.0.0_mars_conjunct_sun__流年火星合本命太阳_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MarsConjunctSun流年火星合本命太阳(SemanticEntry):
    """
    > Tremendous potentials and definite risks. High energy level can have explosive consequences. Ego e...
    """
    
    original_text: str = """> Tremendous potentials and definite risks. High energy level can have explosive consequences. Ego energies high—stand up for yourself. May get into fights and arguments. Great physical energy—prefer physical work. Restless after mental work. Danger of accidents if reckless. If suppress energy, comes out negatively. Use intelligently to accomplish much.

**Narrative Snippets**:
- `[ns_pit_ma013]` `[trigger: transit_mars_conjunct_natal_sun]` `[factor_trigger: astro_transit_mars CONJUNCT natal_sun]` `[role: 主干]` High ego and physical energy. May argue. Use intelligently to accomplish much. → PIT Ch8 Mars☌Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Mars Conjunct Sun (流年火星合本命太阳)"
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
        l1_anchor="pit_v1.0.0_mars_conjunct_sun__流年火星合本命太阳_001_L1",
    )
    version: str = "1.0.0"
