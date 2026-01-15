# 配置与工具文档

## 目录总览

```
LucidSelf/
├── .windsurf/            # Windsurf IDE配置
├── .kiro/                # Kiro配置
├── .vscode/              # VSCode配置
├── .github/              # GitHub Actions
├── docker/               # Docker配置
├── docker-compose.yml    # Docker编排
├── requirements.txt      # Python依赖
└── .pre-commit-config.yaml  # Pre-commit配置
```

---

## 1. .windsurf/ - Windsurf IDE配置

```
.windsurf/
├── memory_graph.json     # 记忆图谱
├── rules/                # Agent规则 (12个)
└── workflows/            # 工作流 (3个)
```

### rules/ - Agent规则
| 规则文件 | 用途 |
|----------|------|
| `KG-agent.md` | 知识图谱构建Agent |
| `L3-rules-agent.md` | L3层规则提取Agent |
| `engine-agent.md` | 引擎开发Agent |
| `eval-agent.md` | 评估Agent |
| `factor-ontology-agent.md` | 因子本体Agent |
| `logic-agent.md` | 逻辑链Agent |
| `ls-system-commander.md` | 系统指挥官 |
| `rule-for-all.md` | 全局规则 |
| `rules-bazi-agent-rules-astro-agent-rules-dream-agent.md` | 多引擎规则 |
| `semantics-agent.md` | 语义Agent |
| `text-cn-agent.md` | 中文典籍Agent |
| `text-en-agent.md` | 英文典籍Agent |

### workflows/ - 工作流
| 工作流 | 触发命令 | 用途 |
|--------|----------|------|
| `openspec-proposal.md` | `/openspec-proposal` | 创建变更提案 |
| `openspec-apply.md` | `/openspec-apply` | 实现变更 |
| `openspec-archive.md` | `/openspec-archive` | 归档变更 |

---

## 2. docker/ - Docker配置

```
docker/
├── Dockerfile            # 后端Docker镜像
└── nginx.conf            # Nginx配置
```

### docker-compose.yml 服务定义
```yaml
services:
  backend:              # FastAPI后端
  frontend:             # Next.js前端
  postgres:             # PostgreSQL数据库
  mongodb:              # MongoDB数据库
  redis:                # Redis缓存
  nginx:                # Nginx反向代理
```

---

## 3. requirements.txt - Python依赖

核心依赖:
```
fastapi>=0.104.0
pydantic>=2.0.0
sqlalchemy>=2.0.0
httpx>=0.25.0
python-jose>=3.3.0
passlib>=1.7.4
redis>=5.0.0
motor>=3.3.0
```

---

## 4. .pre-commit-config.yaml

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
  - repo: https://github.com/psf/black
    hooks:
      - id: black
  - repo: https://github.com/pycqa/isort
    hooks:
      - id: isort
  - repo: https://github.com/pycqa/flake8
    hooks:
      - id: flake8
```

---

## 5. 环境变量

### backend/.env.example
```env
# 数据库
DATABASE_URL=postgresql://...
MONGODB_URL=mongodb://...
REDIS_URL=redis://...

# LLM
OPENAI_API_KEY=...
DEEPSEEK_API_KEY=...
ANTHROPIC_API_KEY=...

# 安全
JWT_SECRET=...
ENCRYPTION_KEY=...

# 服务
DEBUG=false
LOG_LEVEL=INFO
```

### frontend/.env.example
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_WS_URL=ws://localhost:8000
```

---

## 6. 根目录文档

| 文档 | 用途 | 大小 |
|------|------|------|
| `README.md` | 项目说明 | 10KB |
| `AGENTS.md` | AI助手入口指令 | 0.6KB |
| `LLM灵芽api配置.md` | LLM API详细配置 | 84KB |
| `LLM调用及成本方案.md` | LLM成本优化方案 | 34KB |
| `Playbook-TODO.md` | Playbook待办事项 | 53KB |
| `coverage_matrix_report.json` | 测试覆盖率报告 | 10KB |

---

## 7. 开发命令速查

### 后端
```bash
# 启动开发服务器
cd backend && uvicorn api.main:app --reload

# 运行测试
pytest backend/

# 代码检查
black backend/ && isort backend/ && flake8 backend/
```

### 前端
```bash
# 启动开发服务器
cd frontend && npm run dev

# 构建
npm run build

# 代码检查
npm run lint
```

### Docker
```bash
# 启动所有服务
docker-compose up -d

# 查看日志
docker-compose logs -f backend

# 重建
docker-compose up --build
```

### 脚本
```bash
# 代码生成
python -m scripts.codegen

# 知识图谱
python -m scripts.knowledge_graph_builder

# 逻辑链
python -m scripts.logic_chain_builder

# 规则转换
python -m scripts.rule_converter
```
