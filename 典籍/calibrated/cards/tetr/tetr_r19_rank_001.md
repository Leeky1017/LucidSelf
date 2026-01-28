# Deep Calibration Card

## S - Synopsis

- `card_id`: `tetr_r19_rank_001`
- `semantic_unit`: `Ptolemy describes how to judge rank and honor using the luminaries (Sun/Moon) and their angular placement, sect, and rulership configurations.`
- `source_range`: `典籍/texts/Tetrabiblos/原文/Tetrabiblos.md:7105` ~ `:7176`
- `depth_level`: `Deep`
- `confidence`: `High`
- `last_updated`: `2026-01-28`

### Core Thesis in One Sentence
> Rank and honor are judged from the luminaries (Sun and Moon) and their rulers: angular placement with benefic configuration produces high station, while cadent or afflicted placement produces obscurity.

---

## L1 - Deep Comprehension Layer

### L1.1 Source Text and Context

**Source Text** (Book IV Chapter III condensed):
> The judgment of rank and honor is derived from the position of the lights and of those planets which are their attendants and their lords...
>
> When both luminaries are in masculine signs and angular (especially on the angles of the meridian), or if one of them is angular and the other in a succedent house, and attended by the body or ray of one of the five planets, and especially if that planet is in dignity—then honorable station is indicated...
>
> If both luminaries are found in feminine signs, and in cadent houses, without any attendance from the five planets, the person will be low and obscure...
>
> The Sun is more particularly connected with the condition of the father and husband; the Moon with the mother and wife. Saturn and Jupiter assist particularly the solar dignity; Venus and Mars the lunar...

**Context Analysis**:

| Dimension | Analysis |
|:---|:---|
| Preceding context | Chapter II addressed wealth; Chapter III addresses the distinct but related topic of social standing. |
| Following direction | Chapters IV-V continue with employment and marriage. |
| Overall positioning | Book IV, Chapter III: social status delineation methodology. |

### L1.2 Historical Background (Brief)

| Dimension | Content |
|:---|:---|
| Writing context | Roman-era social hierarchy informs Ptolemy's "honor/rank" framing. |
| Academic lineage | Luminaries as dignity indicators is ancient; Ptolemy systematizes their use. |
| Later developments | Medieval astrology elaborated rank indicators for nobility/clergy/commoner distinctions. |

---

## L3 - Semantic Essence Layer

### L3.1 Core Concept Deconstruction

| Concept | Literal Meaning | Deep Semantics | Modern Reconstruction |
|:---|:---|:---|:---|
| rank/honor | social standing | Reputation, public recognition, authority | social_status |
| luminaries | Sun and Moon | The two lights as primary significators of public visibility | lights_as_dignity |
| angular placement | on ASC/MC/DSC/IC | Prominence; planets here are most visible and effective | angular_prominence |
| attendance | aspect/configuration | Planetary support to the luminaries | planetary_support |
| sect dignity | day/night affinity | Sun stronger by day, Moon by night; matching sect enhances dignity | sect_alignment |

### L3.2 Abstract Rule Extraction

**Rule ID**: `rule_tetr_rank_luminaries`

```
IF (Sun AND Moon) are_in masculine_signs AND angular
  AND attended by benefic_planet in dignity
THEN rank = high, honor = prominent
BECAUSE <Tetrabiblos IV.3, lines 7115-7130>

IF (Sun AND Moon) are_in feminine_signs AND cadent
  AND no planetary_attendance
THEN rank = low, obscure
BECAUSE <Tetrabiblos IV.3, lines 7145-7152>
```

**Rule Operationalization**:

| Dimension | Explanation |
|:---|:---|
| Trigger operationalization | Evaluate Sun and Moon: sign gender, house position (angular/succedent/cadent), and aspects from other planets. |
| Conclusion operationalization | Predict social standing: high office vs obscurity, fame vs anonymity. |
| Confidence rationale | High: explicit conditions and outcomes stated. |

### L3.3 Factor Extraction

| Factor Label | Factor ID | Semantic Essence | Extraction Justification |
|:---|:---|:---|:---|
| Luminary dignity | luminary_angular | Sun/Moon on angles = prominence | Chapter III explicitly states. |
| Planetary attendance | planet_attendant | Benefic aspect to luminaries supports rank | Chapter III defines. |
| Sect alignment | sect_luminary | Day chart Sun / night chart Moon | Chapter III implies sect context. |

**Factor Status**: existing (house_angular, sect_luminary in factors)

---

## L4 - Cross-System Bridge Layer

### L4.1 Functional Equivalence Analysis

**Core Function**: Assess social standing and public reputation from chart indicators.

| Target System | Corresponding Concept | Functional Equivalence Argument | Academic Basis |
|:---|:---|:---|:---|
| BaZi | 官星（正官/七杀）论法 | Both systems use designated factors to assess authority and social position. | Functional analogy: status significator analysis. |

### L4.3 Neutral Semantic Tag Mapping

| neutral_tag | Mapping Rationale | Applicability Limits |
|:---|:---|:---|
| neutral_career_support | Angular luminaries with benefic support = career/status success | Only when conditions are fully met. |

---

## L5 - Validation and Calibration Layer

### L5.1 Text-Internal Validation

| Case Description | Conditions Met | Rule-Based Prediction | Actual Outcome | Validation Status |
|:---|:---|:---|:---|:---|
| Chapter III example with Sun angular and Jupiter attending. | Angular luminary, benefic attendance. | Should indicate high rank. | Ptolemy's text confirms this produces eminence. | Validated |

---

## L6 - Meta-Reflection Layer

### L6.2 Uncertainty Annotation

| Layer | Uncertainty | Notes |
|:---|:---|:---|
| L1 Understanding | Low | Explicit conditions and outcomes. |
| L3 Extraction | Low | Rules directly stated. |
| L4 Mapping | Medium | BaZi official stars differ in derivation. |
| L5 Validation | Low | Internal examples confirm rules. |

---

## Appendix

### A2 - Revision History

| Date | Reviser | Revision Content |
|:---|:---|:---|
| 2026-01-28 | LS-CAL-R19-TETR | Initial creation: Book IV rank/honour |
