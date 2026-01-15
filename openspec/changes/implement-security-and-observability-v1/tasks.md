# Tasks — Implement Security/Privacy/Compliance + Observability SLOs (v1)

> 目标：把 `security-privacy-compliance` 与 `observability-slos` 两个 Gate-0 specs 从“验文档”升级为“验工程产物”；所有任务必须在 Evidence 落盘后才可勾选。

## Change bootstrap

- [x] 创建 change 目录、delta specs，并通过 `openspec validate implement-security-and-observability-v1 --strict --no-interactive` (evidence: openspec/changes/implement-security-and-observability-v1/evidence/t01__openspec_validate_change.txt)

## Structured logging + privacy (PII)

- [x] 统一结构化日志字段：`request_id/trace_id/user_id/org_id/engine_id/version_id`，并实现请求级上下文传播（响应头回写 `X-Request-ID`/`X-Trace-ID`） (evidence: openspec/changes/implement-security-and-observability-v1/evidence/t02__log_schema_and_propagation.txt)
- [x] 实现默认脱敏策略：PII/secret/token 不入日志，并修订现有日志点（如 auth/email）避免输出原文 (evidence: openspec/changes/implement-security-and-observability-v1/evidence/t03__log_redaction_tests.txt)

## Metrics + SLO baseline

- [x] 落地核心请求指标并可导出（最小：Prometheus `/metrics` 或等价可抓取输出），且默认标签避免高基数标识符 (evidence: openspec/changes/implement-security-and-observability-v1/evidence/t04__metrics_endpoint_and_core_metrics.txt)
- [x] 新增测试：验证核心指标存在、标签约束成立、请求路径指标可随请求变化 (evidence: openspec/changes/implement-security-and-observability-v1/evidence/t05__metrics_tests.txt)

## Readiness/Liveness (blocking)

- [x] `/ready` 实现真实依赖检查：DB/Redis 连通性 + LLM provider 配置；失败可阻断并返回可判定原因 (evidence: openspec/changes/implement-security-and-observability-v1/evidence/t06__readiness_dependency_checks.txt)
- [x] 新增测试：模拟依赖缺失/不可达时 `/ready` 返回 not-ready 且原因稳定 (evidence: openspec/changes/implement-security-and-observability-v1/evidence/t07__readiness_tests.txt)

## Audit (write + export)

- [x] 定义并实现审计事件写入（最小：文件 NDJSON），并在关键阻断/安全事件上落审计记录 (evidence: openspec/changes/implement-security-and-observability-v1/evidence/t08__audit_write_runtime.txt)
- [x] 提供审计导出命令与导出校验（每行 JSON + 必填字段齐备） (evidence: openspec/changes/implement-security-and-observability-v1/evidence/t09__audit_export_command.txt)
- [x] 新增测试：写入审计事件并导出，验证 NDJSON 合规与必填字段 (evidence: openspec/changes/implement-security-and-observability-v1/evidence/t10__audit_tests.txt)

## Acceptance upgrade + wiring

- [x] 升级两份 spec 的 `acceptance.md`：加入可执行工程验收命令（gate 脚本/pytest/示例命令）证明日志/指标/审计/ready 可用 (evidence: openspec/changes/implement-security-and-observability-v1/evidence/t11__acceptance_docs_updated.txt)
- [x] 提供一键 Gate-0 验收入口（`scripts/gates/gate0_security_observability.sh`）并接入 GitHub Actions (evidence: openspec/changes/implement-security-and-observability-v1/evidence/t12__gate_script_and_ci.txt)
- [x] 更新 `openspec/SPECS_INDEX.md` 中 `security-privacy-compliance` 与 `observability-slos` 状态（至少 “未开始”→“进行中/已完成”） (evidence: openspec/changes/implement-security-and-observability-v1/evidence/t13__specs_index_status_updated.txt)

## Final verification + evidence

- [x] 运行并落盘：`openspec validate --specs --strict --no-interactive` + 本 change 的 gate 脚本 (evidence: openspec/changes/implement-security-and-observability-v1/evidence/t14__final_validation_and_gate.txt)
