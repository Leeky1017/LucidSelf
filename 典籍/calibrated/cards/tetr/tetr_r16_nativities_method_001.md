# Deep Calibration Card

## S - Synopsis

- `card_id`: `tetr_r16_nativities_method_001`
- `semantic_unit`: `Ptolemy outlines the method for natal astrology: systematically proceeding through heads of inquiry (parents, siblings, sex, rearing, lifespan, body, mind, fortune, marriage, children, travel, death).`
- `source_range`: `典籍/texts/Tetrabiblos/原文/Tetrabiblos.md:4867` ~ `:4965`
- `depth_level`: `Deep`
- `confidence`: `High`
- `last_updated`: `2026-01-28`

### Core Thesis in One Sentence
> Natal astrology proceeds systematically through ordered heads of inquiry, each with appropriate significators, requiring the astrologer to identify dominant planets and assess their strength and timing.

---

## L1 - Deep Comprehension Layer

### L1.1 Source Text and Context

**Source Text** (Book III Chapter IV condensed):
> The doctrine of genethliacal prognostication should be separately and distinctly considered in its first, second and successive divisions or heads of inquiry...
>
> One division is applicable to circumstances established previously to the birth (parents); another to circumstances both before and after birth (siblings); another to circumstances at the very time of birth (sex, twins, monstrous births, rearing); and the last division relates to events after birth (duration of life, body, mind, fortune, employment, marriage, children, friends, travel, death)...
>
> Firstly, notice must be taken of that place in the zodiac which corresponds with the particular division of inquiry (e.g., mid-heaven for employment, Sun for father). Secondly, the planets holding right of dominion there are to be observed. Thirdly, the natures of the ruling planet and of the signs are to be considered. Fourthly, the proportionate vigour and strength. Lastly, the general time is to be inferred from the ruling planet's matutine or vespertine position.

**Context Analysis**:

| Dimension | Analysis |
|:---|:---|
| Preceding context | Book III Chapters I-III covered conception, birth timing, and degree ascending. |
| Following direction | Chapters V-XIX systematically address each head of inquiry (parents, siblings, sex, etc.). |
| Overall positioning | Book III, Chapter IV: the methodological blueprint for all natal delineation. |

### L1.2 Historical Background (Brief)

| Dimension | Content |
|:---|:---|
| Writing context | Ptolemy systematizes Hellenistic nativity doctrine into a structured workflow. |
| Academic lineage | Hellenistic astrology had developed significator systems; Ptolemy formalizes the procedural order. |
| Later developments | Medieval and Renaissance astrology followed this ordered-inquiry approach; modern psychological astrology often proceeds more holistically. |

---

## L3 - Semantic Essence Layer

### L3.1 Core Concept Deconstruction

| Concept | Literal Meaning | Deep Semantics | Modern Reconstruction |
|:---|:---|:---|:---|
| heads of inquiry | topics of analysis | Ordered domains of life that natal astrology systematically addresses | life_domain_checklist |
| significator | indicator | The planet or point that primarily signifies a given life domain | domain_significator |
| dominion | rulership | The planet(s) with authority over a zodiacal place via dignity | ruling_planet |
| vigour/strength | planetary power | Cosmical and schematic strength determining magnitude of effect | planetary_strength |
| timing from position | temporal inference | Matutine/vespertine and angular/succedent position indicating early/late manifestation | timing_indicator |

### L3.2 Abstract Rule Extraction

**Rule ID**: `rule_tetr_nativity_method_workflow`

```
FOR each head_of_inquiry IN {parents, siblings, sex, rearing, lifespan, body, mind, fortune, employment, marriage, children, friends, travel, death}:
  1. Identify zodiacal_place corresponding to this inquiry
  2. Find planet(s) with dominion over this place
  3. Assess ruling_planet nature and sign
  4. Evaluate vigour (cosmical and schematic strength)
  5. Infer timing from matutine/vespertine and angular position
BECAUSE <Tetrabiblos III.4, lines 4919-4965>
```

**Rule Operationalization**:

| Dimension | Explanation |
|:---|:---|
| Trigger operationalization | When analyzing a nativity, iterate through each life domain in order. |
| Conclusion operationalization | For each domain, identify significator, assess strength, and determine quality/timing of outcomes. |
| Confidence rationale | High: explicit procedural instruction with clear steps. |

### L3.3 Factor Extraction

| Factor Label | Factor ID | Semantic Essence | Extraction Justification |
|:---|:---|:---|:---|
| Life domain inquiry | life_domain_inquiry | Ordered list of natal topics | Chapter IV enumerates. |
| Domain significator | domain_significator | Planet/place ruling each inquiry | Chapter IV assigns (e.g., Sun for father). |
| Planetary strength | planet_strength | Cosmical + schematic vigor | Chapter IV defines strength assessment. |

**Factor Status**: new_candidate (systematic inquiry framework)

---

## L4 - Cross-System Bridge Layer

### L4.1 Functional Equivalence Analysis

**Core Function**: Provide a systematic workflow for natal interpretation covering all major life domains.

| Target System | Corresponding Concept | Functional Equivalence Argument | Academic Basis |
|:---|:---|:---|:---|
| BaZi | 六亲/十神分论 | Both systems systematically address life domains (parents, siblings, spouse, children) via designated factors. | Structural analogy: ordered domain analysis. |

### L4.3 Neutral Semantic Tag Mapping

| neutral_tag | Mapping Rationale | Applicability Limits |
|:---|:---|:---|
| neutral_career_support | Employment inquiry uses MC and its ruler | Only when benefic ruler with strength. |
| neutral_relationship_harmony | Marriage inquiry uses Moon/Venus positions | Only when configurations are favorable. |

---

## L5 - Validation and Calibration Layer

### L5.1 Text-Internal Validation

| Case Description | Conditions Met | Rule-Based Prediction | Actual Outcome | Validation Status |
|:---|:---|:---|:---|:---|
| Book III.5 on parents follows the method exactly: Sun/Saturn for father, Moon/Venus for mother. | Workflow applied. | Significator identification should match Chapter IV blueprint. | Chapter V explicitly uses Sun/Saturn for father, confirming the method. | Validated |

---

## L6 - Meta-Reflection Layer

### L6.2 Uncertainty Annotation

| Layer | Uncertainty | Notes |
|:---|:---|:---|
| L1 Understanding | Low | Explicit procedural instruction. |
| L3 Extraction | Low | Steps are enumerated clearly. |
| L4 Mapping | Medium | BaZi domains overlap but are not identical. |
| L5 Validation | Low | Strong internal consistency. |

---

## Appendix

### A2 - Revision History

| Date | Reviser | Revision Content |
|:---|:---|:---|
| 2026-01-28 | LS-CAL-R16-TETR | Initial creation: Book III nativities method overview |
