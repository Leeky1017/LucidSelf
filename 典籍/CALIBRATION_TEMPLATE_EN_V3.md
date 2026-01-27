# Western Text Deep Calibration Template V3.0

> **Version**: 3.0 | **Created**: 2026-01-27
> 
> **Design Principle**: Upgrade from "form-filling mechanical calibration" to "deep comprehension + critical analysis + cross-system argumentation + case validation" academic-grade calibration framework

---

## Conventions (MUST follow)

### Core Changes (vs V2.0)

| Dimension | V2.0 | V3.0 |
|:---|:---|:---|
| Granularity | One sentence per card | One semantic unit per card |
| Structure | A-F six sections (form-filling) | L1-L6 six layers (deep analysis) |
| Factor extraction | Direct surface extraction | Comprehend first, extract with justification |
| Cross-system mapping | No evidence required | Must provide academic argumentation |
| Validation | None | At least 1 case validation required |

### Semantic Unit Definition

**Semantic Unit** = A complete, independently comprehensible discourse, containing:
- One core thesis/proposition
- Supporting arguments/examples
- (Optional) Boundaries/exceptions

**Division Principles**:
1. **Completeness**: Contains thesis + argument + (boundaries)
2. **Independence**: Understandable when read alone
3. **Atomicity**: Further splitting would break argument structure
4. **Citability**: Can be independently referenced elsewhere

### Depth Levels

| Level | Target | Template Requirements |
|:---|:---|:---|
| **Scholarly** | Core concepts (P0) | Complete L1-L6 all fields |
| **Deep** | Main concepts (P1) | L1+L3+L4+L5 simplified |
| **Standard** | Supplementary concepts (P2) | L1+L3 core fields |
| **Index** | Index entries (P3) | S Synopsis only |

### Output Location

- Calibration cards go to `典籍/calibrated/cards/<book_abbr>/`
- File naming: `<book_abbr>_<concept>_<seq>.md`

### Hard Prohibitions

- Do NOT create cards for transitional or introductory sentences alone
- Do NOT extract factors without justification
- Do NOT map cross-system without evidence
- Do NOT draft rules that are not operationalizable
- Do NOT ignore applicability boundaries and limitations

---

## Deep Calibration Card Template (Copy to Use)

```markdown
# Deep Calibration Card

## S - Synopsis

- `card_id`: `<book_abbr>_<concept>_<seq>`
- `semantic_unit`: `<Brief description of the complete semantic unit, 10-30 words>`
- `source_range`: `<start anchor> ~ <end anchor>`
- `depth_level`: `Scholarly | Deep | Standard | Index`
- `confidence`: `High | Medium | Low | Mixed`
- `last_updated`: `<YYYY-MM-DD>`

### Core Thesis in One Sentence
> <Summarize the core insight of this semantic unit in one sentence, max 50 words>

---

## L1 - Deep Comprehension Layer

### L1.1 Source Text and Context

**Source Text**:
> <Complete semantic unit text, verbatim, may span multiple paragraphs>

**Context Analysis**:

| Dimension | Analysis |
|:---|:---|
| Preceding context | <What was discussed before? What does this section follow from?> |
| Following direction | <How does the text develop afterwards? What does this section set up?> |
| Overall positioning | <Position and function within the book's structure> |

### L1.2 Historical Background and Academic Lineage

| Dimension | Content |
|:---|:---|
| Writing context | <Author's era, writing purpose, socio-cultural context> |
| Academic lineage | <Intellectual predecessors, explicit or implicit references, school of thought> |
| Later developments | <How was this view received, developed, or criticized by later scholars?> |

### L1.3 Author's Intent and Rhetorical Analysis

| Dimension | Analysis |
|:---|:---|
| Author's intent | <What does the author want readers to accept? What belief to convey?> |
| Rhetorical strategy | <What argumentative methods? Example/analogy/contrast/induction/deduction/authority?> |
| Implicit assumptions | <What premises does the author assume readers already accept?> |

---

## L2 - Critical Analysis Layer

### L2.1 Logical Evaluation of Arguments

| Dimension | Assessment | Explanation |
|:---|:---|:---|
| Are premises reasonable? | `Reasonable / Partially / Questionable` | <Specify which premises are sound, which are questionable> |
| Is reasoning valid? | `Valid / Partially / Questionable` | <Is the reasoning logically consistent? Any gaps?> |
| Is conclusion reliable? | `Reliable / Partially / Questionable` | <Reliability of conclusion and its dependencies> |

### L2.2 Comparison with Other Texts

| Text | Related View | Relationship | Analysis |
|:---|:---|:---|:---|
| `<book_abbr>` | <Quote or summary> | `Consistent / Complementary / Tension / Conflict` | <Analyze reasons for consistency or tension, academic significance> |

### L2.3 Limitations and Applicability Boundaries

| Dimension | Content |
|:---|:---|
| Applicable conditions | <Under what circumstances does this view hold? What prerequisites?> |
| Inapplicable conditions | <When might it fail or need modification?> |
| Known counterexamples | <Are there known counterexamples or exceptions? How explained?> |
| Modern perspective corrections | <How might modern knowledge (psychology/cognitive science) supplement or correct this?> |

---

## L3 - Semantic Essence Layer

### L3.1 Core Concept Deconstruction

| Concept | Literal Meaning | Deep Semantics | Modern Reconstruction |
|:---|:---|:---|:---|
| `<term>` | <Dictionary definition> | <True meaning in this context, author's special connotation> | <Restate in modern language/concepts, understandable and operationalizable> |

### L3.2 Abstract Rule Extraction

**Rule ID**: `rule_<book_abbr>_<semantic_tag>`

**Rule Structure** (pseudo-code form):

```
IF <trigger condition: using factor expressions, be specific>
AND <situational condition: what scenario/context applies>
THEN <judgment conclusion: specific, operationalizable>
WITH confidence = <High/Medium/Low>
BECAUSE <evidence citation: source location>
UNLESS <exception condition: when does the rule not apply>
```

**Rule Operationalization**:

| Dimension | Explanation |
|:---|:---|
| Trigger operationalization | <How to determine if conditions are met in practice? What inputs needed?> |
| Conclusion operationalization | <What specific judgment or recommendation does the conclusion imply? How to present to users?> |
| Confidence rationale | <Why this confidence level? What is the basis?> |

### L3.3 Factor Extraction (Semantic Level)

| Factor Label | Factor ID | Semantic Essence | Extraction Justification |
|:---|:---|:---|:---|
| `<human-readable label>` | `<factor_id>` | <What does this factor truly represent semantically? Not surface word-splitting> | <Justification: why extract this factor from this text? What's the textual basis?> |

**Factor Status**: `existing` (already in factor ontology) / `new_candidate` (needs to be added)

---

## L4 - Cross-System Bridge Layer

### L4.1 Functional Equivalence Analysis

**Core Function**: <What is the function of this concept/rule in the original system (astrology/psychology/dreams)? What problem does it solve?>

| Target System | Corresponding Concept | Functional Equivalence Argument | Academic Basis |
|:---|:---|:---|:---|
| BaZi (bazi) | `<concept>` | <Why functionally equivalent: what problem solved, what effect produced, role in system> | <Academic literature, classic citations, or logical argument> |
| Psychology (psych) | `<concept>` | <same> | <same> |
| Dreams (dream) | `<concept>` | <same> | <same> |
| Tarot (tarot) | `<concept>` | <same> | <same> |

### L4.2 Cultural Context Translation

| Source Culture Expression | Target Culture Expression | Translation Strategy | Gain/Loss Analysis |
|:---|:---|:---|:---|
| `<English concept>` | `<Chinese/Eastern concept>` | <How to translate: literal/sense/functional equivalence/neologism> | <What's preserved, what's lost, potential misunderstandings> |

### L4.3 Neutral Semantic Tag Mapping

| neutral_tag | Mapping Rationale | Applicability Limits |
|:---|:---|:---|
| `<tag_id>` | <Why can this concept map to this neutral tag? What's the logical basis?> | <Within what scope is this mapping valid? Where are the boundaries?> |

---

## L5 - Validation and Calibration Layer

### L5.1 Historical Case Validation

**Case Source**: <Cases from classics, historical figures, case studies, etc.>

| Case Description | Conditions Met | Rule-Based Prediction | Actual Outcome | Validation Status |
|:---|:---|:---|:---|:---|
| `<case summary>` | <Which conditions from L3 rule are met> | <What conclusion should the extracted rule yield> | <Historical/textual actual result> | `Validated / Counterexample / Partial` |

**Validation Analysis**: <If counterexample or partial, analyze reasons, whether rule needs revision>

### L5.2 Modern Application Test Design

| Dimension | Content |
|:---|:---|
| Test scenario | <How would you design a test to validate this rule in modern context?> |
| Test method | <Specific validation methodology> |
| Success criteria | <What results would prove the rule effective> |
| Failure criteria | <What results would prove the rule ineffective or needing revision> |

### L5.3 Academic Literature / Expert Knowledge Verification

| Source Type | Source | Related View | Relationship to This Calibration | Citation/URL |
|:---|:---|:---|:---|:---|
| Academic paper | <Author, title> | <Summary of related view> | `Support / Supplement / Correct / Challenge` | <DOI/URL> |
| Classic work | <Title, author> | <Related view> | `Support / Supplement / Correct / Challenge` | <Chapter citation> |
| Expert opinion | <Expert, source> | <View> | `Support / Supplement / Correct / Challenge` | <Source> |

---

## L6 - Meta-Reflection Layer

### L6.1 Calibration Process Self-Review

| Dimension | Reflection |
|:---|:---|
| Main difficulties | <What was the biggest challenge in calibration? How was it addressed?> |
| Subjective judgments | <Where did calibrator's subjective judgment play a role? What was the basis?> |
| Potential biases | <What biases might the calibrator have brought in? How to minimize?> |

### L6.2 Uncertainty Annotation

| Layer | Uncertainty | Explanation |
|:---|:---|:---|
| L1 Comprehension | `Low / Medium / High` | <Which understandings might be wrong? Dependent on what?> |
| L2 Critical | `Low / Medium / High` | <How reliable is the critical analysis? Blind spots?> |
| L3 Extraction | `Low / Medium / High` | <Factor and rule extraction reliability? Over-interpretation?> |
| L4 Mapping | `Low / Medium / High` | <Cross-system mapping reliability? Forced connections?> |
| L5 Validation | `Low / Medium / High` | <Is validation sufficient? Representative samples?> |

### L6.3 Questions for Further Research

1. <Question 1: Issues requiring further research to determine>
2. <Question 2>
3. <Question 3>

---

## Appendix

### A1 - Web Verification Records

| Verification Dimension | Method | Result | Reference URL |
|:---|:---|:---|:---|
| Source accuracy | <Compared with Archive.org/Google Books/Publisher edition> | <Verified/Discrepancy-corrected/Discrepancy-pending> | <URL> |
| Term universality | <Searched academic/standard definitions> | <Standard/Non-standard-explanation> | <URL> |
| Academic views | <Searched relevant academic papers> | <Support/Supplement/Correct/Challenge> | <URL> |

### A2 - Revision History

| Date | Reviser | Revision Content |
|:---|:---|:---|
| <YYYY-MM-DD> | <ID> | <Initial creation/revision notes> |
```

---

## Quality Checklist (Self-check after completion)

### Scholarly Level Checklist

- [ ] **S Synopsis**: Core thesis accurately captures the semantic unit's insight
- [ ] **L1.1**: Source text complete, context analysis clear
- [ ] **L1.2**: Historical background and academic lineage verifiable
- [ ] **L1.3**: Author's intent and rhetorical strategy analysis reasonable
- [ ] **L2.1**: Logical evaluation honest, does not avoid questionable areas
- [ ] **L2.2**: Compared with at least 1 other text
- [ ] **L2.3**: Applicability boundaries and limitations clearly stated
- [ ] **L3.1**: Deep semantics of core concepts go beyond literal meaning
- [ ] **L3.2**: Rule is operationalizable, can write pseudo-code
- [ ] **L3.3**: Factor extraction justified, not simple word-splitting
- [ ] **L4.1**: Cross-system mapping based on functional equivalence with academic basis
- [ ] **L4.3**: Neutral tag mapping has logical justification
- [ ] **L5.1**: At least 1 case validation
- [ ] **L5.3**: Referenced relevant academic literature or classic works
- [ ] **L6.2**: Honestly annotated uncertainty at each layer
- [ ] **L6.3**: Listed questions for further research

---

## Version Notes

| Version | Date | Major Changes |
|:---|:---|:---|
| V1.0 | - | A-F six-section form-filling template |
| V2.0 | - | Added G section for web verification |
| V3.0 | 2026-01-27 | Complete restructure to L1-L6 six-layer deep analysis model, emphasizing comprehension-critique-argumentation-validation |
