"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.272656
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
    semantic_id="pit_v1.0.0_neptune_in_the_tenth_house__海王_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneInTheTenthHouse海王(SemanticEntry):
    """
    **Source Text** (Lines 16927-16958):
> Can be very confusing and disorienting, but can teach basic t...
    """
    
    original_text: str = """**Source Text** (Lines 16927-16958):
> Can be very confusing and disorienting, but can teach basic truths if you get over fear and confusion. Makes you feel unsure of where you're going and why. If regard work as justification for existence, very difficult time—Neptune makes you wonder if any purpose in what you're doing. Disillusionment may come through defeats or incident showing work not what you thought, or deception. Be careful about deceiving others or being deceived. May feel discouraged—people oppose efforts to get ahead for no apparent reason. May decide present calling not adequate, need more meaning. Need to change whole attitude toward what you're doing—should be appropriate self-expression, not justification. Be less attached to what you're doing—you are not what you do. Ego wrapped up in work probably causing problems with others. Favors social-service work with disadvantaged. Transit not destructive if work in spirit of helping others. May bring interest in psychic, spiritual, occult matters in profession.

**English Paraphrase**: Confusing but teaches basic truths. Feel unsure of direction. If work is ego justification, difficult—wonder about purpose. May be deceived or disillusioned. Change attitude—work should be self-expression, not justification. Favors social service. Not destructive if helping others.

**Complete Chinese Interpretation**: 令人困惑但教导基本真理。感觉方向不确定。如果工作是自我证明，困难——质疑目的。可能被欺骗或幻灭。改变态度——工作应该是自我表达，而不是证明。有利于社会服务。如果帮助他人则不会破坏。

**Narrative Snippets**:
- `[ns_pit_ne010]` `[trigger: neptune_transit_house_10]` `[factor_trigger: astro_transit_neptune AND astro_house_10]` `[role: 主干]` Confusing career period. Question purpose. Change attitude—work as self-expression. Favors social service. → PIT Ch12 Neptune-10H"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune in the Tenth House (海王星过境第十宫)"
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
        l1_anchor="pit_v1.0.0_neptune_in_the_tenth_house__海王_001_L1",
    )
    version: str = "1.0.0"
