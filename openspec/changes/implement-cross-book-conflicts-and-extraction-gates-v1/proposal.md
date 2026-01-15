# Proposal — Implement Cross-Book Conflicts + Semantic Extraction Quality Gates (v1)

## Why

当前仓库已有两份规格：

- `cross-book-consistency-conflicts`：跨书一致性与冲突
- `semantic-extraction-quality-gates`：语义抽取质量门禁（Gate-1）

但工程侧仍缺少“可跑、可审计、可阻断”的门禁闭环：

- 冲突检测存在实现线索（`scripts/knowledge_graph_builder/builders/conflict_detector.py`），但缺少统一报告产物、阈值口径与可审计的例外机制（白名单/审批记录），无法在门禁中稳定阻断。
- 抽取质量校验存在实现线索（`scripts/codegen/validation.py`），但缺少规则版本化、报告化产物与最低阻断集合（失败必须阻断的规则集合）以及门禁入口。

本 change 目标：将二者落地为可执行 Gate/Asset-Gate，输出机器可读报告并在阈值越界时阻断，同时保留可审计的例外/白名单机制。

## Scope

### Cross-book conflicts (asset governance)
- 将冲突检测输出统一为机器可读报告（JSON）+ 人类可读摘要（MD）。
- 定义阈值口径与阻断策略：按冲突类型/严重度计数；超过阈值则门禁失败。
- 增加白名单/例外审批机制：允许对特定冲突项进行显式豁免，并将豁免记录输出为审计可追溯产物。

### Semantic extraction quality gates (Gate-1)
- 将 validation 规则“版本化 + 可配置”：定义最低阻断集合（至少：ERROR 级别必须为 0）。
- 产出质量门禁报告（JSON）：包含错误类型聚合、样本列表、阈值与判定结果，并绑定 `version_id/corpus_release_id`。

### Acceptance / CI wiring
- 升级两份 spec 的 `acceptance.md`：加入实际脚本命令、报告路径、阈值口径与阻断策略。
- 新增门禁脚本入口（scripts/gates）与 GitHub Actions workflow，并上传报告 artifacts。
- 更新 `openspec/SPECS_INDEX.md` 对应两行状态并落盘 Evidence。

## Planned Artifacts

- `artifacts/cross_book_conflicts/conflict_report.json`
- `artifacts/cross_book_conflicts/conflict_report.md`
- `artifacts/cross_book_conflicts/exceptions_applied.json`
- `artifacts/semantic_extraction_quality/quality_report.json`
- `scripts/gates/gate1_cross_book_conflicts_and_quality.sh`
- 配置与例外：
  - `data/knowledge_graph/conflict_gate_policy.v1.yaml`
  - `data/quality_gates/semantic_extraction_rules.v1.yaml`
  - `data/quality_gates/exceptions/`（可选）

## Risks

- **误报/过严阈值**：初版阈值过严会导致阻断频繁；缓解：默认阈值宽松 + 例外机制明确审计。
- **性能**：全量冲突检测/全量校验可能较慢；缓解：门禁默认 deterministic sample（可切 `--all`）。

## Rollback

- 将阻断降级为“只产报告不阻断”（通过阈值/开关实现），保留报告与例外审计产物。

