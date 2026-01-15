"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.288522
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
    semantic_id="pit_v1.0.0_mars_sextile_uranus__流年火星六合本命天_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MarsSextileUranus流年火星六合本命天(SemanticEntry):
    """
    > Pleasant, exciting energy. Innovation favored. Original actions. Good for breaking routine constru...
    """
    
    original_text: str = """> Pleasant, exciting energy. Innovation favored. Original actions. Good for breaking routine constructively.

**Narrative Snippets**:
- `[ns_pit_ma049]` `[trigger: transit_mars_sextile_natal_uranus]` `[factor_trigger: astro_transit_mars SEXTILE natal_uranus]` `[role: 主干]` Exciting energy. Innovation. Good for breaking routine. → PIT Ch8 Mars⚹Uranus"""
    normalized_text_zh: str = """"""
    subject: str = "Mars Sextile Uranus (流年火星六合本命天王星)"
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
        l1_anchor="pit_v1.0.0_mars_sextile_uranus__流年火星六合本命天_001_L1",
    )
    version: str = "1.0.0"
