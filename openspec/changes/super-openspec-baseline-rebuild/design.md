# Super OpenSpec Baseline Rebuild Design

## 设计立场
- Specs-first：规格先于实现；实现必须可追溯映射到 Requirement/Scenario。
- Gates-first：门禁先行；失败必须阻断晋级，直到任务闭环。
- Asset-layer disciplined：资产层并行推进，但必须满足许可/血缘/QA/审计。

## 统一方式
- 统一目录：`openspec/specs/<capability>/spec.md` 为权威入口。
- 统一格式：Requirement/Scenario 的 MUST/SHALL 与结构固定。
- 统一仪表盘：以 checklist 任务进度与严格校验作为工程控制面。
