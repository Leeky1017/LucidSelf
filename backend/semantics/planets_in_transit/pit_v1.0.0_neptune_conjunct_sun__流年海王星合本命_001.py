"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.272694
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
    semantic_id="pit_v1.0.0_neptune_conjunct_sun__流年海王星合本命_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneConjunctSun流年海王星合本命(SemanticEntry):
    """
    > Positive: increases sensitivity and compassion, elevates concern with religion and metaphysics, su...
    """
    
    original_text: str = """> Positive: increases sensitivity and compassion, elevates concern with religion and metaphysics, subordinate ego to others' needs. But Sun is will and energy—Neptune rechannels this energy. Common reaction: fatigue, psychological futility and ineffectualness. Confusion, aimlessness. Difficult for drinking/drug problems. Avoid foreign chemicals. Body extremely sensitive, less able to resist strain. May be inclined to deceive others. Unusually idealistic—make sure ideals rooted in reality.

**Narrative Snippets**:
- `[ns_pit_ne013]` `[trigger: transit_neptune_conjunct_natal_sun]` `[factor_trigger: astro_transit_neptune CONJUNCT natal_sun]` `[role: 主干]` Increased sensitivity/compassion. May feel fatigue, confusion. Avoid drugs/alcohol. Idealism—root in reality. → PIT Ch12 Neptune☌Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune Conjunct Sun (流年海王星合本命太阳)"
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
        l1_anchor="pit_v1.0.0_neptune_conjunct_sun__流年海王星合本命_001_L1",
    )
    version: str = "1.0.0"
