"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.259120
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
    semantic_id="pit_v1.0.0_venus_sextile_moon__流年金星六合本命月亮_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusSextileMoon流年金星六合本命月亮(SemanticEntry):
    """
    > Emotions softened. Difficult to feel anger. Protective and nurturing toward friends. Keep things r...
    """
    
    original_text: str = """> Emotions softened. Difficult to feel anger. Protective and nurturing toward friends. Keep things running smoothly. Relations with women very good. Best expressed at home. One of finest transits to relax. Warmth projects favorably in public dealings.

**Narrative Snippets**:
- `[ns_pit_ve019]` `[trigger: transit_venus_sextile_natal_moon]` `[factor_trigger: astro_transit_venus SEXTILE natal_moon]` `[role: 主干]` Emotions softened. Protective. Good with women. Best at home to relax. → PIT Ch7 Venus⚹Moon"""
    normalized_text_zh: str = """"""
    subject: str = "Venus Sextile Moon (流年金星六合本命月亮)"
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
        l1_anchor="pit_v1.0.0_venus_sextile_moon__流年金星六合本命月亮_001_L1",
    )
    version: str = "1.0.0"
