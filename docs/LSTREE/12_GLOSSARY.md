# 术语表 - 技术名词通俗解释

> 按字母顺序排列，方便查找

---

## A

### API (Application Programming Interface)
**通俗解释**: 程序之间的"翻译官"或"服务员"

就像餐厅的服务员：顾客（前端）通过服务员（API）向厨房（后端）点菜，服务员把菜端回来。

**在LS中**: `backend/api/` 目录下的文件就是各种API接口。

---

### Authentication (认证)
**通俗解释**: 验证"你是谁"

就像进入公司要刷工卡，证明你是员工。

**在LS中**: `backend/api/routes/auth.py` 处理登录注册。

---

## B

### Backend (后端)
**通俗解释**: 用户看不到的服务器程序

就像餐厅的厨房，顾客看不到，但所有菜都在这里做。

**在LS中**: `backend/` 目录，用Python写的服务程序。

---

## C

### Cache (缓存)
**通俗解释**: 临时存放常用数据的地方

就像厨房的备菜区，常用的食材提前切好放着，用的时候直接拿。

**在LS中**: Redis做缓存，`backend/core/cache/` 管理缓存逻辑。

---

### Calculator (计算器)
**通俗解释**: 执行具体计算的模块

在LS中特指命理计算器：八字排盘、星盘计算等。

**在LS中**: `backend/calculators/` 目录下的各个引擎。

---

### CLI (Command Line Interface)
**通俗解释**: 命令行工具

用文字命令操作程序，不用图形界面。

**在LS中**: `scripts/*/cli.py` 是各种命令行工具。

---

### Codegen (Code Generation)
**通俗解释**: 代码生成器

自动写代码的程序。输入数据，输出代码文件。

**在LS中**: `scripts/codegen/` 从典籍数据生成Python代码。

---

### Component (组件)
**通俗解释**: 可重复使用的界面部件

就像乐高积木，可以组合成各种东西。

**在LS中**: `frontend/src/components/` 下的各种UI组件。

---

### Contract (契约/合同)
**通俗解释**: 数据格式的约定

规定数据长什么样，有哪些字段，是什么类型。

**在LS中**: `backend/core/contracts/` 定义所有数据格式。

---

## D

### Database (数据库)
**通俗解释**: 存放数据的仓库

**LS用三种**:
- PostgreSQL: 关系型数据库（像Excel表格）
- MongoDB: 文档数据库（像文件柜）
- Redis: 内存数据库（像临时便签）

---

### Docker
**通俗解释**: 程序的"集装箱"

把程序和它需要的所有东西打包在一起，搬到哪里都能运行。

**在LS中**: `docker/` 和 `docker-compose.yml` 定义如何打包和运行。

---

### Dependency (依赖)
**通俗解释**: 程序需要的其他程序/库

就像做菜需要原料，程序也需要其他库才能运行。

**在LS中**: `requirements.txt` 列出所有Python依赖。

---

## E

### Engine (引擎)
**通俗解释**: 核心计算模块

在LS中指各个命理系统的计算核心。

**在LS中**: 
- `backend/calculators/bazi/` = 八字引擎
- `backend/calculators/astro/` = 占星引擎
- `backend/rules/engine.py` = 规则引擎

---

### Endpoint (端点)
**通俗解释**: API的具体地址

就像商店的柜台，不同柜台卖不同东西。

**在LS中**: `/api/analyze` 是分析端点，`/api/dream` 是解梦端点。

---

### Environment Variable (环境变量)
**通俗解释**: 程序运行时的配置参数

就像餐厅的营业时间、价格表，不写死在程序里，可以随时改。

**在LS中**: `.env` 文件存放环境变量。

---

## F

### Factor (因子)
**通俗解释**: 命理系统中的基本元素

**在LS中**: 
- 八字因子: 甲、乙、子、丑、比肩、劫财...
- 占星因子: 太阳、月亮、上升、合相...
- 塔罗因子: 愚者、魔术师、权杖...

---

### FastAPI
**通俗解释**: Python的Web框架

用来写API接口的工具，特点是快、自动生成文档。

**在LS中**: 后端用FastAPI，入口是 `backend/api/main.py`。

---

### Frontend (前端)
**通俗解释**: 用户看到的界面

就像餐厅大堂，菜单、桌子、装修，顾客能看到的部分。

**在LS中**: `frontend/` 目录，用React/Next.js写的网页。

---

### Fusion (融合)
**通俗解释**: 把多个结果合并

LS的特色功能，把八字、占星等多个系统的结果合并成一个。

**在LS中**: `backend/integration/fusion_engine.py`。

---

## G

### Geocoding (地理编码)
**通俗解释**: 把地名变成经纬度

占星需要出生地的经纬度，所以要把"北京"变成"39.9°N, 116.4°E"。

**在LS中**: `backend/core/geocoding/`。

---

### Git
**通俗解释**: 代码版本管理工具

记录代码的每次修改，可以随时回退。

**在LS中**: `.gitignore` 告诉Git哪些文件不要记录。

---

## H

### Hook (钩子)
**通俗解释**: React中可复用的逻辑

把常用的逻辑提取出来，多个地方都能用。

**在LS中**: `frontend/src/hooks/` 下的 `useAuth.ts` 等。

---

## I

### Integration (集成)
**通俗解释**: 把不同部分连接起来

**在LS中**: `backend/integration/` 负责融合多个引擎的结果。

---

## J

### JSON (JavaScript Object Notation)
**通俗解释**: 一种数据格式

像这样: `{"name": "张三", "age": 25}`

用于程序之间传递数据。

---

### JWT (JSON Web Token)
**通俗解释**: 登录令牌

登录成功后服务器给你一个"通行证"，之后每次请求都带着它。

---

## L

### LLM (Large Language Model)
**通俗解释**: 大语言模型，即AI

ChatGPT、Claude、DeepSeek这类能理解和生成文字的AI。

**在LS中**: `backend/core/llm/` 管理AI调用。

---

### Logic Chain (逻辑链)
**通俗解释**: 推理链条

从典籍中提取的"如果A，那么B"的推理规则。

**在LS中**: `data/logic_chains/` 存放从各书提取的逻辑链。

---

## M

### Middleware (中间件)
**通俗解释**: 请求处理的"关卡"

每个请求都要经过这些关卡，检查权限、记录日志等。

**在LS中**: `backend/api/middleware/`。

---

### Model (模型)
**通俗解释**: 数据的结构定义

规定一个"用户"应该有名字、邮箱、密码等字段。

**在LS中**: 
- `backend/models/` = 数据库模型
- `*/models.py` = 数据结构定义

---

### MongoDB
**通俗解释**: 文档数据库

像文件柜一样存放JSON文档，灵活但不如Excel那样严格。

---

## N

### Narrative (叙事)
**通俗解释**: 讲故事，生成文字描述

把计算结果变成用户能读懂的文字。

**在LS中**: `backend/services/narrative/`。

---

### Next.js
**通俗解释**: React的升级框架

让React更容易做网站，自带路由、服务器渲染等功能。

**在LS中**: 前端用Next.js 14。

---

## O

### Ontology (本体)
**通俗解释**: 概念的定义和分类

定义"什么是什么"，比如定义"甲木"是天干、属阳、属木。

**在LS中**: `data/factor_ontology/` 定义所有因子。

---

### OpenSpec
**通俗解释**: LS项目的变更管理规范

规定怎么提出修改、怎么审核、怎么实现。

**在LS中**: `openspec/` 目录。

---

### Orchestrator (编排器)
**通俗解释**: 调度员

决定按什么顺序做什么事，协调多个服务。

**在LS中**: `backend/core/llm/orchestrator.py` 编排AI调用。

---

## P

### Pipeline (流水线)
**通俗解释**: 处理流程

像工厂流水线，数据一步步处理。

**在LS中**: `backend/pipeline/` 编排计算流程。

---

### PostgreSQL
**通俗解释**: 关系型数据库

像Excel表格一样存数据，有行有列，适合结构化数据。

---

### Provider (提供者)
**通俗解释**: 服务供应商

**在LS中**: 
- `core/llm/providers/` = 不同AI供应商(OpenAI, DeepSeek...)
- `core/geocoding/providers/` = 不同地图服务商

---

### Pydantic
**通俗解释**: Python的数据验证库

自动检查数据格式对不对，错了就报错。

---

## R

### React
**通俗解释**: 前端框架

用组件方式搭建网页界面，像搭乐高。

---

### Redis
**通俗解释**: 内存数据库

数据存在内存里，超级快，但重启会丢失。用于缓存。

---

### Repository (仓库)
**通俗解释**: 数据访问层

专门负责从数据库读写数据的代码。

**在LS中**: `backend/repositories/`。

---

### Route (路由)
**通俗解释**: URL地址的处理规则

决定用户访问某个地址时，执行什么代码。

**在LS中**: `backend/api/routes/` 定义各个API路由。

---

### Rules Engine (规则引擎)
**通俗解释**: 根据规则做判断的系统

输入条件，根据规则库判断，输出结论。

**在LS中**: `backend/rules/engine.py`。

---

## S

### Schema
**通俗解释**: 数据的格式定义

规定数据应该长什么样。

**在LS中**: 
- `data/schema_staging/` = 数据Schema
- `data/factor_ontology/factor_schema.yaml` = 因子Schema

---

### Semantic (语义)
**通俗解释**: 含义、意思

**在LS中**: "语义片段"是从典籍提取的带含义的规则。

---

### Service (服务)
**通俗解释**: 提供特定功能的模块

**在LS中**: `backend/services/` 各种业务服务。

---

### Snippet (片段)
**通俗解释**: 一小段内容

**在LS中**: "语义片段"是一条命理规则+解读。

---

## T

### TailwindCSS
**通俗解释**: CSS工具库

用类名来写样式，不用自己写CSS。

---

### Test (测试)
**通俗解释**: 检验代码是否正确

写测试代码自动检查功能是否正常。

**在LS中**: 各模块下的 `tests/` 目录。

---

### TypeScript
**通俗解释**: 带类型的JavaScript

比JavaScript多了类型检查，减少错误。

---

## U

### Unified (统一)
**通俗解释**: 把不同的东西统一起来

**在LS中**: 
- `unified_time.py` = 统一时间格式
- `unified_dimensions.py` = 统一维度定义

---

## V

### Validation (验证)
**通俗解释**: 检查数据是否合法

比如检查邮箱格式对不对、年龄是不是数字。

---

## W

### Workflow (工作流)
**通俗解释**: 工作流程

**在LS中**: `.windsurf/workflows/` 定义开发工作流程。

---

## Y

### YAML
**通俗解释**: 一种配置文件格式

比JSON更易读，用缩进表示层级：
```yaml
name: 张三
age: 25
hobbies:
  - 读书
  - 编程
```

**在LS中**: 规则、配置大多用YAML格式。

---

# 快速对照表

| 技术术语 | 类比 | LS中的位置 |
|----------|------|------------|
| Backend | 厨房 | `backend/` |
| Frontend | 大堂 | `frontend/` |
| API | 服务员 | `backend/api/` |
| Database | 仓库 | PostgreSQL/MongoDB/Redis |
| Cache | 冰箱 | Redis, `core/cache/` |
| Calculator | 厨师 | `calculators/` |
| Rules Engine | 菜谱 | `rules/` |
| Semantics | 食材库 | `semantics/` |
| LLM | AI助手 | `core/llm/` |
| Narrative | 讲解员 | `services/narrative/` |
| Codegen | 自动化机器 | `scripts/codegen/` |
