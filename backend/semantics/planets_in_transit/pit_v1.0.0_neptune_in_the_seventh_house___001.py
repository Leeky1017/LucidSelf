"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.272621
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
    semantic_id="pit_v1.0.0_neptune_in_the_seventh_house___001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneInTheSeventhHouse(SemanticEntry):
    """
    **Source Text** (Lines 16835-16867):
> Affects all one-to-one relationships—marriage, partnerships, ...
    """
    
    original_text: str = """**Source Text** (Lines 16835-16867):
> Affects all one-to-one relationships—marriage, partnerships, conflicts, consultants. Danger of poor communications, misunderstandings, misrepresentation. In marriage: resentments not brought into open, one or both keeps feelings hidden, acts surreptitiously. Danger of overidealizing relations—thinking what you want to be true is true already. Be attentive to what's really happening. May have to take care of someone close who is sick. If in business, very careful about forming new partnership—not likely to work out, partner may be problem. Extreme cases: swindled by partner. Established partnership that worked well will continue, but communicate clearly. Normally not good for dealings with lawyers and lawsuits—won't get a good deal, factors determining outcome difficult to discover. Same for other consultants.

**English Paraphrase**: All one-to-one relationships affected. Misunderstandings, hidden feelings. May overidealize. May care for sick partner. New partnerships risky—could be swindled. Not good for lawyers/lawsuits. Communicate clearly.

**Complete Chinese Interpretation**: 所有一对一关系受影响。误解、隐藏的感情。可能过度理想化。可能照顾生病的伴侣。新伙伴关系有风险——可能被骗。不利于律师/诉讼。清楚沟通。

**Narrative Snippets**:
- `[ns_pit_ne007]` `[trigger: neptune_transit_house_7]` `[factor_trigger: astro_transit_neptune AND astro_house_7]` `[role: 主干]` Relationships affected. Misunderstandings. May overidealize. New partnerships risky. Not good for legal. → PIT Ch12 Neptune-7H"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune in the Seventh House (海王星过境第七宫)"
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
        l1_anchor="pit_v1.0.0_neptune_in_the_seventh_house___001_L1",
    )
    version: str = "1.0.0"
