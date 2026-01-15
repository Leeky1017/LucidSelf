"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.309933
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
    semantic_id="pit_v1.0.0_jupiter_sextile_sun__流年木星六合本命太_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterSextileSun流年木星六合本命太(SemanticEntry):
    """
    > Life flows easily. Move in intended direction. Period of growth, optimism. Good time for long look...
    """
    
    original_text: str = """> Life flows easily. Move in intended direction. Period of growth, optimism. Good time for long look at how life is working out. Good relations with people in power. Attract accomplishers. Good for advancing interests. Good times with friends. Think big—alert to opportunities. Feel generous and tolerant. May patch up relationships. Sometimes unexpected income.

**Narrative Snippets**:
- `[ns_pit_ju014]` `[trigger: transit_jupiter_sextile_natal_sun]` `[factor_trigger: astro_transit_jupiter SEXTILE natal_sun]` `[role: 主干]` Life flows easily. Growth and optimism. Good with people in power. → PIT Ch9 Jupiter⚹Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter Sextile Sun (流年木星六合本命太阳)"
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
        l1_anchor="pit_v1.0.0_jupiter_sextile_sun__流年木星六合本命太_001_L1",
    )
    version: str = "1.0.0"
