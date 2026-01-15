# Proposal — Implement Security/Privacy/Compliance + Observability SLOs (v1)

## Why

`security-privacy-compliance` 与 `observability-slos` 两个 Gate-0 specs 已具备规格/契约，但工程侧仍缺少可执行、可审计的落地：

- 结构化日志字段不统一，缺少 `request_id/trace_id/user_id/org_id/engine_id/version_id` 的一致关联口径。
- 日志脱敏策略未形成“默认安全”：PII（如 email/phone/token）仍可能进入日志。
- 核心请求链路缺少可导出指标（Prometheus/结构化 metrics），SLO 基线不可量化执行。
- `/ready` 目前为占位返回，无法对关键依赖（DB/Redis/LLM provider 配置）进行阻断。
- 审计事件缺少最小可行写入与导出（NDJSON）能力，无法形成闭环证据。

本 change 目标是把两份 spec 从“验文档”升级为“验工程产物”：提供可运行的 Gate-0 验收入口、可自动化执行的验收命令、以及可落盘的证据。

## Scope

### Structured Logging + Redaction

- 统一请求级结构化日志字段：`request_id/trace_id/user_id/org_id/engine_id/version_id`（缺失字段提供明确契约与默认行为）。
- 增加默认脱敏策略：禁止 PII/secret/token 进入日志（至少覆盖常见键与 email 形式）。
- 请求与响应头传播：回写 `X-Request-ID` 与 `X-Trace-ID` 以支持端到端关联。

### Metrics + SLO Baseline

- 增加 Prometheus 可抓取的指标导出端点，并落地核心请求指标（`ls_requests_total`, `ls_request_duration_ms`, `ls_errors_total`, `ls_blocks_total` 等）。
- 约束指标标签基数：默认禁止 `user_id/org_id/request_id/trace_id/version_id` 作为标签。

### Readiness/Liveness

- `/live` 保持进程存活语义。
- `/ready` 变为真实就绪检查：至少检查 DB/Redis 连通性与 LLM provider 配置有效性；失败返回可判定的阻断原因并计入 metrics/audit。

### Audit (write + export)

- 定义并实现最小审计事件写入（文件 NDJSON 为最小可行）。
- 提供导出命令（CLI/script）与导出校验（每行 JSON + 必填字段齐备）。

### Acceptance + CI Wiring

- 升级两份 spec 的 `acceptance.md`：加入可执行命令（gate 脚本/pytest）证明日志/指标/审计/ready 可用。
- 接入 `scripts/` + GitHub Actions：使 Gate-0 口径可自动化执行并可阻断。
- 关键证据输出落盘到 `openspec/changes/implement-security-and-observability-v1/evidence/`，并更新 `openspec/SPECS_INDEX.md` 两条 spec 状态。

## Risks

- **运行时开销**：metrics/审计写入引入额外开销。缓解：最小指标集合 + 低基数标签 + 文件追加写。
- **脱敏误报/漏报**：regex/键策略可能过度或不足。缓解：以“拒绝/删除敏感字段”为主，配套测试覆盖典型 PII。
- **就绪检查阻断**：在无 DB/Redis 的本地环境可能长期 not-ready。缓解：将“是否强制依赖”为显式配置，并在输出中给出可行动的失败原因。

## Rollback

- 可通过配置关闭严格依赖检查（仅返回 `ready=true` 并标注 degraded），或临时关闭审计写入/metrics 导出（不删除接口，仅返回明确的不可用状态）。
- 回滚不改变对外数据模型；优先通过配置回退而非删改接口。

