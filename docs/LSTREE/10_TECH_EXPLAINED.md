# 技术概念通俗讲解

> 本文档用通俗语言解释LS项目中的所有技术概念，让非技术人员也能理解。

## 📚 极致细化版文档

本文档的每个部分都有更详细的极致细化版：

| 文档 | 内容 | 建议阅读场景 |
|------|------|-------------|
| [10A_BASICS_DEEP.md](10A_BASICS_DEEP.md) | 基础概念极致细化 | 完全不懂技术的人 |
| [10B_BACKEND_DEEP.md](10B_BACKEND_DEEP.md) | 后端模块极致细化 | 想了解后端架构 |
| [10C_RULES_SERVICES_DEEP.md](10C_RULES_SERVICES_DEEP.md) | 规则引擎与服务层 | 想了解业务逻辑 |
| [10D_SEMANTICS_FRONTEND_DEEP.md](10D_SEMANTICS_FRONTEND_DEEP.md) | 语义库与前端 | 想了解知识库和界面 |
| [10E_SCRIPTS_DATA_DEEP.md](10E_SCRIPTS_DATA_DEEP.md) | 脚本与数据处理 | 想了解数据流程 |

---

# 第一部分：基础概念

## 什么是"后端"和"前端"？

想象一个餐厅：
- **前端 (Frontend)** = 餐厅大堂，顾客能看到的部分（菜单、桌子、服务员）
- **后端 (Backend)** = 厨房，顾客看不到的部分（厨师做菜、存放食材）

在LS项目中：
- `frontend/` = 用户看到的网页界面（按钮、输入框、显示结果）
- `backend/` = 服务器程序，负责计算八字、占星等，返回结果

---

## 什么是API？

**API = 服务员**

顾客（前端）不能直接进厨房（后端），需要通过服务员（API）点菜。

```
用户点击"算八字" → 前端发送请求到API → 后端计算 → API返回结果 → 前端显示
```

在LS中，`backend/api/routes/` 就是各种"服务员"：
- `bazi.py` = 专门接八字订单的服务员
- `dream.py` = 专门接解梦订单的服务员
- `astro.py` = 专门接占星订单的服务员

---

## 什么是数据库？

**数据库 = 仓库**

存放所有数据的地方，比如：
- 用户信息（账号、密码、生日）
- 计算历史（之前算过的八字）
- 规则数据（命理规则）

LS用三种仓库：
- **PostgreSQL** = 主仓库，存放结构化数据（用户表、订单表）
- **MongoDB** = 文档仓库，存放非结构化数据（语义片段、规则）
- **Redis** = 临时货架，存放经常用的数据（缓存）

---

## 什么是YAML/JSON/Python文件？

**文件格式 = 写信的格式**

不同格式用于不同目的：

| 格式 | 用途 | 类比 |
|------|------|------|
| `.py` | Python程序代码 | 菜谱（告诉厨师怎么做） |
| `.yaml` | 配置和数据 | 食材清单（告诉厨师用什么） |
| `.json` | 数据交换 | 订单（前后端之间传递） |
| `.md` | 文档说明 | 说明书 |
| `.tsx` | 前端组件 | 餐厅装修图纸 |

---

# 第二部分：Backend详解

## backend/api/ - 服务窗口

```
api/
├── main.py          # 【餐厅大门】程序启动入口，打开这个餐厅才能营业
├── models.py        # 【订单格式】规定顾客点菜的格式（生日要写年月日时）
├── routes/          # 【服务台】各种服务窗口
│   ├── analyze.py   # 【综合分析窗口】接收命盘分析请求
│   ├── auth.py      # 【身份验证窗口】登录、注册
│   ├── dream.py     # 【解梦窗口】
│   ├── health.py    # 【健康检查】检查系统是否正常运行
│   └── ...
├── middleware/      # 【门卫】检查每个请求（是否登录、权限等）
└── tests/           # 【质检】测试这些服务是否正常
```

### ⚠️ 潜在冲突点
- `api/models.py` 和 `backend/models/` 都定义数据模型，可能有重复
- `api/services/` 和 `backend/services/` 都叫services，容易混淆

---

## backend/calculators/ - 计算厨房

**这是LS的核心！** 所有命理计算都在这里。

```
calculators/
├── bazi/            # 【八字厨房】
│   ├── calculator.py   # 主厨：排八字的核心逻辑
│   ├── models.py       # 食材定义：天干地支等数据结构
│   ├── service.py      # 上菜员：把计算结果包装好
│   ├── dayun.py        # 帮厨1：专门算大运
│   ├── hidden_stems.py # 帮厨2：专门算藏干
│   ├── solar_terms.py  # 参考资料：节气表
│   ├── ten_gods.py     # 帮厨3：专门算十神
│   └── tests/          # 质检：测试八字算得对不对
│
├── astro/           # 【西占厨房】
│   ├── calculator.py   # 主厨：排星盘（行星、宫位、相位）
│   ├── models.py       # 食材定义：行星、星座等
│   └── service.py      # 上菜员
│
├── dream/           # 【解梦厨房】
│   ├── extractor.py    # 主厨：从梦境描述中提取元素
│   └── models.py       # 食材定义：梦境符号等
│
├── tarot/           # 【塔罗厨房】
│   ├── interpreter.py  # 主厨：解读牌义
│   └── models.py       # 食材定义：78张牌
│
├── yijing/          # 【周易厨房】
│   ├── calculator.py   # 主厨：起卦
│   └── models.py       # 食材定义：64卦
│
└── ziwei/           # 【紫微厨房】
    ├── calculator.py   # 主厨：排紫微盘
    ├── palace_system.py # 帮厨1：十二宫
    ├── star_placement.py # 帮厨2：安星
    ├── sihua.py        # 帮厨3：四化
    └── lunar_calendar.py # 工具：农历转换
```

### 文件命名规律
- `calculator.py` = 核心计算逻辑
- `models.py` = 数据结构定义
- `service.py` = 对外提供服务的包装
- `tests/` = 测试代码

### ⚠️ 潜在冲突点
- 每个calculator都有自己的`models.py`，可能与`core/contracts/`中的模型重复
- `bazi/solar_terms.py` 和 `data/solar_terms/` 可能有重复数据

---

## backend/core/ - 基础设施

**这是餐厅的水电煤气等基础设施**

```
core/
├── cache/           # 【冰箱】存放常用数据，下次直接拿不用重新计算
│
├── contracts/       # 【标准合同】定义所有数据的格式标准
│   ├── base.py          # 基础合同模板
│   ├── action_models.py # 行动建议的格式
│   ├── narrative_models.py # 叙事文本的格式
│   ├── unified_time.py  # 统一时间格式（很重要！不同系统用不同历法）
│   └── unified_dimensions.py # 统一维度（把不同系统的概念对应起来）
│
├── engines/         # 【发动机管理】管理所有计算引擎
│   ├── manager.py       # 引擎调度员：决定用哪个引擎
│   └── constraints.py   # 使用限制：什么情况用什么引擎
│
├── llm/             # 【AI大脑】调用大语言模型
│   ├── client.py        # AI客户端：发送请求给AI
│   ├── router.py        # AI调度：选择用哪个AI（DeepSeek/GPT/Claude）
│   ├── cost_monitor.py  # 成本监控：AI调用要花钱，要记账
│   ├── orchestrator.py  # 编排器：复杂任务拆分成多个AI调用
│   └── providers/       # AI供应商：不同AI的接口适配
│
├── geocoding/       # 【地图服务】把地名转成经纬度（占星需要出生地）
│   ├── service.py       # 地理编码服务
│   ├── providers/       # 地图供应商（Google/百度等）
│   └── repository.py    # 地名缓存：查过的地名存起来
│
└── observability/   # 【监控室】观察系统运行状态
    ├── logging.py       # 日志：记录发生了什么
    ├── metrics.py       # 指标：统计运行数据
    └── tracing.py       # 追踪：跟踪一个请求的完整流程
```

### ⚠️ 潜在冲突点
- `core/contracts/` 是数据契约的唯一来源，但 `calculators/*/models.py` 也定义了模型
- **建议**：所有公共模型应该在 `contracts/` 中，calculators只做私有模型

---

## backend/semantics/ - 语义仓库

**这是LS的知识库！** 存放从典籍中提取的所有语义片段。

```
semantics/
├── core/            # 【图书管理员】负责加载和查找语义片段
│
├── sanming/         # 【三命通会书架】622条规则
│   ├── __init__.py      # 入口
│   ├── heavenly_stems/  # 天干相关片段
│   ├── ten_gods/        # 十神相关片段
│   └── ...
│
├── planets_in_transit/  # 【行星过境书架】645条规则
│   ├── sun_transits/    # 太阳过境
│   ├── moon_transits/   # 月亮过境
│   └── ...
│
└── [其他30本书的书架...]
```

### 语义片段是什么？

一条语义片段 = 一条命理规则，例如：

```yaml
id: sanming_001
source: 三命通会
factor_refs: ["甲木", "子水"]        # 触发条件
interpretation: "甲木生于子月，水旺木相..."  # 解读内容
confidence: 0.85                      # 可信度
```

当用户的八字满足条件时，就会匹配到这条片段，用于生成解读。

### ⚠️ 潜在冲突点
- 语义片段由代码生成器自动生成，手动修改可能被覆盖
- 不同书籍对同一因子组合可能有不同解读（这是设计如此，用于交叉验证）

---

## backend/rules/ - 规则引擎

**这是LS的推理大脑！** 根据规则做判断。

```
rules/
├── engine.py        # 【规则裁判】执行规则判断
├── condition.py     # 【条件解析】理解"如果...那么..."
├── conflict.py      # 【冲突仲裁】多个规则冲突时怎么办
├── context.py       # 【上下文】记住当前在分析谁
├── coverage.py      # 【覆盖率】统计规则覆盖了多少情况
├── reloader.py      # 【热更新】不重启就能更新规则
└── tests/           # 【测试】
```

### 规则引擎工作流程

```
用户八字 → 规则引擎 → 匹配规则 → 找到语义片段 → 生成解读
   ↓           ↓          ↓
甲木日主    检查所有规则   "甲木生子月"规则命中
子月出生                   返回对应解读
```

---

## backend/services/ - 业务服务

**这是各种具体业务功能**

```
services/
├── narrative/       # 【故事讲述员】把计算结果变成好读的文字
│   ├── generator.py     # 叙事生成器
│   ├── prompt_builder.py # 构建给AI的提示词
│   └── snippet_service.py # 选择合适的语义片段
│
├── scenario/        # 【场景路由】判断用户想问什么（事业/感情/健康）
│   └── router.py        # 场景识别和分发
│
├── action_compiler/ # 【行动顾问】把洞察变成具体建议
│   ├── compiler.py      # 编译器：整理行动建议
│   ├── analyzer.py      # 分析器：从多个引擎提取建议
│   └── aggregator.py    # 聚合器：合并去重
│
├── memory/          # 【记忆管家】记住用户的历史
│   ├── service.py       # 记忆服务
│   └── encryption.py    # 加密：保护隐私
│
├── playbook/        # 【行动手册】生成周期性建议
│   └── generator.py     # 生成每日/每周/每月建议
│
├── timeline/        # 【时间线】展示过去和未来的重要节点
│
├── learning/        # 【学习系统】根据用户反馈改进
│
└── safety/          # 【安全卫士】过滤敏感内容
```

### ⚠️ 潜在冲突点
- `api/services/` 和 `backend/services/` 都叫services
  - `api/services/` = API层的轻量服务
  - `backend/services/` = 核心业务服务
  - **建议**：应该合并或重命名避免混淆

---

## backend/integration/ - 融合引擎

**这是LS的特色！** 把多个系统的结果融合。

```
integration/
├── fusion_engine.py     # 【融合主厨】合并多个引擎的结果
├── cross_validator.py   # 【交叉验证】检查不同系统是否矛盾
├── evidence_chain.py    # 【证据链】记录结论的来源
├── theme_mapper.py      # 【主题映射】不同系统的概念对应
└── weight_manager.py    # 【权重管理】不同系统的权重配比
```

### 融合是怎么工作的？

```
八字说：今年财运好 (权重0.4)
紫微说：今年财运一般 (权重0.3)
占星说：今年财运很好 (权重0.3)
        ↓
融合引擎加权平均 → "今年财运偏好，但需注意..."
```

---

# 第三部分：Frontend详解

## 前端技术栈

```
Next.js = 前端框架（类似餐厅的装修风格指南）
React = 组件库（类似模块化家具）
TailwindCSS = 样式工具（类似油漆和装饰）
TypeScript = 带类型的JavaScript（类似有标签的工具箱）
```

## 前端结构

```
frontend/src/
├── app/             # 【页面】每个页面对应一个路由
│   ├── layout.tsx       # 页面布局（头部、侧边栏）
│   └── page.tsx         # 首页
│
├── components/      # 【组件】可复用的界面元素
│   ├── DreamRecorder.tsx    # 梦境录入组件
│   ├── views/               # 各种视图组件
│   │   ├── BaziView/        # 八字结果显示
│   │   ├── AstroView/       # 占星结果显示
│   │   └── ...
│   └── layout/              # 布局组件
│
├── hooks/           # 【钩子】可复用的逻辑
│   ├── useAuth.ts       # 认证逻辑
│   └── useApi.ts        # API调用逻辑
│
├── lib/             # 【工具库】通用工具函数
│
├── types/           # 【类型定义】数据格式说明
│
└── styles/          # 【样式】CSS文件
```

### ⚠️ 潜在冲突点
- `frontend/src/types/` 和 `backend/core/contracts/` 定义相同数据的类型
  - 前端用TypeScript，后端用Python
  - **必须保持同步**，否则数据传输会出错

---

# 第四部分：Scripts详解

## 脚本是什么？

**脚本 = 一次性或定期运行的工具程序**

不像后端一直运行等请求，脚本是"用完即走"。

## 主要脚本

```
scripts/
├── codegen/                 # 【代码生成器】★最重要★
│   ├── semantic_generator.py    # 从典籍生成语义模块代码
│   ├── rule_generator.py        # 从规则YAML生成代码
│   └── ...
│
├── knowledge_graph_builder/ # 【知识图谱构建】
│   └── ...                      # 把语义片段连接成图谱
│
├── logic_chain_builder/     # 【逻辑链构建】
│   └── ...                      # 从典籍提取推理链
│
└── rule_converter/          # 【规则转换器】
    └── ...                      # 把结构化文本转成YAML规则
```

### 代码生成流程

```
典籍/中文典籍/三命通会/  →  scripts/codegen/  →  backend/semantics/sanming/
     (原文)                 (生成器)              (Python代码)
```

### ⚠️ 潜在冲突点
- `backend/semantics/` 的代码是**自动生成**的
- 如果手动修改，下次运行codegen会被覆盖
- **安全做法**：只修改典籍源文件，然后重新生成

---

# 第五部分：Data详解

## 数据目录结构

```
data/
├── rules/           # 【规则仓库】各引擎的规则定义
│   ├── bazi/            # 八字规则
│   ├── astro/           # 占星规则
│   └── generated/       # ⚠️ 自动生成的规则，勿手动改
│
├── factor_ontology/ # 【因子本体】定义所有因子
│   ├── namespace.yaml   # 因子命名空间
│   ├── candidates/      # 候选因子（待审核）
│   └── certified/       # 已认证因子（正式使用）
│
├── logic_chains/    # 【逻辑链】从典籍提取的推理链
│   ├── 三命通会.yaml        # 26MB，最大
│   ├── planets_in_transit.yaml  # 19MB
│   └── ...
│
├── knowledge_graph/ # 【知识图谱配置】
│   ├── dimension_config.yaml    # 维度配置
│   └── conflict_templates.yaml  # 冲突处理模板
│
└── scenario_templates/  # 【场景模板】
    ├── career.yaml          # 事业咨询模板
    ├── relationship.yaml    # 感情咨询模板
    └── ...
```

### ⚠️ 潜在冲突点
- `data/rules/generated/` 是自动生成的，手动修改会丢失
- `data/factor_ontology/candidates/` 和 `certified/` 需要人工审核流程
- `典籍/因子本体/` 和 `data/factor_ontology/` 可能有重复
  - **建议**：`典籍/因子本体/` 是源，`data/` 是生成结果

---

# 第六部分：配置文件详解

## 环境变量 (.env)

```bash
# 数据库连接（像餐厅的水电地址）
DATABASE_URL=postgresql://user:pass@localhost:5432/lucidself
MONGODB_URL=mongodb://localhost:27017/lucidself
REDIS_URL=redis://localhost:6379

# AI服务密钥（像进入VIP区的钥匙）
OPENAI_API_KEY=sk-xxx        # OpenAI的钥匙
DEEPSEEK_API_KEY=xxx         # DeepSeek的钥匙
ANTHROPIC_API_KEY=xxx        # Claude的钥匙

# 安全配置
JWT_SECRET=xxx               # 登录令牌加密密钥
ENCRYPTION_KEY=xxx           # 数据加密密钥
```

### ⚠️ 安全警告
- `.env` 文件包含敏感信息，**绝对不能**提交到Git
- `.env.example` 是模板，可以提交

## Docker配置

```yaml
# docker-compose.yml 定义了所有服务
services:
  backend:     # 后端服务
  frontend:    # 前端服务
  postgres:    # PostgreSQL数据库
  mongodb:     # MongoDB数据库
  redis:       # Redis缓存
  nginx:       # 反向代理（门卫，分发请求）
```

---

# 第七部分：冲突点汇总

## 🔴 高风险冲突

| 位置1 | 位置2 | 问题 | 建议 |
|-------|-------|------|------|
| `backend/semantics/` | `scripts/codegen/` | 语义代码是自动生成的 | 只改源文件，重新生成 |
| `data/rules/generated/` | 手动修改 | 生成的规则会被覆盖 | 勿手动修改generated目录 |
| `frontend/src/types/` | `backend/core/contracts/` | 前后端类型必须一致 | 建立同步机制 |

## 🟡 中风险冲突

| 位置1 | 位置2 | 问题 | 建议 |
|-------|-------|------|------|
| `api/models.py` | `backend/models/` | 都定义数据模型 | 统一到contracts |
| `api/services/` | `backend/services/` | 命名混淆 | 重命名区分 |
| `典籍/因子本体/` | `data/factor_ontology/` | 可能重复 | 明确源和生成物 |
| `calculators/*/models.py` | `core/contracts/` | 模型定义分散 | 公共模型统一管理 |

## 🟢 低风险/设计如此

| 位置1 | 位置2 | 说明 |
|-------|-------|------|
| 不同书籍的语义片段 | 同一因子组合 | 设计如此，用于交叉验证 |
| 多个calculator | 同一时间 | 设计如此，融合引擎会合并 |

---

# 第八部分：数据流向图

## 用户请求的完整流程

```
用户输入生日
    ↓
┌─────────────────┐
│   Frontend      │  1. 收集用户输入
│   (React)       │  2. 发送API请求
└────────┬────────┘
         ↓
┌─────────────────┐
│   API Layer     │  3. 验证请求格式
│   (FastAPI)     │  4. 路由到对应服务
└────────┬────────┘
         ↓
┌─────────────────┐
│   Services      │  5. 业务逻辑处理
│                 │  6. 调用计算器
└────────┬────────┘
         ↓
┌─────────────────────────────────────────┐
│   Calculators (并行执行)                 │
│   ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐  │
│   │ 八字 │ │ 紫微 │ │ 占星 │ │ ...  │  │  7. 各引擎计算
│   └──────┘ └──────┘ └──────┘ └──────┘  │
└────────────────────┬────────────────────┘
                     ↓
┌─────────────────┐
│   Rules Engine  │  8. 规则匹配
│                 │  9. 查找语义片段
└────────┬────────┘
         ↓
┌─────────────────┐
│   Semantics     │  10. 返回匹配的片段
│   (语义库)      │
└────────┬────────┘
         ↓
┌─────────────────┐
│   Integration   │  11. 融合多引擎结果
│   (融合引擎)    │  12. 解决冲突
└────────┬────────┘
         ↓
┌─────────────────┐
│   Narrative     │  13. 调用LLM
│   (叙事服务)    │  14. 生成文字
└────────┬────────┘
         ↓
┌─────────────────┐
│   LLM Core      │  15. 选择模型
│   (AI调用)      │  16. 发送请求
└────────┬────────┘
         ↓
返回给用户
```

---

# 第九部分：常见问题

## Q: 为什么有这么多models.py？

每个模块都需要定义自己的数据结构。理想状态下：
- **公共模型** → `core/contracts/`
- **私有模型** → 各模块内部

## Q: 语义片段从哪来？

```
典籍原文 → 人工结构化 → logic_chains/*.yaml → codegen → semantics/*.py
```

## Q: 修改规则会影响什么？

修改 `data/rules/` → 规则引擎读取 → 影响匹配结果 → 影响最终解读

## Q: 前后端怎么保持同步？

目前**手动同步**。建议未来：
1. 从 `contracts/` 自动生成 TypeScript 类型
2. 或使用 OpenAPI 规范自动同步
