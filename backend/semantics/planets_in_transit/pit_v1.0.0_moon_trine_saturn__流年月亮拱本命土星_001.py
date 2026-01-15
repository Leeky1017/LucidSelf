"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301476
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
    semantic_id="pit_v1.0.0_moon_trine_saturn__流年月亮拱本命土星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonTrineSaturn流年月亮拱本命土星(SemanticEntry):
    """
    > Emotional maturity and stability. Can handle responsibilities well. Good for organizing domestic l...
    """
    
    original_text: str = """> Emotional maturity and stability. Can handle responsibilities well. Good for organizing domestic life. Feel secure and grounded. Practical approach to feelings. Good with elders.

**Narrative Snippets**:
- `[ns_pit_m059]` `[trigger: transit_moon_trine_natal_saturn]` `[factor_trigger: astro_transit_moon TRINE natal_saturn]` `[role: 主干]` Emotional maturity and stability. Handle responsibilities well. Feel secure and grounded. → PIT Ch5 Moon△Saturn"""
    normalized_text_zh: str = """"""
    subject: str = "Moon Trine Saturn (流年月亮拱本命土星)"
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
        l1_anchor="pit_v1.0.0_moon_trine_saturn__流年月亮拱本命土星_001_L1",
    )
    version: str = "1.0.0"
