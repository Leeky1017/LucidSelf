"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.238447
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
    semantic_id="pit_v1.0.0_pluto_trine_venus__流年冥王星拱本命金星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class PlutoTrineVenus流年冥王星拱本命金星(SemanticEntry):
    """
    > Excellent for deep love transformation. Passion flows positively. Values regenerate. Financial pow...
    """
    
    original_text: str = """> Excellent for deep love transformation. Passion flows positively. Values regenerate. Financial power available constructively.

**Narrative Snippets**:
- `[ns_pit_pl031]` `[trigger: transit_pluto_trine_natal_venus]` `[factor_trigger: astro_transit_pluto TRINE natal_venus]` `[role: 主干]` Excellent for deep love transformation. Passion flows positively. → PIT Ch13 Pluto△Venus"""
    normalized_text_zh: str = """"""
    subject: str = "Pluto Trine Venus (流年冥王星拱本命金星)"
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
        l1_anchor="pit_v1.0.0_pluto_trine_venus__流年冥王星拱本命金星_001_L1",
    )
    version: str = "1.0.0"
