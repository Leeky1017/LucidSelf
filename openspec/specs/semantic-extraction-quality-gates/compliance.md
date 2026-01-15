# 语义抽取质量门禁 — 合规（保留/删除/审计证据与期限）

本文件定义 `semantic-extraction-quality-gates` 的合规最小口径：需要保留的证据项、留存期限与删除口径。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 必须保留的证据项（最小）

系统 MUST 能够在合规审计时提供以下证据项（最小集合）：

- 质量指标口径定义（至少可按 `metric_id`/`metric_name`/`version_id` 定位）
- 阈值配置（至少可按 `threshold_id`/`metric_name`/`version_id` 定位）
- 门禁运行结果（至少可按 `gate_run_id`/`engine_id`/`version_id`/`result` 定位）
- 失败样本清单（至少可按 `sample_id`/`gate_run_id`/`metric_name` 定位，并可关联引用/证据链）
- 复检记录（至少可按 `recheck_id`/`original_gate_run_id`/`decision` 定位）
- 审计记录导出（至少包含 `audit_id`/`event_type`/`engine_id`/`version_id`/`corpus_release_id`/`result`）

## 2) 留存期限（最小）

- 审计记录：MUST 留存 ≥ 365 天（或更长，按更严格合规要求执行）。
- 门禁运行结果与阈值配置：SHOULD 留存 ≥ 365 天，且至少覆盖所有仍可被引用的 `version_id` 范围。
- 失败样本清单与复检记录：SHOULD 留存 ≥ 90 天；若用于对外争议处理或客户审计，MUST 按更严格要求执行。

## 3) 删除与合规审计（MUST）

- 在满足合规保留要求的前提下，系统 SHALL 支持删除/清理策略；任何删除动作 MUST 可审计（形成审计记录并可导出）。
- 对外导出的审计数据 MUST 遵循最小化/脱敏规则（见 `audit_log.md`）。

