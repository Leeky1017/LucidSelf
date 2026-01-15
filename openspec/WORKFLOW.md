# WORKFLOW（推进流程）

## 唯一推进入口
任何推进必须落在某个 spec 的 `tasks.md` checklist 上，任务必须可独立验收、可回写状态。

## 节奏
- P0 先行，Gate-0/1 先行；资产门禁可并行但受门禁阻断约束。
- 门禁失败必须阻断晋级，直到任务闭环。

## Review 规则（最小粒度）
- Requirement：原子、可测试、可审计；禁止揉多目标。
- Scenario：可执行判定（WHEN/THEN/AND）。
- Tasks：可验收且可回写状态；禁止“3 条任务管一坨”。
- 禁止：实现细节、伪代码、代码路径、具体技术选型。

## 仪表盘命令
- `openspec list`
- `openspec list --specs`
- `openspec list --changes`
- `openspec validate --specs --strict --no-interactive`
