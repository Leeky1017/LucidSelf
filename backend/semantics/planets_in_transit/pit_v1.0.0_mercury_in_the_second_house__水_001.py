"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.280713
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
    semantic_id="pit_v1.0.0_mercury_in_the_second_house__水_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MercuryInTheSecondHouse水(SemanticEntry):
    """
    **Source Text** (Lines 5002-5020):
> Attention turns to whatever you value—material, intellectual or...
    """
    
    original_text: str = """**Source Text** (Lines 5002-5020):
> Attention turns to whatever you value—material, intellectual or spiritual. Plan for these elements, enter negotiations concerning property or money. Much more concerned with business and commercial affairs. Shopping more, or important business negotiations. Whatever you do, put great planning into it. Avoid significant transactions on afflicted days—mind likely to be cloudy.

**English Paraphrase**: Attention to values and possessions. Negotiations about property/money. Concerned with business affairs. Great planning in transactions. Avoid significant deals on afflicted days.

**Complete Chinese Interpretation**: 关注价值观和财产。关于财产/金钱的谈判。关注商业事务。交易中需要周密计划。受刑日避免重大交易。

**Narrative Snippets**:
- `[ns_pit_me003]` `[trigger: mercury_transit_house_2]` `[factor_trigger: astro_transit_mercury AND astro_house_2]` `[role: 主干]` Attention to values and possessions. Good for business planning and negotiations. → PIT Ch6 Mercury-2H"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury in the Second House (水星过境第二宫)"
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
        l1_anchor="pit_v1.0.0_mercury_in_the_second_house__水_001_L1",
    )
    version: str = "1.0.0"
