# 跨书一致性与冲突（Cross-Book Consistency Conflicts）

## Purpose

本 spec 定义 LS 的「跨书一致性与冲突」能力（`cross-book-consistency-conflicts`），用于规范 跨书/跨源冲突的发现、归因、决策与例外管理 的契约、门禁与审计。
关键产物包括：冲突记录、来源引用、决策与例外批准记录、冲突报表。
本 spec 只定义 MUST/SHALL 的行为与验收口径，不包含实现细节/伪代码/代码路径。

## Requirements

### Requirement: 资产契约与范围（Scope & Contract）
系统 MUST 为「跨书一致性与冲突」定义资产范围与契约边界，并明确最小标识符集合（至少包含 `corpus_release_id`, `version_id`）。

#### Scenario: 资产可被引用与追溯
- **WHEN** 资产被注册或被引用为证据来源
- **THEN** 其范围、版本与来源被明确记录
- **AND** 引用必须可回到具体 `corpus_release_id` 或等价版本标识

### Requirement: 版本/血缘/许可（Version & License）
系统 MUST 为资产变更建立 `version_id`/血缘，并记录许可与使用约束。

#### Scenario: 许可约束被执行
- **WHEN** 资产被使用或发布
- **THEN** 许可/访问约束被校验
- **AND** 违反约束的使用 MUST 被阻断并留下审计记录

### Requirement: 一致性与冲突（Consistency）
系统 SHALL 定义一致性判定规则，并对冲突/例外给出可审计处置流程。

#### Scenario: 冲突被记录与处置
- **WHEN** 检测到跨源冲突或对齐歧义
- **THEN** 系统产生冲突记录并列出来源证据
- **AND** 处置结果（含例外批准）必须可追溯

### Requirement: QA与复核（QA & Review）
系统 MUST 定义 QA/校对流程与度量口径，确保质量问题可闭环。

#### Scenario: QA 结果可审计
- **WHEN** QA/校对完成
- **THEN** 结果、缺陷与批准记录被持久化
- **AND** 指标报表可按 `corpus_release_id` 聚合

### Requirement: 审计与可观测（Auditability）
系统 MUST 输出可观测信号与审计导出能力，支持最小证据包导出。

#### Scenario: 审计导出可用
- **WHEN** 审计导出被请求
- **THEN** 系统导出包含来源、版本与决策的最小证据包
- **AND** 导出行为被记录并可追责

### Requirement: 资产门禁验收（Asset Gate）
系统 SHALL 定义资产门禁验收口径，且未达标 MUST 阻断进入其所属门禁（资产门禁）。

#### Scenario: 门禁阻断生效
- **WHEN** 资产尝试进入发布或被用于用户可见输出
- **THEN** 门禁检查给出通过/失败判定
- **AND** 失败 MUST 阻断并产出可行动的整改项
