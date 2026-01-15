# Tasks — Implement Versioning/Deviation Detection + Boot/Regression Baseline (v1)

> 目标：把 `versioning-and-deviation-detection`（Gate-0）与 `bootability-and-regression-baseline`（Gate-1）从“验文档”升级为“验工程产物”；所有任务必须在 Evidence 落盘后才可勾选。

## Change bootstrap

- [x] 创建 change 目录与任务清单，并通过 `openspec validate implement-versioning-and-boot-regression-v1 --strict --no-interactive` (evidence: openspec/changes/implement-versioning-and-boot-regression-v1/evidence/t01__openspec_validate_change.txt)

## Versioning IDs + corpus_release_id (Gate-0)

- [x] 定义并落地统一 `version_id` 口径：输出/审计/测试链路可追溯；缺失/非法具备确定性拒绝原因 (evidence: openspec/changes/implement-versioning-and-boot-regression-v1/evidence/t02__version_id_unified.txt)
- [x] 补齐 `corpus_release_id` 最小方案：定义、解析、落盘到回归/偏差报告与版本关联工件 (evidence: openspec/changes/implement-versioning-and-boot-regression-v1/evidence/t03__corpus_release_id_wired.txt)
- [x] 产物：VersionManifest（机器可读）生成并可在回归流程中引用 (evidence: openspec/changes/implement-versioning-and-boot-regression-v1/evidence/t04__version_manifest_artifact.txt)

## Deviation detection wired to regression

- [x] Drift 检测接入回归：pytest 可执行 + 机器可读 drift 报告产物（JSON）+ 漂移超阈值阻断 (evidence: openspec/changes/implement-versioning-and-boot-regression-v1/evidence/t05__drift_regression_wired.txt)

## Bootability + readiness (Gate-1)

- [x] 定义“启动即失败”硬条件（依赖缺失/配置不合法/迁移未跑）并落地到启动流程 (evidence: openspec/changes/implement-versioning-and-boot-regression-v1/evidence/t06__boot_hard_fail_conditions.txt)
- [x] `/ready` 真实反映启动硬条件与依赖检查（required=true 的失败即 503）并输出可审计阻断信号 (evidence: openspec/changes/implement-versioning-and-boot-regression-v1/evidence/t07__readiness_real.txt)

## Acceptance upgrade + wiring

- [x] 升级两个 spec 的 `acceptance.md`：加入可执行工程验收命令（pytest target + gate 脚本）与通过标准 (evidence: openspec/changes/implement-versioning-and-boot-regression-v1/evidence/t08__acceptance_docs_updated.txt)
- [x] 提供 Gate-0/1 一键验收入口（scripts/gates）并接入 CI（GitHub Actions） (evidence: openspec/changes/implement-versioning-and-boot-regression-v1/evidence/t09__gate_scripts_and_ci.txt)
- [x] 更新 `openspec/SPECS_INDEX.md` 中两条 spec 状态（至少 “未开始”→“进行中/已完成”） (evidence: openspec/changes/implement-versioning-and-boot-regression-v1/evidence/t10__specs_index_status_updated.txt)

## Final verification + evidence

- [x] 运行并落盘：`openspec validate --specs --strict --no-interactive` + Gate-0/1 脚本/pytest 入口 (evidence: openspec/changes/implement-versioning-and-boot-regression-v1/evidence/t11__final_validation_and_tests.txt)
