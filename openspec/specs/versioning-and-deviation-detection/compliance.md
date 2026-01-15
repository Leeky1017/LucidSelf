# 版本化与偏差检测 — 合规（保留/删除/审计证据与期限）

本文件定义 `versioning-and-deviation-detection` 的合规最小口径：需要保留的证据项、留存期限与删除口径。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 必须保留的证据项（最小）

系统 MUST 能够在合规审计时提供以下证据项（最小集合）：

- 版本清单（可按 `version_id` 定位）
- 兼容性声明（可按 `from_version_id/to_version_id` 定位）
- 偏差报告（可按 `version_id/baseline_version_id` 定位）
- 阻断记录（可按 `gate/version_id` 定位）
- 审计记录导出（至少包含 `audit_id`/`created_at`/`event_type`/`result`）

## 2) 留存期限（最小）

- 审计记录：MUST 留存 ≥ 365 天（或更长，按更严格合规要求执行）。
- 版本清单/兼容性声明/偏差报告/阻断记录：SHOULD 留存 ≥ 365 天，且至少覆盖所有仍可被引用的 `version_id` 范围。

## 3) 删除与合规审计（MUST）

- 在满足合规保留要求的前提下，系统 SHALL 支持删除/清理策略；任何清理动作 MUST 可审计。

