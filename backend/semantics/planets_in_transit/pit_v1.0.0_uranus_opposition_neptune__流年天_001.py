"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.208414
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
    semantic_id="pit_v1.0.0_uranus_opposition_neptune__流年天_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusOppositionNeptune流年天(SemanticEntry):
    """
    > Others may suddenly reveal or shatter illusions. Reality check on dreams. Good for seeing where id...
    """
    
    original_text: str = """> Others may suddenly reveal or shatter illusions. Reality check on dreams. Good for seeing where idealism needs grounding.

**Narrative Snippets**:
- `[ns_pit_ur057]` `[trigger: transit_uranus_opposition_natal_neptune]` `[factor_trigger: astro_transit_uranus OPPOSITION natal_neptune]` `[role: 主干]` Others reveal or shatter illusions. Reality check on dreams. → PIT Ch11 Uranus☍Neptune"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus Opposition Neptune (流年天王星冲本命海王星)"
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
        l1_anchor="pit_v1.0.0_uranus_opposition_neptune__流年天_001_L1",
    )
    version: str = "1.0.0"
