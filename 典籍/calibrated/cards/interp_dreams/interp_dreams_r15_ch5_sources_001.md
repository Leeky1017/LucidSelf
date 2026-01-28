# Deep Calibration Card

## S - Synopsis

- `card_id`: `interp_dreams_ch5_sources_001`
- `semantic_unit`: `Freud lists three recurrent selection biases in dream memory (recent preference, trivial details, childhood traces) and claims every dream links to the previous day`
- `source_range`: `典籍/texts/The Interpretation of Dreams/原文/The Interpretation of Dreams.md:5568` ~ `:5602`
- `depth_level`: `Deep`
- `confidence`: `Medium`
- `last_updated`: `2026-01-28`

### Core Thesis in One Sentence
> Dream material selection is biased toward recent residues, seemingly trivial details, and early childhood impressions, and every dream contains some link to the immediately preceding day.

---

## L1 - Deep Comprehension Layer

### L1.1 Source Text and Context

**Source Text**:
> … there are three peculiarities  
> of recollection in the dreams, which have been often  
> remarked but never explained:  
> ### 1. That the dream distinctly prefers impressions of the  
> few days preceding; …  
> ### 2. That it makes its selection according to principles other  
> than those of our waking memory, in that it recalls not what  
> is essential and important, but what is subordinate and disregarded …  
> ### 3. That it has at its disposal the earliest impressions of  
> our childhood, and brings to light details from this period of  
> life which again seem trivial to us, and which in waking life  
> were considered long ago forgotten.  
>
> … some reference to the experiences of  
> the day which has most recently passed is to be found in every  
> dream. …

**Context Analysis**:

| Dimension | Analysis |
|:---|:---|
| Preceding context | Chapter V restarts “dream problems” by focusing on sources of dream material. |
| Following direction | Immediately proceeds to examples (“dream chronicle”) to support the day-residue claim. |
| Overall positioning | Provides a compact checklist for what to look for when tracing dream material. |

---

## L3 - Semantic Essence Layer

### L3.2 Abstract Rule Extraction

**Rule ID**: `rule_interp_dreams_material_source_checklist`

**Rule Structure** (pseudo-code form):

```
IF <interpreting a dream’s material sources>
THEN <check: previous-day residues, low-salience details, childhood traces>
WITH confidence = Medium
BECAUSE <Freud explicitly lists these as recurring “peculiarities” and asserts a day-link>
UNLESS <the dream report is too sparse to justify any linkage>
```

### L3.3 Factor Extraction (Semantic Level)

| Factor Label | Factor ID | Semantic Essence | Extraction Justification |
|:---|:---|:---|:---|
| Recent-day linkage | `day_residue_linkage` | Dreams link to the day most recently passed | “reference… is to be found in every dream” |
| Trivial-detail bias | `trivial_detail_bias` | Dreams recall subordinate/disregarded details | “subordinate and disregarded” |
| Childhood resurfacing | `childhood_resurfacing` | Earliest impressions can appear | “earliest impressions… childhood” |

**Factor Status**: `new_candidate`

---

## L6 - Meta-Reflection Layer

### L6.2 Uncertainty Annotation

| Layer | Uncertainty | Explanation |
|:---|:---|:---|
| L3 Extraction | `Medium` | “Trivial vs essential” is observer-dependent and requires explicit criteria. |

---

## Appendix

### A2 - Revision History

| Date | Reviser | Revision Content |
|:---|:---|:---|
| 2026-01-28 | LS-CAL-R15-INTERP_DREAMS | Initial creation (Deep): sources of dream material checklist (recent/trivial/childhood) |
# Deep Calibration Card

## S - Synopsis

- `card_id`: `interp_dreams_ch5_sources_001`
- `semantic_unit`: `Freud summarizes three “selection oddities” of dream memory (recent preference, trivial details, childhood traces) and asserts every dream contains a reference to the immediately preceding day`
- `source_range`: `典籍/texts/The Interpretation of Dreams/原文/The Interpretation of Dreams.md:5568` ~ `:5602`
- `depth_level`: `Deep`
- `confidence`: `Medium`
- `last_updated`: `2026-01-28`

### Core Thesis in One Sentence
> Dream material selection is biased toward recent residues, seemingly trivial details, and early childhood impressions, and (in Freud’s view) every dream includes some link to the immediately preceding day.

---

## L1 - Deep Comprehension Layer

### L1.1 Source Text and Context

**Source Text**:
> The statements of the authors concerning the relation of  
> the dream to waking life, as well as concerning the source of  
> the dream material, have been given at length in the introductory  
> chapter. We may recall that there are three peculiarities  
> of recollection in the dreams, which have been often  
> remarked but never explained:  
> ### 1. That the dream distinctly prefers impressions of the  
> few days preceding; …  
> ### 2. That it makes its selection according to principles other  
> than those of our waking memory, in that it recalls not what  
> is essential and important, but what is subordinate and disregarded …  
> ### 3. That it has at its disposal the earliest impressions of  
> our childhood, and brings to light details from this period of  
> life which again seem trivial to us, and which in waking life  
> were considered long ago forgotten.  
>
> … If I now consult my own experience concerning the source  
> of the elements which appear in the dream, I must at once  
> express the opinion that some reference to the experiences of  
> the day which has most recently passed is to be found in every  
> dream. … In the case of … Irma’s  
> injection … the reference  
> to the previous day is so obvious that it needs no further  
> elucidation.

**Context Analysis**:

| Dimension | Analysis |
|:---|:---|
| Preceding context | After defending wish-fulfilment and distortion, Freud returns to the “materials” question: what sources feed dreams. |
| Following direction | Leads into a “dream chronicle” of examples to support the day-residue claim. |
| Overall positioning | Re-frames prior literature “oddities” as explainable once selection mechanisms are analyzed. |

---

## L3 - Semantic Essence Layer

### L3.1 Core Concept Deconstruction

| Concept | Literal Meaning | Deep Semantics | Modern Reconstruction |
|:---|:---|:---|:---|
| `recent preference` | recent-day bias | Recent experiences provide triggers/material | `day_residue_bias` |
| `trivial detail recall` | minor items recalled | Low-salience carriers link latent thoughts | `low_salience_carrier` |
| `childhood trace access` | early memories appear | Remote traces can re-emerge as dream material | `early_memory_reactivation` |

### L3.2 Abstract Rule Extraction

**Rule ID**: `rule_interp_dreams_day_residue_first`

**Rule Structure** (pseudo-code form):

```
IF <a dream is being interpreted>
THEN <start by identifying links to the immediately preceding day>
AND <treat trivial fragments as potentially meaningful carriers>
WITH confidence = Medium
BECAUSE <Freud asserts recent-day reference in every dream>
UNLESS <report/recall is too sparse to support linkage>
```

### L3.3 Factor Extraction (Semantic Level)

| Factor Label | Factor ID | Semantic Essence | Extraction Justification |
|:---|:---|:---|:---|
| Recent-day linkage | `day_residue_linkage` | Dreams link to the day most recently passed | “reference… is to be found in every dream” |
| Trivial-detail bias | `trivial_detail_bias` | Dreams recall subordinate/disregarded details | “subordinate and disregarded” |
| Childhood resurfacing | `childhood_resurfacing` | Earliest impressions can appear | “earliest impressions… childhood” |

**Factor Status**: `new_candidate`

---

## L4 - Cross-System Bridge Layer

### L4.3 Neutral Semantic Tag Mapping

| neutral_tag | Mapping Rationale | Applicability Limits |
|:---|:---|:---|
| `Day_Residue` | Names the recent-day linkage claim | Depends on recall and diary evidence |
| `Trivial_Carrier` | Names the low-salience carrier idea | “Trivial” is observer-dependent |
| `Childhood_Trace` | Names early-memory access | Mechanism unspecified here |

---

## L6 - Meta-Reflection Layer

### L6.2 Uncertainty Annotation

| Layer | Uncertainty | Explanation |
|:---|:---|:---|
| L1 Comprehension | `Low` | Claims are explicit. |
| L3 Extraction | `Medium` | Operational definitions (trivial/important) vary. |

---

## Appendix

### A2 - Revision History

| Date | Reviser | Revision Content |
|:---|:---|:---|
| 2026-01-28 | LS-CAL-R15-INTERP_DREAMS | Initial creation (Deep): sources of dream material (recent bias + trivial details + childhood traces) |
