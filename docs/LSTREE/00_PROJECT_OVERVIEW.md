# LucidSelf 项目总览

## 项目定位
LucidSelf (LS) 是一个集成多元命理系统的AI洞察引擎，融合八字、紫微、西占、塔罗、周易、解梦等多种推演引擎，结合LLM进行语义推理与叙事生成。

## 根目录结构

```
LucidSelf/
├── backend/              # 后端核心服务 (Python/FastAPI)
├── frontend/             # 前端应用 (Next.js/React)
├── scripts/              # 构建工具与数据处理脚本
├── data/                 # 数据资产 (规则、本体、知识图谱)
├── docs/                 # 项目文档
├── 典籍/                 # 原典文本与结构化成果
├── openspec/             # 变更管理与技术规范
├── docker/               # Docker配置
├── .windsurf/            # Windsurf IDE配置与工作流
├── .kiro/                # Kiro相关配置
├── .github/              # GitHub Actions
├── docker-compose.yml    # Docker编排
├── requirements.txt      # Python依赖
├── README.md             # 项目说明
├── AGENTS.md             # AI助手指令
├── LLM灵芽api配置.md     # LLM API配置文档
├── LLM调用及成本方案.md   # LLM成本优化方案
└── Playbook-TODO.md      # Playbook待办事项
```

## 核心模块概览

### 1. backend/ - 后端服务
- **api/**: FastAPI路由与中间件
- **calculators/**: 各推演引擎计算器 (bazi/astro/dream/tarot/yijing/ziwei)
- **core/**: 核心基础设施 (LLM/缓存/契约/引擎管理)
- **semantics/**: 语义片段库 (~30个书籍源)
- **services/**: 业务服务 (叙事/场景/学习/记忆等)
- **rules/**: 规则引擎
- **integration/**: 跨域融合与证据链

### 2. frontend/ - 前端应用
- Next.js 14 + React + TailwindCSS
- 组件化视图架构
- Auth/Layout/Profile/Views模块

### 3. scripts/ - 工具脚本
- **codegen/**: 代码生成器 (语义/规则/因子)
- **knowledge_graph_builder/**: 知识图谱构建
- **logic_chain_builder/**: 逻辑链构建
- **rule_converter/**: 规则转换

### 4. data/ - 数据资产
- **rules/**: 各引擎规则文件 (YAML)
- **factor_ontology/**: 因子本体定义
- **logic_chains/**: 逻辑链数据 (~30本书)
- **knowledge_graph/**: 知识图谱配置

### 5. 典籍/ - 原典与本体
- **中文典籍/**: 三命通会、子平真诠、周易等
- **texts/**: 西方原典 (塔罗、占星、心理学)
- **因子本体/**: 各系统因子定义

### 6. openspec/ - 变更管理
- **specs/**: 技术规范 (7个核心模块)
- **changes/**: 变更提案
- **project.md**: 项目总体设计

## 详细文档索引

| 文档 | 描述 | 大小 |
|------|------|------|
| [01_BACKEND.md](01_BACKEND.md) | 后端服务详细结构 | 10KB |
| [02_FRONTEND.md](02_FRONTEND.md) | 前端应用详细结构 | 4KB |
| [03_SCRIPTS.md](03_SCRIPTS.md) | 工具脚本详细结构 | 7KB |
| [04_DATA.md](04_DATA.md) | 数据资产详细结构 | 7KB |
| [05_TEXTS.md](05_TEXTS.md) | 典籍目录详细结构 | 7KB |
| [06_OPENSPEC.md](06_OPENSPEC.md) | 变更管理详细结构 | 3KB |
| [07_CONFIG_TOOLS.md](07_CONFIG_TOOLS.md) | 配置与工具文档 | 4KB |
| [08_SERVICES_DETAIL.md](08_SERVICES_DETAIL.md) | Services业务服务详细 | 7KB |
| [09_SEMANTICS_DETAIL.md](09_SEMANTICS_DETAIL.md) | Semantics语义库详细 | 7KB |
| [10_TECH_EXPLAINED.md](10_TECH_EXPLAINED.md) | **技术概念通俗讲解** ★推荐阅读 | 15KB |
| [11_FILE_RELATIONS.md](11_FILE_RELATIONS.md) | **文件关系与依赖图** ★推荐阅读 | 10KB |
| [12_GLOSSARY.md](12_GLOSSARY.md) | **术语表** - 技术名词通俗解释 | 8KB |

### 极致细化版文档（技术深度解读）

| 文档 | 描述 | 大小 |
|------|------|------|
| [10A_BASICS_DEEP.md](10A_BASICS_DEEP.md) | 基础概念极致细化 - 前后端/API/数据库 | 18KB |
| [10B_BACKEND_DEEP.md](10B_BACKEND_DEEP.md) | 后端模块极致细化 - API/计算器/核心 | 25KB |
| [10C_RULES_SERVICES_DEEP.md](10C_RULES_SERVICES_DEEP.md) | 规则引擎与服务层极致细化 | 22KB |
| [10D_SEMANTICS_FRONTEND_DEEP.md](10D_SEMANTICS_FRONTEND_DEEP.md) | 语义库与前端极致细化 | 24KB |
| [10E_SCRIPTS_DATA_DEEP.md](10E_SCRIPTS_DATA_DEEP.md) | 脚本与数据处理极致细化 | 20KB |

## 阅读建议

### 完全不懂技术的人
1. `12_GLOSSARY.md` - 先了解术语
2. `10A_BASICS_DEEP.md` - 基础概念极致细化
3. `10_TECH_EXPLAINED.md` - 技术概念通俗讲解
4. `00_PROJECT_OVERVIEW.md` - 项目总览

### 想深入了解某个模块
- 后端架构 → `10B_BACKEND_DEEP.md`
- 规则引擎 → `10C_RULES_SERVICES_DEEP.md`
- 知识库 → `10D_SEMANTICS_FRONTEND_DEEP.md`
- 数据流程 → `10E_SCRIPTS_DATA_DEEP.md`

### 想了解文件冲突和依赖
- `11_FILE_RELATIONS.md` - 文件关系与依赖图
- `10_TECH_EXPLAINED.md` 第七部分 - 冲突点汇总

## 技术栈

- **后端**: Python 3.11+, FastAPI, Pydantic, SQLAlchemy
- **前端**: Next.js 14, React 18, TailwindCSS
- **数据库**: PostgreSQL, MongoDB, Redis
- **LLM**: 多模型路由 (DeepSeek/Claude/GPT等)
- **部署**: Docker, Docker Compose
