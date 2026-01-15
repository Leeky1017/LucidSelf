"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.258924
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
    semantic_id="pit_v1.0.0_venus_sextile_sun__流年金星六合本命太阳_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusSextileSun流年金星六合本命太阳(SemanticEntry):
    """
    > Excellent for group activity and friends. Feel unusually sociable. Friends may benefit you. Good t...
    """
    
    original_text: str = """> Excellent for group activity and friends. Feel unusually sociable. Friends may benefit you. Good time to ask favors or apply for loan. Good for interviews. Get along well in everyday encounters. May make new friends. Favorable impression on authorities.

**Narrative Snippets**:
- `[ns_pit_ve014]` `[trigger: transit_venus_sextile_natal_sun]` `[factor_trigger: astro_transit_venus SEXTILE natal_sun]` `[role: 主干]` Excellent for groups and friends. Good for favors and interviews. → PIT Ch7 Venus⚹Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Venus Sextile Sun (流年金星六合本命太阳)"
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
        l1_anchor="pit_v1.0.0_venus_sextile_sun__流年金星六合本命太阳_001_L1",
    )
    version: str = "1.0.0"
