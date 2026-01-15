"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.280775
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
    semantic_id="pit_v1.0.0_mercury_in_the_seventh_house___001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MercuryInTheSeventhHouse(SemanticEntry):
    """
    **Source Text** (Lines 5123-5143):
> Good time to clarify and explain issues to spouse or business p...
    """
    
    original_text: str = """**Source Text** (Lines 5123-5143):
> Good time to clarify and explain issues to spouse or business partner. Good for consulting specialists. Don't think alone—need another's consciousness. Finding out partner's thoughts helps clarify yours. Together accomplish more than separately. Good to discuss relationship difficulties—more detached view. Seek intellectual stimulation and conversation, even argument. Good for contracts and negotiations unless afflicted.

**English Paraphrase**: Good for clarifying with partner. Consult specialists. Don't think alone. Together accomplish more. Discuss relationship difficulties with detachment. Seek intellectual stimulation. Good for contracts unless afflicted.

**Complete Chinese Interpretation**: 适合与伴侣澄清。咨询专家。不要独自思考。一起完成更多。超脱地讨论关系困难。寻求智力刺激。适合合同除非受刑。

**Narrative Snippets**:
- `[ns_pit_me008]` `[trigger: mercury_transit_house_7]` `[factor_trigger: astro_transit_mercury AND astro_house_7]` `[role: 主干]` Good for partner discussions. Don't think alone. Seek intellectual stimulation. → PIT Ch6 Mercury-7H"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury in the Seventh House (水星过境第七宫)"
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
        l1_anchor="pit_v1.0.0_mercury_in_the_seventh_house___001_L1",
    )
    version: str = "1.0.0"
