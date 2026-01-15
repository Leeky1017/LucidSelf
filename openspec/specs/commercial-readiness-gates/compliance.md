# 商业化就绪门禁 — 合规（保留/删除/审计证据与期限）

本文件定义 `commercial-readiness-gates` 的合规最小口径：需要保留的证据项、留存期限与删除口径。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 必须保留的证据项（最小）

系统 MUST 能够在合规审计或争议处理时提供以下证据项（最小集合）：

- 就绪清单快照（至少可按 `checklist_id`/`version_id`/Gate 标识定位）
- 审批记录（至少可按 `approval_id`/`version_id`/`approver_role`/`decision` 定位）
- 支持与应急预案快照（至少可按 `plan_id`/`version_id` 定位）
- 发布许可证据（至少可按 `evidence_id`/`version_id` 定位）
- 审计记录导出（至少包含 `audit_id`/`event_type`/`version_id`/`result`）

## 2) 留存期限（最小）

- 审批记录与发布许可证据：MUST 留存 ≥ 7 年（或更长，按更严格法律/合规要求执行）。
- 审计日志：MUST 留存 ≥ 7 年（或更长，按更严格要求执行）。
- 就绪清单与支持/应急预案：MUST 留存 ≥ 365 天，且至少覆盖所有仍可能被引用的 `version_id` 范围。

## 3) 删除与合规审计（MUST）

- 在满足合规保留要求的前提下，系统 SHALL 支持删除/清理策略；任何删除动作 MUST 可审计（形成审计记录并可导出）。
- 对外导出的审计数据 MUST 遵循最小化/脱敏规则（见 `audit_log.md`）。

