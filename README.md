# LucidSelf - 个人自注系统

**Personal Exegesis System: 结构化命理 + 梦境互文 + 可解释推理 + 长期版本管理**

---

## 项目定位

LucidSelf 不是传统的占星/算命 App，而是一个**长期个人叙事管理系统**，核心价值：

1. **可解释推理**：每个结论都有清晰的证据链，可追溯到典籍原文
2. **可追溯版本**：像 Git 一样管理你的"自我认知史"
3. **持续校准**：基于用户反馈不断优化个性化推理
4. **跨域互文**：命理、梦境、现实事件三重验证

**商业逻辑：** LTV（生命周期价值）和 ARPPU（单用户付费额）导向，不追求 DAU。目标用户是愿意为"长期精神结构与叙事管理"付费的"结构控/自省型"用户。

---

## 系统架构

```
用户交互层 → 叙事层 → 推理层 → 数据层 ← 生命周期层
```

### 核心模块

1. **数据层**：规则库、用户状态、梦境记录、事件时间轴、反馈数据
2. **推理层**：规则引擎、冲突解决器、不确定性校准器、个性化权重引擎
3. **叙事层**：LLM 接口、结论卡生成器、证据链可视化、行动模板生成器
4. **生命周期层**：节律触发器、版本管理系统、年鉴编辑器、复盘引擎

详细架构设计见 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

---

## 技术栈

### 后端
- **语言：** Python 3.11+
- **框架：** FastAPI（高性能异步 API）
- **数据库：** PostgreSQL + MongoDB + Redis
- **任务队列：** Celery + Redis

### 前端
- **框架：** React + TypeScript
- **UI：** Tailwind CSS + shadcn/ui
- **状态管理：** Zustand
- **可视化：** D3.js

### 基础设施
- **容器化：** Docker + Docker Compose
- **版本控制：** Git + GitHub
- **CI/CD：** GitHub Actions

---

## 文档目录

| 文档 | 描述 |
|-----|------|
| [ARCHITECTURE.md](docs/ARCHITECTURE.md) | 系统架构设计总览 |
| [规则库结构化设计文档.md](docs/规则库结构化设计文档.md) | 规则库结构化格式 |
| [数据库Schema设计文档.md](docs/数据库Schema设计文档.md) | 数据库 Schema 设计 |
| [项目实施路线.md](docs/项目实施路线.md) | 实施路线图（50周计划） |
| [ROADMAP.md](docs/ROADMAP.md) | 实施路线图（精简版） |

---

## 设计补充说明（2025-11-13）

- 新增/补充的设计要点：
  - 规则 DSL 与数据契约（递归 `Clause`、统一算子语义）
  - 冲突合成策略（强化/抵消/并列/优先级）
  - 不确定性校准（统一 `confidence` 口径，ECE 指标）
  - 个性化权重（全局+个人偏置，反馈驱动，含衰减/回滚）
  - 可复现性与版本化（规则包 hash、输入 hash、engine 版本）
  - API 最小边界与可观测性（结构化日志/指标/追踪）
  - 可度量验收标准（覆盖率、ECE、回放提升、测试覆盖）

- 变更理由：将理念落到工程契约与指标，统一口径，降低后期重构成本与讨论分歧。

- 快速定位：
  - ARCHITECTURE.md 第11节“设计补充与统一口径”。
  - 规则库结构化设计文档 第10节“规则 DSL 与校验规范”。
  - 数据库Schema设计文档 第8-12节“可复现/可观测/单库起步/验收指标/变更理由”。
  - 项目实施路线.md 末尾“修订补充（2025-11-13）”。
  - ROADMAP.md 末尾“修订补充（2025-11-13）”。

---

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/your-username/LucidSelf.git
cd LucidSelf
```

### 2. 启动开发环境

```bash
# 启动数据库服务
docker-compose up -d

# 安装后端依赖
cd backend
pip install -r requirements.txt

# 运行后端
uvicorn api.main:app --reload

# 安装前端依赖（另开终端）
cd frontend
npm install

# 运行前端
npm run dev
```

### 3. 访问应用

- 前端：http://localhost:3000
- 后端 API：http://localhost:8000
- API 文档：http://localhost:8000/docs

---

## 项目结构

```
LucidSelf/
├── backend/              # 后端代码
│   ├── api/             # FastAPI 应用
│   ├── core/            # 核心推理引擎
│   │   ├── bazi/       # 八字计算
│   │   ├── dream/      # 梦境解析
│   │   ├── inference/  # 推理引擎
│   │   └── ziwei/      # 紫微斗数
│   ├── models/          # 数据模型
│   ├── services/        # 业务逻辑
│   ├── utils/           # 工具函数
│   └── tests/           # 测试
├── frontend/            # 前端代码
│   ├── src/
│   │   ├── components/ # UI 组件
│   │   ├── pages/      # 页面
│   │   ├── services/   # API 服务
│   │   └── utils/      # 工具函数
│   └── public/         # 静态资源
├── data/                # 数据文件
│   ├── rules/          # 规则库 JSON
│   ├── factors/        # 因子定义
│   └── sources/        # 典籍元数据
├── docs/                # 文档
├── scripts/             # 脚本工具
├── docker/              # Docker 配置
└── README.md           # 本文件
```

---

## 实施路线图

### Phase 0: 项目初始化（Week 1-2）
- ✅ 代码仓库创建
- ⏳ Docker 环境搭建
- ⏳ 基础项目框架

### Phase 1: MVP - 核心推理系统（Week 3-10）
- 八字计算模块
- 规则库 v0.1（40条核心规则）
- 推理引擎 v0.1
- 基础 API 与数据库
- 前端 MVP

**目标：** 验证核心假设 —— "用户愿意为可解释、可追溯的命理推理买单"

### Phase 2: 梦境功能（Week 11-18）
- 梦境记录与解析
- 梦境规则库（30条）
- 跨域推理（梦境+命理）

### Phase 3: 个性化与反馈闭环（Week 19-26）
- 个性化权重引擎
- 事件时间轴
- 复盘功能

### Phase 4: 版本管理与年鉴（Week 27-34）
- 版本快照系统
- LLM 集成
- 年鉴编辑器

### Phase 5: 紫微斗数与高级功能（Week 35-50）
- 紫微斗数计算
- 时运系统
- 高级可视化

详细计划见 [docs/IMPLEMENTATION_ROADMAP.md](docs/IMPLEMENTATION_ROADMAP.md)

---

## 核心特性

### 1. 可解释推理
每个结论都包含：
- 证据链：显示哪些规则支持这个结论
- 典籍引用：追溯到原文出处
- 置信度：量化的确定性程度
- 反事实推演：如果条件改变，结论会如何变化

### 2. 长期版本管理
- 每次推理生成一个版本快照
- 可以回看历史时刻的推理结果
- 年鉴自动汇编年度数据
- 对比预测与实际结果，持续校准

### 3. 梦境互文
- 梦境不是孤立解读，而是与命理、事件交叉验证
- 梦境高频元素可能预示命局变化
- 梦境情绪与现实事件关联分析

### 4. 个性化校准
- 基于用户反馈动态调整规则权重
- 每个用户有独立的权重配置
- 全局规则 + 个人偏置 = 个性化推理

---

## 规则库设计

### 规则结构

```json
{
  "rule_id": "bazi_001_jia_wood_spring",
  "version": "1.0.0",
  "source": {
    "source_id": "dts",
    "chapter": "通神论",
    "original_text": "甲木参天，脱胎要火。春不容金，秋不容土。"
  },
  "conditions": {
    "operator": "AND",
    "clauses": [
      {"factor": "day_master", "operator": "equals", "value": "甲"},
      {"factor": "birth_season", "operator": "equals", "value": "spring"}
    ]
  },
  "conclusion": {
    "domain": "personality",
    "statement": "你如同春日的大树，充满生命力和创造力",
    "confidence_base": 0.7
  },
  "weight": 0.8
}
```

### 规则来源优先级（MVP）

**Phase 1：40条核心八字规则**
1. 十天干基础特性（10条）- 滴天髓·通神论
2. 季节与五行生克（10条）
3. 十神基础（10条）- 渊海子平
4. 格局基础（10条）

**Phase 2：30条梦境规则**
1. 梦林玄解：水、火、人物、动物、建筑
2. 周公解梦：飞行、掉落、追逐等高频场景

详细设计见 [docs/RULE_STRUCTURE.md](docs/RULE_STRUCTURE.md)

---

## 数据库设计

### PostgreSQL 表
- `users` - 用户账户
- `user_bazi_states` - 用户八字状态
- `user_ziwei_states` - 紫微斗数状态
- `user_events` - 事件时间轴
- `user_feedback` - 反馈记录
- `inference_history` - 推理历史
- `personalized_weights` - 个性化权重
- `version_snapshots` - 版本快照

### MongoDB 集合
- `rules` - 规则库
- `dreams` - 梦境记录
- `inference_results` - 推理结果
- `snapshots` - 版本快照内容

### Redis
- 用户会话
- 推理结果缓存
- 规则索引缓存

详细设计见 [docs/DATABASE_SCHEMA.md](docs/DATABASE_SCHEMA.md)

---

## 开发指南

### 代码风格
- Python: PEP 8 + Black formatter
- TypeScript: ESLint + Prettier
- 变量命名：英文（代码）+ 中文（注释）

### 测试要求
- 单元测试覆盖率 >70%
- 核心推理引擎覆盖率 >80%
- 每个 API 端点都有测试

### Git 工作流
- `main` - 生产环境
- `develop` - 开发环境
- `feature/*` - 功能分支
- Pull Request + Code Review

---

## 部署

### 开发环境
```bash
docker-compose -f docker-compose.dev.yml up
```

### 生产环境
```bash
# 构建镜像
docker-compose -f docker-compose.prod.yml build

# 启动服务
docker-compose -f docker-compose.prod.yml up -d

# 数据库迁移
docker-compose exec backend alembic upgrade head
```

---

## 贡献

欢迎贡献代码、规则库、文档！

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

---

## 许可证

[MIT License](LICENSE)

---

## 联系方式

- 项目主页：https://github.com/your-username/LucidSelf
- 问题反馈：https://github.com/your-username/LucidSelf/issues
- 邮箱：your-email@example.com

---

## 致谢

- **典籍来源：** 滴天髓、渊海子平、紫微斗数、梦林玄解、周易
- **技术框架：** FastAPI, React, PostgreSQL, MongoDB
- **开源社区：** 感谢所有贡献者

---

**LucidSelf：让你的自我认知，像代码一样版本管理。**

## 分层语义提取（三层结构）

- 三层设计：
  - Layer 1：原文保留（可追溯）
  - Layer 2：核心语义（结构化理解）
  - Layer 3：应用规则（情境适配）
- 内容阶段优先：先建 40–50 条核心语义，再派生 100–150 条应用规则；运行时组合叙事，LLM 仅做润色。
- 详细设计：
  - ARCHITECTURE.md 第 12 节
  - 规则库结构化设计文档 第 11 节
  - 数据库Schema设计文档 第 13 节
  - 项目实施路线.md 附录 E