"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.259871
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
    semantic_id="pit_v1.0.0_venus_conjunct_neptune__流年金星合本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusConjunctNeptune流年金星合本(SemanticEntry):
    """
    > Romantic idealism heightened. Beautiful but possibly illusory love. Good for art, music, spiritual...
    """
    
    original_text: str = """> Romantic idealism heightened. Beautiful but possibly illusory love. Good for art, music, spirituality. Avoid deception.

**Narrative Snippets**:
- `[ns_pit_ve053]` `[trigger: transit_venus_conjunct_natal_neptune]` `[factor_trigger: astro_transit_venus CONJUNCT natal_neptune]` `[role: 主干]` Romantic idealism. Beautiful but possibly illusory. Good for art. → PIT Ch7 Venus☌Neptune"""
    normalized_text_zh: str = """"""
    subject: str = "Venus Conjunct Neptune (流年金星合本命海王星)"
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
        l1_anchor="pit_v1.0.0_venus_conjunct_neptune__流年金星合本_001_L1",
    )
    version: str = "1.0.0"
