# 语料治理 — 可观测与指标（规格层）

本文件定义 `corpus-governance` 的最小可观测性契约：metrics、logs、traces 与最小 SLO。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) Metrics（名称/标签/单位/聚合口径）

| 指标名 | 类型 | 单位 | 必选标签（最小） | 可选标签 | 聚合口径（最小） |
| --- | --- | --- | --- | --- | --- |
| `ls_corpus_assets_registered_total` | counter | 1 | `result` |  | 资产登记计数 |
| `ls_corpus_license_violations_total` | counter | 1 | `violation_type` |  | 许可违规计数 |
| `ls_corpus_lineage_unresolvable_total` | counter | 1 |  |  | 血缘不可解析计数 |
| `ls_corpus_retirements_total` | counter | 1 | `result` |  | 退役计数 |
| `ls_corpus_audit_records_total` | counter | 1 | `result` |  | 审计记录写入计数 |

## 2) SLO（最小阈值）

- 许可违规拦截：违反许可的使用 MUST 100% 被阻断并审计（资产门禁阻断条件）
- 血缘可解析性：血缘不可解析率异常抬升 MUST 告警并阻断发布（按资产门禁口径）

