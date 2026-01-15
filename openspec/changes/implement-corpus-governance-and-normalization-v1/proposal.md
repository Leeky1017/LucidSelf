# Proposal — Implement Corpus Governance + Text Normalization/Alignment (v1)

## Why

当前仓库已具备 `corpus-governance` 与 `text-normalization-alignment` 的规格与契约，但工程侧仍缺关键“可执行、可追溯、可复现”的产物：

- `data/` 下语料资产丰富，但缺少统一、机器可读的“语料清单/许可/来源/血缘/版本”清单；`data/sources/` 为空，导致来源与许可无法被门禁与审计链路引用。
- 归一化与对齐目前更多是“有代码线索”，缺少统一的归一化产物定义、输出目录、校验与可定位的对齐报告（至少定位到书/段落/条目）。
- 规格层 `acceptance.md` 仍偏“验文档”，需要升级为“验工程产物”，并提供后续 CI gate 接入点。

本 change 目标：把上述两份 spec 从“文档存在”升级为“工程可验收”，并形成可审计的最小产物闭环。

## Scope

### Corpus Governance（资产门禁）
- 引入机器可读 `corpus manifest`（YAML）作为“语料清单/许可/来源/血缘/版本”的最小权威入口。
- 落地 manifest 生成与校验脚本：生成“编译版”manifest（含 `version_id/corpus_release_id` 与可审计摘要），校验字段/引用/路径可解析。

### Text Normalization + Alignment（资产门禁）
- 定义统一归一化产物：标准字段（book/node/snippet/factor 等）、输出目录、校验策略。
- 基于归一化产物生成对齐报告（JSON + Markdown），对齐条目至少可定位到书/段落/条目（book_id / node_id / snippet_ids）。

### Acceptance / CI Wiring
- 升级 `openspec/specs/{corpus-governance,text-normalization-alignment}/acceptance.md`：加入可执行命令、报告路径、通过标准与阻断策略。
- 提供 `scripts/gates/asset_gate_corpus.sh` 作为资产门禁入口；预留 GitHub Actions workflow 接入点。
- 更新 `openspec/SPECS_INDEX.md`：两条 spec 状态从“未开始”推进到“进行中/已完成”。
- 关键命令输出落盘到 `openspec/changes/implement-corpus-governance-and-normalization-v1/evidence/`。

## Planned Artifacts

- **Corpus manifest（source-of-truth）**: `data/governance/corpus_manifest.v1.yaml`
- **Compiled manifest（auditable）**: `artifacts/corpus_governance/corpus_manifest.compiled.json`
- **Normalized entries（auditable）**: `artifacts/text_normalization_alignment/normalized_entries.jsonl`
- **Alignment report（auditable）**:
  - `artifacts/text_normalization_alignment/alignment_report.json`
  - `artifacts/text_normalization_alignment/alignment_report.md`
- **Gate entrypoint**: `scripts/gates/asset_gate_corpus.sh`

## Risks

- **来源/许可不完整**：初版 manifest 可能只能覆盖 repo 内可核验的最小字段；通过 `license_id=unknown-*` 显式标注并在 gate 中给出可审计提示。
- **性能**：全量扫描/对齐可能较慢；gate 默认采用确定性的“抽样集”并提供 `--all` 扩展参数。

## Rollback

- 将门禁降级为“生成报告但不阻断”（通过阈值/开关实现），同时保留产物与审计输出；不移除 manifest 与归一化产物定义。

