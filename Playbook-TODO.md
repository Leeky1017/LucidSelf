# Action Compiler Layer 规划草案 v2.0

> 总目标：在不削减任何功能的前提下，重整 Action Compiler / To-Do 模块的概念边界和依赖关系，避免后期 Memory 层演化时整块返工。

---

## 一、概念分层与模型边界

### 1.1 三类对象的显式区分

| 类别 | 语义 | 示例 | 存储位置 |
|------|------|------|----------|
| **Memory.*** | 已发生的事实 | 完成/未完成的行为、梦境事件、对话、健康波动 | `memory_models.py` |
| **Insight / Playbook.*** | 解释、策略、倾向 | 命盘结论、Dream/Playbook 的"今天/本周重点"、长期主题 | `insight_models.py` |
| **Action.*** | 未来的计划行为 | ActionProject / ActionItem / 计划中的任务步骤 | `action_models.py` |

### 1.2 Action 层的独立 Base

Action 系列不再继承完整的 `MemoryBase`，而是使用更薄的 `ActionBase`：

```python
class ActionBase(BaseModel):
    """Action 层的轻量基类，与 Memory 层解耦"""
    id: str = Field(..., description="实体ID")
    user_id: str = Field(..., description="用户ID")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
```

### 1.3 关联关系（而非继承）

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         概念边界与关联关系                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Insight / Playbook 层                     Memory 层                    │
│  ┌──────────────────────┐                 ┌──────────────────────┐     │
│  │ PlaybookSuggestion   │                 │ Memory.Event         │     │
│  │ DreamInsight         │                 │ Memory.Insight       │     │
│  │ AstroConclusion      │                 │ Memory.Profile       │     │
│  └──────────┬───────────┘                 └──────────▲───────────┘     │
│             │                                        │                  │
│             │ source_ref                             │ 派生写入          │
│             ▼                                        │                  │
│  ┌──────────────────────────────────────────────────┐│                  │
│  │                   Action 层                       ││                  │
│  │  ┌────────────────┐    ┌─────────────────────┐   ││                  │
│  │  │ ActionProject  │───▶│ ActionItem          │   ││                  │
│  │  │                │    │  - source_ref ──────┼───┼┘                  │
│  │  │                │    │  - feedback (inline)│   │                   │
│  │  └────────────────┘    └──────────┬──────────┘   │                   │
│  │                                   │              │                   │
│  │                                   │ 状态变更时    │                   │
│  │                                   ▼              │                   │
│  │                        ┌─────────────────────┐   │                   │
│  │                        │ → Memory.Event      │───┘                   │
│  │                        │ → Insight 更新      │                       │
│  │                        └─────────────────────┘                       │
│  └──────────────────────────────────────────────────────────────────────┘
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 二、计划行为与实际行为的映射

### 2.1 语义约定

| 概念 | 定义 | 生命周期 |
|------|------|----------|
| **ActionItem** | 计划行为（尚未发生的 event 配置） | 创建 → 执行中 → 终态 |
| **ActionItem.feedback** | 该 Action 实际执行结果的内联摘要 | 状态变更时写入 |
| **Memory.Event** | 真实发生过的事（由 Action 完成/失败派生，或其他输入渠道） | 永久存储 |
| **Memory.Insight/Profile** | 消费 Event 后更新用户画像与长期倾向 | 增量更新 |

### 2.2 状态流转图

```
                    ┌───────────────────────────────────────────────────────┐
                    │              ActionItem 状态机                         │
                    ├───────────────────────────────────────────────────────┤
                    │                                                       │
Insight ─────────▶  │   ┌──────┐                                           │
(source_ref)        │   │ TODO │                                           │
                    │   └──┬───┘                                           │
                    │      │ 用户开始                                       │
                    │      ▼                                               │
                    │   ┌───────┐                                          │
                    │   │ DOING │                                          │
                    │   └───┬───┘                                          │
                    │       │                                              │
                    │       ├──────────────┬──────────────┬───────────────┤
                    │       │              │              │               │
                    │       ▼              ▼              ▼               │
                    │   ┌──────┐      ┌─────────┐    ┌─────────┐         │
                    │   │ DONE │      │ SKIPPED │    │ EXPIRED │         │
                    │   └──┬───┘      └────┬────┘    └────┬────┘         │
                    │      │               │              │               │
                    └──────┼───────────────┼──────────────┼───────────────┘
                           │               │              │
                           ▼               ▼              ▼
                    ┌──────────────────────────────────────────────────────┐
                    │                 状态变更触发器                         │
                    │                                                      │
                    │  1. 写入 ActionItem.feedback (内联)                   │
                    │     - completion_status: done | partial | skipped    │
                    │     - note: 可选备注                                  │
                    │     - actual_effort_minutes: 实际耗时                 │
                    │                                                      │
                    │  2. 派生 Memory.Event                                 │
                    │     - event_type: action_completed | action_skipped  │
                    │     - source_action_id: item_id                      │
                    │     - outcome: 结果摘要                               │
                    │                                                      │
                    │  3. 触发 Insight/Profile 更新（异步）                  │
                    │     - 完成率统计                                      │
                    │     - 耗时校准                                        │
                    │     - 回避模式识别                                    │
                    └──────────────────────────────────────────────────────┘
```

### 2.3 硬性规则

| 规则ID | 规则内容 |
|--------|----------|
| MAP-01 | ActionItem 状态从 TODO/DOING → DONE/SKIPPED/EXPIRED 时，**必须**写入 `feedback` 字段 |
| MAP-02 | 状态变更时，**必须**生成或更新一个 `Memory.Event` |
| MAP-03 | 连续 N 次（默认3次）回避同类 Action 时，**必须**生成"回避型 Insight" |
| MAP-04 | EXPIRED 状态的 Action 也要写入 Event（标记为 `action_expired`） |

---

## 三、编译策略：单条细化 vs Daily/Weekly Compile

### 3.1 两级策略设计

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          编译策略两级分层                                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Level A: 单条 Insight 编译策略                                          │
│  ────────────────────────────────                                       │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  长期 Insight（如"大运沟通运强"）                                  │   │
│  │                                                                   │   │
│  │  • 生成策略: 仅生成有限数量的 ActionProject 模板（最多1个）         │   │
│  │  • 编译次数: 首次生成后，Daily/Weekly 只从模板抽样                  │   │
│  │  • 状态流转: NEW → TEMPLATE_CREATED → (多次抽样) → ARCHIVED       │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  短期 Insight（如"今天适合推进某项目"）                            │   │
│  │                                                                   │   │
│  │  • 生成策略: 最多触发一次 Action 编译                              │   │
│  │  • 编译次数: 严格1次，不重复                                       │   │
│  │  • 状态流转: NEW → COMPILED → (执行完成/过期) → ARCHIVED          │   │
│  │  • 过期处理: 到期后归档，不在下一轮编译中被无脑重生                  │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  Level B: Daily/Weekly Compile 策略                                      │
│  ────────────────────────────────                                       │
│                                                                         │
│  输入集合构成（显式定义，禁止隐式复用）:                                   │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  1. 最近 N 日的新 Insight（compile_status = NEW）                  │   │
│  │  2. 仍处于 active 状态的长期模板（template_status = ACTIVE）        │   │
│  │  3. 用户显式设定的当前 focus 领域                                  │   │
│  │                                                                   │   │
│  │  排除条件:                                                        │   │
│  │  • compile_status = COMPILED 且未过期的短期 Insight               │   │
│  │  • 已归档的 Insight                                               │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Insight 编译状态机

```python
class InsightCompileStatus(str, Enum):
    """Insight 的编译状态"""
    NEW = "new"                     # 新生成，未编译
    COMPILED = "compiled"           # 已编译为 Action（短期）
    TEMPLATE_CREATED = "template"   # 已创建模板（长期）
    ARCHIVED = "archived"           # 已归档，不再参与编译
```

### 3.3 防重复编译规则

| 规则ID | 规则内容 | 检查时机 |
|--------|----------|----------|
| CMP-01 | 每条短期 Insight 只能生成一批 ActionItem | 编译前检查 `compile_status` |
| CMP-02 | 长期 Insight 的模板每日最多抽样 N 个 Item（默认2） | Daily Compile 时 |
| CMP-03 | 已有 active ActionItem 指向的 Insight 不再重新编译 | 编译前检查关联 |
| CMP-04 | Insight 被编译后，`compiled_at` 和 `compile_session_id` 必须写入 | 编译后更新 |

### 3.4 查询接口

```python
def is_insight_compiled(insight_id: str) -> bool:
    """检查某条 Insight 是否已被编译为 Action"""
    ...

def get_pending_insights_for_compile(
    user_id: str, 
    max_age_days: int = 7,
    focus_areas: list[str] = None
) -> list[Insight]:
    """获取待编译的 Insight 列表（按显式规则过滤）"""
    ...
```

---

## 四、过期策略与回避模式识别

### 4.1 过期处理的双重逻辑

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    过期处理 = 清理 + 分析                                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  当 ActionItem 超过 7 天未处理时:                                         │
│                                                                         │
│  ┌───────────────────────────────────────────────────────────────────┐ │
│  │  A. 状态层面（UI 清理）                                             │ │
│  │                                                                   │ │
│  │  1. status → EXPIRED                                              │ │
│  │  2. 从 Today / ThisWeek 视图中移除                                 │ │
│  │  3. 移入"已过期"折叠区（可查看，不干扰主视图）                        │ │
│  └───────────────────────────────────────────────────────────────────┘ │
│                                                                         │
│  ┌───────────────────────────────────────────────────────────────────┐ │
│  │  B. 分析层面（回避识别）                                            │ │
│  │                                                                   │ │
│  │  1. 写入 ActionItem.feedback:                                     │ │
│  │     - completion_status: "expired"                                │ │
│  │     - auto_expired: true                                          │ │
│  │     - expired_at: timestamp                                       │ │
│  │                                                                   │ │
│  │  2. 派生 Memory.Event:                                            │ │
│  │     - event_type: "action_expired"                                │ │
│  │     - context/effort/source 信息保留                              │ │
│  │                                                                   │ │
│  │  3. 追加到"回避分析队列":                                          │ │
│  │     - avoidance_queue.append({                                    │ │
│  │         item_id, context, effort, source_kind, expired_at         │ │
│  │       })                                                          │ │
│  └───────────────────────────────────────────────────────────────────┘ │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 4.2 回避模式识别

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      FeedbackAnalyzer 回避识别                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  输入: avoidance_queue + 历史 ActionFeedback                             │
│                                                                         │
│  识别模式:                                                               │
│  ┌───────────────────────────────────────────────────────────────────┐ │
│  │  1. 场景回避                                                       │ │
│  │     检测: 连续 N 周，context=desk 的完成率 < 30%                    │ │
│  │     输出: Insight(type="avoidance_pattern",                        │ │
│  │            pattern="desk_avoidance",                               │ │
│  │            confidence=0.8)                                         │ │
│  └───────────────────────────────────────────────────────────────────┘ │
│                                                                         │
│  ┌───────────────────────────────────────────────────────────────────┐ │
│  │  2. 领域回避                                                       │ │
│  │     检测: health/relationship 相关 Action 完成率长期 < 40%          │ │
│  │     输出: Insight(type="avoidance_pattern",                        │ │
│  │            pattern="health_relationship_avoidance",                │ │
│  │            affected_areas=["health", "relationship"])              │ │
│  └───────────────────────────────────────────────────────────────────┘ │
│                                                                         │
│  ┌───────────────────────────────────────────────────────────────────┐ │
│  │  3. 来源回避                                                       │ │
│  │     检测: 来自命盘/健康建议的 Action 完成率显著低于 Playbook          │ │
│  │     输出: Insight(type="avoidance_pattern",                        │ │
│  │            pattern="source_bias",                                  │ │
│  │            low_completion_sources=["astro", "health"])             │ │
│  └───────────────────────────────────────────────────────────────────┘ │
│                                                                         │
│  ┌───────────────────────────────────────────────────────────────────┐ │
│  │  4. 努力回避                                                       │ │
│  │     检测: 总是完成 quick/phone，但从不触碰 medium/long 任务          │ │
│  │     输出: Insight(type="avoidance_pattern",                        │ │
│  │            pattern="effort_avoidance",                             │ │
│  │            avoided_efforts=["60min", "90min+"])                    │ │
│  └───────────────────────────────────────────────────────────────────┘ │
│                                                                         │
│  输出写入:                                                               │
│  • Memory.Insight（可被 Playbook 读取）                                  │
│  • UserProfile.behavior_patterns（长期画像）                             │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 4.3 回避 Insight 结构

```python
class AvoidanceInsight(BaseModel):
    """回避型 Insight，供 Playbook 读取"""
    insight_id: str
    user_id: str
    insight_type: Literal["avoidance_pattern"] = "avoidance_pattern"
    
    # 回避模式
    pattern: str  # desk_avoidance | health_avoidance | effort_avoidance | source_bias
    confidence: float  # 0.0 - 1.0
    
    # 详细信息
    affected_contexts: list[str] = []
    affected_areas: list[str] = []
    affected_efforts: list[str] = []
    low_completion_sources: list[str] = []
    
    # 统计依据
    sample_period_weeks: int
    sample_count: int
    completion_rate: float
    
    # 时间戳
    detected_at: datetime
    
    # 可被 Playbook 消费
    playbook_consumable: bool = True
```

---

## 五、LLM 调用链与监控抽象

### 5.1 调用架构：ActionCompiler 只消费 llm-core 接口

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      LLM 调用架构                                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                     ActionCompilerService                        │   │
│  │                                                                   │   │
│  │  • 不直接拼 prompt 字符串                                         │   │
│  │  • 不维护 token/cost 统计                                         │   │
│  │  • 不做输出清洗/修正                                              │   │
│  │                                                                   │   │
│  │  唯一职责: 准备输入结构 + 消费输出结构                              │   │
│  └──────────────────────────┬──────────────────────────────────────┘   │
│                             │                                           │
│                             │ 调用注册的结构化接口                        │
│                             ▼                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                        llm-core                                   │   │
│  │                                                                   │   │
│  │  ┌────────────────────────────────────────────────────────────┐  │   │
│  │  │  StructuredCallRegistry                                     │  │   │
│  │  │                                                             │  │   │
│  │  │  action_compile_call = register_call(                       │  │   │
│  │  │      name="action_compile",                                 │  │   │
│  │  │      input_schema=ActionCompileInput,                       │  │   │
│  │  │      output_schema=ActionCompileOutput,                     │  │   │
│  │  │      model="gpt-4o-mini",                                   │  │   │
│  │  │      temperature=0.3,                                       │  │   │
│  │  │      max_tokens=1500,                                       │  │   │
│  │  │      response_format={"type": "json_object"}                │  │   │
│  │  │  )                                                          │  │   │
│  │  └────────────────────────────────────────────────────────────┘  │   │
│  │                                                                   │   │
│  │  ┌────────────────────────────────────────────────────────────┐  │   │
│  │  │  Telemetry / Observability                                  │  │   │
│  │  │                                                             │  │   │
│  │  │  • tokens_input / tokens_output                             │  │   │
│  │  │  • latency_ms                                               │  │   │
│  │  │  • cost_cents                                               │  │   │
│  │  │  • call_id (可与业务 session 关联)                           │  │   │
│  │  │  • model_used                                               │  │   │
│  │  └────────────────────────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 5.2 结构化输入/输出 Schema

```python
# 在 llm-core 中定义，ActionCompiler 消费

class ActionCompileInput(BaseModel):
    """Action 编译的结构化输入"""
    insights: list[InsightSummary]  # 待编译的 Insight 摘要
    user_goals: list[str]           # 用户当前目标
    user_constraints: dict          # 约束条件
    time_scope: str                 # today | this_week
    max_projects: int = 3
    max_items_per_project: int = 5

class ActionCompileOutput(BaseModel):
    """Action 编译的结构化输出（由 llm-core 验证）"""
    projects: list[ProjectOutput]
    items: list[ItemOutput]

class ProjectOutput(BaseModel):
    title: str = Field(..., max_length=50)
    time_scope: str
    source_summary: str

class ItemOutput(BaseModel):
    project_index: int
    title: str = Field(..., max_length=60)
    reason: str = Field(..., max_length=100)
    effort_estimate: Literal["15min", "30min", "60min", "90min+"]
    context: Literal["desk", "phone", "outdoor", "talk", "rest"]
    priority: int = Field(..., ge=1, le=10)
```

### 5.3 禁止事项

| 禁止ID | 禁止内容 | 原因 |
|--------|----------|------|
| LLM-01 | ActionCompiler 内部不得出现 prompt 模板字符串 | 由 llm-core 统一管理 |
| LLM-02 | ActionCompiler 内部不得维护 CompileSession 表 | 由 telemetry 统一记录 |
| LLM-03 | ActionCompiler 内部不得出现"清洗非 JSON 输出"逻辑 | 由 llm-core 的 response_format 保证 |
| LLM-04 | ActionCompiler 不得直接选择模型/温度 | 通过注册的 call 配置统一管理 |

### 5.4 调用记录关联

```python
# 如需从 Action 视角查看调用记录，通过 session_id 关联
class ActionCompileResult:
    """编译结果，包含 llm-core 的 call_id"""
    projects: list[ActionProject]
    items: list[ActionItem]
    llm_call_id: str  # 关联 llm-core 的 telemetry 日志
```

---

## 六、能力分层实现

### 6.1 Level 1: 行为落地内核（先实现）

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        Level 1: 行为落地内核                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  完整保留的功能:                                                          │
│  ────────────────                                                       │
│  ✓ 多源输入聚合（Playbook / Dream / 命盘 / 手动）                         │
│  ✓ 日/周编译调用（通过 llm-core）                                        │
│  ✓ ActionProject / ActionItem 完整结构                                  │
│  ✓ 状态机（TODO / DOING / DONE / SKIPPED / EXPIRED）                    │
│  ✓ 用户反馈（状态 + 可选 note）                                          │
│  ✓ 来源追溯（source_ref 指向 Insight）                                   │
│                                                                         │
│  简化实现（不删概念，只减依赖）:                                           │
│  ────────────────────────────                                           │
│  • ActionFeedback 以内联字段形式存在于 ActionItem:                        │
│    ```python                                                            │
│    class ActionItem(ActionBase):                                        │
│        # ... 其他字段 ...                                                │
│        # 内联反馈（Level 1）                                             │
│        feedback_status: Optional[str] = None                            │
│        feedback_note: Optional[str] = None                              │
│        feedback_at: Optional[datetime] = None                           │
│    ```                                                                  │
│                                                                         │
│  • CompileSession 不建独立表，由 llm-core telemetry 负责                  │
│                                                                         │
│  • 回避分析在 Level 1 仅做简单计数:                                       │
│    - 记录每个 context/effort/source 的完成/过期次数                       │
│    - 不做复杂模式识别                                                    │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 6.2 Level 2: 行为分析与画像回写（随后实现）

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      Level 2: 行为分析与画像回写                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  依赖 Level 1 已稳定的:                                                  │
│  ─────────────────────                                                  │
│  • Schema 边界（Memory / Insight / Action 三类分离）                     │
│  • ActionItem 状态机                                                    │
│  • LLM 调用接口（通过 llm-core）                                         │
│                                                                         │
│  新增能力:                                                               │
│  ─────────                                                              │
│  ┌───────────────────────────────────────────────────────────────────┐ │
│  │  1. 独立 ActionFeedback 表                                         │ │
│  │     - 细粒度反馈数据                                                │ │
│  │     - actual_effort_minutes 精确记录                               │ │
│  │     - blocking_reason 分类                                         │ │
│  └───────────────────────────────────────────────────────────────────┘ │
│                                                                         │
│  ┌───────────────────────────────────────────────────────────────────┐ │
│  │  2. FeedbackAnalyzer 服务                                          │ │
│  │     - 完成率/耗时统计                                               │ │
│  │     - 回避模式识别（4 种模式）                                       │ │
│  │     - 行为趋势分析                                                  │ │
│  └───────────────────────────────────────────────────────────────────┘ │
│                                                                         │
│  ┌───────────────────────────────────────────────────────────────────┐ │
│  │  3. Memory 回写                                                    │ │
│  │     - AvoidanceInsight 写入 Memory.Insight                         │ │
│  │     - 行为模式写入 UserProfile.behavior_patterns                    │ │
│  │     - Playbook 可消费这些 Insight                                   │ │
│  └───────────────────────────────────────────────────────────────────┘ │
│                                                                         │
│  ┌───────────────────────────────────────────────────────────────────┐ │
│  │  4. 精细化成本分析                                                  │ │
│  │     - 按用户/时间段/功能模块的成本统计                               │ │
│  │     - 成本预警                                                     │ │
│  └───────────────────────────────────────────────────────────────────┘ │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 6.3 实现依赖图

```
                    Phase 5 (已规划)
                    ┌─────────────────────────────────────┐
                    │ 5-1: llm-core ✅                    │
                    │ 5-4: memory-service                 │
                    │ 5-8: playbook-gen                   │
                    └──────────────┬──────────────────────┘
                                   │
                                   │ 依赖
                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Phase 5.5: Action Compiler Layer                                        │
│  ═══════════════════════════════════════════════════════════════════════│
│                                                                         │
│  Level 1 (先实现)                                                        │
│  ┌───────────────────────────────────────────────────────────────────┐ │
│  │  5.5-1: action-contracts        (0.5 周)                          │ │
│  │         ActionBase / ActionProject / ActionItem                   │ │
│  │         ActionSourceRef / 枚举定义                                 │ │
│  │         依赖: 5-4(memory-service 的 Insight 定义)                  │ │
│  └───────────────────────────────────────────────────────────────────┘ │
│                         │                                               │
│                         ▼                                               │
│  ┌───────────────────────────────────────────────────────────────────┐ │
│  │  5.5-2: action-compiler-core    (1 周)                            │ │
│  │         ContextAggregator / ActionCompilerService                 │ │
│  │         Daily/Weekly Compile 逻辑                                 │ │
│  │         依赖: 5.5-1, 5-1(llm-core), 5-8(playbook)                 │ │
│  └───────────────────────────────────────────────────────────────────┘ │
│                                                                         │
│  ─────────────────── Level 1 完成线 ───────────────────────────────── │
│                                                                         │
│  Level 2 (随后实现)                                                      │
│  ┌───────────────────────────────────────────────────────────────────┐ │
│  │  5.5-3: action-feedback-analyzer (0.5 周)                         │ │
│  │         独立 ActionFeedback 表                                    │ │
│  │         FeedbackAnalyzer / 回避模式识别                           │ │
│  │         Memory.Insight 回写                                       │ │
│  │         依赖: 5.5-2, 5-4                                          │ │
│  └───────────────────────────────────────────────────────────────────┘ │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 七、数据模型定义

### 7.1 ActionBase（轻量基类）

```python
class ActionBase(BaseModel):
    """
    Action 层的轻量基类
    
    设计原则：与 MemoryBase 解耦，避免 Memory 层变化影响 Action 层
    """
    id: str = Field(..., description="实体ID")
    user_id: str = Field(..., description="用户ID")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
```

### 7.2 ActionSourceRef（来源引用）

```python
class ActionSourceRef(BaseModel):
    """
    行动来源引用
    
    通过引用而非继承建立与 Insight/Playbook 的关系
    """
    kind: ActionSourceKind = Field(..., description="来源类型")
    source_id: str = Field(..., description="来源记录ID")
    source_summary: str = Field(..., max_length=100, description="来源摘要")
    
    # 可选的细粒度追溯
    factor_ids: list[str] = Field(default_factory=list)
    rule_ids: list[str] = Field(default_factory=list)


class ActionSourceKind(str, Enum):
    """行动来源类型"""
    PLAYBOOK = "playbook"
    DREAM = "dream"
    ASTRO = "astro"
    HEALTH = "health"
    MANUAL = "manual"
    INSIGHT = "insight"
```

### 7.3 ActionProject

```python
class ActionProject(ActionBase):
    """
    行动项目
    
    一个 Project 代表一个目标领域，如"LS引擎开发"、"身体恢复"
    """
    project_id: str = Field(..., pattern=ACTION_PROJECT_ID_PATTERN)
    
    # 基本信息
    title: str = Field(..., max_length=50)
    time_scope: ActionTimeScope
    
    # 来源（可多源聚合）
    sources: list[ActionSourceRef] = Field(default_factory=list)
    
    # 状态
    status: Literal["active", "completed", "archived"] = "active"
    
    # 生成元信息
    llm_generated: bool = True
    llm_call_id: Optional[str] = None  # 关联 llm-core 的调用记录
```

### 7.4 ActionItem（Level 1 版本，内联反馈）

```python
class ActionItem(ActionBase):
    """
    行动条目（Level 1 版本）
    
    包含内联的反馈字段，避免早期引入独立 Feedback 表
    """
    item_id: str = Field(..., pattern=ACTION_ITEM_ID_PATTERN)
    project_id: str
    
    # 核心内容
    title: str = Field(..., max_length=60, description="行为动词开头")
    description: Optional[str] = Field(None, max_length=200)
    reason: str = Field(..., max_length=100, description="追溯来源")
    
    # 执行约束
    effort_estimate: EffortEstimate
    context: ActionContext
    suggested_time_scope: ActionTimeScope = ActionTimeScope.TODAY
    
    # 来源追溯
    source: ActionSourceRef
    
    # 状态
    status: ActionStatus = ActionStatus.TODO
    priority: int = Field(default=5, ge=1, le=10)
    
    # 生成元信息
    llm_generated: bool = True
    
    # 时间戳
    completed_at: Optional[datetime] = None
    expired_at: Optional[datetime] = None
    
    # ========== 内联反馈（Level 1）==========
    feedback_status: Optional[Literal["done", "partial", "skipped", "expired"]] = None
    feedback_note: Optional[str] = Field(None, max_length=200)
    feedback_at: Optional[datetime] = None
    actual_effort_minutes: Optional[int] = None
```

### 7.5 枚举定义

```python
class ActionTimeScope(str, Enum):
    TODAY = "today"
    THIS_WEEK = "this_week"
    THIS_MONTH = "this_month"

class ActionContext(str, Enum):
    DESK = "desk"
    PHONE = "phone"
    OUTDOOR = "outdoor"
    TALK = "talk"
    REST = "rest"

class ActionStatus(str, Enum):
    TODO = "todo"
    DOING = "doing"
    DONE = "done"
    SKIPPED = "skipped"
    EXPIRED = "expired"

class EffortEstimate(str, Enum):
    QUICK = "15min"
    SHORT = "30min"
    MEDIUM = "60min"
    LONG = "90min+"
```

---

## 八、架构约束

| 约束ID | 约束内容 | 原因 |
|--------|----------|------|
| AC-01 | Action 系列不继承 MemoryBase | 避免 Memory 层变化导致 Action 层大改 |
| AC-02 | 每天默认展示的待办不超过 5 条 | 防止认知过载 |
| AC-03 | ActionItem.title 不超过 60 字符 | 一眼可读 |
| AC-04 | 反馈只需状态，文字备注完全可选 | 降低反馈门槛 |
| AC-05 | 超过 7 天未处理的 Action 自动 EXPIRED | 强制回收 |
| AC-06 | LLM 编译每日最多 1 次，手动触发不限 | 成本控制 |
| AC-07 | 每条短期 Insight 最多生成一批 ActionItem | 防止重复编译 |
| AC-08 | ActionCompiler 不维护独立的 token/cost 统计 | 由 llm-core 统一管理 |
| AC-09 | 状态变更时必须写入 feedback + 派生 Event | 保证可追溯 |
| AC-10 | 回避 Insight 必须可被 Playbook 消费 | 闭环学习 |

---

## 九、可验证的验收点

| 验收点 | 验证方式 |
|--------|----------|
| **V-01**: Action 系列不依赖完整 MemoryBase | 单元测试：修改 MemoryBase 字段，Action 层编译不受影响 |
| **V-02**: Insight 是否已编译可查询/追踪 | 接口测试：`is_insight_compiled(insight_id)` 返回正确结果 |
| **V-03**: ActionItem 全生命周期可追溯 | 集成测试：给定 item_id，能查到 source Insight → Action → Event → Profile 更新链 |
| **V-04**: LLM 调用 schema 由 llm-core 统一定义 | 代码审查：ActionCompiler 内无 prompt 模板字符串、无输出清洗逻辑 |
| **V-05**: 连续回避能生成 Insight | 集成测试：模拟 3 周连续 EXPIRED，验证 AvoidanceInsight 生成 |

---

## 十、实施路径

| 阶段 | 任务 | 预估 | 前置 | 产出 |
|------|------|------|------|------|
| **阶段 1** | action-contracts 实现 | 0.5 周 | 5-4 | `action_models.py` |
| **阶段 2** | action-compiler-core 实现 | 1 周 | 阶段 1, 5-1, 5-8 | `ActionCompilerService` |
| **阶段 3** | Level 1 集成测试 | 0.5 周 | 阶段 2 | 测试覆盖 |
| **阶段 4** | action-feedback-analyzer 实现 | 0.5 周 | 阶段 3 | Level 2 能力 |
| **阶段 5** | 端到端验收 | 0.5 周 | 阶段 4 | 5 个验收点通过 |

**总计: 约 3 周**

---

## 十一、Roadmap 更新

在 `ls_v1_implementation_roadmap.md` 中插入 Phase 5.5:

```markdown
## Phase 5.5: Action Compiler Layer (3 changes)

### 5.5-1: add-action-contracts
- **优先级**: P1 | **预估**: 0.5 周 | **依赖**: 5-4
- **路径**: `backend/core/contracts/action_models.py`
- **内容**: ActionBase, ActionProject, ActionItem, ActionSourceRef, 枚举
- **验收**: V-01 通过

### 5.5-2: add-action-compiler-core ⭐
- **优先级**: P1 | **预估**: 1 周 | **依赖**: 5.5-1, 5-1, 5-8
- **路径**: `backend/services/action_compiler/`
- **内容**: ContextAggregator, ActionCompilerService, Daily/Weekly Compile
- **验收**: V-02, V-04 通过

### 5.5-3: add-action-feedback-analyzer
- **优先级**: P2 | **预估**: 0.5 周 | **依赖**: 5.5-2, 5-4
- **路径**: `backend/services/action_compiler/analyzer.py`
- **内容**: FeedbackAnalyzer, AvoidanceInsight, Memory 回写
- **验收**: V-03, V-05 通过
```
