"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.192581
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
    semantic_id="tb_v1.0.0_degree_of_the_horoscopic_point_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class DegreeOfTheHoroscopicPoint(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Horoscope | Ascending degree | Chart anchor |
| Ascendant | Rising sign/degree | Personal expression |
| Exact degree | Precise zodiacal position | Accuracy essential |

#### Source Text

"The horoscopic point is to be taken as the angle of the chart; and its exact degree is to be carefully ascertained, because, on the correct determination of this degree, the whole validity of the nativity depends."

#### English Paraphrase (Primary Language)

The **Ascendant** (horoscopic point) serves as the primary anchor of the natal chart. Ptolemy emphasizes that **accuracy is paramount**—the entire validity of astrological interpretation depends on correct determination of the ascending degree.

**Technical requirement**: The Ascendant must be calculated to the exact degree, not merely the rising sign. A few degrees of error can significantly alter house cusps and planetary positions relative to angles.

**Foundation status**: Among all chart points, the Ascendant holds primacy because it establishes the framework for all other house positions.

#### Complete Chinese Interpretation (Secondary Language)

**上升点**（天宫点）作为本命盘的主要锚点。托勒密强调**准确性至关重要**——占星诠释的全部有效性取决于对上升度数的正确确定。

**技术要求**：上升点必须计算到精确度数，而非仅仅上升星座。几度的误差可以显著改变宫位尖端和行星相对于角宫的位置。

**基础地位**：在所有盘中点位中，上升点具有首要地位，因为它为所有其他宫位建立框架。

#### Core Points

- **Ascendant primacy**: Most important chart point
- **Exact degree required**: Not just sign, but precise degree
- **Foundation function**: Establishes all house positions
- **Validity dependent**: Entire chart interpretation depends on accuracy

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Ptolemy's insistence on exact degree calculation established a standard that persists in modern astrology. This contrasts with some Hellenistic whole-sign house systems that are less degree-sensitive.
- **中文**: 托勒密对精确度数计算的坚持建立了在现代占星术中持续存在的标准。这与一些对度数不太敏感的希腊化整宫制形成对比。

**Narrative Snippets**:
- `[ns_ptolemy_iii_003]` `[trigger: ascendant]` `[factor_trigger: astro_ascendant AND astro_anchor]` `[role: 主干]` The horoscopic point is the anchor of the chart; its exact degree determines the validity of the whole nativity. → Source Text
- `[ns_ptolemy_iii_004]` `[trigger: accuracy]` `[factor_trigger: astro_accuracy AND astro_validity]` `[role: 主干依赖]` A few degrees of error can significantly alter house cusps and planetary positions. → English Paraphrase
- `[ns_tetra_iii_hf]` `[trigger: house_framework]` `[factor_trigger: house_framework]` `[role: 主干]` House framework is established by the Ascendant degree—all twelve houses derive their positions from this primary anchor. → Ptolemy III
- `[ns_tetra_iii_dc]` `[trigger: degree_calc]` `[factor_trigger: degree_calc]` `[role: 条件分支]` Degree calculation accuracy is essential—errors cascade through entire interpretation since all positions are relative. → Ptolemy III
- `[ns_tetra_iii_int]` `[trigger: interpretation]` `[factor_trigger: interpretation]` `[role: 效果]` Interpretation validity depends on accurate degree calculations—the entire nativity's meaning flows from correct foundational positions. → Ptolemy III"""
    normalized_text_zh: str = """"""
    subject: str = "Degree of the Horoscopic Point (Chapter III)"
    factor_refs: list = ['horoscope', 'ascendant', 'new_candidate']
    
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
        l1_anchor="tb_v1.0.0_degree_of_the_horoscopic_point_001_L1",
    )
    version: str = "1.0.0"
