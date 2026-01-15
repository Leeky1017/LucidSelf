"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224544
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
    semantic_id="pit_v1.0.0_sun_sextile_uranus__流年太阳六合本命天王_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunSextileUranus流年太阳六合本命天王(SemanticEntry):
    """
    > Favorable for original thinking and new approaches. Pleasant surprises and opportunities may arise...
    """
    
    original_text: str = """> Favorable for original thinking and new approaches. Pleasant surprises and opportunities may arise. Good day to try something new. You're more open to change than usual. Friends may prove helpful. Group activities favored. Electrical and technological matters go well.

**Narrative Snippets**:
- `[ns_pit_108]` `[trigger: transit_sun_sextile_natal_uranus]` `[factor_trigger: astro_transit_sun SEXTILE natal_uranus]` `[role: 主干]` Favorable for original thinking—pleasant surprises. Open to change. Friends helpful. → PIT Ch4 Sun⚹Uranus"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Sextile Uranus (流年太阳六合本命天王星)"
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
        l1_anchor="pit_v1.0.0_sun_sextile_uranus__流年太阳六合本命天王_001_L1",
    )
    version: str = "1.0.0"
