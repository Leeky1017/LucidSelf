"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.318785
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
    semantic_id="pit_v1.0.0_saturn_sextile_jupiter__流年土星六合_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SaturnSextileJupiter流年土星六合(SemanticEntry):
    """
    > Good for building lasting success. Growth supported by discipline. Practical expansion. Business m...
    """
    
    original_text: str = """> Good for building lasting success. Growth supported by discipline. Practical expansion. Business matters favored.

**Narrative Snippets**:
- `[ns_pit_sa039]` `[trigger: transit_saturn_sextile_natal_jupiter]` `[factor_trigger: astro_transit_saturn SEXTILE natal_jupiter]` `[role: 主干]` Good for lasting success. Practical expansion. → PIT Ch10 Saturn⚹Jupiter"""
    normalized_text_zh: str = """"""
    subject: str = "Saturn Sextile Jupiter (流年土星六合本命木星)"
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
        l1_anchor="pit_v1.0.0_saturn_sextile_jupiter__流年土星六合_001_L1",
    )
    version: str = "1.0.0"
