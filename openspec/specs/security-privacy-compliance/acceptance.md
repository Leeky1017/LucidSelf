# 安全/隐私/合规 Acceptance

## 验收命令（最低集合）
- `openspec validate --specs --strict --no-interactive`
- `openspec list --specs`（确认本 spec 的任务进度可见）
 - `.venv/bin/python -c 'import json; json.load(open(\"openspec/specs/security-privacy-compliance/contract/security_privacy_compliance_contract.v1.json\")); print(\"OK\")'`（契约机器可读校验）

## 工程验收命令（Gate-0：落地证明）
- `bash scripts/gates/gate0_security_observability.sh`
- `PYTHONPATH=. .venv/bin/pytest backend/tests/gate0_security_observability -q`（等价入口，便于本地快速跑）

## 验收指标（最低集合）
- 所有 Requirement 都有至少 1 个 Scenario，且 Scenario 内容非空。
- 关键产物在契约层明确可追溯到 `version_id`（以及 `corpus_release_id`/`engine_id` 如适用）。
- 所属门禁 `Gate-0` 的阻断策略清晰：失败必须阻断晋级/发布/对外开放。
 - 对外契约字段清单与拒绝原因枚举存在且为机器可读（JSON 可解析）。
 - `tasks.md` 中本 spec 的任务状态与 Evidence 指针一致、可追溯、可复现。

## 工程通过标准（最小）
- 结构化日志具备统一字段（至少 `request_id/trace_id/user_id/org_id/engine_id/version_id`），且 PII/secret 不入日志。
- 关键阻断/拒绝会写入审计记录，并可导出为 NDJSON（每行 JSON + 必填字段齐备）。

## 必须产物（最低集合）
- `openspec/specs/security-privacy-compliance/spec.md`
- `openspec/specs/security-privacy-compliance/requirements.md`
- `openspec/specs/security-privacy-compliance/tasks.md`
- `openspec/specs/security-privacy-compliance/design.md`
- `openspec/specs/security-privacy-compliance/acceptance.md`
 - `openspec/specs/security-privacy-compliance/contract/security_privacy_compliance_contract.v1.json`
 - `openspec/specs/security-privacy-compliance/data_dictionary.md`
 - `openspec/specs/security-privacy-compliance/observability.md`
 - `openspec/specs/security-privacy-compliance/audit_log.md`
 - `openspec/specs/security-privacy-compliance/security.md`
 - `openspec/specs/security-privacy-compliance/compliance.md`
 - `openspec/specs/security-privacy-compliance/performance.md`
 - `openspec/specs/security-privacy-compliance/cost.md`

## 通过标准（规格层）
- 上述命令输出为 `VALID`。
- `tasks.md` 的任务可独立验收、可回写状态，并能支撑仪表盘统计。

## 失败阻断策略（Gate-0）
- 任一验收命令失败 MUST 阻断晋级/发布/对外开放，并要求产出可行动整改项（最小：失败原因 + 关联标识符 + 证据路径）。
