"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.258772
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
    semantic_id="pit_v1.0.0_venus_in_the_seventh_house__金星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusInTheSeventhHouse金星(SemanticEntry):
    """
    **Source Text** (Lines 6922-6941):
> One of best positions for all relationships. Ego forces in tune...
    """
    
    original_text: str = """**Source Text** (Lines 6922-6941):
> One of best positions for all relationships. Ego forces in tune—proper balance between yourself and everyone you meet. Express affection easily in marriage/love. New love may enter life. In partnerships, understand partner's needs. Be careful not to let amiability prevent standing up for rights. Best transit for making peace with enemies, settling lawsuits out of court.

**English Paraphrase**: Best for all relationships. Balance with others. Express affection easily. May meet new love. Understand partner's needs. Best for making peace, settling conflicts.

**Complete Chinese Interpretation**: 对所有关系最好。与他人平衡。轻松表达感情。可能遇到新的爱情。理解伴侣的需求。最适合和解、解决冲突。

**Narrative Snippets**:
- `[ns_pit_ve007]` `[trigger: venus_transit_house_7]` `[factor_trigger: astro_transit_venus AND astro_house_7]` `[role: 主干]` Best for all relationships. Express affection easily. Best for making peace. → PIT Ch7 Venus-7H"""
    normalized_text_zh: str = """"""
    subject: str = "Venus in the Seventh House (金星过境第七宫)"
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
        l1_anchor="pit_v1.0.0_venus_in_the_seventh_house__金星_001_L1",
    )
    version: str = "1.0.0"
