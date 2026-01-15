"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.272878
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
    semantic_id="pit_v1.0.0_neptune_conjunct_venus__流年海王星合_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneConjunctVenus流年海王星合(SemanticEntry):
    """
    > Romantic idealism heightened. May seek soulmate or spiritual love. Artistic inspiration enhanced. ...
    """
    
    original_text: str = """> Romantic idealism heightened. May seek soulmate or spiritual love. Artistic inspiration enhanced. Financial confusion possible. Avoid escapism through love.

**Narrative Snippets**:
- `[ns_pit_ne028]` `[trigger: transit_neptune_conjunct_natal_venus]` `[factor_trigger: astro_transit_neptune CONJUNCT natal_venus]` `[role: 主干]` Romantic idealism. Seek spiritual love. Artistic inspiration. Financial confusion. → PIT Ch12 Neptune☌Venus"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune Conjunct Venus (流年海王星合本命金星)"
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
        l1_anchor="pit_v1.0.0_neptune_conjunct_venus__流年海王星合_001_L1",
    )
    version: str = "1.0.0"
