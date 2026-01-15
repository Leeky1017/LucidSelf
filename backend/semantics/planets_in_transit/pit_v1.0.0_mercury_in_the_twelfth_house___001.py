"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.280834
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
    semantic_id="pit_v1.0.0_mercury_in_the_twelfth_house___001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MercuryInTheTwelfthHouse(SemanticEntry):
    """
    **Source Text** (Lines 5231-5255):
> Two sides: may keep opinions to yourself, but also more in touc...
    """
    
    original_text: str = """**Source Text** (Lines 5231-5255):
> Two sides: may keep opinions to yourself, but also more in touch with hidden sides of personality. Problem: may feel others will hold anything you say against you. But what you don't say may be held against you—say everything that has to be said. Keeping secrets undermines confidence. May want to go off to think or study—works well. Greater concern with spiritual and religious matters. Good for research by yourself.

**English Paraphrase**: May keep opinions secret but also in touch with hidden self. Say what needs saying—secrets undermine trust. Good for solitary thinking/study. Spiritual/religious concern. Good for research alone.

**Complete Chinese Interpretation**: 可能保守意见但也接触隐藏的自我。说需要说的——秘密破坏信任。适合独自思考/学习。精神/宗教关注。适合独自研究。

**Narrative Snippets**:
- `[ns_pit_me013]` `[trigger: mercury_transit_house_12]` `[factor_trigger: astro_transit_mercury AND astro_house_12]` `[role: 主干]` May keep opinions secret but in touch with hidden self. Say what needs saying. → PIT Ch6 Mercury-12H
- `[ns_pit_me014]` `[trigger: mercury_transit_house_12]` `[factor_trigger: astro_transit_mercury AND astro_house_12]` `[role: 总结]` Good for solitary thinking, study, research. Spiritual concerns heightened. → PIT Ch6 Mercury-12H"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury in the Twelfth House (水星过境第十二宫)"
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
        l1_anchor="pit_v1.0.0_mercury_in_the_twelfth_house___001_L1",
    )
    version: str = "1.0.0"
