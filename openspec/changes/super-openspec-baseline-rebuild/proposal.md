# Super OpenSpec Baseline Rebuild（全量规格重构基线）

## 为什么必须重写
把 OpenSpec 从“文档堆”升级为“工程控制台”，需要统一：规格结构、门禁定义、依赖 DAG 与任务化推进方式。

## 目标（控制台效果）
- `openspec list` / `openspec list --specs` / `openspec list --changes` 输出具备统计意义。
- `openspec validate --specs --strict --no-interactive` 严格校验通过。
- 26 个 specs 的口径一致：术语、门禁、依赖、验收方式可追溯。

## 范围
- 仅重建 `openspec/` 内的规范体系，不实现任何业务代码。
- 只定义 MUST/SHALL 的行为、门禁与验收口径。
