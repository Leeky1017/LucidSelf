# 梦林玄解｜卷三十（梦征天象部）人工精校记录

- **Change**：`proofread-cn-classics-content-v0-1`
- **目标文件**：`典籍/中文典籍/梦林玄解/编辑/卷之三十_梦征天象部_L1L2.md`
- **范围约束**：仅推进卷三十；未进入/未修改卷三十二、卷三十三、卷三十四及清单外卷。
- **起止条目**：补齐并清理全卷条目 `#### 1.` 至 `#### 118.`，并完成全卷一致性检查。

## 基线与差异

仓库无 `.git`，因此采用“基线备份 vs 当前文件”方式生成 diff：

- **基线文件**：`artifacts/baseline_proofread_mlxj_v30_20251230/卷之三十_梦征天象部_L1L2.md`
- **当前文件**：`典籍/中文典籍/梦林玄解/编辑/卷之三十_梦征天象部_L1L2.md`
- **差异补丁**：`openspec/changes/proofread-cn-classics-content-v0-1/evidence/cn_mlxj_v30_git_diff.patch`

## 精校要点（人工）

- 原文对齐来源：`典籍/中文典籍/梦林玄解/原文/梦林玄解.md`（卷三十），逐条以 `○/〇/口` 对齐补齐 `1–118`。
- 每条均包含并闭合：`<!-- L1_BEGIN -->`、`<!-- L2_BEGIN -->`、`<!-- FACTOR_BEGIN -->`、`<!-- L2.5_BEGIN -->`（及对应 END）。
- `FACTOR` 表：8 列结构；`engine_id` 统一为 `dream-extractor`；“因子ID（必填）”列保持留空。
- 清理全卷残留字面量：确保无 `true/false` 与 `待继续精校`。

## 校验命令与结果

### 1) 文本约束检查

- `rg -n "true|false" 典籍/中文典籍/梦林玄解/编辑/卷之三十_梦征天象部_L1L2.md` → 无匹配
- `rg -n "待继续精校" 典籍/中文典籍/梦林玄解/编辑/卷之三十_梦征天象部_L1L2.md` → 无匹配
- 条目与块结构校验（脚本校验）：
  - `#### <n>.` 连续编号 `1–118` ✅
  - `L1/L2/FACTOR/L2.5` begin/end 计数均为 `118` ✅

### 2) OpenSpec 严格校验

执行命令：

- `openspec validate proofread-cn-classics-content-v0-1 --strict --no-interactive`

输出：

```
Change 'proofread-cn-classics-content-v0-1' is valid
```

