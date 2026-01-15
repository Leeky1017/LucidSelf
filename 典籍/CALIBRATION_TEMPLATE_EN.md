# Western Text Calibration Card Template (Flat Output / Engine-Consumable)

> Scope: Western texts (primary language English; no full Chinese interpretation required, term alignment only)
>
> Design principle: One calibration card directly outputs Factors / Rule drafts / Narrative snippets / Cross-system mappings / Term alignment (no L1/L2/L3/L4 layers)

---

## Conventions (MUST follow)

- **Output location**: All calibration outputs live under `典籍/calibrated/` (never write back into each book folder).
- **Entry granularity**: One card per minimum viable semantic unit (typically one paragraph / one definition / one symbol entry).
- **IDs & naming**:
  - `card_id` format: `<book_abbr>_<chapter>_<seq>` (example: `innersky_foreword_001`).
  - `book_abbr`: stable, lowercase, `[a-z0-9_]+` (no spaces).
  - `chapter`: stable, lowercase; use a short slug from the book’s TOC, or `ch01`/`part02`.
  - `seq`: start at `001`, continuous per `book_abbr`.
  - `factor_id`: MUST match existing IDs in `典籍/因子本体/`; for new candidates, use `[category]_[semantic]` (lowercase, underscore, English-only).
- **Hard prohibitions**:
  - No L1/L2/L2.5/L3/L4 layering or terminology.
  - No bilingual full-interpretation requirement (term alignment only).
  - No boolean judgement fields like `is_xxx = true/false`.
  - No JSON/JSONL/YAML outputs and no Python code.
  - No “manual review/approval required” steps.

---

## Calibration Card (copy this section per entry)

## A - Entry Metadata

- `card_id`: `<book_abbr>_<chapter>_<seq>`
- `source_anchor`: `<precise chapter/paragraph anchor; prefer path#heading or path:line>`
- `source_text`:
  > `<verbatim source excerpt (do not rewrite)>`
- `priority`: `P0 | P1 | P2 | P3`

Priority rubric: P0=core backbone; P1=mainline; P2=background; P3=index-only (keep section A + `source_anchor`).

---

## B - Factor Extraction

Goal: extract reusable variables as factors, directly referenceable by rules and narrative triggers.

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| `<human-readable label>` | `<official ID if existing; suggested ID if new_candidate>` | `existing \| new_candidate` | `结构 \| 状态 \| 时间 \| 关系 \| 能量` | `bazi \| astro \| tarot \| dream \| psych \| common` | `<e.g., planet/house/aspect/symbol/archetype>` |

---

## C - Rule Drafts

Goal: express if-then structures grounded in the source text (draft-level, traceable).

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_<book_abbr>_<semantic_tag>` | `<human-readable condition; cite factor_label>` | `<human-readable conclusion>` | `事业 \| 财富 \| 关系 \| 健康 \| 心理 \| 运势 \| 吉凶` | `吉 \| 凶 \| 中性 \| 混合` | `高 \| 中 \| 低` | `<short quote from source>` |

---

## D - Narrative Snippets

Goal: short, vivid sentences for Playbook/Narrative generation, with factor-ID trigger expressions.

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_<book_abbr>_<seq>` | `<factor_id expression, e.g., planet_saturn AND house_1>` | `<10-40 words; vivid; standalone>` | `主干 \| 主干依赖 \| 条件分支 \| 例外处理 \| 总结` | `<precise anchor>` |

---

## E - Cross-System Mapping

Goal: map by semantic commonality (many-to-many allowed), and tag with neutral semantics.

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| `<concept/term/mechanism>` | `<factor_id list, comma-separated; optional>` | `<...>` | `<...>` | `<...>` | `<...>` | `<neutral tags, e.g., Resource_Conflict, Emotional_Tension>` |

---

## F - Term Alignment

Goal: align stable technical concepts (not single-character fragments); definitions must be localized (not literal translation); link to factors when possible.

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| `<English term>` | `<中文术语>` | `<English definition>` | `<中文定义（本土化表达）>` | `<if any>` | `existing \| new_candidate` |
