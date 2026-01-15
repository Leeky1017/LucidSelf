"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.259949
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
    semantic_id="pit_v1.0.0_venus_opposition_neptune__流年金星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusOppositionNeptune流年金星(SemanticEntry):
    """
    > Others may confuse or deceive in love. Relationship illusions become apparent. Good for seeing whe...
    """
    
    original_text: str = """> Others may confuse or deceive in love. Relationship illusions become apparent. Good for seeing where you've been unrealistic.

**Narrative Snippets**:
- `[ns_pit_ve057]` `[trigger: transit_venus_opposition_natal_neptune]` `[factor_trigger: astro_transit_venus OPPOSITION natal_neptune]` `[role: 主干]` Others may deceive. See relationship illusions. → PIT Ch7 Venus☍Neptune"""
    normalized_text_zh: str = """"""
    subject: str = "Venus Opposition Neptune (流年金星冲本命海王星)"
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
        l1_anchor="pit_v1.0.0_venus_opposition_neptune__流年金星_001_L1",
    )
    version: str = "1.0.0"
