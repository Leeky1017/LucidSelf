"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.280763
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
    semantic_id="pit_v1.0.0_mercury_in_the_sixth_house__水星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MercuryInTheSixthHouse水星(SemanticEntry):
    """
    **Source Text** (Lines 5092-5122):
> Two areas: health and work. Excellent for all kinds of mental w...
    """
    
    original_text: str = """**Source Text** (Lines 5092-5122):
> Two areas: health and work. Excellent for all kinds of mental work. More attentive to detail, concerned about best techniques. Plan carefully, work out every detail. Practical work to be done. Get along well with employers and employees—good time to discuss problems. Be careful of criticizing others. If health aspect, may feel nervous or anxious. May become more concerned with health and hygiene.

**English Paraphrase**: Health and work focus. Excellent for mental work. Attentive to detail. Plan carefully. Good for employer/employee discussions. Careful of criticism. May feel anxious. Health/hygiene attention.

**Complete Chinese Interpretation**: 健康和工作焦点。适合脑力工作。注意细节。仔细计划。适合雇主/雇员讨论。小心批评。可能感到焦虑。健康/卫生关注。

**Narrative Snippets**:
- `[ns_pit_me007]` `[trigger: mercury_transit_house_6]` `[factor_trigger: astro_transit_mercury AND astro_house_6]` `[role: 主干]` Excellent for mental work. Attentive to detail. Good for work discussions. → PIT Ch6 Mercury-6H"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury in the Sixth House (水星过境第六宫)"
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
        l1_anchor="pit_v1.0.0_mercury_in_the_sixth_house__水星_001_L1",
    )
    version: str = "1.0.0"
