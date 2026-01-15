# 文件关系与依赖图

> 本文档展示LS项目中各文件/模块之间的依赖关系和数据流向

---

# 第一部分：核心依赖关系

## 1. 计算器依赖链

```
┌─────────────────────────────────────────────────────────────────┐
│                        calculators/                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  bazi/calculator.py ─────────┬──────→ core/contracts/unified_time.py
│         ↓                    │                   ↑
│  bazi/models.py              │        (时间格式统一)
│         ↓                    │
│  bazi/solar_terms.py ←───────┼──── data/solar_terms/
│         ↓                    │         (节气数据)
│  bazi/ten_gods.py            │
│         ↓                    │
│  bazi/dayun.py               │
│                              │
│  astro/calculator.py ────────┤──────→ core/geocoding/
│         ↓                    │         (需要经纬度)
│  astro/models.py             │
│                              │
│  ziwei/calculator.py ────────┤
│         ↓                    │
│  ziwei/lunar_calendar.py ────┤──────→ (农历转换)
│         ↓                    │
│  ziwei/star_placement.py     │
│                              │
└─────────────────────────────────────────────────────────────────┘
```

### 依赖说明
| 文件 | 依赖 | 原因 |
|------|------|------|
| `bazi/calculator.py` | `unified_time.py` | 需要统一的时间表示 |
| `bazi/calculator.py` | `solar_terms.py` | 需要节气判断月令 |
| `astro/calculator.py` | `geocoding/service.py` | 需要把出生地转经纬度 |
| `ziwei/calculator.py` | `lunar_calendar.py` | 紫微用农历 |

---

## 2. 规则引擎依赖链

```
┌─────────────────────────────────────────────────────────────────┐
│                         rules/                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  engine.py ─────────────→ data/rules/*.yaml                     │
│      ↓                        (加载规则文件)                      │
│      ↓                                                           │
│  condition.py ──────────→ factor_ontology/                       │
│      ↓                        (因子定义)                          │
│      ↓                                                           │
│  context.py ────────────→ calculators/                          │
│      ↓                        (获取计算结果)                      │
│      ↓                                                           │
│  conflict.py ───────────→ semantics/                            │
│                               (获取语义片段)                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### ⚠️ 循环依赖风险
```
rules/engine.py
      ↓ 调用
services/narrative/
      ↓ 可能调用
rules/engine.py   ← 循环！
```

**建议**: narrative不应直接调用rules，应通过服务层解耦

---

## 3. 语义系统依赖链

```
┌─────────────────────────────────────────────────────────────────┐
│                     数据源 → 生成 → 运行时                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  典籍/中文典籍/三命通会/                                          │
│           ↓                                                      │
│           ↓ (人工结构化)                                          │
│           ↓                                                      │
│  data/logic_chains/三命通会.yaml                                 │
│           ↓                                                      │
│           ↓ (codegen运行)                                        │
│           ↓                                                      │
│  scripts/codegen/semantic_generator.py                          │
│           ↓                                                      │
│           ↓ (自动生成)                                           │
│           ↓                                                      │
│  backend/semantics/sanming/                                     │
│           ↓                                                      │
│           ↓ (运行时加载)                                          │
│           ↓                                                      │
│  services/narrative/snippet_service.py                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 关键点
| 步骤 | 文件 | 说明 |
|------|------|------|
| 源文件 | `典籍/中文典籍/*/` | 人工维护的原文 |
| 中间产物 | `data/logic_chains/*.yaml` | 结构化后的逻辑链 |
| 生成器 | `scripts/codegen/semantic_generator.py` | 自动代码生成 |
| 目标代码 | `backend/semantics/*/` | 运行时使用的Python代码 |

### ⚠️ 修改注意
- ❌ 不要直接修改 `backend/semantics/*/`
- ✅ 修改 `典籍/` 或 `data/logic_chains/`，然后重新生成

---

## 4. 服务层依赖链

```
┌─────────────────────────────────────────────────────────────────┐
│                        services/                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  scenario/router.py                                              │
│           ↓                                                      │
│           ↓ (场景识别后分发)                                      │
│           ↓                                                      │
│  ┌────────┴────────────────────────────────────┐                │
│  ↓                        ↓                    ↓                │
│  narrative/generator.py   playbook/generator.py  action_compiler/ │
│           ↓                        ↓                    ↓        │
│           ↓                        ↓                    ↓        │
│  ┌────────┴────────────────────────┴────────────────────┘        │
│  ↓                                                               │
│  core/llm/orchestrator.py                                        │
│           ↓                                                      │
│           ↓ (调用AI)                                              │
│           ↓                                                      │
│  core/llm/providers/                                             │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 服务调用关系
```
用户请求
    ↓
scenario/router.py      ← 识别"这是什么类型的问题"
    ↓
narrative/generator.py  ← 生成叙事文本
    ↓
snippet_service.py      ← 选择语义片段
    ↓
prompt_builder.py       ← 构建AI提示词
    ↓
llm/orchestrator.py     ← 编排AI调用
    ↓
llm/client.py           ← 发送请求
```

---

# 第二部分：前后端数据同步

## 类型定义对应关系

```
后端 (Python/Pydantic)              前端 (TypeScript)
──────────────────────────────────────────────────────
core/contracts/                     frontend/src/types/
    ↓                                   ↓
unified_time.py         ←──?──→     time.ts
    │                                   │
    │  UnifiedTime                      │  UnifiedTime
    │  {                                │  {
    │    gregorian: date                │    gregorian: Date
    │    lunar: LunarDate               │    lunar: LunarDate
    │    solar_term: str                │    solarTerm: string
    │  }                                │  }
    │                                   │
action_models.py        ←──?──→     action.ts
narrative_models.py     ←──?──→     narrative.ts
```

### ⚠️ 同步问题
| 后端字段 | 前端字段 | 问题 |
|----------|----------|------|
| `snake_case` | `camelCase` | 命名风格不同 |
| `Optional[str]` | `string \| undefined` | 可选表示不同 |
| `datetime` | `Date` | 日期类型不同 |

### 建议解决方案
```
方案1: 使用OpenAPI自动生成
    backend → openapi.json → 前端类型生成器 → types/

方案2: 手动维护对照表
    docs/type_mapping.md 记录所有对应关系

方案3: 共享Schema
    使用JSON Schema作为单一来源
```

---

# 第三部分：配置文件关系

## 环境变量传递链

```
.env.example (模板)
      ↓ 复制
.env (实际配置，不提交Git)
      ↓ 加载
backend/core/config.py (读取配置)
      ↓ 注入
各服务模块 (使用配置)
```

### 配置分布

```
根目录/
├── .env                    # 后端环境变量
├── docker-compose.yml      # Docker服务配置
│
├── backend/
│   ├── .env                # 后端专用变量
│   └── core/
│       └── config.py       # 配置加载器
│
└── frontend/
    ├── .env.local          # 前端环境变量
    └── next.config.ts      # Next.js配置
```

### ⚠️ 注意
- 后端和前端的 `.env` 是**独立**的
- Docker环境变量可能**覆盖**本地 `.env`

---

# 第四部分：数据资产关系

## 规则文件流向

```
data/rules/
├── bazi/
│   ├── core.yaml           ← 人工编写的核心规则
│   └── combinations.yaml   ← 人工编写的合化规则
│
├── generated/              ← 自动生成的规则
│   ├── bazi_sanming.yaml   ← 从三命通会生成
│   └── bazi_ziping.yaml    ← 从子平真诠生成
│
└── registry.json           ← 规则注册表（记录所有规则）
```

### 生成关系
```
典籍/中文典籍/三命通会/
          ↓
scripts/rule_converter/
          ↓
data/rules/generated/bazi_sanming.yaml
          ↓
rules/engine.py (运行时加载)
```

---

## 因子本体关系

```
典籍/因子本体/                    data/factor_ontology/
├── bazi/                        ├── candidates/
│   └── stems.yaml      ────→        └── bazi.yaml (待审核)
│                                ├── certified/
│                        ────→       └── bazi.yaml (已认证)
│                                └── namespace.yaml (命名空间)
```

### 审核流程
```
人工定义因子 → candidates/ → 审核 → certified/ → 代码使用
```

---

# 第五部分：测试文件关系

## 测试目录分布

```
backend/
├── api/tests/               # API层测试
├── calculators/
│   ├── bazi/tests/          # 八字计算测试
│   ├── astro/tests/         # 占星计算测试
│   └── .../tests/
├── core/
│   ├── contracts/tests/     # 契约测试
│   ├── llm/tests/           # LLM测试
│   └── geocoding/tests/     # 地理编码测试
├── services/
│   ├── narrative/tests/     # 叙事服务测试
│   └── .../tests/
├── rules/tests/             # 规则引擎测试
├── integration/tests/       # 集成测试
└── testing/                 # 测试框架和工具
    ├── framework/           # 测试框架
    ├── generators/          # 测试数据生成
    └── unit/                # 单元测试工具
```

### 测试类型
| 目录 | 类型 | 说明 |
|------|------|------|
| `*/tests/` | 单元测试 | 测试单个模块 |
| `integration/tests/` | 集成测试 | 测试模块协作 |
| `testing/product/` | 产品测试 | 端到端测试 |

---

# 第六部分：关键路径汇总

## 修改某个文件会影响什么？

### 修改 `core/contracts/*.py`
```
影响范围：全局
    ↓
所有使用该契约的模块
    ↓
可能需要同步修改前端types/
```

### 修改 `calculators/bazi/calculator.py`
```
影响范围：八字计算
    ↓
rules/engine.py (获取八字结果)
    ↓
integration/fusion_engine.py (融合)
    ↓
services/narrative/ (叙事)
    ↓
最终输出
```

### 修改 `data/rules/bazi/*.yaml`
```
影响范围：八字规则
    ↓
rules/engine.py (规则匹配)
    ↓
匹配结果变化
    ↓
叙事内容变化
```

### 修改 `典籍/中文典籍/三命通会/`
```
影响范围：需要重新生成
    ↓
运行 logic_chain_builder
    ↓
data/logic_chains/三命通会.yaml
    ↓
运行 codegen
    ↓
backend/semantics/sanming/
    ↓
语义片段更新
```

---

# 第七部分：文件命名规范

## 文件命名模式

| 模式 | 含义 | 示例 |
|------|------|------|
| `*_models.py` | 数据模型定义 | `action_models.py` |
| `*_service.py` | 服务类 | `snippet_service.py` |
| `*_router.py` | 路由/调度 | `scenario/router.py` |
| `*_generator.py` | 生成器 | `narrative/generator.py` |
| `*_config.yaml` | 配置文件 | `dimension_config.yaml` |
| `test_*.py` | 测试文件 | `test_calculator.py` |

## 目录命名模式

| 模式 | 含义 | 示例 |
|------|------|------|
| `tests/` | 测试目录 | 各模块下的tests/ |
| `providers/` | 供应商适配 | `llm/providers/` |
| `migrations/` | 数据库迁移 | `geocoding/migrations/` |
| `generated/` | 自动生成 | `data/rules/generated/` |
| `archive/` | 归档 | `changes/archive/` |
