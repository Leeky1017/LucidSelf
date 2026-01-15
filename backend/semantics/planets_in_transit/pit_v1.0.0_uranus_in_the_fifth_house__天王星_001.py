"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.206649
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
    semantic_id="pit_v1.0.0_uranus_in_the_fifth_house__天王星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusInTheFifthHouse天王星(SemanticEntry):
    """
    **Source Text** (Lines 14557-14593):
> Exciting period. After 4H transit revolutionized basic approa...
    """
    
    original_text: str = """**Source Text** (Lines 14557-14593):
> Exciting period. After 4H transit revolutionized basic approach, now seek new forms of self-expression and creative release. New recreations and amusements. Attracted to new experiences expanding consciousness. Unusual relationships with opposite sex—break down old rigid patterns but don't expect durability. Characteristic: different age but act as equals. Sudden infatuation breaking up existing relationship. On-and-off or unexpected relationships. Relationship won't settle into routine—must remain in flux. Children can't be taken for granted—their development requires attention. May be unusually rebellious. If involved in creative enterprise, better at innovating, new approaches, new media and techniques. Opportunity to redefine yourself.

**English Paraphrase**: Exciting self-expression. New recreations. Unusual relationships—don't expect durability. Age-different equals. Children require attention. Creative innovation enhanced. Opportunity for self-redefinition.

**Complete Chinese Interpretation**: 令人兴奋的自我表达。新娱乐。不寻常的关系——不要期待持久。年龄不同的平等者。孩子需要关注。创意创新增强。自我重新定义的机会。

**Narrative Snippets**:
- `[ns_pit_ur005]` `[trigger: uranus_transit_house_5]` `[factor_trigger: astro_transit_uranus AND astro_house_5]` `[role: 主干]` Exciting self-expression. Unusual relationships. Children need attention. Creative innovation. → PIT Ch11 Uranus-5H"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus in the Fifth House (天王星过境第五宫)"
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
        l1_anchor="pit_v1.0.0_uranus_in_the_fifth_house__天王星_001_L1",
    )
    version: str = "1.0.0"
