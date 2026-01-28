# Deep Calibration Card

## S - Synopsis

- `card_id`: `tetr_r11_book1_scope_001`
- `semantic_unit`: `Ptolemy defines astrology as the second part of astronomical prognostication and limits it to reasoned tendencies (not infallible rules).`
- `source_range`: `典籍/texts/Tetrabiblos/原文/Tetrabiblos.md:971` ~ `:1006`
- `depth_level`: `Deep`
- `confidence`: `High`
- `last_updated`: `2026-01-28`

### Core Thesis in One Sentence
> Astrology (as Ptolemy practices it) is the interpretation of natural effects produced by celestial configurations, and its outputs must be bounded as general, fallible tendencies because sublunary matter is variable.

---

## L1 - Deep Comprehension Layer

### L1.1 Source Text and Context

**Source Text**:
> The studies preliminary to astronomical prognostication, O Syrus! are  
> two: the one, first alike in order and in power, leads to the knowledge  
> of the figurations of the Sun, the Moon, and the stars; and of their  
> relative aspects to each other, and to the earth: the other takes into  
> consideration the changes which their aspects create, by means of their  
> natural properties, in objects under their influence.  
>   
> The first mentioned study has been already explained in the  
> Syntaxis[19] to the utmost practicable extent; for it is complete  
> in itself, and of essential utility even without being blended with  
> the second; to which this treatise will be devoted, and which is not  
> equally self-complete. The present work shall, however, be regulated  
> by that due regard for truth which philosophy demands: and since the  
> material quality of the objects acted upon renders them weak and  
> variable, and difficult to be accurately apprehended, no positive or  
> infallible rules (as were given in detailing the first doctrine, which  
> is always governed by the same immutable laws) can be here set forth:  
> while, on the other hand, a due observation of most of those general  
> events, which evidently trace their causes to the Ambient, shall not be  
> omitted.  
>   
> [19] The Almagest, or _Magna Constructio_.  
>   
> It is, however, a common practice with the vulgar to slander everything  
> which is difficult of attainment, and surely they who condemn the  
> first of these two studies must be considered totally blind, whatever  
> arguments may be produced in support of those who impugn the second.  
> There are also persons who imagine that whatever they themselves have  
> not been able to acquire, must be utterly beyond the reach of all  
> understanding; while others again will consider as useless any science  
> of which (although they may have been often instructed in it) they  
> have failed to preserve the recollection, owing to its difficulty of  
> retention. In reference to these opinions, therefore, an endeavour  
> shall be made to investigate the extent to which prognostication  
> by astronomy is practicable, as well as serviceable, previously to  
> detailing the particulars of the doctrine.

**Context Analysis**:

| Dimension | Analysis |
|:---|:---|
| Preceding context | The text has just introduced *Tetrabiblos* as the companion to the *Syntaxis* (Almagest), setting expectations for an applied doctrine. |
| Following direction | Chapters II–III defend the possibility and usefulness of prognostication, before Book I turns to planetary qualities and sign classifications. |
| Overall positioning | Book I Proem: methodological charter and epistemic boundary for the whole treatise. |

### L1.2 Historical Background and Academic Lineage (Brief)

| Dimension | Content |
|:---|:---|
| Writing context | Ptolemy (2nd c. CE) writes in a milieu that seeks systematic, “natural reason” explanations for celestial-terrestrial correspondence. |
| Academic lineage | Hellenistic astrology + Greco-Roman natural philosophy (qualities/causation), explicitly tied to mathematical astronomy (*Syntaxis*). |
| Later developments | Later traditions often amplified technique and certainty; modern critiques focus on falsifiability—exactly the limitation Ptolemy flags here (“no infallible rules”). |

---

## L3 - Semantic Essence Layer

### L3.1 Core Concept Deconstruction

| Concept | Literal Meaning | Deep Semantics | Modern Reconstruction |
|:---|:---|:---|:---|
| `two studies` | two preliminary studies | A workflow split: compute configurations → infer effects | `pipeline: compute → infer` |
| `figuration/aspect` | configuration/relationship | Structured relations among celestial bodies and key places (earth/angles) | `configuration_features` |
| `natural properties` | inherent qualities | Mechanism: qualitative causation (e.g., heat/cold/dry/moist) mediating effects | `quality_mechanism` |
| `Ambient` | environment | Causal medium for general events attributed to the heavens | `environment_mediator` |
| `no infallible rules` | bounded certainty | Domain constraint: outputs are tendency-level and uncertainty-aware | `probabilistic_forecast_scope` |

### L3.2 Abstract Rule Extraction

**Rule ID**: `rule_tetr_scope_two_stage_forecast`

**Rule Structure** (pseudo-code form):

```
IF <doing astrological prognostication>
THEN <compute configurations/aspects among luminaries/planets and key places>
AND <infer qualitative tendencies via natural properties and ambient mediation>
WITH confidence = Medium
BECAUSE <Tetrabiblos I.1 (Proem), lines 971-990>
```

**Rule Operationalization**:

| Dimension | Explanation |
|:---|:---|
| Trigger operationalization | Inputs: chart configurations (aspects, placements) and the target domain (what “objects under influence” are being judged). |
| Conclusion operationalization | Output format: qualitative tendency + explicit limits (avoid claiming determinism). |
| Confidence rationale | Medium because Ptolemy explicitly denies infallible rules due to material variability. |

### L3.3 Factor Extraction (Semantic Level)

| Factor Label | Factor ID | Semantic Essence | Extraction Justification |
|:---|:---|:---|:---|
| Two-stage prognostication workflow | `tetr_two_stage_prognostication` | Compute-first, interpret-second workflow | Explicitly defined as the two preliminary studies. |
| Material variability limit | `tetr_material_variability_limit` | Variability of sublunary matter limits certainty | Direct reason given for “no infallible rules.” |
| Ambient-mediated causation | `tetr_ambient_mediator` | General events trace causes to the “Ambient” | Named in the Proem as the locus of general causation. |

**Factor Status**: `new_candidate` (method/epistemic scaffolding)

---

## L4 - Cross-System Bridge Layer

### L4.1 Functional Equivalence Analysis

**Core Function**: Define a disciplined prediction workflow and an honesty constraint on certainty.

| Target System | Corresponding Concept | Functional Equivalence Argument | Academic Basis |
|:---|:---|:---|:---|
| BaZi (bazi) | 排盘 → 断语（先结构、后解释） | Both systems separate *structure computation* from *interpretation*, and both require guarding against over-certainty when inputs are incomplete or context-dependent. | Method-level analogy (workflow), not symbol-level identity. |

### L4.3 Neutral Semantic Tag Mapping

| neutral_tag | Mapping Rationale | Applicability Limits |
|:---|:---|:---|
| `neutral_transformation_opportunity` | Prognostication is framed as anticipating “changes” in the world under celestial influence, i.e., change navigation. | Keep at a meta “forecast supports navigating change” level; do not infer any specific life-domain outcome from this Proem alone. |

---

## L5 - Validation and Calibration Layer

### L5.1 Text-Internal Validation

**Case Source**: Tetrabiblos Book II, Chapter I (continuation of scope framing)

| Case Description | Conditions Met | Rule-Based Prediction | Actual Outcome | Validation Status |
|:---|:---|:---|:---|:---|
| Book II opens by proceeding “within the limits of natural reason” and formally divides astrology into general vs particular domains. | Proem sets scope, workflow, and epistemic boundary. | Later books should preserve natural-reason framing and structured divisions. | Book II reaffirms the boundary and operational division, matching the Proem’s program. | `Validated` |

---

## L6 - Meta-Reflection Layer

### L6.2 Uncertainty Annotation (Simplified)

| Layer | Uncertainty | Notes |
|:---|:---|:---|
| L1 Understanding | `Low` | The Proem is explicit about method and limitations. |
| L3 Extraction | `Medium` | Factorizing “Ambient” and “variability” risks over-formalization; must remain scoped to epistemic framing. |
| L4 Mapping | `Medium` | Workflow equivalence is plausible; symbol/content equivalence is intentionally avoided. |
| L5 Validation | `Low/Medium` | Internal-consistency validation, not empirical test. |

---

## Appendix

### A2 - Revision History

| Date | Reviser | Revision Content |
|:---|:---|:---|
| 2026-01-28 | LS-CAL-R11-TETR | Initial creation: Deep calibration for Book I purpose & scope (Proem) |

# Deep Calibration Card

## S - Synopsis

- `card_id`: `tetr_r11_book1_scope_001`
- `semantic_unit`: `Ptolemy defines astronomical prognostication as (1) computing configurations and (2) judging their natural effects, and sets a non-infallible, naturalistic scope for astrology.`
- `source_range`: `典籍/texts/Tetrabiblos/原文/Tetrabiblos.md:L971` ~ `L1006`
- `depth_level`: `Deep`
- `confidence`: `High`
- `last_updated`: `2026-01-28`

### Core Thesis in One Sentence
> Ptolemy frames astrology as the second half of astronomical prognostication—interpreting the natural effects of celestial configurations—while explicitly limiting it to reasoned, general tendencies rather than infallible rules.

---

## L1 - Deep Comprehension Layer

### L1.1 Source Text and Context

**Source Text**:
> The studies preliminary to astronomical prognostication, O Syrus! are  
> two: the one, first alike in order and in power, leads to the knowledge  
> of the figurations of the Sun, the Moon, and the stars; and of their  
> relative aspects to each other, and to the earth: the other takes into  
> consideration the changes which their aspects create, by means of their  
> natural properties, in objects under their influence.  
>   
> The first mentioned study has been already explained in the  
> Syntaxis[19] to the utmost practicable extent; for it is complete  
> in itself, and of essential utility even without being blended with  
> the second; to which this treatise will be devoted, and which is not  
> equally self-complete. The present work shall, however, be regulated  
> by that due regard for truth which philosophy demands: and since the  
> material quality of the objects acted upon renders them weak and  
> variable, and difficult to be accurately apprehended, no positive or  
> infallible rules (as were given in detailing the first doctrine, which  
> is always governed by the same immutable laws) can be here set forth:  
> while, on the other hand, a due observation of most of those general  
> events, which evidently trace their causes to the Ambient, shall not be  
> omitted.  
>   
> [19] The Almagest, or _Magna Constructio_.  
>   
> It is, however, a common practice with the vulgar to slander everything  
> which is difficult of attainment, and surely they who condemn the  
> first of these two studies must be considered totally blind, whatever  
> arguments may be produced in support of those who impugn the second.  
> There are also persons who imagine that whatever they themselves have  
> not been able to acquire, must be utterly beyond the reach of all  
> understanding; while others again will consider as useless any science  
> of which (although they may have been often instructed in it) they  
> have failed to preserve the recollection, owing to its difficulty of  
> retention. In reference to these opinions, therefore, an endeavour  
> shall be made to investigate the extent to which prognostication  
> by astronomy is practicable, as well as serviceable, previously to  
> detailing the particulars of the doctrine.

**Context Analysis**:

| Dimension | Analysis |
|:---|:---|
| Preceding context | The translator/editor’s preface and apparatus culminate in the presentation of Ptolemy’s text, positioning this treatise as the “second study” after the *Syntaxis* (Almagest). |
| Following direction | Chapters II–III immediately argue for the extent and usefulness of prognostication “by astronomy,” grounding astrology in natural causation before moving into planetary qualities and sign properties. |
| Overall positioning | Book I, Chapter I (Proem): program statement for method, epistemic limits, and the scope of what the work will (and will not) claim. |

### L1.2 Historical Background and Academic Lineage (Brief)

| Dimension | Content |
|:---|:---|
| Writing context | Claudius Ptolemy (2nd century CE, Alexandria) systematizes a “natural philosophy” version of astrology, explicitly pairing it with astronomy and delimiting certainty. |
| Academic lineage | Builds on Hellenistic astrology (aspects, configurations, domiciles) and Greco-Roman natural philosophy (qualities, causation through the “Ambient”). |
| Later developments | Medieval/Islamic/Latin astrological traditions often expanded technique and certainty claims; modern critiques frequently target precisely the “no infallible rules” problem Ptolemy pre-empts here. |

---

## L3 - Semantic Essence Layer

### L3.1 Core Concept Deconstruction

| Concept | Literal Meaning | Deep Semantics | Modern Reconstruction |
|:---|:---|:---|:---|
| `astronomical prognostication` | forecasting by astronomy | A two-part practice: (a) compute celestial configurations; (b) infer qualitative effects on sublunary matter | `two_stage_inference`: measurement/model → interpretation/effect |
| `figuration / aspect` | relative configurations | Structured relations between luminaries/planets and key places (earth, angles) that serve as inputs to judgment | `configuration_features`: graph of angular relations |
| `natural properties` | intrinsic qualities | The mechanism: qualities (heat/cold/dry/moist) mediate how celestial bodies “change” the Ambient and bodies | `quality_mechanism`: qualitative causal pathway |
| `Ambient` | surrounding environment | The shared causal medium linking celestial motions to general terrestrial events | `environmental_mediator`: macro conditions channeling influence |
| `no infallible rules` | no absolute certainty | Domain limitation: material variability and many interacting causes prevent deterministic prediction | `probabilistic_scope`: forecasts as tendencies with uncertainty |

### L3.2 Abstract Rule Extraction

**Rule ID**: `rule_tetr_scope_two_stage_and_non_infallible`

**Rule Structure** (pseudo-code form):

```
IF <you attempt astrological prognostication>
THEN <first compute configurations/aspects among luminaries/planets and key places>
AND <infer qualitative terrestrial tendencies via natural properties and ambient mediation>
WITH confidence = Medium
BECAUSE <Tetrabiblos Book I, Ch. I (Proem), lines 971-990>
```

**Rule Operationalization**:

| Dimension | Explanation |
|:---|:---|
| Trigger operationalization | Requires a computed chart model: luminaries/planets, their relative aspects, and their relation to the earth/angles (inputs). |
| Conclusion operationalization | Output should be phrased as *tendencies* (qualitative deltas) and explicitly bounded (no claims of infallibility). |
| Confidence rationale | Medium: the *framework* is explicit and stable; the *degree of predictive reliability* is stated as limited by material variability. |

### L3.3 Factor Extraction (Semantic Level)

| Factor Label | Factor ID | Semantic Essence | Extraction Justification |
|:---|:---|:---|:---|
| Two-stage prognostication | `tetr_two_stage_prognostication` | Separation of (1) configuration computation from (2) effect judgment | Directly stated as “two studies” defining method boundaries. |
| Material variability limit | `tetr_material_variability_limit` | Recognition that sublunary matter is weak/variable → no infallible rules | Explicitly motivates probabilistic/limited claims. |
| Ambient causal mediation | `tetr_ambient_mediator` | “Ambient” as causal channel for general events | Named as the locus where causes of general events are traced. |

**Factor Status**: `new_candidate` (all three; book-level method/epistemic scaffolding)

---

## L4 - Cross-System Bridge Layer

### L4.1 Functional Equivalence Analysis

**Core Function**: Establish a disciplined workflow and epistemic boundary for prediction: compute state → infer effects; treat outputs as tendencies constrained by uncertainty.

| Target System | Corresponding Concept | Functional Equivalence Argument | Academic Basis |
|:---|:---|:---|:---|
| BaZi (bazi) | 排盘（四柱/大运）→ 断语（十神/格局/旺衰） | BaZi similarly separates *chart construction* from *interpretive inference*, and good practice also distinguishes deterministic structure from contingent outcomes. | Methodological analogy (workflow-level), not a claim of one-to-one symbol identity. |

### L4.3 Neutral Semantic Tag Mapping

| neutral_tag | Mapping Rationale | Applicability Limits |
|:---|:---|:---|
| `neutral_transformation_opportunity` | Prognostication is framed as anticipating qualitative changes “in objects under their influence,” i.e., change/navigation support. | Use only at the “forecasting supports navigating change” level; do not treat as a direct mapping of any specific predictive outcome. |

---

## L5 - Validation and Calibration Layer

### L5.1 Historical / Text-Internal Validation

**Case Source**: Tetrabiblos internal cross-application (method reiterated in later books)

| Case Description | Conditions Met | Rule-Based Prediction | Actual Outcome | Validation Status |
|:---|:---|:---|:---|:---|
| Book II, Ch. I explicitly continues “within the limits of natural reason” and divides astrology into general vs particular domains. | Method requires scoped, naturalistic doctrine and structured inference. | Later content should preserve scoped claims and a structured workflow. | Book II opens by reaffirming natural-reason limits and formal division of domains, consistent with this Proem’s program. | `Validated` |

---

## L6 - Meta-Reflection Layer

### L6.2 Uncertainty Annotation (Simplified)

| Layer | Uncertainty | Notes |
|:---|:---|:---|
| L1 Understanding | `Low` | The Proem is a clear methodological statement. |
| L3 Extraction | `Medium` | Translating “Ambient” and “no infallible rules” into operational factors requires careful scoping to avoid over-claiming. |
| L4 Mapping | `Medium` | Workflow-level equivalence is safe; semantic one-to-one mappings are intentionally not asserted here. |
| L5 Validation | `Low/Medium` | Validation is internal-consistency based (cross-chapter), not empirical falsification. |

---

## Appendix

### A2 - Revision History

| Date | Reviser | Revision Content |
|:---|:---|:---|
| 2026-01-28 | LS-CAL-R11-TETR | Initial creation: Deep calibration for Book I scope/method Proem |

