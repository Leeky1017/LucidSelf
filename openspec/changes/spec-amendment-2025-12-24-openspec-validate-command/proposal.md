# Spec Amendment Proposal — openspec validate command (non-interactive)

## 事实与冲突

当前仓库内多个关键门禁/验收口径使用命令：

- `openspec validate --strict`

但 `openspec validate` 在未指定 `--specs/--changes/--all` 或 `<item-name>` 且处于非交互环境时，会返回：

- 输出：`Nothing to validate...`
- 退出码：`1`

导致：
- `openspec/QUALITY_GATES.md` 定义的 Gate-0/1/2/3 命令在非交互执行时不可通过。
- 多个 spec 的 `acceptance.md` / `tasks.md` 中的验收命令不可复现（自动化/审计环境必然失败）。
- 按 SOP 落盘的 dashboard/runlog 在严格执行“退出码必须为 0”时会触发阻断。

该问题属于“验收不可执行”，必须通过规格修订流程收敛口径，而不是在实现侧“忽略失败”。

## 修订目标

在不改变产品行为的前提下，使门禁与验收命令在非交互环境可执行、可复现、可审计：

- 将门禁/验收校验命令统一为：`openspec validate --specs --strict --no-interactive`
- Gate-1/2 的附加口径保持不变：继续要求 `openspec list --specs` / `openspec list --changes`

## 影响面

- `openspec/QUALITY_GATES.md`
- `openspec/SPECS_INDEX.md`
- 26 个 spec 的 `acceptance.md`
- 26 个 spec 的 `tasks.md` 中“校验通过”类任务描述（与验收口径对齐）
- `_ops` 下后续 runlog/回归日志生成命令（以新口径为准）

## 风险与回滚

- 风险：部分历史 runlog 仍使用旧命令，可能显示非 0 退出码，影响审计一致性。
- 回滚：恢复文档命令为旧口径即可（不涉及运行时代码/数据结构变更）。

## Rollout 策略

1) 先修订 gate/index/acceptance 口径（文档层）。
2) 重新执行 `openspec validate --specs --strict --no-interactive` 与相关 list 命令并落盘证据。
3) 后续所有 spec 推进与 dashboard 落盘，统一使用新口径。

