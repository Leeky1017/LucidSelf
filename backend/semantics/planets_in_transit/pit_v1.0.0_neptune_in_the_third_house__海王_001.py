"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.272573
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
    semantic_id="pit_v1.0.0_neptune_in_the_third_house__海王_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneInTheThirdHouse海王(SemanticEntry):
    """
    **Source Text** (Lines 16714-16745):
> Dealings and communication with everyday world seriously affe...
    """
    
    original_text: str = """**Source Text** (Lines 16714-16745):
> Dealings and communication with everyday world seriously affected. Be very careful how you communicate—difficult to make yourself clear. Serious misunderstandings may disturb personal life, especially with neighbors and relatives. Enter negotiations with extreme care—misunderstanding or misrepresentation could get you involved in unwanted projects. Powerful inner effect: alter ways of dealing with world, thinking profoundly transformed. May begin serious study of metaphysical discipline—karma, reincarnation. Imaginative creativity increased—but don't let imagination interfere with seeing truth. If thinking excessively structured, upsets as you discover what you thought true is not. Can lead to confusion, self-doubt. If mind flexible, Neptune can give subtle insights—latent psychic abilities stimulated.

**English Paraphrase**: Communication seriously affected. Misunderstandings with neighbors/relatives. Negotiations with care. Inner transformation of thinking. May study metaphysics. Creativity increased but check imagination vs truth. If structured thinking, upsets and confusion. If flexible, psychic insights.

**Complete Chinese Interpretation**: 沟通严重受影响。与邻居/亲戚的误解。谈判要小心。思维的内在转变。可能学习形而上学。创造力增加但检查想象vs真相。如果思维结构化，会有动荡和困惑。如果灵活，有心灵洞察。

**Narrative Snippets**:
- `[ns_pit_ne003]` `[trigger: neptune_transit_house_3]` `[factor_trigger: astro_transit_neptune AND astro_house_3]` `[role: 主干]` Communication affected. Misunderstandings. Thinking transformed. May study metaphysics. Psychic insights if flexible. → PIT Ch12 Neptune-3H"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune in the Third House (海王星过境第三宫)"
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
        l1_anchor="pit_v1.0.0_neptune_in_the_third_house__海王_001_L1",
    )
    version: str = "1.0.0"
