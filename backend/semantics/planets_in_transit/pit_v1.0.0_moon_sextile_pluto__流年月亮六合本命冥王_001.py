"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301602
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
    semantic_id="pit_v1.0.0_moon_sextile_pluto__流年月亮六合本命冥王_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonSextilePluto流年月亮六合本命冥王(SemanticEntry):
    """
    > Can access deeper feelings constructively. Good for research, psychology, cleaning out emotional c...
    """
    
    original_text: str = """> Can access deeper feelings constructively. Good for research, psychology, cleaning out emotional closets. Positive transformation available. Influence with others enhanced.

**Narrative Snippets**:
- `[ns_pit_m072]` `[trigger: transit_moon_sextile_natal_pluto]` `[factor_trigger: astro_transit_moon SEXTILE natal_pluto]` `[role: 主干]` Access deeper feelings constructively. Good for research and emotional housecleaning. → PIT Ch5 Moon⚹Pluto"""
    normalized_text_zh: str = """"""
    subject: str = "Moon Sextile Pluto (流年月亮六合本命冥王星)"
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
        l1_anchor="pit_v1.0.0_moon_sextile_pluto__流年月亮六合本命冥王_001_L1",
    )
    version: str = "1.0.0"
