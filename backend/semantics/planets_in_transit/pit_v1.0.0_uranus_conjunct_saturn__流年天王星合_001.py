"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.208110
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
    semantic_id="pit_v1.0.0_uranus_conjunct_saturn__流年天王星合_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusConjunctSaturn流年天王星合(SemanticEntry):
    """
    > Change meets structure. Old structures may break down. May feel torn between security and freedom....
    """
    
    original_text: str = """> Change meets structure. Old structures may break down. May feel torn between security and freedom. Can innovate within structure if balance found.

**Narrative Snippets**:
- `[ns_pit_ur043]` `[trigger: transit_uranus_conjunct_natal_saturn]` `[factor_trigger: astro_transit_uranus CONJUNCT natal_saturn]` `[role: 主干]` Change meets structure. Old structures may break. Balance security and freedom. → PIT Ch11 Uranus☌Saturn"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus Conjunct Saturn (流年天王星合本命土星)"
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
        l1_anchor="pit_v1.0.0_uranus_conjunct_saturn__流年天王星合_001_L1",
    )
    version: str = "1.0.0"
