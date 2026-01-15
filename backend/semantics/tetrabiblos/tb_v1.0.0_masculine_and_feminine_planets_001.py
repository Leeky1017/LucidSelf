"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182487
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
    semantic_id="tb_v1.0.0_masculine_and_feminine_planets_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class MasculineAndFemininePlanets(SemanticEntry):
    """
    **Source Text** (Lines 1670-1691):
> There are two primary sexes, male and female; and the female se...
    """
    
    original_text: str = """**Source Text** (Lines 1670-1691):
> There are two primary sexes, male and female; and the female sex partakes chiefly of moisture. The Moon and Venus are therefore said to be feminine, since their qualities are principally moist. The Sun, Saturn, Jupiter, and Mars are called masculine. Mercury is common to both genders, because at certain times he produces dryness, and at others moisture, and performs each in an equal ratio. The stars, however, are also said to be masculine and feminine, by their positions with regard to the Sun. While they are matutine and preceding the Sun, they are masculine; when vespertine and following the Sun, they become feminine. And they are further regulated in this respect by their positions with regard to the horizon. From the ascendant to the mid-heaven, or from the angle of the west to the lower heaven, they are considered to be masculine, being then oriental: and in the other two quadrants, feminine, being then occidental.

**English Paraphrase (Primary Language)**:
Ptolemy assigns gender to planets based on elemental qualities: **moisture = feminine, dryness = masculine**. Moon and Venus are feminine (moist); Sun, Saturn, Jupiter, Mars are masculine (dry or hot). Mercury is hermaphroditic, alternating between qualities.

Beyond inherent nature, planets also acquire **situational gender** through:
1. **Position relative to Sun**: Matutine (rising before Sun) = masculine; Vespertine (setting after Sun) = feminine
2. **Position relative to horizon**: Eastern quadrants (ASC-MC, DSC-IC) = masculine/oriental; Western quadrants = feminine/occidental

This creates a dynamic system where a naturally feminine planet (Venus) can become masculinized by oriental position, and vice versa.

**Complete Chinese Interpretation (Secondary Language)**:
托勒密根据元素属性为行星分配性别：**湿润=阴性，干燥=阳性**。月亮和金星是阴性的（湿润）；太阳、土星、木星、火星是阳性的（干燥或炎热）。水星是双性的，在两种属性之间交替。

除了固有本质外，行星还通过以下方式获得**情境性别**：
1. **相对于太阳的位置**：晨星（在太阳之前升起）=阳性；昏星（在太阳之后落下）=阴性
2. **相对于地平线的位置**：东方象限（上升-中天，下降-天底）=阳性/东方；西方象限=阴性/西方

这创造了一个动态系统，其中天生阴性的行星（金星）可以通过东方位置变得阳性化，反之亦然。

**Core Points**:
- Feminine = moist (Moon, Venus); Masculine = dry/hot (Sun, Saturn, Jupiter, Mars)
- Mercury is common to both genders (variable)
- Matutine position (before Sun) = masculine
- Vespertine position (after Sun) = feminine
- Eastern quadrants = masculine/oriental
- Western quadrants = feminine/occidental
- Gender is both inherent and situational

**Narrative Snippets**:
- `[ns_tetra_i027]` `[trigger: planet_gender]` `[factor_trigger: sign_gender AND planet_oriental AND planet_masculine]` `[role: 主干]` Moon and Venus are feminine since their qualities are principally moist; Sun, Saturn, Jupiter, Mars are masculine. → Source Text I.6
- `[ns_tetra_i028]` `[trigger: mercury_dual]` `[factor_trigger: planet_position_sun AND lunar_phase]` `[role: 条件分支]` Mercury is common to both genders, producing dryness at certain times and moisture at others. → Source Text I.6
- `[ns_tetra_i029]` `[trigger: matutine_vespertine]` `[factor_trigger: no_relationship AND season_quality]` `[role: 条件分支]` Matutine and preceding the Sun = masculine; vespertine and following the Sun = feminine. → Source Text I.6

**Textual Criticism**: N/A: Consistent across all manuscripts."""
    normalized_text_zh: str = """"""
    subject: str = "Masculine and Feminine Planets (Chapter VI)"
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
        book_id="tetrabiblos",
        chapter="",
        l1_anchor="tb_v1.0.0_masculine_and_feminine_planets_001_L1",
    )
    version: str = "1.0.0"
