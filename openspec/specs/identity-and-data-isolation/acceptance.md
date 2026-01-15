# 身份与数据隔离 Acceptance

## 验收命令（最低集合）
- `openspec validate --specs --strict --no-interactive`
- `bash scripts/gates/gate0_engine_id_identity.sh`（Gate-0 一键验收入口：包含本 spec 的工程验收集合）
- `PYTHONPATH=. .venv/bin/pytest backend/tests/gate0/test_identity_and_data_isolation.py -q`（本 spec 工程验收：鉴权身份派生 + 跨租户阻断）
- `openspec list --specs`（确认本 spec 的任务进度可见）
 - `.venv/bin/python -c 'import json; json.load(open(\"openspec/specs/identity-and-data-isolation/contract/identity_and_data_isolation_contract.v1.json\")); print(\"OK\")'`（契约机器可读校验）

## 验收指标（最低集合）
- 所有 Requirement 都有至少 1 个 Scenario，且 Scenario 内容非空。
- 关键产物在契约层明确可追溯到 `version_id`（以及 `corpus_release_id`/`engine_id` 如适用）。
- 所属门禁 `Gate-0` 的阻断策略清晰：失败必须阻断晋级/发布/对外开放。
 - 对外契约字段清单与拒绝原因枚举存在且为机器可读（JSON 可解析）。
 - `tasks.md` 中本 spec 的任务状态与 Evidence 指针一致、可追溯、可复现。

## 必须产物（最低集合）
- `openspec/specs/identity-and-data-isolation/spec.md`
- `openspec/specs/identity-and-data-isolation/requirements.md`
- `openspec/specs/identity-and-data-isolation/tasks.md`
- `openspec/specs/identity-and-data-isolation/design.md`
- `openspec/specs/identity-and-data-isolation/acceptance.md`
 - `openspec/specs/identity-and-data-isolation/contract/identity_and_data_isolation_contract.v1.json`
 - `openspec/specs/identity-and-data-isolation/data_dictionary.md`
 - `openspec/specs/identity-and-data-isolation/observability.md`
 - `openspec/specs/identity-and-data-isolation/audit_log.md`
 - `openspec/specs/identity-and-data-isolation/security.md`
 - `openspec/specs/identity-and-data-isolation/compliance.md`
 - `openspec/specs/identity-and-data-isolation/performance.md`
 - `openspec/specs/identity-and-data-isolation/cost.md`

## 通过标准（规格层）
- 上述命令输出为 `VALID`。
- `tasks.md` 的任务可独立验收、可回写状态，并能支撑仪表盘统计。

## 失败阻断策略（Gate-0）
- 任一验收命令失败 MUST 阻断晋级/发布/对外开放，并要求产出可行动整改项（最小：失败原因 + 关联标识符 + 证据路径）。
