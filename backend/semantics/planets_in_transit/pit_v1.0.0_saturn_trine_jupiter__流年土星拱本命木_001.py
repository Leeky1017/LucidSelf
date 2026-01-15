"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.318803
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
    semantic_id="pit_v1.0.0_saturn_trine_jupiter__流年土星拱本命木_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SaturnTrineJupiter流年土星拱本命木(SemanticEntry):
    """
    > Excellent for building lasting success. Growth supported by structure. Business, career, practical...
    """
    
    original_text: str = """> Excellent for building lasting success. Growth supported by structure. Business, career, practical matters excel.

**Narrative Snippets**:
- `[ns_pit_sa041]` `[trigger: transit_saturn_trine_natal_jupiter]` `[factor_trigger: astro_transit_saturn TRINE natal_jupiter]` `[role: 主干]` Excellent for lasting success. Growth with structure. → PIT Ch10 Saturn△Jupiter"""
    normalized_text_zh: str = """"""
    subject: str = "Saturn Trine Jupiter (流年土星拱本命木星)"
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
        l1_anchor="pit_v1.0.0_saturn_trine_jupiter__流年土星拱本命木_001_L1",
    )
    version: str = "1.0.0"
