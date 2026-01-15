"""
Test Fixtures

测试夹具，提供测试数据构建和 mock 工具。

对照 design.md §2.1 目录结构
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional
from unittest.mock import MagicMock

from pydantic import BaseModel


class MockRuleResult:
    """Mock 规则结果"""
    
    def __init__(
        self,
        rule_id: str = "test_rule",
        hit: bool = True,
        dimension: str = "事业",
        level: str = "吉",
        confidence: float = 0.8,
        **kwargs,
    ):
        self.rule_id = rule_id
        self.hit = hit
        self.matched = hit  # 别名
        self.dimension = dimension
        self.level = level
        self.confidence = confidence
        for k, v in kwargs.items():
            setattr(self, k, v)


class MockFusionResult:
    """Mock 融合结果"""
    
    def __init__(
        self,
        themes: Optional[List[str]] = None,
        cross_validation_score: float = 0.85,
        engine_results: Optional[Dict[str, Any]] = None,
        **kwargs,
    ):
        self.themes = themes or ["事业发展", "财富积累"]
        self.cross_validation_score = cross_validation_score
        self.engine_results = engine_results or {}
        for k, v in kwargs.items():
            setattr(self, k, v)


class TestFixtures:
    """
    测试夹具工厂
    
    提供创建测试数据的便捷方法。
    """
    
    # =========================================================================
    # 因子数据
    # =========================================================================
    
    @staticmethod
    def mock_factors(
        engine_id: str = "bazi",
        **overrides,
    ) -> Dict[str, Any]:
        """
        创建 mock 因子数据
        
        Args:
            engine_id: 引擎ID
            **overrides: 覆盖默认值
            
        Returns:
            因子字典
        """
        defaults = {
            "bazi": {
                "day_master": "甲",
                "day_branch": "子",
                "month_stem": "丙",
                "month_branch": "寅",
                "year_stem": "壬",
                "year_branch": "寅",
                "hour_stem": "甲",
                "hour_branch": "子",
                "season": "spring",
                "day_master_strength": "strong",
            },
            "ziwei": {
                "ming_gong": "子",
                "shen_gong": "午",
                "zi_wei_star": "紫微",
                "tian_fu_star": "天府",
            },
            "astro": {
                "sun_sign": "aries",
                "moon_sign": "taurus",
                "ascendant": "gemini",
                "sun_house": 1,
                "moon_house": 2,
            },
            "dream": {
                "symbol": "water",
                "emotion": "calm",
                "setting": "nature",
            },
        }
        
        base = defaults.get(engine_id, {}).copy()
        base.update(overrides)
        return base
    
    @staticmethod
    def mock_factor_matrix(
        engine_id: str = "bazi",
        factors: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        创建 mock FactorMatrix 数据
        
        Args:
            engine_id: 引擎ID
            factors: 因子数据 (如不提供则使用默认值)
            
        Returns:
            FactorMatrix 兼容的字典
        """
        if factors is None:
            factors = TestFixtures.mock_factors(engine_id)
        
        return {
            "engine_id": engine_id,
            "factors": factors,
            "computed_at": datetime.now().isoformat(),
            "source": "test_fixtures",
        }
    
    # =========================================================================
    # 出生数据
    # =========================================================================
    
    @staticmethod
    def mock_birth_data(
        year: int = 1990,
        month: int = 3,
        day: int = 15,
        hour: int = 10,
        minute: int = 30,
        timezone: str = "Asia/Shanghai",
        longitude: float = 121.4737,
        latitude: float = 31.2304,
        **overrides,
    ) -> Dict[str, Any]:
        """
        创建 mock 出生数据
        
        Args:
            year, month, day, hour, minute: 出生时间
            timezone: 时区
            longitude, latitude: 出生地经纬度
            **overrides: 覆盖默认值
            
        Returns:
            出生数据字典
        """
        data = {
            "year": year,
            "month": month,
            "day": day,
            "hour": hour,
            "minute": minute,
            "timezone": timezone,
            "longitude": longitude,
            "latitude": latitude,
        }
        data.update(overrides)
        return data
    
    # =========================================================================
    # 规则测试用例
    # =========================================================================
    
    @staticmethod
    def mock_rule_test_case(
        test_id: str = "test_rule_001",
        target_rule_id: str = "dts_jia_spring_001",
        test_type: str = "positive",
        mock_factors: Optional[Dict[str, Any]] = None,
        expect_hit: bool = True,
        expected_dimension: str = "事业",
        expected_level: str = "吉",
        expected_confidence_min: float = 0.7,
        expected_confidence_max: float = 1.0,
        source_book: str = "ditianshui",
        description: str = "Test case",
        **overrides,
    ) -> Dict[str, Any]:
        """
        创建 mock RuleTestCase 数据
        
        Returns:
            RuleTestCase 兼容的字典
        """
        data = {
            "test_id": test_id,
            "target_rule_id": target_rule_id,
            "test_type": test_type,
            "mock_factors": mock_factors or TestFixtures.mock_factors("bazi"),
            "expect_hit": expect_hit,
            "expected_dimension": expected_dimension,
            "expected_level": expected_level,
            "expected_confidence_min": expected_confidence_min,
            "expected_confidence_max": expected_confidence_max,
            "source_book": source_book,
            "description": description,
        }
        data.update(overrides)
        return data
    
    # =========================================================================
    # 黄金用例
    # =========================================================================
    
    @staticmethod
    def mock_golden_case(
        case_id: str = "golden_bazi_001",
        birth_data: Optional[Dict[str, Any]] = None,
        expected_results: Optional[Dict[str, Any]] = None,
        expected_fusion: Optional[Dict[str, Any]] = None,
        max_drift: float = 0.1,
        baseline_hash: Optional[str] = None,
        **overrides,
    ) -> Dict[str, Any]:
        """
        创建 mock GoldenCase 数据
        
        Returns:
            GoldenCase 兼容的字典
        """
        data = {
            "case_id": case_id,
            "birth_data": birth_data or TestFixtures.mock_birth_data(),
            "expected_results": expected_results or {
                "bazi_rule_engine": {"hit_count": 5, "top_dimensions": ["事业", "财富"]},
            },
            "expected_fusion": expected_fusion or {
                "primary_themes": ["事业突破"],
                "cross_validation_score": 0.85,
            },
            "max_drift": max_drift,
            "baseline_hash": baseline_hash,
        }
        data.update(overrides)
        return data
    
    # =========================================================================
    # 叙事黄金标准
    # =========================================================================
    
    @staticmethod
    def mock_narrative_golden(
        golden_id: str = "narrative_career_001",
        scenario: Optional[Dict[str, Any]] = None,
        must_include_themes: Optional[List[str]] = None,
        forbidden_expressions: Optional[List[str]] = None,
        min_quality_score: float = 0.8,
        eval_model: str = "gpt-4o-mini",
        historical_avg_score: float = 0.85,
        **overrides,
    ) -> Dict[str, Any]:
        """
        创建 mock NarrativeGolden 数据
        
        Returns:
            NarrativeGolden 兼容的字典
        """
        data = {
            "golden_id": golden_id,
            "scenario": scenario or {
                "user_type": "career_seeker",
                "question": "今年事业发展如何？",
                "engines": ["bazi", "tarot"],
            },
            "must_include_themes": must_include_themes or ["事业发展", "行动建议"],
            "forbidden_expressions": forbidden_expressions or ["命中注定", "绝对会"],
            "min_quality_score": min_quality_score,
            "eval_model": eval_model,
            "historical_avg_score": historical_avg_score,
        }
        data.update(overrides)
        return data
    
    # =========================================================================
    # Mock 对象
    # =========================================================================
    
    @staticmethod
    def mock_rule_engine() -> MagicMock:
        """创建 mock RuleEngine"""
        engine = MagicMock()
        engine.execute.return_value = [MockRuleResult()]
        engine.execute_single.return_value = MockRuleResult()
        return engine
    
    @staticmethod
    def mock_fusion_engine() -> MagicMock:
        """创建 mock FusionEngine"""
        engine = MagicMock()
        engine.fuse.return_value = MockFusionResult()
        return engine
    
    @staticmethod
    def mock_llm_client() -> MagicMock:
        """创建 mock LLMClient"""
        client = MagicMock()
        client.complete.return_value = MagicMock(content="Mock response")
        client.complete_json.return_value = {"score": 0.9, "feedback": "Good"}
        return client
