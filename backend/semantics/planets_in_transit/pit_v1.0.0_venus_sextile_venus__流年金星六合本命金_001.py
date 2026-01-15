"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.259327
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
    semantic_id="pit_v1.0.0_venus_sextile_venus__流年金星六合本命金_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusSextileVenus流年金星六合本命金(SemanticEntry):
    """
    > Pleasant social interactions. Relationships flow easily. Good for enjoyment and relaxation.

**Nar...
    """
    
    original_text: str = """> Pleasant social interactions. Relationships flow easily. Good for enjoyment and relaxation.

**Narrative Snippets**:
- `[ns_pit_ve029]` `[trigger: transit_venus_sextile_natal_venus]` `[factor_trigger: astro_transit_venus SEXTILE natal_venus]` `[role: 主干]` Pleasant social interactions. Relationships flow easily. → PIT Ch7 Venus⚹Venus"""
    normalized_text_zh: str = """"""
    subject: str = "Venus Sextile Venus (流年金星六合本命金星)"
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
        l1_anchor="pit_v1.0.0_venus_sextile_venus__流年金星六合本命金_001_L1",
    )
    version: str = "1.0.0"
