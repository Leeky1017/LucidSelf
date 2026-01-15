# L3L4 Structured Extraction Template for Western Texts

> **Version**: v2 (2025-11-27)  
> **Target Role**: **For system-level tasks (L3/L4)**, used for structured design of rule content layer and narrative layer. Text-EN-Agent in current phase **does not use this template**.  
> **Related Templates**:  
> - L1/L2 Calibration & Factor Layer → `典籍/texts/Western_Texts_Template.md`  
> - L2.5 Bridge Layer → `典籍/texts/L2.5_Bridge_Layer_Template.md`  
> - L3/L4 General Process → `典籍/典籍结构化作业手册.md`

---

## 0. Agent Roles and Boundaries

- **Target Roles**:
  - **System-level L3 agent**: From `L3_CANDIDATE` comment blocks and L1/L2/Factor Layer in texts, organize stable rule specifications and narrative materials
  - **Rule Engineer**: Reference this template, map L3 content layer to Python rules, and design input structures for Narrative Generator per `RuleRegistry` / `RuleResult` specifications
  - **Product / Narrative Design**: Supplement style and evidence selection preferences in L4 section

- **Current Phase Text-EN-Agent Boundaries**:
  - Only needs to:
    - Complete L1/L2 + Factor Layer per `Western_Texts_Template.md`
    - If clear rule structures are found, mark candidate rules nearby using `<!-- L3_CANDIDATE_BEGIN ... --> ... <!-- L3_CANDIDATE_END -->`
  - **Not required** nor **allowed** to hand-write L3/L4 content for each source entry in this file
  - This file is maintained centrally by subsequent system-level tasks at appropriate phases

---

## 1. Entry Outer Structure and Positioning

### 1.1 Entry Anchor and Source Reference

Each L3/L4 record must be traceable to corresponding L1/L2 entry and factor layer. Recommended outer structure:

- `### [Book]·[Chapter]·[Entry Title]`
  - Example: `### The Inner Sky·Saturn·First House`
- Basic metadata:
  - `source_book`: Book name (e.g., "The Inner Sky", "78 Degrees of Wisdom")
  - `source_chapter`: Chapter name / section
  - `source_entry`: Entry number or source text excerpt (corresponds to L1 template `[Number]. [Entry Title]`)
  - `l1_anchor`: Anchor pointing to source in text file (e.g., Markdown heading / custom id)
  - `l2_refs`: Associated L2 section titles or semantic labels (can add `semantic_id` after onboarding)

> Rules and narrative layers **do not duplicate L1/L2 text**, only reference and link; if source text is needed, use short quotes or line numbers.

---

## 2. L3 Content Layer: Rule Specification

### 2.1 Rule List Structure (One Rule Per Row)

Use table format for rule list:

| Rule ID Draft | Rule Label | Associated L2/Semantic Core | Condition | Result Dimension | Result Direction | Result Description | Referenced L1/L2 Fragments & Factors | Scope/Notes |
|---------------|------------|----------------------------|-----------|------------------|------------------|--------------------|--------------------------------------|-------------|
| innersky_saturn_1h_001 | Saturn 1H Restriction | Saturn·First House | [Under what chart structure] | Personality/Career/... | Beneficial/Challenging/Neutral/Mixed | Tendency and typical manifestations | Which L1/L2 and factor labels | Usage boundaries and caveats |

**Field Descriptions**:

- **Rule ID Draft**: Use `book_abbreviation_topic_sequence` style (e.g., `innersky_saturn_1h_001`)
- **Rule Label**: One-sentence summary of rule's core meaning
- **Associated L2/Semantic Core**: L2 semantic unit this rule attaches to
- **Condition**: Complete if-condition describing prerequisites
- **Result Dimension**: Analysis dimension for rule conclusion (e.g., Personality / Career / Relationships / Health)
- **Result Direction**: `Beneficial` / `Challenging` / `Neutral` / `Mixed`
- **Result Description**: Natural language description of typical outcomes
- **Referenced L1/L2 Fragments & Factors**: L1 key sentences, L2 points, factor labels supporting this rule
- **Scope/Notes**: Usage limitations and conflict handling

### 2.2 Core Insights

After rule table, summarize 3-6 key insights:

- **Core Insights**:
  - `[Insight 1: Core logic directly usable for rule creation]`
  - `[Insight 2: ...]`
  - `[Insight 3: ...]`

### 2.3 Application Sequence

Describe how practitioners or systems apply this rule step by step:

1. `[Step 1: First observe which factors/structures]`
2. `[Step 2: How to combine factors for judgment]`
3. `[Step 3: How to adjust with transits/progressions]`
4. `[Step 4: When to use caution or defer conclusions]`

### 2.4 Counter-examples and Boundaries

- **Counter-examples**:
  - `[Misuse 1: When surface conditions match but conclusion doesn't hold]`
  - `[Misuse 2: ...]`

- **Applicable Boundaries**:
  - `[Boundary 1: Only applies under... conditions]`
  - `[Boundary 2: When conflicting with rule X, how to handle priority]`

---

## 3. L4 Narrative Layer: Narrative Draft

L4 layer provides **structured expression configuration** for Narrative Generator.

### 3.1 Narrative Configuration Structure

```yaml
narrative_profile:
  target_rules: ["innersky_saturn_1h_001", "innersky_saturn_1h_002"]
  tone: "supportive"  # Options: neutral / supportive / direct / serious / humorous
  perspective: "second_person"
  intensity: "medium"

  evidence_strategy:
    quote_l1: true
    quote_l2_summary: true
    surface_factors:
      - "Saturn in First House"
      - "Natal chart placement"

  prompt_blocks:
    opening_hint: |
      Begin with overall character impression, then Saturn's maturation theme.
    challenge_hint: |
      If restrictions or delays are present, frame as growth opportunities.
    closing_hint: |
      End with constructive advice, avoid deterministic statements.

  safety_and_boundaries:
    avoid_claims:
      - "This is your destiny"
      - "You cannot change this"
    required_disclaimers:
      - "This interpretation is based on astrological symbolism for self-reflection, not life decisions."
```

### 3.2 NarrativeSnippet Extraction

Narrative snippets are refined sentences from L1L2 calibration output, directly usable as LLM reference material.

#### NarrativeSnippet Table Structure

| snippet_id | trigger_condition | en_snippet | source_ref | related_rules |
|------------|-------------------|------------|------------|---------------|
| ns_innersky_001 | planet=saturn AND house=1 | Saturn in the first house fundamentally shapes personality through restriction. | The Inner Sky #Saturn-1H | innersky_saturn_1h_001 |
| ns_innersky_002 | planet=saturn AND house=1 AND life_phase=early | Early life typically involves significant obstacles and delays. | The Inner Sky #Saturn-1H | innersky_saturn_1h_001 |

---

## 3.3 L2.5 Bridge Layer to L3 Rule Transformation

### 3.3.1 Generating Rules from ConfigRelation

L2.5 Factor Relation Layer, after Schema validation, can generate Python rules via Codegen:

```python
# Generated by Codegen from ConfigRelation
# Source: rel_innersky_001 | planet_house | planet_saturn | house_1 | falls_in | - | restrictive

@register_rule(rule_id="rel_saturn_1h_001", category="planet_house")
def evaluate_saturn_first_house(
    factor_matrix: FactorMatrix,
    ctx: RuleExecutionContext
) -> RuntimeRuleResult:
    """Saturn in First House - Restriction"""
    saturn = factor_matrix.factors.get("planet_saturn")
    house_1 = factor_matrix.factors.get("house_1")
    
    if saturn and saturn.house == 1:
        return RuntimeRuleResult(
            rule_id="rel_saturn_1h_001",
            matched=True,
            dimension="Personality",
            level="Challenging",
            confidence=0.85,
            weight=1.2,
            tags=["saturn", "first_house", "restriction"],
            evidence_factors=["planet_saturn", "house_1"],
            semantic_refs=["innersky_saturn_sem_001"],
            source_book="The Inner Sky",
            l1_anchor="Saturn#First House",
            execution_time_ms=1.0
        )
    return RuntimeRuleResult(rule_id="rel_saturn_1h_001", matched=False, ...)
```

### 3.3.2 Generating Rules from EvidenceChainEntry

```python
# Generated by Codegen from EvidenceChainEntry
# Source: evi_innersky_001 | "Saturn...restricts" | planet_saturn, house_1 | Saturn limits personality | restrictive | High | ✅

@register_rule(rule_id="evi_saturn_restrict_001", category="personality_constraint")
def evaluate_saturn_restriction(
    factor_matrix: FactorMatrix,
    ctx: RuleExecutionContext
) -> RuntimeRuleResult:
    """Saturn restricts self-expression in First House"""
    saturn = factor_matrix.factors.get("planet_saturn")
    
    if saturn and saturn.house == 1:
        return RuntimeRuleResult(
            rule_id="evi_saturn_restrict_001",
            matched=True,
            dimension="Self-Expression",
            level="Restrictive",
            confidence=0.90,
            weight=1.5,
            tags=["saturn_restriction", "personality_challenge"],
            evidence_factors=["planet_saturn", "house_1"],
            semantic_refs=["innersky_saturn_sem_001"],
            source_book="The Inner Sky",
            l1_anchor="Saturn#limits self-expression",
            execution_time_ms=1.2
        )
    return RuntimeRuleResult(rule_id="evi_saturn_restrict_001", matched=False, ...)
```

### 3.3.3 L2.5 to L3L4 Data Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│  L2.5 Bridge Layer (Markdown Tables)                                    │
│  ┌────────────────┐ ┌────────────────┐ ┌────────────────┐              │
│  │ Relation Layer │ │ Evidence Chain │ │ Cross-System   │              │
│  │ ConfigRelation │ │ EvidenceChain  │ │ Mapping        │              │
│  └────────────────┘ └────────────────┘ └────────────────┘              │
└──────────────────────────────┬──────────────────────────────────────────┘
                               ↓ Extraction Script + Schema Validation
┌─────────────────────────────────────────────────────────────────────────┐
│  JSON/JSONL Configuration Source (Offline Transfer, Version Control)    │
│  data/relations/*.jsonl  data/evidence/*.jsonl  data/mappings/*.jsonl   │
└──────────────────────────────┬──────────────────────────────────────────┘
                               ↓ Codegen Compilation
┌─────────────────────────────────────────────────────────────────────────┐
│  L3 Rule Layer (Python Code) + L4 Narrative Layer                       │
│  backend/rules/generated/*.py  backend/narrative/snippets/*.py          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Migration Strategy

1. **Respect existing L1/L2 and Factor Layer**:
   - As long as existing content generally follows template spirit, it's valid input
   - L3/L4 work builds on top for "rule summarization and narrative design"

2. **Start from L3_CANDIDATE and historical rules**:
   - Prioritize consuming existing `L3_CANDIDATE` comment blocks
   - Organize into rule tables, core insights, application sequences per this template

3. **Phase-by-phase governance**:
   - Can complete L3/L4 by book / chapter / topic in batches
   - Each batch only needs to close loop within this template

4. **Clear role division**:
   - Text-EN-Agent: Focus on L1/L2 + Factor Layer
   - System-level L3/L4 tasks: Maintain this file and interface with Python rules
   - Engineering team: Map L3 content + Factor Layer + L4 narrative config to executable code

---

## 5. Summary

- All text structuring follows "**L1/L2 + Factor Layer first, then L3 Content Layer, then L4 Narrative Layer**"
- This file only defines **future L3/L4 content specification**, does not change any completed L1/L2 text
- Current phase Text-EN-Agent only needs to:
  - Complete L1/L2 and Factor Layer per `Western_Texts_Template.md`
  - Mark rule candidates with `L3_CANDIDATE` when needed
- Later, when system-level L3/L4 tasks start, organize rules and narrative per this template
