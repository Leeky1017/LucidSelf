"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238159
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
    semantic_id="ap_v1.0.0_entry_5__zodiac_as_planetary_i_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry5ZodiacAsPlanetaryI(SemanticEntry):
    """
    **Source Text** (Lines 8569-8630):
> The Zodiac as the Cycle of the Planetary Individual: So far we ...
    """
    
    original_text: str = """**Source Text** (Lines 8569-8630):
> The Zodiac as the Cycle of the Planetary Individual: So far we have considered zodiacal signs mostly from the point of view of their being a series of cosmic energies projected... by the Macrocosm (the Twelve Hierarchies) upon the microcosm...
>
> But we can also think of the zodiac as the cycle of houses of the planetary Individual Who "dwells at the North Pole," and for Whom a year is as a day...
>
> The zodiac gives us a knowledge of the life-contents of every living entity. The houses tell us the manner in which these contents are distributed in a form of selfhood and destiny. The Planets are focal points for and symbols of all life-activities. The Degrees give us a clue to the inherent creative significance of all activities.

**Key Term Analysis**:
- **Zodiac dual interpretation**: `cosmic energies (equatorial-collective)` / `consciousness cycle (polar-individual)`
- **Planetary Individual**: `dwells at North Pole` / `year = day`
- **Four-element synthesis**: `Zodiac = life-contents` / `Houses = distribution` / `Planets = activities` / `Degrees = creative significance`

**English Paraphrase (Primary Language)**:
The zodiac has dual interpretation:
1. **Equatorial-collective**: cosmic energies projected from Macrocosm (Twelve Hierarchies)
2. **Polar-individual**: consciousness cycle for the "Planetary Individual" dwelling at North Pole

Four-element synthesis: "The zodiac gives us knowledge of life-contents. Houses = distribution in selfhood. Planets = focal points of activities. Degrees = inherent creative significance."

**Complete Chinese Interpretation (Secondary Language)**:
黄道有双重解释：
1. **赤道-集体**：从大宇宙（十二等级）投射的宇宙能量
2. **极点-个体**：居住在北极的"行星个体"的意识周期

四要素综合："黄道给我们生命内容的知识。宫位 = 在自性中的分布。行星 = 活动的焦点。度数 = 内在的创造性意义。"

**Narrative Snippets**:
- `[ns_aop_173]` `[trigger: zodiac_dual]` `[factor_trigger: astro_zodiac_dual_view AND astro_zodiac_dual]` `[role: 主干]` Zodiac dual view: equatorial-collective (cosmic energies) vs polar-individual (consciousness). → L8569-8594
- `[ns_aop_174]` `[trigger: four_synthesis]` `[factor_trigger: astro_four_elements_synthesis AND astro_four_synthesis AND astro_elements_struct]` `[role: 总结]` Four-element synthesis: Zodiac (contents) + Houses (distribution) + Planets (activities) + Degrees (significance). → L8624-8630"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 5: Zodiac as Planetary Individual Cycle"
    factor_refs: list = ['planetary_individual', 'four_synthesis']
    
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
        l1_anchor="ap_v1.0.0_entry_5__zodiac_as_planetary_i_001_L1",
    )
    version: str = "1.0.0"
