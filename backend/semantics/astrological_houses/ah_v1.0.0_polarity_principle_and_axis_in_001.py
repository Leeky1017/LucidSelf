"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333835
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
    semantic_id="ah_v1.0.0_polarity_principle_and_axis_in_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class PolarityPrincipleAndAxisIn(SemanticEntry):
    """
    #### Source Text

"The most important fact is that everything in a chart has its polar opposite. The...
    """
    
    original_text: str = """#### Source Text

"The most important fact is that everything in a chart has its polar opposite. The horizon and meridian are axes; the Ascendant and Descendant, the Zenith and Nadir are theoretical ends of these axes. To define the meaning of one end without including the meaning of the other end simply does not make sense. If one wishes to describe qualities of a Leo Ascendant, one should take into consideration the inevitable fact that his approach to partnership—Descendant—will have an Aquarius character. One cannot separate the way one sees oneself from the manner in which one meets people and enters partnerships. These two factors—selfhood and relationship—are constantly interacting because they are two interdependent aspects of one fundamental drive, the drive to full individualized consciousness."

#### English Paraphrase (Primary Language)

Rudhyar establishes the polarity principle as the cornerstone of sound astrological interpretation. Every point in a chart implies its opposite—the horizon connects Ascendant (selfhood) and Descendant (relationship), while the meridian links Nadir (private integration) and Zenith (public achievement). To interpret any angle without its opposite produces incomplete understanding. This bipolar approach recognizes that consciousness itself is inherently relational: you cannot be conscious alone, in a vacuum. Selfhood and relationship are not separate factors but interdependent aspects of the single drive toward individualized consciousness.

#### Complete Chinese Interpretation (Secondary Language)

鲁迪亚将**极性原则**确立为健全占星解释的基石。命盘中每一点都暗含其对立面——地平线连接上升点（自我）和下降点（关系），子午线连接天底（私人整合）和天顶（公共成就）。

**轴线解释原则**：
- 地平线轴 = 意识轴：上升点（自我认知）↔ 下降点（关系方式）
- 子午线轴 = 力量轴：天底（私人力量）↔ 天顶（社会力量）

解释任何角度而不考虑其对立面会产生不完整的理解。这种双极方法认识到意识本身是关系性的：你无法独自在真空中保持意识。自我与关系不是分离的因素，而是朝向个体化意识的单一驱动的相互依存方面。

#### Core Points

- **Polarity cornerstone**: Everything implies its opposite
- **Horizon axis**: Connects selfhood (ASC) and relationship (DSC)
- **Meridian axis**: Links private integration (IC) and public achievement (MC)
- **Interdependence**: Selfhood and relationship are two aspects of one drive
- **Relational consciousness**: Cannot be conscious alone, in vacuum
- **Complete interpretation**: Must include both ends of any axis

#### Narrative Snippets

- `[ns_houses_032]` `[trigger: polarity_principle]` `[factor_trigger: astro_ascendant AND astro_descendant]` `[role: 主干]` One cannot separate the way one sees oneself from the manner in which one meets people—selfhood and relationship are interdependent aspects of one fundamental drive. → Polarity Principle
- `[ns_houses_033]` `[trigger: axis_interpretation]` `[factor_trigger: astro_horizon OR astro_meridian]` `[role: 主干依赖]` To define the meaning of one end of an axis without including the meaning of the other simply does not make sense—both ends constantly interact. → Polarity Principle"""
    normalized_text_zh: str = """"""
    subject: str = "Polarity Principle and Axis Interpretation"
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
        book_id="astrological_houses",
        chapter="",
        l1_anchor="ah_v1.0.0_polarity_principle_and_axis_in_001_L1",
    )
    version: str = "1.0.0"
