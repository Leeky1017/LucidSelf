# Proposal — Implement Engine ID Governance + Identity Foundation (v1)

## Why

当前 `engine-id-governance` 与 `identity-and-data-isolation` 两个 Gate-0 specs 已具备文档与契约，但工程侧仍存在关键缺口：

- 请求侧仍存在“客户端传 `user_id`”的路径，缺少统一的“鉴权产生身份”与 `org_id` 方案。
- 运行态 `engine_id` 在关键链路（pipeline / rule / fusion / narrative）缺少统一的格式校验与 registry 校验，失败原因不够确定性、不可审计。
- 两个 spec 的 `acceptance.md` 仍以“验文档”为主，缺少可执行的工程验收命令（pytest/脚本/CI 入口）。

本 change 目标是将上述两份 spec 从“文档存在”升级为“工程可验收”，并提供 Gate-0 可执行门禁入口与证据落盘。

## Scope

### Identity / Data Isolation

- 引入 `org_id` 最小方案：鉴权产出 `user_id/org_id`，并在关键数据访问与写入路径携带并校验。
- 将关键写接口从“客户端传 user_id”迁移到“鉴权产生 user_id/org_id”（最小可行：Dream Journal 写入链路）。
- 为越权/跨租户访问提供确定性的拒绝原因代码与可审计的记录（日志/测试可验证）。

### Engine ID Governance

- 统一运行态 `engine_id` 的格式校验与 registry 校验，覆盖关键路径：pipeline / rule / fusion / narrative。
- 缺失/非法/未注册的 `engine_id` 产生确定性的拒绝原因代码，并在日志中可关联 `engine_id`（以及请求关联字段，如 `request_id`）。

### Acceptance / CI Wiring

- 升级两个 spec 的 `acceptance.md`：加入可执行命令（pytest target + gate 脚本）与“通过/失败”标准。
- 提供可一键执行的 Gate-0 验收入口（scripts/pytest），便于 CI 接入。
- 为本 change 的关键命令输出落盘到 `openspec/changes/<change-id>/evidence/`。
- 更新 `openspec/SPECS_INDEX.md` 中两条 spec 的状态（至少 “未开始” → “进行中/已完成”）。

## Interfaces / Artifacts (Planned)

- **New/Updated runtime interfaces**
  - 引入统一身份上下文（`user_id/org_id`）的传递方式（FastAPI 依赖/上下文对象）。
  - `Dream` 写接口使用鉴权用户身份，不再信任客户端传 `user_id`。
- **Registry / validation**
  - `data/engines/registry.json` 与运行态 `engine_id` 口径对齐，并提供统一校验入口供 pipeline/rule/fusion/narrative 调用。
- **Tests**
  - 新增 Gate-0 单元/集成测试：`engine_id` 校验（格式/注册表/拒绝原因确定性）与身份隔离（`user_id/org_id` 绑定与越权阻断）。
- **Scripts**
  - 新增 gate 脚本：一键运行本 change 对应的工程验收集合（pytest + openspec validate）。

## Risks

- **API 兼容性**：部分旧路径可能依赖“客户端传 user_id”。缓解：仅对关键写接口强制鉴权；读接口按需逐步迁移。
- **引擎ID口径变更影响面**：若 registry 与运行态 ID 不一致，将导致阻断。缓解：先对齐 registry，再补齐测试覆盖。

## Rollback

- 若出现大面积兼容问题，可临时回退为“仅格式校验 + registry 软告警（不阻断）”的策略，并保留确定性拒绝原因与审计输出。
- 逐步恢复到严格阻断策略（以 tests + evidence 作为放量依据）。

