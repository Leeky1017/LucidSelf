# Backend 后端服务详细结构

## 目录总览

```
backend/
├── api/                  # FastAPI 应用层
├── calculators/          # 推演引擎计算器
├── core/                 # 核心基础设施
├── semantics/            # 语义片段库
├── services/             # 业务服务层
├── rules/                # 规则引擎
├── integration/          # 跨域融合
├── models/               # 数据库模型
├── pipeline/             # 流水线编排
├── scheduler/            # 定时任务
├── testing/              # 测试框架
├── repositories/         # 数据仓库
├── db/                   # 数据库配置
├── .env                  # 环境变量
└── .env.example          # 环境变量模板
```

---

## 1. api/ - FastAPI 应用层

```
api/
├── main.py               # FastAPI入口，应用初始化
├── models.py             # API请求/响应模型
├── routes/               # 路由定义
│   ├── analyze.py        # 命盘分析路由
│   ├── auth.py           # 认证授权路由
│   ├── dream.py          # 解梦路由
│   ├── geocoding.py      # 地理编码路由
│   ├── health.py         # 健康检查
│   ├── insights.py       # 洞察生成路由
│   ├── interpret.py      # 解读路由
│   ├── patterns.py       # 模式识别路由
│   ├── playbook.py       # Playbook路由
│   ├── scheduler.py      # 调度器路由
│   ├── subscription.py   # 订阅路由
│   ├── timeline.py       # 时间线路由
│   ├── todo.py           # 待办事项路由
│   ├── user.py           # 用户路由
│   └── versions.py       # 版本管理路由
├── middleware/           # 中间件
├── services/             # API层服务
└── tests/                # API测试
```

---

## 2. calculators/ - 推演引擎计算器

```
calculators/
├── __init__.py           # 计算器注册中心
├── astro/                # 西方占星计算器
│   ├── calculator.py     # 星盘计算 (行星/宫位/相位)
│   ├── models.py         # 占星数据模型
│   ├── service.py        # 占星服务
│   └── tests/            # 测试
├── bazi/                 # 八字计算器
│   ├── calculator.py     # 八字排盘核心
│   ├── models.py         # 八字数据模型 (天干地支等)
│   ├── service.py        # 八字服务
│   ├── dayun.py          # 大运计算
│   ├── hidden_stems.py   # 藏干
│   ├── solar_terms.py    # 节气
│   ├── ten_gods.py       # 十神
│   └── tests/            # 测试
├── dream/                # 解梦计算器
│   ├── extractor.py      # 梦境元素提取
│   ├── models.py         # 解梦数据模型
│   └── tests/            # 测试
├── tarot/                # 塔罗计算器
│   ├── interpreter.py    # 塔罗解读器
│   ├── models.py         # 塔罗数据模型
│   └── tests/            # 测试
├── yijing/               # 周易计算器
│   ├── calculator.py     # 起卦计算
│   ├── models.py         # 周易数据模型
│   ├── service.py        # 周易服务
│   └── tests/            # 测试
└── ziwei/                # 紫微斗数计算器
    ├── calculator.py     # 紫微排盘
    ├── models.py         # 紫微数据模型
    ├── service.py        # 紫微服务
    ├── decade.py         # 大限计算
    ├── lunar_calendar.py # 农历转换
    ├── palace_system.py  # 十二宫系统
    ├── sihua.py          # 四化
    ├── star_placement.py # 星曜安放
    └── tests/            # 测试
```

---

## 3. core/ - 核心基础设施

```
core/
├── cache/                # 缓存层
├── contracts/            # 数据契约 (Pydantic模型)
│   ├── base.py           # 基础契约
│   ├── action_models.py  # 行动模型
│   ├── auth_models.py    # 认证模型
│   ├── config_models.py  # 配置模型
│   ├── engine_models.py  # 引擎模型
│   ├── l25_models.py     # L2.5层模型
│   ├── life_version_models.py  # 生命版本模型
│   ├── memory_models.py  # 记忆模型
│   ├── narrative_models.py     # 叙事模型
│   ├── narrative_snippet_models.py  # 叙事片段模型
│   ├── runtime_models.py       # 运行时模型
│   ├── subscription_models.py  # 订阅模型
│   ├── todo_models.py          # 待办模型
│   ├── toon_models.py          # Toon模型
│   ├── unified_dimensions.py   # 统一维度
│   ├── unified_time.py         # 统一时间
│   ├── validation.py           # 验证工具
│   └── tests/            # 测试
├── decorators/           # 装饰器
├── deployment/           # 部署工具
├── engines/              # 引擎管理
│   ├── manager.py        # 引擎管理器
│   ├── constraints.py    # 引擎约束
│   ├── exceptions.py     # 异常定义
│   └── tests/            # 测试
├── geocoding/            # 地理编码
├── llm/                  # LLM客户端
│   ├── client.py         # LLM客户端
│   ├── cost_monitor.py   # 成本监控
│   ├── layered_router.py # 分层路由
│   ├── models.py         # LLM模型定义
│   ├── orchestrator.py   # 编排器
│   ├── router.py         # 路由器
│   ├── toon_serializer.py # Toon序列化
│   ├── providers/        # 提供商适配
│   └── tests/            # 测试
├── observability/        # 可观测性 (日志/指标/追踪)
└── testing/              # 测试工具
```

---

## 4. semantics/ - 语义片段库

```
semantics/
├── core/                 # 核心加载器与基类
├── README.md             # 语义库说明
│
├── # 西方占星系列
├── astrology_personality/     # 《Astrology of Personality》
├── christian_astrology/       # 《Christian Astrology》
├── planets_in_transit/        # 《Planets in Transit》(645条目)
├── tetrabiblos/              # 《Tetrabiblos》
├── the_inner_sky/            # 《The Inner Sky》
├── astrological_houses/      # 《The Astrological Houses》
│
├── # 塔罗系列
├── book_of_thoth/            # 《The Book of Thoth》
├── learning_tarot/           # 《Learning the Tarot》
├── pollack_tarot/            # Pollack塔罗
├── waite_tarot/              # 韦特塔罗
│
├── # 解梦系列
├── dreams_visions_dict/      # Dreams & Visions Dictionary (229条目)
├── interpretation_dreams/    # 《The Interpretation of Dreams》
├── llewellyns_dreams/        # Llewellyns Dreams
├── zhougong/                 # 周公解梦
│
├── # 心理学系列
├── archetypes_unconscious/   # 《集体无意识原型》(148条目)
├── collected_works/          # 荣格全集
│
├── # 八字系列
├── sanming/                  # 三命通会 (622条目)
├── yuanhaiziping/            # 渊海子平
├── qiongtongbaojian/         # 穷通宝鉴
├── zipingzhenquan/           # 子平真诠
├── dts/                      # 滴天髓
├── mlxj/                     # 梦林玄解 (205条目)
│
├── # 紫微系列
├── ziwei/                    # 紫微斗数全书 (256条目)
│
└── # 周易系列
    └── zhouyi/               # 周易 (64卦)
```

---

## 5. services/ - 业务服务层

```
services/
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

## 6. rules/ - 规则引擎

```
rules/
├── core.py               # 规则核心
├── engine.py             # 规则引擎
├── condition.py          # 条件解析
├── conflict.py           # 冲突检测
├── context.py            # 上下文管理
├── coverage.py           # 覆盖率统计
├── dimension.py          # 维度处理
├── changelog.py          # 变更日志
├── reloader.py           # 热重载
└── tests/                # 测试
```

---

## 7. integration/ - 跨域融合

```
integration/
├── fusion_engine.py      # 融合引擎
├── cross_validator.py    # 跨系统验证
├── decision_calculator.py # 决策计算
├── evidence_chain.py     # 证据链
├── theme_mapper.py       # 主题映射
├── weight_manager.py     # 权重管理
├── models.py             # 融合模型
└── tests/                # 测试
```

---

## 8. 其他模块

### models/ - 数据库模型
```
models/
├── auth.py               # 认证模型
├── dream.py              # 梦境模型
├── subscription.py       # 订阅模型
├── todo.py               # 待办模型
└── user.py               # 用户模型
```

### pipeline/ - 流水线
```
pipeline/
├── orchestrator.py       # 流水线编排器
└── tests/                # 测试
```

### scheduler/ - 定时任务
```
scheduler/
├── base.py               # 调度器基类
├── registry.py           # 任务注册
└── jobs/                 # 具体任务
```

### testing/ - 测试框架
```
testing/
├── framework/            # 测试框架
├── generators/           # 测试数据生成
├── integration/          # 集成测试
├── product/              # 产品测试
└── unit/                 # 单元测试
```
