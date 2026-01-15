# bootability-and-regression-baseline — Done Report

## 完成范围

- `openspec/specs/bootability-and-regression-baseline/tasks.md` 全部任务已完成并回写为 `[x]`，每条任务行已追加 Evidence 指针。
- 补齐并固化本 spec 的契约产物与 Gate-1 可执行验收口径（规格层）。

## 验收命令（全部可复现）

- `openspec validate --specs --strict --no-interactive`
- `openspec list --specs`
- `.venv/bin/python -c 'import json; json.load(open("openspec/specs/bootability-and-regression-baseline/contract/bootability_and_regression_baseline_contract.v1.json")); print("OK")'`

## 关键输出路径

- 规格产物：
  - `openspec/specs/bootability-and-regression-baseline/contract/bootability_and_regression_baseline_contract.v1.json`
  - `openspec/specs/bootability-and-regression-baseline/data_dictionary.md`
  - `openspec/specs/bootability-and-regression-baseline/observability.md`
  - `openspec/specs/bootability-and-regression-baseline/audit_log.md`
  - `openspec/specs/bootability-and-regression-baseline/security.md`
  - `openspec/specs/bootability-and-regression-baseline/compliance.md`
  - `openspec/specs/bootability-and-regression-baseline/performance.md`
  - `openspec/specs/bootability-and-regression-baseline/cost.md`
  - `openspec/specs/bootability-and-regression-baseline/acceptance.md`
  - `openspec/specs/bootability-and-regression-baseline/design.md`
- 运行记录与证据：
  - `openspec/_ops/spec_runs/bootability-and-regression-baseline/evidence/`（逐任务验收输出）
  - `openspec/_ops/spec_runs/bootability-and-regression-baseline/02_regression_after_group_*.txt`（逐任务组最小回归）

## 风险与未覆盖项（不属于本 spec 任务范围）

- 本轮交付聚焦于规格层契约/门禁/证据产物；并未对回归套件的真实执行集与阈值落地做系统实现（需由后续相关 specs 或变更任务承接）。

