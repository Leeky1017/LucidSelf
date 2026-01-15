# Proposal — Implement Versioning/Deviation Detection + Boot/Regression Baseline (v1)

## Why

当前 `versioning-and-deviation-detection`（Gate-0）与 `bootability-and-regression-baseline`（Gate-1）两份 specs 已具备规格与契约，但工程侧仍存在关键缺口：

- 运行态 `version_id` 口径不统一：输出/审计/测试链路无法稳定追溯到同一 `version_id`；`APP_VERSION` 与 `version_id` 语义边界混用。
- `corpus_release_id` 缺少最小可执行方案：无法在回归/偏差报告中稳定记录“语料版本”。
- 漂移检测虽有雏形（`DriftDetector`），但未接入回归流程，缺少可执行门禁入口与可落盘报告产物。
- 启动性（bootability）缺少“启动即失败”的硬条件定义；`/ready` 未覆盖关键失败类型（配置不合法/迁移未跑/依赖缺失）。
- 两个 spec 的 `acceptance.md` 仍偏“验文档”，需要升级为“验工程产物”，并接入 tests/scripts/CI。

本 change 目标是将上述两份 spec 从“文档存在”升级为“工程可验收”，提供 Gate-0/1 可执行门禁入口与证据落盘，支撑“版本可追溯、回归可重复、偏差可检测；ready/boot 失败能阻断”。

## Scope

### Versioning + corpus_release_id (Gate-0)
- 引入统一的 `version_id`/`corpus_release_id` 运行态口径：可解析、可校验、可注入（环境变量优先）。
- 关键链路统一携带并输出：结构化日志/审计事件/回归产物（报告、基线、版本关联报告）。
- 最小“版本清单（VersionManifest）”产物落盘，用于把 `version_id` 与 `engine_id` 关联并可审计。

### Deviation detection wired to regression
- 将 drift 检测接入回归流程：最小实现为 `pytest` 入口 + 机器可读 drift 报告产物（JSON）+ JUnit（pytest）。
- 失败阻断：漂移超过阈值时回归失败（Gate-1 阻断），并输出可行动摘要。

### Bootability + readiness (Gate-1)
- 定义并落地“启动即失败”的硬条件（最小集合）：依赖缺失、配置不合法、迁移未跑。
- `/ready` 真实反映上述硬条件（required=true 的检查失败即 503），并形成可审计阻断信号。

### Acceptance / CI Wiring
- 升级两个 spec 的 `acceptance.md`：加入可执行命令（pytest target + gate 脚本）与通过/失败标准。
- 新增 Gate-0/1 一键验收脚本并接入 CI（GitHub Actions workflow）。
- 更新 `openspec/SPECS_INDEX.md` 中两条 spec 状态（至少 “未开始”→“进行中/已完成”）。
- 关键命令输出落盘到 `openspec/changes/implement-versioning-and-boot-regression-v1/evidence/`。

## Interfaces / Artifacts (Planned)

- **Runtime identifiers**
  - 统一 `version_id` 与 `corpus_release_id` 的解析/校验与默认策略（可注入）。
- **Artifacts**
  - Version manifest（机器可读）
  - Drift report（机器可读）
  - Startup check list（机器可读）
  - Regression suite baseline（机器可读）
  - Version link report（机器可读：版本 ↔ 测试/报告/产物）
- **Scripts**
  - Gate-0 脚本：版本化/偏差检测工程验收集合
  - Gate-1 脚本：bootability/回归基线工程验收集合
- **Tests**
  - Gate-0 tests：`version_id`/`corpus_release_id` 口径与产物校验
  - Gate-1 tests：boot checks/readiness + drift regression + pipeline E2E 基线

## Risks

- **兼容性**：新增响应字段/严格校验可能影响旧调用方。缓解：新增字段保持可选；严格阻断仅在 Gate/production 模式启用。
- **漂移误报**：阈值过严导致回归不稳定。缓解：基线范围最小化 + 明确可行动 drift 报告 + 分阶段收紧阈值。
- **启动检查过严**：开发环境受阻。缓解：默认仅 production/显式开关启用硬失败；其他环境仍可通过 `/ready` 观察。

## Rollback

- 可将“启动即失败”降级为“仅 `/ready` 503 + 告警/审计，不崩溃进程”（通过环境开关）。
- 可将 drift 阈值调高或临时降级为“报告但不阻断”，并保留 drift 报告产物与审计输出。

