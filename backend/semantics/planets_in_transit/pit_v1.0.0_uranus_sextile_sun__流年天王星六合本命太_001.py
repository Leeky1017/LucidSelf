"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.207097
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
    semantic_id="pit_v1.0.0_uranus_sextile_sun__流年天王星六合本命太_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusSextileSun流年天王星六合本命太(SemanticEntry):
    """
    > Pleasant opportunities for change and freedom. New experiences enhance identity. Good for innovati...
    """
    
    original_text: str = """> Pleasant opportunities for change and freedom. New experiences enhance identity. Good for innovation and self-expression. Changes come more easily.

**Narrative Snippets**:
- `[ns_pit_ur014]` `[trigger: transit_uranus_sextile_natal_sun]` `[factor_trigger: astro_transit_uranus SEXTILE natal_sun]` `[role: 主干]` Pleasant change opportunities. Innovation and self-expression. → PIT Ch11 Uranus⚹Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus Sextile Sun (流年天王星六合本命太阳)"
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
        l1_anchor="pit_v1.0.0_uranus_sextile_sun__流年天王星六合本命太_001_L1",
    )
    version: str = "1.0.0"
