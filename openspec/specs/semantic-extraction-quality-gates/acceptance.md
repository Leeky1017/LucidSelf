# 语义抽取质量门禁 Acceptance

## 验收命令（最低集合）
- `openspec validate --specs --strict --no-interactive`
- `.venv/bin/python -c 'import json; json.load(open("openspec/specs/semantic-extraction-quality-gates/contract/semantic_extraction_quality_gates_contract.v1.json")); print("OK")'`（契约机器可读校验）
- `bash scripts/gates/gate1_cross_book_conflicts_and_quality.sh`
- `PYTHONPATH=. .venv/bin/python scripts/semantic_extraction_quality_gates/run_quality_gate.py --output-dir artifacts/semantic_extraction_quality`

## 验收口径（工程产物）
- `artifacts/semantic_extraction_quality/quality_report.json` 为可解析 JSON，且包含 `version_id`、`corpus_release_id`、`ruleset.ruleset_id` 与 `summary.verdict`。
- `summary.thresholds` 中 `max_total_errors` MUST 为 `pass`（最小阻断集合：ERROR>0 必阻断）。
- 阈值与规则版本以 `data/quality_gates/semantic_extraction_rules.v1.yaml` 为准（可审计、可版本化、可复现）。

## 必须产物（最低集合）
- `data/quality_gates/semantic_extraction_rules.v1.yaml`
- `data/quality_gates/exceptions/semantic_extraction_exceptions.v1.yaml`
- `scripts/semantic_extraction_quality_gates/run_quality_gate.py`
- `scripts/gates/gate1_cross_book_conflicts_and_quality.sh`

## 失败阻断策略（Gate-1）
- 任一验收命令失败 MUST 阻断 Gate-1 晋级，并输出可行动证据（最小：失败原因 + 报告路径）。
