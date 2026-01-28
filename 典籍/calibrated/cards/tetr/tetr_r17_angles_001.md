# Deep Calibration Card

## S - Synopsis

- `card_id`: `tetr_r17_angles_001`
- `semantic_unit`: `Ptolemy emphasizes the importance of the ascending degree and angles (ASC, MC, DSC, IC) as the primary reference points in chart interpretation.`
- `source_range`: `典籍/texts/Tetrabiblos/原文/Tetrabiblos.md:4779` ~ `:4863`
- `depth_level`: `Deep`
- `confidence`: `High`
- `last_updated`: `2026-01-28`

### Core Thesis in One Sentence
> The degree ascending (Ascendant) and the four angles are the foundation of natal interpretation; Ptolemy provides methods to rectify uncertain birth times using planetary rulers of the prenatal lunation.

---

## L1 - Deep Comprehension Layer

### L1.1 Source Text and Context

**Source Text** (Book III Chapter III condensed):
> There frequently arises some uncertainty as to the precise time of birth... To obviate the difficulty arising from the inaccuracy of these instruments, it seems highly necessary to present some method by which the actually ascending degree of the zodiac may be easily ascertained...
>
> In order to attain this essential point, it is necessary first to set down the ordinary degree which, by the Doctrine of Ascensions, is found near the ascendant at the presumed hour. After this has been done, the new or full Moon, whichever it may be, that may take place next before the time of parturition, must be observed... it must be observed what planets have dominion over the said degree: and their dominion depends always on the five following prerogatives, viz. on triplicity, house, exaltation, terms, and phase or configuration...

**Context Analysis**:

| Dimension | Analysis |
|:---|:---|
| Preceding context | Book III opens with conception/birth distinction and the importance of the actual birth moment. |
| Following direction | Chapter IV (method of nativities) builds on a correctly determined ascendant to proceed through life domains. |
| Overall positioning | Book III, Chapter III: the critical technical step of ascertaining the true Ascendant before any delineation. |

### L1.2 Historical Background (Brief)

| Dimension | Content |
|:---|:---|
| Writing context | Birth time accuracy was difficult in antiquity; Ptolemy's Animodar rectification method addresses this. |
| Academic lineage | The prenatal lunation (syzygy) as a rectification anchor is distinctly Ptolemaic. |
| Later developments | Later astrologers developed additional rectification methods; Ptolemy's remains foundational. |

---

## L3 - Semantic Essence Layer

### L3.1 Core Concept Deconstruction

| Concept | Literal Meaning | Deep Semantics | Modern Reconstruction |
|:---|:---|:---|:---|
| degree ascending | rising degree | The exact zodiacal degree on the eastern horizon at birth | Ascendant (ASC) |
| angles | four pivots | ASC, MC (mid-heaven), DSC, IC: the four cardinal points of the chart | angular_houses |
| Animodar | rectification method | Using prenatal lunation ruler to refine the Ascendant degree | rectification_method |
| doctrine of ascensions | oblique ascension tables | Mathematical tables for converting time to zodiacal degrees at a given latitude | ascension_calculation |
| dominion by prerogatives | essential dignities | Rulership via house, exaltation, triplicity, terms, and configuration | dignity_based_rulership |

### L3.2 Abstract Rule Extraction

**Rule ID**: `rule_tetr_animodar_rectification`

```
IF birth_time is_uncertain:
  1. Find prenatal_lunation (new or full Moon before birth)
  2. Identify degree of lunation
  3. Find planet(s) with dominion over that degree (by 5 prerogatives)
  4. The ruling_planet's degree = numerical denomination of true ASC
BECAUSE <Tetrabiblos III.3, lines 4799-4855>
```

**Rule Operationalization**:

| Dimension | Explanation |
|:---|:---|
| Trigger operationalization | When birth time is uncertain, apply Animodar as a rectification step before delineation. |
| Conclusion operationalization | The refined Ascendant degree then anchors all subsequent house and angle determinations. |
| Confidence rationale | Medium: the method is explicit but its accuracy depends on chart context and competing traditions. |

### L3.3 Factor Extraction

| Factor Label | Factor ID | Semantic Essence | Extraction Justification |
|:---|:---|:---|:---|
| Ascendant | Ascendant | Rising degree at birth | Chapter III's primary focus. |
| Prenatal lunation | prenatal_lunation | New/full Moon before birth | Rectification anchor per Animodar. |
| Angle strength | house_angular | Planets in angles are strongest | Implicit: angles are primary reference points. |

**Factor Status**: existing (Ascendant, house_angular in factors)

---

## L4 - Cross-System Bridge Layer

### L4.1 Functional Equivalence Analysis

**Core Function**: Establish accurate chart anchoring before interpretation.

| Target System | Corresponding Concept | Functional Equivalence Argument | Academic Basis |
|:---|:---|:---|:---|
| BaZi | 日主确定（以日柱为中心） | Both systems require a fixed reference point (ASC / 日主) as interpretation anchor. | Structural analogy: central reference point. |

### L4.3 Neutral Semantic Tag Mapping

| neutral_tag | Mapping Rationale | Applicability Limits |
|:---|:---|:---|
| neutral_transformation_opportunity | Angles mark major life pivots and transitions | Only in context of significant transits/directions to angles. |

---

## L5 - Validation and Calibration Layer

### L5.1 Text-Internal Validation

| Case Description | Conditions Met | Rule-Based Prediction | Actual Outcome | Validation Status |
|:---|:---|:---|:---|:---|
| Book III.15 provides a worked example of prorogation that relies on correct Ascendant. | Ascendant must be accurately determined. | Delineation should fail if Ascendant is wrong. | Ptolemy's example calculations presuppose correct Ascendant from Chapter III method. | Validated |

---

## L6 - Meta-Reflection Layer

### L6.2 Uncertainty Annotation

| Layer | Uncertainty | Notes |
|:---|:---|:---|
| L1 Understanding | Low | Procedure is explicit. |
| L3 Extraction | Medium | Animodar has competing versions in tradition. |
| L4 Mapping | Medium | BaZi does not use rectification the same way. |
| L5 Validation | Low | Internal consistency strong. |

---

## Appendix

### A2 - Revision History

| Date | Reviser | Revision Content |
|:---|:---|:---|
| 2026-01-28 | LS-CAL-R17-TETR | Initial creation: Book III angles/ascendant focus |
