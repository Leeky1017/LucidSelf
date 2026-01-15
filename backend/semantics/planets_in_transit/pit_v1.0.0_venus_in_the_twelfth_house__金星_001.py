"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.258884
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
    semantic_id="pit_v1.0.0_venus_in_the_twelfth_house__金星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusInTheTwelfthHouse金星(SemanticEntry):
    """
    **Source Text** (Lines 7020-7041):
> One of best planetary transits through difficult 12H. At highes...
    """
    
    original_text: str = """**Source Text** (Lines 7020-7041):
> One of best planetary transits through difficult 12H. At highest, unusual selflessness in love. May care for loved one in need, or charitable activity. May not get immediate gratification but greater rewards later. Avoid playing martyr. If cannot serve selflessly, do nothing. May endure difficult psychological energies as unresolved relationship problems surface. Forbearance and grace will work to advantage. Spiritual rewards and real satisfaction.

**English Paraphrase**: Best Venus through 12H. Selflessness in love. May care for others. Delayed rewards. Avoid martyrdom. Unresolved issues surface. Forbearance brings advantage. Spiritual rewards.

**Complete Chinese Interpretation**: 金星过第十二宫最佳。爱中的无私。可能照顾他人。延迟的回报。避免殉道。未解决的问题浮出水面。忍耐带来优势。精神回报。

**Narrative Snippets**:
- `[ns_pit_ve012]` `[trigger: venus_transit_house_12]` `[factor_trigger: astro_transit_venus AND astro_house_12]` `[role: 主干]` Selflessness in love. May care for others. Avoid martyrdom. Spiritual rewards. → PIT Ch7 Venus-12H"""
    normalized_text_zh: str = """"""
    subject: str = "Venus in the Twelfth House (金星过境第十二宫)"
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
        l1_anchor="pit_v1.0.0_venus_in_the_twelfth_house__金星_001_L1",
    )
    version: str = "1.0.0"
