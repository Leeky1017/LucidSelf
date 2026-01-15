"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.258986
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
    semantic_id="pit_v1.0.0_venus_opposition_sun__流年金星冲本命太_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusOppositionSun流年金星冲本命太(SemanticEntry):
    """
    > Not especially troublesome. Good times, agreeable relationships, sexual attraction. Problems: over...
    """
    
    original_text: str = """> Not especially troublesome. Good times, agreeable relationships, sexual attraction. Problems: overindulgence, lack of discipline, unwilling to work. Amorous mood—good in existing relationships. Lack discrimination in new ones. Creative energies stimulated but may lack discipline.

**Narrative Snippets**:
- `[ns_pit_ve017]` `[trigger: transit_venus_opposition_natal_sun]` `[factor_trigger: astro_transit_venus OPPOSITION natal_sun]` `[role: 主干]` Good times and attraction. Watch overindulgence and lack of discipline. → PIT Ch7 Venus☍Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Venus Opposition Sun (流年金星冲本命太阳)"
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
        l1_anchor="pit_v1.0.0_venus_opposition_sun__流年金星冲本命太_001_L1",
    )
    version: str = "1.0.0"
