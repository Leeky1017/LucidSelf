# Golden Set与回归评测 — 合规（保留/删除/审计证据与期限）

本文件定义 `golden-sets-and-regression` 的合规最小口径：需要保留的证据项、留存期限与删除口径。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 必须保留的证据项（最小）

系统 MUST 能够在合规审计时提供以下证据项（最小集合）：

- golden set 清单（至少可按 `golden_set_id`/`version_id` 定位）
- 覆盖率报告（至少可按 `coverage_report_id`/`golden_set_id`/`version_id` 定位）
- 回归阈值定义（至少可按 `threshold_id`/`golden_set_id`/`version_id` 定位）
- 回归运行结果（至少可按 `run_id`/`golden_set_id`/`version_id` 定位）
- 漂移告警记录（至少可按 `alert_id`/`golden_set_id`/`version_id` 定位）
- 审计记录导出（至少包含 `audit_id`/`event_type`/`version_id`/`corpus_release_id`/`engine_id`/`result`）

## 2) 留存期限（最小）

- 审计记录：MUST 留存 ≥ 365 天（或更长，按更严格合规要求执行）。
- 评测产物（清单/报告/阈值/结果/告警）：SHOULD 留存 ≥ 365 天，且至少覆盖所有仍可被引用的 `version_id` 范围。
- 审计导出包：SHOULD 留存 ≥ 90 天；若导出用于对外争议处理或客户审计，MUST 按更严格要求执行。

## 3) 删除与合规审计（MUST）

- 在满足合规保留要求的前提下，系统 SHALL 支持删除/清理策略；任何删除动作 MUST 可审计（形成审计记录并可导出）。
- 对外导出的审计数据 MUST 遵循最小化/脱敏规则（见 `audit_log.md`）。

