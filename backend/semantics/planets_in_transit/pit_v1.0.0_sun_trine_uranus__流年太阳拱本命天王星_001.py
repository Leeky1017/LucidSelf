"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224562
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
    semantic_id="pit_v1.0.0_sun_trine_uranus__流年太阳拱本命天王星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunTrineUranus流年太阳拱本命天王星(SemanticEntry):
    """
    > Excellent for creative and original work. New insights and ideas flow easily. Pleasant surprises a...
    """
    
    original_text: str = """> Excellent for creative and original work. New insights and ideas flow easily. Pleasant surprises and opportunities. Good day to try new approaches without risk. Friends and groups helpful. Technology and innovation favored. Freedom and independence feel natural.

**Narrative Snippets**:
- `[ns_pit_110]` `[trigger: transit_sun_trine_natal_uranus]` `[factor_trigger: astro_transit_sun TRINE natal_uranus]` `[role: 主干]` Excellent for creative, original work—new insights flow easily. Try new approaches without risk. → PIT Ch4 Sun△Uranus"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Trine Uranus (流年太阳拱本命天王星)"
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
        l1_anchor="pit_v1.0.0_sun_trine_uranus__流年太阳拱本命天王星_001_L1",
    )
    version: str = "1.0.0"
