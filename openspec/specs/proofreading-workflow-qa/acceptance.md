# 校对工作流与QA Acceptance

## 验收命令（最低集合）
- `openspec validate --specs --strict --no-interactive`
- `openspec list --specs`（确认本 spec 的任务进度可见）
- `.venv/bin/python -c 'import json; json.load(open("openspec/specs/proofreading-workflow-qa/contract/proofreading_workflow_qa_contract.v1.json")); print("OK")'`（契约机器可读校验）
- `bash scripts/gates/asset_gate_corpus.sh`（确保归一化产物存在，作为 QA 全量输入）
- `PYTHONPATH=. .venv/bin/python scripts/proofreading_qa/run_workflow.py run --policy data/proofreading_qa/qa_policy.v2.zh_full.yaml --output-dir artifacts/proofreading_qa`
- `PYTHONPATH=. .venv/bin/python -c 'import json; r=json.load(open("artifacts/proofreading_qa/qa_report.json")); print("verdict", r["summary"]["verdict"]); print("tasks_total", r["summary"]["tasks_total"])'`
- `bash scripts/gates/gate2_proofreading_and_corpus_release.sh`（Gate-2 集成入口：QA+发布流水线）

## 验收指标（最低集合）
- 所有 Requirement 都有至少 1 个 Scenario，且 Scenario 内容非空。
- 关键产物在契约层明确可追溯到 `version_id`（以及 `corpus_release_id`/`engine_id` 如适用）。
- 所属门禁 `资产门禁` 的阻断策略清晰：失败必须阻断晋级/发布/对外开放。
- 对外契约字段清单与拒绝原因枚举存在且为机器可读（JSON 可解析）。
- `tasks.md` 中本 spec 的任务状态与 Evidence 指针一致、可追溯、可复现。

## 必须产物（最低集合）
- `openspec/specs/proofreading-workflow-qa/spec.md`
- `openspec/specs/proofreading-workflow-qa/requirements.md`
- `openspec/specs/proofreading-workflow-qa/tasks.md`
- `openspec/specs/proofreading-workflow-qa/design.md`
- `openspec/specs/proofreading-workflow-qa/acceptance.md`
- `openspec/specs/proofreading-workflow-qa/contract/proofreading_workflow_qa_contract.v1.json`
- `openspec/specs/proofreading-workflow-qa/data_dictionary.md`
- `openspec/specs/proofreading-workflow-qa/observability.md`
- `openspec/specs/proofreading-workflow-qa/audit_log.md`
- `openspec/specs/proofreading-workflow-qa/security.md`
- `openspec/specs/proofreading-workflow-qa/compliance.md`
- `openspec/specs/proofreading-workflow-qa/performance.md`
- `openspec/specs/proofreading-workflow-qa/cost.md`
- `data/proofreading_qa/qa_policy.v2.zh_full.yaml`
- `scripts/proofreading_qa/run_workflow.py`
- `scripts/gates/gate2_proofreading_and_corpus_release.sh`

## 通过标准（工程产物）
- 上述命令退出码为 0，且 `openspec validate --specs --strict --no-interactive` 显示本 spec 为通过状态。
- `artifacts/proofreading_qa/qa_queue.json` 与 `artifacts/proofreading_qa/qa_report.json` 均为机器可读 JSON。
- `artifacts/proofreading_qa/qa_report.json` 中 `summary.verdict` 为 `pass`。
- `artifacts/proofreading_qa/qa_queue.json` 的每个任务至少包含 `task_id`/`book_id`/`entry_id`/`source_ref`（可定位到书/段落/条目）。
- `qa_report.json` 与 `qa_queue.json` 均包含一致的 `version_id`/`corpus_release_id`/`policy_id`，用于审计与复现。

## 失败阻断策略（资产门禁）

- 任一验收命令失败 MUST 阻断资产晋级/发布/被用于用户可见输出，并要求产出可行动整改项（最小：失败原因 + 关联标识符 + 证据路径）。
