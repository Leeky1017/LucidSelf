"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.280787
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
    semantic_id="pit_v1.0.0_mercury_in_the_eighth_house__水_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MercuryInTheEighthHouse水(SemanticEntry):
    """
    **Source Text** (Lines 5144-5166):
> Good to look inward and reflect on deep psychological truths. R...
    """
    
    original_text: str = """**Source Text** (Lines 5144-5166):
> Good to look inward and reflect on deep psychological truths. Rational intellect closer to usually hidden areas. Conversations may have profound effect on mind, causing deep changes in viewpoint. May have tremendous hold over each other's minds. Very deep thinking, including about mortality. Good for discussions about joint finances or property.

**English Paraphrase**: Look inward, reflect on deep psychological truths. Conversations have profound effect. Deep thinking, including mortality. Good for joint finance discussions.

**Complete Chinese Interpretation**: 向内看，反思深层心理真相。对话有深刻影响。深度思考，包括死亡。适合共同财务讨论。

**Narrative Snippets**:
- `[ns_pit_me009]` `[trigger: mercury_transit_house_8]` `[factor_trigger: astro_transit_mercury AND astro_house_8]` `[role: 主干]` Look inward, deep psychological reflection. Conversations have profound effect. → PIT Ch6 Mercury-8H"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury in the Eighth House (水星过境第八宫)"
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
        l1_anchor="pit_v1.0.0_mercury_in_the_eighth_house__水_001_L1",
    )
    version: str = "1.0.0"
