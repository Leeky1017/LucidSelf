"""
Tests for Unified Time Module

对照文档: docs/ls_roadmap_executable.md §3.5 验收标准
"""

from datetime import date

import pytest

from backend.core.contracts.unified_time import (
    BranchPoint,
    HORIZON_TO_GRANULARITY,
    SystemTemporalMapping,
    TEMPORAL_FACTOR_MAPPINGS,
    TIME_HORIZON_LABELS,
    TimeBucket,
    TimeBucketGranularity,
    TimeHorizon,
    TimelineNode,
    TimelineProjection,
    TimeRegistry,
)


class TestTimeHorizon:
    """TimeHorizon 枚举测试"""
    
    def test_five_horizons_defined(self):
        """测试 5 级时间视野全部定义"""
        expected = {"immediate", "short_term", "medium_term", "long_term", "life_phase"}
        actual = {h.value for h in TimeHorizon}
        assert actual == expected
    
    def test_all_horizons_have_labels(self):
        """测试所有时间视野都有中英文标签和范围"""
        for horizon in TimeHorizon:
            assert horizon in TIME_HORIZON_LABELS
            assert "zh" in TIME_HORIZON_LABELS[horizon]
            assert "en" in TIME_HORIZON_LABELS[horizon]
            assert "range" in TIME_HORIZON_LABELS[horizon]
    
    def test_horizon_is_string_enum(self):
        """测试时间视野是字符串枚举"""
        assert TimeHorizon.SHORT_TERM == "short_term"
        assert TimeHorizon.LONG_TERM == "long_term"


class TestTimeBucketGranularity:
    """TimeBucketGranularity 枚举测试"""
    
    def test_six_granularities_defined(self):
        """测试 6 种粒度全部定义"""
        expected = {"week", "month", "quarter", "half_year", "year", "decade"}
        actual = {g.value for g in TimeBucketGranularity}
        assert actual == expected


class TestTimeBucket:
    """TimeBucket 模型测试"""
    
    def test_from_date_quarter(self):
        """测试从日期创建季度时间桶"""
        bucket = TimeBucket.from_date(date(2025, 2, 15), TimeBucketGranularity.QUARTER)
        assert bucket.bucket_id == "2025-Q1"
        assert bucket.start_date == date(2025, 1, 1)
        assert bucket.end_date == date(2025, 3, 31)
        assert "Q1" in bucket.label_en
    
    def test_from_date_month(self):
        """测试从日期创建月度时间桶"""
        bucket = TimeBucket.from_date(date(2025, 6, 15), TimeBucketGranularity.MONTH)
        assert bucket.bucket_id == "2025-06"
        assert bucket.start_date == date(2025, 6, 1)
        assert bucket.end_date == date(2025, 6, 30)
    
    def test_from_date_year(self):
        """测试从日期创建年度时间桶"""
        bucket = TimeBucket.from_date(date(2025, 8, 1), TimeBucketGranularity.YEAR)
        assert bucket.bucket_id == "2025"
        assert bucket.start_date == date(2025, 1, 1)
        assert bucket.end_date == date(2025, 12, 31)
    
    def test_from_date_decade(self):
        """测试从日期创建十年时间桶"""
        bucket = TimeBucket.from_date(date(2025, 1, 1), TimeBucketGranularity.DECADE)
        assert bucket.bucket_id == "2020s"
        assert bucket.start_date == date(2020, 1, 1)
        assert bucket.end_date == date(2029, 12, 31)
    
    def test_from_date_week(self):
        """测试从日期创建周时间桶"""
        bucket = TimeBucket.from_date(date(2025, 1, 15), TimeBucketGranularity.WEEK)
        assert bucket.bucket_id.startswith("2025-W")
        assert bucket.granularity == TimeBucketGranularity.WEEK
    
    def test_from_date_half_year(self):
        """测试从日期创建半年时间桶"""
        bucket1 = TimeBucket.from_date(date(2025, 3, 15), TimeBucketGranularity.HALF_YEAR)
        assert bucket1.bucket_id == "2025-H1"
        
        bucket2 = TimeBucket.from_date(date(2025, 9, 15), TimeBucketGranularity.HALF_YEAR)
        assert bucket2.bucket_id == "2025-H2"


class TestHorizonToGranularityMapping:
    """时间视野到粒度映射测试"""
    
    def test_all_horizons_mapped(self):
        """测试所有时间视野都有对应粒度"""
        for horizon in TimeHorizon:
            assert horizon in HORIZON_TO_GRANULARITY
    
    def test_immediate_maps_to_week(self):
        """测试即时映射到周"""
        assert HORIZON_TO_GRANULARITY[TimeHorizon.IMMEDIATE] == TimeBucketGranularity.WEEK
    
    def test_life_phase_maps_to_decade(self):
        """测试人生阶段映射到十年"""
        assert HORIZON_TO_GRANULARITY[TimeHorizon.LIFE_PHASE] == TimeBucketGranularity.DECADE


class TestTemporalFactorMappings:
    """体系时间因子映射测试"""
    
    def test_bazi_mappings_exist(self):
        """测试八字时间因子映射存在"""
        bazi_mappings = [m for m in TEMPORAL_FACTOR_MAPPINGS if m.system_id == "bazi"]
        assert len(bazi_mappings) >= 3  # 流年、大运、流月
    
    def test_astro_mappings_exist(self):
        """测试占星时间因子映射存在"""
        astro_mappings = [m for m in TEMPORAL_FACTOR_MAPPINGS if m.system_id == "astro"]
        assert len(astro_mappings) >= 2  # 土星、木星过境
    
    def test_ziwei_mappings_exist(self):
        """测试紫微时间因子映射存在"""
        ziwei_mappings = [m for m in TEMPORAL_FACTOR_MAPPINGS if m.system_id == "ziwei"]
        assert len(ziwei_mappings) >= 2  # 大限、流年


class TestTimeRegistry:
    """TimeRegistry 统一接口测试"""
    
    def test_get_granularity_for_horizon(self):
        """测试获取时间视野对应粒度"""
        assert TimeRegistry.get_granularity_for_horizon(TimeHorizon.SHORT_TERM) == TimeBucketGranularity.MONTH
        assert TimeRegistry.get_granularity_for_horizon(TimeHorizon.LONG_TERM) == TimeBucketGranularity.YEAR
    
    def test_get_horizon_label(self):
        """测试获取时间视野标签"""
        assert TimeRegistry.get_horizon_label(TimeHorizon.SHORT_TERM, "zh") == "短期"
        assert TimeRegistry.get_horizon_label(TimeHorizon.SHORT_TERM, "en") == "Short-term"
    
    def test_get_horizon_range(self):
        """测试获取时间视野范围"""
        assert TimeRegistry.get_horizon_range(TimeHorizon.SHORT_TERM) == "1-3个月"
        assert TimeRegistry.get_horizon_range(TimeHorizon.LIFE_PHASE) == "10年+"
    
    def test_get_factor_mapping_bazi(self):
        """测试获取八字因子映射"""
        mapping = TimeRegistry.get_factor_mapping("bazi_liunian_stem")
        assert mapping is not None
        assert mapping.system_id == "bazi"
        assert mapping.target_granularity == TimeBucketGranularity.YEAR
    
    def test_get_factor_mapping_astro(self):
        """测试获取占星因子映射"""
        mapping = TimeRegistry.get_factor_mapping("astro_transit_saturn_house")
        assert mapping is not None
        assert mapping.system_id == "astro"
    
    def test_get_factor_mapping_unknown(self):
        """测试未知因子返回 None"""
        mapping = TimeRegistry.get_factor_mapping("unknown_factor")
        assert mapping is None
    
    def test_generate_buckets_quarters(self):
        """测试生成季度时间桶序列"""
        buckets = TimeRegistry.generate_buckets(
            date(2025, 1, 1),
            date(2025, 12, 31),
            TimeBucketGranularity.QUARTER
        )
        assert len(buckets) == 4
        bucket_ids = [b.bucket_id for b in buckets]
        assert "2025-Q1" in bucket_ids
        assert "2025-Q4" in bucket_ids
    
    def test_generate_buckets_months(self):
        """测试生成月度时间桶序列"""
        buckets = TimeRegistry.generate_buckets(
            date(2025, 1, 1),
            date(2025, 6, 30),
            TimeBucketGranularity.MONTH
        )
        assert len(buckets) == 6
    
    def test_generate_buckets_years(self):
        """测试生成年度时间桶序列（3年）"""
        buckets = TimeRegistry.generate_buckets(
            date(2025, 1, 1),
            date(2027, 12, 31),
            TimeBucketGranularity.YEAR
        )
        assert len(buckets) == 3
        bucket_ids = [b.bucket_id for b in buckets]
        assert "2025" in bucket_ids
        assert "2027" in bucket_ids
    
    def test_normalize_time_horizon_english(self):
        """测试英文时间视野标准化"""
        assert TimeRegistry.normalize_time_horizon("short_term") == TimeHorizon.SHORT_TERM
        assert TimeRegistry.normalize_time_horizon("LONG_TERM") == TimeHorizon.LONG_TERM
    
    def test_normalize_time_horizon_chinese(self):
        """测试中文时间视野标准化"""
        assert TimeRegistry.normalize_time_horizon("短期") == TimeHorizon.SHORT_TERM
        assert TimeRegistry.normalize_time_horizon("长期") == TimeHorizon.LONG_TERM
    
    def test_normalize_time_horizon_unknown(self):
        """测试未知时间视野返回 None"""
        assert TimeRegistry.normalize_time_horizon("unknown") is None
    
    def test_get_all_time_horizons(self):
        """测试获取所有时间视野"""
        horizons = TimeRegistry.get_all_time_horizons()
        assert len(horizons) == 5
    
    def test_get_all_granularities(self):
        """测试获取所有时间桶粒度"""
        granularities = TimeRegistry.get_all_granularities()
        assert len(granularities) == 6


class TestTimelineModels:
    """时间线模型测试"""
    
    def test_timeline_node_creation(self):
        """测试时间线节点创建"""
        bucket = TimeBucket.from_date(date(2025, 3, 1), TimeBucketGranularity.QUARTER)
        node = TimelineNode(
            node_id="node_2025Q1",
            bucket=bucket,
            domain_scores={"career": 0.8, "health": 0.7},
            confidence=0.75,
        )
        assert node.node_id == "node_2025Q1"
        assert node.domain_scores["career"] == 0.8
    
    def test_branch_point_creation(self):
        """测试分支点创建"""
        bucket = TimeBucket.from_date(date(2025, 6, 1), TimeBucketGranularity.QUARTER)
        point = BranchPoint(
            point_id="bp_001",
            bucket=bucket,
            decision_question="是否接受新工作机会？",
            options=["接受", "拒绝", "协商条件"],
            recommendation="接受",
        )
        assert len(point.options) == 3
        assert point.decision_question == "是否接受新工作机会？"
