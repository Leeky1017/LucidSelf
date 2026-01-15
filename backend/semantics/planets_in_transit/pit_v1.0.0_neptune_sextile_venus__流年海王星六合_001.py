"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.272887
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
    semantic_id="pit_v1.0.0_neptune_sextile_venus__流年海王星六合_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneSextileVenus流年海王星六合(SemanticEntry):
    """
    > Pleasant romantic and artistic inspiration. Compassion in relationships. Good for creative express...
    """
    
    original_text: str = """> Pleasant romantic and artistic inspiration. Compassion in relationships. Good for creative expression and spiritual love.

**Narrative Snippets**:
- `[ns_pit_ne029]` `[trigger: transit_neptune_sextile_natal_venus]` `[factor_trigger: astro_transit_neptune SEXTILE natal_venus]` `[role: 主干]` Pleasant romantic/artistic inspiration. Compassion in relationships. → PIT Ch12 Neptune⚹Venus"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune Sextile Venus (流年海王星六合本命金星)"
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
        l1_anchor="pit_v1.0.0_neptune_sextile_venus__流年海王星六合_001_L1",
    )
    version: str = "1.0.0"
