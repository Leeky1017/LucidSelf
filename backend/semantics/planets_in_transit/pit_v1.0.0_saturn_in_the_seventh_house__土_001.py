"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.318462
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
    semantic_id="pit_v1.0.0_saturn_in_the_seventh_house__土_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SaturnInTheSeventhHouse土(SemanticEntry):
    """
    **Source Text** (Lines 12422-12453):
> Culmination of process that began 14 years ago. Need to exper...
    """
    
    original_text: str = """**Source Text** (Lines 12422-12453):
> Culmination of process that began 14 years ago. Need to experience yourself through one-to-one encounters—partnerships, intimate associations. Close associations test you and make demands. Some relationships end. Often coincides with marital breakup. Even good marriage confronts flaws. Coworkers make demands because see you as someone who can accomplish. Saturn above horizon again—attention focused on social world. If prepared well, begin to get recognition. But tests of ability through confrontations. Better you handle, better relationship in future. Must understand nature of relationships—expectations. What agreements have you made? Live up to them.

**English Paraphrase**: Culmination of 14-year cycle. Partnerships test you. Some relationships end—often marital. Even good ones confront flaws. Coworkers demand proof. Begin getting recognition if prepared. Tests through confrontations. Understand and fulfill agreements.

**Complete Chinese Interpretation**: 14年周期的顶点。伙伴关系测试你。一些关系结束——经常是婚姻。即使好的也面对缺陷。同事要求证明。如果准备好了开始获得认可。通过对抗测试。理解并履行协议。

**Narrative Snippets**:
- `[ns_pit_sa007]` `[trigger: saturn_transit_house_7]` `[factor_trigger: transit_saturn AND astro_house_7 AND astro_relationship_power AND astro_relationship_test]` `[role: 主干]` Partnerships tested. Some end. Recognition if prepared. Understand and fulfill agreements. → PIT Ch10 Saturn-7H"""
    normalized_text_zh: str = """"""
    subject: str = "Saturn in the Seventh House (土星过境第七宫)"
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
        l1_anchor="pit_v1.0.0_saturn_in_the_seventh_house__土_001_L1",
    )
    version: str = "1.0.0"
