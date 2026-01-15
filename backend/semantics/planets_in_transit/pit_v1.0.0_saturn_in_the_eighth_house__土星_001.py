"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.318473
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
    semantic_id="pit_v1.0.0_saturn_in_the_eighth_house__土星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SaturnInTheEighthHouse土星(SemanticEntry):
    """
    **Source Text** (Lines 12454-12486):
> Finances and possessions held with others in focus. Greater t...
    """
    
    original_text: str = """**Source Text** (Lines 12454-12486):
> Finances and possessions held with others in focus. Greater transformations questioned. Must come to terms with other people's values without destroying your individuality. Often through conflict with others' values. Other people's resources may be cut off. Can't count on others for material backing now. Not getting loans because haven't met criteria. Partner may encounter hard times. Get into position where don't depend on others' resources. Also house of major transformations and death—unlikely your own death, but may be someone else's or psychological concern with mortality. Review changes since Saturn crossed Ascendant. Understand where you're going.

**English Paraphrase**: Focus on shared resources. Come to terms with others' values. Others' resources may be cut off. Can't depend on others now. Get independent position. May concern with mortality. Review changes, understand direction.

**Complete Chinese Interpretation**: 聚焦共享资源。接受他人的价值观。他人的资源可能被切断。现在不能依赖他人。获得独立地位。可能关注死亡。回顾变化，理解方向。

**Narrative Snippets**:
- `[ns_pit_sa008]` `[trigger: saturn_transit_house_8]` `[factor_trigger: astro_house_8 AND astro_deep_transformation]` `[role: 主干]` Shared resources focus. Others' values. Resources may be cut off. Get independent. → PIT Ch10 Saturn-8H"""
    normalized_text_zh: str = """"""
    subject: str = "Saturn in the Eighth House (土星过境第八宫)"
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
        l1_anchor="pit_v1.0.0_saturn_in_the_eighth_house__土星_001_L1",
    )
    version: str = "1.0.0"
