"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.280729
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
    semantic_id="pit_v1.0.0_mercury_in_the_third_house__水星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MercuryInTheThirdHouse水星(SemanticEntry):
    """
    **Source Text** (Lines 5023-5044):
> Mercury in its own house—action intensified. Many group discuss...
    """
    
    original_text: str = """**Source Text** (Lines 5023-5044):
> Mercury in its own house—action intensified. Many group discussions, conversations, meet new people, possibly travel, more contact with relatives and neighbors. Electricity turned on in your mind—need to communicate with many people. Very good for intellectual activities. Not good to try to settle down. Tempo of events too fast. Use this time to gather information rather than reach conclusions. Keep mind flexible.

**English Paraphrase**: Mercury's own house—intensified. Many conversations, new people, travel, relatives. Mind electrified. Good for intellectual activities but tempo fast. Gather information, don't conclude. Stay flexible.

**Complete Chinese Interpretation**: 水星的本宫——加强。许多对话、新人、旅行、亲戚。思维通电。适合智力活动但节奏快。收集信息，不要下结论。保持灵活。

**Narrative Snippets**:
- `[ns_pit_me004]` `[trigger: mercury_transit_house_3]` `[factor_trigger: astro_transit_mercury AND astro_house_3]` `[role: 主干]` Mercury's own house—intensified communication. Gather information, don't conclude yet. → PIT Ch6 Mercury-3H"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury in the Third House (水星过境第三宫)"
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
        l1_anchor="pit_v1.0.0_mercury_in_the_third_house__水星_001_L1",
    )
    version: str = "1.0.0"
