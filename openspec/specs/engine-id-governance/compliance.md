# 引擎ID治理 — 合规（保留/删除/审计证据与期限）

本文件定义 `engine-id-governance` 的合规最小口径：需要保留的证据项、留存期限与删除口径。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 必须保留的证据项（最小）

系统 MUST 能够在合规审计时提供以下证据项（最小集合）：

- 引擎注册表的版本化快照（至少可按 `version_id` 定位）
- 生命周期事件记录（至少可按 `event_id`/`engine_id`/`version_id` 定位）
- 弃用/替代关系记录（至少可按 `deprecated_engine_id`/`effective_version_id` 定位）
- 审计记录导出（至少包含 `audit_id`/`event_id`/`engine_id`/`version_id`/`result`）

## 2) 留存期限（最小）

- 审计记录：MUST 留存 ≥ 365 天（或更长，按更严格合规要求执行）。
- 生命周期事件：MUST 留存 ≥ 365 天；对 `deprecated` 相关事件 SHOULD 覆盖至少两个版本周期（若存在版本周期定义）。
- 引擎注册表快照：SHOULD 留存 ≥ 365 天，且至少覆盖所有仍可被引用的 `version_id` 范围。

## 3) 删除与合规审计（MUST）

- 在满足合规保留要求的前提下，系统 SHALL 支持删除/清理策略；任何删除动作 MUST 可审计（形成生命周期事件与审计记录）。
- 对外导出的审计数据 MUST 遵循最小化/脱敏规则（见 `audit_log.md`）。

