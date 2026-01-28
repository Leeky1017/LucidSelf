# Deep Calibration Card

## S - Synopsis

- `card_id`: `tetr_r12_planets_001`
- `semantic_unit`: `Ptolemy defines each planet's primary qualities (heat/cold/dry/moist) and classifies them as benefic, malefic, or common based on whether their qualities promote or hinder natural growth.`
- `source_range`: `典籍/texts/Tetrabiblos/原文/Tetrabiblos.md:1585` ~ `:1662`
- `depth_level`: `Deep`
- `confidence`: `High`
- `last_updated`: `2026-01-28`

### Core Thesis in One Sentence
> Each planet has inherent qualities (heat/cold/dry/moist) derived from its cosmic position, and planets producing nutritive qualities (heat+moisture) are benefic while those producing destructive qualities (cold+dryness) are malefic.

---

## L1 - Deep Comprehension Layer

### L1.1 Source Text and Context

**Source Text** (Chapters IV-V condensed):
> The Sun is found to produce heat and moderate dryness...  
> The Moon principally generates moisture...  
> Saturn produces cold and dryness... Mars chiefly causes dryness, and is also strongly heating...  
> Jupiter revolves in an intermediate sphere... and has consequently a temperate influence: he therefore at once promotes both warmth and moisture...  
> To Venus also the same temperate quality belongs...  
> Mercury sometimes produces dryness, and at other times moisture...  
>   
> Of the four temperaments or qualities above mentioned, two are nutritive and prolific, viz. heat and moisture; by these all matter coalesces and is nourished: the other two are noxious and destructive, viz. dryness and cold; by these all matter is decayed and dissipated.  
>   
> Therefore, two of the planets, on account of their temperate quality, and because heat and moisture are predominant in them, are considered by the ancients as benefic, or causers of good: these are Jupiter and Venus. And the Moon also is so considered for the same reasons.  
>   
> But Saturn and Mars are esteemed of a contrary nature, and malefic, or causers of evil: the first from his excess of cold, the other from his excess of dryness.  
>   
> The Sun and Mercury are deemed of common influence, and productive either of good or evil in unison with whatever planets they may be connected with.

**Context Analysis**:

| Dimension | Analysis |
|:---|:---|
| Preceding context | The Proem and Chapters II-III have established the philosophical foundation for how celestial bodies influence terrestrial matter through qualities. |
| Following direction | Chapters VI-VII extend to gender classifications (masculine/feminine) and sect (diurnal/nocturnal), refining how planetary natures manifest contextually. |
| Overall positioning | Book I, Chapters IV-V: the core "quality table" for planets that underlies all subsequent delineation. |

### L1.2 Historical Background and Academic Lineage (Brief)

| Dimension | Content |
|:---|:---|
| Writing context | Ptolemy systematizes Hellenistic astrological tradition using Aristotelian four-qualities physics (hot/cold/dry/moist). |
| Academic lineage | Draws on Greco-Roman natural philosophy and earlier Hellenistic astrologers; the benefic/malefic distinction is ancient and widespread. |
| Later developments | The benefic/malefic classification remains central in traditional astrology; modern psychological astrology often reframes malefics as "challenging" rather than "evil." |

---

## L3 - Semantic Essence Layer

### L3.1 Core Concept Deconstruction

| Concept | Literal Meaning | Deep Semantics | Modern Reconstruction |
|:---|:---|:---|:---|
| `heat/cold/dry/moist` | elemental qualities | The four primary qualities that define planetary "nature" and mechanism of influence | `planetary_quality_vector`: a 4-dimensional quality profile per planet |
| `benefic` | causing good | Planets whose qualities (warmth + moisture) support growth and well-being | `benefic_polarity`: positive valence in outcome prediction |
| `malefic` | causing evil | Planets whose qualities (cold + dryness) tend toward decay and obstruction | `malefic_polarity`: negative valence in outcome prediction |
| `common` | variable influence | Sun and Mercury adapt their effect to context (what they are configured with) | `context_dependent_polarity`: valence determined by configuration |

### L3.2 Abstract Rule Extraction

**Rule ID**: `rule_tetr_planet_benefic_malefic`

**Rule Structure** (pseudo-code form):

```
IF planet IN {Jupiter, Venus, Moon}
THEN planet_nature = benefic
BECAUSE <heat+moisture dominant, Tetrabiblos I.5, lines 1646-1654>

IF planet IN {Saturn, Mars}
THEN planet_nature = malefic
BECAUSE <cold or dryness excess, Tetrabiblos I.5, lines 1656-1658>

IF planet IN {Sun, Mercury}
THEN planet_nature = context_dependent
BECAUSE <common influence, Tetrabiblos I.5, lines 1660-1662>
```

**Rule Operationalization**:

| Dimension | Explanation |
|:---|:---|
| Trigger operationalization | Planet identification in a chart; classify by inherent nature before applying contextual modifiers. |
| Conclusion operationalization | Use benefic/malefic polarity as a baseline for outcome valence; common planets require configuration analysis. |
| Confidence rationale | High: explicit enumeration in the source text with clear reasoning. |

### L3.3 Factor Extraction (Semantic Level)

| Factor Label | Factor ID | Semantic Essence | Extraction Justification |
|:---|:---|:---|:---|
| Planet quality profile | `tetr_planet_quality_profile` | Each planet's heat/cold/dry/moist signature | Chapters IV defines each planet's qualities. |
| Benefic/malefic classification | `tetr_planet_benefic_malefic` | Binary (or ternary with "common") classification of planetary valence | Chapter V explicitly classifies planets. |
| Context-dependent planets | `tetr_planet_common` | Sun and Mercury as valence-neutral until configured | Chapter V names them as "common." |

**Factor Status**: `existing` (benefic_ruler, malefic_ruler already in tetrabiblos_factors.yaml); `new_candidate` for quality profiles

---

## L4 - Cross-System Bridge Layer

### L4.1 Functional Equivalence Analysis

**Core Function**: Assign baseline valence (positive/negative/neutral) to planets as a foundation for outcome judgment.

| Target System | Corresponding Concept | Functional Equivalence Argument | Academic Basis |
|:---|:---|:---|:---|
| BaZi (bazi) | 十神吉凶分类（正印/食神=吉；七杀/伤官=凶等） | Both systems assign inherent valence to planetary/star factors that is then modulated by context (旺衰, configuration). | Functional analogy: baseline valence + contextual modification. |

### L4.3 Neutral Semantic Tag Mapping

| neutral_tag | Mapping Rationale | Applicability Limits |
|:---|:---|:---|
| `neutral_career_support` | Jupiter (benefic) is associated with prosperity and rank | Only when Jupiter is well-placed; malefic configurations may reverse. |
| `neutral_resource_conflict` | Saturn/Mars (malefic) associated with obstruction and loss | Baseline tendency; can be mitigated by sect, dignity, etc. |

---

## L5 - Validation and Calibration Layer

### L5.1 Text-Internal Validation

**Case Source**: Tetrabiblos Book IV on wealth/rank judgments

| Case Description | Conditions Met | Rule-Based Prediction | Actual Outcome | Validation Status |
|:---|:---|:---|:---|:---|
| Book IV.2-3 uses benefic/malefic classification to judge fortune of wealth and rank. | Jupiter/Venus ruling Part of Fortune = prosperity; Saturn/Mars = diminished fortune. | The benefic/malefic rule should consistently inform later delineation chapters. | Book IV explicitly relies on benefic ruler → wealth, malefic ruler → poverty, matching the classification. | `Validated` |

---

## L6 - Meta-Reflection Layer

### L6.2 Uncertainty Annotation (Simplified)

| Layer | Uncertainty | Notes |
|:---|:---|:---|
| L1 Understanding | `Low` | Direct enumeration of planets and qualities. |
| L3 Extraction | `Low` | Benefic/malefic is explicitly stated. |
| L4 Mapping | `Medium` | BaZi 十神 mapping is functional analogy, not identity. |
| L5 Validation | `Low` | Internal consistency with Book IV is strong. |

---

## Appendix

### A2 - Revision History

| Date | Reviser | Revision Content |
|:---|:---|:---|
| 2026-01-28 | LS-CAL-R12-TETR | Initial creation: Deep calibration for Book I planets (qualities/benefic-malefic) |
