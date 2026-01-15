"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.287973
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
    semantic_id="pit_v1.0.0_mars_in_the_fifth_house__火星过境第_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MarsInTheFifthHouse火星过境第(SemanticEntry):
    """
    **Source Text** (Lines 8373-8404):
> Demand to be yourself and express who you are. Filled with "I a...
    """
    
    original_text: str = """**Source Text** (Lines 8373-8404):
> Demand to be yourself and express who you are. Filled with "I am!" energies. Not inclined to self-denial or discipline. Expressed in playful, sportive way—house of amusement. Athletic activity excellent outlet. More competitive than usual. In love: desire nature strong, know what you want. Physical lovemaking important. May have conflicts with children. Lack discipline for unappealing tasks.

**English Paraphrase**: Demand to be yourself. "I am!" energies. Playful, athletic outlets good. Competitive. Strong desire in love—physical expression important. May conflict with children. Lack discipline.

**Complete Chinese Interpretation**: 要求做自己。"我是！"能量。有趣、运动的出口好。竞争性强。爱情中强烈的欲望——身体表达重要。可能与孩子冲突。缺乏纪律。

**Narrative Snippets**:
- `[ns_pit_ma005]` `[trigger: mars_transit_house_5]` `[factor_trigger: astro_transit_mars AND astro_house_5]` `[role: 主干]` Demand to be yourself. Athletic outlets. Strong desire in love. May lack discipline. → PIT Ch8 Mars-5H"""
    normalized_text_zh: str = """"""
    subject: str = "Mars in the Fifth House (火星过境第五宫)"
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
        l1_anchor="pit_v1.0.0_mars_in_the_fifth_house__火星过境第_001_L1",
    )
    version: str = "1.0.0"
