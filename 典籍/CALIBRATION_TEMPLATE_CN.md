# 中文典籍精校卡模板（扁平产出 / 可被引擎直接消费）

> 适用范围：中文典籍（主语言中文；不做英文全文诠释，仅做术语对齐）
>
> 设计原则：一张精校卡 = 直接产出因子 / 规则草案 / 叙事素材 / 跨体系映射 / 术语对齐（无 L1/L2/L3/L4 分层）

---

## 使用约定（必须遵守）

- **产出位置**：精校卡与产物统一放在 `典籍/calibrated/`（不得回写到各典籍书籍目录）。
- **条目粒度**：以“最小可行语义单元”为一卡（通常对应原文一个段落/一句歌诀/一条定义/一条梦象条目）。
- **ID 与命名**：
  - `card_id` 格式：`<book_abbr>_<chapter>_<seq>`（示例：`dts_tongtian_001`）。
  - `book_abbr`：稳定、全小写、英文/数字/下划线（禁止中文/拼音大写/空格）。
  - `chapter`：稳定、全小写；可用目录标题的英文化短名或 `ch01`/`vol02`。
  - `seq`：三位起（`001`），同一 `book_abbr` 内连续编号即可。
  - `factor_id`：必须与 `典籍/因子本体/` 中的既有 ID 精确一致；新候选用 `new_candidate`，并用 `[category]_[semantic]` 规范建议 ID（全小写、下划线、纯英文）。
- **禁止项（硬性）**：
  - 禁止 L1/L2/L2.5/L3/L4 分层结构与术语。
  - 禁止要求双语全文对等诠释（仅术语对齐）。
  - 禁止 `is_xxx = true/false` 这类布尔判定字段。
  - 禁止要求生成 JSON/JSONL/YAML 文件或任何 Python 代码。
  - 禁止任何“需要人工审核/审批/复核后才算完成”的环节描述。

---

## 精校卡（复制本节作为一张卡）

## A - 条目元信息（Entry Metadata）

- `card_id`: `<book_abbr>_<chapter>_<seq>`
- `source_anchor`: `<精确到章节/段落；推荐用 路径#标题 或 路径:行号>`
- `source_text`:
  > `<原文内容：保持原貌，不改字；如需断句/标点，仅在原文文件中完成后再引用此处>`
- `priority`: `P0 | P1 | P2 | P3`

> 优先级口径：P0=核心骨架；P1=主干扩展；P2=背景补足；P3=仅保留索引（此卡仍需保留 A 段与 source_anchor）。

---

## B - 因子提取（Factor Extraction）

> 目标：把本条原文能稳定复用的“变量”抽成因子，供规则与叙事触发直接引用。

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| `<人话因子标签>` | `<existing 填正式ID；new_candidate 填建议ID>` | `existing \| new_candidate` | `结构 \| 状态 \| 时间 \| 关系 \| 能量` | `bazi \| astro \| tarot \| dream \| psych \| common` | `<如 日主/用神/十神/卦象/梦象/原型 等>` |

---

## C - 规则草案（Rule Drafts）

> 目标：把原文中可推导的 if-then 结构写成“可追溯的草案规则”。  
> 规则条件用人话描述并**引用 B 段的 factor_label**；叙事触发可直接用因子表达式（见 D 段）。

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_<book_abbr>_<semantic_tag>` | `<人话条件：引用 factor_label>` | `<人话结论>` | `事业 \| 财富 \| 关系 \| 健康 \| 心理 \| 运势 \| 吉凶` | `吉 \| 凶 \| 中性 \| 混合` | `高 \| 中 \| 低` | `<原文证据片段（短引）>` |

---

## D - 叙事素材（Narrative Snippets）

> 目标：可用于 Playbook / Narrative 生成的“精炼句子”，并能用因子表达式触发。

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_<book_abbr>_<seq>` | `<使用 factor_id 表达式，如 day_master_jia AND season_spring>` | `<10-40字；有画面感；可独立理解>` | `主干 \| 主干依赖 \| 条件分支 \| 例外处理 \| 总结` | `<精确到原文章节/段落>` |

---

## E - 跨体系映射（Cross-System Mapping）

> 目标：用“语义共通性”把本书概念挂到八字/占星/塔罗/梦学/心理学，并给出中立语义标签（允许多对多）。

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| `<本书概念/术语/机制>` | `<factor_id 列表，逗号分隔；无则留空>` | `<...>` | `<...>` | `<...>` | `<...>` | `<中立标签，如 Resource_Conflict, Authority_Challenge>` |

---

## F - 术语对齐（Term Alignment）

> 目标：只对齐稳定技术概念（非单字碎片），定义要本土化优化；并尽量挂接因子。

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| `<中文术语>` | `<英文术语>` | `<中文定义>` | `<英文定义（非直译，面向英文语境）>` | `<如有则填>` | `existing \| new_candidate` |
