"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.192523
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
    semantic_id="tb_v1.0.0_proem_to_genethliacal_astrolog_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class ProemToGenethliacalAstrolog(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Genethliacal | Relating to birth/nativity | Individual astrology |
| Universal | Affecting nations/regions | Mundane astrology |
| Particular | Affecting individuals | Natal astrology |

#### Source Text

"The consideration of nativities, or genethliacal astrology, must be now entered upon. The doctrine of nativities consists of two parts: one to be contemplated before the birth, the other after. The rules for prenatal consideration are directed to the ascertainment of the conception, and to the casting of the corresponding figure. The rules for postnatal consideration lead to the ascertainment of the hour of the nativity, and the casting of the nativity figure."

#### English Paraphrase (Primary Language)

**Genethliacal astrology** (natal astrology) forms the individual counterpart to mundane/universal astrology. Ptolemy divides this study into two temporal domains:

1. **Prenatal consideration**: Determining conception time and its astrological figure
2. **Postnatal consideration**: Establishing birth time and the nativity chart

This dual framework acknowledges that the soul's incarnation involves both the **moment of conception** (seed) and the **moment of birth** (manifestation). The nativity cannot be fully understood without considering both.

**Foundation principle**: Individual destiny operates within the larger cosmic framework established by mundane influences (regional, temporal, seasonal).

#### Complete Chinese Interpretation (Secondary Language)

**诞生占星学**（本命占星学）构成世运/普遍占星学的个体对应。托勒密将此研究分为两个时间领域：

1. **产前考量**：确定受孕时间及其占星图象
2. **产后考量**：确立出生时间和本命盘

这种双重框架承认灵魂的化身涉及**受孕时刻**（种子）和**出生时刻**（显化）两者。不考虑两者，本命盘无法被完全理解。

**基础原则**：个体命运在由世运影响（地区、时间、季节）建立的更大宇宙框架内运作。

#### Core Points

- **Genethliacal astrology**: Study of individual nativities
- **Two temporal domains**: Prenatal (conception) and postnatal (birth)
- **Dual consideration**: Both conception and birth matter
- **Hierarchical framework**: Individual within universal

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Ptolemy's emphasis on conception as well as birth distinguishes his approach from later medieval astrology that focused primarily on birth charts. Modern research on prenatal astrology draws on this Ptolemaic foundation.
- **中文**: 托勒密对受孕和出生的双重强调使其方法区别于后来主要关注出生图的中世纪占星术。现代产前占星研究借鉴了这一托勒密基础。

**Narrative Snippets**:
- `[ns_ptolemy_iii_001]` `[trigger: genethliacal]` `[factor_trigger: astro_genethliacal AND astro_nativity AND genethliacal AND prenatal_postnatal AND mundane_natal AND natal_chart AND complete_analysis]` `[role: 主干]` Genethliacal astrology consists of prenatal (conception) and postnatal (birth) considerations. → Source Text
- `[ns_ptolemy_iii_002]` `[trigger: individual_destiny]` `[factor_trigger: astro_individual AND astro_cosmic]` `[role: 主干依赖]` Individual destiny operates within the larger cosmic framework of mundane influences. → English Paraphrase
- `[ns_ptolemy_iii_027]` `[trigger: nativity_doctrine]` `[factor_trigger: astro_nativity AND astro_method]` `[role: 条件分支]` The doctrine of nativities consists of rules for prenatal consideration and rules for postnatal casting of nativity figure. → Method"""
    normalized_text_zh: str = """"""
    subject: str = "Proem to Genethliacal Astrology"
    factor_refs: list = ['genethliacal', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="tb_v1.0.0_proem_to_genethliacal_astrolog_001_L1",
    )
    version: str = "1.0.0"
