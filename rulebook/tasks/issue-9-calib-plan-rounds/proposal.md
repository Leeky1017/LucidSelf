# Proposal: issue-9-calib-plan-rounds

## Why
当前“典籍精校”计划需要以可复制、可并行执行的形式长期保存到仓库中，避免计划丢失，并支持多对话框并行推进中英文典籍精校。

## What Changes
- 在仓库 `.cursor/plans/` 新增一份“轮次任务清单”（纯文字，不使用表格）。
- 每条任务只对应一本书一行，包含：任务身份（可作为对话框任务 ID）与可复制执行指令。
- 更新 `.gitignore`：保持 `.cursor/` 默认忽略，但允许追踪 `.cursor/plans/**`。
- 新增 `openspec/_ops/task_runs/ISSUE-9.md` 记录交付证据。

## Impact
- Affected specs: None (documentation/planning artifact only)
- Affected code: `.gitignore`, `.cursor/plans/*`, `openspec/_ops/task_runs/ISSUE-9.md`
- Breaking change: NO
- User benefit: 可追踪、可复用、可并行执行的精校轮次计划

