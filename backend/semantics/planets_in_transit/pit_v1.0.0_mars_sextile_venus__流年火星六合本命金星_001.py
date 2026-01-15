"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.288284
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
    semantic_id="pit_v1.0.0_mars_sextile_venus__流年火星六合本命金星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MarsSextileVenus流年火星六合本命金星(SemanticEntry):
    """
    > Harmonious blend of passion and love. Good for romance and creativity. Attractive and attracted.

...
    """
    
    original_text: str = """> Harmonious blend of passion and love. Good for romance and creativity. Attractive and attracted.

**Narrative Snippets**:
- `[ns_pit_ma029]` `[trigger: transit_mars_sextile_natal_venus]` `[factor_trigger: astro_transit_mars SEXTILE natal_venus]` `[role: 主干]` Harmonious passion and love. Good for romance. → PIT Ch8 Mars⚹Venus"""
    normalized_text_zh: str = """"""
    subject: str = "Mars Sextile Venus (流年火星六合本命金星)"
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
        l1_anchor="pit_v1.0.0_mars_sextile_venus__流年火星六合本命金星_001_L1",
    )
    version: str = "1.0.0"
