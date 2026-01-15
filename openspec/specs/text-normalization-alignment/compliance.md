# 文本归一化与对齐 — 合规（保留/删除/审计证据与期限）

本文件定义 `text-normalization-alignment` 的合规最小口径：需要保留的证据项、留存期限与删除口径。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 必须保留的证据项（最小）

系统 MUST 能够在合规审计时提供以下证据项（最小集合）：

- 归一化规则集版本化快照（至少可按 `rule_set_id`/`version_id` 定位）
- 对齐映射版本化快照（至少可按 `mapping_id`/`version_id` 定位）
- 变换审计记录导出（至少包含 `audit_id`/`event_type`/`corpus_release_id`/`version_id`/`result`）
- 覆盖率报告与例外清单（至少可按 `coverage_report_id`/`exception_list_id`/`version_id` 定位）

## 2) 留存期限（最小）

- 审计记录：MUST 留存 ≥ 365 天（或更长，按更严格合规要求执行）。
- 规则集/映射/覆盖率/例外清单：SHOULD 留存 ≥ 365 天，且至少覆盖所有仍可被引用的 `version_id` 范围。
- 审计导出包：SHOULD 留存 ≥ 90 天；若导出用于对外争议处理或客户审计，MUST 按更严格要求执行。

## 3) 删除与合规审计（MUST）

- 在满足合规保留要求的前提下，系统 SHALL 支持删除/清理策略；任何删除动作 MUST 可审计（形成审计记录并可导出）。
- 对外导出的审计数据 MUST 遵循最小化/脱敏规则（见 `audit_log.md`）。

