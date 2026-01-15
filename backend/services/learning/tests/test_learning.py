"""
Tests for Learning Service

对照文档: docs/ls_roadmap_executable.md §GAP-06
"""

import pytest

from backend.services.learning.factor_updater import (
    FactorUpdater,
    FeedbackRecord,
)
from backend.services.learning.weight_adjuster import WeightAdjuster
from backend.services.learning.global_stats import RuleStatsCollector


class TestFactorUpdater:
    """FactorUpdater 测试"""
    
    @pytest.fixture
    def updater(self):
        return FactorUpdater()
    
    @pytest.fixture
    def positive_feedback(self):
        return FeedbackRecord(
            feedback_id="fb_test12345678",
            user_id="user_001",
            action_item_id="action_001",
            feedback_type="positive",
            rating=5,
            source_factors=["factor_a", "factor_b"],
            source_rules=["rule_001"],
        )
    
    @pytest.fixture
    def negative_feedback(self):
        return FeedbackRecord(
            feedback_id="fb_test87654321",
            user_id="user_001",
            action_item_id="action_002",
            feedback_type="negative",
            rating=1,
            source_factors=["factor_a"],
            source_rules=["rule_002"],
        )
    
    def test_record_positive_feedback(self, updater, positive_feedback):
        """测试记录正面反馈"""
        updater.record_feedback(positive_feedback)
        
        assert updater.get_feedback_count() == 1
        # 正面反馈应该增加权重
        assert updater.get_factor_weight("factor_a") > 1.0
    
    def test_record_negative_feedback(self, updater, negative_feedback):
        """测试记录负面反馈"""
        updater.record_feedback(negative_feedback)
        
        # 负面反馈应该降低权重
        assert updater.get_factor_weight("factor_a") < 1.0
    
    def test_weight_bounded(self, updater, positive_feedback):
        """测试权重边界"""
        # 多次正面反馈
        for _ in range(100):
            updater.record_feedback(positive_feedback)
        
        # 权重不应超过上限
        assert updater.get_factor_weight("factor_a") <= updater.MAX_WEIGHT
    
    def test_adjustments_tracked(self, updater, positive_feedback):
        """测试调整历史追踪"""
        updater.record_feedback(positive_feedback)
        
        adjustments = updater.get_adjustments("factor_a")
        assert len(adjustments) >= 1


class TestWeightAdjuster:
    """WeightAdjuster 测试"""
    
    @pytest.fixture
    def adjuster(self):
        return WeightAdjuster()
    
    def test_record_rule_hit(self, adjuster):
        """测试记录规则命中"""
        adjuster.record_rule_hit("rule_001", "bazi")
        
        weights = adjuster.get_all_rule_weights()
        assert "rule_001" in weights
        assert weights["rule_001"].hit_count == 1
    
    def test_positive_feedback_increases_weight(self, adjuster):
        """测试正面反馈增加权重"""
        adjuster.record_rule_hit("rule_001", "bazi")
        initial = adjuster.get_rule_weight("rule_001")
        
        adjuster.record_rule_feedback("rule_001", is_positive=True)
        
        assert adjuster.get_rule_weight("rule_001") > initial
    
    def test_negative_feedback_decreases_weight(self, adjuster):
        """测试负面反馈降低权重"""
        adjuster.record_rule_hit("rule_001", "bazi")
        initial = adjuster.get_rule_weight("rule_001")
        
        adjuster.record_rule_feedback("rule_001", is_positive=False)
        
        assert adjuster.get_rule_weight("rule_001") < initial
    
    def test_effectiveness_calculated(self, adjuster):
        """测试有效性计算"""
        adjuster.record_rule_hit("rule_001", "bazi")
        adjuster.record_rule_feedback("rule_001", is_positive=True)
        adjuster.record_rule_feedback("rule_001", is_positive=True)
        adjuster.record_rule_feedback("rule_001", is_positive=False)
        
        # 2/3 正面反馈
        effectiveness = adjuster.get_rule_effectiveness("rule_001")
        assert 0.6 <= effectiveness <= 0.7


class TestRuleStatsCollector:
    """RuleStatsCollector 测试"""
    
    @pytest.fixture
    def collector(self):
        return RuleStatsCollector()
    
    def test_record_execution(self, collector):
        """测试记录执行"""
        collector.record_execution("rule_001", "bazi", matched=True)
        
        stats = collector.get_rule_stats("rule_001")
        assert stats is not None
        assert stats.total_executions == 1
        assert stats.hit_count == 1
    
    def test_hit_rate_calculated(self, collector):
        """测试命中率计算"""
        collector.record_execution("rule_001", "bazi", matched=True)
        collector.record_execution("rule_001", "bazi", matched=True)
        collector.record_execution("rule_001", "bazi", matched=False)
        
        stats = collector.get_rule_stats("rule_001")
        # 2/3 命中
        assert 0.6 <= stats.hit_rate <= 0.7
    
    def test_feedback_updates_effectiveness(self, collector):
        """测试反馈更新有效性"""
        collector.record_execution("rule_001", "bazi", matched=True)
        collector.record_feedback("rule_001", is_positive=True)
        collector.record_feedback("rule_001", is_positive=False)
        
        stats = collector.get_rule_stats("rule_001")
        assert stats.effectiveness == 0.5  # 1/2
    
    def test_get_engine_stats(self, collector):
        """测试获取引擎统计"""
        collector.record_execution("rule_001", "bazi", matched=True)
        collector.record_execution("rule_002", "bazi", matched=False)
        
        stats = collector.get_engine_stats("bazi")
        assert stats.total_rules == 2
        assert stats.total_executions == 2
    
    def test_get_global_stats(self, collector):
        """测试获取全局统计"""
        collector.record_execution("rule_001", "bazi", matched=True)
        collector.record_execution("rule_002", "astro", matched=True)
        
        stats = collector.get_global_stats()
        assert stats.total_rules == 2
        assert stats.total_executions == 2
        assert len(stats.engines) == 2
    
    def test_top_and_bottom_rules(self, collector):
        """测试高效/低效规则识别"""
        # 创建不同有效性的规则
        collector.record_execution("rule_high", "bazi", matched=True)
        collector.record_feedback("rule_high", is_positive=True)
        collector.record_feedback("rule_high", is_positive=True)
        
        collector.record_execution("rule_low", "bazi", matched=True)
        collector.record_feedback("rule_low", is_positive=False)
        collector.record_feedback("rule_low", is_positive=False)
        
        top = collector.get_top_rules(1)
        bottom = collector.get_bottom_rules(1)
        
        assert top[0].rule_id == "rule_high"
        assert bottom[0].rule_id == "rule_low"
