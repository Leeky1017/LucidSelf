"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.258747
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
    semantic_id="pit_v1.0.0_venus_in_the_sixth_house__金星过境_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusInTheSixthHouse金星过境(SemanticEntry):
    """
    **Source Text** (Lines 6904-6921):
> Sixth house intrinsically incompatible with Venus. Subordinate ...
    """
    
    original_text: str = """**Source Text** (Lines 6904-6921):
> Sixth house intrinsically incompatible with Venus. Subordinate desire for amusement to present needs. Confront relationship difficulties not handled earlier. Discuss tacit agreements openly. Accept real duties and obligations. Good for work/profession—enjoy good relationships with superiors/employees. May gain favors from employer. Good for health but avoid sweet/fattening foods. Practical matters important—least romantic Venus position.

**English Paraphrase**: Subordinate pleasure to duty. Confront relationship issues. Discuss tacit agreements. Good for work relationships. Practical matters important. Least romantic position.

**Complete Chinese Interpretation**: 将快乐服从于责任。面对关系问题。讨论默契。适合工作关系。实际事务重要。最不浪漫的位置。

**Narrative Snippets**:
- `[ns_pit_ve006]` `[trigger: venus_transit_house_6]` `[factor_trigger: astro_transit_venus AND astro_house_6]` `[role: 主干]` Subordinate pleasure to duty. Good for work relationships. Practical matters important. → PIT Ch7 Venus-6H"""
    normalized_text_zh: str = """"""
    subject: str = "Venus in the Sixth House (金星过境第六宫)"
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
        l1_anchor="pit_v1.0.0_venus_in_the_sixth_house__金星过境_001_L1",
    )
    version: str = "1.0.0"
