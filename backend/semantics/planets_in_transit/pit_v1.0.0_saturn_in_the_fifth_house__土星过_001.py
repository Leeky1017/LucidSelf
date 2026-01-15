"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.318438
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
    semantic_id="pit_v1.0.0_saturn_in_the_fifth_house__土星过_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SaturnInTheFifthHouse土星过(SemanticEntry):
    """
    **Source Text** (Lines 12355-12389):
> Learn more about yourself and how to express yourself best. M...
    """
    
    original_text: str = """**Source Text** (Lines 12355-12389):
> Learn more about yourself and how to express yourself best. Must work for it, proceed carefully. House of recreation, but Saturn's transit not amusing. Everything has learning purpose. Begin to give restructured self new form through interaction. Areas associated with 5H may become burden—children heavy responsibility, love affairs difficult. May involve older person as parent/teacher or you play that role. May withdraw from encounters—understandable but avoid it. If want relationship but frustrated, examine real feelings—may be subconsciously avoiding. House of gambling/speculation—do not take such risks now. Anything produced through hard work.

**English Paraphrase**: Learn self-expression through work. Not amusing—everything has purpose. Children, love may be burden. May involve older person. May withdraw—don't avoid encounters. Examine why relationships frustrated. No gambling or speculation. Produce through hard work.

**Complete Chinese Interpretation**: 通过工作学习自我表达。不有趣——一切都有目的。孩子、爱情可能是负担。可能涉及年长者。可能退缩——不要回避相遇。检视为什么关系受挫。不要赌博或投机。通过努力工作产出。

**Narrative Snippets**:
- `[ns_pit_sa005]` `[trigger: saturn_transit_house_5]` `[factor_trigger: astro_transit_saturn AND astro_house_5]` `[role: 主干]` Learn self-expression through work. Children/love may be burden. No speculation. Hard work produces. → PIT Ch10 Saturn-5H"""
    normalized_text_zh: str = """"""
    subject: str = "Saturn in the Fifth House (土星过境第五宫)"
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
        l1_anchor="pit_v1.0.0_saturn_in_the_fifth_house__土星过_001_L1",
    )
    version: str = "1.0.0"
