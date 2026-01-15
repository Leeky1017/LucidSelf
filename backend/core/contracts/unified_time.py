"""
统一时间体系

解决 GAP-02: time_horizon 与 temporal 因子无映射问题

设计原则：
1. 四层时间概念各有职责
2. 提供体系到统一时间桶的映射
3. 支持任意时间点到时间桶的转换

对照文档: docs/ls_roadmap_executable.md §三、统一时间体系
"""

from datetime import date, datetime, timedelta
from enum import Enum
from typing import Dict, List, Optional

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
        if granularity == TimeBucketGranularity.WEEK:
            year, week, _ = dt.isocalendar()
            # 计算周的开始和结束日期
            start = dt - timedelta(days=dt.weekday())
            end = start + timedelta(days=6)
            return cls(
                bucket_id=f"{year}-W{week:02d}",
                granularity=granularity,
                start_date=start,
                end_date=end,
                label_zh=f"{year}年第{week}周",
                label_en=f"{year} W{week:02d}",
            )
        elif granularity == TimeBucketGranularity.MONTH:
            # 月初和月末
            start = date(dt.year, dt.month, 1)
            if dt.month == 12:
                end = date(dt.year + 1, 1, 1) - timedelta(days=1)
            else:
                end = date(dt.year, dt.month + 1, 1) - timedelta(days=1)
            return cls(
                bucket_id=f"{dt.year}-{dt.month:02d}",
                granularity=granularity,
                start_date=start,
                end_date=end,
                label_zh=f"{dt.year}年{dt.month}月",
                label_en=f"{dt.year}-{dt.month:02d}",
            )
        elif granularity == TimeBucketGranularity.QUARTER:
            q = (dt.month - 1) // 3 + 1
            start_month = (q - 1) * 3 + 1
            end_month = q * 3
            start = date(dt.year, start_month, 1)
            if end_month == 12:
                end = date(dt.year, 12, 31)
            else:
                end = date(dt.year, end_month + 1, 1) - timedelta(days=1)
            return cls(
                bucket_id=f"{dt.year}-Q{q}",
                granularity=granularity,
                start_date=start,
                end_date=end,
                label_zh=f"{dt.year}年第{q}季度",
                label_en=f"{dt.year} Q{q}",
            )
        elif granularity == TimeBucketGranularity.HALF_YEAR:
            h = 1 if dt.month <= 6 else 2
            start_month = 1 if h == 1 else 7
            end_month = 6 if h == 1 else 12
            start = date(dt.year, start_month, 1)
            end = date(dt.year, end_month, 30 if end_month == 6 else 31)
            return cls(
                bucket_id=f"{dt.year}-H{h}",
                granularity=granularity,
                start_date=start,
                end_date=end,
                label_zh=f"{dt.year}年{'上' if h == 1 else '下'}半年",
                label_en=f"{dt.year} H{h}",
            )
        elif granularity == TimeBucketGranularity.YEAR:
            return cls(
                bucket_id=str(dt.year),
                granularity=granularity,
                start_date=date(dt.year, 1, 1),
                end_date=date(dt.year, 12, 31),
                label_zh=f"{dt.year}年",
                label_en=str(dt.year),
            )
        elif granularity == TimeBucketGranularity.DECADE:
            decade_start = (dt.year // 10) * 10
            return cls(
                bucket_id=f"{decade_start}s",
                granularity=granularity,
                start_date=date(decade_start, 1, 1),
                end_date=date(decade_start + 9, 12, 31),
                label_zh=f"{decade_start}年代",
                label_en=f"{decade_start}s",
            )
        else:
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
        target_granularity=TimeBucketGranularity.YEAR,
        cycle_description="土星过境，约29年一周期",
    ),
    SystemTemporalMapping(
        system_id="astro",
        factor_pattern="astro_transit_jupiter_*",
        target_granularity=TimeBucketGranularity.YEAR,
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


class TimelineProjection(BaseModel):
    """
    时间线投射 - 完整的时间预测结果
    """
    projection_id: str = Field(..., pattern=r"^proj_[a-z0-9]{12}$")
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
    branch_points: List[BranchPoint] = Field(default_factory=list)
    
    # 元数据
    created_at: datetime = Field(default_factory=datetime.now)
    confidence: float = Field(..., ge=0.0, le=1.0)


# =============================================================================
# 统一访问接口
# =============================================================================

class TimeRegistry:
    """
    时间注册表 - 统一时间访问入口
    """
    
    @staticmethod
    def get_granularity_for_horizon(horizon: TimeHorizon) -> TimeBucketGranularity:
        """获取时间视野对应的推荐时间桶粒度"""
        return HORIZON_TO_GRANULARITY[horizon]
    
    @staticmethod
    def get_horizon_label(horizon: TimeHorizon, lang: str = "zh") -> str:
        """获取时间视野标签"""
        return TIME_HORIZON_LABELS[horizon][lang]
    
    @staticmethod
    def get_horizon_range(horizon: TimeHorizon) -> str:
        """获取时间视野的时间范围描述"""
        return TIME_HORIZON_LABELS[horizon]["range"]
    
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
        seen_ids = set()
        
        while current <= end:
            bucket = TimeBucket.from_date(current, granularity)
            if bucket.bucket_id not in seen_ids:
                buckets.append(bucket)
                seen_ids.add(bucket.bucket_id)
            
            # 移动到下一个桶
            if granularity == TimeBucketGranularity.WEEK:
                current = current + timedelta(days=7)
            elif granularity == TimeBucketGranularity.MONTH:
                if current.month == 12:
                    current = date(current.year + 1, 1, 1)
                else:
                    current = date(current.year, current.month + 1, 1)
            elif granularity == TimeBucketGranularity.QUARTER:
                q = (current.month - 1) // 3 + 1
                if q == 4:
                    current = date(current.year + 1, 1, 1)
                else:
                    current = date(current.year, q * 3 + 1, 1)
            elif granularity == TimeBucketGranularity.HALF_YEAR:
                if current.month <= 6:
                    current = date(current.year, 7, 1)
                else:
                    current = date(current.year + 1, 1, 1)
            elif granularity == TimeBucketGranularity.YEAR:
                current = date(current.year + 1, 1, 1)
            elif granularity == TimeBucketGranularity.DECADE:
                decade_start = (current.year // 10) * 10
                current = date(decade_start + 10, 1, 1)
        
        return buckets
    
    @staticmethod
    def normalize_time_horizon(raw: str) -> Optional[TimeHorizon]:
        """
        标准化时间视野名称
        
        支持：
        - 英文: "short_term" -> SHORT_TERM
        - 中文: "短期" -> SHORT_TERM
        """
        lower = raw.lower().strip()
        for horizon in TimeHorizon:
            if horizon.value == lower:
                return horizon
        
        for horizon, labels in TIME_HORIZON_LABELS.items():
            if raw.strip() == labels["zh"]:
                return horizon
        
        return None
    
    @staticmethod
    def get_all_time_horizons() -> List[TimeHorizon]:
        """获取所有时间视野"""
        return list(TimeHorizon)
    
    @staticmethod
    def get_all_granularities() -> List[TimeBucketGranularity]:
        """获取所有时间桶粒度"""
        return list(TimeBucketGranularity)
