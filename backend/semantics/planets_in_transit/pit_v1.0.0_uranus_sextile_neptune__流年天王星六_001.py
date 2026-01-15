"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.208351
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
    semantic_id="pit_v1.0.0_uranus_sextile_neptune__流年天王星六_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusSextileNeptune流年天王星六(SemanticEntry):
    """
    > Pleasant spiritual/creative expansion. Inspiration flows. Good for innovative art and spirituality...
    """
    
    original_text: str = """> Pleasant spiritual/creative expansion. Inspiration flows. Good for innovative art and spirituality.

**Narrative Snippets**:
- `[ns_pit_ur054]` `[trigger: transit_uranus_sextile_natal_neptune]` `[factor_trigger: astro_transit_uranus SEXTILE natal_neptune]` `[role: 主干]` Pleasant spiritual expansion. Inspiration flows. → PIT Ch11 Uranus⚹Neptune"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus Sextile Neptune (流年天王星六合本命海王星)"
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
        l1_anchor="pit_v1.0.0_uranus_sextile_neptune__流年天王星六_001_L1",
    )
    version: str = "1.0.0"
