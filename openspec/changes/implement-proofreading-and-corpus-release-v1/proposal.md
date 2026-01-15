# Proposal — Implement Proofreading Workflow QA + Corpus Release Pipeline (v1)

## Why

当前仓库已有 `proofreading-workflow-qa` 与 `corpus-release-pipeline` 两份规格，但工程侧缺少可执行、可审计、可复现的 Gate-2 闭环：
- 校对 QA 缺少“任务队列/状态/抽样/复核/例外”的最小工具链与可落盘产物。
- 语料发布缺少“corpus_release_id 生成/存储/引用/回滚”的工程实现，以及可复现的发布包工件定义（manifest + hashes + reports）。

本 change 的目标是在不引入重型系统的前提下，提供最小可用的脚本工具链与 Gate-2 接入点，使 QA 与发布流程可跑、可审计、可阻断、可回滚。

## Scope

### Proofreading workflow QA
- 定义并实现机器可读的 QA workflow：任务队列、状态机、抽样策略、复核与例外审批记录。
- 产出 QA 报告（JSON + MD），可定位到书/条目（book_id / entry_id / snippet_ids）。
- 报告绑定 `version_id` 与 `corpus_release_id`，可审计与可复现。

### Corpus release pipeline
- 实现 `corpus_release_id` 的生成、存储、引用与回滚策略（以可复现工件为中心）。
- 定义发布包为可复现工件：manifest + hashes + gate reports（资产门禁/ Gate-1 / QA）。
- 提供发布/校验/回滚的一键命令入口（脚本），并作为后续 CI Gate-2 的接入点。

### Acceptance / CI wiring
- 升级两份 spec 的 `acceptance.md`：加入实际脚本命令、工件路径、阈值口径与阻断策略。
- 新增 Gate-2 脚本入口（`scripts/gates`）与 GitHub Actions workflow，并上传 artifacts。
- 更新 `openspec/SPECS_INDEX.md` 对应两行状态并落盘 Evidence。

## Planned Artifacts

- QA workflow：
  - `artifacts/proofreading_qa/qa_queue.json`
  - `artifacts/proofreading_qa/qa_report.json`
  - `artifacts/proofreading_qa/qa_report.md`
  - `scripts/proofreading_qa/run_workflow.py`
  - `data/proofreading_qa/qa_policy.v1.yaml`
- Corpus release：
  - `artifacts/corpus_releases/<corpus_release_id>/release_manifest.json`
  - `artifacts/corpus_releases/<corpus_release_id>/hashes.json`
  - `artifacts/corpus_releases/active_release.json`
  - `scripts/corpus_release_pipeline/release.py`
- Gate-2：
  - `scripts/gates/gate2_proofreading_and_corpus_release.sh`
  - `.github/workflows/gate2-proofreading-and-corpus-release.yml`

## Risks

- **QA 非人工化的现实约束**：CI 环境无法执行真实人工校对；缓解：提供可审计的 workflow 与工件，并将阻断阈值配置化（默认不引入误阻断）。
- **可复现性与路径漂移**：发布包必须可复现；缓解：对纳入发布包的关键产物计算哈希并生成 package digest，校验与回滚以 manifest/hashes 为准。
- **回滚误用**：回滚需要可追责；缓解：生成回滚记录并落盘到 release 工件中。

## Rollback

- Gate-2 可通过策略开关降级为“仅产出报告不阻断”，保留工件与审计记录。
- 回滚通过切换 `active_release.json` 指向实现，保留历史 release 包不删除。

