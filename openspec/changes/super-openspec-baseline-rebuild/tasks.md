# Super OpenSpec Baseline Rebuild Tasks（项目级）

- [x] 基线盘点：命令输出固化到 `openspec/_ops/before.txt`
- [x] 清理与重置：清空旧 specs/changes 并记录 `openspec/_ops/cleanup_log.md`
- [x] 顶层控制面：project/index/workflow/gates 四份文档中文化并可审计
- [x] 重建 26 specs：每个 spec 具备 5 件套（spec/requirements/tasks/design/acceptance）
- [x] 依赖与门禁对齐：SPECS_INDEX 的 DAG 与 Gate 归属一致且无环
- [x] 严格校验：`openspec validate --specs --strict --no-interactive` 通过
- [x] 仪表盘落盘：`openspec/_ops/final_dashboard.txt` 写入 list/specs/changes/validate 输出
- [ ] 归档：待实现侧完成并验证后移入 `openspec/changes/archive/`（负责人执行）
