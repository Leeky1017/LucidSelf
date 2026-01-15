"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.258794
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
    semantic_id="pit_v1.0.0_venus_in_the_eighth_house__金星过_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusInTheEighthHouse金星过(SemanticEntry):
    """
    **Source Text** (Lines 6942-6957):
> Can stimulate sexual side of relationships, greater intensity. ...
    """
    
    original_text: str = """**Source Text** (Lines 6942-6957):
> Can stimulate sexual side of relationships, greater intensity. Sex becomes vehicle for self-transformation. Love relationship beginning now will be intense throughout and have greater impact. May attract money through spouse, partner, bank, or institution—good time to seek loan. Hidden relationship factors may surface. Learn much about how you relate to people.

**English Paraphrase**: Stimulates sexual intensity. Sex as transformation. New love intense and impactful. May attract money through others. Hidden factors surface. Learn about relating.

**Complete Chinese Interpretation**: 刺激性的强度。性作为转化。新的爱情强烈而有影响力。可能通过他人吸引金钱。隐藏因素浮出水面。学习如何与人相处。

**Narrative Snippets**:
- `[ns_pit_ve008]` `[trigger: venus_transit_house_8]` `[factor_trigger: astro_transit_venus AND astro_house_8]` `[role: 主干]` Stimulates sexual intensity and transformation. May attract money through others. → PIT Ch7 Venus-8H"""
    normalized_text_zh: str = """"""
    subject: str = "Venus in the Eighth House (金星过境第八宫)"
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
        l1_anchor="pit_v1.0.0_venus_in_the_eighth_house__金星过_001_L1",
    )
    version: str = "1.0.0"
