"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.258641
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
    semantic_id="pit_v1.0.0_venus_in_the_second_house__金星过_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusInTheSecondHouse金星过(SemanticEntry):
    """
    **Source Text** (Lines 6832-6849):
> Financially good or difficult depending on handling. Venus attr...
    """
    
    original_text: str = """**Source Text** (Lines 6832-6849):
> Financially good or difficult depending on handling. Venus attracts material possessions and money. Financial opportunities may come but tendency to be extravagant. Tastes may be more lavish than budget allows. Susceptible to beautiful clothes, jewelry, art. Care in spending advisable. Favorable for financial negotiations. Borrowing money not difficult. Investments usually advantageous, especially in art.

**English Paraphrase**: Financial opportunities but watch extravagance. Venus attracts money but tastes exceed budget. Good for negotiations, loans. Investments in art favorable.

**Complete Chinese Interpretation**: 财务机会但注意奢侈。金星吸引金钱但品味超出预算。适合谈判、贷款。艺术投资有利。

**Narrative Snippets**:
- `[ns_pit_ve002]` `[trigger: venus_transit_house_2]` `[factor_trigger: astro_transit_venus AND astro_house_2]` `[role: 主干]` Financial opportunities but watch extravagance. Good for negotiations and loans. → PIT Ch7 Venus-2H"""
    normalized_text_zh: str = """"""
    subject: str = "Venus in the Second House (金星过境第二宫)"
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
        l1_anchor="pit_v1.0.0_venus_in_the_second_house__金星过_001_L1",
    )
    version: str = "1.0.0"
