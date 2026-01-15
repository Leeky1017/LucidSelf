# 语料发布流水线 Acceptance

## 验收命令（最低集合）
- `openspec validate --specs --strict --no-interactive`
- `openspec list --specs`（确认本 spec 的任务进度可见）
- `.venv/bin/python -c 'import json; json.load(open("openspec/specs/corpus-release-pipeline/contract/corpus_release_pipeline_contract.v1.json")); print("OK")'`（契约机器可读校验）
- `bash scripts/gates/gate2_proofreading_and_corpus_release.sh`
- `PYTHONPATH=. .venv/bin/python scripts/corpus_release_pipeline/release.py validate --release-root artifacts/corpus_releases --corpus-release-id $(PYTHONPATH=. .venv/bin/python -c "from backend.core.versioning.ids import resolve_corpus_release_id; print(resolve_corpus_release_id())")`

## 验收指标（最低集合）
- 所有 Requirement 都有至少 1 个 Scenario，且 Scenario 内容非空。
- 关键产物在契约层明确可追溯到 `version_id`（以及 `corpus_release_id`/`engine_id` 如适用）。
- 所属门禁 `Gate-2` 的阻断策略清晰：失败必须阻断晋级/发布/对外开放。
- 对外契约字段清单与拒绝原因枚举存在且为机器可读（JSON 可解析）。
- `tasks.md` 中本 spec 的任务状态与 Evidence 指针一致、可追溯、可复现。

## 必须产物（最低集合）
- `openspec/specs/corpus-release-pipeline/spec.md`
- `openspec/specs/corpus-release-pipeline/requirements.md`
- `openspec/specs/corpus-release-pipeline/tasks.md`
- `openspec/specs/corpus-release-pipeline/design.md`
- `openspec/specs/corpus-release-pipeline/acceptance.md`
- `openspec/specs/corpus-release-pipeline/contract/corpus_release_pipeline_contract.v1.json`
- `openspec/specs/corpus-release-pipeline/data_dictionary.md`
- `openspec/specs/corpus-release-pipeline/observability.md`
- `openspec/specs/corpus-release-pipeline/audit_log.md`
- `openspec/specs/corpus-release-pipeline/security.md`
- `openspec/specs/corpus-release-pipeline/compliance.md`
- `openspec/specs/corpus-release-pipeline/performance.md`
- `openspec/specs/corpus-release-pipeline/cost.md`
- `scripts/corpus_release_pipeline/release.py`
- `scripts/gates/gate2_proofreading_and_corpus_release.sh`

## 通过标准（工程产物）
- 上述命令退出码为 0，且 `openspec validate --specs --strict --no-interactive` 显示本 spec 为通过状态。
- `artifacts/corpus_releases/active_release.json` 为机器可读 JSON，且包含 `active_corpus_release_id`。
- `artifacts/corpus_releases/<corpus_release_id>/release_manifest.json` 与 `hashes.json` 为机器可读 JSON，且 `release.py validate` 校验为 `OK`。
- `release_manifest.json` 中的 `package_digest_sha256` 与 `hashes.json.items[*].sha256` 可用于复现/审计，并能覆盖 Gate-0/1/2 的关键报告与产物。
- `release.py rollback` 会写入 `artifacts/corpus_releases/<corpus_release_id>/rollback_record.json`，并更新 `active_release.json`（可回滚、可追溯）。

## 失败阻断策略（Gate-2）

- 任一验收命令失败 MUST 阻断晋级/发布/对外开放，并要求产出可行动整改项（最小：失败原因 + 关联标识符 + 证据路径）。
