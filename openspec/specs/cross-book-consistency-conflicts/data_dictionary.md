# 跨书一致性与冲突 — 数据字典与字段级约束（规格层）

本文件为 `cross-book-consistency-conflicts` 的关键产物提供字段级约束表与最小完整性语义。禁止写实现细节；仅定义 MUST/SHALL 与可判定约束。

## 1) 冲突记录（ConflictRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| conflict_id | string | 是 | MUST 唯一 | 冲突标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| corpus_release_id | string | 是 | MUST 非空 | 语料发布版本 |
| conflict_type | string | 是 | MUST 非空 | 冲突类型（枚举在规格层固定） |
| subject_key | string | 是 | MUST 非空 | 冲突主题键（规范化后） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 2) 来源引用（SourceCitation）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| citation_id | string | 是 | MUST 唯一 | 引用标识 |
| conflict_id | string | 是 | MUST 非空 | 关联冲突 |
| asset_id | string | 是 | MUST 非空 | 来源资产标识 |
| anchor_id | string | 否 |  | 来源锚点标识（若适用） |
| corpus_release_id | string | 是 | MUST 非空 | 语料发布版本 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 3) 冲突决策（ConflictDecision）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| decision_id | string | 是 | MUST 唯一 | 决策标识 |
| conflict_id | string | 是 | MUST 非空 | 关联冲突 |
| decision | string | 是 | MUST 非空 | 决策枚举（RESOLVED/UNRESOLVED/EXCEPTION 等） |
| rationale | string | 否 |  | 理由摘要（禁止敏感原文） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 4) 例外批准（ExceptionApproval）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| approval_id | string | 是 | MUST 唯一 | 批准标识 |
| conflict_id | string | 是 | MUST 非空 | 关联冲突 |
| approved_by | string | 否 |  | 批准人标识（脱敏/最小化） |
| expires_at | string | 否 | MUST 为 ISO-8601（若存在） | 到期时间 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 5) 冲突报表（ConflictReport）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| report_id | string | 是 | MUST 唯一 | 报表标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| corpus_release_id | string | 是 | MUST 非空 | 语料发布版本 |
| total_conflicts | number | 是 | MUST ≥ 0 | 冲突总数 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 完整性语义（最小）

- `SourceCitation.asset_id` MUST 可解析到 `corpus-governance` 的资产登记；不可解析 MUST 阻断（`VALIDATION_FAILED`）。
- `SourceCitation.anchor_id` 若存在，MUST 可解析到引用/证据协议中的锚点集合（`citations-evidence-protocol`）；不可解析 MUST 阻断（`VALIDATION_FAILED`）。
- `ConflictDecision.conflict_id` / `ExceptionApproval.conflict_id` MUST 可解析到 `ConflictRecord.conflict_id`；不可解析 MUST 阻断（`CONFLICT_NOT_FOUND`）。

