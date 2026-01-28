# Deep Calibration Card

## S - Synopsis

- `card_id`: `tetr_r13_signs_001`
- `semantic_unit`: `Ptolemy classifies zodiacal signs by modality (tropical/equinoctial/fixed/bicorporeal), gender (masculine/feminine), and mutual configurations (aspects), grounding these in seasonal and geometric principles.`
- `source_range`: `典籍/texts/Tetrabiblos/原文/Tetrabiblos.md:2097` ~ `:2227`
- `depth_level`: `Deep`
- `confidence`: `High`
- `last_updated`: `2026-01-28`

### Core Thesis in One Sentence
> Signs derive their qualities from their seasonal position (tropical at solstices, equinoctial at equinoxes, fixed after these, bicorporeal between) and their geometric relationships (aspects based on angular distance), with masculine/feminine alternating from Aries.

---

## L1 - Deep Comprehension Layer

### L1.1 Source Text and Context

**Source Text** (Chapters XIV-XVI condensed):
> Among the twelve signs, some are termed tropical, others equinoctial, others fixed, and others bicorporeal.  
>   
> The tropical signs are two: viz. the first thirty degrees after the summer solstice, which compose the sign of Cancer; and the first thirty degrees after the winter solstice, composing the sign of Capricorn. These are called _tropical_, because the Sun, after he has arrived at their first points, seems to _turn_, and to change his course towards a contrary latitude...  
>   
> There are also two equinoctial signs: Aries, the first after the vernal equinox; and Libra, the first after the autumnal equinox...  
>   
> Of the remaining eight signs, four are fixed, and four bicorporeal. Those signs, which severally follow immediately after the two tropical and the two equinoctial signs, are termed fixed... The bicorporeal signs severally follow the fixed signs; and, being thus intermediately placed between the fixed and the tropical signs, they participate in the constitutional properties of both...  
>   
> Again, among the twelve signs, six are called masculine and diurnal, and six feminine and nocturnal. They are arranged in alternate order...  
>   
> There are certain familiarities or connections between different parts of the zodiac; and the chief of these is that which exists between such parts as are configurated with each other. This mutual configuration attaches to all parts diametrically distant from each other... also in all parts at the triangular distance... also, in all parts at the quadrate distance... and, also, in all parts at the hexagonal distance...

**Context Analysis**:

| Dimension | Analysis |
|:---|:---|
| Preceding context | Planetary qualities and classifications (Chapters IV-VII) have established the "actors"; now the zodiac provides the "stage." |
| Following direction | Chapters XVII-XXVII detail additional sign properties (commanding/obeying, houses, triplicities, exaltations, terms). |
| Overall positioning | Book I, Chapters XIV-XVI: foundational sign taxonomy that underpins all chart interpretation. |

### L1.2 Historical Background and Academic Lineage (Brief)

| Dimension | Content |
|:---|:---|
| Writing context | Ptolemy systematizes inherited Hellenistic sign classifications, grounding them in astronomical (seasonal) and geometric (aspect) rationale. |
| Academic lineage | Modal classification (cardinal/fixed/mutable in modern terms) is ancient; aspect doctrine derives from Pythagorean harmonic ratios. |
| Later developments | Modern astrology uses "cardinal/fixed/mutable" for Ptolemy's "tropical/fixed/bicorporeal" with semantic continuity. |

---

## L3 - Semantic Essence Layer

### L3.1 Core Concept Deconstruction

| Concept | Literal Meaning | Deep Semantics | Modern Reconstruction |
|:---|:---|:---|:---|
| `tropical` (Cardinal) | turning | Signs at solstices where the Sun's declination reverses; initiating energy | `modality_cardinal`: initiating, activating |
| `equinoctial` | equal night | Signs at equinoxes where day=night; balance/pivot points | `modality_cardinal` (Aries/Libra are also cardinal) |
| `fixed` | stable | Signs following cardinal; seasonal qualities are "established" | `modality_fixed`: sustaining, consolidating |
| `bicorporeal` (Mutable) | double-bodied | Signs between fixed and cardinal; transitional, adaptable | `modality_mutable`: changing, synthesizing |
| `aspect` | configuration | Angular relationships (60°/90°/120°/180°) that create familiarity or tension | `aspect_type`: geometric relationship with semantic implications |

### L3.2 Abstract Rule Extraction

**Rule ID**: `rule_tetr_sign_modality`

**Rule Structure** (pseudo-code form):

```
IF sign IN {Aries, Cancer, Libra, Capricorn}
THEN modality = cardinal (tropical/equinoctial)
BECAUSE <Tetrabiblos I.14, lines 2102-2116>

IF sign IN {Taurus, Leo, Scorpio, Aquarius}
THEN modality = fixed
BECAUSE <Tetrabiblos I.14, lines 2118-2126>

IF sign IN {Gemini, Virgo, Sagittarius, Pisces}
THEN modality = mutable (bicorporeal)
BECAUSE <Tetrabiblos I.14, lines 2128-2131>
```

**Rule Operationalization**:

| Dimension | Explanation |
|:---|:---|
| Trigger operationalization | Identify sign placement of any planet or angle in chart; classify by modality. |
| Conclusion operationalization | Modality informs behavioral tendency: cardinal=initiate, fixed=sustain, mutable=adapt. |
| Confidence rationale | High: explicit enumeration with astronomical grounding. |

### L3.3 Factor Extraction (Semantic Level)

| Factor Label | Factor ID | Semantic Essence | Extraction Justification |
|:---|:---|:---|:---|
| Sign modality | `sign_modality` | Cardinal/fixed/mutable classification | Chapter XIV explicitly defines. |
| Sign gender | `sign_gender` | Masculine/feminine alternation | Chapter XV defines alternating pattern from Aries. |
| Aspect type | `aspect_type` | Sextile (60°), square (90°), trine (120°), opposition (180°) | Chapter XVI defines configurations geometrically. |

**Factor Status**: `existing` (sign_modality, sign_gender, aspect_type already in tetrabiblos_factors.yaml)

---

## L4 - Cross-System Bridge Layer

### L4.1 Functional Equivalence Analysis

**Core Function**: Classify signs by behavioral mode (initiate/sustain/adapt) and relational geometry (harmonious vs tense aspects).

| Target System | Corresponding Concept | Functional Equivalence Argument | Academic Basis |
|:---|:---|:---|:---|
| BaZi (bazi) | 地支三合/六合/相冲/相刑 | Both systems define structural relationships between zodiacal positions that modify interpretation (harmony vs conflict). | Structural analogy: geometric relationships → semantic implications. |

### L4.3 Neutral Semantic Tag Mapping

| neutral_tag | Mapping Rationale | Applicability Limits |
|:---|:---|:---|
| `neutral_timing_fast` | Cardinal signs associated with initiation and action | Only as baseline tendency; actual speed depends on planetary configuration. |
| `neutral_timing_slow` | Fixed signs associated with stability and persistence | Same caveat. |

---

## L5 - Validation and Calibration Layer

### L5.1 Text-Internal Validation

**Case Source**: Tetrabiblos Book III marriage chapter (bicorporeal signs → multiple marriages)

| Case Description | Conditions Met | Rule-Based Prediction | Actual Outcome | Validation Status |
|:---|:---|:---|:---|:---|
| Book IV.5 states if Moon is in bicorporeal sign, men may marry multiple times. | Modality classification applied to marriage significator. | Bicorporeal = multiple/variable outcomes should be consistent. | Book IV explicitly uses bicorporeal → multiple marriages, matching the modality definition. | `Validated` |

---

## L6 - Meta-Reflection Layer

### L6.2 Uncertainty Annotation (Simplified)

| Layer | Uncertainty | Notes |
|:---|:---|:---|
| L1 Understanding | `Low` | Explicit enumeration and geometric grounding. |
| L3 Extraction | `Low` | Classifications are unambiguous. |
| L4 Mapping | `Medium` | BaZi relationship types are structurally similar but not identical. |
| L5 Validation | `Low` | Internal consistency with Book IV is strong. |

---

## Appendix

### A2 - Revision History

| Date | Reviser | Revision Content |
|:---|:---|:---|
| 2026-01-28 | LS-CAL-R13-TETR | Initial creation: Deep calibration for Book I signs (qualities/temperaments) |
