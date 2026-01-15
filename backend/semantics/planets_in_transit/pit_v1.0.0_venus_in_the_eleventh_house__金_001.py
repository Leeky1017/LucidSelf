"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.258862
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
    semantic_id="pit_v1.0.0_venus_in_the_eleventh_house__金_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusInTheEleventhHouse金(SemanticEntry):
    """
    **Source Text** (Lines 6999-7019):
> One of best transits for group activities or with friends. Feel...
    """
    
    original_text: str = """**Source Text** (Lines 6999-7019):
> One of best transits for group activities or with friends. Feel friendly toward almost everyone. Good time for party or going out with friends. Any group situation favored—business conference, organizational meeting. Ego energies low, can compromise without losing something personal. Feel secure, willing to help group achieve objective. Love relationships possess friendly quality.

**English Paraphrase**: Best for groups and friends. Feel friendly. Good for parties. Group situations favored. Can compromise easily. Secure and helpful. Love has friendly quality.

**Complete Chinese Interpretation**: 对群体和朋友最好。感觉友好。适合派对。群体情况受青睐。可以轻松妥协。安全和乐于助人。爱情有友好的品质。

**Narrative Snippets**:
- `[ns_pit_ve011]` `[trigger: venus_transit_house_11]` `[factor_trigger: astro_transit_venus AND astro_house_11]` `[role: 主干]` Best for groups and friends. Group situations favored. Love has friendly quality. → PIT Ch7 Venus-11H"""
    normalized_text_zh: str = """"""
    subject: str = "Venus in the Eleventh House (金星过境第十一宫)"
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
        l1_anchor="pit_v1.0.0_venus_in_the_eleventh_house__金_001_L1",
    )
    version: str = "1.0.0"
