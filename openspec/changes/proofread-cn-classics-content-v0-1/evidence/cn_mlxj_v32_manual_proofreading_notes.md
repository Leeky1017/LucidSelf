# 证据记录：梦林玄解 卷之三十二（梦征形貌政事部）连续精校（L1+L2+因子层）

- 任务：`openspec/changes/proofread-cn-classics-content-v0-1/tasks.md`（Phase A）
- 卷文件：`典籍/中文典籍/梦林玄解/编辑/卷之三十二_梦征形貌政事部_L1L2.md`
- 原文来源：`典籍/中文典籍/梦林玄解/原文/梦林玄解.md`
- 证据时间：2025-12-31

## 基线与 diff

> 仓库当前无 `.git`，因此使用“基线备份 vs 当前文件”的 unified diff 作为证据。

- 基线备份：`artifacts/baseline_proofread_mlxj_v32_20251231/卷之三十二_梦征形貌政事部_L1L2.md`
- diff patch：`openspec/changes/proofread-cn-classics-content-v0-1/evidence/cn_mlxj_v32_git_diff.patch`

## 卷内一致性检查（rg/结构/编号）

### 1) 禁用项（必须 0 命中）

```bash
rg -n "true|false" "典籍/中文典籍/梦林玄解/编辑/卷之三十二_梦征形貌政事部_L1L2.md"
rg -n "待继续精校" "典籍/中文典籍/梦林玄解/编辑/卷之三十二_梦征形貌政事部_L1L2.md"
```

- 结果：均为 0 命中（无输出）。

### 2) 结构块计数（BEGIN/END 必须成对，且数量=条目数）

```bash
rg -c "<!-- L1_BEGIN -->"   "典籍/中文典籍/梦林玄解/编辑/卷之三十二_梦征形貌政事部_L1L2.md"
rg -c "<!-- L1_END -->"     "典籍/中文典籍/梦林玄解/编辑/卷之三十二_梦征形貌政事部_L1L2.md"
rg -c "<!-- L2_BEGIN -->"   "典籍/中文典籍/梦林玄解/编辑/卷之三十二_梦征形貌政事部_L1L2.md"
rg -c "<!-- L2_END -->"     "典籍/中文典籍/梦林玄解/编辑/卷之三十二_梦征形貌政事部_L1L2.md"
rg -c "<!-- FACTOR_BEGIN -->" "典籍/中文典籍/梦林玄解/编辑/卷之三十二_梦征形貌政事部_L1L2.md"
rg -c "<!-- FACTOR_END -->"   "典籍/中文典籍/梦林玄解/编辑/卷之三十二_梦征形貌政事部_L1L2.md"
rg -c "<!-- L2\\.5_BEGIN -->" "典籍/中文典籍/梦林玄解/编辑/卷之三十二_梦征形貌政事部_L1L2.md"
rg -c "<!-- L2\\.5_END -->"   "典籍/中文典籍/梦林玄解/编辑/卷之三十二_梦征形貌政事部_L1L2.md"
```

输出：

```
94
94
94
94
94
94
94
94
```

### 3) 条目编号连续性

- 本卷条目 `#### 1.` 至 `#### 94.` 连续，无缺号、无重复。
- `source_ref` 统一为 `卷三十二#<n>`（随条目编号变化）。

## OpenSpec validate（严格模式）

```bash
cd work/LucidSelf
openspec validate proofread-cn-classics-content-v0-1 --strict --no-interactive
```

输出：

```
Change 'proofread-cn-classics-content-v0-1' is valid
```

