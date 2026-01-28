# Deep Calibration Card

## S - Synopsis

- `card_id`: `tetr_r20_domains_001`
- `semantic_unit`: `Ptolemy describes how to judge marriage from Venus (for men) and Mars (for women), with sign modality, benefic/malefic aspects, and luminary configurations determining marriage quality and number.`
- `source_range`: `典籍/texts/Tetrabiblos/原文/Tetrabiblos.md:7400` ~ `:7530`
- `depth_level`: `Deep`
- `confidence`: `High`
- `last_updated`: `2026-01-28`

### Core Thesis in One Sentence
> Marriage is judged from Venus (for men) and Mars (for women): benefic configurations produce harmonious unions, malefic configurations produce strife or separation, and bicorporeal signs indicate multiple marriages.

---

## L1 - Deep Comprehension Layer

### L1.1 Source Text and Context

**Source Text** (Book IV Chapter V condensed):
> The consideration of marriage is taken from the positions of Venus and the Moon in male nativities and from Mars and the Sun in female nativities...
>
> When Venus is found in the sign of Saturn or Mars, or is configurated with them by opposition or quadrature, the marriage will not be fortunate... If she be found in her own places, or in those of Jupiter, or configurated with Jupiter or with the Sun, the marriage is advantageous and happy...
>
> If Venus be placed in a bicorporeal sign, she produces more than one marriage, and especially if she be also configurated with some planet in a bicorporeal sign... If she be in tropical signs, the person marries late; in fixed signs, only once...
>
> For females, the consideration is similarly taken from Mars: if Mars be well placed and with benefics, the husband is good; if ill-placed or with malefics, the husband is troublesome or the marriage ends...

**Context Analysis**:

| Dimension | Analysis |
|:---|:---|
| Preceding context | Chapters II-IV addressed wealth, rank, and employment. |
| Following direction | Chapters VI-VII continue with children and friends. |
| Overall positioning | Book IV, Chapter V: relationship and partnership delineation. |

### L1.2 Historical Background (Brief)

| Dimension | Content |
|:---|:---|
| Writing context | Roman-era marriage norms (patriarchal, often arranged) inform Ptolemy's framing. |
| Academic lineage | Venus/Mars as marriage significators by gender is ancient Hellenistic doctrine. |
| Later developments | Medieval and modern traditional astrology continue to use these significators with refinements. |

---

## L3 - Semantic Essence Layer

### L3.1 Core Concept Deconstruction

| Concept | Literal Meaning | Deep Semantics | Modern Reconstruction |
|:---|:---|:---|:---|
| Venus (male charts) | love/relationship | Primary significator of spouse/partner for men | spouse_significator_male |
| Mars (female charts) | husband | Primary significator of spouse/partner for women | spouse_significator_female |
| bicorporeal sign | double-bodied | Gemini, Virgo, Sagittarius, Pisces = multiple or changeable outcomes | modality_mutable |
| tropical sign | cardinal | Late marriage; initiating new phases | modality_cardinal |
| fixed sign | stable | Single marriage; stable unions | modality_fixed |

### L3.2 Abstract Rule Extraction

**Rule ID**: `rule_tetr_marriage_venus_mars`

```
FOR male_nativity:
  IF Venus is_in benefic_sign AND with Jupiter_or_Sun
  THEN marriage = fortunate, partner = good
  BECAUSE <Tetrabiblos IV.5, lines 7418-7425>
  
  IF Venus is_in bicorporeal_sign
  THEN marriages = multiple
  BECAUSE <Tetrabiblos IV.5, lines 7448-7455>

FOR female_nativity:
  IF Mars is_in benefic_configuration
  THEN husband = good, marriage = stable
  IF Mars is_in malefic_configuration
  THEN husband = troublesome, marriage = difficult
  BECAUSE <Tetrabiblos IV.5, lines 7498-7515>
```

**Rule Operationalization**:

| Dimension | Explanation |
|:---|:---|
| Trigger operationalization | Identify gender of native; examine Venus (male) or Mars (female) by sign, aspects, and dignity. |
| Conclusion operationalization | Predict marriage quality (harmonious/contentious), number (single/multiple), and timing (early/late). |
| Confidence rationale | High: explicit conditional logic with gender-specific rules. |

### L3.3 Factor Extraction

| Factor Label | Factor ID | Semantic Essence | Extraction Justification |
|:---|:---|:---|:---|
| Venus as spouse (male) | venus_spouse_male | Venus signifies wife for men | Chapter V explicitly states. |
| Mars as spouse (female) | mars_spouse_female | Mars signifies husband for women | Chapter V explicitly states. |
| Spouse count | spouse_count | Bicorporeal = multiple marriages | Chapter V explicitly states. |

**Factor Status**: existing (spouse_count in tetrabiblos_factors.yaml)

---

## L4 - Cross-System Bridge Layer

### L4.1 Functional Equivalence Analysis

**Core Function**: Assess relationship/marriage outcomes from chart indicators.

| Target System | Corresponding Concept | Functional Equivalence Argument | Academic Basis |
|:---|:---|:---|:---|
| BaZi | 财星论妻（男）、官杀论夫（女） | Both systems use gendered significators for spouse assessment. | Structural analogy: spouse significator by gender. |

### L4.3 Neutral Semantic Tag Mapping

| neutral_tag | Mapping Rationale | Applicability Limits |
|:---|:---|:---|
| neutral_relationship_harmony | Venus/Mars well-placed with benefics = harmonious union | Only when configurations are favorable. |
| neutral_relationship_conflict | Venus/Mars afflicted = strife or separation | Baseline tendency; can be mitigated. |

---

## L5 - Validation and Calibration Layer

### L5.1 Text-Internal Validation

| Case Description | Conditions Met | Rule-Based Prediction | Actual Outcome | Validation Status |
|:---|:---|:---|:---|:---|
| Chapter V example: Venus in Gemini (bicorporeal) with Saturn aspect. | Bicorporeal + malefic aspect. | Multiple marriages, unfortunate. | Ptolemy's text confirms: "more than one marriage" and "not fortunate." | Validated |

---

## L6 - Meta-Reflection Layer

### L6.2 Uncertainty Annotation

| Layer | Uncertainty | Notes |
|:---|:---|:---|
| L1 Understanding | Low | Explicit gender-specific rules. |
| L3 Extraction | Low | Rules directly stated. |
| L4 Mapping | Medium | BaZi spouse stars have different derivation but same function. |
| L5 Validation | Low | Internal examples confirm rules. |

---

## Appendix

### A2 - Revision History

| Date | Reviser | Revision Content |
|:---|:---|:---|
| 2026-01-28 | LS-CAL-R20-TETR | Initial creation: Book IV marriage (core domain from marriage/children/illness set) |
