# 文本归一化与对齐 Acceptance

## 验收命令（最低集合）
- `openspec validate --specs --strict --no-interactive`
- `openspec list --specs`（确认本 spec 的任务进度可见）
- `.venv/bin/python -c 'import json; json.load(open("openspec/specs/text-normalization-alignment/contract/text_normalization_alignment_contract.v1.json")); print("OK")'`（契约机器可读校验）
- `PYTHONPATH=. .venv/bin/python scripts/text_normalization_alignment/run_pipeline.py --output-dir artifacts/text_normalization_alignment`
- `bash scripts/gates/asset_gate_corpus.sh`

## 验收指标（最低集合）
- 所有 Requirement 都有至少 1 个 Scenario，且 Scenario 内容非空。
- 关键产物在契约层明确可追溯到 `version_id`（以及 `corpus_release_id`/`engine_id` 如适用）。
- 所属门禁 `资产门禁` 的阻断策略清晰：失败必须阻断升级/发布/对外开放。
- 对外契约字段清单与拒绝原因枚举存在且为机器可读（JSON 可解析）。
- `tasks.md` 的任务状态与 Evidence 指针一致、可追溯、可复现。

## 必须产物（最低集合）
- `openspec/specs/text-normalization-alignment/spec.md`
- `openspec/specs/text-normalization-alignment/requirements.md`
- `openspec/specs/text-normalization-alignment/tasks.md`
- `openspec/specs/text-normalization-alignment/design.md`
- `openspec/specs/text-normalization-alignment/acceptance.md`
- `openspec/specs/text-normalization-alignment/contract/text_normalization_alignment_contract.v1.json`
- `scripts/text_normalization_alignment/run_pipeline.py`
- `scripts/gates/asset_gate_corpus.sh`

## 通过标准（工程产物）
- 上述命令退出码为 0，且 `openspec validate --specs --strict --no-interactive` 显示为通过状态。
- `artifacts/text_normalization_alignment/normalized_entries.jsonl` 可解析，至少包含 `book_id/node_id/snippet_ids/summary_norm/factor_refs`，且 `normalization_summary.json` 包含 `version_id/corpus_release_id`。
- `artifacts/text_normalization_alignment/alignment_report.json` 包含每条对齐的定位信息：`book_a/node_a/snippet_ids_a` 与 `book_b/node_b/snippet_ids_b`，可追溯到书/段落/条目。

## 失败阻断策略（资产门禁）
- 任一验收命令失败 MUST 阻断语料发布与依赖该资产的用户可见输出，并要求产出可行动整改项（最小：失败原因 + 关联标识符 + 证据路径）。
