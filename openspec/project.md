# LucidSelf（LS）— OpenSpec 项目宪法（Project Constitution）

## 目标（Mission）
OpenSpec 是 LS 的“工程控制台”：以可审计、可追溯、可复现的规格与门禁，约束系统演进，防止能力漂移与不可控变更。

## 边界（Scope）
- OpenSpec 只定义“系统 MUST/SHALL 做什么”以及如何验收。
- OpenSpec 禁止写实现细节、伪代码、代码路径与具体技术选型。
- 所有新增能力/行为变更/数据契约变更 MUST 先落在 `openspec/changes/` 并通过严格校验。

## 统一术语（Terms）
- `user_id`：用户身份（读写隔离的主边界）。
- `org_id`：组织/租户身份（多租户隔离边界）。
- `engine_id`：引擎标识（注册表中唯一、可治理）。
- `version_id`：不可变版本标识（用于可复现与可审计）。
- `corpus_release_id`：语料发布版本标识（证据链必须引用到此）。
- `request_id` / `trace_id`：可观测与审计关联标识。

## 质量门禁（Quality Gates）
- Gate-0：基础安全、身份隔离、版本体系、生产默认值、可观测基线。
- Gate-1：语义可靠性、证据/引用正确性、抽取质量门禁、回归基线。
- Gate-2：端到端契约、发布/回滚、运行手册、操作可观测。
- Gate-3：商业化就绪（权益/计费/发布审批/支持体系）。
- 资产门禁：典籍/语料资产治理、血缘、许可、QA 与审计。

## 工程原则（Principles）
- 可解释性：用户可见结论 MUST 附带可验证的证据链与引用（如适用）。
- 可追溯性：输出 MUST 能映射到 `version_id`、`engine_id`、`corpus_release_id`（如适用）。
- 可复现性：相同输入+相同版本下输出应可复现；不可复现部分 MUST 显式标注并可审计。
- 身份优先：所有数据读写 MUST 受 `user_id`/`org_id` 约束。
- 生产禁止 mock：生产环境 MUST 拒绝 mock 默认值与静默降级。

## OpenSpec 严格格式（Strict）
- Specs 位于 `openspec/specs/<capability>/spec.md`。
- `spec.md` MUST 包含 `## Purpose` 与 `## Requirements`。
- 每条 Requirement 的第一句 MUST 包含 `MUST` 或 `SHALL`。
- 每条 Requirement MUST 至少包含一个 `#### Scenario:`，且内容非空。
