# 梦林玄解｜卷三十一（梦征人物部）人工精校记录

- **Change**：`proofread-cn-classics-content-v0-1`
- **目标文件**：`典籍/中文典籍/梦林玄解/编辑/卷之三十一_梦征彝伦部_L1L2.md`
- **范围约束**：仅推进卷三十一；未进入/未修改卷三十。
- **起止条目**：在 `#### 80. 不必吾言` 之后追加 `#### 81.` 至 `#### 111.`，并完成全卷清理与一致性检查。

## 基线与差异

仓库无 `.git`，因此采用“基线备份 vs 当前文件”方式生成 diff：

- **基线文件**：`artifacts/baseline_proofread_mlxj_v31_20251230/卷之三十一_梦征彝伦部_L1L2.md`
- **当前文件**：`典籍/中文典籍/梦林玄解/编辑/卷之三十一_梦征彝伦部_L1L2.md`
- **差异补丁**：`openspec/changes/proofread-cn-classics-content-v0-1/evidence/cn_mlxj_v31_git_diff.patch`

## 精校要点（人工）

- 原文对齐来源：`典籍/中文典籍/梦林玄解/原文/梦林玄解.md`（卷三十一），逐条以 `○/〇` 对齐并补齐 `81–111`。
- 每条均包含并闭合：`<!-- L1_BEGIN -->`、`<!-- L2_BEGIN -->`、`<!-- FACTOR_BEGIN -->`、`<!-- L2.5_BEGIN -->`（及对应 END）。
- `FACTOR` 表：8 列结构；`engine_id` 统一为 `dream-extractor`；“因子ID（必填）”列保持留空。
- 删除残留占位段：`待继续精校（61+）`、`待继续精校（67+）`。
- 清理全卷残留字面量：移除所有 `true/false`（含英文单词子串匹配风险）。

## 校验命令与结果

### 1) 文本约束检查

- `rg -n "true|false" 典籍/中文典籍/梦林玄解/编辑/卷之三十一_梦征彝伦部_L1L2.md` → 无匹配
- `rg -n "待继续精校" 典籍/中文典籍/梦林玄解/编辑/卷之三十一_梦征彝伦部_L1L2.md` → 无匹配
- 条目与块结构校验（脚本校验）：
  - `#### <n>.` 连续编号 `1–111` ✅
  - `L1/L2/FACTOR/L2.5` begin/end 计数均为 `111` ✅

### 2) OpenSpec 严格校验

执行命令：

- `openspec validate proofread-cn-classics-content-v0-1 --strict --no-interactive`

输出：

```
Change 'proofread-cn-classics-content-v0-1' is valid
```

