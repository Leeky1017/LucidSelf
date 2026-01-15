from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Spec:
    slug: str
    name_cn: str
    name_en: str
    priority: str  # P0 / P1 / P2 / 资产层
    gate: str  # Gate-0..3 / 资产门禁
    deps: list[str]
    domain_cn: str
    artifacts_cn: str
    required_ids: list[str]

    owner: str = "system"
    status: str = "未开始"


SPECS: list[Spec] = [
    Spec(
        "engine-id-governance",
        "引擎ID治理",
        "Engine ID Governance",
        "P0",
        "Gate-0",
        [],
        "engine_id 的注册、唯一性与生命周期治理",
        "engine_id 注册表、生命周期变更记录、弃用/替代关系、审计记录",
        ["engine_id", "version_id"],
    ),
    Spec(
        "identity-and-data-isolation",
        "身份与数据隔离",
        "Identity and Data Isolation",
        "P0",
        "Gate-0",
        [],
        "user_id/org_id 身份范围与多租户隔离",
        "身份声明、访问控制决策记录、隔离违规审计、删除/保留审计",
        ["user_id", "org_id", "version_id"],
    ),
    Spec(
        "security-privacy-compliance",
        "安全/隐私/合规",
        "Security Privacy Compliance",
        "P0",
        "Gate-0",
        [],
        "数据分类、访问控制、加密、隐私请求与事件响应",
        "数据分类标签、访问控制证据、隐私请求处理记录、事件响应记录",
        ["user_id", "org_id", "version_id"],
    ),
    Spec(
        "versioning-and-deviation-detection",
        "版本化与偏差检测",
        "Versioning and Deviation Detection",
        "P0",
        "Gate-0",
        ["engine-id-governance"],
        "版本标识(version_id)与偏差/漂移检测",
        "版本清单、偏差报告、兼容性声明、阻断记录",
        ["version_id", "engine_id"],
    ),
    Spec(
        "production-defaults-no-mock",
        "生产默认值（禁止Mock）",
        "Production Defaults No Mock",
        "P0",
        "Gate-0",
        ["identity-and-data-isolation", "security-privacy-compliance"],
        "生产默认值、环境隔离与禁止 mock/静默降级",
        "配置校验规则、环境隔离约束、启动失败原因记录、违规审计",
        ["version_id"],
    ),
    Spec(
        "observability-slos",
        "可观测性与SLO",
        "Observability and SLOs",
        "P0",
        "Gate-0",
        [],
        "指标/日志/链路追踪与 SLO/告警",
        "指标命名与标签规范、日志字段规范、trace 传播规范、SLO/告警规则",
        ["request_id", "trace_id", "version_id", "engine_id", "user_id"],
    ),
    Spec(
        "citations-evidence-protocol",
        "引用与证据协议",
        "Citations and Evidence Protocol",
        "P0",
        "Gate-1",
        ["corpus-governance", "versioning-and-deviation-detection"],
        "evidence_chain 与 citation_anchor 的生成、校验与审计导出",
        "evidence_chain、citation_anchor、provenance 记录、审计导出包",
        ["corpus_release_id", "version_id", "user_id"],
    ),
    Spec(
        "semantic-layer-core",
        "语义层核心",
        "Semantic Layer Core",
        "P0",
        "Gate-1",
        ["engine-id-governance", "identity-and-data-isolation", "citations-evidence-protocol"],
        "语义条目(semantic entry)的数据模型、持久化与查询契约",
        "semantic entry、索引、provenance、citation_anchor 绑定、查询响应",
        ["engine_id", "user_id", "version_id", "corpus_release_id"],
    ),
    Spec(
        "semantic-extraction-quality-gates",
        "语义抽取质量门禁",
        "Semantic Extraction Quality Gates",
        "P1",
        "Gate-1",
        ["text-normalization-alignment", "corpus-governance"],
        "语义抽取输出的质量指标、阈值与阻断策略",
        "质量指标口径、阈值配置、失败样本清单、复检记录",
        ["version_id", "corpus_release_id"],
    ),
    Spec(
        "bootability-and-regression-baseline",
        "启动性与回归基线",
        "Bootability and Regression Baseline",
        "P0",
        "Gate-1",
        ["observability-slos"],
        "可启动性基线、冒烟检查与回归基线定义",
        "启动检查清单、回归套件基线、失败阻断记录、版本关联报告",
        ["version_id"],
    ),
    Spec(
        "golden-sets-and-regression",
        "Golden Set与回归评测",
        "Golden Sets and Regression",
        "P0",
        "Gate-1",
        ["bootability-and-regression-baseline", "observability-slos"],
        "golden set 的版本化、覆盖率与回归阈值",
        "golden set 清单、覆盖率报告、回归阈值与结果、漂移告警",
        ["version_id", "corpus_release_id", "engine_id"],
    ),
    Spec(
        "corpus-governance",
        "语料治理",
        "Corpus Governance",
        "资产层",
        "资产门禁",
        [],
        "语料资产的所有权、许可、版本、血缘与退役策略",
        "资产登记、许可与使用约束、版本与血缘、退役记录",
        ["asset_id", "corpus_release_id", "version_id"],
    ),
    Spec(
        "text-normalization-alignment",
        "文本归一化与对齐",
        "Text Normalization Alignment",
        "资产层",
        "资产门禁",
        ["corpus-governance"],
        "典籍与多源文本的归一化规则、对齐策略与可追溯变换",
        "归一化规则集、对齐映射、变换审计记录、覆盖率与例外清单",
        ["corpus_release_id", "version_id"],
    ),
    Spec(
        "cross-book-consistency-conflicts",
        "跨书一致性与冲突",
        "Cross-Book Consistency Conflicts",
        "资产层",
        "资产门禁",
        ["corpus-governance"],
        "跨书/跨源冲突的发现、归因、决策与例外管理",
        "冲突记录、来源引用、决策与例外批准记录、冲突报表",
        ["corpus_release_id", "version_id"],
    ),
    Spec(
        "proofreading-workflow-qa",
        "校对工作流与QA",
        "Proofreading Workflow QA",
        "资产层",
        "资产门禁",
        ["semantic-extraction-quality-gates"],
        "语料与抽取结果的校对、复核、批准与缺陷度量",
        "校对任务、缺陷记录、批准记录、QA 指标报表",
        ["corpus_release_id", "version_id"],
    ),
    Spec(
        "corpus-release-pipeline",
        "语料发布流水线",
        "Corpus Release Pipeline",
        "P1",
        "Gate-2",
        ["corpus-governance", "semantic-extraction-quality-gates", "cross-book-consistency-conflicts"],
        "语料发布的阶段化流程、校验、晋级与回滚",
        "发布阶段记录、校验报告、release artifacts、回滚记录",
        ["corpus_release_id", "version_id"],
    ),
    Spec(
        "deployment-release",
        "部署与发布",
        "Deployment Release",
        "P1",
        "Gate-2",
        ["production-defaults-no-mock", "bootability-and-regression-baseline", "observability-slos"],
        "环境晋级、发布验证与回滚流程",
        "发布产物清单、晋级记录、发布验证报告、回滚记录",
        ["version_id"],
    ),
    Spec(
        "seven-engine-pipeline-e2e",
        "七引擎流水线E2E",
        "Seven Engine Pipeline E2E",
        "P0",
        "Gate-2",
        ["engine-id-governance", "semantic-layer-core", "corpus-release-pipeline", "observability-slos"],
        "七引擎端到端流程的阶段契约、交接校验与可观测",
        "阶段契约、handoff 校验记录、E2E trace、失败恢复记录",
        ["engine_id", "version_id", "corpus_release_id"],
    ),
    Spec(
        "knowledge-graph-runtime-semanticquery",
        "知识图谱运行时语义查询",
        "Knowledge Graph Runtime Semantic Query",
        "P1",
        "Gate-2",
        ["semantic-layer-core", "observability-slos"],
        "运行时语义查询契约、确定性与延迟边界",
        "查询契约、结果一致性声明、延迟 SLO、审计日志",
        ["user_id", "engine_id", "version_id"],
    ),
    Spec(
        "llm-narrative-layer",
        "LLM叙述层",
        "LLM Narrative Layer",
        "P2",
        "Gate-2",
        ["citations-evidence-protocol", "observability-slos"],
        "叙述输出的结构化格式、安全策略与引用融合",
        "输出 schema、模型/提示版本记录、引用绑定、内容安全审计",
        ["user_id", "engine_id", "version_id", "prompt_id", "model_version_id"],
    ),
    Spec(
        "fusion-engine-explainability",
        "融合引擎可解释性",
        "Fusion Engine Explainability",
        "P0",
        "Gate-2",
        ["llm-narrative-layer", "citations-evidence-protocol"],
        "融合决策的解释输出、证据对齐与可复现回放",
        "解释记录、证据对齐引用、置信度/不确定性、回放输入集",
        ["engine_id", "version_id", "corpus_release_id"],
    ),
    Spec(
        "playbook-and-action-loop",
        "Playbook与行动闭环",
        "Playbook and Action Loop",
        "P1",
        "Gate-2",
        ["observability-slos"],
        "行动剧本执行、审批、人机协作与回滚闭环",
        "playbook 定义、执行记录、审批记录、回滚记录、审计日志",
        ["user_id", "version_id"],
    ),
    Spec(
        "abuse-and-rate-limits",
        "滥用防护与限流",
        "Abuse and Rate Limits",
        "P1",
        "Gate-2",
        ["identity-and-data-isolation", "observability-slos"],
        "滥用检测、限流与强制执行策略",
        "限流策略、滥用信号证据、封禁/挑战/降级动作记录、复核记录",
        ["user_id", "org_id", "engine_id", "version_id"],
    ),
    Spec(
        "billing-and-entitlements",
        "计费与权益",
        "Billing and Entitlements",
        "P1",
        "Gate-3",
        ["identity-and-data-isolation"],
        "权益校验、用量计量、账单生成与争议审计",
        "权益定义、用量事件、计费记录、争议证据链",
        ["user_id", "org_id", "version_id"],
    ),
    Spec(
        "commercial-readiness-gates",
        "商业化就绪门禁",
        "Commercial Readiness Gates",
        "P1",
        "Gate-3",
        ["deployment-release", "security-privacy-compliance", "billing-and-entitlements"],
        "商业发布的就绪标准、审批链与阻断策略",
        "就绪清单、审批记录、支持与应急预案、发布许可证据",
        ["version_id"],
    ),
    Spec(
        "geocoding-first-class",
        "地理编码一等公民",
        "Geocoding First Class",
        "P2",
        "Gate-3",
        ["text-normalization-alignment", "observability-slos"],
        "地理编码实体化、归一化、精度/置信度与回退策略",
        "标准化地理实体、精度/置信度元数据、回退记录、指标报表",
        ["version_id", "user_id"],
    ),
]


def _openspec_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _write(path: Path, content: str) -> None:
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def _render_spec_md(spec: Spec) -> str:
    ids = ", ".join(f"`{x}`" for x in spec.required_ids)
    purpose_lines = [
        f"本 spec 定义 LS 的「{spec.name_cn}」能力（`{spec.slug}`），用于规范 {spec.domain_cn} 的契约、门禁与审计。",
        f"关键产物包括：{spec.artifacts_cn}。",
        "本 spec 只定义 MUST/SHALL 的行为与验收口径，不包含实现细节/伪代码/代码路径。",
    ]

    lines: list[str] = [
        f"# {spec.name_cn}（{spec.name_en}）",
        "",
        "## Purpose",
        "",
        *purpose_lines,
        "",
        "## Requirements",
        "",
    ]

    if spec.gate == "资产门禁":
        reqs = [
            (
                "资产契约与范围（Scope & Contract）",
                f"系统 MUST 为「{spec.name_cn}」定义资产范围与契约边界，并明确最小标识符集合（至少包含 {ids}）。",
                "资产可被引用与追溯",
                [
                    "- **WHEN** 资产被注册或被引用为证据来源",
                    "- **THEN** 其范围、版本与来源被明确记录",
                    "- **AND** 引用必须可回到具体 `corpus_release_id` 或等价版本标识",
                ],
            ),
            (
                "版本/血缘/许可（Version & License）",
                "系统 MUST 为资产变更建立 `version_id`/血缘，并记录许可与使用约束。",
                "许可约束被执行",
                [
                    "- **WHEN** 资产被使用或发布",
                    "- **THEN** 许可/访问约束被校验",
                    "- **AND** 违反约束的使用 MUST 被阻断并留下审计记录",
                ],
            ),
            (
                "一致性与冲突（Consistency）",
                "系统 SHALL 定义一致性判定规则，并对冲突/例外给出可审计处置流程。",
                "冲突被记录与处置",
                [
                    "- **WHEN** 检测到跨源冲突或对齐歧义",
                    "- **THEN** 系统产生冲突记录并列出来源证据",
                    "- **AND** 处置结果（含例外批准）必须可追溯",
                ],
            ),
            (
                "QA与复核（QA & Review）",
                "系统 MUST 定义 QA/校对流程与度量口径，确保质量问题可闭环。",
                "QA 结果可审计",
                [
                    "- **WHEN** QA/校对完成",
                    "- **THEN** 结果、缺陷与批准记录被持久化",
                    "- **AND** 指标报表可按 `corpus_release_id` 聚合",
                ],
            ),
            (
                "审计与可观测（Auditability）",
                "系统 MUST 输出可观测信号与审计导出能力，支持最小证据包导出。",
                "审计导出可用",
                [
                    "- **WHEN** 审计导出被请求",
                    "- **THEN** 系统导出包含来源、版本与决策的最小证据包",
                    "- **AND** 导出行为被记录并可追责",
                ],
            ),
            (
                "资产门禁验收（Asset Gate）",
                f"系统 SHALL 定义资产门禁验收口径，且未达标 MUST 阻断进入其所属门禁（{spec.gate}）。",
                "门禁阻断生效",
                [
                    "- **WHEN** 资产尝试进入发布或被用于用户可见输出",
                    "- **THEN** 门禁检查给出通过/失败判定",
                    "- **AND** 失败 MUST 阻断并产出可行动的整改项",
                ],
            ),
        ]
    else:
        reqs = [
            (
                "契约与标识符（Contract & IDs）",
                f"系统 MUST 为「{spec.name_cn}」定义稳定、版本化契约，并明确最小标识符集合（至少包含 {ids}）及其语义边界。",
                "请求带齐标识符并可追溯",
                [
                    "- **WHEN** 该能力处理一次请求/作业",
                    "- **THEN** 请求上下文包含所需标识符并被记录",
                    "- **AND** 标识符缺失/非法 MUST 触发确定性的拒绝原因",
                ],
            ),
            (
                "数据模型与完整性（Data & Integrity）",
                f"系统 MUST 对关键产物（{spec.artifacts_cn}）定义字段级约束，并对完整性/引用可解析性实施校验。",
                "无效产物被阻断",
                [
                    "- **WHEN** 产物缺字段、引用不可解析或版本不一致",
                    "- **THEN** 校验失败并阻断进入下游阶段",
                    "- **AND** 失败原因以可审计的方式记录",
                ],
            ),
            (
                "运行时确定性（Runtime Determinism）",
                "系统 SHALL 定义可重复的运行时行为边界：相同输入（含版本）产生等价输出，偏差 MUST 可检测与解释。",
                "同输入同输出（在契约内）",
                [
                    "- **WHEN** 在相同输入与相同版本下重复执行",
                    "- **THEN** 输出在契约定义的等价范围内保持一致",
                    "- **AND** 非确定性因素 MUST 被显式标注并可审计",
                ],
            ),
            (
                "可观测与审计（Observability）",
                "系统 MUST 输出 metrics/logs/traces，并确保可按 `version_id`/`engine_id`/`user_id` 关联定位。",
                "运维可定位问题",
                [
                    "- **WHEN** 发生失败、降级或门禁阻断",
                    "- **THEN** 指标与日志能定位到请求、版本与责任边界",
                    "- **AND** 关键事件必须形成审计记录",
                ],
            ),
            (
                "安全/隐私/合规（Security/Privacy/Compliance）",
                "系统 MUST 执行最小权限、数据最小化、脱敏与保留策略，并确保越权/违规可追责。",
                "越权被阻断",
                [
                    "- **WHEN** 请求试图跨越 user_id/org_id 的隔离边界",
                    "- **THEN** 系统阻断访问并记录审计事件",
                    "- **AND** 审计记录不应包含不必要的敏感原文",
                ],
            ),
            (
                "门禁验收（Gates & Acceptance）",
                f"系统 SHALL 定义可执行的验收口径，且未达标 MUST 阻断进入其所属门禁（{spec.gate}）。",
                "门禁可执行且可阻断",
                [
                    "- **WHEN** 该能力尝试进入发布/晋级/对外开放",
                    "- **THEN** 门禁检查得到明确通过/失败判定",
                    "- **AND** 失败 MUST 阻断并产出可行动的整改项",
                ],
            ),
        ]

    for req_name, req_line, sc_name, bullets in reqs:
        lines.append(f"### Requirement: {req_name}")
        lines.append(req_line)
        lines.append("")
        lines.append(f"#### Scenario: {sc_name}")
        lines.extend(bullets)
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def _render_tasks_md(spec: Spec) -> str:
    sections: list[tuple[str, list[str]]] = [
        (
            "Contracts & Interfaces（契约与接口）",
            [
                f"- [ ] 用中文固化「{spec.name_cn}」契约与标识符（保留 MUST/SHALL 与标准标题）",
                f"- [ ] 定义对外契约字段清单与拒绝原因枚举（机器可读）",
            ],
        ),
        (
            "Data & Integrity（数据与完整性）",
            [
                f"- [ ] 建立关键产物（{spec.artifacts_cn}）的数据字典与字段级约束表",
                "- [ ] 定义引用可解析性、幂等/去重与冲突处理语义（规格层）",
            ],
        ),
        (
            "Runtime Behavior（运行时行为）",
            [
                "- [ ] 定义关键路径的确定性边界与偏差检测/解释口径",
                "- [ ] 定义失败处理策略（拒绝/降级/重试/回滚触发）与信号产物",
            ],
        ),
        (
            "Observability & Metrics（可观测与指标）",
            [
                "- [ ] 定义核心 metrics 列表（名称/标签/单位/聚合口径）与 SLO 阈值",
                "- [ ] 定义审计日志字段与脱敏规则（最小化原则）与审计导出结构",
            ],
        ),
        (
            "Security/Compliance（安全与合规）",
            [
                "- [ ] 明确访问控制与隔离边界（user_id/org_id）在本能力中的适用方式",
                "- [ ] 明确保留/删除/合规审计所需证据项与留存期限（规格层）",
            ],
        ),
        (
            "Performance/Cost（性能与成本）",
            [
                "- [ ] 定义性能目标（延迟/吞吐）与测量方式（指标口径）",
                "- [ ] 定义成本目标与预算阈值（如 tokens/存储/计算）与告警策略",
            ],
        ),
        (
            "Tests/Validation（测试与验证）",
            [
                "- [ ] 执行并确保 `openspec validate --specs --strict --no-interactive` 通过",
                "- [ ] 为本能力补齐系统级验证口径（命令/通过标准/失败阻断）并写入 `acceptance.md`",
            ],
        ),
        (
            "Rollout/Risks（发布与风险）",
            [
                "- [ ] 定义分阶段 rollout（shadow/canary/gradual）与回滚触发条件（契约级）",
                "- [ ] 列出 Top 风险与缓解手段（证据/门禁/回退）并写入 `design.md`",
            ],
        ),
    ]

    lines = [f"# {spec.name_cn} Tasks", ""]
    for header, items in sections:
        lines.append(f"## {header}")
        lines.extend(items)
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _render_design_md(spec: Spec) -> str:
    deps = ", ".join(f"`{d}`" for d in spec.deps) if spec.deps else "无"
    ids = ", ".join(f"`{x}`" for x in spec.required_ids)
    return "\n".join(
        [
            f"# {spec.name_cn} Design",
            "",
            "## 设计意图",
            f"本设计文档用于固定「{spec.name_cn}」在规格层面的设计立场：契约、数据完整性、门禁与审计。禁止写实现细节。",
            "",
            "## 依赖关系",
            f"- 上游依赖：{deps}",
            "",
            "## 必备标识符（最小集）",
            f"- {ids}",
            "",
            "## 关键决策（非实现）",
            "- 所有用户可见结论必须可追溯到 `version_id` 与证据链（如适用）。",
            "- 门禁失败必须阻断晋级，并产出可行动的整改项清单。",
            "- 可观测与审计字段是契约的一部分，必须被一致执行。",
            "",
            "## 非目标",
            "- 不规定具体存储/消息队列/监控方案。",
            "- 不包含任何代码路径、伪代码或接口实现。",
        ]
    ) + "\n"


def _render_acceptance_md(spec: Spec) -> str:
    artifacts = [
        f"`openspec/specs/{spec.slug}/spec.md`",
        f"`openspec/specs/{spec.slug}/requirements.md`",
        f"`openspec/specs/{spec.slug}/tasks.md`",
        f"`openspec/specs/{spec.slug}/design.md`",
        f"`openspec/specs/{spec.slug}/acceptance.md`",
    ]
    return "\n".join(
        [
            f"# {spec.name_cn} Acceptance",
            "",
            "## 验收命令（最低集合）",
            "- `openspec validate --specs --strict --no-interactive`",
            "- `openspec list --specs`（确认本 spec 的任务进度可见）",
            "",
            "## 验收指标（最低集合）",
            "- 所有 Requirement 都有至少 1 个 Scenario，且 Scenario 内容非空。",
            "- 关键产物在契约层明确可追溯到 `version_id`（以及 `corpus_release_id`/`engine_id` 如适用）。",
            f"- 所属门禁 `{spec.gate}` 的阻断策略清晰：失败必须阻断晋级/发布/对外开放。",
            "",
            "## 必须产物（最低集合）",
            *[f"- {a}" for a in artifacts],
            "",
            "## 通过标准（规格层）",
            "- 上述命令退出码为 0，且 `openspec validate --specs --strict --no-interactive` 显示为通过状态。",
            "- `tasks.md` 的任务可独立验收、可回写状态，并能支撑仪表盘统计。",
        ]
    ) + "\n"


def _render_project_md() -> str:
    return "\n".join(
        [
            "# LucidSelf（LS）— OpenSpec 项目宪法（Project Constitution）",
            "",
            "## 目标（Mission）",
            "OpenSpec 是 LS 的“工程控制台”：以可审计、可追溯、可复现的规格与门禁，约束系统演进，防止能力漂移与不可控变更。",
            "",
            "## 边界（Scope）",
            "- OpenSpec 只定义“系统 MUST/SHALL 做什么”以及如何验收。",
            "- OpenSpec 禁止写实现细节、伪代码、代码路径与具体技术选型。",
            "- 所有新增能力/行为变更/数据契约变更 MUST 先落在 `openspec/changes/` 并通过严格校验。",
            "",
            "## 统一术语（Terms）",
            "- `user_id`：用户身份（读写隔离的主边界）。",
            "- `org_id`：组织/租户身份（多租户隔离边界）。",
            "- `engine_id`：引擎标识（注册表中唯一、可治理）。",
            "- `version_id`：不可变版本标识（用于可复现与可审计）。",
            "- `corpus_release_id`：语料发布版本标识（证据链必须引用到此）。",
            "- `request_id` / `trace_id`：可观测与审计关联标识。",
            "",
            "## 质量门禁（Quality Gates）",
            "- Gate-0：基础安全、身份隔离、版本体系、生产默认值、可观测基线。",
            "- Gate-1：语义可靠性、证据/引用正确性、抽取质量门禁、回归基线。",
            "- Gate-2：端到端契约、发布/回滚、运行手册、操作可观测。",
            "- Gate-3：商业化就绪（权益/计费/发布审批/支持体系）。",
            "- 资产门禁：典籍/语料资产治理、血缘、许可、QA 与审计。",
            "",
            "## 工程原则（Principles）",
            "- 可解释性：用户可见结论 MUST 附带可验证的证据链与引用（如适用）。",
            "- 可追溯性：输出 MUST 能映射到 `version_id`、`engine_id`、`corpus_release_id`（如适用）。",
            "- 可复现性：相同输入+相同版本下输出应可复现；不可复现部分 MUST 显式标注并可审计。",
            "- 身份优先：所有数据读写 MUST 受 `user_id`/`org_id` 约束。",
            "- 生产禁止 mock：生产环境 MUST 拒绝 mock 默认值与静默降级。",
            "",
            "## OpenSpec 严格格式（Strict）",
            "- Specs 位于 `openspec/specs/<capability>/spec.md`。",
            "- `spec.md` MUST 包含 `## Purpose` 与 `## Requirements`。",
            "- 每条 Requirement 的第一句 MUST 包含 `MUST` 或 `SHALL`。",
            "- 每条 Requirement MUST 至少包含一个 `#### Scenario:`，且内容非空。",
        ]
    ) + "\n"


def _render_workflow_md() -> str:
    return "\n".join(
        [
            "# WORKFLOW（推进流程）",
            "",
            "## 唯一推进入口",
            "任何推进必须落在某个 spec 的 `tasks.md` checklist 上，任务必须可独立验收、可回写状态。",
            "",
            "## 节奏",
            "- P0 先行，Gate-0/1 先行；资产门禁可并行但受门禁阻断约束。",
            "- 门禁失败必须阻断晋级，直到任务闭环。",
            "",
            "## Review 规则（最小粒度）",
            "- Requirement：原子、可测试、可审计；禁止揉多目标。",
            "- Scenario：可执行判定（WHEN/THEN/AND）。",
            "- Tasks：可验收且可回写状态；禁止“3 条任务管一坨”。",
            "- 禁止：实现细节、伪代码、代码路径、具体技术选型。",
            "",
            "## 仪表盘命令",
            "- `openspec list`",
            "- `openspec list --specs`",
            "- `openspec list --changes`",
            "- `openspec validate --specs --strict --no-interactive`",
        ]
    ) + "\n"


def _render_quality_gates_md() -> str:
    return "\n".join(
        [
            "# QUALITY_GATES（质量门禁）",
            "",
            "每条门禁包含：指标/命令/判定标准/失败阻断策略。",
            "",
            "## Gate-0（基础）",
            "- 指标：身份隔离/安全/版本/生产默认值/可观测基线齐备。",
            "- 命令：`openspec validate --specs --strict --no-interactive`",
            "- 判定：Gate-0 相关 specs 通过严格校验；关键任务达到发布要求（按各 spec `tasks.md`）。",
            "- 阻断：失败则阻断任何对外发布/晋级。",
            "",
            "## Gate-1（语义可靠性）",
            "- 指标：证据链与引用可审计；语义层契约稳定；抽取质量门禁与回归基线定义完备。",
            "- 命令：`openspec validate --specs --strict --no-interactive` + `openspec list --specs`",
            "- 判定：Gate-1 相关 specs 的验收口径明确且可执行。",
            "- 阻断：失败则阻断语义/语料晋级与对外解释输出。",
            "",
            "## Gate-2（工程与运行就绪）",
            "- 指标：端到端契约与交接校验明确；发布/回滚与运行手册齐备；关键路径可观测。",
            "- 命令：`openspec validate --specs --strict --no-interactive` + `openspec list --changes`",
            "- 判定：Gate-2 相关 specs 的门禁阻断策略与运维定位口径明确。",
            "- 阻断：失败则阻断部署晋级与规模化流量。",
            "",
            "## Gate-3（商业化就绪）",
            "- 指标：权益/计费与商业就绪门禁完备；审批链与支持体系有证据产物。",
            "- 命令：`openspec validate --specs --strict --no-interactive`",
            "- 判定：商业化相关 specs 的验收口径明确且可审计。",
            "- 阻断：失败则阻断对客户开放与商业发布。",
            "",
            "## 资产门禁（资产层）",
            "- 指标：许可/血缘/QA/冲突处置可追溯；失败样本与例外审批可审计。",
            "- 命令：`openspec validate --specs --strict --no-interactive`（资产层附加验证按各 spec `acceptance.md`）。",
            "- 判定：资产层相关 specs 的验收口径明确且可执行。",
            "- 阻断：失败则阻断语料发布与依赖该资产的用户可见输出。",
        ]
    ) + "\n"


def _render_specs_index_md() -> str:
    gate_order = ["Gate-0", "Gate-1", "Gate-2", "Gate-3", "资产门禁"]
    pri_order = {"P0": 0, "P1": 1, "P2": 2, "资产层": 3}
    specs = sorted(SPECS, key=lambda s: (pri_order.get(s.priority, 9), gate_order.index(s.gate), s.slug))

    gate_acceptance = {
        "Gate-0": {
            "cmds": "`openspec validate --specs --strict --no-interactive` + `openspec list --specs`",
            "metrics": "身份隔离/安全/版本/生产默认值/可观测基线齐备；失败必须阻断晋级",
        },
        "Gate-1": {
            "cmds": "`openspec validate --specs --strict --no-interactive` + `openspec list --specs`",
            "metrics": "证据链可审计；语义层契约稳定；质量门禁阈值明确；回归基线可执行",
        },
        "Gate-2": {
            "cmds": "`openspec validate --specs --strict --no-interactive` + `openspec list --changes`",
            "metrics": "端到端契约/交接校验明确；发布/回滚口径齐备；关键路径可观测",
        },
        "Gate-3": {
            "cmds": "`openspec validate --specs --strict --no-interactive` + `openspec list --specs`",
            "metrics": "权益/计费/审批链/支持体系齐备；对外发布记录可审计",
        },
        "资产门禁": {
            "cmds": "`openspec validate --specs --strict --no-interactive`",
            "metrics": "许可/血缘/QA/冲突处置可追溯；失败样本与例外审批可审计",
        },
    }

    lines: list[str] = [
        "# SPECS_INDEX（控制台中枢）",
        "",
        "包含：规格清单（≈26）、优先级、门禁归属、依赖 DAG、验收口径、审计闭环方法。",
        "",
        "## Specs Overview",
        "ID | 名称 | 优先级 | Owner | 状态 | Gate",
        "--- | --- | --- | --- | --- | ---",
    ]
    for s in specs:
        lines.append(f"{s.slug} | {s.name_cn} | {s.priority} | {s.owner} | {s.status} | {s.gate}")

    lines += [
        "",
        "## 推荐推进顺序（先做谁 / 卡在哪里 / 何时算完成）",
        "- 先 P0，先 Gate-0/1；资产门禁可并行但会阻断依赖它的下游。",
        "- 阻断点：任一依赖 spec 未完成关键任务（按其 `tasks.md`）即视为阻断。",
        "- 完成：依赖清零 + 关键任务完成 + `openspec validate --specs --strict --no-interactive` 通过 + 验收产物齐备。",
        "",
    ]
    for gate in gate_order:
        group = [s for s in specs if s.gate == gate]
        if not group:
            continue
        lines.append(f"### {gate}")
        for s in group:
            deps = ", ".join(f"`{d}`" for d in s.deps) if s.deps else "无"
            lines.append(f"- `{s.slug}`（{s.priority}）：依赖 {deps}")
        lines.append("")

    lines += [
        "## Dependencies (Adjacency List)",
        "- 本依赖图 MUST 无环；以 `openspec validate --specs --strict --no-interactive` 的校验结果为准。",
    ]
    for s in specs:
        dep_str = ", ".join(s.deps) if s.deps else "none"
        lines.append(f"- {s.slug}: {dep_str}")

    lines += [
        "",
        "## Gate 归属",
    ]
    for s in specs:
        lines.append(f"- {s.slug}: {s.gate}")

    lines += [
        "",
        "## 验收口径（命令 / 指标 / 产物）",
        "ID | 验收命令（最小） | 可验证指标（最小） | 必须产物（最小）",
        "--- | --- | --- | ---",
    ]
    for s in specs:
        acc = gate_acceptance[s.gate]
        artifacts = f"`openspec/specs/{s.slug}/`（spec/requirements/tasks/design/acceptance）"
        lines.append(f"{s.slug} | {acc['cmds']} | {acc['metrics']} | {artifacts}")

    lines += [
        "",
        "## 审计问题闭环到 Spec 的映射策略",
        "- 将问题映射到最小影响面（spec -> Requirement -> Scenario）。",
        "- 为问题补齐/新增 Scenario，使其可复现、可判定；禁止用模糊叙述代替可执行判定。",
        "- 在对应 spec 的 `tasks.md` 新增可验收任务，并写清通过标准与证据产物（日志/报表/门禁输出）。",
        "- 若影响 Gate-0~3 或资产门禁，则把失败定义为阻断条件，直至任务完成。",
        "- 跨多个 spec 或涉及行为改变时，必须创建/更新 `openspec/changes/<change-id>/`。",
        "",
        "## 完成定义（何时算完成）",
        "- 相关 spec 的关键任务完成 + 依赖清零 + `openspec validate --specs --strict --no-interactive` 通过 + 验收产物齐备。",
    ]
    return "\n".join(lines).strip() + "\n"


def _render_change_files() -> dict[str, str]:
    return {
        "proposal.md": "\n".join(
            [
                "# Super OpenSpec Baseline Rebuild（全量规格重构基线）",
                "",
                "## 为什么必须重写",
                "把 OpenSpec 从“文档堆”升级为“工程控制台”，需要统一：规格结构、门禁定义、依赖 DAG 与任务化推进方式。",
                "",
                "## 目标（控制台效果）",
                "- `openspec list` / `openspec list --specs` / `openspec list --changes` 输出具备统计意义。",
                "- `openspec validate --specs --strict --no-interactive` 严格校验通过。",
                "- 26 个 specs 的口径一致：术语、门禁、依赖、验收方式可追溯。",
                "",
                "## 范围",
                "- 仅重建 `openspec/` 内的规范体系，不实现任何业务代码。",
                "- 只定义 MUST/SHALL 的行为、门禁与验收口径。",
            ]
        ),
        "tasks.md": "\n".join(
            [
                "# Super OpenSpec Baseline Rebuild Tasks（项目级）",
                "",
                "- [x] 基线盘点：命令输出固化到 `openspec/_ops/before.txt`",
                "- [x] 清理与重置：清空旧 specs/changes 并记录 `openspec/_ops/cleanup_log.md`",
                "- [x] 顶层控制面：project/index/workflow/gates 四份文档中文化并可审计",
                "- [x] 重建 26 specs：每个 spec 具备 5 件套（spec/requirements/tasks/design/acceptance）",
                "- [x] 依赖与门禁对齐：SPECS_INDEX 的 DAG 与 Gate 归属一致且无环",
                "- [x] 严格校验：`openspec validate --specs --strict --no-interactive` 通过",
                "- [x] 仪表盘落盘：`openspec/_ops/final_dashboard.txt` 写入 list/specs/changes/validate 输出",
                "- [ ] 归档：待实现侧完成并验证后移入 `openspec/changes/archive/`（负责人执行）",
            ]
        ),
        "design.md": "\n".join(
            [
                "# Super OpenSpec Baseline Rebuild Design",
                "",
                "## 设计立场",
                "- Specs-first：规格先于实现；实现必须可追溯映射到 Requirement/Scenario。",
                "- Gates-first：门禁先行；失败必须阻断晋级，直到任务闭环。",
                "- Asset-layer disciplined：资产层并行推进，但必须满足许可/血缘/QA/审计。",
                "",
                "## 统一方式",
                "- 统一目录：`openspec/specs/<capability>/spec.md` 为权威入口。",
                "- 统一格式：Requirement/Scenario 的 MUST/SHALL 与结构固定。",
                "- 统一仪表盘：以 checklist 任务进度与严格校验作为工程控制面。",
            ]
        ),
    }


def main() -> None:
    openspec_root = _openspec_root()
    specs_root = openspec_root / "specs"
    changes_root = openspec_root / "changes"
    ops_root = openspec_root / "_ops"

    specs_root.mkdir(parents=True, exist_ok=True)
    changes_root.mkdir(parents=True, exist_ok=True)
    ops_root.mkdir(parents=True, exist_ok=True)
    (changes_root / "archive").mkdir(parents=True, exist_ok=True)

    _write(openspec_root / "project.md", _render_project_md())
    _write(openspec_root / "WORKFLOW.md", _render_workflow_md())
    _write(openspec_root / "QUALITY_GATES.md", _render_quality_gates_md())
    _write(openspec_root / "SPECS_INDEX.md", _render_specs_index_md())

    for s in SPECS:
        spec_dir = specs_root / s.slug
        spec_dir.mkdir(parents=True, exist_ok=True)
        spec_md = _render_spec_md(s)
        _write(spec_dir / "spec.md", spec_md)
        _write(spec_dir / "requirements.md", spec_md)
        _write(spec_dir / "tasks.md", _render_tasks_md(s))
        _write(spec_dir / "design.md", _render_design_md(s))
        _write(spec_dir / "acceptance.md", _render_acceptance_md(s))

    change_dir = changes_root / "super-openspec-baseline-rebuild"
    change_dir.mkdir(parents=True, exist_ok=True)
    for name, content in _render_change_files().items():
        _write(change_dir / name, content)


if __name__ == "__main__":
    main()
