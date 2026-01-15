"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.310351
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
    semantic_id="pit_v1.0.0_jupiter_trine_saturn__流年木星拱本命土_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterTrineSaturn流年木星拱本命土(SemanticEntry):
    """
    > Excellent for building lasting success. Growth supported by structure. Business, career, practical...
    """
    
    original_text: str = """> Excellent for building lasting success. Growth supported by structure. Business, career, practical matters excel.

**Narrative Snippets**:
- `[ns_pit_ju046]` `[trigger: transit_jupiter_trine_natal_saturn]` `[factor_trigger: astro_transit_jupiter TRINE natal_saturn]` `[role: 主干]` Excellent for lasting success. Growth with structure. → PIT Ch9 Jupiter△Saturn"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter Trine Saturn (流年木星拱本命土星)"
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
        l1_anchor="pit_v1.0.0_jupiter_trine_saturn__流年木星拱本命土_001_L1",
    )
    version: str = "1.0.0"
