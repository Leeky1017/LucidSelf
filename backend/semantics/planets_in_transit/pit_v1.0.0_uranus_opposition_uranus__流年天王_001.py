"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.208309
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
    semantic_id="pit_v1.0.0_uranus_opposition_uranus__流年天王_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusOppositionUranus流年天王(SemanticEntry):
    """
    > Midlife crisis (~42 years). Others bring awareness of unlived life. Major reassessment. What have ...
    """
    
    original_text: str = """> Midlife crisis (~42 years). Others bring awareness of unlived life. Major reassessment. What have you not done that you need to?

**Narrative Snippets**:
- `[ns_pit_ur052]` `[trigger: transit_uranus_opposition_natal_uranus]` `[factor_trigger: astro_transit_uranus OPPOSITION natal_uranus]` `[role: 主干]` Midlife crisis (~42). Awareness of unlived life. Major reassessment. → PIT Ch11 Uranus☍Uranus"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus Opposition Uranus (流年天王星冲本命天王星)"
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
        l1_anchor="pit_v1.0.0_uranus_opposition_uranus__流年天王_001_L1",
    )
    version: str = "1.0.0"
