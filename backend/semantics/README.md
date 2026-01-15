# LucidSelf 语义层 (Semantic Layer)

> **版本**: v2.0  
> **更新日期**: 2025-11-24  
> **状态**: 新架构，取代旧的 `data/semantics/*.jsonl` 方式

---

## 📖 概述

这是 LucidSelf 的 **L2 语义层**实现，采用 **Python 定义 + PostgreSQL 存储 + Redis 缓存** 的三层架构。

### 核心理念

- **源头真理**: Markdown 精校稿（`典籍/**/*.md`）是唯一权威来源
- **Python 定义**: 提供类型安全、IDE 支持、代码审查能力
- **数据库存储**: PostgreSQL 提供高性能索引和复杂查询
- **缓存加速**: Redis 缓存热点数据，毫秒级响应

---

## 🏗️ 架构设计

```
典籍 Markdown（L1+L2 精校稿）
          ↓
    Python 类定义
          ↓
   PostgreSQL 存储 ← Redis 缓存
          ↓
      查询引擎
          ↓
   规则引擎/应用层
```

### 三层架构

1. **Python 定义层** (`backend/semantics/**/*.py`)
   - 开发时编写，提供类型检查和 IDE 支持
   - 使用 `@SemanticRegistry.register` 装饰器注册
   - 启动时自动同步到数据库

2. **PostgreSQL 存储层**
   - 持久化存储，支持复杂查询
   - 全文搜索（tsvector）
   - 向量搜索（pgvector）
   - JSONB 灵活字段

3. **Redis 缓存层**
   - 热点数据内存缓存
   - 倒排索引加速
   - TTL 自动过期

---

## 📁 目录结构

```
backend/semantics/
├── __init__.py              # 模块入口
├── README.md                # 本文档
│
├── core/                    # 核心基础设施
│   ├── __init__.py
│   ├── base.py              # SemanticEntry 基类和 Registry
│   ├── index.py             # 查询引擎（TODO）
│   ├── cache.py             # 缓存管理（TODO）
│   └── sync.py              # 数据库同步（TODO）
│
├── dts/                     # 滴天髓
│   ├── __init__.py
│   ├── _example.py          # 示例文件（开发后删除）
│   ├── tiangan.py           # 天干篇（TODO）
│   └── ...
│
├── waite_tarot/             # Waite Pictorial Key
│   ├── __init__.py
│   ├── major_arcana.py      # 大阿卡纳（TODO）
│   └── ...
│
├── pollack_tarot/           # 78 Degrees of Wisdom
│   └── __init__.py
│
├── mlxj/                    # 梦林玄解
│   └── __init__.py
│
├── zhougong/                # 周公解梦
│   └── __init__.py
│
├── the_inner_sky/           # The Inner Sky
│   └── __init__.py
│
└── ziwei/                   # 紫微斗数
    └── __init__.py
```

---

## 🚀 使用指南

### 1. 编写语义条目

```python
# backend/semantics/dts/jiamu.py
from backend.semantics.core.base import SemanticEntry, SemanticRegistry

@SemanticRegistry.register(
    semantic_id="dts_v2_jia_001",
    book_id="dts"
)
class 甲木参天(SemanticEntry):
    """滴天髓·天干·甲木第一条"""
    
    original_text = "甲木参天，脱胎要火"
    normalized_text_zh = "甲木如参天大树，需要火来温养生发..."
    normalized_text_en = "Jia Wood like towering tree needs Fire..."
    
    subject = "甲木日主的季节宜忌与五行平衡"
    
    natural_attributes = {
        "symbolism": ["参天大树", "阳木"],
        "characteristics": ["刚健", "向上"]
    }
    
    factor_refs = ["day_master_jia", "season_spring"]
    
    terms = [
        {
            "term_zh": "甲木",
            "term_en": "Jia Wood",
            "def_zh": "十天干之首，阳木",
            "def_en": "First Heavenly Stem, Yang Wood"
        }
    ]
```

### 2. 查询语义（TODO）

```python
from backend.semantics import SemanticQueryEngine

# 按因子查询
results = await SemanticQueryEngine.query_by_factors(
    ["day_master_jia", "season_spring"]
)

# 语义搜索
results = await SemanticQueryEngine.semantic_search(
    "甲木在春季的表现"
)

# 跨领域导航
western = await SemanticQueryEngine.cross_domain_navigate(
    "dts_v2_jia_001", 
    "western_astro"
)
```

### 3. 获取已注册的语义

```python
from backend.semantics import SemanticRegistry

# 获取单个
entry = SemanticRegistry.get("dts_v2_jia_001")

# 获取某本书的全部
dts_entries = SemanticRegistry.get_by_book("dts")

# 获取总数
count = SemanticRegistry.count()
```

---

## 📋 开发规范

### 字段说明

| 字段 | 类型 | 必填 | 说明 |
|-----|------|------|------|
| `semantic_id` | str | ✅ | 唯一标识，格式：`{book_id}_v{version}_{topic}_{number}` |
| `book_id` | str | ✅ | 书籍标识（dts, mlxj, waite_tarot等） |
| `original_text` | str | ✅ | 原文（保持原语种） |
| `normalized_text_zh` | str | ✅ | 中文规范化释义 |
| `normalized_text_en` | str | ⭕ | 英文规范化释义 |
| `subject` | str | ✅ | 主题概括 |
| `natural_attributes` | dict | ⭕ | 自然属性（象征、特性、元素） |
| `necessary_conditions` | list | ⭕ | 必要条件 |
| `enhancing_conditions` | list | ⭕ | 增强条件 |
| `failing_conditions` | list | ⭕ | 失效条件 |
| `interpretation_modes` | dict | ⭕ | 多层解释 |
| `factor_refs` | list | ✅ | 因子引用（仅 existing 因子） |
| `terms` | list | ⭕ | 双语术语对齐 |
| `related_semantics` | list | ⭕ | 关联语义 ID |
| `cross_domain_refs` | dict | ⭕ | 跨领域映射 |

### 命名规范

- **语义 ID**: `{book_id}_v{version}_{topic}_{number}`
  - 示例: `dts_v2_jia_001`, `waite_v1_fool_001`
  
- **类名**: 使用有意义的中文或英文名称
  - 示例: `甲木参天`, `TheFoolCard`

- **文件名**: 按书籍结构组织
  - 示例: `dts/tiangan.py`, `waite_tarot/major_arcana.py`

### 禁止事项

❌ **禁止在语义层包含规则逻辑**
- 不得包含 `is_xxx = true/false` 布尔判定
- 不得包含 `triggered`、`matched` 等执行结果
- 只做纯语义描述，不做判定

❌ **禁止引用不存在的因子**
- `factor_refs` 只能引用 `existing` 状态的因子
- 新因子需先在因子本体中定义

---

## 🔄 迁移路径

### Phase 1: 框架建立 ✅
- [x] 创建目录结构
- [x] 实现 `SemanticEntry` 基类
- [x] 实现 `SemanticRegistry` 注册机制
- [x] 创建示例文件

### Phase 2: 核心功能（TODO）
- [ ] 实现 PostgreSQL Schema
- [ ] 实现数据同步机制
- [ ] 实现查询引擎
- [ ] 实现 Redis 缓存

### Phase 3: 数据迁移（TODO）
- [ ] 高频语义优先迁移
- [ ] 批量转换工具
- [ ] 数据验证

### Phase 4: 完全切换（TODO）
- [ ] 所有核心语义转为 Python
- [ ] 更新相关代码引用
- [ ] 性能测试和优化

---

## 📊 性能目标

| 指标 | 目标 | 当前 |
|-----|------|------|
| 启动时间 | <2秒 | TODO |
| 单次查询 | <10ms | TODO |
| 并发查询 | >1000 QPS | TODO |
| 内存占用 | 按需加载 | TODO |
| 缓存命中率 | >80% | TODO |

---

## 🔗 相关文档

- 典籍精校模板: `典籍/精校模板_L1L2.md`
- 因子本体: `典籍/lucidself_factor_ontology.md`
- 规则实现: `backend/rules/`
- 系统设计: `docs/SYSTEM_DESIGN.md`

---

## ⚠️ 注意事项

1. **本模块仍在开发中**，核心查询功能标记为 TODO
2. **不要直接操作数据库**，所有操作通过 Python API
3. **保持 Markdown 为真理来源**，Python 代码是实现而非数据源
4. **测试覆盖**：所有语义条目应有对应的测试用例

---

**维护者**: Semantics-Agent  
**最后更新**: 2025-11-24
