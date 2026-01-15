"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.318427
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
    semantic_id="pit_v1.0.0_saturn_in_the_fourth_house__土星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SaturnInTheFourthHouse土星(SemanticEntry):
    """
    **Source Text** (Lines 12322-12354):
> Extremely important transit. Focus on innermost personal and ...
    """
    
    original_text: str = """**Source Text** (Lines 12322-12354):
> Extremely important transit. Focus on innermost personal and domestic life. Any domestic problems become more critical. Effects range from simple reorganization to total reshuffling of relationships. Home may become tremendous burden. Past elements come back into prominence. Excellent for psychotherapy. May take on parental responsibility or seek parent figure—ensure leads to independence. Period of preparation ending—ready to emerge from dormancy. Must start modestly. Pay attention to securing foundation. Inner problems not cleared now will be source of problems next 14 years. Time of new beginnings.

**English Paraphrase**: Extremely important. Focus on home and inner life. Domestic problems critical. Home may be burden. Past returns. Good for therapy. May assume/seek parental role. Preparation ending—secure foundation. Problems not cleared now cause future trouble. New beginnings.

**Complete Chinese Interpretation**: 极其重要。聚焦家庭和内在生活。家庭问题关键。家可能是负担。过去回归。适合治疗。可能承担/寻求父母角色。准备结束——巩固基础。现在没清除的问题导致未来麻烦。新的开始。

**Narrative Snippets**:
- `[ns_pit_sa004]` `[trigger: saturn_transit_house_4]` `[factor_trigger: astro_transit_saturn AND astro_house_4]` `[role: 主干]` Focus on home and foundation. Domestic issues critical. Clear inner problems now. New beginnings. → PIT Ch10 Saturn-4H"""
    normalized_text_zh: str = """"""
    subject: str = "Saturn in the Fourth House (土星过境第四宫)"
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
        l1_anchor="pit_v1.0.0_saturn_in_the_fourth_house__土星_001_L1",
    )
    version: str = "1.0.0"
