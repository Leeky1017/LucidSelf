"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.280740
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
    semantic_id="pit_v1.0.0_mercury_in_the_fourth_house__水_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MercuryInTheFourthHouse水(SemanticEntry):
    """
    **Source Text** (Lines 5045-5068):
> Time of intellectual withdrawal to reflect and think about rece...
    """
    
    original_text: str = """**Source Text** (Lines 5045-5068):
> Time of intellectual withdrawal to reflect and think about recent ideas. Good to examine personal and domestic life. Excellent for family discussions about important matters. Voice your innermost thoughts. Don't allow pressures to build up. Thoughts may drift to past events—look for links to present concerns. May need to communicate with parents.

**English Paraphrase**: Intellectual withdrawal to reflect. Examine personal/domestic life. Good for family discussions. Voice innermost thoughts. Past events on mind—find links to present. Communicate with parents.

**Complete Chinese Interpretation**: 智力退缩以反思。检视个人/家庭生活。适合家庭讨论。表达内心想法。过去事件在心——找到与现在的联系。与父母沟通。

**Narrative Snippets**:
- `[ns_pit_me005]` `[trigger: mercury_transit_house_4]` `[factor_trigger: astro_transit_mercury AND astro_house_4]` `[role: 主干]` Intellectual withdrawal to reflect. Good for family discussions. Past events link to present. → PIT Ch6 Mercury-4H"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury in the Fourth House (水星过境第四宫)"
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
        l1_anchor="pit_v1.0.0_mercury_in_the_fourth_house__水_001_L1",
    )
    version: str = "1.0.0"
