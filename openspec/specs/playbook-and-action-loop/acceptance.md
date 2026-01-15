# Playbook与行动闭环 Acceptance

## 验收命令（最低集合）
- `openspec validate --specs --strict --no-interactive`
- `openspec list --specs`（确认本 spec 的任务进度可见）
- `.venv/bin/python -c 'import json; json.load(open(\"openspec/specs/playbook-and-action-loop/contract/playbook_and_action_loop_contract.v1.json\")); print(\"OK\")'`（契约机器可读校验）

## 验收指标（最低集合）
- 所有 Requirement 都有至少 1 个 Scenario，且 Scenario 内容非空。
- 关键产物在契约层明确可追溯到 `version_id`（以及 `corpus_release_id`/`engine_id` 如适用）。
- 所属门禁 `Gate-2` 的阻断策略清晰：失败必须阻断晋级/发布/对外开放。
- 对外契约字段清单与拒绝原因枚举存在且为机器可读（JSON 可解析）。
- `tasks.md` 中本 spec 的任务状态与 Evidence 指针一致、可追溯、可复现。

## 必须产物（最低集合）
- `openspec/specs/playbook-and-action-loop/spec.md`
- `openspec/specs/playbook-and-action-loop/requirements.md`
- `openspec/specs/playbook-and-action-loop/tasks.md`
- `openspec/specs/playbook-and-action-loop/design.md`
- `openspec/specs/playbook-and-action-loop/acceptance.md`
- `openspec/specs/playbook-and-action-loop/contract/playbook_and_action_loop_contract.v1.json`
- `openspec/specs/playbook-and-action-loop/data_dictionary.md`
- `openspec/specs/playbook-and-action-loop/observability.md`
- `openspec/specs/playbook-and-action-loop/audit_log.md`
- `openspec/specs/playbook-and-action-loop/security.md`
- `openspec/specs/playbook-and-action-loop/compliance.md`
- `openspec/specs/playbook-and-action-loop/performance.md`
- `openspec/specs/playbook-and-action-loop/cost.md`

## 通过标准（规格层）
- 上述命令退出码为 0，且 `openspec validate --specs --strict --no-interactive` 显示本 spec 为通过状态。
- `tasks.md` 的任务可独立验收、可回写状态，并能支撑仪表盘统计。

## 失败阻断策略（Gate-2）

- 任一验收命令失败 MUST 阻断晋级/发布/对外开放，并要求产出可行动整改项（最小：失败原因 + 关联标识符 + 证据路径）。
