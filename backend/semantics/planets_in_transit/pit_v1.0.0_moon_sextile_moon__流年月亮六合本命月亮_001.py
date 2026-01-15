"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301182
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
    semantic_id="pit_v1.0.0_moon_sextile_moon__流年月亮六合本命月亮_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonSextileMoon流年月亮六合本命月亮(SemanticEntry):
    """
    > Emotional equilibrium and flow. Easy to express feelings and connect with others emotionally. Good...
    """
    
    original_text: str = """> Emotional equilibrium and flow. Easy to express feelings and connect with others emotionally. Good time for domestic activities and family contact. Feelings support your intentions.

**Narrative Snippets**:
- `[ns_pit_m032]` `[trigger: transit_moon_sextile_natal_moon]` `[factor_trigger: astro_transit_moon SEXTILE natal_moon]` `[role: 主干]` Emotional equilibrium—easy to express feelings. Good for domestic and family activities. → PIT Ch5 Moon⚹Moon"""
    normalized_text_zh: str = """"""
    subject: str = "Moon Sextile Moon (流年月亮六合本命月亮)"
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
        l1_anchor="pit_v1.0.0_moon_sextile_moon__流年月亮六合本命月亮_001_L1",
    )
    version: str = "1.0.0"
