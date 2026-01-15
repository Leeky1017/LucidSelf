"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.272681
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
    semantic_id="pit_v1.0.0_neptune_in_the_twelfth_house___001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneInTheTwelfthHouse(SemanticEntry):
    """
    **Source Text** (Lines 16979-17011):
> Time of reflection and deep inner concerns. No longer adequat...
    """
    
    original_text: str = """**Source Text** (Lines 16979-17011):
> Time of reflection and deep inner concerns. No longer adequate to be successful on external/material plane—must question and evaluate life's spiritual meaning. Have you been inwardly fulfilled or has life been shallow masquerade? Must deal with this dimension. May want to withdraw from rapid pace to find peace to examine yourself. If working hard on career, may want to slack off—more concerned with meaning in life. May stimulate concern with religion and faith. Discover inadequacies of rational intellect—capability for belief, intuition, sensitivity more important. Psychic abilities may be aroused. Take great interest in psychic sciences—any means for getting in touch with deeper dimensions. Most difficult effects if examine past life and find you haven't served spiritual needs well. May become subject to depression when life seems meaningless and empty. If happens, make changes facilitating spiritual dimension. Never too late. Greatest disease of modern age is alienation—Neptune in 12H is opportunity to discover essential oneness with all being.

**English Paraphrase**: Time for reflection and spiritual meaning. Question if life has been fulfilling. May withdraw from pace to examine self. Concern with religion, faith. Intuition and belief more important than intellect. Psychic abilities aroused. May feel depression if spiritual needs unserved. Make changes—never too late. Opportunity to discover oneness with all.

**Complete Chinese Interpretation**: 反思和精神意义的时间。质疑生活是否充实。可能从节奏中退出以审视自己。对宗教、信仰的关注。直觉和信念比智力更重要。心灵能力被唤醒。如果精神需求未被满足可能感到沮丧。做出改变——永远不晚。发现与一切合一的机会。

**Narrative Snippets**:
- `[ns_pit_ne012]` `[trigger: neptune_transit_house_12]` `[factor_trigger: astro_transit_neptune AND astro_house_12 AND astro_spiritual_peak]` `[role: 主干]` Time for spiritual reflection. Intuition over intellect. Psychic abilities. May feel depression. Discover oneness. → PIT Ch12 Neptune-12H"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune in the Twelfth House (海王星过境第十二宫)"
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
        l1_anchor="pit_v1.0.0_neptune_in_the_twelfth_house___001_L1",
    )
    version: str = "1.0.0"
