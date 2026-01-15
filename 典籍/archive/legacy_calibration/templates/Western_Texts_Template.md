# L1+L2 Calibration Template for Western Texts (Bilingual Standard)

> **Last Updated**: 2025-11-27 (v2.1)  
> **Applicable Scope**: Western Astrology, Tarot, Dream Symbolism, Psychology texts requiring L1/L2 calibration  
> **Status**: **This is the official bilingual L1+L2 calibration template for English-primary texts**  
> **Core Principle**: **Primary Language and Secondary Language both require complete in-depth interpretation, equal depth without hierarchy, mutually mirroring, localized optimization**  
> **v2.1 Updates**: Factor layer upgraded to eight columns (added engine_id); Term glossary adds factor_id/status columns; Narrative snippets add factor_trigger field; Conditional structure adds temporal scope.

---

## 0. Agent Roles and Work Boundaries

- **Target Roles**:
  - **Text-EN-Agent**: Completes L1 text calibration + L2 semantic extraction + L2.5 bridge layer + factor layer annotation for English texts
  - **System-level agents**: Use L2 and factor layer outputs for L3 rules and narrative design (not Text-EN-Agent's responsibility)

- **Text-EN-Agent Work Boundaries**:
  - ✅ **Must Complete**:
    - L1: Source text organization, annotations, English paraphrase, core points, detailed explanation, textual criticism
    - L2: Semantic extraction (themes / natural attributes / functional symbolism / conditions / multi-layered interpretation)
    - Factor Layer: Semantic factor table with `existing` / `new_candidate` markers
    - L2.5: Factor Relation table + Evidence Chain table + Cross-System Mapping table (all three mandatory)
  - 🚫 **Explicitly Prohibited**:
    - Writing formal L3 rule tables
    - Writing Python rule functions
    - Directly editing JSON / JSONL / YAML rule files
    - Creating factor IDs or `semantic_id` - only write human-readable labels and `existing/new_candidate` markers
  - 💡 **If rule ideas naturally emerge in L1 explanations**:
    - Only write in **natural language** within L1 "Detailed Explanation"
    - Or add `<!-- L3_CANDIDATE_BEGIN ... -->` comment blocks for future L3 tasks
    - **Never** write these into L2 fields or factor IDs

---

## 1. Bilingual Calibration Principles (English-Chinese Equal Depth Strategy)

### 1.1 Primary and Secondary Language Definition

- **Primary Language**: English - provides complete in-depth interpretation
  - For Western Astrology, Tarot, Psychology texts → Primary = **English**
  
- **Secondary Language**: Chinese - provides complete in-depth interpretation equal to Primary
  - For English texts → Secondary = Chinese (**complete interpretation, not brief summary**)
  - **Depth Requirement**: Secondary must be as thorough as Primary, enabling Chinese readers to fully understand without referencing English

### 1.2 Bilingual Depth Requirements

**Core Principle: Both languages require complete in-depth treatment, not translation but localized expression**

- ✅ **Both languages must provide**:
  - Complete normalized interpretation (full depth, not superficial)
  - Full semantic extraction
  - Complete term definitions
  - Full textual criticism (bilingual)

- ✅ **Localization Requirements**:
  - **English**: Use natural English expressions, avoid Pinyin stacking
  - **Chinese**: Use idiomatic Chinese, avoid literal translation style
  - Find culturally equivalent concepts, not word-for-word correspondence

### 1.3 Term Alignment Requirements

- Each technical term must establish English-Chinese correspondence on first appearance
- Terms must be registered in factor ontology (lucidself_factor_ontology.md) first
- Maintain consistent translation throughout the text
- Handle synonyms through aliases

---

## 2. Single Entry Calibration Structure (L1 + L2 + Factor Layer)

### 2.1 Entry Outer Structure

Each text entry should follow this structure:

- `#### [Number]. [Entry Title or First Sentence]`
  - Followed by **L1 Section**, **L2 Section**, and **Factor Table**
  - Audit markers (mandatory convention for FACTOR table):
    - `<!-- L1_BEGIN --> ... <!-- L1_END -->`
    - `<!-- L2_BEGIN --> ... <!-- L2_END -->`
    - `<!-- FACTOR_BEGIN --> ... <!-- FACTOR_END -->`

> Note: Heading levels (`###`/`####`) can be adjusted per document structure, but **field names and order must align with this template**.

---

### 2.2 L1 Section (Text Layer, Bilingual Enhanced)

Under each `[Number]. [Entry Title]`, write in order:

- **Source Text**:  
  `[Original English passage, maintaining original phrasing and punctuation]`

- **Original Annotations** (if present in source):  
  `[Source text's own annotations, preserve original wording, adjust punctuation only]`

- **Key Term Analysis** (decompose exhaustively, no upper limit):
  - `[Term 1]`: `[literal meaning]` / `[symbolic significance]` / `[contextual usage]`
  - `[Term 2]`: `[literal meaning]` / `[symbolic significance]` / `[contextual usage]`
  - … (as many terms as exist, each term on separate line)

- **English Paraphrase (Primary Language)**:  
  `[Complete in-depth English interpretation with full normalized explanation. Develop thoroughly, not superficially]`

- **Complete Chinese Interpretation (Secondary Language)**:  
  `[完整深度的中文诠释，与英文Primary完全对等深度。使用地道中文表达，非直译英文，确保中文读者无需参照英文即可完全理解全部内容]`

- **Core Points** (decompose by semantic unit, no upper limit):
  - `[Each point expresses ONE independent insight or structural observation]`
  - `[As many independent insights as exist, prefer more over fewer, avoid merging semantics]`

- **Detailed Explanation**:  
  `[Extended explanation of structure, reasoning chains, and implications. Keep close to source text, avoid subjective interpretation]`

- **Narrative Snippets** (primary language only, decompose exhaustively):
  - `[ns_ID_001]` `[trigger: trigger_condition]` `[factor_trigger: factor_id_expression (mandatory)]` `[role: logical_role]` `[refined snippet in English]` → `[source anchor]`
  - `[ns_ID_002]` `[trigger: trigger_condition]` `[factor_trigger: factor_id_expression (mandatory)]` `[role: logical_role]` `[refined snippet in English]` → `[source anchor]`
  - … (decompose by semantic atom, no upper limit)

**Narrative Snippet Requirements**:
  - **Maximum decoupling**: Decompose by semantic unit, each snippet expresses **one independent image or judgment**, never merge multiple semantics
  - **Concise and powerful**: 10-40 words per snippet, independently understandable without context
  - **Vivid imagery**: Prioritize sentences with metaphors or imagery
  - **Tag trigger conditions**: Each snippet tags its corresponding factor/condition combination (human-readable, to be systematized as `trigger_condition` later)
  - **Tag factor_trigger (mandatory)**: Use `factor_id` to express trigger conditions, enabling direct Codegen generation of NarrativeSnippet
    - If factor is registered in factor ontology (existing), use official factor_id
    - If factor is new_candidate, use suggested ID format: `[category]_[semantic]`, e.g., `condition_saturn_1h`
    - Format examples: `planet_saturn AND house_1`, `day_master_jia OR day_master_yi`
  - **Tag logical role (`role`)**: For each snippet, mark its logical position in the reasoning chain. Allowed values (LS standard, in Chinese for consistency): `主干` / `主干依赖` / `条件分支` / `例外处理` / `总结`
  - **Traceable**: Must tag source anchor, corresponding to L1 source position
  - **ID format**: `ns_book_abbreviation_sequence` (e.g., `ns_innersky_001`, `ns_waite_042`), continuous numbering per book
  - **Source priority**: English Paraphrase > Core Points > Detailed Explanation > Source Text refined
  - **No free creation**: Snippets must have source text basis, no creation beyond source
  - **No upper limit**: Extract as many usable snippets as possible, prefer more over fewer

> L1 layer only handles "text + multi-layered interpretation + narrative snippets", not rules or engine structures. Any rule-like content here is treated as **unstructured explanation**.

- **Textual Criticism & Variant Analysis (Bilingual, mandatory)**:
  - **English**: `[Edition A reads X, Edition B reads Y, we follow Z because... Critical analysis of key terms and version differences]`
  - **中文**: `[某版本作 X，某版本作 Y，本文采用 Z，理由是……关键术语的版本差异分析]`
  - (If no variants exist, write: "N/A: Single authoritative source, no textual variants.")

> **Bilingual Requirements**: Source text remains in English; both Primary and Secondary languages provide **complete in-depth interpretation of equal depth**. Textual criticism must be bilingual. Both languages must be localized expressions, not mechanical translations.

---

### 2.3 L2 Section: Semantic Extraction (Pure Semantic Layer)

Following L1 section, write the L2 section with this structure:

- **Semantic Extraction (L2)**:
  - **Theme**: `[Core object / scenario / mechanism this entry focuses on]`
  - **Natural Attributes**:
    - Symbolism: `[...]`  
    - Characteristics: `[...]`  
    - Elements (planetary / zodiacal / house / aspect / archetype): `[...]`
  - **Functional Symbolism**:
    - `[...] Function 1`  
    - `[...] Function 2`
  - **Conditional Structure** (include if relevant):
    - **Necessary Conditions**: `[Prerequisites that must be met]`
    - **Enhancing Conditions**: `[Additional factors that strengthen the effect]`
    - **Nullifying Conditions**: `[Circumstances that weaken or reverse the proposition]`
    - **Temporal Scope (check applicable items)**:
      - [ ] Natal layer: Applies to natal chart analysis
      - [ ] Transit layer: Applies to planetary transit analysis
      - [ ] Progression layer: Applies to progressed chart analysis
  - **Multi-layered Interpretation (Structured Points)**:
    - Literal Layer: `[...]`  
    - Symbolic Layer: `[...]`  
    - Practical/Manifest Layer: `[...]`  
    - Psychological Layer (mandatory): `[...]`

**Writing Requirements**:

- Use bullet lists with **complete point sentences**
- **Correspond to specific sentences or passages** in source text, avoid free interpretation
- Allow reasonable abstraction and generalization, but must be grounded in source text and L1 explanation
- One source passage can be decomposed into 1-N L2 units, use sub-headings if needed (e.g., "L2-1: Saturn in First House", "L2-2: Saturn in Tenth House")

> L2 only answers "what it is" and "what generally happens under what conditions", **not boolean judgments of "whether it's true"**, nor final fortune/misfortune conclusions.

---

### 2.4 Factor Layer Section: Semantic Factor Table

After L2 section, add the factor layer table with **eight columns** (v2.1 upgrade: added engine_id column):

| Factor Type | Factor Label (Human-readable) | Factor ID (mandatory) | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|-------------------------------|------------------------|---------------|---------------|-------------------|-----------|-------|
| [Type]      | [label_1]                     | [factor_id_1 or empty] | existing / new_candidate | [role_1] | [...] | [engine_module] | [...] |
| ...         | ...                           | ...                    | ...           | ...           | ...               | ...       | ...   |

**Column Meanings (Concise)**:

- **Factor Type**: Structure / State / Temporal / Boundary / Relational / Energy, etc.
- **Factor Label (Human-readable)**: Natural language label, e.g., "Saturn in 1st House", "Major Arcana Card", "Jung Shadow Archetype". Use **minimum viable conceptual granularity (最小可行颗粒度)**: labels should represent reusable semantic units (usually words/phrases describing stable factors), not mechanical single-word fragments like "in", "of", "the".
- **Factor ID (mandatory)**:
  - If factor exists in engineering factor library, fill official factor_id, e.g., `planet_saturn`, `house_1`, `aspect_conjunction`
  - If factor is new_candidate, fill suggested ID format: `[category]_[semantic]`, e.g., `state_saturn_dignity`
  - Never leave empty, must fill
- **Factor Source**:
  - `existing`: Factor exists in library, Factor ID must be official, can be referenced directly in rules/code
  - `new_candidate`: New concept proposed by content side, Factor ID must use suggested format `[category]_[semantic]`, awaiting "factor onboarding" process
- **Role/Position**: e.g., "Planet", "House", "Aspect", "Card Position", "Dream Symbol", "Archetype"
- **Value/Constraints**: Typical values / enumerations / ranges / thresholds
- **engine_id** (v2.1 new): Specify the engine module this factor belongs to, aligning with `ls_engine_architecture_v3.md` §4.6 Engine Registry:
  - Astrology system: `astro_calculator` / `astro_semantic` / `astro_rule_engine`
  - Tarot system: `tarot_calculator` / `tarot_semantic` / `tarot_rule_engine`
  - Dream system: `dream_semantic` / `dream_rule_engine`
  - Psychology system: `psych_semantic` / `psych_rule_engine`
  - Bazi system: `bazi_calculator` / `bazi_semantic` / `bazi_rule_engine`
  - Cross-engine common factors: `common`
- **Notes**: Relationships with other factors, caveats, version records

> **Hard Constraint**: Future rule JSON/JSONL, inference engines, and Python rules can only directly depend on rows with `Factor Source = existing` and assigned `Factor ID`; `new_candidate` rows are for design discussion only, not to be written into rule files or code.

---

## 3. L2 "No Boolean Judgment" Hard Constraint

L2 is a **pure semantic layer**, describing objects, attributes, conditions, and multi-layered interpretations, **not logical judgments or rule execution results**. Therefore:

- ❌ **Prohibited in L2 or Factor Layer**:
  - `is_xxx = true/false` boolean fields
  - `triggered`, `matched`, `pattern_matched`, `condition_met` or similar "hit or miss" fields
  - Any direct conclusion stating "this rule holds / does not hold"
- ✅ **Allowed patterns**:
  - Descriptive values: `jupiter_strength: 0.85` (degree of strength, an attribute not a judgment)
  - Conditional points: `necessary_conditions` list, `enhancing_conditions`, `nullifying_conditions` (still "prerequisite descriptions", no true/false)

**Example (Correct)**:

```yaml
L2:
  subject: "Saturn in First House"
  necessary_conditions:
    - "Saturn positioned in the first house"
    - "Natal chart context"
  attribute_scores:
    restriction_level: 0.75  # Descriptive value, not judgment result
```

**Example (Incorrect, Prohibited)**:

```yaml
L2:
  subject: "Saturn in First House"
  is_afflicted: true        # ❌ Judgment logic, belongs in L3
  pattern_matched: false    # ❌ Rule execution result, not L2
```

> If such fields are found in old documents, calibration agents need not restructure immediately; just avoid adding similar fields in current edits, and mark with `L3_CANDIDATE` comments for future L3 cleanup tasks.

---

## 4. L2-Embedded Term Glossary (Unified Position)

### 4.1 Glossary Position (Unified in L2 Section)

**Mandatory**: Term glossary must be embedded within L2 section, not at chapter end:

```markdown
<!-- L2_BEGIN -->
- **Semantic Extraction (L2)**:
  - **Theme**: ...
  - **Natural Attributes**: ...
  - **Functional Symbolism**: ...
  - **Conditional Structure**: ...
  - **Multi-layered Interpretation**: ...

- **L2-Term Glossary**:

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Ascendant | 上升点 | The zodiacal degree rising on the eastern horizon at birth | 出生时东方地平线升起的黄道度数，代表个性面具 | ascendant | existing |
| Conjunction | 合相 | Planets within 0-10° forming unified energy | 行星相距0-10度形成统一能量场 | aspect_conjunction | existing |
| Shadow | 阴影 | Jung's repressed unconscious aspects seeking integration | 荣格理论中被压抑的无意识面向，寻求整合 | psych_archetype_shadow | existing |
<!-- L2_END -->
```

### 4.2 Term Granularity and Localization Requirements

- **Granularity (minimum viable conceptual unit / 最小可行颗粒度)**: Extract terms at the level of stable technical concepts (single words or short phrases), not mechanical token/character splits. Avoid flooding the glossary with function words or trivial fragments; single-word entries are acceptable only when they are established technical terms (e.g., Ascendant, Saturn, Shadow).

- **factor_id column**: If the term is registered in factor ontology, fill in the official factor_id; otherwise leave empty
- **status column**: `existing` (already in factor library) or `new_candidate` (pending onboarding), consistent with factor layer markers

- **English→Chinese**: Find culturally equivalent Chinese concepts, avoid literal translation
  - Example: "Shadow" → "阴影/潜意识暗面" (not just "影子")
  - Example: "Ascendant" → "上升点/命宫起点" (cultural context added)
  
- **Chinese→English**: Use English-world comprehensible concepts, avoid Pinyin stacking
  - Example: "七杀" → "Seven Killings / Aggressive Controller" (not just "Qi Sha")
  - Example: "日主" → "Day Master / Self-Element" (explanatory translation)

- All terms must be registered in factor ontology before use
- Maintain consistency across entire text
- Use aliases for synonyms

---

## 5. Applicable Directories and Examples

### 5.1 Target Directories

This template applies to:
- `texts/astro/**` - Western astrology texts
- `texts/dream/**` - Dream symbolism and interpretation texts  
- `texts/psychology/**` - Psychology texts (Jung, Freud, etc.)

### 5.2 Example Entry (Western Astrology)

```markdown
#### 1. Saturn in the First House

<!-- L1_BEGIN -->
**Source Text**:
Saturn in the first house of the natal chart indicates a serious, reserved demeanor. The native often experiences delays and restrictions in early life, developing resilience and self-discipline through challenges.

**English Paraphrase**:
When Saturn occupies the first house of the natal chart, it fundamentally shapes the native's personality structure and life approach through the principle of restriction and maturation. This placement creates an individual who naturally embodies gravity, seriousness, and a sense of responsibility that others immediately perceive. The first house governs one's physical presence, initial self-expression, and the persona presented to the world—with Saturn here, these manifestations carry an inherent weight and solemnity. Early life typically involves significant obstacles, delays, and limitations that may manifest as childhood hardships, parental strictness, or circumstances demanding premature responsibility. However, these very challenges serve as the crucible through which resilience, self-discipline, and authentic authority are forged. Over time, what initially feels burdensome transforms into enduring strength and wisdom.

**Complete Chinese Interpretation**:
土星落入本命盘第一宫时，通过「限制与成熟」的原则从根本上塑造了命主的人格结构与人生态度。此配置造就的个体天然散发出庄重、严肃以及责任感，他人在初次见面时便能立即感知到这种气质。第一宫主管个人的物质呈现、最初的自我表达以及向世界展示的面具——当土星位于此宫时，这些显化都带有内在的分量与庄严感。早年生活通常会遭遇显著的障碍、延迟和限制，可能表现为童年艰辛、父母严苛，或是需要过早承担责任的环境。然而，正是这些挑战成为熔炉，淬炼出坚韧、自律和真实的权威感。随着时间推移，最初感到沉重的负担会转化为持久的力量和智慧。

**Core Points** (decomposed, no upper limit):
- Saturn in first house shapes personality through restriction
- Creates reserved, serious demeanor perceived immediately by others
- First house governs physical presence and initial self-expression
- Saturn here brings inherent weight and solemnity to persona
- Early life involves significant obstacles and delays
- Childhood hardships or parental strictness common
- Circumstances often demand premature responsibility
- Challenges serve as crucible for resilience building
- Self-discipline develops through adversity
- What feels burdensome transforms into enduring strength
- Authority becomes authentic over time
- Wisdom emerges from early limitations

**Detailed Explanation**:
Saturn's placement in the first house fundamentally shapes the native's approach to life and self-expression. This position often manifests as a natural gravitas that others perceive immediately upon meeting the individual. The first house governs physical appearance and initial impressions, so Saturn here can create a mature or aged appearance even in youth...

**Narrative Snippets** (English only, decomposed exhaustively):
 - `[ns_innersky_001]` `[trigger: saturn_in_house_1]` `[role: 主干]` Saturn in the first house fundamentally shapes the native's personality structure through the principle of restriction and maturation. → The Inner Sky #Saturn-1H
 - `[ns_innersky_002]` `[trigger: saturn_in_house_1]` `[role: 主干依赖]` This placement creates an individual who naturally embodies gravity, seriousness, and a sense of responsibility that others immediately perceive. → The Inner Sky #Saturn-1H
 - `[ns_innersky_003]` `[trigger: saturn_in_house_1]` `[role: 主干依赖]` The first house governs one's physical presence and the persona presented to the world—with Saturn here, these carry inherent weight and solemnity. → The Inner Sky #Saturn-1H
 - `[ns_innersky_004]` `[trigger: saturn_in_house_1 AND early_life]` `[role: 条件分支]` Early life typically involves significant obstacles, delays, and limitations. → The Inner Sky #Saturn-1H
 - `[ns_innersky_005]` `[trigger: saturn_in_house_1 AND childhood]` `[role: 条件分支]` Childhood hardships, parental strictness, or circumstances demanding premature responsibility are common. → The Inner Sky #Saturn-1H
 - `[ns_innersky_006]` `[trigger: saturn_in_house_1 AND maturation]` `[role: 条件分支]` These challenges serve as the crucible through which resilience, self-discipline, and authentic authority are forged. → The Inner Sky #Saturn-1H
 - `[ns_innersky_007]` `[trigger: saturn_in_house_1 AND later_life]` `[role: 总结]` Over time, what initially feels burdensome transforms into enduring strength and wisdom. → The Inner Sky #Saturn-1H
<!-- L1_END -->

<!-- L2_BEGIN -->
**Semantic Extraction (L2)**:
- **Theme**: Saturn's influence on personality and life approach when in the first house
- **Natural Attributes**:
  - Symbolism: Restriction, maturity, responsibility, time
  - Characteristics: Serious, cautious, disciplined, enduring
  - Elements: Earth element, cardinal quality, angular house
- **Functional Symbolism**:
  - Personality shaping through limitation
  - Character building through adversity
  - Authority development through experience
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Saturn placement | planet_saturn | existing | Planet | House 1 | astro_calculator | Angular house |
| State | First house occupied | house_1 | existing | House | Natal position | astro_calculator | Personality house |
| Relational | Saturn-Ascendant aspect | | new_candidate | Aspect | 0-10° | astro_rule_engine | Needs calculation |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_innersky_001 | planet_house | planet_saturn | house_1 | Saturn rules 1H | - | restrictive | The Inner Sky #Saturn-1H |
| rel_innersky_002 | planet_aspect | planet_saturn | ascendant | Conjunct ASC | orb<10° | restrictive | The Inner Sky #Saturn-1H |
| rel_innersky_003 | psych_archetype_relation | planet_saturn | senex_archetype | Saturn=Senex | - | neutral | The Inner Sky #Saturn-1H |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_innersky_001 | "Saturn in 1H shapes personality through restriction" | planet_saturn, house_1 | Saturn in angular house→direct life impact→personality restriction | Saturn 1H = reserved personality | High | ✅ | rule_saturn_1h_reserved |
| evi_innersky_002 | "early life involves significant obstacles and delays" | planet_saturn, house_1 | Saturn = delays→1H = early life→early life delays | Saturn 1H = early obstacles | High | ✅ | rule_saturn_1h_early_delays |
| evi_innersky_003 | "what feels burdensome transforms into enduring strength" | planet_saturn, house_1 | Saturn challenges→time→maturation→strength | Saturn 1H = late life improvement | High | ✅ | rule_saturn_1h_late_bloom |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_restriction_discipline | Restriction and discipline | element_metal, seven_kill | planet_saturn, house_10 | authority_figure_symbol | superego_function | External limiting force |
| concept_maturation_wisdom | Maturation through hardship | da_yun_late_period | saturn_return, progressed_saturn | elder_guide_symbol | individuation_later_stage | Wisdom from experience |
| concept_persona_mask | Public persona and mask | day_master_expression | house_1, ascendant | mask_symbol | persona_archetype | How one presents to world |
<!-- L2.5_END -->
```

---

## 6. L2.5 Bridge Layer (Mandatory)

> **Purpose**: L2.5 is a **mandatory component** of L1L2 calibration, for expressing factor relationships, evidence chains, and cross-system mappings. Every calibration entry must complete all three L2.5 tables.

### 6.1 L2.5 Work Boundaries

- ✅ **Can Complete**:
  - Factor Relation Layer tables
  - Evidence Chain Layer tables
  - Cross-System Mapping tables (if multi-system content is involved)
- 🚫 **Explicitly Prohibited**:
  - Writing Python code
  - Writing JSON/JSONL/YAML files
  - Writing ConfigRelation/EvidenceChainEntry Pydantic instances

### 6.2 Factor Relation Layer

Express relationships and combination patterns between factors. Each row describes the relationship between two factors.

**Table Structure**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_book_seq | [type enum] | [factor_id_a] | [factor_id_b] | [nature] | [condition or -] | [direction] | [source reference] |

**Relation Type Enumeration**:
- `wuxing_shengke`: Five Elements generating/controlling
- `dizhi_interaction`: Earthly Branch interactions
- `ten_god_relation`: Ten Gods relationship
- `planet_house`: Planet-House relationship
- `planet_aspect`: Planetary aspect relationship
- `dream_symbol_relation`: Dream symbol relationship
- `psych_archetype_relation`: Psychological archetype relationship
- `cross_system`: Cross-system mapping relationship

**Effect Direction**: `beneficial` / `harmful` / `restrictive` / `neutral` / `mixed`

### 6.3 Evidence Chain Layer

Establish complete evidence chains from source text to conclusions. Each row describes one reasoning chain.

**Table Structure**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_book_seq | [L1 source fragment] | [factor_id list] | [reasoning description] | [direction] | [High/Medium/Low] | [✅/❌] | [optional] |

**Confidence Levels**:
- `High`: Source text explicitly states
- `Medium`: Source text implicitly suggests
- `Low`: Requires inference from multiple sources

### 6.4 Cross-System Concept Mapping Layer

Establish common semantic bridges between Chinese destiny arts / Western astrology / Dream studies / Psychology. Each row describes a cross-system common concept.

**Table Structure**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_label | [semantic core] | [factor_id list] | [factor_id list] | [factor_id list] | [factor_id list] | [optional] |

### 6.5 L2.5 Mandatory Requirements

**Every calibration entry must complete**:
- **Factor Relation Layer**: At least 1 factor relation (if no obvious relation, fill in main factor and its core attribute relation)
- **Evidence Chain Layer**: At least 1 evidence chain (trace reasoning path from source text to conclusion)
- **Cross-System Mapping Layer**: Mandatory, at least 1 mapping; if truly no cross-system correspondence, fill main concept with psychological layer mapping

> Reason for mandatory status: L2.5 is essential input for downstream Logic-Agent and Schema extraction; missing L2.5 will break the downstream pipeline.

---

## 7. Relationship with Other Standards

- **Relation to Chinese Template**:
  - `典籍/精校模板_L1L2.md`: Parallel template for Chinese texts (Chinese primary, English secondary)
  - This template: For English texts (English primary, Chinese secondary)

- **Relation to L2.5 Bridge Layer**:
  - L2.5 is **integrated in this template §6**, and is a **mandatory component** of L1L2 calibration
  - Every calibration entry must complete Factor Relation table, Evidence Chain table, and Cross-System Mapping table
  
- **Relation to L3/L4**:
  - This template covers **L1 + L2 + L2.5 + Factor Layer** only
  - L3/L4 content handled by: `典籍/texts/L3L4_Extraction_Template.md`
  
- **Relation to Master Handbook**:
  - `典籍/典籍结构化作业手册.md` serves as navigation document
  - When conflicts arise, **this template is the final standard for English text L1/L2/L2.5 calibration**

- **Relation to Schema Engineering**:
  - After calibration, Schema extraction scripts convert Markdown to structured YAML
  - Schema engineering guide: `典籍/Schema工程说明.md`
  - Data contract: `docs/数据契约_Schema定义规范_v1.md`

---

## 8. Quality Control and Validation

### 8.1 Completeness Checklist

For each entry, verify:
- [ ] Source text preserved exactly
- [ ] Key Term Analysis decomposed exhaustively (no upper limit)
- [ ] English paraphrase clear and complete
- [ ] Complete Chinese Interpretation (Secondary Language) present and aligned with English paraphrase
- [ ] Core points decomposed by semantic unit (no upper limit, one insight per point)
- [ ] Narrative Snippets extracted exhaustively (primary language only, with trigger conditions and logical role `role`)
- [ ] L2 semantic extraction complete
- [ ] Factor table filled with appropriate markers
- [ ] Terms added to glossary

### 8.2 Bilingual Consistency

- Primary language (English) must be complete and thorough
- Secondary language (Chinese) must be complete and accurate, with depth equal to English (no downgrading to brief notes)
- Terms must align with factor ontology
- No word-for-word full-sentence translations – both languages should use localized, natural expression while preserving full meaning

### 8.3 Prohibition Reminders

Never include in this calibration work:
- JSON/JSONL files
- Python rule functions
- Clause/Condition/Rule structures
- Boolean judgments (true/false)
- Factor IDs you create yourself

---

> **Important**: All Western text calibration tasks must use **L1+L2 Calibration Template for Western Texts** as the sole operational standard. This template ensures consistency with the broader bilingual architecture while respecting the unique needs of English-primary texts.
