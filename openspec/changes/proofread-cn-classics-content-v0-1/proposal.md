# Proposal — Proofread CN Classics Content to Template V0.1

## Why

中文典籍目录下虽已存在大量“编辑/规范化”稿，但仍存在部分卷未补齐 L2 语义提取与因子层标注（尤其是《梦林玄解》若干卷），导致“按模板产出可用于后续工程抽象”的内容资产不完整。

本 change 的目标是：以 `典籍/精校模板_L1L2.md`（V0.1）为唯一规范，对中文典籍（不含已归档的 `记纂渊海`）逐卷补齐/修正到“L1+L2+因子层”完整结构，并按固定顺序一本一本推进。

## Scope

### In scope
- 目录范围：`典籍/中文典籍/**/编辑/*.md`（排除 `典籍/中文典籍/archive/记纂渊海/**`）。
- 工作类型：
  - 补齐缺失的 `<!-- L2_BEGIN --> ... <!-- L2_END -->`（L2 语义提取 + 术语对齐表）。
  - 补齐缺失的 `<!-- FACTOR_BEGIN --> ... <!-- FACTOR_END -->`（因子层表，含 engine_id 列）。
  - 必要的模板引用一致性修正（把“精校依据/模板版本”统一指向 `典籍/精校模板_L1L2.md` 的 `V0.1` 口径）。

### Out of scope
- 不在本 change 内扩展到西方典籍（`典籍/texts/**`）。
- 不在本 change 内新增/修改规则库或生成代码（仅对 Markdown 内容资产做精校补齐）。

## Acceptance (minimum)
- `openspec validate proofread-cn-classics-content-v0-1 --strict --no-interactive`
- `openspec validate --specs --strict --no-interactive`
- 对 scope 内每个目标文件：
  - 必须包含 `<!-- L1_BEGIN -->`（现状已满足）
  - 必须包含 `<!-- L2_BEGIN -->` 与 `<!-- FACTOR_BEGIN -->`

## Risks
- **规模与质量风险**：内容资产量大，逐卷补齐需要严格的顺序与验收口径；缓解：在 `tasks.md` 固化顺序与每卷完成定义，逐卷落盘证据。

## Rollback
- 内容变更为文本资产，不涉及运行时行为；若需回退，仅回退对应 Markdown 文件版本即可。

