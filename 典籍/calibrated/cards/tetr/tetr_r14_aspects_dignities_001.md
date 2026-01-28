# Deep Calibration Card

## S - Synopsis

- `card_id`: `tetr_r14_aspects_dignities_001`
- `semantic_unit`: `Ptolemy defines planetary dignities (houses, triplicities, exaltations, terms) as modes of planetary-sign familiarity that strengthen or modify planetary influence.`
- `source_range`: `典籍/texts/Tetrabiblos/原文/Tetrabiblos.md:2368` ~ `:2805`
- `depth_level`: `Deep`
- `confidence`: `High`
- `last_updated`: `2026-01-28`

### Core Thesis in One Sentence
> Planets have "familiarity" with certain signs through domicile (house), triplicity, exaltation, and terms; these dignities amplify or specify planetary influence in ways grounded in astronomical/elemental logic.

---

## L1 - Deep Comprehension Layer

### L1.1 Source Text and Context

**Source Text** (Chapters XX-XXIV condensed):
> Those stars which are denominated planetary orbs have particular familiarity with certain places in the zodiac, by means of parts designated as their houses, and also by their triplicities, exaltations, terms, and so forth.  
>   
> **Houses (XX)**: Cancer and Leo are the most northerly of all the twelve signs... they are consequently appropriated as houses for the two principal and greater luminaries; Leo for the Sun, as being masculine; and Cancer for the Moon, as being feminine... Saturn, since he is cold and inimical to heat... occupies the signs opposite to Cancer and Leo: these are Aquarius and Capricorn...  
>   
> **Triplicities (XXI)**: The triplicity preserves accordance with an equilateral triangle... The first triangle, or triplicity, is formed by three masculine signs, Aries, Leo, and Sagittarius, having the Sun, Jupiter, and Mars as lords by house...  
>   
> **Exaltations (XXII)**: The Sun on his entrance into Aries is then passing into the higher and more northern semicircle... his exaltation, therefore, is determined to be in Aries... Saturn on the contrary... obtains his exaltation in Libra...  
>   
> **Terms (XXIII-XXIV)**: There are two methods of disposing the terms of the planets... The Ægyptian method preserves no regular distribution... [Ptolemy then presents his own terms based on aspect-based logic]

**Context Analysis**:

| Dimension | Analysis |
|:---|:---|
| Preceding context | Sign modalities and aspect geometry have been established; now planetary "ownership" of sign segments is defined. |
| Following direction | Chapter XXVII discusses application/separation and planetary strength by position, completing the toolkit. |
| Overall positioning | Book I, Chapters XX-XXIV: the essential dignity system for evaluating planetary "strength" and "affinity." |

### L1.2 Historical Background and Academic Lineage (Brief)

| Dimension | Content |
|:---|:---|
| Writing context | Ptolemy inherits Hellenistic dignity systems but provides naturalistic rationale (distance from Sun, seasonal logic). |
| Academic lineage | Domicile assignments are ancient (Babylonian/Hellenistic); Ptolemy's terms differ from "Egyptian" terms and are based on aspect logic. |
| Later developments | Medieval/Renaissance astrology used both Egyptian and Ptolemaic terms; modern traditional astrology debates which to prefer. |

---

## L3 - Semantic Essence Layer

### L3.1 Core Concept Deconstruction

| Concept | Literal Meaning | Deep Semantics | Modern Reconstruction |
|:---|:---|:---|:---|
| `domicile/house` | planetary home | The sign where a planet has maximum affinity and operates "at home" | `dignity_domicile`: planet at full natural expression |
| `triplicity` | triangular grouping | Elemental affinity (fire/earth/air/water) with day/night rulers | `dignity_triplicity`: elemental support |
| `exaltation` | elevated position | The sign where a planet is "honored" and powerfully expressed | `dignity_exaltation`: planet at peak influence |
| `terms/bounds` | degree segments | Subdivisions of signs ruled by different planets for fine-grained analysis | `dignity_terms`: micro-level planetary influence |
| `essential dignity` (composite) | inherent strength | Aggregate of domicile/exaltation/triplicity/terms → planetary power | `essential_dignity_score`: strength metric |

### L3.2 Abstract Rule Extraction

**Rule ID**: `rule_tetr_essential_dignities`

**Rule Structure** (pseudo-code form):

```
IF planet is_in its_domicile_sign
THEN dignity += domicile_strength
BECAUSE <Tetrabiblos I.20, lines 2373-2432>

IF planet is_in its_exaltation_sign
THEN dignity += exaltation_strength
BECAUSE <Tetrabiblos I.22, lines 2509-2553>

IF planet is_in its_triplicity (and sect matches)
THEN dignity += triplicity_strength
BECAUSE <Tetrabiblos I.21, lines 2435-2504>

IF planet is_in its_terms (degree range)
THEN dignity += term_strength
BECAUSE <Tetrabiblos I.23-24, lines 2556-2803>
```

**Rule Operationalization**:

| Dimension | Explanation |
|:---|:---|
| Trigger operationalization | For any planet, check sign placement against domicile/exaltation/triplicity/terms tables. |
| Conclusion operationalization | Higher dignity → planet's significations manifest more fully and favorably; lower dignity → weakened or distorted expression. |
| Confidence rationale | High: systematic enumeration with explicit tables and rationale. |

### L3.3 Factor Extraction (Semantic Level)

| Factor Label | Factor ID | Semantic Essence | Extraction Justification |
|:---|:---|:---|:---|
| Domicile dignity | `planet_domicile` | Planet in own sign | Chapter XX lists all domiciles. |
| Exaltation dignity | `planet_exaltation` | Planet in exaltation sign | Chapter XXII enumerates. |
| Triplicity dignity | `sign_triplicity` | Planet ruling the triplicity of its sign | Chapter XXI defines. |
| Terms dignity | `planet_dignity_terms` | Planet in its own term degrees | Chapters XXIII-XXIV provide tables. |

**Factor Status**: `existing` (planet_domicile, planet_exaltation, sign_triplicity already in tetrabiblos_factors.yaml)

---

## L4 - Cross-System Bridge Layer

### L4.1 Functional Equivalence Analysis

**Core Function**: Quantify planetary strength/affinity to assess how fully a planet can express its significations.

| Target System | Corresponding Concept | Functional Equivalence Argument | Academic Basis |
|:---|:---|:---|:---|
| BaZi (bazi) | 旺相休囚死（五行旺衰） | Both systems assess whether a factor is "strong" or "weak" in its current position, affecting interpretation magnitude. | Functional analogy: positional strength → interpretive weight. |

### L4.3 Neutral Semantic Tag Mapping

| neutral_tag | Mapping Rationale | Applicability Limits |
|:---|:---|:---|
| `neutral_vitality_high` | Planet in dignity → stronger, more vital expression | Only for inherently benefic planets or well-aspected malefics. |
| `neutral_vitality_low` | Planet in detriment/fall → weakened expression | Baseline tendency; can be mitigated by other factors. |

---

## L5 - Validation and Calibration Layer

### L5.1 Text-Internal Validation

**Case Source**: Tetrabiblos Book III-IV use dignities in delineation

| Case Description | Conditions Met | Rule-Based Prediction | Actual Outcome | Validation Status |
|:---|:---|:---|:---|:---|
| Book III.11 on duration of life uses planet "cosmically powerful when in one of its own places." | Dignity system applied to life-length significators. | Planets in dignity should correlate with longer/better outcomes. | Book III explicitly requires dignity for prorogator strength, matching the dignity definitions. | `Validated` |

---

## L6 - Meta-Reflection Layer

### L6.2 Uncertainty Annotation (Simplified)

| Layer | Uncertainty | Notes |
|:---|:---|:---|
| L1 Understanding | `Low` | Explicit tables and rationale provided. |
| L3 Extraction | `Low/Medium` | Terms have variant traditions (Egyptian vs Ptolemaic); Ptolemy's own terms are well-defined but not universally used. |
| L4 Mapping | `Medium` | 旺衰 analogy is functional, not exact. |
| L5 Validation | `Low` | Internal consistency with later books is strong. |

---

## Appendix

### A2 - Revision History

| Date | Reviser | Revision Content |
|:---|:---|:---|
| 2026-01-28 | LS-CAL-R14-TETR | Initial creation: Deep calibration for Book I aspects/dignities/terms |
