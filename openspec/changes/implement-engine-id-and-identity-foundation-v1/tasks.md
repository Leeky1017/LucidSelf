# Tasks — Implement Engine ID Governance + Identity Foundation (v1)

> 目标：把 `engine-id-governance` 与 `identity-and-data-isolation` 两个 Gate-0 specs 从“验文档”升级为“验工程产物”；所有任务必须在 Evidence 落盘后才可勾选。

## Change bootstrap

- [x] 创建 change 目录与任务清单，并通过 `openspec validate implement-engine-id-and-identity-foundation-v1 --strict --no-interactive` (evidence: openspec/changes/implement-engine-id-and-identity-foundation-v1/evidence/t01__openspec_validate_change.txt)

## Identity foundation (user_id/org_id)

- [x] 引入 `org_id` 最小方案：鉴权产出 `user_id/org_id`，并形成可传递的统一身份上下文（至少覆盖 Dream 写路径） (evidence: openspec/changes/implement-engine-id-and-identity-foundation-v1/evidence/t02__identity_context.txt)
- [x] Dream 写接口迁移：不再信任客户端传 `user_id`，改为使用鉴权身份；数据访问携带 `user_id/org_id` 并阻断越权 (evidence: openspec/changes/implement-engine-id-and-identity-foundation-v1/evidence/t03__dream_auth_migration.txt)
- [x] 新增测试：覆盖 `user_id/org_id` 绑定与越权/跨租户访问阻断（含确定性拒绝原因码） (evidence: openspec/changes/implement-engine-id-and-identity-foundation-v1/evidence/t04__identity_tests.txt)

## Engine ID governance (format + registry)

- [x] 对齐 engine registry 与运行态 `engine_id` 口径，并补齐 registry 中关键引擎（至少 pipeline/rule/fusion/narrative 使用到的集合） (evidence: openspec/changes/implement-engine-id-and-identity-foundation-v1/evidence/t05__engine_registry_aligned.txt)
- [x] 在 pipeline / rule / fusion / narrative 关键路径加入 `engine_id`：格式校验 + registry 校验 + 缺失时确定性拒绝原因 (evidence: openspec/changes/implement-engine-id-and-identity-foundation-v1/evidence/t06__engine_id_governance_runtime.txt)
- [x] 新增测试：覆盖 `engine_id` 缺失/非法/未注册的拒绝原因确定性，以及关键路径的校验触发 (evidence: openspec/changes/implement-engine-id-and-identity-foundation-v1/evidence/t07__engine_id_tests.txt)

## Acceptance upgrade + wiring

- [x] 升级两个 spec 的 `acceptance.md`：加入可执行工程验收命令（pytest target + gate 脚本）与通过标准 (evidence: openspec/changes/implement-engine-id-and-identity-foundation-v1/evidence/t08__acceptance_docs_updated.txt)
- [x] 提供一键 Gate-0 验收入口（scripts/pytest），并给出 CI 可直接调用的命令行 (evidence: openspec/changes/implement-engine-id-and-identity-foundation-v1/evidence/t09__gate_script.txt)
- [x] 更新 `openspec/SPECS_INDEX.md` 中 `engine-id-governance` 与 `identity-and-data-isolation` 状态（至少 “未开始”→“进行中/已完成”） (evidence: openspec/changes/implement-engine-id-and-identity-foundation-v1/evidence/t10__specs_index_status_updated.txt)

## Final verification + evidence

- [x] 运行并落盘：`openspec validate --specs --strict --no-interactive` + 本 change 的 gate 脚本/pytest 入口 (evidence: openspec/changes/implement-engine-id-and-identity-foundation-v1/evidence/t11__final_validation_and_tests.txt)
