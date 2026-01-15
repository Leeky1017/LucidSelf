# 语料治理 Acceptance

## 验收命令（最低集合）
- `openspec validate --specs --strict --no-interactive`
- `openspec list --specs`（确认本 spec 的任务进度可见）
- `.venv/bin/python -c 'import json; json.load(open("openspec/specs/corpus-governance/contract/corpus_governance_contract.v1.json")); print("OK")'`（契约机器可读校验）
- `bash scripts/gates/asset_gate_corpus.sh`
- `PYTHONPATH=. .venv/bin/python scripts/corpus_governance/generate_manifest.py --input data/governance/corpus_manifest.v1.yaml --output artifacts/corpus_governance/corpus_manifest.compiled.json`
- `PYTHONPATH=. .venv/bin/python scripts/corpus_governance/validate_manifest.py artifacts/corpus_governance/corpus_manifest.compiled.json --strict`

## 验收指标（最低集合）
- 所有 Requirement 都有至少 1 个 Scenario，且 Scenario 内容非空。
- 关键产物在契约层明确可追溯到 `version_id`（以及 `corpus_release_id`/`engine_id` 如适用）。
- 所属门禁 `资产门禁` 的阻断策略清晰：失败必须阻断升级/发布/对外开放。
- 对外契约字段清单与拒绝原因枚举存在且为机器可读（JSON 可解析）。
- `tasks.md` 的任务状态与 Evidence 指针一致、可追溯、可复现。

## 必须产物（最低集合）
- `openspec/specs/corpus-governance/spec.md`
- `openspec/specs/corpus-governance/requirements.md`
- `openspec/specs/corpus-governance/tasks.md`
- `openspec/specs/corpus-governance/design.md`
- `openspec/specs/corpus-governance/acceptance.md`
- `openspec/specs/corpus-governance/contract/corpus_governance_contract.v1.json`
- `data/governance/corpus_manifest.v1.yaml`
- `scripts/corpus_governance/generate_manifest.py`
- `scripts/corpus_governance/validate_manifest.py`
- `scripts/gates/asset_gate_corpus.sh`

## 通过标准（工程产物）
- 上述命令退出码为 0，且 `openspec validate --specs --strict --no-interactive` 显示为通过状态。
- `artifacts/corpus_governance/corpus_manifest.compiled.json` 为机器可读 JSON，包含 `version_id`/`corpus_release_id`，且每个 asset 的 `path` 可解析且存在。
- manifest 每个 asset 都可追溯到 `license_id`，且 `derived_from` 引用可解析。

## 失败阻断策略（资产门禁）
- 任一验收命令失败 MUST 阻断语料发布与依赖该资产的下游升级，并要求产出可行动整改项（最小：失败原因 + 关联标识符 + 证据路径）。
