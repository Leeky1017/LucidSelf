# 语料发布流水线 — 成本目标与预算阈值（规格层）

本文件定义 `corpus-release-pipeline` 的成本目标、预算阈值与告警策略。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 成本维度（最小）

- **存储**：发布阶段记录、校验报告、release artifacts、回滚记录、审计记录与导出包
- **计算**：语料处理、抽取/QA 校验与漂移检测
- **可观测**：结构化日志与审计导出带来的 IO/存储成本

## 2) 预算阈值（最小）

以下阈值用于早期商业化基线（Gate-2）；后续可按真实负载修订，但口径必须可执行、可判定：

- 流水线阶段运行量：日均 `ls_corpus_release_pipeline_runs_total` SHOULD ≤ 100,000
- 校验报告量：日均 `ls_corpus_release_pipeline_validation_reports_total` SHOULD ≤ 100,000
- 单次审计导出体量：单次导出 SHOULD ≤ 1GB（超过则必须分片/分页导出；策略实现可选）
- 单个 release artifacts 摘要体量：序列化后的 `ReleaseArtifact` SHOULD ≤ 64KB（超过则必须拒绝或降级）

## 3) 告警策略（最小）

- 超过预算阈值（连续 3 个评估窗口）MUST 告警，并形成可审计事件。
- 告警 MUST 可关联到：时间窗口、影响面（阶段/校验/回滚/导出）、拒绝原因/阻断类型（若适用）。

