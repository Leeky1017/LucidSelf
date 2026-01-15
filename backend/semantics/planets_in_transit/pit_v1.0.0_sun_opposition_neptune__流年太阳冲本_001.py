"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224621
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
    semantic_id="pit_v1.0.0_sun_opposition_neptune__流年太阳冲本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunOppositionNeptune流年太阳冲本(SemanticEntry):
    """
    > Critical test of your ideals and illusions. What you've believed may be challenged by reality. Oth...
    """
    
    original_text: str = """> Critical test of your ideals and illusions. What you've believed may be challenged by reality. Others may deceive you or reveal hidden truths. Confusion in relationships. Energy low—may feel disillusioned. Time to see things as they really are. Spiritual crisis possible but also spiritual awakening. Avoid alcohol/drugs.

**Narrative Snippets**:
- `[ns_pit_116]` `[trigger: transit_sun_opposition_natal_neptune]` `[factor_trigger: astro_transit_sun OPPOSITION natal_neptune]` `[role: 主干]` Test of ideals and illusions—beliefs challenged by reality. Others may deceive. See things as they are. → PIT Ch4 Sun☍Neptune"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Opposition Neptune (流年太阳冲本命海王星)"
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
        l1_anchor="pit_v1.0.0_sun_opposition_neptune__流年太阳冲本_001_L1",
    )
    version: str = "1.0.0"
