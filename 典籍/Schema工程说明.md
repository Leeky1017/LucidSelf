# Schema工程说明

> **版本**: v1.0  
> **生效日期**: 2025-11-27  
> **定位**: 指导精校内容到结构化数据的转换工程，明确为什么做、怎么做、避免哪些坑  
> **适用范围**: 精校Agent、Schema提取脚本开发者、Logic-Agent、KG-Agent

---

## 一、为什么要做Schema工程？

### 1.1 问题背景

**现状**：
- 精校Agent产出的是Markdown格式的人类可读文档
- LS引擎需要的是Pydantic/YAML格式的机器可处理数据
- 两者之间存在一道**不可逾越的鸿沟**

**没有Schema工程会发生什么**：
```
精校Markdown ──────────────────────────────────→ ??? ──→ 引擎代码
             ↑                                        ↑
             无法自动验证                              无法自动生成
             无法自动提取                              手工转换易出错
             格式不统一                                版本无法追溯
```

**有Schema工程的流程**：
```
精校Markdown ──→ Schema提取脚本 ──→ 验证通过的YAML ──→ Codegen ──→ 引擎代码
             ↑                   ↑                  ↑
             格式规范            自动验证            自动生成
             标签完整            错误报告            版本追溯
```

### 1.2 核心价值

| 价值点 | 没有Schema工程 | 有Schema工程 |
|-------|---------------|-------------|
| **数据一致性** | 各书格式不一，难以统一处理 | 强制符合统一Schema |
| **错误检测** | 运行时才发现错误 | 提取时即刻发现 |
| **版本追溯** | 难以追溯数据来源 | 完整的source_ref链路 |
| **自动化程度** | 大量手工操作 | 高度自动化 |
| **下游依赖** | Logic-Agent无法工作 | 结构化数据直接可用 |

---

## 二、Schema工程做什么？

### 2.1 输入与输出

**输入**：精校后的Markdown文件
- L1层：原文、规范化释义、核心要点、叙事素材（含trigger+role）
- L2层：语义提取、术语表、因子表（八列）
- L2.5层：因子关系表、证据链表、跨体系映射表

**输出**：符合Schema定义的YAML文件
```
data/semantics/
├── factors/           # ConfigFactor
│   ├── bazi_factors.yaml
│   ├── astro_factors.yaml
│   └── ...
├── snippets/          # NarrativeSnippet
│   ├── ditianshui_snippets.yaml
│   └── ...
├── relations/         # ConfigRelation
│   ├── bazi_relations.yaml
│   └── ...
├── evidence/          # EvidenceChainEntry
│   ├── ditianshui_evidence.yaml
│   └── ...
└── cross_system/      # CrossSystemMapping
    └── cross_system_mappings.yaml
```

### 2.2 Schema类型对照

| 精校内容 | Schema类型 | 数据契约位置 |
|---------|-----------|-------------|
| 因子层表格 | `ConfigFactor` | §1.1 |
| 叙事素材 | `NarrativeSnippet` | §3.4 |
| L2.5因子关系层 | `ConfigRelation` | §1.5.1 |
| L2.5推理溯源层 | `EvidenceChainEntry` | §1.5.2 |
| L2.5跨体系映射层 | `CrossSystemMapping` | §1.5.3 |

---

## 三、怎么做Schema工程？

### 3.1 阶段划分

```
阶段1：精校补充（精校Agent）
    ↓ 产出：完整的精校Markdown（含L2.5）
阶段2：Schema提取（提取脚本）
    ↓ 产出：验证通过的YAML文件
阶段3：逻辑链构建（Logic-Agent）
    ↓ 产出：LogicChain YAML
阶段4：因子对齐（KG-Agent）
    ↓ 产出：跨书对照表
阶段5：因子本体更新（Factor-Ontology-Agent）
    ↓ 产出：更新后的因子本体
```

### 3.2 精校Markdown要求

为确保Schema提取顺利，精校Markdown必须满足以下要求：

#### 因子层表格格式
```markdown
<!-- FACTOR_BEGIN -->
| 类别 | 中文名 | factor_id | 状态 | 功能简述 | 取值 | 引擎归属 | 备注 |
|------|-------|-----------|------|---------|------|---------|------|
| 结构类 | 甲木日主 | day_master_jia | existing | 日主 | 甲 | bazi_calculator | 十天干之一 |
<!-- FACTOR_END -->
```

**关键点**：
- 必须有`<!-- FACTOR_BEGIN -->`和`<!-- FACTOR_END -->`标签
- 表格必须是8列，顺序固定
- `factor_id`必须全小写，蛇形命名

#### 叙事素材格式
```markdown
- **叙事素材（narrative_snippets）**：
  1. **trigger**: day_master=甲  
     **role**: 主干  
     **snippet**: 甲木参天大树，性刚健而向上。
```

**关键点**：
- 必须包含trigger、role、snippet三个字段
- role只能是：`主干`/`主干依赖`/`条件分支`/`例外处理`/`总结`

#### L2.5表格格式
```markdown
<!-- L2.5_RELATION_BEGIN -->
| 关系ID | 关系类型 | 因子A | 因子B | 关系性质 | 条件约束 | 效果方向 | source_ref |
|-------|---------|-------|-------|---------|---------|---------|-----------|
| rel_dts_001 | wuxing_shengke | day_master_jia | element_fire | 生 | - | 增益 | 《滴天髓》#甲木条 |
<!-- L2.5_RELATION_END -->
```

**关键点**：
- 必须有对应的`BEGIN`/`END`标签
- 关系类型必须是枚举值之一
- 效果方向必须是：`增益`/`损害`/`限制`/`中性`/`混合`

### 3.3 Schema提取脚本工作流程

```python
# 伪代码示意
def extract_schema(markdown_path: str) -> Dict[str, List[BaseModel]]:
    """从Markdown提取Schema"""
    
    content = read_markdown(markdown_path)
    
    # 1. 提取因子表
    factors = extract_between_tags(content, "FACTOR_BEGIN", "FACTOR_END")
    config_factors = [ConfigFactor(**row) for row in parse_table(factors)]
    
    # 2. 提取叙事素材
    snippets = extract_narrative_snippets(content)
    narrative_snippets = [NarrativeSnippet(**s) for s in snippets]
    
    # 3. 提取L2.5三表
    relations = extract_between_tags(content, "L2.5_RELATION_BEGIN", "L2.5_RELATION_END")
    evidence = extract_between_tags(content, "L2.5_EVIDENCE_BEGIN", "L2.5_EVIDENCE_END")
    cross_system = extract_between_tags(content, "L2.5_CROSS_BEGIN", "L2.5_CROSS_END")
    
    # 4. Pydantic验证
    validate_all(config_factors, narrative_snippets, relations, evidence, cross_system)
    
    # 5. 输出YAML
    output_yaml(config_factors, "data/semantics/factors/")
    output_yaml(narrative_snippets, "data/semantics/snippets/")
    # ...
    
    return results
```

---

## 四、避免哪些坑？

### 4.1 精校阶段常见错误

| 错误类型 | 示例 | 正确写法 | 后果 |
|---------|------|---------|------|
| factor_id大写 | `Day_Master_Jia` | `day_master_jia` | Schema验证失败 |
| role值错误 | `核心`、`主要` | `主干` | Schema验证失败 |
| 缺少BEGIN/END标签 | 直接写表格 | 用标签包裹 | 提取脚本找不到内容 |
| 表格列数不对 | 少一列或多一列 | 严格8列 | 解析错误 |
| trigger格式错误 | `甲木日主` | `day_master=甲` | 运行时匹配失败 |

### 4.2 Schema提取阶段常见错误

| 错误类型 | 原因 | 解决方案 |
|---------|------|---------|
| 编码错误 | Markdown文件不是UTF-8 | 统一使用UTF-8编码 |
| 特殊字符 | 表格中有`|`字符 | 用转义或避免 |
| 空行问题 | 表格中间有空行 | 确保表格连续 |
| 引用缺失 | source_ref为空 | 强制要求填写 |

### 4.3 版本一致性问题

**问题**：精校模板更新后，旧的精校文件格式不兼容

**解决方案**：
1. 精校模板版本号与数据契约版本号保持一致
2. Schema提取脚本检查模板版本
3. 旧文件需要按新模板补充

```python
# 版本检查示例
def check_template_version(content: str) -> bool:
    version = extract_version(content)
    if version < REQUIRED_VERSION:
        raise VersionError(f"需要更新到模板v{REQUIRED_VERSION}")
    return True
```

### 4.4 跨书一致性问题

**问题**：同一个概念在不同书中有不同的factor_id

**示例**：
- 《滴天髓》：`day_master_jia`
- 《子平真诠》：`jia_wood_master`

**解决方案**：
1. 因子本体是唯一真相来源
2. 精校时必须查阅因子本体
3. new_candidate因子在KG-Agent阶段统一归类

---

## 五、质量检查清单

### 5.1 精校完成后自查

- [ ] 每条条目都有L1（原文+释义+核心要点+叙事素材）
- [ ] 每个叙事素材都有trigger+role+snippet三个字段
- [ ] role只使用五个枚举值之一
- [ ] 因子表有BEGIN/END标签包裹
- [ ] 因子表是8列格式
- [ ] factor_id全小写蛇形命名
- [ ] L2.5因子关系表至少1条
- [ ] L2.5证据链表至少1条
- [ ] L2.5跨体系映射表（如适用）已填写或标注"无跨体系对应"

### 5.2 Schema提取后验证

- [ ] 所有Pydantic模型验证通过
- [ ] 无孤立的factor_id引用（引用的因子都存在）
- [ ] source_ref格式正确（《书名》#章节）
- [ ] 版本号符合语义化版本规范
- [ ] YAML输出可被正常解析

### 5.3 逻辑链构建后验证

- [ ] 每本书都有对应的LogicChain
- [ ] 所有节点都有至少一个snippet_id
- [ ] 所有边引用的节点都存在
- [ ] narrative_order包含所有terminal_nodes
- [ ] 无孤立节点（没有任何边连接的非入口节点）

---

## 六、工具与资源

### 6.1 相关文档

| 文档 | 位置 | 用途 |
|------|------|------|
| 数据契约 | `docs/数据契约_Schema定义规范_v1.md` | Schema定义的权威来源 |
| 精校模板（中文） | `典籍/精校模板_L1L2.md` | 中文典籍精校标准 |
| 精校模板（西方） | `典籍/texts/Western_Texts_Template.md` | 英文典籍精校标准 |
| Roadmap | `openspec/notes/ls_v1_implementation_roadmap.md` | Phase 0.5定义 |
| 架构文档 | `docs/ls_engine_architecture_v3.md` | 整体数据流向 |

### 6.2 Schema提取脚本（待开发）

**位置**：`scripts/schema_extractor/`

**接口设计**：
```bash
# 提取单个文件
python -m schema_extractor extract 典籍/中文典籍/子平/滴天髓/精校/通神论.md

# 批量提取
python -m schema_extractor batch 典籍/中文典籍/

# 验证已提取的YAML
python -m schema_extractor validate data/semantics/
```

### 6.3 Agent调用指令

**精校Agent**：
```
@Text-CN-Agent 请按 典籍/精校模板_L1L2.md 补充《滴天髓·通神论》的精校，确保L2.5三表完整。
```

**Schema提取**（脚本就绪后）：
```bash
python -m schema_extractor extract 典籍/中文典籍/子平/滴天髓/精校/通神论.md --output data/semantics/
```

**Logic-Agent**：
```
@Logic-Agent 请为《滴天髓》构建逻辑链，读取 data/semantics/snippets/ditianshui_*.yaml，输出到 data/logic_chains/chain_ditianshui.yaml
```

---

## 七、FAQ

### Q1: 精校时发现因子本体中没有的概念怎么办？
**A**: 在因子表中填写`status=new_candidate`，并在备注中说明建议的factor_id。后续由KG-Agent和Factor-Ontology-Agent统一处理。

### Q2: L2.5跨体系映射表什么时候可以标注"无跨体系对应"？
**A**: 仅当该条目的概念**确实**只存在于单一体系时。例如"甲木"这个概念本身不直接对应西方占星，但"阳刚、领导力"这个语义内核可以映射到太阳/火星，此时应该填写映射。

### Q3: Schema提取失败怎么办？
**A**: 
1. 查看错误报告，定位具体哪一行出错
2. 检查是否符合本文档第三节的格式要求
3. 修复后重新提取
4. 如果是模板本身的问题，反馈到本文档进行更新

### Q4: 不同版本的精校模板如何兼容？
**A**: Schema提取脚本会检查模板版本。旧版本精校需要按新模板补充后才能提取。不存在自动升级机制。

---

> **重要提醒**：Schema工程是连接内容精校与引擎代码的关键桥梁。任何跳过Schema验证直接使用数据的行为都是危险的，会导致运行时错误和数据不一致。请严格按照本文档执行。
