"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224602
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
    semantic_id="pit_v1.0.0_sun_square_neptune__流年太阳刑本命海王星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunSquareNeptune流年太阳刑本命海王星(SemanticEntry):
    """
    > Confusion and uncertainty possible. Energy low or diffused. May be deceived by others or deceive y...
    """
    
    original_text: str = """> Confusion and uncertainty possible. Energy low or diffused. May be deceived by others or deceive yourself. Avoid important decisions if possible. Not good for business or practical matters. Escapist tendencies strong—don't use alcohol or drugs. Boundaries unclear—protect yourself. Creative imagination strong but may lack focus.

**Narrative Snippets**:
- `[ns_pit_114]` `[trigger: transit_sun_square_natal_neptune]` `[factor_trigger: astro_transit_sun SQUARE natal_neptune]` `[role: 主干]` Confusion possible—may be deceived. Energy diffused. Avoid important decisions. Escapist tendencies. → PIT Ch4 Sun□Neptune"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Square Neptune (流年太阳刑本命海王星)"
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
        l1_anchor="pit_v1.0.0_sun_square_neptune__流年太阳刑本命海王星_001_L1",
    )
    version: str = "1.0.0"
