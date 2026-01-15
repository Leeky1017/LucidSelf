"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238070
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
    semantic_id="ap_v1.0.0_entry_1__houses_as_individual__001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry1HousesAsIndividual(SemanticEntry):
    """
    **Source Text** (Lines 7108-7141):
> At the beginning it may be well to try to clear up a point whic...
    """
    
    original_text: str = """**Source Text** (Lines 7108-7141):
> At the beginning it may be well to try to clear up a point which has puzzled students of astrology. If we look at an ordinary birth-chart... we find a wheel divided by twelve spokes into twelve geometrically equal sections of 30 degrees of arc...
>
> What brings a relative uniqueness to an individual is the way this twelve-fold framework is correlated to the zodiac. And this correlation is indicated by the degrees and signs of the zodiac written at the beginning (or cusp) of each house...
>
> When we speak of "individual" we do not mean the "absolutely unique"; we refer to that which assumes the position and significance of uniqueness.

**Key Term Analysis**:
- **Twelve houses**: `generic framework same for all` / `individual selfhood structure`
- **Houses-Zodiac correlation**: `brings relative uniqueness` / `cusps show zodiac degrees`
- **Individual defined**: `not absolutely unique` / `assumes position and significance of uniqueness`

**English Paraphrase (Primary Language)**:
The twelve-house framework is geometrically identical for all charts—representing the generic structure of individual selfhood. What makes each individual relatively unique is how this framework correlates to the zodiac (cusp positions).

"When we speak of 'individual' we do not mean the 'absolutely unique'; we refer to that which assumes the position and significance of uniqueness."

**Complete Chinese Interpretation (Secondary Language)**:
十二宫框架在几何上对所有图都相同——代表个体自性的通用结构。使每个个体相对独特的是这个框架如何与黄道关联（宫首位置）。

"当我们说'个体'时，我们不是指'绝对独特'；我们指的是那种承担独特性的位置和意义的东西。"

**Narrative Snippets**:
- `[ns_aop_155]` `[trigger: houses_framework]` `[factor_trigger: astro_houses_generic AND houses_framework]` `[role: 主干]` Houses: generic framework same for all, individual selfhood structure. → L7117-7123
- `[ns_aop_156]` `[trigger: individuality_defined]` `[factor_trigger: astro_individuality_def]` `[role: 总结]` Individual = assumes position and significance of uniqueness, not absolutely unique. → L7135-7141"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 1: Houses as Individual Framework"
    factor_refs: list = ['houses_twelve', 'house_cusps']
    
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
        book_id="astrology_personality",
        chapter="",
        l1_anchor="ap_v1.0.0_entry_1__houses_as_individual__001_L1",
    )
    version: str = "1.0.0"
