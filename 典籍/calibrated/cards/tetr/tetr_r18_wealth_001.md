# Deep Calibration Card

## S - Synopsis

- `card_id`: `tetr_r18_wealth_001`
- `semantic_unit`: `Ptolemy describes how to judge material fortune (wealth) using the Lot of Fortune and its ruler, with benefic/malefic configurations determining prosperity or poverty.`
- `source_range`: `典籍/texts/Tetrabiblos/原文/Tetrabiblos.md:7049` ~ `:7102`
- `depth_level`: `Deep`
- `confidence`: `High`
- `last_updated`: `2026-01-28`

### Core Thesis in One Sentence
> Wealth is judged from the Lot of Fortune and its ruler: benefics well-placed produce prosperity, malefics produce poverty or loss, and mixed configurations produce variable fortunes.

---

## L1 - Deep Comprehension Layer

### L1.1 Source Text and Context

**Source Text** (Book IV Chapter II condensed):
> The inquiry into the means and quality of the provision of wealth depends on the Lot of Fortune... The nature of the means of acquiring wealth is to be inferred from the particular mode in which the lords of the Lot of Fortune may be disposed...
>
> If these lords are found well situated, the acquisition of wealth will arise from good and praiseworthy sources; but should the lords be inappropriately disposed, the acquisition will be made by evil and unworthy means...
>
> If Jupiter and Venus hold dominion over this Lot, and if they are well placed, wealth and glory will be abundant... If Saturn and Mars rule the Lot and are ill-placed, poverty and disgrace result... When the lights and other benefics are configurated with the Lot or its lord, the fortune is increased; when malefics are so configurated, it is diminished.

**Context Analysis**:

| Dimension | Analysis |
|:---|:---|
| Preceding context | Book IV Chapter I introduced the topic of material fortune. |
| Following direction | Chapter III addresses rank and honor (related to but distinct from wealth). |
| Overall positioning | Book IV, Chapter II: the practical delineation of financial outcomes. |

### L1.2 Historical Background (Brief)

| Dimension | Content |
|:---|:---|
| Writing context | The Lot of Fortune is a Hellenistic construct; Ptolemy applies it for material matters. |
| Academic lineage | Arabian Parts (Lots) were extensively developed; Ptolemy's treatment is foundational. |
| Later developments | Medieval and modern traditional astrology continue to use the Lot of Fortune for wealth judgments. |

---

## L3 - Semantic Essence Layer

### L3.1 Core Concept Deconstruction

| Concept | Literal Meaning | Deep Semantics | Modern Reconstruction |
|:---|:---|:---|:---|
| Lot of Fortune | calculated point | Derived from ASC + Moon - Sun (or reverse by sect); represents material circumstances | part_of_fortune |
| lord of Lot | ruling planet | Planet with dignity over the Lot's sign; determines quality of wealth acquisition | lot_ruler |
| benefic ruler | Jupiter/Venus/Moon | Wealth through good means, abundance | benefic_wealth_indicator |
| malefic ruler | Saturn/Mars | Poverty, loss, or wealth through disreputable means | malefic_poverty_indicator |

### L3.2 Abstract Rule Extraction

**Rule ID**: `rule_tetr_wealth_lot_fortune`

```
IF Lot_of_Fortune ruler IN {Jupiter, Venus} AND well_placed
THEN wealth = abundant, acquisition = praiseworthy
BECAUSE <Tetrabiblos IV.2, lines 7069-7076>

IF Lot_of_Fortune ruler IN {Saturn, Mars} AND ill_placed
THEN wealth = poor, acquisition = disreputable_or_difficult
BECAUSE <Tetrabiblos IV.2, lines 7078-7085>

IF benefics configurated with Lot
THEN fortune += increase
IF malefics configurated with Lot
THEN fortune -= decrease
BECAUSE <Tetrabiblos IV.2, lines 7088-7095>
```

**Rule Operationalization**:

| Dimension | Explanation |
|:---|:---|
| Trigger operationalization | Calculate Lot of Fortune; identify its sign ruler and assess placement/aspects. |
| Conclusion operationalization | Predict financial outcomes: abundance vs scarcity, honorable vs questionable sources. |
| Confidence rationale | High: explicit conditional logic in the source text. |

### L3.3 Factor Extraction

| Factor Label | Factor ID | Semantic Essence | Extraction Justification |
|:---|:---|:---|:---|
| Lot of Fortune | lot_of_fortune | Material fortune indicator | Chapter II's primary significator. |
| Benefic wealth ruler | benefic_ruler | Jupiter/Venus ruling Lot = prosperity | Chapter II explicitly states. |
| Malefic poverty ruler | malefic_ruler | Saturn/Mars ruling Lot = poverty | Chapter II explicitly states. |

**Factor Status**: existing (benefic_ruler, malefic_ruler in tetrabiblos_factors.yaml)

---

## L4 - Cross-System Bridge Layer

### L4.1 Functional Equivalence Analysis

**Core Function**: Assess material/financial outcomes from chart indicators.

| Target System | Corresponding Concept | Functional Equivalence Argument | Academic Basis |
|:---|:---|:---|:---|
| BaZi | 财星（正财/偏财）论法 | Both systems have dedicated factors for wealth judgment. | Functional analogy: wealth significator analysis. |

### L4.3 Neutral Semantic Tag Mapping

| neutral_tag | Mapping Rationale | Applicability Limits |
|:---|:---|:---|
| neutral_resource_abundance | Benefic ruler of Lot = abundant resources | Only when well-placed and unafflicted. |
| neutral_resource_conflict | Malefic ruler or afflicted Lot = resource scarcity | Baseline tendency; timing matters. |

---

## L5 - Validation and Calibration Layer

### L5.1 Text-Internal Validation

| Case Description | Conditions Met | Rule-Based Prediction | Actual Outcome | Validation Status |
|:---|:---|:---|:---|:---|
| Book IV.2 examples showing Jupiter ruling Lot producing wealth. | Benefic ruler, well-placed. | Should produce abundant fortune. | Ptolemy's text explicitly confirms this outcome. | Validated |

---

## L6 - Meta-Reflection Layer

### L6.2 Uncertainty Annotation

| Layer | Uncertainty | Notes |
|:---|:---|:---|
| L1 Understanding | Low | Explicit significator and conditional logic. |
| L3 Extraction | Low | Rules directly stated. |
| L4 Mapping | Medium | BaZi wealth stars differ in derivation. |
| L5 Validation | Low | Internal examples confirm rules. |

---

## Appendix

### A2 - Revision History

| Date | Reviser | Revision Content |
|:---|:---|:---|
| 2026-01-28 | LS-CAL-R18-TETR | Initial creation: Book IV wealth |
