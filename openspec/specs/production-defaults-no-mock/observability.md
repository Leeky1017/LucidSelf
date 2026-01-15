# 生产默认值（禁止Mock）— 可观测与指标（规格层）

本文件定义 `production-defaults-no-mock` 的最小可观测性契约：metrics、logs、traces 与最小 SLO。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) Metrics（名称/标签/单位/聚合口径）

| 指标名 | 类型 | 单位 | 必选标签（最小） | 可选标签 | 聚合口径（最小） |
| --- | --- | --- | --- | --- | --- |
| `ls_prod_defaults_config_checks_total` | counter | 1 | `result` | `environment`, `reason_code` | 配置校验计数 |
| `ls_prod_defaults_config_check_duration_ms` | histogram | ms | `result` | `environment` | 配置校验耗时 |
| `ls_prod_defaults_mock_violations_total` | counter | 1 | `violation_type` | `environment` | mock/静默降级违规计数 |
| `ls_prod_defaults_startup_failures_total` | counter | 1 | `reason_code` | `environment` | 启动失败计数 |
| `ls_prod_defaults_audit_records_total` | counter | 1 | `result` |  | 审计记录写入计数 |

## 2) SLO（最小阈值）

- **生产红线**：检测到 mock 默认值或静默降级 MUST 100% 阻断并审计（作为 Gate-0 阻断条件）
- **配置校验可用性**：配置校验成功率（不含客户端拒绝）SHALL ≥ 99.9%
- **配置校验延迟**：p95 `ls_prod_defaults_config_check_duration_ms` SHALL ≤ 100ms

