# Scripts 工具脚本详细结构

## 目录总览

```
scripts/
├── codegen/                    # 代码生成器
├── knowledge_graph_builder/    # 知识图谱构建
├── logic_chain_builder/        # 逻辑链构建
├── rule_converter/             # 规则转换器
├── factor_extractor/           # 因子提取器
├── schema_extractor/           # Schema提取器
├── extract_dream_fields.py     # 梦境字段提取
├── generate_schemas.py         # Schema生成
├── generate_solar_terms_1900_2100.py  # 节气生成
├── init_db.py                  # 数据库初始化
├── init-postgres.sql           # PostgreSQL初始化
├── llm_model_benchmark.py      # LLM模型基准测试
└── logic_chain_query.py        # 逻辑链查询
```

---

## 1. codegen/ - 代码生成器

核心功能：从Schema/规则/典籍自动生成Python代码

```
codegen/
├── __init__.py               # 模块入口
├── __main__.py               # CLI入口
├── cli.py                    # 命令行接口
├── base.py                   # 生成器基类
├── models.py                 # 代码生成模型
├── exceptions.py             # 异常定义
│
├── # 核心生成器
├── semantic_generator.py     # 语义代码生成 (55KB，最复杂)
├── rule_generator.py         # 规则代码生成
├── factor_generator.py       # 因子代码生成
├── engine_mapping.py         # 引擎映射生成
│
├── # 辅助工具
├── validation.py             # 生成代码验证
├── manifest.py               # 生成清单
├── reporter.py               # 生成报告
├── hot_reload.py             # 热重载支持
├── rollback.py               # 回滚机制
├── error_report.py           # 错误报告
└── tests/                    # 测试 (11个文件)
```

**生成流程**:
1. 读取 `data/rules/` YAML规则
2. 解析 `典籍/` 结构化文本
3. 生成 `backend/semantics/` Python模块
4. 输出 `.codegen_manifest.json`

---

## 2. knowledge_graph_builder/ - 知识图谱构建

核心功能：构建命理知识图谱

```
knowledge_graph_builder/
├── __init__.py               # 模块入口
├── __main__.py               # CLI入口
├── cli.py                    # 命令行接口 (16KB)
├── importer.py               # 数据导入器 (20KB)
│
├── builders/                 # 图谱构建器
│   ├── factor_builder.py     # 因子构建
│   ├── relation_builder.py   # 关系构建
│   ├── semantic_builder.py   # 语义构建
│   └── ...
│
├── models/                   # 数据模型
│   ├── node.py               # 节点模型
│   ├── edge.py               # 边模型
│   ├── graph.py              # 图模型
│   └── ...
│
├── persistence/              # 持久化
│   ├── neo4j_writer.py       # Neo4j写入
│   ├── json_writer.py        # JSON写入
│   └── ...
│
├── query/                    # 查询引擎
├── export/                   # 导出工具
├── validation/               # 验证器
└── tests/                    # 测试
```

---

## 3. logic_chain_builder/ - 逻辑链构建

核心功能：从典籍提取推理逻辑链

```
logic_chain_builder/
├── __init__.py               # 模块入口
├── __main__.py               # CLI入口
├── cli.py                    # 命令行接口 (38KB，主入口)
├── builder.py                # 逻辑链构建器 (17KB)
├── models.py                 # 数据模型
├── constants.py              # 常量定义
│
├── # 核心处理
├── loader.py                 # 数据加载
├── validator.py              # 验证器 (26KB)
├── clusterer.py              # 聚类器
├── edge_inferrer.py          # 边推断
├── factor_cooccurrence.py    # 因子共现分析
│
├── # 质量与报告
├── quality_scorer.py         # 质量评分 (18KB)
├── report.py                 # 报告生成 (15KB)
├── summary_generator.py      # 摘要生成 (15KB)
│
├── # 优化与精化
├── refinement_engine.py      # 精化引擎 (26KB)
├── semantic_refiner.py       # 语义精化 (16KB)
├── book_type_adapter.py      # 书籍类型适配
│
├── writer.py                 # 输出写入
├── logging_config.py         # 日志配置
├── v2/                       # V2版本 (14个文件)
└── tests/                    # 测试 (15个文件)
```

**输出**: `data/logic_chains/*.yaml`

---

## 4. rule_converter/ - 规则转换器

核心功能：将结构化文本转换为规则YAML

```
rule_converter/
├── __init__.py               # 模块入口
├── cli.py                    # 命令行接口 (15KB)
├── orchestrator.py           # 转换编排器 (16KB)
│
├── converters/               # 转换器
│   ├── bazi_converter.py     # 八字规则转换
│   ├── astro_converter.py    # 占星规则转换
│   └── ...
│
├── loaders/                  # 加载器
│   ├── yaml_loader.py        # YAML加载
│   └── ...
│
├── validators/               # 验证器
│   ├── schema_validator.py   # Schema验证
│   └── ...
│
├── outputs/                  # 输出格式
├── models/                   # 数据模型
│
├── # 补充工具
├── fix_invalid_snippets.py   # 修复无效片段
├── supplement_factor_refs.py # 补充因子引用
├── supplement_logic_chain.py # 补充逻辑链
└── tests/                    # 测试 (8个文件)
```

---

## 5. factor_extractor/ - 因子提取器

核心功能：从文本提取因子

```
factor_extractor/
├── __init__.py
├── extractor.py              # 提取核心
├── models.py                 # 数据模型
├── patterns/                 # 模式定义
└── tests/
```

---

## 6. schema_extractor/ - Schema提取器

核心功能：提取数据Schema

```
schema_extractor/
├── __init__.py
├── extractor.py              # 提取核心
├── analyzer.py               # 结构分析
├── models.py                 # 数据模型
└── tests/
```

---

## 7. 独立脚本

| 脚本 | 功能 | 大小 |
|------|------|------|
| `extract_dream_fields.py` | 梦境字段提取 | 6.8KB |
| `generate_schemas.py` | Schema生成 | 8.2KB |
| `generate_solar_terms_1900_2100.py` | 节气表生成 | 5.1KB |
| `init_db.py` | 数据库初始化 | 10.5KB |
| `init-postgres.sql` | PostgreSQL DDL | 3.2KB |
| `llm_model_benchmark.py` | LLM基准测试 | 10.8KB |
| `logic_chain_query.py` | 逻辑链查询 | 8.3KB |

---

## 使用示例

```bash
# 代码生成
python -m scripts.codegen generate --engine bazi

# 知识图谱构建
python -m scripts.knowledge_graph_builder build --source sanming

# 逻辑链构建
python -m scripts.logic_chain_builder build --book 三命通会

# 规则转换
python -m scripts.rule_converter convert --input 典籍/中文典籍/三命通会/

# 数据库初始化
python scripts/init_db.py
```
