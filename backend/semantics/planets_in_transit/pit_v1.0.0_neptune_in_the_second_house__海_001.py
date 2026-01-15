"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.272561
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
    semantic_id="pit_v1.0.0_neptune_in_the_second_house__海_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneInTheSecondHouse海(SemanticEntry):
    """
    **Source Text** (Lines 16681-16713):
> Fundamental change of attitude toward possessions, coinciding...
    """
    
    original_text: str = """**Source Text** (Lines 16681-16713):
> Fundamental change of attitude toward possessions, coinciding with change in values. More attached to possessions, more likely to lose what you consider important. Neptune works against ego by muddying and confusing ideas prior to complete reorientation. Probably considerable confusion about property, may be deluded into costly mistakes. Worst trouble only if totally identify with material possessions. Neptune rules mystical principle of detachment. May be tempted to gamble or risky speculation—if playful spirit might do well, if serious and worried will probably lose. Sense of values may become spiritualized and idealized—learn that possessions not so important, what you need will be provided to extent you are detached. Be careful managing money, avoid gambling unless truly detached. Avoid risky schemes—could be swindled.

**English Paraphrase**: Change in possessions/values attitude. Confusion about property, costly mistakes possible. Worst if over-identified with possessions. Learn detachment. Gambling risky. Values may spiritualize. Be careful with money—could be swindled.

**Complete Chinese Interpretation**: 财产/价值态度改变。财产困惑，可能犯代价高昂的错误。如果过度认同财产则最糟。学习超脱。赌博有风险。价值观可能精神化。小心金钱——可能被骗。

**Narrative Snippets**:
- `[ns_pit_ne002]` `[trigger: neptune_transit_house_2]` `[factor_trigger: astro_transit_neptune AND astro_house_2]` `[role: 主干]` Change in values/possessions. Learn detachment. Avoid gambling unless detached. Could be swindled. → PIT Ch12 Neptune-2H"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune in the Second House (海王星过境第二宫)"
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
        l1_anchor="pit_v1.0.0_neptune_in_the_second_house__海_001_L1",
    )
    version: str = "1.0.0"
