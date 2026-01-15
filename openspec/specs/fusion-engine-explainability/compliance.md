# 融合引擎可解释性 — 合规（保留/删除/审计证据与期限）

本文件定义 `fusion-engine-explainability` 的合规最小口径：需要保留的证据项、留存期限与删除口径。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 必须保留的证据项（最小）

系统 MUST 能够在合规审计或安全事件复盘时提供以下证据项（最小集合）：

- 解释记录（至少可按 `explanation_id`/`decision_id`/`engine_id`/`version_id`/`corpus_release_id` 定位）
- 回放输入集（至少可按 `playback_input_set_id`/`engine_id`/`version_id`/`corpus_release_id` 定位）
- 证据对齐引用（至少包含 `alignment_id`/`explanation_id`/`chain_id`，且 `chain_id` 可解析）
- 审计记录导出（至少包含 `audit_id`/`event_type`/`engine_id`/`version_id`/`corpus_release_id`/`result`）

## 2) 留存期限（最小）

- 审计日志：MUST 留存 ≥ 365 天（或更长，按更严格法律/合规要求执行）。
- 解释记录与回放输入集：MUST 留存覆盖所有仍可能被引用的 `version_id/corpus_release_id` 范围，且 MUST ≥ 180 天。
- 证据对齐引用：MUST 留存覆盖所有仍可能被引用的 `chain_id`，且 MUST ≥ 180 天。

## 3) 删除与合规审计（MUST）

- 在满足合规保留要求的前提下，系统 SHALL 支持删除/清理策略；任何删除动作 MUST 可审计（形成审计记录并可导出）。
- 对外导出的审计数据 MUST 遵循最小化/脱敏规则（见 `audit_log.md`）。

