"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333660
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
    semantic_id="ah_v1.0.0_sidereal_vs_tropical_zodiac_de_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class SiderealVsTropicalZodiacDe(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Sidereal | Constellation...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Sidereal | Constellation-based | Pantheistic |
| Tropical | Orbit-based | Monotheistic |
| Precession | 23° drift | Technical cause |
| Cosmological Choice | Multiple vs single | Philosophy |

#### Source Text

"The sidereal zodiac is based on the actual constellations, reflecting a pantheistic cosmology where the twelve star-groups represent creative hierarchies channeling galactic energies through the Sun. The tropical zodiac is based on Earth's orbital relationship to the Sun, reflecting a monotheistic cosmology where the Sun is the one divine center and the twelve signs mark twelve avenues of the soul. Rudhyar advocates the tropical zodiac as appropriate for modern individualized consciousness."

#### English Paraphrase (Primary Language)

Two competing zodiacal systems exist: sidereal and tropical. The sidereal zodiac aligns with the actual star constellations, treating them as cosmic hierarchies that channel energies from galactic center through the Sun to Earth—a pantheistic view where multiple divine powers operate through stellar configurations. The tropical zodiac ignores constellation positions, instead using Earth's orbital relationship to the Sun as measured by the equinoxes and solstices—a monotheistic view where the Sun alone is the divine center, and the twelve signs represent qualities of the Earth-Sun dialogue. Due to precession of the equinoxes, these two zodiacs have drifted 23° apart over two millennia. Rudhyar argues the tropical zodiac better serves modern consciousness focused on individual development within the Earth-Sun relationship.

#### Complete Chinese Interpretation (Secondary Language)

**恒星星座**(Sidereal)使用固定恒星背景作为参考框架，反映多层级星空和泛神论宇宙观，太阳只是众多神性力量之一。**回归星座**(Tropical)使用春分点(太阳回归点)作为白羊座0度，反映太阳中心和一神论宇宙观，太阳是唯一神圣来源。由于**岁差**(precession)——地轴2.6万年缓慢摆动——回归春分点每72年后退1度，现在与恒星春分点相差约23度。这不仅是技术差异，而是哲学选择：恒星系统说"星空群体是神"，回归系统说"太阳是神"。西方占星主要用回归(季节/太阳节奏)，印度占星主要用恒星(星群模式)。

#### Core Points

- **Sidereal**: Constellation-based, pantheistic, galactic hierarchy
#### L2 Semantic Extraction

- **Theme**: Two zodiacal systems reflecting fundamentally different cosmologies and consciousness structures

- **Natural Attributes**:
  - Symbolism: Pantheism vs Monotheism, Galactic vs Solar, Collective vs Individual
  - Characteristics: Sidereal (constellations, multiple hierarchies), Tropical (Earth-Sun, singular divinity)
  - Elements: Precession (23° drift), Equinox/Solstice markers, Stellar vs orbital reference

- **Functional Symbolism**:
  - Sidereal function: Channels galactic energies through stellar hierarchies
  - Tropical function: Defines soul development through Earth-Sun relationship
  - Choice function: Reflects cosmological and consciousness assumptions

- **Conditional Structure**:
  - Necessary Conditions: Awareness of theological implications, understanding of monotheistic vs pantheistic worldviews
  - Enhancing Conditions: Knowledge of constellation mythology vs solar cycle symbolism
  - Nullifying Conditions: Treating astrology as value-neutral technique, ignoring spiritual/philosophical foundations

- **Multi-layered Interpretation**:
  - Literal Layer: Constellation alignment vs equinox alignment
  - Symbolic Layer: Space hierarchies vs relationship dialogue
  - Practical Layer: Vedic astrology (sidereal) vs Western astrology (tropical)
  - Philosophical Layer: Pantheistic multiplicity vs monotheistic unity

---

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition |
|--------------|--------------|-------------------|-------------------|
| Sidereal Zodiac | 恒星星座 | Constellation-based, pantheistic, galactic hierarchy | 星群基础，泛神论，银河等级 |
| Tropical Zodiac | 回归星座 | Orbit-based, monotheistic, Sun-centered | 轨道基础，一神论，太阳中心 |
| Precession | 岁差 | 26,000-year wobble creating 23° discrepancy | 2.6万年摆动造成23度差异 |
| Philosophical Choice | 哲学选择 | Sidereal (multiple gods) vs Tropical (one god) | 恒星（多神）vs 回归（一神） |

---

#### Factor Layer

<!-- L2_END -->
<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | Notes | engine_id |
|-------------|--------------|-----------|---------------|---------------|-------------------|-------|------------|
| **Structure** | Sidereal zodiac | zodiac_sidereal | existing | Zodiac System | Constellation-based | Pantheistic | astro_semantic |
| **Structure** | Tropical zodiac | zodiac_tropical | existing | Zodiac System | Equinox-based | Monotheistic | astro_semantic |
| **Temporal** | Precession drift | | new_candidate | Astronomical | ~23° current difference | Increases ~1° per 72 years | astro_semantic |
| **State** | Pantheistic cosmology | | new_candidate | Worldview | Multiple divine hierarchies | Galactic-centered | astro_semantic |
| **State** | Monotheistic cosmology | | new_candidate | Worldview | Single divine center (Sun) | Solar-centered | astro_semantic |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_House_Philosophy_12H_6 | concept | House_Philosophy_12H_6 | system | Framework | When framework connects concept to system interpretation | connecting | Source |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_House_Philosophy_12H_6 | "Source" | House_Philosophy_12H_6 | Concept -> application | Theory | High | Yes | rule_House_Philosophy_12H_6 |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_House_Philosophy_12H_6 | Core concept | | relevant | relevant | relevant | System |
<!-- L2.5_END -->

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Rudhyar's sidereal/tropical: cosmological choice. Sidereal = pantheistic (constellation hierarchies). Tropical = monotheistic (Sun as one God). Parallels Chinese 多神教/一神教张力.
- **中文**: Rudhyar的恒星/回归:宇宙论选择。恒星=泛神论(星群等级)。回归=一神论(太阳为唯一神)。平行中国多神教/一神教张力。

---

### 7. Monotheistic vs Pantheistic Cosmology

#### Key Term Analysis"""
    normalized_text_zh: str = """"""
    subject: str = "Sidereal vs Tropical Zodiac Debate"
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
        l1_anchor="ah_v1.0.0_sidereal_vs_tropical_zodiac_de_001_L1",
    )
    version: str = "1.0.0"
