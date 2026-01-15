# Design — Proofreading QA + Corpus Release Pipeline (v1)

## Goals
- 以“可复现工件”为中心：发布包必须包含 manifest + hashes + 报告，并可独立校验。
- 以“可审计闭环”为中心：QA 产生队列与决策记录，发布/回滚产生可追责记录。
- 工具链最小化：脚本优先，不引入重型服务依赖。

## QA Workflow Artifacts (v1)

### Storage
- 工作目录（默认）：`artifacts/proofreading_qa/`
- 策略文件：`data/proofreading_qa/qa_policy.v1.yaml`

### Files
- `qa_queue.json`：任务队列（含任务状态、定位信息与可审计字段）
- `qa_report.json`：汇总报告（含阈值判定与 gate verdict）
- `qa_report.md`：人类可读摘要

### Deterministic sampling
- 从 `artifacts/text_normalization_alignment/normalized_entries.jsonl` 构建候选条目集合。
- 抽样方法采用“稳定哈希 + 每书取前 N 条”，确保同输入同输出（默认并行度 1）。

## Corpus Release Artifacts (v1)

### Storage
- 发布根目录（默认）：`artifacts/corpus_releases/`
- 发布包目录：`artifacts/corpus_releases/<corpus_release_id>/`

### Files
- `release_manifest.json`：发布包清单（绑定 `version_id` / `corpus_release_id` / package_digest）
- `hashes.json`：发布包内文件的 sha256/bytes 清单
- `active_release.json`：当前活动 release 指针（用于回滚）

### Included reports (minimum set)
- `artifacts/corpus_governance/corpus_manifest.compiled.json`
- `artifacts/text_normalization_alignment/*`
- `artifacts/cross_book_conflicts/*`
- `artifacts/semantic_extraction_quality/*`
- `artifacts/proofreading_qa/*`

## Rollback Strategy (v1)
- 回滚通过切换 `active_release.json` 指向实现。
- 回滚动作生成记录并写入目标 release 目录（最小：from/to/reason/version_id/corpus_release_id）。

