# 启动性与回归基线（Bootability and Regression Baseline）

## Purpose

本 spec 定义 LS 的「启动性与回归基线」能力（`bootability-and-regression-baseline`），用于规范 可启动性基线、冒烟检查与回归基线定义 的契约、门禁与审计。
关键产物包括：启动检查清单、回归套件基线、失败阻断记录、版本关联报告。
本 spec 只定义 MUST/SHALL 的行为与验收口径，不包含实现细节/伪代码/代码路径。

## Requirements

### Requirement: 契约与标识符（Contract & IDs）
系统 MUST 为「启动性与回归基线」定义稳定、版本化契约，并明确最小标识符集合（至少包含 `version_id`）及其语义边界。

#### Scenario: 请求带齐标识符并可追溯
- **WHEN** 该能力处理一次请求/作业
- **THEN** 请求上下文包含所需标识符并被记录
- **AND** 标识符缺失/非法 MUST 触发确定性的拒绝原因

### Requirement: 数据模型与完整性（Data & Integrity）
系统 MUST 对关键产物（启动检查清单、回归套件基线、失败阻断记录、版本关联报告）定义字段级约束，并对完整性/引用可解析性实施校验。

#### Scenario: 无效产物被阻断
- **WHEN** 产物缺字段、引用不可解析或版本不一致
- **THEN** 校验失败并阻断进入下游阶段
- **AND** 失败原因以可审计的方式记录

### Requirement: 运行时确定性（Runtime Determinism）
系统 SHALL 定义可重复的运行时行为边界：相同输入（含版本）产生等价输出，偏差 MUST 可检测与解释。

#### Scenario: 同输入同输出（在契约内）
- **WHEN** 在相同输入与相同版本下重复执行
- **THEN** 输出在契约定义的等价范围内保持一致
- **AND** 非确定性因素 MUST 被显式标注并可审计

### Requirement: 可观测与审计（Observability）
系统 MUST 输出 metrics/logs/traces，并确保可按 `version_id`/`engine_id`/`user_id` 关联定位。

#### Scenario: 运维可定位问题
- **WHEN** 发生失败、降级或门禁阻断
- **THEN** 指标与日志能定位到请求、版本与责任边界
- **AND** 关键事件必须形成审计记录

### Requirement: 安全/隐私/合规（Security/Privacy/Compliance）
系统 MUST 执行最小权限、数据最小化、脱敏与保留策略，并确保越权/违规可追责。

#### Scenario: 越权被阻断
- **WHEN** 请求试图跨越 user_id/org_id 的隔离边界
- **THEN** 系统阻断访问并记录审计事件
- **AND** 审计记录不应包含不必要的敏感原文

### Requirement: 门禁验收（Gates & Acceptance）
系统 SHALL 定义可执行的验收口径，且未达标 MUST 阻断进入其所属门禁（Gate-1）。

#### Scenario: 门禁可执行且可阻断
- **WHEN** 该能力尝试进入发布/晋级/对外开放
- **THEN** 门禁检查得到明确通过/失败判定
- **AND** 失败 MUST 阻断并产出可行动的整改项
