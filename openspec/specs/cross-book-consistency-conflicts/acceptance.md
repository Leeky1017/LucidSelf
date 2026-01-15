# 跨书一致性与冲突 Acceptance

## 验收命令（最低集合）
- `openspec validate --specs --strict --no-interactive`
- `.venv/bin/python -c 'import json; json.load(open("openspec/specs/cross-book-consistency-conflicts/contract/cross_book_consistency_conflicts_contract.v1.json")); print("OK")'`（契约机器可读校验）
- `bash scripts/gates/gate1_cross_book_conflicts_and_quality.sh`
- `PYTHONPATH=. .venv/bin/python scripts/cross_book_consistency_conflicts/run_conflict_gate.py --output-dir artifacts/cross_book_conflicts`

## 验收口径（工程产物）
- `artifacts/cross_book_conflicts/conflict_report.json` 为可解析 JSON，且包含 `version_id`、`corpus_release_id`、`policy.policy_id` 与 `summary.verdict`。
- `summary.thresholds[*].status` 全部为 `pass`；任一为 `fail` MUST 导致命令退出码非 0（可阻断）。
- `artifacts/cross_book_conflicts/exceptions_applied.json` 记录被应用的例外（即使为空列表也必须存在且可解析）。
- 阈值口径以 `data/knowledge_graph/conflict_gate_policy.v1.yaml` 为准（可审计、可版本化、可复现）。

## 必须产物（最低集合）
- `data/knowledge_graph/conflict_gate_policy.v1.yaml`
- `data/knowledge_graph/exceptions/conflict_exceptions.v1.yaml`
- `scripts/cross_book_consistency_conflicts/run_conflict_gate.py`
- `scripts/gates/gate1_cross_book_conflicts_and_quality.sh`

## 失败阻断策略（Gate-1）
- 任一验收命令失败 MUST 阻断 Gate-1 晋级，并输出可行动证据（最小：失败原因 + 报告路径）。
