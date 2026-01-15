# LS Roadmap 可执行版 v2.0 (生产级)

> **版本**: v2.0  
> **日期**: 2025-12-07  
> **定位**: 从"命理分析引擎"演进到"人生版本系统"的完整架构统一与实施路线  
> **关联**: `ls_roadmap_plus.md` (差距分析)  
> **原则**: 不做 MVP，一步到位设计正确架构

---

## 目录

1. [架构审计：现有断层识别](#一架构审计现有断层识别)
2. [统一维度体系](#二统一维度体系)
3. [统一时间体系](#三统一时间体系)
4. [场景系统设计](#四场景系统设计)
5. [Life Versions 核心架构](#五life-versions-核心架构)
6. [版本树与决策追踪](#六版本树与决策追踪)
7. [学习系统设计](#七学习系统设计)
8. [现有模块对接修复](#八现有模块对接修复)
9. [文档与契约更新](#九文档与契约更新)
10. [实施路线](#十实施路线)

---

## 一、架构审计：现有断层识别

### 1.1 已识别的核心断层

经过代码库审计，发现以下 **必须修复** 的断层：

| 断层编号 | 位置 | 问题描述 | 严重程度 |
|---------|------|---------|---------|
| **GAP-01** | 维度体系 | 三套维度定义不统一：`dimension.py`(10个) vs `CrossDomainAxes.life_domain`(4个) vs `PlaybookGenerator.DIMENSIONS`(4个中文) | 🔴 高 |
| **GAP-02** | 时间体系 | `CrossDomainAxes.time_horizon` 与因子本体的 temporal 类型无映射 | 🔴 高 |
| **GAP-03** | Playbook断接 | `PlaybookGenerator._generate_playbook` 标注 TODO，未集成 L1-L4 Pipeline | 🔴 高 |
| **GAP-04** | 规则→决策 | `RuntimeRuleResult.dimension` 到"决策维度"无映射链路 | 🟡 中 |
| **GAP-05** | 场景缺失 | 有 `life_domain` 标签但无"场景路由"实体 | 🟡 中 |
| **GAP-06** | 反馈断链 | `ActionItem.feedback_*` 字段存在但无回流到因子/规则的 pipeline | 🟡 中 |

### 1.2 断层关系图

```
┌─────────────────────────────────────────────────────────────────────┐
│                     当前系统断层地图                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  L1 Calculator ──→ FactorMatrix ──→ L3 RuleEngine                   │
│       │                                    │                        │
│       │                                    ▼                        │
│       │                           RuntimeRuleResult                 │
│       │                           ├─ dimension (10种)    ←──┐       │
│       │                           └─ cross_domain_axes      │       │
│       │                              └─ life_domain (4种) ──┤ GAP-01│
│       │                                                     │       │
│       │                    PlaybookGenerator.DIMENSIONS ────┘       │
│       │                    (4种中文，未对接 Pipeline) ←── GAP-03    │
│       │                                                             │
│       ▼                                                             │
│  temporal 因子 ──────────────────────────────────────→ ?            │
│  (流年/大运/流月)          GAP-02: 无时间桶映射                      │
│                                                                     │
│  ActionItem.feedback ─────────────────────────────────→ ?           │
│                              GAP-06: 无回流 pipeline                │
│                                                                     │
│  用户问题 ─────────────────────────────────────────────→ ?          │
│                              GAP-05: 无场景路由                      │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.3 修复优先级

**第一优先级（阻塞性）**：
- GAP-01: 维度体系统一 → 所有下游都依赖
- GAP-02: 时间体系统一 → 时间线预测依赖
- GAP-03: Playbook 对接 → 产品主入口

**第二优先级（功能性）**：
- GAP-04: 规则→决策映射
- GAP-05: 场景路由

**第三优先级（闭环性）**：
- GAP-06: 反馈回流

---

## 二、统一维度体系（修复 GAP-01）

### 2.1 问题分析

当前存在三套相互独立的维度定义：

| 来源 | 维度列表 | 用途 |
|------|---------|------|
| `dimension.py` | career, health, marriage, wealth, personality, fortune, omen, guidance, unconscious, general (10个) | 规则结果分类 |
| `CrossDomainAxes.life_domain` | career, health, relationship, wealth (4个) | 跨域轴标注 |
| `PlaybookGenerator.DIMENSIONS` | 事业, 财富, 感情, 健康 (4个中文) | Playbook 生成 |

**核心问题**：
- "婚姻(marriage)" vs "感情(relationship)" 语义重叠
- personality, fortune, omen, guidance, unconscious 等维度在 life_domain 中缺失
- 中英文映射不一致

### 2.2 统一设计：三层维度体系

```
┌─────────────────────────────────────────────────────────────────────┐
│                       统一维度体系架构                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Layer 1: 生活领域 (LifeDomain) - 7个                               │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │ career | wealth | relationship | health | family |          │    │
│  │ creativity | spiritual                                      │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                              │                                      │
│                              ▼                                      │
│  Layer 2: 分析维度 (AnalysisDimension) - 10个                       │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │ career | health | marriage | wealth | personality |         │    │
│  │ fortune | omen | guidance | unconscious | general          │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                              │                                      │
│                              ▼                                      │
│  Layer 3: 决策维度 (DecisionAxis) - 每场景5-8个                     │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │ income_ceiling | stability | autonomy | growth_potential |  │    │
│  │ social_density | risk_tolerance | ...                       │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.3 详细定义

**文件**: `backend/core/contracts/unified_dimensions.py` (新建)

```python
"""
统一维度体系

解决 GAP-01: 三套维度定义不统一问题

设计原则：
1. 三层维度各有职责，不混用
2. 提供完整的映射关系
3. 所有现有代码通过此模块访问维度
"""

from enum import Enum
from typing import Dict, List, Set
from pydantic import BaseModel, Field


# =============================================================================
# Layer 1: 生活领域 (产品层面向用户)
# =============================================================================

class LifeDomain(str, Enum):
    """
    生活领域 - 用户可感知的人生维度
    
    用于：场景选择、版本分类、用户交互
    """
    CAREER = "career"           # 职业/事业
    WEALTH = "wealth"           # 财富/收入
    RELATIONSHIP = "relationship"  # 感情/人际
    HEALTH = "health"           # 健康/身体
    FAMILY = "family"           # 家庭/亲属
    CREATIVITY = "creativity"   # 创造力/学习
    SPIRITUAL = "spiritual"     # 精神/内心


LIFE_DOMAIN_LABELS: Dict[LifeDomain, Dict[str, str]] = {
    LifeDomain.CAREER: {"zh": "事业", "en": "Career"},
    LifeDomain.WEALTH: {"zh": "财富", "en": "Wealth"},
    LifeDomain.RELATIONSHIP: {"zh": "感情", "en": "Relationship"},
    LifeDomain.HEALTH: {"zh": "健康", "en": "Health"},
    LifeDomain.FAMILY: {"zh": "家庭", "en": "Family"},
    LifeDomain.CREATIVITY: {"zh": "创造力", "en": "Creativity"},
    LifeDomain.SPIRITUAL: {"zh": "精神", "en": "Spiritual"},
}


# =============================================================================
# Layer 2: 分析维度 (规则引擎层面)
# =============================================================================

class AnalysisDimension(str, Enum):
    """
    分析维度 - 规则执行结果的分类
    
    用于：RuntimeRuleResult.dimension、主题映射
    """
    CAREER = "career"           # 事业
    HEALTH = "health"           # 健康
    MARRIAGE = "marriage"       # 婚姻（比 relationship 更具体）
    WEALTH = "wealth"           # 财富
    PERSONALITY = "personality" # 性格
    FORTUNE = "fortune"         # 运势
    OMEN = "omen"               # 预兆
    GUIDANCE = "guidance"       # 指引
    UNCONSCIOUS = "unconscious" # 潜意识
    GENERAL = "general"         # 通用


ANALYSIS_DIMENSION_LABELS: Dict[AnalysisDimension, Dict[str, str]] = {
    AnalysisDimension.CAREER: {"zh": "事业", "en": "Career"},
    AnalysisDimension.HEALTH: {"zh": "健康", "en": "Health"},
    AnalysisDimension.MARRIAGE: {"zh": "婚姻", "en": "Marriage"},
    AnalysisDimension.WEALTH: {"zh": "财富", "en": "Wealth"},
    AnalysisDimension.PERSONALITY: {"zh": "性格", "en": "Personality"},
    AnalysisDimension.FORTUNE: {"zh": "运势", "en": "Fortune"},
    AnalysisDimension.OMEN: {"zh": "预兆", "en": "Omen"},
    AnalysisDimension.GUIDANCE: {"zh": "指引", "en": "Guidance"},
    AnalysisDimension.UNCONSCIOUS: {"zh": "潜意识", "en": "Unconscious"},
    AnalysisDimension.GENERAL: {"zh": "通用", "en": "General"},
}


# =============================================================================
# 维度映射关系
# =============================================================================

# LifeDomain → 对应的 AnalysisDimensions
DOMAIN_TO_DIMENSIONS: Dict[LifeDomain, List[AnalysisDimension]] = {
    LifeDomain.CAREER: [
        AnalysisDimension.CAREER,
        AnalysisDimension.FORTUNE,
        AnalysisDimension.GUIDANCE,
    ],
    LifeDomain.WEALTH: [
        AnalysisDimension.WEALTH,
        AnalysisDimension.FORTUNE,
    ],
    LifeDomain.RELATIONSHIP: [
        AnalysisDimension.MARRIAGE,
        AnalysisDimension.PERSONALITY,
    ],
    LifeDomain.HEALTH: [
        AnalysisDimension.HEALTH,
    ],
    LifeDomain.FAMILY: [
        AnalysisDimension.MARRIAGE,
        AnalysisDimension.PERSONALITY,
    ],
    LifeDomain.CREATIVITY: [
        AnalysisDimension.PERSONALITY,
        AnalysisDimension.GUIDANCE,
        AnalysisDimension.UNCONSCIOUS,
    ],
    LifeDomain.SPIRITUAL: [
        AnalysisDimension.UNCONSCIOUS,
        AnalysisDimension.OMEN,
        AnalysisDimension.GUIDANCE,
    ],
}

# AnalysisDimension → 可能归属的 LifeDomains
DIMENSION_TO_DOMAINS: Dict[AnalysisDimension, List[LifeDomain]] = {
    dim: [d for d, dims in DOMAIN_TO_DIMENSIONS.items() if dim in dims]
    for dim in AnalysisDimension
}


# =============================================================================
# Layer 3: 决策维度 (版本比较层面)
# =============================================================================

class DecisionAxis(BaseModel):
    """
    决策维度 - 用于 Life Versions 比较
    
    每个场景(LifeDomain)有自己的决策维度集合
    """
    axis_id: str = Field(..., pattern="^[a-z][a-z0-9_]*$")
    label_zh: str
    label_en: str
    description: str = ""
    value_type: str = Field(default="float", pattern="^(float|enum|boolean)$")
    value_range: tuple = Field(default=(0.0, 1.0))
    default_weight: float = Field(default=1.0, ge=0.0, le=2.0)


# 各场景的决策维度定义
CAREER_DECISION_AXES: List[DecisionAxis] = [
    DecisionAxis(
        axis_id="income_ceiling",
        label_zh="收入上限",
        label_en="Income Ceiling",
        description="该路径的预期最高收入水平",
    ),
    DecisionAxis(
        axis_id="stability",
        label_zh="稳定性",
        label_en="Stability",
        description="工作/收入的稳定程度",
    ),
    DecisionAxis(
        axis_id="autonomy",
        label_zh="自主性",
        label_en="Autonomy",
        description="工作的自由度和决策权",
    ),
    DecisionAxis(
        axis_id="growth_potential",
        label_zh="成长性",
        label_en="Growth Potential",
        description="技能和职级的上升空间",
    ),
    DecisionAxis(
        axis_id="social_exposure",
        label_zh="社交曝光",
        label_en="Social Exposure",
        description="社交和人脉拓展机会",
    ),
    DecisionAxis(
        axis_id="work_life_balance",
        label_zh="工作生活平衡",
        label_en="Work-Life Balance",
        description="工作与生活的平衡程度",
    ),
]

RELATIONSHIP_DECISION_AXES: List[DecisionAxis] = [
    DecisionAxis(
        axis_id="emotional_depth",
        label_zh="情感深度",
        label_en="Emotional Depth",
        description="关系的情感连接程度",
    ),
    DecisionAxis(
        axis_id="compatibility",
        label_zh="匹配度",
        label_en="Compatibility",
        description="价值观和生活方式的匹配",
    ),
    DecisionAxis(
        axis_id="independence",
        label_zh="独立性",
        label_en="Independence",
        description="保持个人空间的程度",
    ),
    DecisionAxis(
        axis_id="social_harmony",
        label_zh="社交和谐",
        label_en="Social Harmony",
        description="与双方社交圈的融洽程度",
    ),
    DecisionAxis(
        axis_id="future_planning",
        label_zh="未来规划",
        label_en="Future Planning",
        description="对未来的共同规划清晰度",
    ),
]

# ... 其他场景的决策维度 (WEALTH, HEALTH, FAMILY, CREATIVITY, SPIRITUAL)


# =============================================================================
# 统一访问接口
# =============================================================================

class DimensionRegistry:
    """
    维度注册表 - 所有维度访问的统一入口
    
    废弃直接使用 dimension.py 的旧接口
    """
    
    @staticmethod
    def get_life_domain_label(domain: LifeDomain, lang: str = "zh") -> str:
        return LIFE_DOMAIN_LABELS[domain][lang]
    
    @staticmethod
    def get_analysis_dimension_label(dim: AnalysisDimension, lang: str = "zh") -> str:
        return ANALYSIS_DIMENSION_LABELS[dim][lang]
    
    @staticmethod
    def get_dimensions_for_domain(domain: LifeDomain) -> List[AnalysisDimension]:
        return DOMAIN_TO_DIMENSIONS.get(domain, [])
    
    @staticmethod
    def get_domains_for_dimension(dim: AnalysisDimension) -> List[LifeDomain]:
        return DIMENSION_TO_DOMAINS.get(dim, [])
    
    @staticmethod
    def normalize_dimension(raw: str) -> AnalysisDimension:
        """标准化维度名称（兼容旧数据）"""
        # 英文小写
        lower = raw.lower()
        for dim in AnalysisDimension:
            if dim.value == lower:
                return dim
        
        # 中文映射
        for dim, labels in ANALYSIS_DIMENSION_LABELS.items():
            if raw == labels["zh"]:
                return dim
        
        return AnalysisDimension.GENERAL
```

### 2.4 迁移方案

**需要修改的文件**：

| 文件 | 修改内容 |
|------|---------|
| `backend/rules/dimension.py` | 废弃，改为 import from `unified_dimensions` |
| `backend/core/contracts/cross_domain_models.py` | `life_domain` 改为 `List[LifeDomain]` |
| `backend/services/playbook/generator.py` | `DIMENSIONS` 改为从 `DimensionRegistry` 获取 |
| `backend/integration/theme_mapper.py` | 使用 `DimensionRegistry.normalize_dimension` |

**迁移步骤**：

1. 创建 `unified_dimensions.py`
2. 添加 `@deprecated` 装饰器到 `dimension.py` 的旧函数
3. 修改 `CrossDomainAxes`，使用强类型 `List[LifeDomain]`
4. 修改 `PlaybookGenerator`，使用 `DimensionRegistry`
5. 运行全量测试，确保映射正确

### 2.5 验收标准

- [ ] 所有维度通过 `DimensionRegistry` 访问
- [ ] `dimension.py` 旧接口标记为 deprecated
- [ ] `CrossDomainAxes.life_domain` 改为强类型
- [ ] 现有测试全部通过
- [ ] 新增维度映射测试（覆盖所有 domain ↔ dimension 关系）

---

## 三、统一时间体系（修复 GAP-02）

### 3.1 问题分析

当前时间相关概念分散且不统一：

| 来源 | 时间概念 | 用途 |
|------|---------|------|
| `CrossDomainAxes.time_horizon` | short_term/medium_term/long_term | 跨域轴标注 |
| 因子本体 temporal 类 | 流年/大运/流月/行星过境等 | 因子分类 |
| 规则 tags | 近期/长期等文本 | 规则标签 |

**核心问题**：
- 无统一的"时间桶"定义
- temporal 因子与 time_horizon 无映射
- 不同体系的时间周期差异大（八字大运10年 vs 占星行星周期不等）

### 3.2 统一设计：四层时间体系

```
┌─────────────────────────────────────────────────────────────────────┐
│                       统一时间体系架构                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Layer 1: 时间视野 (TimeHorizon) - 产品层                           │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │ immediate (1周内) | short_term (1-3月) | medium_term (1年) |│    │
│  │ long_term (1-3年) | life_phase (10年+)                      │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                              │                                      │
│                              ▼                                      │
│  Layer 2: 时间桶 (TimeBucket) - 预测层                              │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │ week | month | quarter | half_year | year | decade          │    │
│  │ 格式: 2025-W03 | 2025-03 | 2025-Q1 | 2025-H1 | 2025 | 2020s │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                              │                                      │
│                              ▼                                      │
│  Layer 3: 时间因子映射 (TemporalFactorMapping)                      │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │ 八字: 流年→year, 大运→decade, 流月→month                      │    │
│  │ 占星: 土星周期→2.5year, 木星周期→year, 流日→day               │    │
│  │ 紫微: 大限→decade, 流年→year                                 │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                              │                                      │
│                              ▼                                      │
│  Layer 4: 时间线节点 (TimelineNode) - 展示层                        │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │ 每个节点: time_bucket + domain_scores + confidence          │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.3 详细定义

**文件**: `backend/core/contracts/unified_time.py` (新建)

```python
"""
统一时间体系

解决 GAP-02: time_horizon 与 temporal 因子无映射问题

设计原则：
1. 四层时间概念各有职责
2. 提供体系到统一时间桶的映射
3. 支持任意时间点到时间桶的转换
"""

from enum import Enum
from datetime import datetime, date
from typing import Dict, List, Optional, Tuple
from pydantic import BaseModel, Field


# =============================================================================
# Layer 1: 时间视野 (产品层面向用户)
# =============================================================================

class TimeHorizon(str, Enum):
    """
    时间视野 - 用户可感知的时间范围
    
    比原有 short/medium/long 更细分
    """
    IMMEDIATE = "immediate"     # 即时 (1周内)
    SHORT_TERM = "short_term"   # 短期 (1-3个月)
    MEDIUM_TERM = "medium_term" # 中期 (3-12个月)
    LONG_TERM = "long_term"     # 长期 (1-3年)
    LIFE_PHASE = "life_phase"   # 人生阶段 (10年+)


TIME_HORIZON_LABELS: Dict[TimeHorizon, Dict[str, str]] = {
    TimeHorizon.IMMEDIATE: {"zh": "即时", "en": "Immediate", "range": "1周内"},
    TimeHorizon.SHORT_TERM: {"zh": "短期", "en": "Short-term", "range": "1-3个月"},
    TimeHorizon.MEDIUM_TERM: {"zh": "中期", "en": "Medium-term", "range": "3-12个月"},
    TimeHorizon.LONG_TERM: {"zh": "长期", "en": "Long-term", "range": "1-3年"},
    TimeHorizon.LIFE_PHASE: {"zh": "人生阶段", "en": "Life Phase", "range": "10年+"},
}


# =============================================================================
# Layer 2: 时间桶 (预测层)
# =============================================================================

class TimeBucketGranularity(str, Enum):
    """时间桶粒度"""
    WEEK = "week"           # 周: 2025-W03
    MONTH = "month"         # 月: 2025-03
    QUARTER = "quarter"     # 季: 2025-Q1
    HALF_YEAR = "half_year" # 半年: 2025-H1
    YEAR = "year"           # 年: 2025
    DECADE = "decade"       # 十年: 2020s


class TimeBucket(BaseModel):
    """
    时间桶 - 时间线预测的基本单位
    """
    bucket_id: str = Field(..., description="唯一标识，如 2025-Q1")
    granularity: TimeBucketGranularity
    start_date: date
    end_date: date
    label_zh: str
    label_en: str
    
    @classmethod
    def from_date(cls, dt: date, granularity: TimeBucketGranularity) -> "TimeBucket":
        """从日期创建时间桶"""
        if granularity == TimeBucketGranularity.QUARTER:
            q = (dt.month - 1) // 3 + 1
            return cls(
                bucket_id=f"{dt.year}-Q{q}",
                granularity=granularity,
                start_date=date(dt.year, (q-1)*3+1, 1),
                end_date=date(dt.year, q*3, 28),  # 简化
                label_zh=f"{dt.year}年第{q}季度",
                label_en=f"{dt.year} Q{q}",
            )
        # ... 其他粒度实现
        raise NotImplementedError(f"Granularity {granularity} not implemented")


# TimeHorizon → 推荐的 TimeBucketGranularity
HORIZON_TO_GRANULARITY: Dict[TimeHorizon, TimeBucketGranularity] = {
    TimeHorizon.IMMEDIATE: TimeBucketGranularity.WEEK,
    TimeHorizon.SHORT_TERM: TimeBucketGranularity.MONTH,
    TimeHorizon.MEDIUM_TERM: TimeBucketGranularity.QUARTER,
    TimeHorizon.LONG_TERM: TimeBucketGranularity.YEAR,
    TimeHorizon.LIFE_PHASE: TimeBucketGranularity.DECADE,
}


# =============================================================================
# Layer 3: 体系时间因子映射
# =============================================================================

class SystemTemporalMapping(BaseModel):
    """体系时间因子映射配置"""
    system_id: str  # bazi, astro, ziwei
    factor_pattern: str  # 因子ID通配符
    target_granularity: TimeBucketGranularity
    cycle_description: str  # 周期说明


# 各体系时间因子到统一时间桶的映射
TEMPORAL_FACTOR_MAPPINGS: List[SystemTemporalMapping] = [
    # 八字
    SystemTemporalMapping(
        system_id="bazi",
        factor_pattern="bazi_liunian_*",
        target_granularity=TimeBucketGranularity.YEAR,
        cycle_description="流年，每年一轮",
    ),
    SystemTemporalMapping(
        system_id="bazi",
        factor_pattern="bazi_dayun_*",
        target_granularity=TimeBucketGranularity.DECADE,
        cycle_description="大运，每10年一轮",
    ),
    SystemTemporalMapping(
        system_id="bazi",
        factor_pattern="bazi_liuyue_*",
        target_granularity=TimeBucketGranularity.MONTH,
        cycle_description="流月，每月一轮",
    ),
    
    # 占星
    SystemTemporalMapping(
        system_id="astro",
        factor_pattern="astro_transit_saturn_*",
        target_granularity=TimeBucketGranularity.YEAR,  # 土星约2.5年一宫
        cycle_description="土星过境，约29年一周期",
    ),
    SystemTemporalMapping(
        system_id="astro",
        factor_pattern="astro_transit_jupiter_*",
        target_granularity=TimeBucketGranularity.YEAR,  # 木星约1年一宫
        cycle_description="木星过境，约12年一周期",
    ),
    SystemTemporalMapping(
        system_id="astro",
        factor_pattern="astro_solar_return_*",
        target_granularity=TimeBucketGranularity.YEAR,
        cycle_description="太阳回归，每年一次",
    ),
    
    # 紫微
    SystemTemporalMapping(
        system_id="ziwei",
        factor_pattern="ziwei_daxian_*",
        target_granularity=TimeBucketGranularity.DECADE,
        cycle_description="大限，每10年一轮",
    ),
    SystemTemporalMapping(
        system_id="ziwei",
        factor_pattern="ziwei_liunian_*",
        target_granularity=TimeBucketGranularity.YEAR,
        cycle_description="流年，每年一轮",
    ),
]


# =============================================================================
# Layer 4: 时间线节点
# =============================================================================

class TimelineNode(BaseModel):
    """
    时间线节点 - 预测结果的展示单位
    """
    node_id: str
    bucket: TimeBucket
    
    # 各生活领域在该时间桶的预期得分
    domain_scores: Dict[str, float] = Field(
        default_factory=dict,
        description="LifeDomain → score (0-1)"
    )
    
    # 该时间桶的关键信息
    favorable_factors: List[str] = Field(default_factory=list)
    risk_factors: List[str] = Field(default_factory=list)
    key_events: List[str] = Field(default_factory=list)
    suggested_actions: List[str] = Field(default_factory=list)
    
    # 元数据
    confidence: float = Field(..., ge=0.0, le=1.0)
    source_factors: List[str] = Field(default_factory=list)
    source_rules: List[str] = Field(default_factory=list)
    contributing_systems: List[str] = Field(default_factory=list)


class TimelineProjection(BaseModel):
    """
    时间线投射 - 完整的时间预测结果
    """
    projection_id: str = Field(..., pattern="^proj_[a-z0-9]{12}$")
    user_id: str
    scenario_id: str
    
    # 时间范围
    horizon: TimeHorizon
    granularity: TimeBucketGranularity
    start_date: date
    end_date: date
    
    # 节点列表
    nodes: List[TimelineNode] = Field(..., min_length=1)
    
    # 关键决策点
    branch_points: List["BranchPoint"] = Field(default_factory=list)
    
    # 元数据
    created_at: datetime = Field(default_factory=datetime.now)
    confidence: float = Field(..., ge=0.0, le=1.0)


class BranchPoint(BaseModel):
    """
    分支点 - 关键决策节点
    """
    point_id: str
    bucket: TimeBucket
    decision_question: str
    options: List[str] = Field(..., min_length=2, max_length=5)
    recommendation: Optional[str] = None
    source_rules: List[str] = Field(default_factory=list)


# =============================================================================
# 统一访问接口
# =============================================================================

class TimeRegistry:
    """
    时间注册表 - 统一时间访问入口
    """
    
    @staticmethod
    def get_granularity_for_horizon(horizon: TimeHorizon) -> TimeBucketGranularity:
        return HORIZON_TO_GRANULARITY[horizon]
    
    @staticmethod
    def get_factor_mapping(factor_id: str) -> Optional[SystemTemporalMapping]:
        """根据因子ID获取时间映射"""
        import fnmatch
        for mapping in TEMPORAL_FACTOR_MAPPINGS:
            if fnmatch.fnmatch(factor_id, mapping.factor_pattern):
                return mapping
        return None
    
    @staticmethod
    def generate_buckets(
        start: date,
        end: date,
        granularity: TimeBucketGranularity
    ) -> List[TimeBucket]:
        """生成时间桶序列"""
        buckets = []
        current = start
        while current < end:
            bucket = TimeBucket.from_date(current, granularity)
            buckets.append(bucket)
            # 移动到下一个桶
            if granularity == TimeBucketGranularity.QUARTER:
                current = date(
                    current.year + (current.month + 2) // 12,
                    ((current.month + 2) % 12) + 1,
                    1
                )
            # ... 其他粒度
        return buckets
```

### 3.4 迁移方案

**需要修改的文件**：

| 文件 | 修改内容 |
|------|---------|
| `backend/core/contracts/cross_domain_models.py` | `time_horizon` 改为 `TimeHorizon` 枚举 |
| `data/factor_ontology/namespace.yaml` | 新增 temporal 因子命名规范 |
| `backend/calculators/*/` | 确保时间因子 ID 符合映射规范 |

### 3.5 验收标准

- [ ] `TimeHorizon` 5级时间视野定义完成
- [ ] `TimeBucket` 6种粒度支持
- [ ] 八字/占星/紫微时间因子映射完成
- [ ] `TimeRegistry.generate_buckets` 可生成任意时间范围的桶序列
- [ ] 现有 `cross_domain_axes.time_horizon` 兼容性保持

---

## 四、场景系统设计（修复 GAP-05）

场景路由是将"报告"变成"决策画布"的关键。生产级实现需要：多层分类、多场景混合、置信度评估。

**核心文件**: `backend/services/scenario/router.py`

关键设计要点：
1. **三层分类**: 关键词(<1ms) → 语义匹配(<10ms) → LLM fallback(<500ms)
2. **完整关键词表**: 每场景包含同义词、否定词、权重
3. **多场景混合处理**: 识别主场景和次场景
4. **因子/规则筛选**: 根据场景模板过滤，减少 50%+ 执行量

**场景模板配置**: `data/scenario_templates/*.yaml`

每个场景包含：
- 6-8个决策维度（带计算公式ID）
- 因子筛选规则（include/exclude/always_include）
- 规则分类列表
- 场景关联关系

---

## 五、现有模块对接修复（修复 GAP-03/04/06）

### 5.1 GAP-03: Playbook 对接 Pipeline

**修复**: `PlaybookGenerator` 注入 `Pipeline`，调用完整链路获取 `FusionResult`

### 5.2 GAP-04: 规则→决策维度映射

**修复**: 新增 `ANALYSIS_TO_DECISION` 映射表 + `DecisionScoreCalculator`

### 5.3 GAP-06: 反馈回流 Pipeline

**修复**: 新增 `FeedbackPipeline`，监听 ActionItem 状态变化，触发因子/权重更新

---

## 六、Life Versions 核心架构

详见原 Phase 3-5 设计。核心要点：

1. **LifeVersion**: 包含策略、预期收益、风险、适合人群
2. **LifeVersionGenerator**: 规则聚类→版本生成→差异化校验
3. **VersionTree**: 用户决策轨迹追踪
4. **学习闭环**: FactorUpdater + RuleWeightAdjuster + GlobalRuleStats

---

## 七、实施路线

| 阶段 | 任务 | 周期 | 依赖 |
|------|------|------|------|
| **W1-2** | GAP-01 维度统一 | 2周 | 无 |
| **W2-3** | GAP-02 时间统一 | 1.5周 | W1 |
| **W3-4** | GAP-03 Playbook对接 | 1周 | W1 |
| **W4-5** | GAP-05 场景路由 | 1.5周 | W1+W2 |
| **W5-7** | Life Versions | 2周 | W4 |
| **W7-9** | 版本树 | 2周 | W5 |
| **W9-12** | GAP-06 学习闭环 | 3周 | W7 |

---

## 八、文档更新清单

| 文档 | 更新内容 |
|------|---------|
| `数据契约_Schema定义规范_v1.md` | 新增 §10-15（维度/时间/场景/版本/学习模型） |
| `ls_engine_architecture_v3.md` | 更新 Pipeline 流程图，新增组件 |
| `factor_ontology/namespace.yaml` | 新增 temporal 命名空间 |

---

## 九、验收标准总表

| GAP | 验收标准 |
|-----|---------|
| GAP-01 | 所有维度通过 `DimensionRegistry` 访问 |
| GAP-02 | 时间因子→时间桶映射完整 |
| GAP-03 | Playbook 输出包含真实规则结论 |
| GAP-04 | `FusionResult.decision_scores` 正确计算 |
| GAP-05 | 7场景分类准确率 >90% |
| GAP-06 | 行动反馈触发因子/权重更新 |

---

## （以下保留原 Phase 设计供参考）

#### Task 2.2: 实现时间推演器（原设计）

**文件**: `backend/services/timeline/projector.py` (新建)

```python
class TimelineProjector:
    """时间线推演器"""
    
    def project(
        self,
        factor_matrix: FactorMatrix,
        scenario_ctx: ScenarioContext,
        rule_results: List[RuntimeRuleResult],
        years: int = 3
    ) -> TimelineProjection:
        """
        基于因子和规则结果，推演未来时间线
        
        核心逻辑:
        1. 提取 temporal 类因子（流年、大运等）
        2. 按时间桶聚合规则结果
        3. 识别关键分支点
        """
        temporal_factors = self._extract_temporal_factors(factor_matrix)
        time_buckets = self._generate_time_buckets(years)
        
        nodes = []
        for bucket in time_buckets:
            node = self._project_bucket(
                bucket, temporal_factors, rule_results, scenario_ctx
            )
            nodes.append(node)
        
        branch_points = self._identify_branch_points(nodes)
        
        return TimelineProjection(
            projection_id=self._gen_id(),
            scenario_id=scenario_ctx.scenario_id,
            user_id="",  # 由调用方填充
            nodes=nodes,
            branch_points=branch_points,
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=years*365),
        )
    
    def _extract_temporal_factors(self, matrix: FactorMatrix) -> Dict:
        """提取时间类因子"""
        result = {}
        for fid, fv in matrix.factors.items():
            # 流年、大运、流月等
            if any(k in fid for k in ["liunian", "dayun", "liuyue", "transit"]):
                result[fid] = fv
        return result
    
    def _project_bucket(
        self, 
        bucket: str, 
        temporal: Dict,
        rules: List[RuntimeRuleResult],
        ctx: ScenarioContext
    ) -> TimelineNode:
        """推演单个时间桶"""
        # MVP: 基于 temporal 因子和规则的 tags 做简单聚合
        # 后续: 接入专门的流年推演规则
        
        domain_scores = {}
        for axis in ctx.decision_axes:
            # 计算该维度在该时间桶的得分
            score = self._calc_axis_score(axis, temporal, rules, bucket)
            domain_scores[axis.axis_id] = score
        
        return TimelineNode(
            node_id=f"node_{bucket}",
            time_bucket=bucket,
            bucket_type=TimeBucket.QUARTER,
            domain_scores=domain_scores,
            confidence=0.6,  # MVP 固定值
            source_rules=[r.rule_id for r in rules if r.matched][:5],
        )
```

**验收标准**:
- [ ] 能生成 12 个季度节点（3年）
- [ ] 每个节点包含场景相关的维度得分
- [ ] 能识别至少 1 个分支点

**潜在坑点**:
- ⚠️ 时间因子（流年大运）的具体格式需与 Calculator 对齐
- ⚠️ MVP 阶段的 confidence 计算是简化版，生产需更复杂模型
- ⚠️ 不同体系（八字/占星）的时间周期不同，需统一映射

---

#### Task 2.3: 集成到 Pipeline

**文件**: `backend/pipeline/orchestrator.py` (修改)

```python
# 在 L4 Fusion 之前插入
timeline = None
if scenario_ctx:
    timeline = self._timeline_projector.project(
        factor_matrix,
        scenario_ctx,
        rule_results,
        years=3
    )

# FusionResult 新增
fusion_result.timeline = timeline
```

---

#### Task 2.4: 时间因子规范化

**文件**: `data/factor_ontology/temporal_factors.yaml` (新建/整理)

```yaml
# 统一时间因子命名规范
temporal_factors:
  # 八字
  - id: bazi_liunian_stem
    description: 流年天干
    value_type: enum
    value_range: [甲,乙,丙,丁,戊,己,庚,辛,壬,癸]
  - id: bazi_liunian_branch
    description: 流年地支
  - id: bazi_dayun_index
    description: 当前大运序号 (0-7)
    value_type: int
  
  # 占星
  - id: astro_transit_saturn_house
    description: 土星过境宫位
  - id: astro_transit_jupiter_house
    description: 木星过境宫位
```

**验收标准**:
- [ ] 八字、占星、紫微的时间因子统一命名
- [ ] 每个因子有 time_scope 标注（年/月/日）

---

### 3.3 Phase 2 测试计划

| 测试类型 | 文件 | 覆盖内容 |
|---------|------|---------|
| 单元测试 | `tests/timeline/test_projector.py` | 时间桶生成、节点计算 |
| 集成测试 | `tests/pipeline/test_timeline_pipeline.py` | 完整链路 |

### 3.4 Phase 2 文档更新

| 文档 | 更新内容 |
|------|---------|
| `docs/数据契约_Schema定义规范_v1.md` | 新增 §11 TimelineModels |
| `data/factor_ontology/namespace.yaml` | 新增 temporal 命名空间 |

---

## 四、Phase 3: Life Versions 核心

### 4.1 目标

让系统输出 2-3 个可选人生版本。

### 4.2 任务清单

#### Task 3.1: 定义 Life Version 数据模型

**文件**: `backend/core/contracts/life_version_models.py` (新建)

```python
class LifeVersion(BaseModel):
    """人生版本"""
    version_id: str = Field(..., pattern="^ver_[a-z0-9]{12}$")
    title: str = Field(..., max_length=20)  # "保守版" / "激进版"
    subtitle: str = Field(..., max_length=50)  # 一句话描述
    
    # 策略
    strategy: List[str] = Field(..., min_length=1, max_length=5)
    key_actions: List[str] = Field(default_factory=list)
    
    # 预期收益
    expected_outcomes: Dict[str, float] = Field(
        ..., description="决策维度 → 预期得分"
    )
    outcome_ranges: Dict[str, Tuple[float, float]] = Field(
        default_factory=dict, description="决策维度 → (下限, 上限)"
    )
    
    # 风险与代价
    risks: List[str] = Field(default_factory=list, max_length=5)
    costs: List[str] = Field(default_factory=list, max_length=3)
    
    # 适合人群
    suitable_for: List[str] = Field(default_factory=list)
    not_suitable_for: List[str] = Field(default_factory=list)
    
    # 置信度与来源
    confidence: float = Field(..., ge=0.0, le=1.0)
    source_factors: List[str] = Field(default_factory=list)
    source_rules: List[str] = Field(default_factory=list)
    
    # 时间线
    timeline_summary: Optional[str] = None

class LifeVersionSet(BaseModel):
    """版本集合"""
    set_id: str
    user_id: str
    scenario_id: str
    domain: LifeDomain
    
    versions: List[LifeVersion] = Field(..., min_length=2, max_length=4)
    comparison_axes: List[str]  # 用于对比的维度
    recommended_version_id: Optional[str] = None
    
    created_at: datetime = Field(default_factory=datetime.now)

class VersionComparison(BaseModel):
    """版本对比视图"""
    set_id: str
    axes: List[str]
    matrix: Dict[str, Dict[str, float]]  # version_id → axis → score
    summary_zh: str
```

---

#### Task 3.2: 实现版本生成器

**文件**: `backend/services/life_version/generator.py` (新建)

```python
class LifeVersionGenerator:
    """人生版本生成器"""
    
    def generate(
        self,
        fusion_result: FusionResult,
        scenario_ctx: ScenarioContext,
        timeline: TimelineProjection,
        version_count: int = 3
    ) -> LifeVersionSet:
        """
        从融合结果生成多个人生版本
        
        核心逻辑:
        1. 聚类规则结果，识别不同"倾向"
        2. 为每个倾向生成版本
        3. 计算版本间的差异化
        """
        # 1. 提取决策相关的规则结果
        decision_rules = self._filter_decision_rules(
            fusion_result.evidence_chain,
            scenario_ctx
        )
        
        # 2. 聚类为不同策略
        clusters = self._cluster_strategies(decision_rules)
        
        # 3. 生成版本
        versions = []
        templates = ["保守版", "平衡版", "激进版"]
        for i, cluster in enumerate(clusters[:version_count]):
            version = self._build_version(
                cluster,
                templates[i],
                scenario_ctx,
                timeline
            )
            versions.append(version)
        
        return LifeVersionSet(
            set_id=self._gen_id(),
            user_id="",
            scenario_id=scenario_ctx.scenario_id,
            domain=scenario_ctx.domain,
            versions=versions,
            comparison_axes=[a.axis_id for a in scenario_ctx.decision_axes],
        )
    
    def _cluster_strategies(self, rules: List[RuntimeRuleResult]) -> List[List]:
        """将规则聚类为不同策略倾向"""
        # MVP: 基于 level (吉/凶) 和 tags 简单分组
        # 后续: 使用 embedding 聚类
        conservative = [r for r in rules if "稳" in str(r.tags) or r.level in ["中等", "吉"]]
        aggressive = [r for r in rules if "变" in str(r.tags) or "突破" in str(r.description or "")]
        balanced = [r for r in rules if r not in conservative and r not in aggressive]
        return [conservative, balanced, aggressive]
```

**验收标准**:
- [ ] 能生成 2-3 个差异化版本
- [ ] 每个版本的 expected_outcomes 与场景 decision_axes 对应
- [ ] 版本间的策略描述明显不同

**潜在坑点**:
- ⚠️ 聚类策略是核心难点，MVP 用规则属性，生产需 LLM 辅助
- ⚠️ 版本"差异化"需要量化指标，否则可能生成相似版本
- ⚠️ 版本命名需考虑文化敏感性（避免"激进"等负面词）

---

#### Task 3.3: 实现版本对比视图

**文件**: `backend/services/life_version/comparator.py` (新建)

```python
class VersionComparator:
    """版本对比器"""
    
    def compare(self, version_set: LifeVersionSet) -> VersionComparison:
        """生成对比矩阵"""
        matrix = {}
        for version in version_set.versions:
            matrix[version.version_id] = version.expected_outcomes
        
        summary = self._generate_summary(version_set)
        
        return VersionComparison(
            set_id=version_set.set_id,
            axes=version_set.comparison_axes,
            matrix=matrix,
            summary_zh=summary,
        )
    
    def _generate_summary(self, vs: LifeVersionSet) -> str:
        """生成对比摘要"""
        # MVP: 模板化
        # 后续: LLM 生成
        return f"针对{vs.domain.value}场景，系统为您生成了{len(vs.versions)}个可选方案..."
```

---

#### Task 3.4: 改造 NarrativeGenerator

**文件**: `backend/services/narrative/generator.py` (修改)

```python
class NarrativeGenerator:
    # 新增方法
    async def generate_version_narrative(
        self,
        version_set: LifeVersionSet,
        comparison: VersionComparison,
    ) -> str:
        """生成版本对比叙事"""
        prompt = self._build_version_prompt(version_set, comparison)
        return await self._llm_client.generate(prompt)
```

---

#### Task 3.5: 前端对比组件（API契约）

**文件**: `backend/api/routes/versions.py` (新建)

```python
@router.get("/versions/{set_id}")
async def get_version_set(set_id: str) -> LifeVersionSet:
    """获取版本集合"""
    pass

@router.get("/versions/{set_id}/compare")
async def get_comparison(set_id: str) -> VersionComparison:
    """获取对比视图"""
    pass

@router.post("/versions/{set_id}/select/{version_id}")
async def select_version(set_id: str, version_id: str) -> None:
    """用户选择版本（记录到 Memory）"""
    pass
```

---

### 4.3 Phase 3 潜在坑点汇总

| 坑点 | 风险等级 | 应对策略 |
|------|---------|---------|
| 版本聚类质量差 | 高 | 增加规则 tags 规范，后续接 LLM |
| 版本差异化不足 | 中 | 增加"版本距离"指标，强制差异 |
| 版本数量不稳定 | 中 | 设置最小差异阈值，不足则合并 |
| 期望值计算不准 | 高 | MVP 用加权平均，后续需校准 |

---

## 五、Phase 4: 版本树与决策追踪

### 5.1 目标

让系统记录用户在版本树中的选择轨迹。

### 5.2 任务清单

#### Task 4.1: 定义版本树数据模型

**文件**: `backend/core/contracts/version_tree_models.py` (新建)

```python
class TreeNode(BaseModel):
    """版本树节点"""
    node_id: str
    parent_id: Optional[str] = None
    version_id: str  # 关联的 LifeVersion
    
    # 决策信息
    decision_point: Optional[str] = None  # 用户在此做的决策
    selected_option: Optional[str] = None
    
    # 时间
    decision_time: Optional[datetime] = None
    
    # 子节点
    children: List[str] = Field(default_factory=list)  # 子节点 node_id

class VersionTree(BaseModel):
    """版本树"""
    tree_id: str
    user_id: str
    root_node_id: str
    current_node_id: str  # 用户当前所在节点
    
    nodes: Dict[str, TreeNode]
    
    created_at: datetime
    updated_at: datetime

class DecisionRecord(BaseModel):
    """决策记录"""
    record_id: str
    user_id: str
    tree_id: str
    node_id: str
    
    decision_point: str
    options_presented: List[str]
    option_selected: str
    
    # 决策时的上下文
    context_snapshot: Dict[str, Any]
    
    created_at: datetime
```

---

#### Task 4.2: 实现版本树服务

**文件**: `backend/services/version_tree/service.py` (新建)

```python
class VersionTreeService:
    """版本树服务"""
    
    def __init__(self, memory_service: MemoryService):
        self._memory = memory_service
    
    async def create_tree(
        self, 
        user_id: str, 
        version_set: LifeVersionSet
    ) -> VersionTree:
        """从版本集创建版本树"""
        root_nodes = []
        for version in version_set.versions:
            node = TreeNode(
                node_id=self._gen_id(),
                version_id=version.version_id,
            )
            root_nodes.append(node)
        
        # 创建虚拟根节点
        root = TreeNode(
            node_id="root",
            version_id="",
            children=[n.node_id for n in root_nodes],
        )
        
        tree = VersionTree(
            tree_id=self._gen_id(),
            user_id=user_id,
            root_node_id="root",
            current_node_id="root",
            nodes={"root": root, **{n.node_id: n for n in root_nodes}},
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        
        await self._persist(tree)
        return tree
    
    async def record_decision(
        self,
        tree_id: str,
        node_id: str,
        option: str,
        context: Dict
    ) -> DecisionRecord:
        """记录用户决策"""
        tree = await self._load(tree_id)
        node = tree.nodes[node_id]
        
        record = DecisionRecord(
            record_id=self._gen_id(),
            user_id=tree.user_id,
            tree_id=tree_id,
            node_id=node_id,
            decision_point=node.decision_point or "",
            options_presented=node.children,
            option_selected=option,
            context_snapshot=context,
            created_at=datetime.now(),
        )
        
        # 更新当前节点
        tree.current_node_id = option
        tree.updated_at = datetime.now()
        
        # 持久化
        await self._persist(tree)
        await self._memory.record_event(
            user_id=tree.user_id,
            event_type="version_decision",
            data=record.model_dump(),
        )
        
        return record
```

---

### 5.3 Phase 4 潜在坑点

| 坑点 | 风险等级 | 应对策略 |
|------|---------|---------|
| 树结构膨胀 | 中 | 设置最大深度、定期归档 |
| 决策上下文太大 | 低 | 只保存关键因子快照 |
| 并发更新冲突 | 低 | 乐观锁 + 版本号 |

---

## 六、Phase 5: 学习闭环

### 6.1 目标

让系统根据反馈自校正。

### 6.2 任务清单

#### Task 5.1: 反馈 → 因子更新

**文件**: `backend/services/learning/factor_updater.py` (新建)

```python
class FactorUpdater:
    """因子更新器"""
    
    async def update_from_feedback(
        self,
        user_id: str,
        feedback_type: str,  # "action_completed" | "outcome_reported"
        data: Dict
    ) -> List[str]:
        """
        从反馈数据更新因子
        
        例如：连续12周高执行力 → 更新 user_execution_factor
        """
        updated_factors = []
        
        if feedback_type == "action_completed":
            # 统计近期完成率
            recent_actions = await self._get_recent_actions(user_id, weeks=12)
            completion_rate = self._calc_completion_rate(recent_actions)
            
            if completion_rate > 0.8:
                # 更新执行力因子
                await self._update_user_factor(
                    user_id,
                    "user_execution_ability",
                    value=completion_rate,
                    confidence=0.9,
                    source="behavior_learning"
                )
                updated_factors.append("user_execution_ability")
        
        return updated_factors
```

---

#### Task 5.2: 反馈 → 规则权重

**文件**: `backend/services/learning/weight_adjuster.py` (新建)

```python
class RuleWeightAdjuster:
    """规则权重调整器"""
    
    async def adjust_from_outcome(
        self,
        user_id: str,
        rule_id: str,
        predicted_outcome: str,
        actual_outcome: str,
    ) -> float:
        """
        根据预测 vs 实际调整规则权重
        
        返回新权重乘数
        """
        # 计算误差
        error = self._calc_error(predicted_outcome, actual_outcome)
        
        # 获取当前权重
        current = await self._get_user_weight(user_id, rule_id)
        
        # 调整（简单线性）
        adjustment = -0.1 * error  # 误差越大，权重降越多
        new_weight = max(0.1, min(2.0, current + adjustment))
        
        await self._save_user_weight(user_id, rule_id, new_weight)
        
        return new_weight

class PersonalizedWeights(BaseModel):
    """用户个性化权重表"""
    user_id: str
    weights: Dict[str, float]  # rule_id → multiplier
    sample_counts: Dict[str, int]  # rule_id → 样本数
    last_updated: datetime
```

---

#### Task 5.3: 全局规则统计

**文件**: `backend/services/learning/global_stats.py` (新建)

```python
class GlobalRuleStats:
    """全局规则统计"""
    
    async def update_stats(
        self,
        rule_id: str,
        prediction_correct: bool
    ) -> None:
        """更新规则的全局准确率"""
        stats = await self._get_stats(rule_id)
        stats.total_predictions += 1
        if prediction_correct:
            stats.correct_predictions += 1
        stats.accuracy = stats.correct_predictions / stats.total_predictions
        await self._save_stats(stats)

class RuleStatistics(BaseModel):
    rule_id: str
    total_predictions: int = 0
    correct_predictions: int = 0
    accuracy: float = 0.0
    last_updated: datetime
```

---

### 6.3 Phase 5 潜在坑点

| 坑点 | 风险等级 | 应对策略 |
|------|---------|---------|
| 冷启动问题 | 高 | 新用户使用全局权重 |
| 过拟合 | 中 | 设置权重调整上下限 |
| 反馈稀疏 | 高 | 主动收集反馈、推送回访 |
| 长周期验证 | 高 | 区分短期/长期反馈类型 |

---

## 七、文档更新清单

### 7.1 数据契约更新

**文件**: `docs/数据契约_Schema定义规范_v1.md`

| 章节 | 新增内容 |
|------|---------|
| §10 | ScenarioModels (LifeDomain, DecisionAxis, ScenarioContext) |
| §11 | TimelineModels (TimelineNode, BranchPoint, TimelineProjection) |
| §12 | LifeVersionModels (LifeVersion, LifeVersionSet, VersionComparison) |
| §13 | VersionTreeModels (TreeNode, VersionTree, DecisionRecord) |
| §14 | LearningModels (PersonalizedWeights, RuleStatistics) |

### 7.2 架构文档更新

**文件**: `docs/ls_engine_architecture_v3.md`

| 章节 | 更新内容 |
|------|---------|
| §2 | 更新 Pipeline 流程图，新增 ScenarioRouter/TimelineProjector/LifeVersionGenerator |
| §4 | 新增 Layer 4.5: Version Generation |
| §5 | 新增 Layer 6: Learning |

### 7.3 因子本体更新

**文件**: `data/factor_ontology/`

| 文件 | 更新内容 |
|------|---------|
| `namespace.yaml` | 新增 temporal、user_behavior 命名空间 |
| `temporal_factors.yaml` | 新增统一时间因子定义 |
| `user_factors.yaml` | 新增用户行为派生因子 |

### 7.4 新增文件清单

```
backend/
├── core/contracts/
│   ├── scenario_models.py      # P1
│   ├── timeline_models.py      # P2
│   ├── life_version_models.py  # P3
│   └── version_tree_models.py  # P4
├── services/
│   ├── scenario/
│   │   ├── __init__.py
│   │   └── router.py           # P1
│   ├── timeline/
│   │   ├── __init__.py
│   │   └── projector.py        # P2
│   ├── life_version/
│   │   ├── __init__.py
│   │   ├── generator.py        # P3
│   │   └── comparator.py       # P3
│   ├── version_tree/
│   │   ├── __init__.py
│   │   └── service.py          # P4
│   └── learning/
│       ├── __init__.py
│       ├── factor_updater.py   # P5
│       ├── weight_adjuster.py  # P5
│       └── global_stats.py     # P5
└── api/routes/
    └── versions.py             # P3

data/
├── scenario_templates/
│   ├── career.yaml
│   ├── wealth.yaml
│   ├── relationship.yaml
│   ├── health.yaml
│   ├── family.yaml
│   ├── creativity.yaml
│   └── spiritual.yaml
└── factor_ontology/
    ├── temporal_factors.yaml
    └── user_factors.yaml
```

---

## 八、风险与依赖

### 8.1 技术风险

| 风险 | 影响 | 概率 | 缓解措施 |
|------|------|------|---------|
| LLM 版本聚类质量差 | P3 延期 | 中 | 先用规则，后接 LLM |
| 时间因子格式不统一 | P2 返工 | 中 | 先整理因子本体 |
| 前端对比视图复杂 | P3 延期 | 低 | 先出 API，前端并行 |

### 8.2 外部依赖

| 依赖 | Phase | 说明 |
|------|-------|------|
| RuleEngine categories 过滤 | P1 | 需确认已支持 |
| MemoryService 持久化 | P4 | 需确认支持 VersionTree |
| LLM Client | P3/P5 | 叙事生成需要 |

---

## 九、里程碑

| 里程碑 | 预计日期 | 验收标准 |
|--------|---------|---------|
| M1: 场景路由 MVP | P1 +2周 | 7场景分类准确率 >80% |
| M2: 时间线 MVP | P2 +2周 | 生成12节点时间线 |
| M3: Life Versions v1 | P3 +3周 | 前端展示3版本对比 |
| M4: 版本树 v1 | P4 +3周 | 用户决策可追踪 |
| M5: 学习闭环 v1 | P5 +4周 | 权重调整可观测 |
