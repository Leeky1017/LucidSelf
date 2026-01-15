# Schema Staging 目录

**用途**：存放从精校Markdown提取的中间产物（YAML），供后续流程审核和转换。

**⚠️ 这不是最终位置**：
- 最终语义层代码位于 `backend/semantics/**/*.py`
- 本目录是 Factor-Ontology-Agent 和 Semantics-Agent 的**输入**

---

## 数据流程

```
典籍/**/*.md (精校Markdown)
    │
    ▼ [schema_extractor]
data/schema_staging/*.yaml (本目录)
    │
    ▼ [Factor-Ontology-Agent]
典籍/lucidself_factor_ontology.md (因子本体更新)
    │
    ▼ [Semantics-Agent]
backend/semantics/**/*.py (最终代码)
```

---

## 目录结构

```
data/schema_staging/
├── factors/          # 提取的因子 (ConfigFactor)
├── snippets/         # 提取的叙事素材 (NarrativeSnippet)
├── terms/            # 提取的术语表 (TermGlossary)
├── relations/        # 提取的因子关系 (ConfigRelation)
├── evidence/         # 提取的证据链 (EvidenceChainEntry)
├── cross_system/     # 提取的跨体系映射 (CrossSystemMapping)
└── extraction_report.md
```

---

## 待处理项

### 1. Factor ID 分配

当前大量因子的 `factor_id` 为 `new_candidate`，需要：

1. **Factor-Ontology-Agent** 审核：
   - 识别重复/同义因子
   - 分配正式 factor_id（遵循命名规范）
   - 更新 `典籍/lucidself_factor_ontology.md`

2. **命名规范**：
   - 格式：`[类别]_[语义]`，如 `day_master_jia`、`season_spring`
   - 小写字母 + 下划线
   - 唯一性保证

### 2. 跨书因子对齐

同一概念在不同书中可能有不同表述：

| 概念 | 滴天髓 | 子平真诠 | 统一ID |
|------|--------|---------|--------|
| 甲木日主 | tiangan_jia | day_stem_jia | → `day_master_jia` |

需要 **KG-Agent** 进行跨书对齐。

---

## 使用命令

```bash
# 重新提取
.venv/bin/python -m scripts.schema_extractor batch 典籍/

# 验证YAML
.venv/bin/python -m scripts.schema_extractor validate data/schema_staging
```

---

## 后续步骤

1. [ ] Factor-Ontology-Agent 审核 new_candidate 因子
2. [ ] 分配正式 factor_id
3. [ ] Semantics-Agent 生成 `backend/semantics/**/*.py`
4. [ ] 删除本 staging 目录（或归档）
