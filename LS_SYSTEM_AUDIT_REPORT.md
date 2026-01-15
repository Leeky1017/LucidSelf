# LS 系统代码审计报告（LucidSelf / LS）

> 审计对象：`/home/leeky/work/LucidSelf`  
> 审计日期：2025-12-23  
> 审计身份：代码审计专家（只读审计，不修改任何现有代码/配置）  
> 交付物：本文件 `LS_SYSTEM_AUDIT_REPORT.md`

---

## 0. 四问直答（结论摘要）

### 0.1 系统本质：LS 到底做什么？核心价值主张是什么？

LS（LucidSelf）定位为“个人自注 / 长期个人叙事管理系统”，不是传统算命/占星 App，而是把命理×梦境×事件的长期自我认知沉淀成可版本化、可追溯、可解释的叙事与洞察体系（`README.md:9`）。其核心价值主张由 README 明确给出：可解释推理（证据链可追溯典籍原文）、可追溯版本（像 Git 管理“自我认知史”）、持续校准（基于反馈个性化）、跨域互文（命理×梦境×现实事件交叉验证）（`README.md:11`、`README.md:12`、`README.md:13`、`README.md:14`）。

在工程实现上，系统主链路以 L1-L5 分层编排：L1 计算因子（FactorMatrix）→ L3 规则推理（RuntimeRuleResult）→ L4 融合（FusionResult）→ L5 LLM 叙事（可选）→ API 输出（`backend/pipeline/orchestrator.py:1`、`backend/pipeline/orchestrator.py:7`、`backend/pipeline/orchestrator.py:10`）。

### 0.2 当前状态：已实现哪些功能？质量如何？覆盖率多少？

已实现（按层）：
- **L1**：已存在 6 个 Calculator（bazi/ziwei/yijing/astro/tarot/dream，目录可见 `backend/calculators/*`）。但在线 Pipeline 仅实际接入 4 个（bazi/astro/dream/tarot）（`backend/pipeline/orchestrator.py:272`、`backend/pipeline/orchestrator.py:286`、`backend/pipeline/orchestrator.py:293`）。
- **L3**：规则引擎、装饰器注册、批执行、规则 codegen 与生成规则模块链路已落地（`backend/rules/engine.py:47`、`backend/pipeline/orchestrator.py:120`、`scripts/codegen/rule_generator.py:70`）。数据侧 `data/rules/generated/**.jsonl` 显示生成规则规模约 4993 条（JSONL 行数，见附录命令统计）。
- **L4**：FusionEngine（权重、主题、交叉验证、证据链、冲突）实现完整且有较强测试覆盖（`backend/integration/fusion_engine.py:75`）。
- **L5**：TOON v2 序列化与 Orchestrator 已实现，且当存在 raw_factors 时优先走 v2（`backend/core/llm/toon_serializer.py:498`、`backend/core/llm/orchestrator.py:300`）。
- **API/前后端**：FastAPI 路由结构齐全（`backend/api/main.py:32`），前端为 Next.js（`frontend/package.json:10`、`frontend/package.json:13`）。但当前后端 **无法干净启动/全量 pytest 无法收集**：Playbook 包初始化导入了缺失文件 `backend/services/playbook/generator.py`（`backend/services/playbook/__init__.py:11`），导致 `pytest` 在收集阶段即中断（见“问题清单 / Blocker”）。

质量与覆盖（以“可验证证据”为准）：
- **测试现状**：  
  - `backend/integration/tests`：73 passed（命令输出见附录）。  
  - `backend/rules/tests`：146 passed, 1 skipped（命令输出见附录）。  
  - `backend/pipeline/tests/test_orchestrator.py`：1 failed（测试与实现签名漂移，`backend/pipeline/tests/test_orchestrator.py:135`；实现侧解包点 `backend/pipeline/orchestrator.py:274`）。  
  - `backend/calculators`：ziwei/astro/yijing 测试通过；bazi/tarot/dream 各有 1 条性质测试失败（命名规范/断言口径问题，见问题清单）。
  - **全量 `pytest -q` 无法运行**：收集期即报 `ModuleNotFoundError: backend.services.playbook.generator`（由 `backend/services/playbook/__init__.py:11` 触发）。
- **覆盖率现状**：存在 `.coverage` 文件，但当前 coverage report 仅覆盖 `backend/integration/*` 范围（TOTAL 94%），不能代表系统整体覆盖率（见附录 coverage 输出）。
- **Calculator Golden 覆盖矩阵**：`coverage_matrix_report.json` 显示 bazi/ziwei/yijing 未达到用例门槛（bazi 25<50；yijing 0<64）（`coverage_matrix_report.json:9`、`coverage_matrix_report.json:12`、`coverage_matrix_report.json:79`、`coverage_matrix_report.json:82`）。

### 0.3 规划差距：spec 规划了什么？哪些已落地？哪些待完成？

结论（按 `.kiro/specs` 主规格 + `archive` 规格汇总）：
- **已落地（主干）**：L4 Fusion（`.kiro/specs/layer4-fusion/*`）在代码中可见完整实现（`backend/integration/fusion_engine.py:75`）；Pipeline 链路修复中的“引擎 ID 标准化、raw_factors 输出、TOON v2、INS 行”已落地（`.kiro/specs/pipeline-link-fix/requirements.md:75`、`backend/core/constants/engines.py:24`、`backend/pipeline/orchestrator.py:195`、`backend/pipeline/orchestrator.py:69`、`backend/core/llm/toon_serializer.py:498`）。
- **部分落地/链路断流**：spec 明确系统包含 7 个体系（`bazi/astro/ziwei/tarot/dream/yijing/psych`）（`.kiro/specs/pipeline-link-fix/requirements.md:14`），但在线 Pipeline L1 仅接入 4 个（`backend/pipeline/orchestrator.py:272`、`backend/pipeline/orchestrator.py:293`），TOON v2 虽支持 ziwei/yijing 块（`backend/core/llm/toon_serializer.py:523`），但 raw_factors 侧不会产生对应输入 → LLM 上下文缺失。
- **未落地（核心缺口）**：跨书知识图谱 spec 要求“向 FusionEngine 提供只读 SemanticQuery 接口”（`.kiro/specs/archive/cross-book-knowledge-graph/requirements.md:5`、`.kiro/specs/archive/cross-book-knowledge-graph/requirements.md:11`），但代码仅存在离线 CLI/构建工具（`scripts/knowledge_graph_builder/cli.py:343`），运行期 FusionEngine 未接入查询服务（`backend/integration/fusion_engine.py:95`）。
- **与 spec/文档不一致**：Layer 5 tasks 声称 Playbook Generator 文件存在（`.kiro/specs/layer5-application/tasks.md:20`、`.kiro/specs/pipeline-link-fix/tasks.md:38`），但仓库中 `backend/services/playbook/generator.py` 缺失，已造成运行与测试阻断（`backend/services/playbook/__init__.py:11`）。

### 0.4 商业级差距：距离生产级/商业级系统还差什么？

以“生产可运行 + 数据可靠 + 质量可回归 + 知识可追溯”为标准，当前存在显著商业级差距：
- **可运行性/CI 阻断**：缺失模块导致 API/测试无法全量启动与回归（`backend/services/playbook/__init__.py:11`）。
- **数据与身份隔离风险**：梦境写入的 `user_id` 被设置为 `day_master`（命理字段），存在多用户污染与合规风险（`backend/api/routes/dream.py:247`、`backend/api/routes/dream.py:251`）。
- **默认行为不符合生产**：核心 `/api/v1/analyze` 默认走 Mock（`USE_REAL_PIPELINE=false`）（`backend/api/routes/analyze.py:30`、`backend/api/routes/analyze.py:151`）。
- **契约与命名体系治理缺口**：engine_id 在 contracts/registry/runtime 三套风格并存（下划线/连字符/`*_rule_engine`），且 contracts 的 ID 正则不允许连字符（`backend/core/contracts/base.py:18`），与当前实际 engine_id（`bazi-calculator`）不一致（`backend/core/constants/engines.py:24`、`backend/calculators/bazi/models.py:1320`、`data/engines/registry.json:3`）。
- **知识工程质量不稳**：语义层生成物存在明显字段空置与 `factor_refs` 污染（`backend/semantics/sanming/smth_v1.0.0_壬水_阳水之生死与象_001.py:45`、`backend/semantics/sanming/smth_v1.0.0_壬水_阳水之生死与象_001.py:47`、`backend/semantics/astrological_houses/ah_v1.0.0_house_1___self_identity__ascen_001.py:65`、`backend/semantics/astrological_houses/ah_v1.0.0_house_1___self_identity__ascen_001.py:70`），会直接削弱“可解释推理/可追溯典籍”的核心卖点。

---

## 1. 审计范围与方法

### 1.1 审计范围

覆盖以下内容源与代码域：
- 规格与规范：`.kiro/specs/**`、`.kiro/specs/archive/**`、`.kiro/docs/**`、`docs/**`
- 运行期主链路：`backend/pipeline/**`、`backend/rules/**`、`backend/integration/**`、`backend/core/llm/**`、`backend/api/**`
- 离线知识工程：`scripts/**`、`data/**`、`典籍/**`
- 前端对齐：`frontend/**`（仅审计 API 对齐与调用形态）

### 1.2 方法与证据标准

- **不假设路径**：所有模块位置均通过目录遍历与 `rg` 搜索确认。
- **证据要求**：所有问题点在“问题清单”中均提供 **具体文件路径 + 行号**（以 `nl -ba` 为准）。
- **可执行验证**：对关键模块运行了局部测试（pytest）与局部 coverage report（详见附录）。

---

## 2. 系统蓝图（架构图 / 数据流 / 模块清单）

### 2.1 系统定位与价值主张（产品层）

- “长期个人叙事管理系统”定位：`README.md:9`
- “可解释推理、证据链溯源典籍原文”：`README.md:11`
- “像 Git 一样版本管理自我认知史”：`README.md:12`、`README.md:378`
- “跨域互文：命理×梦境×现实事件”：`README.md:14`

### 2.2 在线链路（运行时：L1-L5）

Pipeline 编排在 `backend/pipeline/orchestrator.py` 明确给出 L1-L5 流程（`backend/pipeline/orchestrator.py:1`、`backend/pipeline/orchestrator.py:7`）。

```mermaid
flowchart LR
  U[User Input] --> API[FastAPI Routes]
  API --> P[Pipeline.execute]
  P --> L1[L1 Calculators\n(Bazi/Astro/Dream/Tarot...)]
  L1 --> FM[FactorMatrix[]]
  FM --> L3[L3 RuleEngine.execute_batch]
  L3 --> RR[engine_id -> RuntimeRuleResult[]]
  RR --> L4[L4 FusionEngine.fuse_results]
  L4 --> FR[FusionResult]
  FR -->|optional| L5[L5 NarrativeGenerator / LLM Orchestrator]
  L5 --> OUT[Narrative + Disclaimer]
  FR --> OUT2[API Response]
```

关键实现锚点：
- PipelineOutput 增加 raw_factors（供 TOON v2）：`backend/pipeline/orchestrator.py:69`、`backend/pipeline/orchestrator.py:81`
- 引擎 ID 标准化：`backend/pipeline/orchestrator.py:195`（使用 `backend/core/constants/engines.py:97`）
- L4 融合组件组合：`backend/integration/fusion_engine.py:95`、`backend/integration/fusion_engine.py:108`
- TOON v2 序列化与 INS 行：`backend/core/llm/toon_serializer.py:498`、`backend/core/llm/toon_serializer.py:545`
- Orchestrator 在 raw_factors 存在时优先走 v2：`backend/core/llm/orchestrator.py:300`

### 2.3 离线知识工程链路（典籍 → 因子本体/逻辑链/规则/图谱）

当前仓库中离线链路较完整，主要由 `scripts/**` 驱动，数据落到 `data/**` 与 `backend/generated/**`。

```mermaid
flowchart TB
  MD[典籍 Markdown/资料\n典籍/**] --> FE[scripts/factor_extractor\n提取 new_candidate]
  FE --> CAND[data/factor_ontology/candidates/*]
  CAND --> FC[scripts/factor_extractor/certify\n认证/分配ID]
  FC --> CERT[data/factor_ontology/certified/*]
  MD --> STG[data/schema_staging/*\n(snippets/relations/...)]
  STG --> LCB[scripts/logic_chain_builder\n生成 LogicChain]
  LCB --> LC[data/logic_chains/*.yaml]
  LC --> RC[scripts/rule_converter\nLogicChain -> rules JSONL]
  RC --> RJSON[data/rules/**.jsonl\n+ data/rules/generated/**.jsonl]
  RJSON --> CG[scripts/codegen/rule_generator\nJSON -> Python rules]
  CG --> PR[backend/generated/rules/*.py]
  LC --> KGB[scripts/knowledge_graph_builder\n(离线)构建/验证/导出]
  KGB --> KG[data/knowledge_graph/*]
```

实现证据锚点（离线工具）：
- 因子提取 CLI 默认输出 candidates：`scripts/factor_extractor/__main__.py:6`、`scripts/factor_extractor/__main__.py:37`
- 因子认证 CLI 默认输出 certified：`scripts/factor_extractor/certify.py:6`、`scripts/factor_extractor/certify.py:40`
- LogicChain staging → 输出目录常量：`scripts/logic_chain_builder/constants.py:98`、`scripts/logic_chain_builder/constants.py:101`
- LogicChain 写入 `data/logic_chains/`：`scripts/logic_chain_builder/writer.py:23`、`scripts/logic_chain_builder/writer.py:45`
- 规则 codegen 输出 `backend/generated/rules`：`scripts/codegen/rule_generator.py:78`、`scripts/codegen/rule_generator.py:80`
- 知识图谱 CLI（build/validate/export/query/snapshot）：`scripts/knowledge_graph_builder/cli.py:343`、`scripts/knowledge_graph_builder/cli.py:353`、`scripts/knowledge_graph_builder/cli.py:396`

### 2.4 模块清单（工程结构视角）

**后端（runtime & services）**
- `backend/pipeline/**`：L1-L5 编排、raw_factors 输出（`backend/pipeline/orchestrator.py:175`）
- `backend/calculators/**`：各体系 Calculator（bazi/astro/ziwei/yijing/tarot/dream）
- `backend/rules/**`：规则引擎、上下文、冲突、热重载、测试框架（`backend/rules/engine.py:47`）
- `backend/integration/**`：L4 融合引擎与组件（`backend/integration/fusion_engine.py:34`）
- `backend/core/llm/**`：LLM client/router/cost monitor、TOON serializer、Orchestrator（`.kiro/specs/layer5-application/tasks.md:15`、`backend/core/llm/orchestrator.py:266`）
- `backend/semantics/**`：L2 语义条目与 core（查询/缓存/索引）（`backend/semantics/README.md:11`）
- `backend/api/**`：FastAPI app 与 routes（`backend/api/main.py:32`）
- `backend/testing/**`：Testing & Ops spec 中的测试框架与生成器（`.kiro/specs/testing-ops/tasks.md:13`、`backend/testing/__init__.py:1`）

**数据与脚本**
- `data/**`：规则 JSONL、logic chains、知识图谱、因子本体、golden sets 等
- `scripts/**`：离线构建/转换/验证工具链
- `docker/**` + `docker-compose.yml`：部署与本地依赖编排（`docker-compose.yml:3`）

**前端**
- `frontend/**`：Next.js 应用，API URL 通过 `NEXT_PUBLIC_API_URL` 传入（`docker-compose.yml:95`、`frontend/package.json:10`）

---

## 3. 实现现状（功能覆盖率、质量评估、可运行性）

### 3.1 功能覆盖（按层）

#### L1（Calculator）

已实现的 Calculator（目录存在，且各自 tests 大多可运行）：
- bazi：`backend/calculators/bazi/**`
- ziwei：`backend/calculators/ziwei/**`
- yijing：`backend/calculators/yijing/**`
- astro：`backend/calculators/astro/**`
- tarot：`backend/calculators/tarot/**`
- dream：`backend/calculators/dream/**`

在线 Pipeline 实际接入：
- bazi（但依赖 birth_location 已解析）：`backend/pipeline/orchestrator.py:272`、`backend/calculators/bazi/calculator.py:189`、`backend/calculators/bazi/calculator.py:203`
- astro（仅当 lat/lon 存在时）：`backend/pipeline/orchestrator.py:279`、`backend/pipeline/orchestrator.py:280`
- dream：`backend/pipeline/orchestrator.py:286`
- tarot：`backend/pipeline/orchestrator.py:293`

#### L2（Semantic）

语义层规模很大（约 3265 个 `.py` 文件，约 6526 个 `@SemanticRegistry.register` 装饰器，来自目录统计），但存在明显质量与契约问题（详见问题清单）。

语义层架构文档声称“三层：Python 定义 + PostgreSQL 存储 + Redis 缓存”（`backend/semantics/README.md:11`、`backend/semantics/__init__.py:5`），但当前查询实现为内存扫描 `SemanticRegistry`，缓存为本地 dict（`backend/semantics/core/query.py:49`、`backend/semantics/core/query.py:70`）。

#### L3（Rules）

规则引擎支持 decorator 注册、按 engine_id/category 索引、batch 执行（`backend/rules/engine.py:88`、`backend/rules/engine.py:500`）。

规则生成链路已接入 Pipeline：启动时动态导入 `backend/generated/rules/*` 并触发注册（`backend/pipeline/orchestrator.py:120`、`backend/pipeline/orchestrator.py:133`、`backend/pipeline/orchestrator.py:158`）。

#### L4（Fusion）

FusionEngine 组合 WeightManager/CrossValidator/ThemeMapper/EvidenceChainBuilder/ConflictResolver（`backend/integration/fusion_engine.py:69`、`backend/integration/fusion_engine.py:105`）。

但 spec 要求复用 `backend/rules/dimension.py`（`.kiro/specs/layer4-fusion/requirements.md:19`），而实际 ThemeMapper 已迁移到 `DimensionRegistry`（`backend/integration/theme_mapper.py:18`、`backend/integration/theme_mapper.py:76`），并且 `backend/rules/dimension.py` 标注弃用（`backend/rules/dimension.py:7`）。

#### L5（LLM/叙事）

TOON v2 在 serializer 中实现（`backend/core/llm/toon_serializer.py:498`），Orchestrator 在 raw_factors 存在时启用 v2（`backend/core/llm/orchestrator.py:300`）。

但 v2 引擎块覆盖 ziwei/yijing 的代码存在（`backend/core/llm/toon_serializer.py:533`、`backend/core/llm/toon_serializer.py:535`），与 Pipeline raw_factors 仅产出 4 体系的现实冲突（`backend/pipeline/orchestrator.py:277`、`backend/pipeline/orchestrator.py:291`）。

#### API / 前后端

FastAPI app 注册了多路由，但存在“路由未挂载/启动阻断/默认 mock”等问题（见问题清单）。

### 3.2 测试与覆盖率（可量化信号）

#### 3.2.1 单元/集成测试通过情况（基于实际命令结果）

- `backend/integration/tests`：73 passed（附录命令）
- `backend/rules/tests`：146 passed, 1 skipped（附录命令）
- `backend/pipeline/tests/test_orchestrator.py`：1 failed（`backend/pipeline/tests/test_orchestrator.py:135` 处 mock 返回值与实现签名不一致；实现解包点 `backend/pipeline/orchestrator.py:274`）
- `backend/calculators/*/tests`：  
  - bazi：1 failed（断言“day_master_”因子数量 ==10；`backend/calculators/bazi/tests/test_integration.py:142`）  
  - tarot：1 failed（FactorMatrix 因子 ID 必须 `tarot_` 前缀；`backend/calculators/tarot/tests/test_interpreter_properties.py:286`、`backend/calculators/tarot/tests/test_interpreter_properties.py:299`）  
  - dream：1 failed（`dream_symbol_*` 分类前缀规则；`backend/calculators/dream/tests/test_extractor_properties.py:595`、`backend/calculators/dream/tests/test_extractor_properties.py:615`）
  - astro/ziwei/yijing：测试均通过（附录命令）
- 全量 `pytest -q`：**收集期失败**（Playbook generator 缺失，见 Blocker）

#### 3.2.2 覆盖率

当前 `.coverage` 报告仅覆盖 `backend/integration/*`（TOTAL 94%），覆盖范围口径偏窄，不能推导全系统覆盖率（附录 coverage 输出）。

#### 3.2.3 Calculator 覆盖矩阵（Golden Set/覆盖门槛）

`coverage_matrix_report.json` 提示：
- bazi 用例不足（25 < 50）（`coverage_matrix_report.json:11`、`coverage_matrix_report.json:12`、`coverage_matrix_report.json:29`）
- ziwei 缺关键维度覆盖（`coverage_matrix_report.json:37`）
- yijing 用例为 0（`coverage_matrix_report.json:81`、`coverage_matrix_report.json:90`）

对应 archive spec 的 Golden Set 门槛要求（`bazi>=50`、`ziwei>=30`、`yijing>=64`）见 `.kiro/specs/archive/calculator-accuracy-audit/requirements.md:171`、`.kiro/specs/archive/calculator-accuracy-audit/requirements.md:177`、`.kiro/specs/archive/calculator-accuracy-audit/requirements.md:178`。

### 3.3 可运行性与 API 可达性

#### 3.3.1 API 启动阻断（Playbook 包缺失文件）

任何导入 `backend.services.playbook.cache` 都会先执行 package `__init__`，而其中导入缺失模块 `backend.services.playbook.generator`（`backend/services/playbook/__init__.py:11`），导致：
- FastAPI routes 导入 `PlaybookCache` 会失败（`backend/api/routes/playbook.py:28`）
- `pytest` 收集 `backend/api` 时失败（错误输出见附录）

#### 3.3.2 路由挂载缺失（Versions）

`backend/api/routes/__init__.py` 导出了 `versions_router`（`backend/api/routes/__init__.py:13`），但 `backend/api/main.py` 未导入与 include（`backend/api/main.py:32`、`backend/api/main.py:179`），意味着 `/api/v1/versions/*` 可能不可达（除非另有入口）。

#### 3.3.3 /analyze 默认走 Mock（生产风险）

`/api/v1/analyze` 通过环境变量 `USE_REAL_PIPELINE` 控制是否执行真实 Pipeline，默认值为 false（`backend/api/routes/analyze.py:30`、`backend/api/routes/analyze.py:151`、`backend/api/routes/analyze.py:155`）。若未显式配置，线上将返回 Mock 结果而非真实推理链路。

### 3.4 数据契约遵循度（Schema vs 实现）

#### 3.4.1 engine_id 命名与正则约束冲突

- contracts 中 `FACTOR_ID_PATTERN` 仅允许字母/数字/下划线（不允许连字符）（`backend/core/contracts/base.py:18`）。  
- 但运行期 engine_id 大量使用连字符（如 `bazi-calculator`）（`backend/core/constants/engines.py:24`、`backend/calculators/bazi/models.py:1320`、`backend/generated/rules/bazi_wealth.py:23`）。  
- `FactorMatrix` 示例中 engine_id 又使用下划线风格（`backend/core/contracts/runtime_models.py:105`）。  
=> engine_id 作为跨模块关键字段，当前存在契约与实现“多口径并存”。

#### 3.4.2 引擎注册表与运行时不一致

`data/engines/registry.json` 使用下划线 engine_id（`data/engines/registry.json:3`），而 Pipeline/Rules/TOON 使用连字符 engine_id（`backend/core/constants/engines.py:24`）。若后续引擎治理、前端展示、权限门控依赖 registry，将存在错配风险。

### 3.5 知识工程质量（L1-L4 结构化提取与可追溯）

- 规则层（L3）在结果中保留 `source_book` 与 `l1_anchor` 字段（示例见生成规则 `backend/generated/rules/bazi_wealth.py:51`、`backend/generated/rules/bazi_wealth.py:52`），可支持“结论 → 典籍锚点”的可追溯链路。
- 语义层（L2）生成物存在大量“字段空置/污染”，使得 L2→L3 的解释性与一致性面临风险：  
  - `normalized_text_zh` 为空（`backend/semantics/sanming/smth_v1.0.0_壬水_阳水之生死与象_001.py:45`）  
  - `factor_refs` 混入 `new_candidate`、`engine_id`、`bazi_calculator`、`bazi_rule_engine`、`source_ref` 等非因子 ID（`backend/semantics/sanming/smth_v1.0.0_壬水_阳水之生死与象_001.py:47`）  
  - 文档中存在 Narrative Snippets，但结构化列表为空（`backend/semantics/astrological_houses/ah_v1.0.0_house_1___self_identity__ascen_001.py:60`、`backend/semantics/astrological_houses/ah_v1.0.0_house_1___self_identity__ascen_001.py:70`）

---

## 4. spec ↔ 实现对照矩阵（含 archive）

> 说明：状态分为 ✅已实现 / 🟡部分实现 / ❌未实现 / ⚠️与 spec 不一致 / ➕实现超出 spec

### 4.1 `.kiro/specs/`（主规格）

| Spec | 关键承诺（节选） | 状态 | 证据锚点（spec / code） |
|---|---|---:|---|
| `pipeline-link-fix` | 7 体系、引擎 ID 标准化、Pipeline 保留 raw_factors、TOON v2（含 INS） | 🟡 | 7体系定义：`.kiro/specs/pipeline-link-fix/requirements.md:14`；标准化：`backend/pipeline/orchestrator.py:195`、`backend/core/constants/engines.py:24`；raw_factors：`backend/pipeline/orchestrator.py:81`；TOON v2：`backend/core/llm/toon_serializer.py:498`；但 Pipeline 仅接入 4 体系：`backend/pipeline/orchestrator.py:272` |
| `layer4-fusion` | 复用 ConflictResolver、DimensionMapper；实现 FusionEngine（权重/主题/证据链/冲突） | ⚠️ | 复用要求：`.kiro/specs/layer4-fusion/requirements.md:18`、`.kiro/specs/layer4-fusion/requirements.md:19`；FusionEngine：`backend/integration/fusion_engine.py:75`；ThemeMapper 改用 DimensionRegistry：`backend/integration/theme_mapper.py:18`；dimension.py 已弃用：`backend/rules/dimension.py:7` |
| `layer5-application` | LLM core、TOON、Memory、Narrative、Safety、Playbook、API 全部完成 | ⚠️ | spec 声称 playbook generator 存在：`.kiro/specs/layer5-application/tasks.md:20`；但 `backend/services/playbook/generator.py` 缺失且导入报错：`backend/services/playbook/__init__.py:11` |
| `frontend-backend-alignment` | Playbook/Dream/Timeline/Patterns/Insights/User API 对齐；Playbook 支持 7 引擎 | 🟡 | Playbook 7引擎承诺：`.kiro/specs/frontend-backend-alignment/requirements.md:12`；Playbook route 引擎列表：`backend/api/routes/playbook.py:168`；但因 playbook 包缺失文件导致 API 启动阻断：`backend/services/playbook/__init__.py:11` |
| `rule-converter` | LogicChain → 规则 JSONL → codegen，形成数据闭环（目标 3000-4000+ 规则） | ✅ | 转换器说明：`.kiro/specs/rule-converter/requirements.md:5`；codegen 输出目录：`scripts/codegen/rule_generator.py:80`；Pipeline 导入生成规则：`backend/pipeline/orchestrator.py:120`；数据侧 `data/rules/generated` 约 4993 行（见附录统计） |
| `testing-ops` | Test framework / hot reload / observability / cache / deployment 全部完成 | 🟡 | tasks 总览宣称完成：`.kiro/specs/testing-ops/tasks.md:13`；但 pre-commit 指向缺失脚本：`.pre-commit-config.yaml:15`；deploy/ 目录不存在（本仓库使用 `docker/` 目录，`docker/Dockerfile.backend:1`） |

### 4.2 `.kiro/specs/archive/`（历史规格，仍影响规划差距）

| Archive Spec | 关键承诺（节选） | 状态 | 证据锚点 |
|---|---|---:|---|
| `cross-book-knowledge-graph` | Layer2.5 图谱为 FusionEngine 提供只读 SemanticQuery 接口 | ❌ | spec 明确定位：`.kiro/specs/archive/cross-book-knowledge-graph/requirements.md:5`、`.kiro/specs/archive/cross-book-knowledge-graph/requirements.md:11`；离线 CLI 存在：`scripts/knowledge_graph_builder/cli.py:353`；FusionEngine 运行期无查询接入点：`backend/integration/fusion_engine.py:95` |
| `semantic-core` | Zero JSON 内存对象；SemanticCache 基于 Redis；索引持久化等 | 🟡 | 约束/Redis cache：`.kiro/specs/archive/semantic-core/requirements.md:11`、`.kiro/specs/archive/semantic-core/requirements.md:28`；但实际 `backend/semantics/core/cache.py` 为内存缓存：`backend/semantics/core/cache.py:47`，且查询为内存扫描：`backend/semantics/core/query.py:70` |
| `calculator-integration` | FactorMatrix 因子命名遵循 `{system}_*`；Geocoding 集成 | 🟡 | 命名规范要求：`.kiro/specs/archive/calculator-integration/requirements.md:146`、`.kiro/specs/archive/calculator-integration/requirements.md:147`；但 tarot/dream 性质测试失败：`backend/calculators/tarot/tests/test_interpreter_properties.py:299`、`backend/calculators/dream/tests/test_extractor_properties.py:615`；BaziCalculator 要求 birth_location 已解析：`backend/calculators/bazi/calculator.py:189`、`backend/calculators/bazi/calculator.py:203`，Pipeline 未自动解析 birth_place：`backend/pipeline/orchestrator.py:324` |
| `calculator-accuracy-audit` | Golden Set 门槛：bazi≥50、ziwei≥30、yijing≥64 等 | 🟡 | 门槛：`.kiro/specs/archive/calculator-accuracy-audit/requirements.md:171`、`.kiro/specs/archive/calculator-accuracy-audit/requirements.md:178`；覆盖矩阵显示未达标：`coverage_matrix_report.json:11`、`coverage_matrix_report.json:81` |
| `action-compiler-layer` | Playbook/Dream/Insight → Action 编译闭环 | ❌ | spec 定义：`.kiro/specs/archive/action-compiler-layer/requirements.md:5`；代码中仅发现 contracts，无 service 实现（contracts：`backend/core/contracts/action_models.py:191`；未发现 `ActionCompilerService` 实现：全局搜索无命中） |
| `geocoding-service` | 地理编码服务与 API | ✅ | API route：`backend/api/routes/geocoding.py:64`；服务入口：`backend/api/routes/geocoding.py:13` |
| `factor-ontology-completion` | 因子提取/认证工具链、候选/认证数据结构 | ✅/🟡 | 工具链存在：`scripts/factor_extractor/__main__.py:1`、`scripts/factor_extractor/certify.py:1`；但语义生成物仍出现 `new_candidate` 污染（`backend/semantics/sanming/smth_v1.0.0_壬水_阳水之生死与象_001.py:47`） |

---

## 5. 问题清单（按严重程度分级，含证据行号）

### 5.0 严重度定义

- **Blocker**：阻断系统启动/CI/关键路径验证
- **Critical**：高概率导致数据污染/安全合规问题/核心功能结果失真
- **Major**：重要能力缺失或 spec 关键承诺未落地，或导致显著体验/一致性问题
- **Minor**：非关键但会累积技术债（文档缺失、告警、轻度不一致）

### 5.1 Blocker

**B1. Playbook 模块缺失关键文件，阻断 API 启动与全量测试收集**  
影响：`backend/api` 在 import routes 时触发 Playbook 包初始化，抛 `ModuleNotFoundError`，导致服务不可用、CI 无法跑全量 pytest。  
证据：
- `backend/services/playbook/__init__.py:11`（导入不存在的 `backend.services.playbook.generator`）
- spec 声称 `generator.py` 存在：`.kiro/specs/layer5-application/tasks.md:20`、`.kiro/specs/pipeline-link-fix/tasks.md:38`

**B2. 全量 `pytest` 无法运行（收集期即中断）**  
影响：无法建立“提交即回归”的商业级质量底座；覆盖率与质量门槛失效。  
证据（根因同 B1）：
- `backend/services/playbook/__init__.py:11`

### 5.2 Critical

**C1. Dream Insight 写入使用 `day_master` 作为 `user_id`，存在跨用户数据污染风险**  
影响：多用户共享同一日主（或日主重复概率高）时，梦境洞察会被写入同一个 user_id 命名空间；属于身份隔离/合规级风险。  
证据：
- `backend/api/routes/dream.py:247`（注释“生成后写入 Insight”）
- `backend/api/routes/dream.py:251`（`user_id = request.user_profile.bazi.day_master`）

**C2. 版本选择偏离推荐检测恒为 false（推荐对比失效）**  
影响：Memory 中的“偏离推荐”事件永远不会触发，决策洞察链路被静默破坏。  
证据：
- `backend/api/routes/versions.py:186`（先将 `recommended_version_id` 设为 `version_id`）
- `backend/api/routes/versions.py:192`、`backend/api/routes/versions.py:196`（把同值作为 `recommended_id` 写入）
- `backend/services/memory/background_writer.py:101`（`is_deviation = version_id != recommended_id`）

**C3. `/api/v1/analyze` 默认走 Mock，生产环境极易输出“假分析”**  
影响：若未正确配置环境变量，用户会持续收到非真实推理结果，属于产品级严重风险。  
证据：
- `backend/api/routes/analyze.py:30`（默认 `USE_REAL_PIPELINE=false`）
- `backend/api/routes/analyze.py:151`、`backend/api/routes/analyze.py:155`（else 分支走 mock）

### 5.3 Major

**M1. 7 体系规划未贯通：在线 Pipeline 仅接入 4 体系（链路断流）**  
影响：spec/前端宣称支持 7 引擎，但实际运行时无法产出 ziwei/yijing/psych 结果；并导致 TOON v2 设计的引擎块长期缺失输入。  
证据：
- 7 体系定义：`.kiro/specs/pipeline-link-fix/requirements.md:14`、`.kiro/specs/frontend-backend-alignment/requirements.md:12`
- Pipeline L1 实际接入：`backend/pipeline/orchestrator.py:272`、`backend/pipeline/orchestrator.py:286`、`backend/pipeline/orchestrator.py:293`
- TOON v2 支持 ziwei/yijing 块但依赖 raw_factors：`backend/core/llm/toon_serializer.py:523`、`backend/core/llm/toon_serializer.py:533`

**M2. Pipeline 未自动集成 Geocoding，BaziCalculator 要求 birth_location 已解析**  
影响：API 输入允许仅提供 `location`（城市名）而不提供经纬度（`backend/api/models.py:28`），但 Pipeline 构造 `birth_location` 仅在 lat/lon 存在时（`backend/pipeline/orchestrator.py:325`），且 BaziCalculator 校验要求 birth_location 必须存在（`backend/calculators/bazi/calculator.py:203`）。这会导致“正常输入 → bazi 计算失败 → pipeline 结果为空/降级”。  
证据：
- API BirthData 字段：`backend/api/models.py:28`、`backend/api/models.py:29`
- Pipeline 构造 birth_location：`backend/pipeline/orchestrator.py:324`、`backend/pipeline/orchestrator.py:325`
- BaziCalculator 校验：`backend/calculators/bazi/calculator.py:189`、`backend/calculators/bazi/calculator.py:203`

**M3. Versions 路由未挂载到 FastAPI app（功能不可达）**  
影响：版本树/版本选择/导航 API 可能无法对外提供，前端/产品功能缺口。  
证据：
- routes 导出：`backend/api/routes/__init__.py:13`
- main.py 未导入/未 include：`backend/api/main.py:32`、`backend/api/main.py:179`

**M4. engine_id 命名/契约/注册表多套并存，存在治理与集成风险**  
影响：引擎治理、门控、权重、缓存 key、前端展示等若依赖“统一 engine_id”，当前状态会导致错配。  
证据：
- contracts 正则仅允许下划线：`backend/core/contracts/base.py:18`
- runtime 使用连字符：`backend/core/constants/engines.py:24`、`backend/calculators/bazi/models.py:1320`
- registry 使用下划线：`data/engines/registry.json:3`
- FactorMatrix 示例为下划线：`backend/core/contracts/runtime_models.py:105`

**M5. 语义层（L2）架构与数据质量存在系统性问题（影响可解释性与一致性）**  
影响：L2 作为“规则/叙事的语义底座”，若 factor_refs 污染/字段空置，将直接降低“证据链可追溯典籍原文”的可信度与可维护性。  
证据：
- 文档宣称 Postgres/Redis 三层：`backend/semantics/README.md:11`
- 实现为内存扫描/本地缓存：`backend/semantics/core/query.py:49`、`backend/semantics/core/query.py:70`
- `factor_refs` 污染与字段空置示例：`backend/semantics/sanming/smth_v1.0.0_壬水_阳水之生死与象_001.py:45`、`backend/semantics/sanming/smth_v1.0.0_壬水_阳水之生死与象_001.py:47`
- Narrative Snippets 文档存在但结构化列表为空：`backend/semantics/astrological_houses/ah_v1.0.0_house_1___self_identity__ascen_001.py:60`、`backend/semantics/astrological_houses/ah_v1.0.0_house_1___self_identity__ascen_001.py:70`

**M6. 语义缓存接口契约不一致（未来接入语义缓存会触发运行时错误）**  
影响：RuleContext 期望缓存具备 `get_sync/set_sync`（`backend/rules/context.py:176`、`backend/rules/context.py:192`），但现有缓存实现仅提供 `get/set`（`backend/core/cache/semantic_cache.py:115`、`backend/semantics/core/cache.py:76`）。当前 pipeline 未注入 semantic_cache 所以暂未爆炸，但一旦启用会出现 `AttributeError` 风险。  
证据：
- 调用方：`backend/rules/context.py:176`、`backend/rules/context.py:192`
- 实现方（无 get_sync）：`backend/core/cache/semantic_cache.py:115`、`backend/semantics/core/cache.py:76`

**M7. 知识图谱（L2.5）未接入运行期 FusionEngine（spec 未落地）**  
影响：archive spec 期望 FusionEngine 可查询跨书对齐/冲突/权威性，但当前仅离线构建/导出，不产生在线价值。  
证据：
- spec 目标：`.kiro/specs/archive/cross-book-knowledge-graph/requirements.md:11`
- 离线 CLI：`scripts/knowledge_graph_builder/cli.py:353`
- FusionEngine 主流程无 query 接入点：`backend/integration/fusion_engine.py:95`

**M8. Pipeline 测试与实现签名漂移（CI 信号失真）**  
影响：测试无法真实验证 Pipeline；同时暴露“接口变更未同步测试”的工程流程问题。  
证据：
- 测试 mock 返回值类型错误：`backend/pipeline/tests/test_orchestrator.py:135`、`backend/pipeline/tests/test_orchestrator.py:136`
- 实现解包点：`backend/pipeline/orchestrator.py:274`

**M9. Calculator 命名规范性质测试失败（契约一致性问题）**  
影响：archive spec 要求 FactorMatrix 因子命名 `{system}_*`（`.kiro/specs/archive/calculator-integration/requirements.md:147`），但当前至少 tarot/dream 存在不满足前缀规则的因子（测试失败）。  
证据：
- spec：`.kiro/specs/archive/calculator-integration/requirements.md:147`
- tarot 测试：`backend/calculators/tarot/tests/test_interpreter_properties.py:299`
- dream 测试：`backend/calculators/dream/tests/test_extractor_properties.py:615`

**M10. README 引用的核心设计文档缺失（文档完整性不足）**  
影响：对外/对内沟通与交接成本高；审计与规划容易基于过期信息。  
证据：
- README 引用 `docs/ARCHITECTURE.md`：`README.md:33`（但 `docs/ARCHITECTURE.md` 不存在）
- README 引用多个 docs 文件：`README.md:62`、`README.md:65`、`README.md:66`（对应文件均缺失）

**M11. pre-commit 本地钩子指向不存在脚本，质量门禁形同虚设**  
影响：数据校验钩子无法运行，破坏“提交即校验”的工程纪律。  
证据：
- `.pre-commit-config.yaml:15`（`backend/scripts/validate_data.py` 不存在）

### 5.4 Minor

**m1. `backend/rules/dimension.py` 已弃用但仍被 import，导致运行时 DeprecationWarning**  
影响：噪声告警，降低日志信噪比。  
证据：
- 弃用声明：`backend/rules/dimension.py:7`

**m2. 多处文档/任务单宣称“已完成”，但与仓库事实不一致**  
影响：规划与交付预期偏差（例如 Layer5 tasks 认为 playbook generator 存在）。  
证据：
- `.kiro/specs/layer5-application/tasks.md:20`
- `.kiro/specs/testing-ops/tasks.md:19`

---

## 6. 商业级差距分析（架构 / 质量 / 完整性）

### 6.1 架构差距（Production Architecture）

1) **核心链路“可用引擎数”与宣称/规划不一致**：  
   7 体系规划（`.kiro/specs/pipeline-link-fix/requirements.md:14`）未在运行期贯通（`backend/pipeline/orchestrator.py:272`），直接影响产品“多体系交叉验证”的核心卖点。

2) **关键输入依赖（Geocoding）未被 Pipeline 内建**：  
   API 层允许 location-only（`backend/api/models.py:28`），但 Pipeline 不负责解析（`backend/pipeline/orchestrator.py:324`），Calculator 反而强制要求 birth_location（`backend/calculators/bazi/calculator.py:203`）。这会把“正常用户输入”变成隐式前置条件（必须先调用 geocoding）。

3) **engine_id 治理缺失**：  
   contracts/registry/runtime 多套 ID 体系并存（`backend/core/contracts/base.py:18` vs `backend/core/constants/engines.py:24` vs `data/engines/registry.json:3`），会在权限门控、权重、缓存 key、前端配置同步等方面形成长期技术债。

4) **L2.5 图谱未融入运行期**：  
   仅离线工具存在（`scripts/knowledge_graph_builder/cli.py:353`），与 spec 设想的“FusionEngine 只读查询”脱节（`.kiro/specs/archive/cross-book-knowledge-graph/requirements.md:11`）。

### 6.2 质量差距（Testing, Coverage, CI, Maintainability）

1) **全量测试回归被阻断**：Blocker 级问题（`backend/services/playbook/__init__.py:11`）。  
2) **测试集存在漂移与口径不一致**：例如 Pipeline 测试签名漂移（`backend/pipeline/tests/test_orchestrator.py:135`），Calculator 命名规范性质测试失败（`backend/calculators/tarot/tests/test_interpreter_properties.py:299`）。  
3) **覆盖率口径不足**：当前 coverage report 仅覆盖 `backend/integration/*`，无法支撑“商业级发布”需要的风险评估。  
4) **pre-commit 门禁失效**：本地数据校验脚本缺失（`.pre-commit-config.yaml:15`）。  

### 6.3 完整性差距（功能、数据、文档、运维）

1) **核心业务模块（Playbook/Versions/ActionCompiler）完整性不足**：  
   - Playbook 启动阻断（`backend/services/playbook/__init__.py:11`）  
   - Versions 路由未挂载（`backend/api/main.py:179`）  
   - ActionCompiler 仅停留在 contracts（`backend/core/contracts/action_models.py:191`）  

2) **文档缺失与不一致**：README 引用的关键 docs 文件不存在（`README.md:33`）。  

3) **数据与隐私合规**：  
   Dream 写入 user_id 污染（`backend/api/routes/dream.py:251`）属于必须优先修复的合规风险点。

---

## 7. 优先级建议（先做什么后做什么）

### P0（立即做：恢复可运行性 + 消除数据污染 + 纠正默认行为）

1) **修复 Playbook 模块缺失，恢复 API 启动与全量测试回归**（根因：`backend/services/playbook/__init__.py:11`）。  
2) **修复 Dream 写入 user_id 污染**（`backend/api/routes/dream.py:251`）。  
3) **修复 Versions 偏离推荐检测逻辑**（`backend/api/routes/versions.py:186` + `backend/services/memory/background_writer.py:101`）。  
4) **将 `/api/v1/analyze` 默认行为切换为真实 Pipeline（或显式失败）**，避免“默认 mock”进入生产（`backend/api/routes/analyze.py:30`）。  
5) **挂载 versions_router**，恢复端点可达性（`backend/api/main.py:179`）。  

### P1（短期：贯通 7 体系链路 + 统一契约口径）

1) **在线 Pipeline 接入 ziwei/yijing/psych（至少保证 L1-L4 可跑通）**（`backend/pipeline/orchestrator.py:272`）。  
2) **engine_id 统一治理**：明确“唯一 canonical engine_id”并让 contracts/registry/runtime 对齐（`backend/core/contracts/base.py:18`、`backend/core/constants/engines.py:24`、`data/engines/registry.json:3`）。  
3) **Geocoding 内建到 Pipeline（或在 API 层强制要求 lat/lon 并给出明确错误）**（`backend/calculators/bazi/calculator.py:203` vs `backend/api/models.py:28`）。  

### P2（中期：知识工程质量与商业级能力补齐）

1) **语义层生成质量治理**：修复 `factor_refs` 污染、补齐 `normalized_text_zh`、填充 narrative_snippets 结构化字段（示例见 `backend/semantics/sanming/smth_v1.0.0_壬水_阳水之生死与象_001.py:47`）。  
2) **将跨书知识图谱接入 FusionEngine 作为只读查询增强**（对齐 `.kiro/specs/archive/cross-book-knowledge-graph/requirements.md:11`）。  
3) **补齐 ActionCompiler Layer（从 contracts 走向 service + API + batch）**（对齐 `.kiro/specs/archive/action-compiler-layer/requirements.md:63`）。  
4) **文档修复与发布就绪**：补齐 README 引用的架构与 Schema 文档，形成单一可信来源（`README.md:33`）。  

---

## 附录 A：审计命令与结果摘要（节选）

> 说明：本附录用于记录“可复现”的验证结果；问题条目仍以代码行号为主证据。

### A.1 Python/pytest 版本

- Python：3.12.3（`.venv`）
- pytest：7.4.3

### A.2 关键测试结果（节选）

- `./.venv/bin/python -m pytest backend/integration/tests -q` → 73 passed
- `./.venv/bin/python -m pytest backend/rules/tests -q` → 146 passed, 1 skipped
- `./.venv/bin/python -m pytest backend/pipeline/tests/test_orchestrator.py -q` → 1 failed（见 `backend/pipeline/tests/test_orchestrator.py:135`）
- `./.venv/bin/python -m pytest -q` → 收集期失败（根因见 `backend/services/playbook/__init__.py:11`）

### A.3 覆盖率报告（局部）

- `./.venv/bin/python -m coverage report -m` → 仅覆盖 `backend/integration/*`，TOTAL 94%（口径有限）

### A.4 数据规模（目录统计）

- LogicChain YAML 数量：27（`data/logic_chains/*.yaml`）
- 生成规则 JSONL 行数：`data/rules/generated/**.jsonl` 合计约 4993（目录统计）
- 生成规则 Python 模块：54（`backend/generated/rules/*.py`）
- 语义条目规模：`backend/semantics/**/*.py` ~3265 文件，`@SemanticRegistry.register` ~6526 处（目录/搜索统计）

