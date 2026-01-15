"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.318624
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
    semantic_id="pit_v1.0.0_saturn_opposition_moon__流年土星冲本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SaturnOppositionMoon流年土星冲本(SemanticEntry):
    """
    > Others challenge emotional security. Domestic relationships tested. May feel judged or restricted ...
    """
    
    original_text: str = """> Others challenge emotional security. Domestic relationships tested. May feel judged or restricted by women/family. See where emotional maturity needed.

**Narrative Snippets**:
- `[ns_pit_sa022]` `[trigger: transit_saturn_opposition_natal_moon]` `[factor_trigger: astro_transit_saturn OPPOSITION natal_moon]` `[role: 主干]` Emotional security challenged. Domestic relationships tested. → PIT Ch10 Saturn☍Moon"""
    normalized_text_zh: str = """"""
    subject: str = "Saturn Opposition Moon (流年土星冲本命月亮)"
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
        l1_anchor="pit_v1.0.0_saturn_opposition_moon__流年土星冲本_001_L1",
    )
    version: str = "1.0.0"
