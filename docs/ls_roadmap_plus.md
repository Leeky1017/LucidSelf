# LS Roadmap Plus: 从命理分析引擎到人生版本系统

> **版本**: v1.0  
> **日期**: 2025-12-06  
> **定位**: 综合评估 LS 当前能力与"人生版本系统"目标的差距，并给出分阶段演进路线  
> **适用**: 产品决策、技术架构、投资人沟通

---

## 一、核心结论

**LS 当前是一个成熟的"多体系命理分析引擎"，但还不是设计目标中的"人生 AB 测试系统"。**

| 维度 | 完成度 | 说明 |
|------|--------|------|
| **基础设施层** (因子/规则/记忆) | **70-80%** | 可支撑复杂分析业务 |
| **产品目标层** (版本/预测/学习) | **20-30%** | 核心产品形态尚未动工 |

**粗暴讲**：
- 作为"多体系命盘 + 梦境 + 心理分析后端"，LS 的骨架基本立起来了
- 作为"帮用户管理人生版本、做 AB 测试和长期实验的系统"，只走完了"拆因子"和"做解释"的前半截

---

## 二、层级对照表：逐层定位差距

用目标模型（因子 → 规则 → 场景/时间 → Life Versions/版本树 → 记忆/学习）来对照：

| 层级 | 目标形态 | 当前实现状态 | 与目标的本质差距 |
|------|---------|-------------|-----------------|
| **① 因子层** | 统一的人生特征坐标系，多体系都映射成因子 | 因子本体、类型、分类、因子矩阵都已有，覆盖度极高 | 主要是"太全太细"后的治理问题，不是缺功能 |
| **② 规则层** | "因子组合 → 结构判断/概率"，可溯源、可冲突处理 | RuleEngine 完整，规则结构、冲突解决、溯源链路都有 | 靠近目标；还缺"概率/样本量"等统计维度 |
| **③ 场景/时间层** | 按场景路由因子+规则，并能做时间推演 | 有 life_domain 等标签，但没有真正的"场景路由"和时间推演逻辑 | **这里开始出现结构性缺口** |
| **④ Life Versions / 版本树层** | 把推理+预测压缩成 2–3 个可选人生版本，随时间展开成分叉树 | 完全没有版本对象、版本生成器、版本树模型，只停留在"融合报告" | **这是和"人生 AB 测试系统"概念差距最大的层** |
| **⑤ 记忆/学习层** | 长期记录选择和结果，用来调整因子、规则权重，实现个体和群体层面的自校正 | MemoryService 已能存 Event、Action、Insight，但没有系统化"学习"逻辑，规则权重静态 | 数据入口有了，学习机制缺失 |

---

## 三、分层详细分析

### 3.1 因子层：基础很强，但偏"科研型"

#### 目标
把"人"的状态拆成一张统一的因子表，能被任何引擎读取、比较、计算。

#### 当前实现

| 指标 | 状态 | 数据 |
|------|------|------|
| 因子定义覆盖 | ✅ 完备 | 16万行（bazi 10万, astro 9千, dream 2.3万, tarot 7千, yijing 8千, psych 2千） |
| 类型系统 | ✅ 完备 | `value_type: boolean/numeric/enum/reference/string` |
| 分类体系 | ✅ 完备 | `category: structure/state/relation/temporal/energy/neutral` |
| 统一抽象 | ✅ 完备 | `FactorMatrix` + `FactorValue` |

```python
# 现有因子示例 (factor_schema.yaml)
- id: day_master
  value_type: enum
  value_range: [甲, 乙, 丙, 丁, 戊, 己, 庚, 辛, 壬, 癸]
  applicable_systems: [bazi]

- id: dream_anxiety_level
  value_type: numeric
  value_range: [0, 1]
  applicable_systems: [dream]
```

#### 差异不在"有没有因子"，而在：

**问题1：抽象层次不均衡**
- 一些因子是很底层（干支原始结构）
- 一些已经是半解释（如"焦虑程度"）
- 对于"版本树/预测系统"来说，更需要一套"中层因子"（可直接作为决策维度）的统一定义

**问题2：缺少"因子质量"的元信息**
- 目前有 `value + confidence + source`
- 没有"来源样本量/统计可靠度"等信息
- 后续做版本比较时，很难区分"硬事实因子"和"推导出来的软因子"

#### 本质
> 因子系统已经足够支撑"解释引擎"，但要撑起"版本比较"，还缺一层"决策用因子"的明确切面。

---

### 3.2 规则层：结构完成度高，但还停在"静态推理"

#### 目标
规则是"因子组合 → 结构判断/概率"的形式化载体，可以标注来源、置信度，可以互相冲突、被数据弱化。

#### 当前实现

**规则表达力**：
- ✅ 支持 AND/OR/NOT、11种运算符、多级嵌套
- ✅ 冲突组、优先级、互斥
- ✅ RuleEngine 只看 FactorMatrix，不依赖具体命理系统

**溯源与标签**：
- ✅ `source_book`、`l1_anchor` 典籍溯源
- ✅ 规则结果有 `dimension/level/tags`

```python
# engine.py 核心能力
class RuleEngine:
    - O(1) 规则查找
    - 按 category/engine_id 过滤
    - 错误隔离（单规则失败不影响整体）
    - execution_time_ms 跟踪
    - ConflictResolver 冲突解决
```

#### 缺的东西

| 缺口 | 说明 |
|------|------|
| 真正的"统计型置信度" | 现在的 confidence 更多是"人工赋值"，不是"系统记录该规则在多少样本上被印证/打脸" |
| 多源规则权重分层 | 典籍规则 vs 现代心理学规则 vs 数据挖掘规则，目前没有明显的分层与对抗关系 |

#### 本质
> 从"规则语言"和"工程结构"看，已经具备演化成可学习系统的潜力。但现在实际运行形态更像"静态推理机"而不是"可训练的假说网络"。

---

### 3.3 场景/时间层：抽象存在，真正的"决策逻辑"几乎为空

#### 目标
- 用户问的是"职业/感情/财富/健康/创造力哪一块"
- 系统自动选择与该场景最相关的因子子集和规则集
- 再在时间轴上把这些判断拉成"未来 1–3 年的关键节点"

#### 当前实现

```python
# cross_domain_models.py
class CrossDomainAxes:
    life_domain: List[str]  # ['career', 'health', 'relationship', 'wealth']
    time_horizon: Literal["short_term", "medium_term", "long_term"]
    advice_type: List[str]  # ['action', 'reflection', 'warning', 'opportunity']
```

- ⚠️ `life_domain`、`time_horizon`、`advice_type` 作为**标签维度**存在
- ⚠️ 规则有 `category` 字段，可以按维度过滤

#### 缺少的关键拼图

| 缺口 | 说明 |
|------|------|
| **场景路由器** | 没有组件负责：接收用户问题 → 解析成场景 → 根据场景选因子/选规则。大部分选择还是通过 prompt 或人工配置在外层完成 |
| **场景内的"主视图"** | "职业场景"应该有固定的决策视角（收入上限/稳定度/自主性/社交密度/成长性），目前没有顶层的"场景视角统一器" |
| **时间维** | 因子有 temporal 分类，但没看到成型的"timeline 节点"模型。没有任何"2026 Q1 / 2027 H2 这类时间桶"的预测结构 |

#### 本质
> 现在 LS 比较像"一台很强的跨体系命理/心理分析器"，但缺少把这些分析抓成"围绕某个目标问题的决策画布"的那一层。

---

### 3.4 预测层：时间因子存在，真正的"多路径预测"还没起步

#### 目标
对未来一段时间内的几个关键时间点，给出：
- 如果选路径 A，大致会怎样
- 如果选路径 B，大致会怎样
- 分别的风险、收益、波动区间

#### 当前实现
- ⚠️ 有 `temporal` 因子分类
- ⚠️ 流年/大运等在本体中已经预留位置
- ❌ 预测逻辑、timeline 节点、不同选择路径的对比结构都不存在

#### 几层差距

| 差距类型 | 目标 | 现状 |
|---------|------|------|
| **时间建模** | 时间桶 + 状态估计 | 只有"带时间属性的因子"，没有"时间离散化后的节点模型" |
| **决策路径** | 不同决策策略 → 不同时间线 | 所有推理都是在"给定现状"的单条世界线上的静态判断，没有"分支"的概念 |
| **概率化** | "版本 A：收入大于X的概率约为 0.6" | 规则输出有 confidence，但那不是严格意义上的"某条路径成功/失败概率" |

#### 本质
> LS 已经具备了做"结构分析 + 倾向判断"的能力。但缺少做"动态模拟 + 路径比较"的内核。

---

### 3.5 Life Versions / 版本树层：抽象概念存在，代码是空白

#### 目标
把所有计算过的因子、规则、场景、时间，压缩成 2–3 个清晰的人生版本：
- 每个版本有：命名、操作策略、预期收益/代价、适合人群、主要风险点
- 随着时间推进，每一个关键决策点往下再分出若干子版本，形成"版本树"

#### 当前实现
后端输出形态是 `FusionResult`：
- 多引擎、多规则结果合并成一份"复杂分析结果"
- 面向的对象是"解释/洞察"，不是"可直接拿来当人生方案对比"

#### 完全缺失的结构

| 缺失项 | 说明 |
|--------|------|
| **"版本"这个一级对象** | 没有 `LifeVersion` 结构来承载"一个可选方案"；没有定义"版本的核心度量维度"（钱/稳定/自由/名望/精神满足度） |
| **"版本比较"逻辑** | 没有任何组件在做：从大量推理结果中抽象出若干"互相足够不同"的版本，并做"对比视图" |
| **"版本树"结构** | 没有节点、分支、父子关系这些基础数据结构；记忆层记录的是"事件/行动"，而不是"在版本树中选了哪条枝干" |

#### 本质
> 当前 LS 的主语仍然是"系统在说你怎样"。目标是把主语改成"你在版本之间做选择，系统只是呈现版本和后果"。这中间缺少一整层"决策建模"的数据结构和服务。

---

### 3.6 记忆/学习层：数据有了，学习几乎没有

#### 目标
LS 长期记住：
- 用户的选择（做了/没做/拖延/绕路）
- 用户的真实结果（收入、健康、关系状态变动等）

使用这些信息来：
- 更新个体因子值（例如：抗压能力从假设变成实测）
- 在群体层面调整规则权重（某些典籍断语在现代样本中经常失效，就降权）

#### 当前实现

```python
# MemoryService 已支持
- Event（事件）
- ActionItem（行动项）
- Insight（洞察，包括 AvoidanceInsight）

# ActionItem 字段
- feedback_status: Literal["done", "partial", "skipped", "expired"]
- feedback_note: str
- actual_effort_minutes: int
```

#### 缺损点

| 缺口 | 说明 |
|------|------|
| **从记忆到因子的回流路径** | 结构上支持"更新因子"，但没有系统化的"从 Event/Action → 新因子/因子更新"的 pipeline。例如"连续 12 周执行力高"应沉淀成"执行力因子上调"，目前没有这一层 |
| **从记忆到规则权重的回流** | RuleEngine 没有个性化权重表，也没有全局统计权重表。所有规则的存在感，对所有用户基本是一样的 |
| **版本结果统计** | 因为根本没有版本树，自然也就没有"走了版本 A 的人后续平均怎样"的统计入口 |

#### 本质
> LS 已经具备"记事本"和"行为记录仪"的功能。但离"自校正系统"还隔着两层：一个是"行为 → 因子"，一个是"行为 → 规则权重"。

---

## 四、综合能力矩阵

| 模块 | 状态 | 完成度 | 备注 |
|------|------|--------|------|
| **因子本体** | ✅ 成熟 | 95% | 7体系16万行，类型/分类完备 |
| **因子矩阵** | ✅ 完成 | 95% | FactorMatrix + FactorValue |
| **规则引擎** | ✅ 生产就绪 | 90% | 表达力强，缺统计维度 |
| **溯源链路** | ✅ 完成 | 85% | source_book + l1_anchor |
| **多体系计算器** | ⚠️ 框架完成 | 60% | 6个Calculator框架在，计算逻辑待完善 |
| **场景选择** | ⚠️ 基础存在 | 40% | 标签有，路由器无 |
| **时间推演** | ⚠️ 基础存在 | 30% | 因子槽位有，timeline逻辑无 |
| **预测系统** | ⚠️ 概念存在 | 20% | 无多路径、无概率化 |
| **Life Versions** | ❌ 未实现 | 0% | 核心产品形态空白 |
| **版本树** | ❌ 未实现 | 0% | 无数据结构 |
| **记忆层** | ✅ 完成 | 80% | Event/Action/Insight |
| **学习机制** | ❌ 未实现 | 10% | 有AvoidanceInsight，无系统化学习 |

---

## 五、关键缺口与解决方案

### 缺口 1: Life Versions（人生版本）

**问题**：系统输出"融合分析报告"，不是"可选人生方案"

**方案**：新增 `LifeVersionGenerator` 服务

```python
# 目标数据结构
class LifeVersion(BaseModel):
    """人生版本"""
    version_id: str
    title: str                    # "保守版" / "激进版" / "折中版"
    strategy: List[str]           # 决策建议
    expected_outcomes: Dict[str, float]  # {收入区间, 稳定度, 自由度, 成长性}
    risks: List[str]              # 主要风险
    suitable_for: List[str]       # 适合人群特征
    confidence: float
    source_factors: List[str]     # 支撑因子
    source_rules: List[str]       # 支撑规则

class LifeVersionSet(BaseModel):
    """版本集合（2-3个互斥版本）"""
    user_id: str
    scenario: str                 # 场景（career/relationship/...）
    versions: List[LifeVersion]
    comparison_axes: List[str]    # 对比维度
    generated_at: datetime
```

### 缺口 2: 时间推演引擎

**问题**：有流年/大运因子定义，无时间推演逻辑

**方案**：基于时间因子扩展推理引擎

```python
# 目标数据结构
class TimelineNode(BaseModel):
    """时间节点"""
    time_bucket: str              # "2025-Q3" / "2026-H1"
    event_probability: float
    favorable_actions: List[str]
    risk_factors: List[str]
    confidence: float

class TimelineProjection(BaseModel):
    """时间线投射"""
    scenario: str
    version_id: str
    nodes: List[TimelineNode]
    branch_points: List[str]      # 关键决策点
```

### 缺口 3: 场景自动路由

**问题**：规则有分类，但无自动筛选

**方案**：`ScenarioRouter` 根据用户问题自动选择因子+规则子集

```python
class ScenarioRouter:
    """场景路由器"""
    
    def route(self, user_query: str, factor_matrix: FactorMatrix) -> ScenarioContext:
        """
        1. 解析用户问题 → 识别场景
        2. 根据场景选择因子子集
        3. 根据场景选择规则集
        4. 返回场景上下文
        """
        pass

class ScenarioContext(BaseModel):
    scenario_id: str
    life_domain: str
    active_factors: List[str]
    active_rule_categories: List[str]
    decision_axes: List[str]      # 该场景的决策维度
```

### 缺口 4: 个性化权重学习

**问题**：规则权重静态

**方案**：基于反馈数据动态调整权重

```python
class RuleWeightAdjuster:
    """规则权重调整器"""
    
    async def learn_from_feedback(
        self,
        user_id: str,
        rule_id: str,
        prediction: str,
        actual_outcome: str,
        confidence_delta: float
    ) -> None:
        """
        1. 记录规则预测 vs 实际结果
        2. 更新用户个性化权重表
        3. 累积到群体统计权重
        """
        pass

class PersonalizedWeights(BaseModel):
    """用户个性化权重"""
    user_id: str
    rule_weights: Dict[str, float]  # rule_id -> weight_multiplier
    last_updated: datetime
    sample_count: int
```

---

## 六、演进路线图

### Phase 1: 场景化重构（2-3周）
**目标**：让系统输出从"报告"变成"围绕某场景的决策画布"

| 任务 | 产出 |
|------|------|
| 定义 ScenarioRouter | 场景路由器，自动选因子+规则 |
| 定义决策维度表 | 每个场景的标准对比轴 |
| 重构 FusionResult | 增加 scenario_context 字段 |

### Phase 2: 时间线建模（2-3周）
**目标**：让系统能输出"未来N年的关键节点"

| 任务 | 产出 |
|------|------|
| 定义 TimelineNode / TimelineProjection | 时间节点数据结构 |
| 实现 temporal 因子推演逻辑 | 流年大运 → 时间桶 |
| 集成到场景输出 | 场景+时间线组合视图 |

### Phase 3: Life Versions 核心（3-4周）
**目标**：让系统输出 2-3 个可选人生版本

| 任务 | 产出 |
|------|------|
| 定义 LifeVersion / LifeVersionSet | 版本数据结构 |
| 实现 LifeVersionGenerator | 从推理结果生成版本 |
| 实现版本对比视图 | 前端多版本对比 |

### Phase 4: 版本树与决策追踪（3-4周）
**目标**：让系统记录用户在版本树中的选择轨迹

| 任务 | 产出 |
|------|------|
| 定义 VersionTree / TreeNode | 版本树数据结构 |
| 实现决策点追踪 | 记录用户选择 |
| 实现版本分叉逻辑 | 根据选择生成子版本 |

### Phase 5: 学习闭环（4-6周）
**目标**：让系统根据反馈自校正

| 任务 | 产出 |
|------|------|
| 实现 Feedback → Factor 回流 | 行为沉淀为因子 |
| 实现 Feedback → Rule Weight | 个性化+群体权重 |
| 实现版本结果统计 | "走版本A的人平均怎样" |

---

## 七、技术架构对齐

### 现有五层架构 vs 新增能力

```
┌─────────────────────────────────────────────────────────────┐
│  Layer 5: Application (已有)                                │
│  ├── NarrativeGenerator ✅                                  │
│  └── 【新增】LifeVersionPresenter                           │
├─────────────────────────────────────────────────────────────┤
│  Layer 4: Fusion (已有)                                     │
│  ├── FusionEngine ✅                                        │
│  ├── 【新增】LifeVersionGenerator                           │
│  ├── 【新增】TimelineProjector                              │
│  └── 【新增】ScenarioRouter                                 │
├─────────────────────────────────────────────────────────────┤
│  Layer 3: Rule (已有)                                       │
│  ├── RuleEngine ✅                                          │
│  ├── ConflictResolver ✅                                    │
│  └── 【新增】RuleWeightAdjuster                             │
├─────────────────────────────────────────────────────────────┤
│  Layer 2: Semantic (已有)                                   │
│  └── SemanticEngine ✅                                      │
├─────────────────────────────────────────────────────────────┤
│  Layer 1: Calculator (已有)                                 │
│  ├── BaziCalculator ✅                                      │
│  ├── ZiweiCalculator ✅                                     │
│  ├── AstroCalculator ✅                                     │
│  └── ... ✅                                                 │
└─────────────────────────────────────────────────────────────┘
                              ↕
┌─────────────────────────────────────────────────────────────┐
│  Memory Layer (已有)                                        │
│  ├── MemoryService ✅                                       │
│  ├── Event / Insight / UserProfile ✅                       │
│  ├── ActionProject / ActionItem ✅                          │
│  ├── 【新增】VersionTree                                    │
│  └── 【新增】LearningPipeline                               │
└─────────────────────────────────────────────────────────────┘
```

### 数据契约扩展

在 `backend/core/contracts/` 新增：

| 文件 | 内容 |
|------|------|
| `life_version_models.py` | LifeVersion, LifeVersionSet, VersionComparison |
| `timeline_models.py` | TimelineNode, TimelineProjection, BranchPoint |
| `scenario_models.py` | ScenarioContext, ScenarioView, DecisionAxis |
| `learning_models.py` | PersonalizedWeights, RuleFeedback, FactorUpdate |

---

## 八、从投资人口径看

**第1步（拆因子）和第2步（规则推理）已扎实** ✅
- 16万行因子定义，7体系覆盖
- RuleEngine 生产就绪，溯源链路完整

**第3步（Life Versions）是核心产品形态，尚未开始** ❌
- 这是从"工具"变成"产品"的关键一跃
- 没有这一层，LS 只能是"很强的分析后端"

**用户故事对比**：

| 当前能力 | 目标能力 |
|---------|---------|
| "系统分析你是这样的人" | "系统给你3条路，你选" |
| "你的八字显示..." | "如果走保守版，收入稳定但..." |
| 单次输出，无追踪 | 选择后继续跟踪，持续校准 |

---

## 九、总结

**LS 的定位需要明确**：

| 定位 | 当前完成度 | 差距 |
|------|-----------|------|
| 多体系命理分析后端 | 80% | 计算器逻辑待完善 |
| 人生版本系统 | 25% | 版本/预测/学习缺失 |
| 人生 AB 测试平台 | 10% | 需要完整的版本树+学习闭环 |

**核心差距**：
- **基础层**（因子/规则/记忆）已经是"科研级命理后端"
- **产品层**（版本/预测/学习）离"人生版本系统"还很远
- 关键缺失：`LifeVersion` 作为一级对象，以及围绕它的生成、比较、追踪、学习机制

**下一步**：
1. 先做 ScenarioRouter（场景路由）—— 让输出变成"决策画布"
2. 再做 TimelineProjector（时间线）—— 让输出有"未来感"
3. 最后做 LifeVersionGenerator —— 让输出变成"可选方案"

这三步完成后，LS 才真正从"分析引擎"变成"人生版本系统"。
