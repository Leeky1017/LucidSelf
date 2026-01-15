"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.258722
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
    semantic_id="pit_v1.0.0_venus_in_the_fifth_house__金星过境_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusInTheFifthHouse金星过境(SemanticEntry):
    """
    **Source Text** (Lines 6886-6903):
> More than any other position signifies time for fun, entertainm...
    """
    
    original_text: str = """**Source Text** (Lines 6886-6903):
> More than any other position signifies time for fun, entertainment, good times. Fifth house: amusement, creative self-expression, love affairs, children. Self-discipline at all-time low. Enjoy yourself but don't overdo. Relate well with children—games and fun. Creative activities favored. Need to express through creative activity. Love relationships favored—get along smoothly without surrendering identity.

**English Paraphrase**: Time for fun, entertainment. Self-discipline low. Good with children. Creative activities and love relationships favored. Be yourself, enjoy.

**Complete Chinese Interpretation**: 娱乐、享乐的时光。自律性低。与孩子相处好。创意活动和爱情关系受青睐。做自己，享受。

**Narrative Snippets**:
- `[ns_pit_ve005]` `[trigger: venus_transit_house_5]` `[factor_trigger: astro_transit_venus AND astro_house_5]` `[role: 主干]` Time for fun and entertainment. Creative activities and love favored. Be yourself. → PIT Ch7 Venus-5H"""
    normalized_text_zh: str = """"""
    subject: str = "Venus in the Fifth House (金星过境第五宫)"
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
        l1_anchor="pit_v1.0.0_venus_in_the_fifth_house__金星过境_001_L1",
    )
    version: str = "1.0.0"
