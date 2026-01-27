# Golden Set（回归金样本集）

本目录用于存放 **Golden Set**（金样本/金标准）资产：用于回归测试、质量门禁与人工验收的最小可复现实例集合。

## 约定

- 该目录是 `data/governance/corpus_manifest.v1.yaml` 中声明的资产项 `golden_set` 的落盘路径。
- 当前阶段允许为空目录（以 README 作为占位文件），后续可逐步补齐：
  - 引擎级 golden cases（bazi/astro/dream/tarot/yijing/ziwei）
  - 端到端 regression fixtures
  - 期望输出与漂移阈值（drift thresholds）

