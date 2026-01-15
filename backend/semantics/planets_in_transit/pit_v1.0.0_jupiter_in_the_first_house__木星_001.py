"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.309694
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
    semantic_id="pit_v1.0.0_jupiter_in_the_first_house__木星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterInTheFirstHouse木星(SemanticEntry):
    """
    **Source Text** (Lines 10165-10191):
> Beginning of major cycle of growth. Discover what you really ...
    """
    
    original_text: str = """**Source Text** (Lines 10165-10191):
> Beginning of major cycle of growth. Discover what you really are as an individual. Feel more secure about yourself and impression you make. Less need to withdraw or hide talents. But don't exaggerate importance—look at truth of who you are. Time for learning and gaining new experience. Outgrow childish attitudes and prejudices. Persons and resources drawn to you. Spiritual dimension of life should be greater. Quite fortunate year—increased self-confidence. But try not to be overbearing, you are still learning.

**English Paraphrase**: Major growth cycle begins. Discover yourself. Feel secure, don't hide talents. Don't exaggerate importance. Time for learning, outgrow prejudices. Resources attracted. Spiritual growth. Fortunate year but don't be overbearing.

**Complete Chinese Interpretation**: 主要成长周期开始。发现自己。感觉安全，不要隐藏才能。不要夸大重要性。学习的时间，超越偏见。资源被吸引。精神成长。幸运的一年但不要傲慢。

**Narrative Snippets**:
- `[ns_pit_ju001]` `[trigger: jupiter_transit_house_1]` `[factor_trigger: astro_transit_jupiter AND astro_house_1]` `[role: 主干]` Major growth cycle begins. Self-discovery. Fortunate but don't be overbearing. → PIT Ch9 Jupiter-1H"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter in the First House (木星过境第一宫)"
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
        l1_anchor="pit_v1.0.0_jupiter_in_the_first_house__木星_001_L1",
    )
    version: str = "1.0.0"
