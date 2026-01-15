"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.207843
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
    semantic_id="pit_v1.0.0_uranus_sextile_mars__流年天王星六合本命_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusSextileMars流年天王星六合本命(SemanticEntry):
    """
    > Pleasant exciting energy. Innovation in action. Good for breaking routine constructively. Physical...
    """
    
    original_text: str = """> Pleasant exciting energy. Innovation in action. Good for breaking routine constructively. Physical activity enhanced.

**Narrative Snippets**:
- `[ns_pit_ur034]` `[trigger: transit_uranus_sextile_natal_mars]` `[factor_trigger: astro_transit_uranus SEXTILE natal_mars]` `[role: 主干]` Exciting energy. Innovation. Good for breaking routine. → PIT Ch11 Uranus⚹Mars"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus Sextile Mars (流年天王星六合本命火星)"
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
        l1_anchor="pit_v1.0.0_uranus_sextile_mars__流年天王星六合本命_001_L1",
    )
    version: str = "1.0.0"
