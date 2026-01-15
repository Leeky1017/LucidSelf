# Services 业务服务详细结构

## 目录总览

```
backend/services/
├── action_compiler/      # 行动编译器
├── auth/                 # 认证服务
├── learning/             # 学习服务
├── life_version/         # 生命版本服务
├── memory/               # 记忆服务
├── narrative/            # 叙事服务
├── playbook/             # Playbook服务
├── preference/           # 偏好服务
├── safety/               # 安全服务
├── scenario/             # 场景服务
├── subscription/         # 订阅服务
├── timeline/             # 时间线服务
├── todo/                 # 待办服务
└── version_tree/         # 版本树服务
```

---

## 1. action_compiler/ - 行动编译器

将洞察转化为可执行行动

```
action_compiler/
├── __init__.py           # 模块入口
├── compiler.py           # 行动编译器核心 (13KB)
├── analyzer.py           # 洞察分析器 (20KB)
├── aggregator.py         # 行动聚合器 (8KB)
├── prompts.py            # LLM提示词 (3.8KB)
├── schemas.py            # 数据Schema (3.4KB)
└── tests/                # 测试
```

**核心流程**:
1. 分析多引擎洞察
2. 提取行动建议
3. 聚合去重
4. 生成优先级排序

---

## 2. narrative/ - 叙事服务

生成个性化叙事文本

```
narrative/
├── __init__.py           # 模块入口
├── generator.py          # 叙事生成器 (12KB)
├── prompt_builder.py     # 提示词构建 (8.8KB)
├── snippet_service.py    # 片段服务 (8.9KB)
└── tests/                # 测试
```

**核心功能**:
- 语义片段选择
- 上下文融合
- LLM叙事生成
- 风格定制

---

## 3. scenario/ - 场景服务

管理用户查询场景

```
scenario/
├── __init__.py           # 模块入口
├── models.py             # 场景模型 (3.2KB)
├── router.py             # 场景路由器 (11KB)
└── tests/                # 测试
```

**支持场景**:
- 事业决策
- 感情咨询
- 健康评估
- 财务规划
- 时机选择
- 通用问答

---

## 4. memory/ - 记忆服务

用户记忆管理与加密

```
memory/
├── __init__.py           # 模块入口
├── service.py            # 记忆服务核心 (12KB)
├── models.py             # 记忆模型 (4.3KB)
├── encryption.py         # 加密模块 (4.9KB)
└── tests/                # 测试
```

**核心功能**:
- 记忆存储与检索
- 端到端加密
- 记忆关联
- 遗忘机制

---

## 5. playbook/ - Playbook服务

生成个性化行动手册

```
playbook/
├── __init__.py           # 模块入口
├── generator.py          # Playbook生成器 (15KB)
├── cache.py              # 缓存管理 (6.3KB)
└── tests/                # 测试
```

**Playbook结构**:
1. 时间窗口分析
2. 优势/挑战识别
3. 行动建议
4. 注意事项
5. 每日提醒

---

## 6. life_version/ - 生命版本服务

管理用户生命版本

```
life_version/
├── __init__.py           # 模块入口
├── service.py            # 版本服务
├── models.py             # 版本模型
├── calculator.py         # 版本计算
└── tests/                # 测试
```

**功能**:
- 基础版本计算
- 版本快照
- 版本对比
- 时间线追踪

---

## 7. learning/ - 学习服务

用户反馈学习与模型优化

```
learning/
├── __init__.py           # 模块入口
├── service.py            # 学习服务
├── models.py             # 学习模型
├── feedback.py           # 反馈处理
├── optimizer.py          # 模型优化
└── tests/                # 测试
```

---

## 8. preference/ - 偏好服务

用户偏好管理

```
preference/
├── __init__.py           # 模块入口
├── service.py            # 偏好服务
├── models.py             # 偏好模型
└── tests/                # 测试
```

---

## 9. safety/ - 安全服务

内容安全与敏感话题处理

```
safety/
├── __init__.py           # 模块入口
├── filter.py             # 内容过滤
├── detector.py           # 敏感检测
├── handler.py            # 安全处理
├── models.py             # 安全模型
├── rules.py              # 安全规则
└── tests/                # 测试
```

---

## 10. timeline/ - 时间线服务

生成用户时间线视图

```
timeline/
├── __init__.py           # 模块入口
├── service.py            # 时间线服务
├── models.py             # 时间线模型
└── tests/                # 测试
```

---

## 11. subscription/ - 订阅服务

用户订阅管理

```
subscription/
├── __init__.py           # 模块入口
└── service.py            # 订阅服务
```

---

## 12. todo/ - 待办服务

用户待办事项管理

```
todo/
├── __init__.py           # 模块入口
└── service.py            # 待办服务
```

---

## 13. version_tree/ - 版本树服务

版本树结构管理

```
version_tree/
├── __init__.py           # 模块入口
├── service.py            # 版本树服务
└── models.py             # 版本树模型
```

---

## 14. auth/ - 认证服务

用户认证与授权

```
auth/
├── __init__.py           # 模块入口
└── service.py            # 认证服务
```

---

## 服务依赖关系

```
                    ┌─────────────┐
                    │   auth      │
                    └──────┬──────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│   scenario   │   │   timeline   │   │  subscription│
└──────┬───────┘   └──────┬───────┘   └──────────────┘
       │                  │
       ▼                  ▼
┌──────────────┐   ┌──────────────┐
│  narrative   │   │   playbook   │
└──────┬───────┘   └──────┬───────┘
       │                  │
       ▼                  ▼
┌──────────────────────────────────┐
│        action_compiler           │
└──────────────────────────────────┘
       │
       ▼
┌──────────────┐   ┌──────────────┐
│   memory     │   │   learning   │
└──────────────┘   └──────────────┘
```
