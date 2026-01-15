# LS系统数据契约与Schema定义规范 v1.2

> **版本**: v1.2  
> **生效日期**: 2025-11-30  
> **定位**: 连接L1-L4内容精校与Python引擎实现的标准契约  
> **适用范围**: 规则工程师、后端架构师、内容精校团队、Logic-Agent、KG-Agent、L3/L4结构化提取Agent
>
> **v1.2 更新说明**：
> - 新增 §9.7 Action层Schema定义（ActionBase、ActionSourceRef、ActionProject、ActionItem）
> - Action层与Memory层解耦设计：ActionBase独立于MemoryBase，通过引用建立关联
> - 新增枚举：ActionSourceKind、ActionTimeScope、ActionContext、ActionStatus、EffortEstimate
> - 详细设计参见 `Playbook-TODO.md` Action Compiler Layer 规划草案 v2.0
>
> **v1.1 更新说明**：
> - 新增 §1.5 L2.5桥接层Schema（ConfigRelation、EvidenceChainEntry、CrossSystemMapping）
> - 升级 §3.4 NarrativeSnippet为完整Pydantic模型
> - 新增 §3.5 LogicChain结构定义
> - 新增 §3.6 AssemblyProtocol组装协议

---

## 0. 核心原则

### 0.1 设计理念
1. **Python原生优先**: 所有Schema使用Pydantic定义，JSON仅作为序列化格式
2. **类型安全**: 利用Python typing系统确保编译时类型检查
3. **双向映射**: 确保Markdown→Python和Python→Markdown的无损转换
4. **渐进式验证**: 从基础字段到业务逻辑的分层验证
5. **配置态vs运行态分离**: 严格区分Config*（配置源码）与Runtime*（运行时对象）

### 0.2 数据流向（完整链路）
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  阶段1：精校Agent（内容层，Markdown）                                        │
│  模板：典籍/精校模板_L1L2.md                                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│  产出：                                                                      │
│  ├── L1：原文、释义、核心要点、叙事素材(trigger+role)                         │
│  ├── L2：语义提取、术语表、因子表                                            │
│  └── L2.5：因子关系表、证据链表、跨体系映射表（必选）                          │
└─────────────────────────────────────────────────────────────────────────────┘
                                     ↓ [Schema提取脚本]
┌─────────────────────────────────────────────────────────────────────────────┐
│  阶段2：Schema提取（Markdown → Pydantic/YAML）                               │
│  脚本：scripts/schema_extractor/                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  产出：                                                                      │
│  ├── ConfigFactor → backend/semantics/{book_id}/*.py (SemanticEntry类)      │
│  ├── NarrativeSnippet → backend/semantics/{book_id}/*.py (内嵌叙事素材)     │
│  ├── ConfigRelation → backend/semantics/{book_id}/*.py (related_semantics)  │
│  ├── EvidenceChainEntry → backend/semantics/{book_id}/*.py (evidence字段)   │
│  └── CrossSystemMapping → backend/semantics/{book_id}/*.py (cross_domain)   │
└─────────────────────────────────────────────────────────────────────────────┘
                                     ↓ [Logic-Agent]
┌─────────────────────────────────────────────────────────────────────────────┐
│  阶段3：逻辑链构建                                                           │
│  产出：LogicChain → data/logic_chains/*.yaml                                │
└─────────────────────────────────────────────────────────────────────────────┘
                                     ↓ [Codegen编译]
┌─────────────────────────────────────────────────────────────────────────────┐
│  阶段4：代码生成                                                             │
│  产出：                                                                      │
│  ├── backend/semantics/*.py (语义模块)                                      │
│  ├── backend/rules/*.py (规则代码)                                          │
│  └── backend/tests/*.py (测试用例)                                          │
└─────────────────────────────────────────────────────────────────────────────┘
                                     ↓ [热重载]
┌─────────────────────────────────────────────────────────────────────────────┐
│  阶段5：运行时                                                               │
│  ├── FactorMatrix → RuntimeRuleResult → FusionResult                        │
│  └── NarrativeSnippet → AssemblyProtocol → LLM Prompt                       │
└─────────────────────────────────────────────────────────────────────────────┘
                                     ↓ [TOON序列化]
┌─────────────────────────────────────────────────────────────────────────────┐
│  阶段6：LLM边界（Token压缩输出）                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 0.3 命名规范表

| 前缀 | 用途 | 示例 | 位置 |
|------|------|------|------|
| `Config...` | 配置态（JSONL/Markdown输出） | `ConfigRuleDefinition`, `ConfigFactor` | JSON文件、Codegen输入 |
| `Runtime...` | 运行态（Engine内存对象） | `RuntimeRuleResult`, `FactorValue` | Engine Layer1-4 |
| `...Descriptor` | 元信息登记 | `EngineDescriptor`, `FactorDescriptor` | 注册表 |
| `...Record` | 日志/观测 | `LLMUsageRecord`, `FusionAuditRecord` | 观测层 |

---

## 1. Content-L2语义层：因子契约 (Factor Schema)

**注意**：本章节定义的是**配置态模型**，用于Markdown提取和Codegen输入。运行时使用`FactorValue`和`FactorMatrix`。

### 1.1 核心数据模型

```python
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Dict, Any, Literal
from datetime import datetime
from enum import Enum

class FactorCategory(str, Enum):
    """因子类别枚举"""
    STRUCTURE = "structure"    # 结构类
    TIME = "time"              # 时间类
    RELATION = "relation"      # 关系类
    CONDITION = "condition"    # 条件类
    ENERGY = "energy"          # 能量类
    STATE = "state"           # 状态类
    PRINCIPLE = "principle"    # 原理类

class SourceMetadata(BaseModel):
    """溯源元数据"""
    book_id: str = Field(..., description="来源书籍ID")
    chapter: Optional[str] = None
    l1_anchor: str = Field(..., description="Content-L1锚点")
    extraction_date: datetime = Field(default_factory=datetime.now)
    extraction_tool_version: Optional[str] = Field(None, description="提取工具版本")

class ConfigFactor(BaseModel):
    """配置态因子定义 - 对应Markdown表格中的每一行"""
    # 标识
    factor_id: str = Field(..., regex="^[a-z][a-z0-9_]*$")
    label_zh: str
    label_en: Optional[str] = None
    
    # 分类
    category: FactorCategory
    value_type: Literal["boolean", "float", "enum", "string"]
    enum_values: Optional[List[str]] = Field(None, description="仅value_type=enum时必填")
    status: Literal["active", "experimental", "deprecated"] = "active"
    
    # 描述
    description_zh: str
    knowledge_ref: List[str] = Field(
        default_factory=list,
        description="知识引用，格式：book_id:chapter[:section]"
    )
    
    @validator('enum_values', always=True)
    def check_enum_values(cls, v, values):
        """确保enum类型必须提供enum_values"""
        if values.get('value_type') == 'enum' and not v:
            raise ValueError('enum_values required when value_type is enum')
        if v and values.get('value_type') != 'enum':
            raise ValueError('enum_values only valid when value_type is enum')
        return v
    
    # 版本与归属
    version: str = Field(..., regex="^\\d+\\.\\d+\\.\\d+$", description="语义包版本")
    engine_id: str = Field(..., description="所属引擎ID")
    
    # 溯源
    metadata: SourceMetadata

# 运行态模型
class FactorValue(BaseModel):
    """运行态因子值 - Calculator层计算产出"""
    factor_id: str
    value: Any
    confidence: float = Field(ge=0.0, le=1.0)
    source: str = Field(..., description="计算源：calculator/semantic/manual")

class FactorMatrix(BaseModel):
    """运行态因子矩阵 - 完整的因子集合"""
    factors: Dict[str, FactorValue]
    timestamp: datetime = Field(default_factory=datetime.now)
    engine_id: str
```

### 1.2 Markdown映射规则

| Markdown表格字段 | Python字段 | 映射规则 |
|-----------------|-----------|---------|
| 类别 | category | 中文→枚举值 |
| 中文名 | label_zh | 直接映射 |
| 因子ID | factor_id | 生成或提取 |
| 状态 | status | active/experimental/deprecated |
| 功能简述 | description_zh | 直接映射 |

### 1.3 中文到ID的映射示例

```python
# 映射规则
"甲木日主" → "day_master_jia"
"春季" → "season_spring"
"正官" → "ten_god_zhengguan"
"身强" → "strength_strong"
```

---

## 1.5 L2.5桥接层Schema（必选）

> **定位**：L2.5是L1L2精校的**必选输出**，为后续Logic-Agent和规则引擎提供结构化的因子关系、证据链和跨体系映射数据。
>
> **来源模板**：`典籍/精校模板_L1L2.md` §3 L2.5桥接层

### 1.5.1 ConfigRelation（因子关系）

```python
from pydantic import BaseModel, Field
from typing import Literal, Optional, List
from datetime import datetime

class RelationType(str, Enum):
    """关系类型枚举"""
    WUXING_SHENGKE = "wuxing_shengke"          # 五行生克
    DIZHI_INTERACTION = "dizhi_interaction"    # 地支刑冲合害
    TEN_GOD_RELATION = "ten_god_relation"      # 十神关系
    PLANET_HOUSE = "planet_house"              # 行星-宫位关系
    PLANET_ASPECT = "planet_aspect"            # 行星相位关系
    DREAM_SYMBOL_RELATION = "dream_symbol_relation"  # 梦境符号关系
    PSYCH_ARCHETYPE_RELATION = "psych_archetype_relation"  # 心理原型关系
    CROSS_SYSTEM = "cross_system"              # 跨体系映射关系

class EffectDirection(str, Enum):
    """效果方向枚举"""
    BENEFICIAL = "增益"
    HARMFUL = "损害"
    RESTRICTIVE = "限制"
    NEUTRAL = "中性"
    MIXED = "混合"

class ConfigRelation(BaseModel):
    """配置态因子关系 - 对应L2.5因子关系层表格"""
    
    # 标识
    relation_id: str = Field(
        ..., 
        regex="^rel_[a-z0-9_]+_\\d{3}$",
        description="关系ID，格式：rel_书籍简称_序号"
    )
    
    # 关系定义
    relation_type: RelationType
    factor_a: str = Field(..., description="因子A的factor_id")
    factor_b: str = Field(..., description="因子B的factor_id")
    relation_nature: str = Field(..., description="关系性质，如：生、克、冲、合")
    condition_constraint: Optional[str] = Field(None, description="条件约束，如：春季限定")
    effect_direction: EffectDirection
    
    # 溯源
    source_ref: str = Field(..., description="来源引用，格式：《书名》#章节")
    metadata: SourceMetadata
    
    # 版本
    version: str = Field(..., regex="^\\d+\\.\\d+\\.\\d+$")
    engine_id: str
    
    class Config:
        schema_extra = {
            "example": {
                "relation_id": "rel_dts_001",
                "relation_type": "wuxing_shengke",
                "factor_a": "day_master_jia",
                "factor_b": "element_fire",
                "relation_nature": "生",
                "effect_direction": "增益",
                "source_ref": "《滴天髓》#甲木条"
            }
        }
```

### 1.5.2 EvidenceChainEntry（证据链）

```python
class ConfidenceLevel(str, Enum):
    """置信度等级"""
    HIGH = "高"      # 原文明确陈述
    MEDIUM = "中"    # 原文有隐含暗示
    LOW = "低"       # 需要结合多处推断

class EvidenceChainEntry(BaseModel):
    """配置态证据链条目 - 对应L2.5推理溯源层表格"""
    
    # 标识
    evidence_id: str = Field(
        ..., 
        regex="^evi_[a-z0-9_]+_\\d{3}$",
        description="证据ID，格式：evi_书籍简称_序号"
    )
    
    # 证据链内容
    l1_anchor: str = Field(..., description="原文锚点（L1原文片段）")
    involved_factors: List[str] = Field(..., description="涉及的factor_id列表")
    reasoning_step: str = Field(..., description="推理步骤描述")
    conclusion_direction: str = Field(..., description="结论方向，如：吉、凶、中性")
    confidence: ConfidenceLevel
    
    # 规则关联
    can_generate_rule: bool = Field(..., description="是否可生成规则")
    target_rule_id: Optional[str] = Field(None, description="目标规则ID（如可生成规则）")
    
    # 溯源
    source_ref: str
    metadata: SourceMetadata
    
    # 版本
    version: str = Field(..., regex="^\\d+\\.\\d+\\.\\d+$")
    engine_id: str
    
    class Config:
        schema_extra = {
            "example": {
                "evidence_id": "evi_dts_001",
                "l1_anchor": "甲木参天，脱胎要火",
                "involved_factors": ["day_master_jia", "element_fire"],
                "reasoning_step": "甲木刚健需火泄秀，否则生机郁结",
                "conclusion_direction": "吉",
                "confidence": "高",
                "can_generate_rule": True,
                "target_rule_id": "rule_jia_needs_fire"
            }
        }
```

### 1.5.3 CrossSystemMapping（跨体系映射）

```python
class CrossSystemMapping(BaseModel):
    """配置态跨体系概念映射 - 对应L2.5跨体系映射层表格"""
    
    # 标识
    concept_id: str = Field(
        ..., 
        regex="^concept_[a-z0-9_]+$",
        description="概念ID，格式：concept_语义标签"
    )
    
    # 共通语义
    common_semantics: str = Field(..., description="共通语义核心描述")
    
    # 各体系对应因子
    bazi_factors: List[str] = Field(default_factory=list, description="八字对应factor_id列表")
    astro_factors: List[str] = Field(default_factory=list, description="占星对应factor_id列表")
    dream_factors: List[str] = Field(default_factory=list, description="梦学对应factor_id列表")
    psych_factors: List[str] = Field(default_factory=list, description="心理学对应factor_id列表")
    ziwei_factors: List[str] = Field(default_factory=list, description="紫微对应factor_id列表")
    tarot_factors: List[str] = Field(default_factory=list, description="塔罗对应factor_id列表")
    yijing_factors: List[str] = Field(default_factory=list, description="易经对应factor_id列表")
    
    # 备注
    notes: Optional[str] = None
    
    # 溯源
    source_refs: List[str] = Field(default_factory=list, description="来源引用列表")
    metadata: SourceMetadata
    
    # 版本
    version: str = Field(..., regex="^\\d+\\.\\d+\\.\\d+$")
    
    @validator('concept_id')
    def validate_has_at_least_two_systems(cls, v, values):
        """跨体系映射必须涉及至少两个体系"""
        systems = [
            values.get('bazi_factors', []),
            values.get('astro_factors', []),
            values.get('dream_factors', []),
            values.get('psych_factors', []),
            values.get('ziwei_factors', []),
            values.get('tarot_factors', []),
            values.get('yijing_factors', [])
        ]
        non_empty_systems = sum(1 for s in systems if s)
        if non_empty_systems < 2:
            raise ValueError('跨体系映射必须涉及至少两个体系')
        return v
    
    class Config:
        schema_extra = {
            "example": {
                "concept_id": "concept_authority_pressure",
                "common_semantics": "权威压力/父权/社会规范的限制",
                "bazi_factors": ["ten_god_qisha", "ten_god_zhengguan"],
                "astro_factors": ["saturn_square_sun", "saturn_conjunct_mc"],
                "dream_factors": ["dream_symbol_father", "dream_theme_exam"],
                "psych_factors": ["psych_archetype_shadow", "psych_process_shadow_integration"],
                "notes": "代表来自权威的压力与成长契机"
            }
        }
```

### 1.5.4 L2.5 Markdown映射规则

| Markdown表格字段 | Python字段 | 模型 | 映射规则 |
|-----------------|-----------|------|---------|
| 关系ID | relation_id | ConfigRelation | 直接映射 |
| 关系类型 | relation_type | ConfigRelation | 中文→枚举值 |
| 因子A | factor_a | ConfigRelation | 直接映射 |
| 因子B | factor_b | ConfigRelation | 直接映射 |
| 效果方向 | effect_direction | ConfigRelation | 中文→枚举值 |
| 证据ID | evidence_id | EvidenceChainEntry | 直接映射 |
| 原文锚点 | l1_anchor | EvidenceChainEntry | 直接映射 |
| 置信度 | confidence | EvidenceChainEntry | 高/中/低→枚举值 |
| 概念ID | concept_id | CrossSystemMapping | 直接映射 |
| 共通语义 | common_semantics | CrossSystemMapping | 直接映射 |

---

## 2. Content-L3规则层：规则契约 (Rule Schema)

**注意**：本章节定义的是**配置态模型**，用于Markdown提取和Codegen输入。运行时使用`RuntimeRuleResult`。

### 2.1 配置态规则模型

```python
class RuleCondition(BaseModel):
    """规则触发条件"""
    factor_id: str
    operator: Literal["==", "!=", ">", "<", ">=", "<=", "in", "exists"]
    value: Any

class LogicalExpression(BaseModel):
    """复合逻辑表达式"""
    operator: Literal["AND", "OR", "NOT"]
    conditions: List[Union[RuleCondition, "LogicalExpression"]]

class ConfigRuleResult(BaseModel):
    """配置态规则结果（规则定义时的静态配置）"""
    dimension: str = Field(..., description="维度：事业/健康/婚姻等")
    level: Literal["大吉", "吉", "中等", "凶", "大凶"]
    conclusion_template_zh: str = Field(..., description="中文结论模板，支持{factor_id}变量插值")
    weight: float = Field(default=1.0, ge=0.0, le=10.0)
    confidence: float = Field(default=0.8, ge=0.0, le=1.0)
    tags: List[str] = Field(default_factory=list)
    evidence_factors: List[str] = Field(default_factory=list)
    
    class Config:
        schema_extra = {
            "example": {
                "dimension": "事业",
                "level": "吉",
                "conclusion_template_zh": "由于{day_master}生于{season}，五行能量{energy_state}，适合发展领导才能。",
                "weight": 1.5,
                "confidence": 0.85
            }
        }

class ConfigRuleDefinition(BaseModel):
    """配置态规则定义"""
    rule_id: str = Field(..., regex="^[a-z][a-z0-9_]*$")
    human_label: str = Field(..., description="人话规则名")
    category: str = Field(..., description="规则分类")
    
    # 触发条件
    condition: Union[RuleCondition, LogicalExpression]
    required_factors: List[str] = Field(..., description="依赖的因子ID列表")
    
    # 复杂逻辑标记（逃生舱）
    is_complex_logic: bool = Field(default=False, description="是否为复杂逻辑，需人工Python实现")
    python_handler_ref: Optional[str] = Field(None, description="复杂规则的Python函数名")
    
    # 结果与优先级
    result: ConfigRuleResult
    priority: int = Field(default=100, ge=0, le=999)
    
    # 互斥组（冲突解决）
    exclusive_group: Optional[str] = Field(None, description="互斥组ID，同组规则不应同时触发")
    
    # 版本与归属
    version: str = Field(..., regex="^\\d+\\.\\d+\\.\\d+$", description="规则包版本")
    status: Literal["active", "experimental", "deprecated"] = "active"
    engine_id: str = Field(..., description="所属引擎ID")
    
    metadata: SourceMetadata
    
    class Config:
        schema_extra = {
            "example": {
                "rule_id": "dts_complex_001",
                "human_label": "天干透出地支藏干被冲",
                "is_complex_logic": True,
                "python_handler_ref": "evaluate_tiangan_chong",
                "exclusive_group": "body_strength_group",
                "version": "1.0.0",
                "engine_id": "bazi_doushu"
            }
        }

# 运行态模型
class RuntimeRuleResult(BaseModel):
    """运行态规则执行结果 - Rule Engine实际返回"""
    rule_id: str
    matched: bool
    
    # 仅匹配时填充
    dimension: Optional[str] = None
    level: Optional[str] = None
    description: Optional[str] = None  # 模板渲染后的成品文案
    
    # 运行时元数据
    confidence: float
    weight: float
    tags: List[str]
    evidence_factors: List[str]
    semantic_refs: List[str] = []  # 关联的语义条目ID
    
    # 溯源信息
    source_book: Optional[str] = None
    l1_anchor: Optional[str] = None
    execution_time_ms: float
```

### 2.2 Codegen映射规则

**严格映射**（禁止跨用）：

```python
CODEGEN_MAPPING = {
    # 配置态 → Codegen → 运行态
    "ConfigRuleDefinition": "Python函数 → 返回RuntimeRuleResult",
    "ConfigRuleResult.conclusion_template_zh": "TemplateEngine → RuntimeRuleResult.description",
    "ConfigFactor": "Calculator → FactorValue → FactorMatrix",
    
    # 禁止行为
    "FORBIDDEN": [
        "直接读取ConfigRuleDefinition进行规则执行",
        "将RuntimeRuleResult序列化回JSON作为配置源",
        "在Fusion中混用Config和Runtime类型",
        "跳过Codegen直接消费JSON配置"
    ]
}
```

### 2.3 规则示例

```python
# 八字规则示例
{
    "rule_id": "dts_jia_spring_001",
    "human_label": "甲木春生得时",
    "condition": {
        "operator": "AND",
        "conditions": [
            {"factor_id": "day_master_jia", "operator": "==", "value": true},
            {"factor_id": "season", "operator": "==", "value": "spring"}
        ]
    },
    "required_factors": ["day_master_jia", "season"],
    "result": {
        "dimension": "personality",
        "level": "吉",
        "conclusion_template_zh": "甲木生于春季，木气当令，性格积极向上"
    }
}
```

---

## 3. L4叙事层：叙事配置契约 (Narrative Schema)

### 3.1 叙事配置模型

```python
class NarrativeConfig(BaseModel):
    """叙事配置"""
    config_id: str
    target_rule_patterns: List[str]  # 支持通配符
    
    # 风格
    tone: Literal["professional", "friendly", "mystical", "scientific"]
    audience_level: Literal["beginner", "intermediate", "advanced"]
    
    # 多语言/多产品线支持（扩展字段）
    locale: str = Field("zh-CN", regex="^[a-z]{2}-[A-Z]{2}$")
    product_line: str = "default"
    channel: Literal["app", "web", "miniapp", "api"] = "app"
    risk_disclosure: Literal["none", "brief", "detailed"] = "brief"
    
    # 长度
    min_length: int = Field(50, ge=10)
    max_length: int = Field(500, le=2000)
    
    # 证据展示
    show_evidence: bool = True
    evidence_detail_level: Literal["simple", "detailed", "full"] = "simple"
    
    # Prompt模板
    prompt_templates: Dict[str, str] = {}
```

### 3.2 配置示例

```python
{
    "config_id": "bazi_career_friendly",
    "target_rule_patterns": ["bazi_career_*"],
    "tone": "friendly",
    "audience_level": "intermediate",
    "prompt_templates": {
        "opening": "让我们一起探讨您的事业发展...",
        "evidence": "根据您的命盘显示...",
        "conclusion": "综合来看..."
    }
}
```

### 3.3 FusionResult契约（融合层输出）

**定位**：Layer4融合层的标准输出契约，被TOON序列化和叙事生成使用。

```python
class ConflictWarning(BaseModel):
    """冲突警告"""
    group: str = Field(..., description="互斥组ID")
    conflicting_rules: List[str] = Field(..., description="冲突的规则ID列表")
    severity: Literal["LOW", "MEDIUM", "HIGH"]
    resolution_strategy: str

class FusionResult(BaseModel):
    """融合结果契约 - Layer4标准输出"""
    fusion_id: str = Field(..., regex="^fus_[a-z0-9]{12}$")
    
    # 核心输出
    primary_themes: List[str] = Field(..., max_items=5, description="主要主题，最多5个")
    evidence_chain: List[RuntimeRuleResult] = Field(..., max_items=20, description="证据链")
    
    # 置信度矩阵
    confidence_matrix: Dict[str, float] = Field(
        ..., 
        description="维度→置信度映射，如{'事业':0.85,'健康':0.72}"
    )
    
    # 交叉验证
    cross_validation_score: float = Field(..., ge=0.0, le=1.0, description="多引擎一致性分数")
    contributing_engines: List[str] = Field(default_factory=list, description="参与融合的引擎ID")
    
    # 冲突信息
    conflicts: List[ConflictWarning] = Field(default_factory=list)
    
    # 元数据
    fusion_time_ms: float = Field(..., description="融合耗时（毫秒）")
    created_at: datetime = Field(default_factory=datetime.now)
    
    class Config:
        schema_extra = {
            "example": {
                "fusion_id": "fus_abc123456789",
                "primary_themes": ["事业突破", "财富积累", "人际拓展"],
                "cross_validation_score": 0.87,
                "contributing_engines": ["bazi_rule_engine", "tarot_semantic"],
                "fusion_time_ms": 45.2
            }
        }
```

### 3.4 NarrativeSnippet（叙事素材）

**定位**：承载从典籍精校与L2语义提取得到的原子化叙事片段，在叙事生成时与TOON一起作为LLM参考输入。

```python
class SnippetRole(str, Enum):
    """叙事素材逻辑角色"""
    MAIN = "主干"              # 核心论述
    MAIN_DEPENDENCY = "主干依赖"  # 主干成立的前提
    CONDITIONAL = "条件分支"     # 特定条件下的变体
    EXCEPTION = "例外处理"       # 异常情况
    SUMMARY = "总结"            # 归纳性陈述

class NarrativeSnippet(BaseModel):
    """配置态叙事素材 - 对应L1精校中的narrative_snippets"""
    
    # 标识
    snippet_id: str = Field(
        ..., 
        regex="^[a-z][a-z0-9_]*_\\d{3}$",
        description="叙事素材ID，格式：书籍简称_主题_序号"
    )
    
    # 触发条件
    trigger_condition: str = Field(
        ..., 
        description="触发条件，与因子/规则系统共享命名空间，如：day_master=甲 AND month∈[寅,卯]"
    )
    
    # 逻辑角色
    role: SnippetRole = Field(..., description="在推理链中的逻辑位置")
    
    # 语言与内容
    primary_lang: Literal["zh-CN", "en-US"] = Field(
        ..., 
        description="主语种，中文典籍为zh-CN，英文典籍为en-US"
    )
    snippet_text: str = Field(
        ..., 
        min_length=5,
        max_length=200,
        description="精校后的主语种短句，建议10-40字/词，满足原子化原则"
    )
    
    # 溯源
    source_ref: str = Field(..., description="来源引用，格式：《书名》#章节#行号")
    metadata: SourceMetadata
    
    # 关联
    related_factors: List[str] = Field(
        default_factory=list, 
        description="关联的factor_id列表"
    )
    related_rules: List[str] = Field(
        default_factory=list, 
        description="关联的rule_id列表"
    )
    
    # 版本
    version: str = Field(..., regex="^\\d+\\.\\d+\\.\\d+$")
    engine_id: str
    
    class Config:
        schema_extra = {
            "example": {
                "snippet_id": "dts_jia_spring_001",
                "trigger_condition": "day_master=甲 AND month∈[寅,卯]",
                "role": "主干",
                "primary_lang": "zh-CN",
                "snippet_text": "甲木生于春，得时得令，如参天大树。",
                "source_ref": "《滴天髓》#通神论#L23",
                "related_factors": ["day_master_jia", "season_spring"],
                "related_rules": ["rule_jia_spring_strong"]
            }
        }
```

**约束说明**：
- `snippet_id`：全局唯一ID，建议与规则/语义ID保持可追溯关系
- `trigger_condition`：与因子/规则系统共享同一`factor_id`/`rule_id`命名空间，用于在RuntimeRuleResult命中时检索合适片段
- `role`：逻辑角色，对应精校模板中的`role: 逻辑位置`字段，**仅允许五个枚举值**
- `snippet_text`：需满足「最大拆分 + 单一语义单元」原则

> 从典籍精校到 NarrativeSnippet 的完整链路与工程细节，见 `docs/ls_knowledge_to_output_pipeline.md` 第五章；
> 片段拆分与`role`标注规范应与《典籍/精校模板_L1L2.md》与《典籍/texts/Western_Texts_Template.md》中关于narrative_snippets的要求保持完全一致。

### 3.5 LogicChain（逻辑链）

**定位**：由Logic-Agent构建的推理结构，连接叙事素材形成完整的论证链。每本书产出一个逻辑链文件。

```python
class LogicNode(BaseModel):
    """逻辑链节点"""
    node_id: str = Field(..., description="节点ID")
    snippet_ids: List[str] = Field(..., description="关联的NarrativeSnippet ID列表")
    role: SnippetRole = Field(..., description="节点在推理链中的角色")
    condition: Optional[str] = Field(None, description="节点激活条件")
    summary: str = Field(..., description="节点语义摘要")

class LogicEdge(BaseModel):
    """逻辑链边"""
    from_node: str = Field(..., description="起始节点ID")
    to_node: str = Field(..., description="目标节点ID")
    relation: Literal["depends_on", "leads_to", "conflicts_with", "supports"] = Field(
        ..., 
        description="边的关系类型"
    )
    condition: Optional[str] = Field(None, description="边的激活条件")

class LogicChain(BaseModel):
    """逻辑链 - 单书推理结构"""
    
    # 标识
    chain_id: str = Field(
        ..., 
        regex="^chain_[a-z0-9_]+$",
        description="逻辑链ID，格式：chain_书籍简称"
    )
    book_id: str = Field(..., description="来源书籍ID")
    
    # 结构
    nodes: List[LogicNode] = Field(..., description="逻辑节点列表")
    edges: List[LogicEdge] = Field(..., description="逻辑边列表")
    
    # 叙事顺序
    narrative_order: List[str] = Field(
        ..., 
        description="推荐的叙事输出顺序（节点ID列表）"
    )
    
    # 入口与出口
    entry_nodes: List[str] = Field(..., description="入口节点ID列表（无前置依赖）")
    terminal_nodes: List[str] = Field(..., description="终端节点ID列表（总结性节点）")
    
    # 元数据
    metadata: SourceMetadata
    version: str = Field(..., regex="^\\d+\\.\\d+\\.\\d+$")
    
    @validator('edges')
    def validate_edge_references(cls, v, values):
        """确保所有边引用的节点都存在"""
        if 'nodes' in values:
            node_ids = {n.node_id for n in values['nodes']}
            for edge in v:
                if edge.from_node not in node_ids:
                    raise ValueError(f"Edge references non-existent node: {edge.from_node}")
                if edge.to_node not in node_ids:
                    raise ValueError(f"Edge references non-existent node: {edge.to_node}")
        return v
    
    class Config:
        schema_extra = {
            "example": {
                "chain_id": "chain_ditianshui",
                "book_id": "ditianshui",
                "nodes": [
                    {"node_id": "n1", "snippet_ids": ["dts_jia_001"], "role": "主干", "summary": "甲木基本特性"},
                    {"node_id": "n2", "snippet_ids": ["dts_jia_002"], "role": "条件分支", "summary": "春季特殊表现"}
                ],
                "edges": [
                    {"from_node": "n1", "to_node": "n2", "relation": "leads_to"}
                ],
                "narrative_order": ["n1", "n2"],
                "entry_nodes": ["n1"],
                "terminal_nodes": ["n2"]
            }
        }
```

### 3.6 AssemblyProtocol（组装协议）

**定位**：定义规则命中后如何组装叙事素材，包括冲突解决、叙事顺序和风格控制。

```python
class ConflictResolutionStrategy(str, Enum):
    """冲突解决策略"""
    PRIORITY_BASED = "priority_based"      # 按优先级选择
    WEIGHT_BASED = "weight_based"          # 按权重选择
    CONFIDENCE_BASED = "confidence_based"  # 按置信度选择
    SOURCE_BASED = "source_based"          # 按典籍权威性选择
    MERGE = "merge"                        # 合并展示（标注分歧）

class NarrativeOrderStrategy(str, Enum):
    """叙事顺序策略"""
    LOGIC_CHAIN = "logic_chain"            # 按逻辑链顺序
    CONFIDENCE_DESC = "confidence_desc"    # 按置信度降序
    DIMENSION_GROUP = "dimension_group"    # 按维度分组
    CHRONOLOGICAL = "chronological"        # 按时间顺序（流年类）

class AssemblyProtocol(BaseModel):
    """组装协议 - 定义叙事素材如何组装成最终输出"""
    
    # 标识
    protocol_id: str = Field(
        ..., 
        regex="^asm_[a-z0-9_]+$",
        description="协议ID"
    )
    
    # 适用范围
    target_dimensions: List[str] = Field(
        ..., 
        description="适用的维度列表，如：['事业', '财富']"
    )
    target_engines: List[str] = Field(
        default_factory=list, 
        description="适用的引擎ID列表，空表示全部"
    )
    
    # 冲突解决
    conflict_resolution: ConflictResolutionStrategy = Field(
        default=ConflictResolutionStrategy.PRIORITY_BASED,
        description="冲突解决策略"
    )
    
    # 叙事顺序
    narrative_order: NarrativeOrderStrategy = Field(
        default=NarrativeOrderStrategy.LOGIC_CHAIN,
        description="叙事顺序策略"
    )
    
    # 素材选择
    max_snippets_per_dimension: int = Field(
        default=5, 
        ge=1, 
        le=20,
        description="每个维度最多选择的素材数量"
    )
    role_priority: List[SnippetRole] = Field(
        default=[
            SnippetRole.MAIN,
            SnippetRole.MAIN_DEPENDENCY,
            SnippetRole.CONDITIONAL,
            SnippetRole.EXCEPTION,
            SnippetRole.SUMMARY
        ],
        description="角色优先级顺序"
    )
    
    # 输出控制
    include_source_citation: bool = Field(
        default=True, 
        description="是否包含典籍引用"
    )
    include_confidence_indicator: bool = Field(
        default=False, 
        description="是否显示置信度指示"
    )
    
    # 版本
    version: str = Field(..., regex="^\\d+\\.\\d+\\.\\d+$")
    
    class Config:
        schema_extra = {
            "example": {
                "protocol_id": "asm_career_standard",
                "target_dimensions": ["事业", "财富"],
                "conflict_resolution": "priority_based",
                "narrative_order": "logic_chain",
                "max_snippets_per_dimension": 5,
                "include_source_citation": True
            }
        }
```

---

## 4. 人话到机器话的映射表

### 4.1 八字系统映射

| 人话（Markdown） | 机器话（factor_id） | 说明 |
|-----------------|-------------------|------|
| 甲木日主 | day_master_jia | 日柱天干 |
| 乙木日主 | day_master_yi | 日柱天干 |
| 春季 | season_spring | 季节 |
| 夏季 | season_summer | 季节 |
| 正官 | ten_god_zhengguan | 十神 |
| 七杀 | ten_god_qisha | 十神 |
| 身强 | strength_strong | 日主强度 |
| 身弱 | strength_weak | 日主强度 |

### 4.2 塔罗系统映射

| 人话（Markdown） | 机器话（factor_id） | 说明 |
|-----------------|-------------------|------|
| 愚者 | tarot_fool | 大阿卡纳 |
| 魔术师 | tarot_magician | 大阿卡纳 |
| 权杖牌组 | suit_wands | 小阿卡纳 |
| 圣杯牌组 | suit_cups | 小阿卡纳 |
| 正位 | orientation_upright | 牌面方向 |
| 逆位 | orientation_reversed | 牌面方向 |

### 4.3 占星系统映射

| 人话（Markdown） | 机器话（factor_id） | 说明 |
|-----------------|-------------------|------|
| 太阳白羊 | sun_in_aries | 行星星座 |
| 月亮巨蟹 | moon_in_cancer | 行星星座 |
| 第一宫 | house_1 | 宫位 |
| 上升点 | ascendant | 关键点 |

### 4.4 紫微系统映射

| 人话（Markdown） | 机器话（factor_id） | 说明 |
|-----------------|-------------------|------|
| 紫微星 | ziwei_star_ziwei | 十四主星 |
| 天机星 | ziwei_star_tianji | 十四主星 |
| 太阳星 | ziwei_star_taiyang | 十四主星 |
| 武曲星 | ziwei_star_wuqu | 十四主星 |
| 天同星 | ziwei_star_tiantong | 十四主星 |
| 廉贞星 | ziwei_star_lianzhen | 十四主星 |
| 天府星 | ziwei_star_tianfu | 十四主星 |
| 太阴星 | ziwei_star_taiyin | 十四主星 |
| 贪狼星 | ziwei_star_tanlang | 十四主星 |
| 巨门星 | ziwei_star_jumen | 十四主星 |
| 天相星 | ziwei_star_tianxiang | 十四主星 |
| 天梁星 | ziwei_star_tianliang | 十四主星 |
| 七杀星 | ziwei_star_qisha | 十四主星 |
| 破军星 | ziwei_star_pojun | 十四主星 |
| 命宫 | ziwei_palace_ming | 十二宫 |
| 兄弟宫 | ziwei_palace_xiongdi | 十二宫 |
| 夫妻宫 | ziwei_palace_fuqi | 十二宫 |
| 子女宫 | ziwei_palace_zinv | 十二宫 |
| 财帛宫 | ziwei_palace_caibo | 十二宫 |
| 疾厄宫 | ziwei_palace_jie | 十二宫 |
| 迁移宫 | ziwei_palace_qianyi | 十二宫 |
| 交友宫 | ziwei_palace_jiaoyou | 十二宫 |
| 官禄宫 | ziwei_palace_guanlu | 十二宫 |
| 田宅宫 | ziwei_palace_tianzhai | 十二宫 |
| 福德宫 | ziwei_palace_fude | 十二宫 |
| 父母宫 | ziwei_palace_fumu | 十二宫 |
| 化禄 | ziwei_transform_lu | 四化 |
| 化权 | ziwei_transform_quan | 四化 |
| 化科 | ziwei_transform_ke | 四化 |
| 化忌 | ziwei_transform_ji | 四化 |
| 左辅 | ziwei_aux_zuofu | 辅星 |
| 右弼 | ziwei_aux_youbi | 辅星 |
| 文昌 | ziwei_aux_wenchang | 辅星 |
| 文曲 | ziwei_aux_wenqu | 辅星 |

### 4.5 易经系统映射

| 人话（Markdown） | 机器话（factor_id） | 说明 |
|-----------------|-------------------|------|
| 乾卦 | yijing_gua_qian | 八卦/六十四卦 |
| 坤卦 | yijing_gua_kun | 八卦/六十四卦 |
| 震卦 | yijing_gua_zhen | 八卦/六十四卦 |
| 巽卦 | yijing_gua_xun | 八卦/六十四卦 |
| 坎卦 | yijing_gua_kan | 八卦/六十四卦 |
| 离卦 | yijing_gua_li | 八卦/六十四卦 |
| 艮卦 | yijing_gua_gen | 八卦/六十四卦 |
| 兑卦 | yijing_gua_dui | 八卦/六十四卦 |
| 上卦 | yijing_upper_trigram | 卦象结构 |
| 下卦 | yijing_lower_trigram | 卦象结构 |
| 互卦 | yijing_mutual_gua | 卦象结构 |
| 变卦 | yijing_changed_gua | 卦象结构 |
| 初爻 | yijing_yao_1 | 爻位 |
| 二爻 | yijing_yao_2 | 爻位 |
| 三爻 | yijing_yao_3 | 爻位 |
| 四爻 | yijing_yao_4 | 爻位 |
| 五爻 | yijing_yao_5 | 爻位 |
| 上爻 | yijing_yao_6 | 爻位 |
| 阳爻 | yijing_yang_yao | 爻性 |
| 阴爻 | yijing_yin_yao | 爻性 |
| 动爻 | yijing_moving_yao | 爻性 |

### 4.6 梦境系统映射

| 人话（Markdown） | 机器话（factor_id） | 说明 |
|-----------------|-------------------|------|
| 动物符号 | dream_symbol_animal | 符号类别 |
| 人物符号 | dream_symbol_person | 符号类别 |
| 场景符号 | dream_symbol_scene | 符号类别 |
| 物品符号 | dream_symbol_object | 符号类别 |
| 自然符号 | dream_symbol_nature | 符号类别 |
| 身体符号 | dream_symbol_body | 符号类别 |
| 追逐主题 | dream_theme_chase | 主题 |
| 坠落主题 | dream_theme_falling | 主题 |
| 飞行主题 | dream_theme_flying | 主题 |
| 考试主题 | dream_theme_exam | 主题 |
| 裸体主题 | dream_theme_naked | 主题 |
| 死亡主题 | dream_theme_death | 主题 |
| 迷路主题 | dream_theme_lost | 主题 |
| 水主题 | dream_theme_water | 主题 |
| 恐惧情绪 | dream_emotion_fear | 情绪 |
| 愉悦情绪 | dream_emotion_joy | 情绪 |
| 焦虑情绪 | dream_emotion_anxiety | 情绪 |
| 平静情绪 | dream_emotion_calm | 情绪 |
| 愤怒情绪 | dream_emotion_anger | 情绪 |

### 4.7 心理学系统映射

| 人话（Markdown） | 机器话（factor_id） | 说明 |
|-----------------|-------------------|------|
| 阴影原型 | psych_archetype_shadow | 荣格原型 |
| 阿尼玛原型 | psych_archetype_anima | 荣格原型 |
| 阿尼姆斯原型 | psych_archetype_animus | 荣格原型 |
| 智慧老人原型 | psych_archetype_wise_old_man | 荣格原型 |
| 大母神原型 | psych_archetype_great_mother | 荣格原型 |
| 自性原型 | psych_archetype_self | 荣格原型 |
| 人格面具原型 | psych_archetype_persona | 荣格原型 |
| 永恒少年原型 | psych_archetype_puer | 荣格原型 |
| 思维功能 | psych_function_thinking | 心理功能 |
| 情感功能 | psych_function_feeling | 心理功能 |
| 感觉功能 | psych_function_sensation | 心理功能 |
| 直觉功能 | psych_function_intuition | 心理功能 |
| 内倾态度 | psych_attitude_introvert | 态度类型 |
| 外倾态度 | psych_attitude_extravert | 态度类型 |
| 个体化进程 | psych_process_individuation | 发展阶段 |
| 阴影整合 | psych_process_shadow_integration | 发展阶段 |

### 4.8 Geocoding 系统映射

| 人话（Markdown） | 机器话（factor_id） | 说明 |
|-----------------|-------------------|------|
| 出生地 | geo_birth_place | 出生地名 |
| 经度 | geo_longitude | 经度坐标 |
| 纬度 | geo_latitude | 纬度坐标 |
| 时区 | geo_timezone | IANA时区标识 |
| 国家代码 | geo_country_code | ISO 3166-1 alpha-2 |
| 城市名 | geo_city_name | 标准城市名 |

---

## 4.9 Geocoding Schema 定义

**定位**：地理编码服务的数据模型，为需要位置信息的 Calculator（BaZi、ZiWei、Astro、Yijing-时间起卦）提供经纬度和时区解析能力。

### 4.9.1 Place Schema

```python
from dataclasses import dataclass
from typing import Optional, Literal

@dataclass
class Place:
    """
    Canonical place object returned by geocoding service.
    
    地理编码服务返回的标准地点对象，包含坐标、时区和元数据。
    """
    place_id: str
    """Unique place identifier, e.g., 'gn-2038060'"""
    
    country_code: str
    """ISO 3166-1 alpha-2 country code"""
    
    city_name: str
    """Canonical city name"""
    
    lat: float
    """Latitude (-90 to 90)"""
    
    lng: float
    """Longitude (-180 to 180)"""
    
    timezone: str
    """IANA timezone identifier, e.g., 'Asia/Shanghai'"""
    
    source: Literal['local_db', 'amap', 'nominatim', 'manual']
    """Data source indicator"""
    
    accuracy: Literal['city'] = 'city'
    """Resolution accuracy level"""
    
    admin1_code: Optional[str] = None
    """First-level administrative division code"""
    
    admin1_name: Optional[str] = None
    """First-level administrative division name"""
    
    district_name_raw: Optional[str] = None
    """Raw district name for display only"""
```

### 4.9.2 ResolvePlaceInput Schema

```python
@dataclass
class ResolvePlaceInput:
    """
    Input for place resolution.
    
    地点解析请求的输入参数。
    """
    input_text: str
    """User-provided location text (Chinese or English)"""
    
    hint_country: Optional[str] = None
    """Optional ISO 3166-1 alpha-2 country code hint"""
    
    hint_label: Optional[str] = None
    """Semantic label, e.g., 'birth_place', 'current_city'"""
    
    user_id: Optional[str] = None
    """User identifier for user-level caching"""
```

### 4.9.3 LocationResolver Pattern

```python
from typing import Optional, Tuple

class LocationResolver:
    """
    位置解析器 - 在 Calculator 外部处理 Geocoding。
    
    设计理由：
    1. Calculator 保持纯同步计算，便于测试和复用
    2. Geocoding 是 I/O 操作，应在调用层处理
    3. 支持批量解析和缓存优化
    
    优先级：birth_location > birth_place
    """
    
    async def resolve(
        self,
        birth_place: Optional[str],
        birth_location: Optional[Tuple[float, float]],
        timezone: Optional[str] = None
    ) -> Tuple[Tuple[float, float], str]:
        """
        解析位置信息。
        
        Returns:
            Tuple of (longitude, latitude) and timezone
        
        Raises:
            InvalidInputError: Neither birth_place nor birth_location provided
            GeocodingError: Failed to resolve birth_place
        """
        ...
    
    def resolve_sync(
        self,
        birth_place: Optional[str],
        birth_location: Optional[Tuple[float, float]],
        timezone: Optional[str] = None
    ) -> Tuple[Tuple[float, float], str]:
        """同步版本，用于非异步上下文。"""
        ...
```

### 4.9.4 Geocoding Factor ID 映射

| Factor ID | 类型 | 说明 |
|-----------|------|------|
| geo_place_id | string | 地点唯一标识 |
| geo_country_code | string | ISO 3166-1 alpha-2 国家代码 |
| geo_city_name | string | 标准城市名 |
| geo_lat | float | 纬度 |
| geo_lng | float | 经度 |
| geo_timezone | string | IANA 时区标识 |
| geo_source | enum | 数据来源：local_db/amap/nominatim/manual |
| geo_accuracy | enum | 精度级别：city |

---

## 4.10 Layer 1 Calculator Schema 定义

**定位**：Layer 1 Calculator 的输入/输出模型定义，所有 Calculator 输出统一的 FactorMatrix 格式。

### 4.10.1 AstroCalculator Schema

**功能**：西洋占星计算器，计算星历、宫位、相位。需要位置信息。

#### AstroInput

```python
from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from typing import Optional, Literal

class AstroInput(BaseModel):
    """
    Western astrology calculation input model.
    
    Supports two location input methods:
    1. birth_location: Direct coordinates (backward compatible)
    2. birth_place: City name, resolved via GeocodingService
    
    Priority: birth_location > birth_place
    """
    birth_datetime: datetime = Field(..., description="出生日期时间 (公历)")
    birth_place: Optional[str] = Field(
        default=None,
        description="出生地名（中文或英文），如 '北京' 或 'New York, USA'"
    )
    birth_location: Optional[tuple[float, float]] = Field(
        default=None,
        description="(经度, 纬度)，经度范围-180~180，纬度范围-90~90"
    )
    timezone: Optional[str] = Field(
        default=None,
        description="时区标识，如 'Asia/Shanghai', 'America/New_York'"
    )
    house_system: Literal["placidus", "koch", "equal", "whole_sign"] = Field(
        default="placidus",
        description="宫位系统"
    )
    
    @model_validator(mode='after')
    def validate_location(self) -> 'AstroInput':
        """Validate that at least one location field is provided."""
        if not self.birth_place and not self.birth_location:
            raise ValueError("Either birth_place or birth_location must be provided")
        return self
```

#### PlanetPosition

```python
class PlanetPosition(BaseModel):
    """Planetary position data."""
    planet: str = Field(..., description="Planet name (lowercase)")
    longitude: float = Field(..., ge=0.0, lt=360.0, description="Ecliptic longitude 0-360°")
    latitude: float = Field(..., ge=-90.0, le=90.0, description="Ecliptic latitude")
    distance: float = Field(..., gt=0.0, description="Distance in AU")
    speed: float = Field(..., description="Daily motion in degrees/day")
    sign: str = Field(..., description="Zodiac sign")
    degree_in_sign: float = Field(..., ge=0.0, lt=30.0, description="Degree within sign 0-30°")
    house: int = Field(..., ge=1, le=12, description="House placement 1-12")
    retrograde: bool = Field(..., description="Whether planet is retrograde")
```

#### Aspect

```python
class Aspect(BaseModel):
    """Aspect between two planets."""
    planet1: str = Field(..., description="First planet")
    planet2: str = Field(..., description="Second planet")
    aspect_type: Literal["conjunction", "opposition", "trine", "square", "sextile"]
    exact_angle: float = Field(..., description="Exact angle between planets")
    orb: float = Field(..., ge=0.0, description="Actual orb (deviation from exact)")
    applying: bool = Field(..., description="Whether aspect is applying (forming)")
```

#### AstroFactors

```python
class AstroFactors(BaseModel):
    """
    Western astrology factors output model.
    
    Contains complete chart data and provides to_factor_matrix() method
    to convert to unified FactorMatrix format for Layer 2.
    """
    planets: Dict[str, PlanetPosition] = Field(..., description="Planet positions keyed by planet name")
    houses: Dict[int, float] = Field(..., description="House cusp degrees (1-12)")
    ascendant: float = Field(..., ge=0.0, lt=360.0, description="Ascendant degree")
    midheaven: float = Field(..., ge=0.0, lt=360.0, description="Midheaven (MC) degree")
    ascendant_sign: str = Field(..., description="Ascendant sign")
    midheaven_sign: str = Field(..., description="Midheaven sign")
    aspects: List[Aspect] = Field(default_factory=list, description="List of aspects")
    julian_day: float = Field(..., description="Julian Day number")
    house_system: str = Field(default="placidus", description="House system used")
    calculation_time_ms: float = Field(default=0.0, description="Calculation time in ms")
    
    def to_factor_matrix(self) -> FactorMatrix:
        """Convert to unified FactorMatrix format."""
        ...
```

#### AstroCalculator Factor ID 映射

| Factor ID Pattern | 类型 | 说明 |
|-------------------|------|------|
| astro_{planet}_in_{sign} | boolean | 行星在星座，如 astro_sun_in_aries |
| astro_{planet}_house_{n} | boolean | 行星在宫位，如 astro_moon_house_4 |
| astro_{planet}_retrograde | boolean | 行星逆行，如 astro_mercury_retrograde |
| astro_{planet}_longitude | float | 行星黄道经度 |
| astro_ascendant | string | 上升星座 |
| astro_midheaven | string | 中天星座 |
| astro_ascendant_degree | float | 上升点度数 |
| astro_midheaven_degree | float | 中天度数 |
| astro_{p1}_{aspect}_{p2} | boolean | 相位，如 astro_sun_trine_moon |
| astro_house_{n}_cusp | float | 宫头度数 |

**行星列表**：sun, moon, mercury, venus, mars, jupiter, saturn, uranus, neptune, pluto

**星座列表**：aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius, pisces

**相位类型**：conjunction, opposition, trine, square, sextile

---

### 4.10.2 TarotInterpreter Schema

**功能**：塔罗牌解释器，解析牌阵和牌义。不需要位置信息。

#### TarotInput

```python
class CardInfo(BaseModel):
    """Card information from input."""
    card_name: str = Field(..., description="Card name (English)")
    reversed: bool = Field(default=False, description="Whether card is reversed")
    position: Optional[str] = Field(None, description="Position in spread")

class TarotInput(BaseModel):
    """
    Tarot interpretation input model.
    
    Does NOT require location information.
    """
    spread_type: Literal["single", "three_card", "celtic_cross", "custom"] = Field(
        ..., description="牌阵类型"
    )
    cards: List[CardInfo] = Field(
        ..., 
        min_length=1,
        description="牌阵中的牌列表"
    )
    question: Optional[str] = Field(None, description="问题（可选）")
    
    @model_validator(mode='after')
    def validate_spread(self) -> 'TarotInput':
        """Validate that card count matches spread type."""
        expected_counts = {"single": 1, "three_card": 3, "celtic_cross": 10, "custom": None}
        expected = expected_counts.get(self.spread_type)
        if expected is not None and len(self.cards) != expected:
            raise ValueError(f"Spread type '{self.spread_type}' requires {expected} cards")
        return self
```

#### CardInterpretation

```python
class CardInterpretation(BaseModel):
    """Interpretation for a single card."""
    card_name: str = Field(..., description="Card name (English)")
    card_name_zh: str = Field(..., description="Card name (Chinese)")
    card_number: int = Field(..., ge=0, le=77, description="Card number 0-77")
    suit: Optional[Literal["wands", "cups", "swords", "pentacles"]] = Field(
        None, description="Suit for Minor Arcana"
    )
    is_major: bool = Field(..., description="Whether card is Major Arcana")
    reversed: bool = Field(..., description="Whether card is reversed")
    position: str = Field(..., description="Position in spread")
    position_meaning: str = Field(..., description="Meaning of position")
```

#### TarotFactors

```python
class TarotFactors(BaseModel):
    """
    Tarot factors output model.
    
    Contains complete interpretation data and provides to_factor_matrix() method.
    """
    cards: List[CardInterpretation] = Field(..., description="Interpreted cards")
    spread_type: str = Field(..., description="Spread type used")
    question: Optional[str] = Field(None, description="Question asked")
    calculation_time_ms: float = Field(default=0.0, description="Calculation time in ms")
    
    def to_factor_matrix(self) -> FactorMatrix:
        """Convert to unified FactorMatrix format."""
        ...
```

#### TarotInterpreter Factor ID 映射

| Factor ID Pattern | 类型 | 说明 |
|-------------------|------|------|
| tarot_spread_{type} | boolean | 牌阵类型，如 tarot_spread_three_card |
| tarot_major_{card}_{orientation} | boolean | 大阿卡纳，如 tarot_major_the_fool_upright |
| tarot_{suit}_{card}_{orientation} | boolean | 小阿卡纳，如 tarot_wands_ace_reversed |
| tarot_position_{pos}_{card} | boolean | 位置牌，如 tarot_position_past_the_fool |
| tarot_card_number_{n} | boolean | 牌号，如 tarot_card_number_0 |

**大阿卡纳 (0-21)**：the_fool, the_magician, the_high_priestess, the_empress, the_emperor, the_hierophant, the_lovers, the_chariot, strength, the_hermit, wheel_of_fortune, justice, the_hanged_man, death, temperance, the_devil, the_tower, the_star, the_moon, the_sun, judgement, the_world

**小阿卡纳花色**：wands (权杖), cups (圣杯), swords (宝剑), pentacles (钱币)

**牌阵位置**：answer, past, present, future, challenge, above, below, advice, external, hopes_fears, outcome

---

### 4.10.3 DreamExtractor Schema

**功能**：梦境符号提取器，匹配符号和主题。不需要位置信息。

#### DreamInput

```python
class DreamInput(BaseModel):
    """
    Dream extraction input model.
    
    Does NOT require location information.
    """
    dream_text: str = Field(
        ..., 
        min_length=10, 
        description="梦境描述文本，至少10个字符"
    )
    language: Literal["zh", "en"] = Field(
        default="zh", 
        description="文本语言：zh=中文, en=英文"
    )
```

#### DreamSymbol

```python
class DreamSymbol(BaseModel):
    """A single dream symbol identified from text."""
    symbol: str = Field(..., description="Symbol name (normalized)")
    category: Literal["animal", "person", "scene", "object", "nature", "body"]
    confidence: float = Field(..., ge=0.0, le=1.0, description="Match confidence")
    matched_text: str = Field(..., description="Original text that matched")
```

#### DreamFactors

```python
class DreamFactors(BaseModel):
    """
    Dream factors output model.
    
    Contains extracted symbols, themes, and emotions.
    """
    symbols: List[DreamSymbol] = Field(default_factory=list, description="Extracted dream symbols")
    themes: List[str] = Field(default_factory=list, description="Detected dream themes")
    emotions: List[str] = Field(default_factory=list, description="Detected emotional tones")
    raw_tokens: List[str] = Field(default_factory=list, description="Tokenization result")
    language: str = Field(default="zh", description="Input language")
    calculation_time_ms: float = Field(default=0.0, description="Calculation time in ms")
    
    def to_factor_matrix(self) -> FactorMatrix:
        """Convert to unified FactorMatrix format."""
        ...
```

#### DreamExtractor Factor ID 映射

| Factor ID Pattern | 类型 | 说明 |
|-------------------|------|------|
| dream_symbol_{category}_{symbol} | boolean | 符号，如 dream_symbol_animal_dog |
| dream_theme_{theme} | boolean | 主题，如 dream_theme_flying |
| dream_emotion_{emotion} | boolean | 情绪，如 dream_emotion_fear |

**符号类别**：animal (动物), person (人物), scene (场景), object (物品), nature (自然), body (身体)

**主题列表**：chase, falling, flying, exam, death, water, lost, naked, teeth, late, trapped, reunion, journey, conflict, transformation

**情绪列表**：fear, joy, anxiety, calm, anger, sadness, confusion, excitement, peace, surprise

---

### 4.10.4 YijingCalculator Schema

**功能**：六爻/易经计算器，计算卦象、爻变、互卦。时间起卦需要位置信息。

#### YijingInput

```python
class YijingInput(BaseModel):
    """
    六爻计算输入模型.
    
    Supports multiple divination methods:
    - coin: Three-coin toss simulation
    - yarrow: Traditional yarrow stalk method
    - time: Time-based hexagram generation (requires location)
    - manual: Direct line value input
    """
    divination_method: Literal["coin", "yarrow", "time", "manual"] = Field(
        ..., description="起卦方法"
    )
    manual_lines: Optional[List[int]] = Field(
        default=None,
        description="手动输入的六爻值 (6=老阴, 7=少阳, 8=少阴, 9=老阳)，从初爻到上爻"
    )
    birth_place: Optional[str] = Field(
        default=None,
        description="位置（用于时间起卦的真太阳时计算）"
    )
    query_time: Optional[datetime] = Field(
        default=None,
        description="起卦时间，默认当前时间"
    )
    question: Optional[str] = Field(
        default=None,
        description="所问问题（可选，用于记录）"
    )
    
    @model_validator(mode='after')
    def validate_manual_lines(self) -> 'YijingInput':
        """Validate manual_lines when divination_method is 'manual'."""
        if self.divination_method == 'manual':
            if not self.manual_lines or len(self.manual_lines) != 6:
                raise ValueError("manual method requires exactly 6 line values")
            for line in self.manual_lines:
                if line not in {6, 7, 8, 9}:
                    raise ValueError(f"Invalid line value: {line}")
        return self
```

#### Hexagram

```python
class Hexagram(BaseModel):
    """卦象 (Hexagram) model."""
    number: int = Field(..., ge=1, le=64, description="卦序号 1-64")
    name_zh: str = Field(..., description="中文名称")
    name_pinyin: str = Field(..., description="拼音")
    upper_trigram: str = Field(..., description="上卦名")
    lower_trigram: str = Field(..., description="下卦名")
    lines: List[int] = Field(..., min_length=6, max_length=6, description="六爻值 (0=阴, 1=阳)")
    raw_lines: Optional[List[int]] = Field(default=None, description="原始六爻值 (6/7/8/9)")
```

#### YijingFactors

```python
class YijingFactors(BaseModel):
    """
    六爻因子输出模型.
    
    包含完整的卦象信息，并提供 to_factor_matrix() 方法。
    """
    main_hexagram: Hexagram = Field(..., description="主卦")
    mutual_hexagram: Hexagram = Field(..., description="互卦（取2-5爻组成）")
    changed_hexagram: Optional[Hexagram] = Field(default=None, description="变卦")
    moving_lines: List[int] = Field(default_factory=list, description="动爻位置 (1-6)")
    divination_method: str = Field(..., description="起卦方法")
    query_time: Optional[datetime] = Field(default=None, description="起卦时间")
    question: Optional[str] = Field(default=None, description="所问问题")
    calculation_time_ms: float = Field(default=0.0, description="计算耗时(ms)")
    
    def to_factor_matrix(self) -> FactorMatrix:
        """Convert to unified FactorMatrix format."""
        ...
```

#### YijingCalculator Factor ID 映射

| Factor ID Pattern | 类型 | 说明 |
|-------------------|------|------|
| yijing_gua_{pinyin} | boolean | 主卦，如 yijing_gua_qian |
| yijing_gua_number | int | 卦序号 1-64 |
| yijing_upper_trigram | string | 上卦名 |
| yijing_lower_trigram | string | 下卦名 |
| yijing_mutual_{pinyin} | boolean | 互卦，如 yijing_mutual_kun |
| yijing_changed_{pinyin} | boolean | 变卦，如 yijing_changed_zhen |
| yijing_moving_yao_{n} | boolean | 动爻位置，如 yijing_moving_yao_3 |
| yijing_method_{method} | boolean | 起卦方法，如 yijing_method_coin |
| yijing_line_{n} | string | 爻值 (yang/yin)，如 yijing_line_1 |

**八卦列表**：qian (乾), kun (坤), zhen (震), xun (巽), kan (坎), li (离), gen (艮), dui (兑)

**起卦方法**：coin (铜钱法), yarrow (蓍草法), time (时间起卦), manual (手动输入)

**爻值说明**：
- 6 = 老阴（动爻，阴变阳）
- 7 = 少阳（静爻，阳）
- 8 = 少阴（静爻，阴）
- 9 = 老阳（动爻，阳变阴）

---

## 5. 变量插值与模板引擎

### 5.1 插值语法规范

```python
from string import Template
from typing import Dict, Any
import re

class TemplateEngine:
    """模板引擎 - 支持变量插值"""
    
    # 支持的插值语法
    PATTERNS = {
        "simple": r"\{(\w+)\}",  # {factor_id}
        "dotted": r"\{(\w+\.\w+)\}",  # {day_master.element}
        "filter": r"\{(\w+)\|(\w+)\}"  # {season|chinese}
    }
    
    @staticmethod
    def render(template: str, context: Dict[str, Any]) -> str:
        """渲染模板"""
        # 简单变量替换
        for match in re.finditer(TemplateEngine.PATTERNS["simple"], template):
            factor_id = match.group(1)
            if factor_id in context:
                value = context[factor_id]
                template = template.replace(match.group(0), str(value))
        
        return template

# 示例使用
template = "由于{day_master}生于{season}，五行能量{energy_state}，适合{career_direction}。"
context = {
    "day_master": "甲木",
    "season": "春季",
    "energy_state": "旺盛",
    "career_direction": "创业创新"
}
result = TemplateEngine.render(template, context)
# 输出："由于甲木生于春季，五行能量旺盛，适合创业创新。"
```

### 5.2 变量名规范

- 所有插值变量必须是已注册的factor_id
- 支持点分隔的属性访问：`{day_master.element}`
- 支持过滤器：`{season|chinese}` 输出中文名
- 禁止任意代码执行

## 6. 复杂规则处理（逃生舱）

### 6.1 复杂规则标记

```python
class ComplexRuleMarker:
    """复杂规则标记器"""
    
    # 复杂度指标
    COMPLEXITY_INDICATORS = [
        "天干透出",
        "地支藏干",
        "三合",
        "六冲",
        "相刑",
        "反吟",
        "伏吟",
        "流年作用"
    ]
    
    @staticmethod
    def should_mark_complex(rule_text: str) -> bool:
        """判断是否应标记为复杂规则"""
        for indicator in ComplexRuleMarker.COMPLEXITY_INDICATORS:
            if indicator in rule_text:
                return True
        return False

# 复杂规则Python实现模板
def evaluate_tiangan_chong(factor_matrix: FactorMatrix) -> RuntimeRuleResult:
    """
    复杂规则：天干透出地支藏干被冲
    此函数由人工编写，不由JSON生成
    """
    # 从因子矩阵提取业务逻辑所需数据
    tiangan = factor_matrix.factors.get("tiangan").value
    dizhi = factor_matrix.factors.get("dizhi").value
    hidden_stems = factor_matrix.factors.get("hidden_stems").value
    
    # 判断透出情况
    for gan in tiangan:
        if gan in hidden_stems and is_clashed(dizhi):
            return RuntimeRuleResult(
                rule_id="tiangan_chong_001",
                matched=True,
                dimension="命格",
                level="凶",
                description="天干透出被冲，事业多波折",
                confidence=0.85,
                weight=1.5,
                tags=["天干冲克", "事业"],
                evidence_factors=["tiangan", "dizhi", "hidden_stems"],
                execution_time_ms=2.5
            )
    
    return RuntimeRuleResult(
        rule_id="tiangan_chong_001",
        matched=False,
        confidence=1.0,
        weight=0.0,
        tags=[],
        evidence_factors=[],
        execution_time_ms=1.2
    )
```

## 7. 冲突解决与互斥组

### 7.1 互斥组定义

```python
class ExclusiveGroups:
    """互斥组管理"""
    
    GROUPS = {
        "body_strength_group": [
            "rule_body_strong",
            "rule_body_weak",
            "rule_body_neutral"
        ],
        "wealth_pattern_group": [
            "rule_wealth_abundant",
            "rule_wealth_scarce",
            "rule_wealth_broken"
        ],
        "career_direction_group": [
            "rule_career_north",
            "rule_career_south",
            "rule_career_east",
            "rule_career_west"
        ]
    }
    
    @staticmethod
    def validate_results(results: List[RuntimeRuleResult]) -> List[ConflictWarning]:
        """检查互斥冲突"""
        warnings = []
        
        for group_name, rule_ids in ExclusiveGroups.GROUPS.items():
            triggered_rules = [
                r for r in results 
                if r.rule_id in rule_ids and r.matched
            ]
            
            if len(triggered_rules) > 1:
                warnings.append(ConflictWarning(
                    group=group_name,
                    conflicting_rules=[r.rule_id for r in triggered_rules],
                    severity="HIGH",
                    resolution_strategy="priority_based"  # 或 "weight_based"
                ))
        
        return warnings
```

### 7.2 冲突解决策略

```python
class ConflictResolver:
    """冲突解决器"""
    
    STRATEGIES = {
        "priority_based": lambda rules: max(rules, key=lambda r: r.weight),  # 运行态用weight替代priority
        "weight_based": lambda rules: max(rules, key=lambda r: r.weight),
        "confidence_based": lambda rules: max(rules, key=lambda r: r.confidence),
        "source_based": lambda rules: rules[0]  # 优先选择特定典籍
    }
    
    @staticmethod
    def resolve(conflicting_rules: List[RuntimeRuleResult], 
                strategy: str = "priority_based") -> RuntimeRuleResult:
        """解决冲突，返回最终选中的规则"""
        resolver = ConflictResolver.STRATEGIES.get(
            strategy, 
            ConflictResolver.STRATEGIES["priority_based"]
        )
        return resolver(conflicting_rules)
```

## 8. 三层测试体系Schema

**定位**：与架构文档《ls_engine_architecture_v3.md §10.7》完全对齐，构建Unit→Integration→Product三层测试金字塔。

### 8.1 规则级测试（Unit）

```python
class RuleTestCase(BaseModel):
    """单条规则测试用例 - Agent自动生成"""
    test_id: str
    target_rule_id: str
    test_type: Literal["positive", "negative", "edge"]
    
    # 输入数据
    mock_factors: Dict[str, Any] = Field(..., description="模拟因子值")
    
    # 期望结果
    expect_hit: bool = Field(..., description="是否应该触发")
    expected_dimension: Optional[str] = None
    expected_level: Optional[str] = None
    expected_confidence_min: float = Field(0.0, ge=0.0, le=1.0, description="期望置信度下限")
    expected_confidence_max: float = Field(1.0, ge=0.0, le=1.0, description="期望置信度上限")
    
    # 溯源
    source_book: str
    l1_anchor: Optional[str]
    description: str

### 8.2 引擎级测试（Integration）

```python
class GoldenCase(BaseModel):
    """黄金测试用例 - 多引擎集成基线"""
    case_id: str
    
    # 完整输入
    birth_data: dict[str, Any]
    
    # 多引擎基线
    expected_results: dict[str, Any] = Field(
        ...,
        description="各引擎期望输出"
    )
    
    # 融合基线
    expected_fusion: dict = Field(
        ...,
        description="FusionResult的themes/cross_validation_score基线"
    )
    
    # 容差
    max_drift: float = Field(0.1, description="允许的最大漂移")
    baseline_hash: Optional[str] = Field(None, description="基线版本哈希")

### 8.3 叙事级测试（Product）

```python
class NarrativeGolden(BaseModel):
    """叙事黄金标准 - 产品级质量验收"""
    golden_id: str
    
    # 输入场景
    scenario: dict[str, Any]
    
    # 期望特征
    must_include_themes: list[str] = Field(
        ...,
        description="必须出现的主题关键字"
    )
    
    forbidden_expressions: list[str] = Field(
        default_factory=list,
        description="禁用的偏差表述"
    )
    
    # 质量阈值
    min_quality_score: float = Field(0.8, ge=0.0, le=1.0)
    eval_model: str = Field(..., description="使用的Eval-Agent模型")
    
    # 历史基线
    historical_avg_score: float = Field(..., description="历史版本平均得分")
```

### 8.4 测试金字塔与验收标准

| 层级 | 覆盖率目标 | 运行频率 | 失败处理 |
|------|-----------|---------|---------|
| Rule (Unit) | 100% | 每次提交 | 阻断合并 |
| Golden (Integration) | 核心场景100% | 每日CI/CD | 告警+人工复核 |
| Narrative (Product) | 关键旅程100% | 发布前 | 阻断发布 |

**发布前检查清单**：
- 所有RuleTestCase全部通过
- GoldenCase漂移 < max_drift
- NarrativeGolden质量 >= min_quality_score且不低于历史均值
- 性能基准测试无明显退化
```

## 9. 数据验证规则

### 9.1 因子验证

```python
class FactorValidator:
    """因子验证器"""
    
    @staticmethod
    def validate(factor: ConfigFactor) -> List[str]:
        errors = []
        
        # ID格式验证
        if not factor.factor_id.islower():
            errors.append(f"factor_id必须全小写: {factor.factor_id}")
        
        # 必填字段验证
        if not factor.description_zh:
            errors.append("缺少中文描述")
        
        # 状态验证（更新为正确的枚举值）
        if factor.status not in ["active", "experimental", "deprecated"]:
            errors.append(f"无效状态值: {factor.status}")
        
        # 版本与引擎ID验证
        if not factor.version:
            errors.append("缺少版本号")
        if not factor.engine_id:
            errors.append("缺少引擎ID")
        
        # 实验性因子必须标注来源
        if factor.status == "experimental" and not factor.metadata.book_id:
            errors.append("实验性因子必须标注来源")
        
        return errors
```

### 9.2 规则验证

```python
class RuleValidator:
    """规则验证器"""
    
    @staticmethod
    def validate(rule: ConfigRuleDefinition, factor_registry: Set[str]) -> List[str]:
        errors = []
        
        # 因子引用验证
        for factor_id in rule.required_factors:
            if factor_id not in factor_registry:
                errors.append(f"引用了未定义的因子: {factor_id}")
        
        # 优先级验证
        if rule.priority < 0 or rule.priority > 999:
            errors.append(f"优先级超出范围: {rule.priority}")
        
        # 版本与引擎ID验证
        if not rule.version:
            errors.append("缺少版本号")
        if not rule.engine_id:
            errors.append("缺少引擎ID")
        
        # 状态验证
        if rule.status not in ["active", "experimental", "deprecated"]:
            errors.append(f"无效状态值: {rule.status}")
        
        # 复杂规则必须指定handler
        if rule.is_complex_logic and not rule.python_handler_ref:
            errors.append("复杂规则必须指定python_handler_ref")
        
        return errors
```

---

## 9.5 引擎注册表Schema

**定位**：统一管理多体系引擎的元信息与状态。

```python
from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime

class EngineDescriptor(BaseModel):
    """引擎描述符 - 引擎注册表核心模型"""
    engine_id: str = Field(
        ...,
        regex="^[a-z][a-z0-9_]*$",
        description="引擎唯一标识"
    )
    
    kind: Literal[
        "calculator",  # 计算器（Layer1）
        "semantic",    # 语义引擎（Layer2）
        "rule",        # 规则引擎（Layer3）
        "fusion"       # 融合引擎（Layer4）
    ]
    
    # 能力声明
    supported_dimensions: list[str] = Field(
        ...,
        description="支持的维度：事业、财富、婚姻、健康等"
    )
    
    supported_systems: list[str] = Field(
        ...,
        description="支持的体系：bazi/tarot/astrology/dream/zwds"
    )
    
    # 默认配置
    default_weight: float = Field(
        1.0,
        ge=0.0,
        le=10.0,
        description="融合时的默认权重"
    )
    
    # 依赖声明
    depends_on: List[str] = Field(
        default_factory=list,
        description="依赖的引擎ID列表，如fusion引擎依赖哪些rule引擎"
    )
    
    # 状态管理
    status: Literal[
        "active",       # 生产可用
        "experimental", # 实验性
        "deprecated"    # 已废弃
    ]
    
    # 责任归属
    owner_team: str = Field(
        ...,
        description="负责团队：content/engine/product"
    )
    
    # 版本信息
    version: str = Field(..., regex="^\\d+\\.\\d+\\.\\d+$")
    created_at: datetime
    updated_at: datetime
    
    # 性能指标
    avg_execution_time_ms: Optional[float] = Field(
        None,
        description="平均执行时间"
    )
    
    class Config:
        schema_extra = {
            "example": {
                "engine_id": "bazi_doushu",
                "kind": "rule",
                "supported_dimensions": ["事业", "财富", "婚姻", "健康"],
                "supported_systems": ["bazi", "zwds"],
                "default_weight": 1.5,
                "status": "active",
                "owner_team": "content",
                "version": "1.2.0"
            }
        }

# 引擎注册表示例（覆盖全部7体系）
ENGINE_REGISTRY_EXAMPLE = [
    # ===== Layer 1: Calculator =====
    {"engine_id": "bazi_calculator", "kind": "calculator", "supported_systems": ["bazi"], "status": "active"},
    {"engine_id": "ziwei_calculator", "kind": "calculator", "supported_systems": ["ziwei"], "status": "active"},
    {"engine_id": "yijing_calculator", "kind": "calculator", "supported_systems": ["yijing"], "status": "active"},
    {"engine_id": "astro_calculator", "kind": "calculator", "supported_systems": ["astrology"], "status": "active"},
    {"engine_id": "tarot_interpreter", "kind": "calculator", "supported_systems": ["tarot"], "status": "active"},
    {"engine_id": "dream_extractor", "kind": "calculator", "supported_systems": ["dream"], "status": "active"},
    
    # ===== Layer 2: Semantic =====
    {"engine_id": "bazi_semantic", "kind": "semantic", "supported_systems": ["bazi"], "status": "active"},
    {"engine_id": "ziwei_semantic", "kind": "semantic", "supported_systems": ["ziwei"], "status": "active"},
    {"engine_id": "yijing_semantic", "kind": "semantic", "supported_systems": ["yijing"], "status": "active"},
    {"engine_id": "astro_semantic", "kind": "semantic", "supported_systems": ["astrology"], "status": "active"},
    {"engine_id": "tarot_semantic", "kind": "semantic", "supported_systems": ["tarot"], "status": "active"},
    {"engine_id": "dream_semantic", "kind": "semantic", "supported_systems": ["dream"], "status": "active"},
    {"engine_id": "psychology_semantic", "kind": "semantic", "supported_systems": ["psychology"], "status": "active"},  # 跨体系底层
    
    # ===== Layer 3: Rule =====
    {"engine_id": "bazi_rule_engine", "kind": "rule", "supported_systems": ["bazi"], "status": "active"},
    {"engine_id": "ziwei_rule_engine", "kind": "rule", "supported_systems": ["ziwei"], "status": "active"},
    {"engine_id": "yijing_rule_engine", "kind": "rule", "supported_systems": ["yijing"], "status": "active"},
    {"engine_id": "astro_rule_engine", "kind": "rule", "supported_systems": ["astrology"], "status": "active"},
    {"engine_id": "tarot_rule_engine", "kind": "rule", "supported_systems": ["tarot"], "status": "active"},
    {"engine_id": "dream_rule_engine", "kind": "rule", "supported_systems": ["dream"], "status": "active"},
    {"engine_id": "psychology_rule_engine", "kind": "rule", "supported_systems": ["psychology"], "status": "active"},  # 跨体系原型规则
    
    # ===== Layer 4: Fusion =====
    {"engine_id": "cross_system_fusion", "kind": "fusion", "supported_systems": ["bazi", "ziwei", "yijing", "astrology", "tarot", "dream"], "status": "active"}
]
```

**注册约束**：
- `PreferenceManager`和`FusionEngine`只接受`engine_id`属于注册表中的引擎
- 新增体系（例如新塔罗引擎）必须先在`EngineDescriptor`注册
- 引擎状态变更必须通过版本升级体现
- `deprecated`引擎必须保留至少两个版本周期
- 所有`ConfigFactor`和`ConfigRuleDefinition`必须指定`engine_id`

---

## 9.6 记忆层Schema定义

**定位**：结构化存储用户事件、洞察与长期画像，支持隐私分级。

```python
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal, Optional, Any
from enum import Enum

class PrivacyLevel(str, Enum):
    """隐私级别枚举"""
    PUBLIC = "public"          # 可以用于匿名统计/模型训练
    PRIVATE = "private"        # 仅该用户可见
    SENSITIVE = "sensitive"    # 禁止用于训练，需加密存储

class MemoryBase(BaseModel):
    """记忆基类"""
    privacy: PrivacyLevel = PrivacyLevel.PRIVATE

# ============ Event层：原始事件 ============

class Event(MemoryBase):
    """原始事件记录"""
    event_id: str = Field(..., regex="^evt_[a-z0-9]{12}$")
    user_id: str
    timestamp: datetime
    
    kind: Literal[
        "dream_record",      # 梦境记录
        "reading_request",   # 解读请求
        "feedback",          # 用户反馈
        "profile_edit",      # 档案编辑
        "preference_change", # 偏好调整
        "system_action"      # 系统动作
    ]
    
    payload: dict[str, Any]  # 仅边界JSON，内部转换成专门类型
    source_channel: Literal["app", "web", "miniapp", "partner_api"]
    sensitive: bool = False
    
    class Config:
        schema_extra = {
            "example": {
                "event_id": "evt_abc123456789",
                "user_id": "user_12345",
                "kind": "dream_record",
                "payload": {"dream_text": "梦到飞在天空"},
                "privacy": "private"
            }
        }

# ============ Insight层：结构化洞察 ============

class Insight(MemoryBase):
    """结构化洞察"""
    insight_id: str = Field(..., regex="^ins_[a-z0-9]{12}$")
    user_id: str
    created_at: datetime
    
    # 来源关联
    factors: list[str] = Field(default_factory=list, description="关联的factor_id")
    rules: list[str] = Field(default_factory=list, description="关联的rule_id")
    themes: list[str] = Field(
        default_factory=list,
        description="主题标签，如：事业突破窗口、情感风险"
    )
    
    # 核心内容
    summary_zh: str = Field(..., max_length=200, description="结构化短句，复杂洞察可用更长描述")
    strength: float = Field(..., ge=0.0, le=1.0, description="置信度")
    time_scope: Literal["past", "present", "near_future", "long_term"]
    
    class Config:
        schema_extra = {
            "example": {
                "insight_id": "ins_xyz987654321",
                "user_id": "user_12345",
                "summary_zh": "事业发展进入突破期",
                "strength": 0.85,
                "time_scope": "near_future",
                "themes": ["事业突破", "领导力提升"],
                "privacy": "private"
            }
        }

# ============ Profile层：长期画像 ============

class UserProfile(MemoryBase):
    """用户长期画像"""
    user_id: str
    
    # 稳定特质
    traits: dict[str, float] = Field(
        default_factory=dict,
        description="性格特质，如risk_tolerance:0.7"
    )
    
    # 偏好设置
    preferences: dict[str, Any] = Field(
        default_factory=dict,
        description="引擎偏好、语言偏好、叙事风格等"
    )
    
    # 长期主轴
    long_term_themes: list[str] = Field(
        default_factory=list,
        description="长期叙事主轴"
    )
    
    # 元信息
    last_updated: datetime
    update_count: int = 0
    
    class Config:
        schema_extra = {
            "example": {
                "user_id": "user_12345",
                "traits": {"risk_tolerance": 0.7, "creativity": 0.9},
                "preferences": {"language": "zh", "tone": "friendly"},
                "long_term_themes": ["事业发展", "家庭平衡"],
                "privacy": "private"
            }
        }
```

**记忆层约束**：
- **Event层**：只存原始事实，不做推断
- **Insight层**：只存结构化洞察，禁止直接存LLM自然语言段落
- **Profile层**：只存稳定trait/偏好，不存一次性情绪
- **SENSITIVE级别数据**：必须使用AES-256加密存储，禁止用于任何形式的模型训练
- **TOON payload**：禁止携带SENSITIVE内容
- **跨层查询**：必须通过`MemoryService`接口，不得直接访问数据库

**SENSITIVE字段示例**：
```python
SENSITIVE_FIELDS = {
    "UserProfile": ["real_name", "phone_number", "email", "address", "id_number"],
    "Event.payload": ["location_detail", "contacts", "medical_history"]
}
```

---

## 9.7 Action层Schema定义

**定位**：将 Playbook/Dream/Insight 等"认知层"输出编译为可执行的行动步骤（Action），支持反馈闭环和行为分析。

**设计原则**：
- **与Memory层解耦**：ActionBase 独立于 MemoryBase，修改 Memory 层不影响 Action 层编译
- **显式来源引用**：通过 ActionSourceRef 关联 Insight/Playbook，而非继承
- **两级实现**：Level 1 内核先行，Level 2 分析随后

### 9.7.1 Action层枚举定义

```python
from enum import Enum

class ActionSourceKind(str, Enum):
    """Action来源类型"""
    PLAYBOOK = "playbook"           # 来自Playbook生成
    DREAM_INSIGHT = "dream_insight" # 来自梦境解读
    ASTRO_TRANSIT = "astro_transit" # 来自占星流年
    MANUAL = "manual"               # 用户手动创建
    SYSTEM = "system"               # 系统自动生成

class ActionTimeScope(str, Enum):
    """行动时间范围"""
    TODAY = "today"                 # 今日
    THIS_WEEK = "this_week"         # 本周
    THIS_MONTH = "this_month"       # 本月
    LONG_TERM = "long_term"         # 长期（模板）

class ActionContext(str, Enum):
    """行动适用情境"""
    MORNING = "morning"             # 早晨
    WORK = "work"                   # 工作时间
    EVENING = "evening"             # 晚间
    WEEKEND = "weekend"             # 周末
    FLEXIBLE = "flexible"           # 灵活时间

class ActionStatus(str, Enum):
    """行动状态"""
    TODO = "todo"                   # 待办
    DOING = "doing"                 # 进行中
    DONE = "done"                   # 已完成
    SKIPPED = "skipped"             # 跳过
    EXPIRED = "expired"             # 过期

class EffortEstimate(str, Enum):
    """预计投入"""
    MINIMAL = "minimal"             # <5分钟
    LOW = "low"                     # 5-15分钟
    MEDIUM = "medium"               # 15-30分钟
    HIGH = "high"                   # 30-60分钟
    MAJOR = "major"                 # >1小时

class InsightCompileStatus(str, Enum):
    """Insight编译状态"""
    NEW = "new"                     # 新建，待编译
    COMPILED = "compiled"           # 已编译为ActionItem
    TEMPLATE_CREATED = "template_created"  # 已生成长期模板
    ARCHIVED = "archived"           # 已归档
```

### 9.7.2 ActionBase 基类

**设计理由**：ActionBase 不继承 MemoryBase，确保 Memory 层演化时 Action 层不需大规模重构。

```python
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ActionBase(BaseModel):
    """
    Action层轻量基类 - 与MemoryBase解耦
    
    设计约束：
    - 不继承MemoryBase
    - 通过ActionSourceRef显式关联Memory/Insight
    - 修改MemoryBase不影响Action层编译
    """
    id: str = Field(
        ..., 
        regex="^(aprj|aitm)_[a-z0-9]{12}$",
        description="Action对象ID，前缀区分类型：aprj=Project, aitm=Item"
    )
    user_id: str = Field(..., description="所属用户ID")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
```

### 9.7.3 ActionSourceRef 来源引用

```python
from typing import List, Optional

class ActionSourceRef(BaseModel):
    """
    Action来源引用 - 显式关联而非继承
    
    用于追溯Action的生成来源，支持多源聚合。
    """
    kind: ActionSourceKind = Field(..., description="来源类型")
    source_id: str = Field(..., description="来源对象ID（Insight/Playbook ID）")
    source_summary: str = Field(
        ..., 
        max_length=200,
        description="来源内容摘要，用于展示"
    )
    factor_ids: List[str] = Field(
        default_factory=list,
        description="关联的因子ID列表，用于溯源"
    )
    rule_ids: List[str] = Field(
        default_factory=list,
        description="关联的规则ID列表，用于溯源"
    )
    
    class Config:
        schema_extra = {
            "example": {
                "kind": "playbook",
                "source_id": "ins_abc123456789",
                "source_summary": "本周事业运势：适合主动出击，把握机会",
                "factor_ids": ["ten_god_zhengguan", "astro_sun_trine_jupiter"],
                "rule_ids": ["rule_career_expansion_001"]
            }
        }
```

### 9.7.4 ActionProject 行动项目

```python
from typing import List

class ActionProject(ActionBase):
    """
    行动项目 - 长期或周期性行动计划的容器
    
    用途：
    - 承载同一主题的多个ActionItem
    - 支持长期模板（如"每周社交拓展"）
    - 聚合多个来源的建议
    """
    title: str = Field(..., max_length=100, description="项目标题")
    time_scope: ActionTimeScope = Field(..., description="时间范围")
    sources: List[ActionSourceRef] = Field(
        default_factory=list,
        description="来源引用列表（支持多源聚合）"
    )
    status: ActionStatus = Field(default=ActionStatus.TODO)
    
    # 统计字段
    total_items: int = Field(default=0, description="包含的Item总数")
    completed_items: int = Field(default=0, description="已完成的Item数")
    
    class Config:
        schema_extra = {
            "example": {
                "id": "aprj_abc123456789",
                "user_id": "user_12345",
                "title": "本周事业拓展计划",
                "time_scope": "this_week",
                "status": "todo",
                "sources": [
                    {
                        "kind": "playbook",
                        "source_id": "ins_abc123456789",
                        "source_summary": "适合主动出击的一周"
                    }
                ]
            }
        }
```

### 9.7.5 ActionItem 行动条目

**Level 1 版本**：feedback 作为内联字段，简化实现。

```python
from typing import Optional

class ActionItem(ActionBase):
    """
    行动条目 - 单个可执行的行动步骤
    
    Level 1 设计：
    - feedback 作为内联字段（feedback_status + feedback_note）
    - 不单独建ActionFeedback表
    - 状态变更时写入Memory.Event
    """
    # 基本信息
    project_id: Optional[str] = Field(
        None, 
        regex="^aprj_[a-z0-9]{12}$",
        description="所属项目ID（可选，支持独立Item）"
    )
    title: str = Field(..., max_length=200, description="行动标题")
    reason: str = Field(
        ..., 
        max_length=500,
        description="建议理由（来自Playbook/Insight的解释）"
    )
    
    # 执行参数
    effort_estimate: EffortEstimate = Field(
        default=EffortEstimate.MEDIUM,
        description="预计投入"
    )
    context: ActionContext = Field(
        default=ActionContext.FLEXIBLE,
        description="适用情境"
    )
    due_date: Optional[datetime] = Field(None, description="截止日期")
    
    # 状态
    status: ActionStatus = Field(default=ActionStatus.TODO)
    
    # 来源追溯
    source: ActionSourceRef = Field(..., description="来源引用")
    
    # Level 1 内联反馈字段
    feedback_status: Optional[str] = Field(
        None, 
        description="反馈状态：completed/partial/skipped/difficult"
    )
    feedback_note: Optional[str] = Field(
        None, 
        max_length=500,
        description="用户反馈备注"
    )
    feedback_at: Optional[datetime] = Field(None, description="反馈时间")
    
    class Config:
        schema_extra = {
            "example": {
                "id": "aitm_def456789012",
                "user_id": "user_12345",
                "project_id": "aprj_abc123456789",
                "title": "主动联系一位潜在合作伙伴",
                "reason": "本周正官得力，适合拓展正式合作关系",
                "effort_estimate": "medium",
                "context": "work",
                "status": "todo",
                "source": {
                    "kind": "playbook",
                    "source_id": "ins_abc123456789",
                    "source_summary": "事业运势建议"
                }
            }
        }
```

### 9.7.6 Action层约束

```python
ACTION_CONSTRAINTS = [
    # 模型解耦约束
    "AC-01: Action系列类型不得继承MemoryBase，只能通过ActionSourceRef引用",
    "AC-02: ActionSourceRef.source_id必须是合法的Insight/Playbook ID",
    "AC-03: 修改MemoryBase不得导致Action层编译失败",
    
    # 编译约束
    "AC-04: 单条Insight最多编译一次（通过InsightCompileStatus控制）",
    "AC-05: 长期建议生成Template，短期建议直接生成ActionItem",
    "AC-06: Daily/Weekly Compile显式定义输入集合，排除已编译Insight",
    "AC-07: 短期Insight编译后标记COMPILED，过期后归档而非重复生成",
    
    # 状态流转约束
    "AC-08: ActionItem状态变更(TODO/DOING→DONE/SKIPPED/EXPIRED)必须写feedback",
    "AC-09: ActionItem完成/跳过时必须派生Memory.Event",
    "AC-10: ActionItem过期(>7天)自动标记EXPIRED并写入回避分析队列",
    
    # 回避分析约束
    "AC-11: 连续3周回避同类Action时FeedbackAnalyzer生成AvoidanceInsight",
    "AC-12: AvoidanceInsight写入Memory.Insight，可被Playbook消费"
]
```

### 9.7.7 Action ID 格式

| 前缀 | 类型 | 示例 |
|------|------|------|
| aprj_ | ActionProject | aprj_abc123456789 |
| aitm_ | ActionItem | aitm_def456789012 |

**ID生成规则**：
- 前缀 + 12位小写字母数字（nanoid或uuid截取）
- 全局唯一，用于跨表关联

### 9.7.8 Action层与Memory层映射

```
┌─────────────────────────────────────────────────────────────────┐
│  Memory.Insight / Playbook (认知层)                              │
│  ├── 事业建议: "本周适合主动出击"                                  │
│  └── 梦境解读: "梦中飞翔象征突破欲望"                              │
└─────────────────────────────────────────────────────────────────┘
                          ↓ [ActionCompiler编译]
┌─────────────────────────────────────────────────────────────────┐
│  ActionProject + ActionItem (计划层)                             │
│  ├── 项目: "本周事业拓展"                                         │
│  └── 条目: "主动联系合作伙伴" (source → Insight)                  │
└─────────────────────────────────────────────────────────────────┘
                          ↓ [用户执行 + 反馈]
┌─────────────────────────────────────────────────────────────────┐
│  ActionItem.feedback (内联反馈)                                   │
│  ├── feedback_status: "completed"                                │
│  └── feedback_note: "已联系3位，其中1位有意向"                     │
└─────────────────────────────────────────────────────────────────┘
                          ↓ [状态变更触发]
┌─────────────────────────────────────────────────────────────────┐
│  Memory.Event (事件层)                                           │
│  └── event_type: "action_completed", payload: {...}              │
└─────────────────────────────────────────────────────────────────┘
                          ↓ [FeedbackAnalyzer分析]
┌─────────────────────────────────────────────────────────────────┐
│  Memory.Insight / Profile (洞察层)                               │
│  └── "用户在社交类Action上完成率较高，建议持续强化"                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 10. 交付标准与目录结构

### 10.1 配置源码vs编译产物

**核心原则**：JSON/JSONL是配置源码，Python是编译产物，运行时只认Python。

#### 配置源码目录（Config Source）

```
data/
├── factors/               # 因子配置源码
│   ├── bazi/
│   │   ├── factors.jsonl          # 八字因子定义（ConfigFactor）
│   │   └── metadata.json          # 八字体系元信息
│   ├── tarot/
│   │   ├── factors.jsonl
│   │   └── metadata.json
│   └── registry.json              # 全局因子注册表
│
├── rules/                 # 规则配置源码
│   ├── bazi/
│   │   ├── career.jsonl           # 事业规则（ConfigRuleDefinition）
│   │   ├── wealth.jsonl           # 财富规则
│   │   └── metadata.json
│   ├── tarot/
│   │   └── ...
│   └── registry.json              # 全局规则注册表
│
├── semantics/             # 语义配置源码
│   ├── bazi/
│   │   └── semantic_core.jsonl    # 八字语义核心
│   └── tarot/
│       └── semantic_core.jsonl
│
└── engines/               # 引擎注册表
    └── registry.json              # EngineDescriptor列表
```

#### 编译产物目录（Generated Code）

```
backend/generated/         # Codegen输出目录
├── factors/
│   ├── __init__.py
│   ├── bazi_factors_v1_0_0.py     # 自动生成，含FactorValue生成逻辑
│   └── tarot_factors_v1_0_0.py
│
├── rules/
│   ├── __init__.py
│   ├── bazi_career_v1_0_0.py      # 自动生成规则函数 → RuntimeRuleResult
│   ├── bazi_wealth_v1_0_0.py
│   └── tarot_meaning_v1_0_0.py
│
├── semantics/
│   ├── __init__.py
│   ├── bazi_semantic_v1_0_0.py    # 自动生成语义查询类
│   └── tarot_semantic_v1_0_0.py
│
└── .codegen_manifest.json         # 生成记录（哈希、版本、时间戳）
```

#### 失败处理与回退流程

```python
# Codegen流程
CODEGEN_FLOW = {
    "步骤1_校验": "Pydantic校验Config*模型 → 失败则拒绝",
    "步骤2_编译": "生成Python代码 → 失败则打回精校队列",
    "步骤3_测试": "运行RuleTestCase → 失败则标记experimental",
    "步骤4_部署": "热重载到运行时 → 失败则回滚到上一版本",
    
    "回滚策略": {
        "保留历史": "保留最近3个版本的生成物",
        "版本哈希": "用哈希验证配置源码与生成物一致性",
        "灰度发布": "新版本先标记experimental，观察一周"
    }
}
```

### 10.2 必需文件清单

#### 配置源码（提交到版本控制）
1. **data/factors/registry.json** - 全局因子注册表
2. **data/rules/**/*.jsonl** - 规则定义（ConfigRuleDefinition）
3. **data/engines/registry.json** - EngineDescriptor列表
4. **backend/semantics/**/*.py** - 语义核心定义（Python SemanticEntry类）
5. **validation_report.txt** - 数据验证报告

#### 编译产物（.gitignore，CI/CD自动生成）
1. **backend/generated/**/*.py** - Codegen生成的Python模块
2. **backend/generated/.codegen_manifest.json** - 生成清单
3. **backend/generated/.version_hashes.json** - 版本哈希表

### 10.3 质量要求

- 所有factor_id必须全局唯一
- 所有规则引用的因子必须已定义
- 所有配置必须通过Pydantic验证
- 覆盖率：Content-L2因子100%，Content-L3规则90%+
- 所有Config模型必须标注version/status/engine_id
- 编译产物必须与配置源码哈希对应

---

## 11. TOON v1正式规范

**定位**：LLM边界Token压缩协议，与架构文档《ls_engine_architecture_v3.md §10.4》完全对齐。

### 11.1 顶层数据模型

```python
from pydantic import BaseModel, Field
from typing import Literal

class ToonPayload(BaseModel):
    """TOON协议顶层载体"""
    version: Literal["1"] = "1"
    kind: Literal["rule", "fusion", "memory", "factor_matrix"]
    body: str = Field(..., max_length=1000, description="具体TOON文本")
    
    class Config:
        schema_extra = {
            "examples": [
                {
                    "version": "1",
                    "kind": "rule",
                    "body": "dts_jia_spring_001:C/+/0.8/dm,sn,st"
                },
                {
                    "version": "1",
                    "kind": "fusion",
                    "body": "T:事业突破|财富积累|团队建设\\n"
                           "dts_jia_001:C/+/0.85/dm,sn\\n"
                           "bazi_cai_002:W/++/0.9/cai,shn\\n"
                           "XV:0.87\\nCF:0"
                }
            ]
        }
```

### 11.2 TOON语法规范

```python
TOON_SYNTAX = {
    "rule": {
        "format": "rid:dim/lvl/conf/ev1,ev2,ev3",
        "example": "dts_jia_spring_001:C/+/0.8/dm,sn,st",
        "fields": {
            "rid": "规则ID",
            "dim": "维度缩写(C=事业,H=健康,M=婚姻,W=财富)",
            "lvl": "等级(++=大吉,+=吉,0=中等,-=凶,--=大凶)",
            "conf": "置信度(0.0-1.0)",
            "ev": "证据因子缩写列表(逗号分隔)"
        }
    },
    
    "fusion": {
        "format": "T:theme1|theme2|theme3\\n[rules]\\nXV:score\\n[CF:count]",
        "lines": {
            "T": "主题行(竖线分隔)",
            "rules": "各条规则的TOON简写",
            "XV": "交叉验证分数",
            "CF": "冲突数量(可选)"
        }
    },
    
    "factor_matrix": {
        "format": "fid1:val1,fid2:val2,...",
        "example": "dm:jia,ssn:spring,str:0.75",
        "max_factors": 20
    }
}
```

### 11.3 缩写映射表

```python
ABBREVIATIONS = {
    # 维度缩写
    "事业": "C",  # Career
    "健康": "H",  # Health
    "婚姻": "M",  # Marriage
    "财富": "W",  # Wealth
    
    # 等级缩写
    "大吉": "++",
    "吉": "+",
    "中等": "0",
    "凶": "-",
    "大凶": "--",
    
    # 常用因子缩写(示例)
    "day_master": "dm",
    "season": "ssn",
    "strength": "str",
    "ten_god_zhengguan": "zg",
    "ten_god_cai": "cai"
}
```

### 11.4 约束规则

```python
TOON_CONSTRAINTS = [
    "TOON中不得出现原始PII(姓名、精确地址、身份证号等)",
    "所有枚举值必须来自Factor/Rule的注册表缩写映射",
    "默认一切TOON文本视为'一次性prompt上下文'，不做长期存储",
    "长期存储只能存结构化对象(Pydantic模型)",
    "单个TOON payload不得超过1000字符",
    "TOON只能出现在LLM边界，禁止在Engine Layer1-4传递"
]
```

### 11.5 压缩效果对比

| 格式 | Token数 | 压缩率 | 示例 |
|------|--------|---------|------|
| JSON | ~200 | 0% | `{"rule_id":"dts_jia_spring_001",...}` |
| TOON | ~30 | 85% | `dts_jia_spring_001:C/+/0.8/dm,ssn` |
| Fusion JSON | ~500 | 0% | 完整FusionResult对象 |
| Fusion TOON | ~80 | 84% | `T:事业突破|...\nXV:0.87` |

---

## 12. 实施路线图

### Phase 1: 基础定义（当前）
- [x] 定义Factor Schema
- [x] 定义Rule Schema
- [x] 定义Narrative Schema
- [x] 定义Memory Schema (Event/Insight/Profile)
- [x] 定义Action Schema (ActionBase/ActionSourceRef/ActionProject/ActionItem)
- [ ] 创建验证工具

### Phase 2: 数据迁移
- [ ] 从Markdown提取因子
- [ ] 转换现有规则
- [ ] 生成JSONL文件

### Phase 3: 引擎对接
- [ ] Python规则引擎集成
- [ ] API接口实现
- [ ] 端到端测试

### Phase 4: Action层实现
- [ ] 实现action_models.py (ActionBase/ActionSourceRef/ActionProject/ActionItem)
- [ ] 实现ActionCompilerService
- [ ] 实现FeedbackAnalyzer (Level 2)
- [ ] Action层与Memory层集成测试

---

*本规范是连接内容与代码的桥梁，确保典籍智慧能够被程序准确理解和执行。*

*最后更新：2025-11-30*
