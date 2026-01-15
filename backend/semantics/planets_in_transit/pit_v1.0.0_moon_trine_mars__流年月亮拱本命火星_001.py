"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301340
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
    semantic_id="pit_v1.0.0_moon_trine_mars__流年月亮拱本命火星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonTrineMars流年月亮拱本命火星(SemanticEntry):
    """
    > Harmonious blend of emotions and energy. Can act on feelings confidently. Good for physical activi...
    """
    
    original_text: str = """> Harmonious blend of emotions and energy. Can act on feelings confidently. Good for physical activity, domestic projects, defending loved ones. Feel emotionally strong and capable.

**Narrative Snippets**:
- `[ns_pit_m049]` `[trigger: transit_moon_trine_natal_mars]` `[factor_trigger: astro_transit_moon TRINE natal_mars]` `[role: 主干]` Harmonious emotions and energy. Act on feelings confidently. Feel emotionally strong. → PIT Ch5 Moon△Mars"""
    normalized_text_zh: str = """"""
    subject: str = "Moon Trine Mars (流年月亮拱本命火星)"
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
        l1_anchor="pit_v1.0.0_moon_trine_mars__流年月亮拱本命火星_001_L1",
    )
    version: str = "1.0.0"
