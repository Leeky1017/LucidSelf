# 语义抽取质量门禁 — 成本目标与预算阈值（规格层）

本文件定义 `semantic-extraction-quality-gates` 的成本目标、预算阈值与告警策略。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 成本维度（最小）

- **存储**：门禁运行结果、失败样本清单、复检记录、审计记录与导出包
- **计算**：门禁评估、阈值比较、引用解析与偏差检测
- **可观测**：结构化日志与审计导出带来的 IO/存储成本

## 2) 预算阈值（最小）

以下阈值用于早期商业化基线（Gate-1）；后续可按真实负载修订，但口径必须可执行、可判定：

- 门禁评估量：日均 `ls_semantic_extraction_quality_gate_requests_total` SHOULD ≤ 5,000,000
- 失败样本写入量：日均 `ls_semantic_extraction_quality_gate_failure_samples_total` SHOULD ≤ 500,000
- 单次审计导出体量：单次导出 SHOULD ≤ 1GB（超过则必须分片/分页导出；策略实现可选）
- 单次门禁运行结果体量：序列化后的 `QualityGateRunResult`（含 failures）SHOULD ≤ 256KB（超过则必须拒绝或降级）

## 3) 告警策略（最小）

- 超过预算阈值（连续 3 个评估窗口）MUST 告警，并形成可审计事件。
- 告警 MUST 可关联到：时间窗口、影响面（评估/写入/导出）、拒绝原因/阻断类型（若适用）。

