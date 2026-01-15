# backend/tests/test_toon_v2.py
"""
TOON v2 Serializer Tests

测试 TOON v2 格式的序列化和解析。

审计修复: 补充 TOON v2 测试覆盖
参考 tasks.md Phase 3
"""

import pytest
from unittest.mock import MagicMock
from datetime import datetime

from backend.core.llm.toon_serializer import TOONSerializer, TOONParser
from backend.core.contracts import RuntimeRuleResult, FusionResult


class TestTOONSerializerV2:
    """TOON v2 序列化测试"""
    
    @pytest.fixture
    def serializer(self):
        return TOONSerializer()
    
    @pytest.fixture
    def mock_fusion_result(self):
        """Mock FusionResult - 使用 MagicMock 避免严格验证"""
        fusion = MagicMock()
        fusion.fusion_id = "fus_test1234567"
        fusion.primary_themes = ["career", "wealth", "health"]
        fusion.evidence_chain = [
            RuntimeRuleResult(
                rule_id="rule_001",
                matched=True,
                dimension="career",
                level="strong",
                confidence=0.85,
                weight=1.0,
                evidence_factors=["day_master", "season"],
                execution_time_ms=1.0,
            ),
        ]
        fusion.cross_validation_score = 0.78
        fusion.conflicts = []
        fusion.confidence_matrix = {"career": 0.85}
        fusion.fusion_time_ms = 10.5
        return fusion
    
    @pytest.fixture
    def mock_bazi_factors(self):
        """Mock BaziFactors - 使用字典访问方式"""
        factors = MagicMock()
        # four_pillars 使用字典访问 p['year']['stem']
        factors.four_pillars = {
            'year': {'stem': '甲', 'branch': '子'},
            'month': {'stem': '丙', 'branch': '寅'},
            'day': {'stem': '戊', 'branch': '辰'},
            'hour': {'stem': '庚', 'branch': '午'},
        }
        factors.day_master = "戊土"
        factors.day_master_element = "土"
        factors.day_master_yinyang = "阳"
        factors.day_master_strength = 0.65
        factors.strength_category = "中和"
        factors.ten_god_counts = {"正财": 2, "偏财": 1, "正官": 1}
        factors.dayun_list = []
        factors.start_dayun_age = 3
        factors.birth_season = "春"
        return factors
    
    @pytest.fixture
    def mock_astro_factors(self):
        """Mock AstroFactors - 需要 sign, house, degree_in_sign"""
        factors = MagicMock()
        
        # 行星需要 sign, house, degree_in_sign 属性
        sun = MagicMock()
        sun.sign = "Leo"
        sun.house = 5
        sun.degree_in_sign = 15.5
        
        moon = MagicMock()
        moon.sign = "Cancer"
        moon.house = 4
        moon.degree_in_sign = 22.3
        
        factors.planets = {"sun": sun, "moon": moon}
        factors.ascendant_sign = "Aries"
        factors.midheaven_sign = "Capricorn"
        factors.aspects = []
        factors.retrograde = []
        return factors
    
    # =========================================================================
    # serialize_full_v2 测试
    # =========================================================================
    
    def test_serialize_full_v2_structure(self, serializer, mock_fusion_result, mock_bazi_factors):
        """测试 V2 格式结构"""
        raw_factors = {"bazi-calculator": mock_bazi_factors}
        
        result = serializer.serialize_full_v2(mock_fusion_result, raw_factors)
        
        # 验证版本头
        assert result.startswith("V:2")
        
        # 验证引擎列表
        assert "E:bazi" in result
        
        # 验证八字块 (BZ.P: 格式)
        assert "BZ.P:" in result
    
    def test_serialize_full_v2_multi_engine(
        self, serializer, mock_fusion_result, mock_bazi_factors, mock_astro_factors
    ):
        """测试多体系序列化"""
        raw_factors = {
            "bazi-calculator": mock_bazi_factors,
            "astro-calculator": mock_astro_factors,
        }
        
        result = serializer.serialize_full_v2(mock_fusion_result, raw_factors)
        
        # 验证引擎列表包含两个
        assert "E:bazi,astro" in result or "E:astro,bazi" in result
        
        # 验证两个体系块都存在 (BZ.P: 和 AS.SUN: 格式)
        assert "BZ.P:" in result
        assert "AS.SUN:" in result
    
    def test_serialize_full_v2_with_insights(self, serializer, mock_fusion_result, mock_bazi_factors):
        """测试带洞察的序列化"""
        raw_factors = {"bazi-calculator": mock_bazi_factors}
        
        # Mock insights
        insight = MagicMock()
        insight.dimension = "behavior"
        insight.strength = 0.85
        insight.summary = "用户倾向于计划性工作"
        insight.related_factors = ["factor1", "factor2"]
        
        result = serializer.serialize_full_v2(mock_fusion_result, raw_factors, insights=[insight])
        
        # 验证洞察行
        assert "INS:behavior" in result
    
    def test_serialize_full_v2_truncation(self, serializer, mock_fusion_result):
        """测试超长截断"""
        # 创建超长因子
        mock_factors = MagicMock()
        mock_factors.four_pillars = MagicMock()
        mock_factors.four_pillars.year = MagicMock(stem="甲", branch="子")
        mock_factors.four_pillars.month = MagicMock(stem="丙", branch="寅")
        mock_factors.four_pillars.day = MagicMock(stem="戊", branch="辰")
        mock_factors.four_pillars.hour = MagicMock(stem="庚", branch="午")
        mock_factors.day_master = MagicMock(element="土", polarity="阳")
        mock_factors.ten_gods = {f"神煞_{i}": 1 for i in range(100)}  # 大量十神
        mock_factors.dayun = []
        
        raw_factors = {"bazi-calculator": mock_factors}
        
        result = serializer.serialize_full_v2(mock_fusion_result, raw_factors)
        
        # 验证结果长度不超过限制
        assert len(result) <= serializer.MAX_V2_BODY_LENGTH
    
    # =========================================================================
    # serialize_bazi_v2 测试
    # =========================================================================
    
    def test_serialize_bazi_v2_format(self, serializer, mock_bazi_factors):
        """测试八字 V2 格式"""
        result = serializer.serialize_bazi_v2(mock_bazi_factors)
        
        # 验证 BZ.P: 四柱前缀
        assert result.startswith("BZ.P:")
        
        # 验证四柱信息
        assert "甲子" in result
        assert "丙寅" in result
        assert "戊辰" in result
        assert "庚午" in result
    
    def test_serialize_bazi_v2_missing_data(self, serializer):
        """测试缺失数据的处理"""
        empty_factors = MagicMock()
        empty_factors.four_pillars = None
        empty_factors.day_master = None
        empty_factors.ten_gods = {}
        empty_factors.dayun = []
        
        result = serializer.serialize_bazi_v2(empty_factors)
        
        # 应返回空或带默认值的结果
        assert result == "" or "BZ:" in result
    
    # =========================================================================
    # serialize_astro_v2 测试
    # =========================================================================
    
    def test_serialize_astro_v2_format(self, serializer, mock_astro_factors):
        """测试占星 V2 格式"""
        result = serializer.serialize_astro_v2(mock_astro_factors)
        
        # 验证 AS.SUN: 前缀 (太阳行)
        assert result.startswith("AS.SUN:")
        
        # 验证行星信息
        assert "Leo" in result  # 太阳星座
    
    # =========================================================================
    # 边界条件测试
    # =========================================================================
    
    def test_empty_raw_factors(self, serializer, mock_fusion_result):
        """测试空因子"""
        result = serializer.serialize_full_v2(mock_fusion_result, {})
        
        # 应有版本头和融合结果
        assert "V:2" in result
        assert "T:" in result  # 主题行
    
    def test_unknown_engine(self, serializer, mock_fusion_result):
        """测试未知引擎"""
        unknown_factors = MagicMock()
        raw_factors = {"unknown-engine": unknown_factors}
        
        result = serializer.serialize_full_v2(mock_fusion_result, raw_factors)
        
        # 应正常生成，跳过未知引擎
        assert "V:2" in result
        assert "E:unknown" in result


class TestTOONParser:
    """TOON 解析测试"""
    
    @pytest.fixture
    def parser(self):
        return TOONParser()
    
    def test_parse_rule_basic(self, parser):
        """测试基本规则解析"""
        toon = "rule_001:C/+/0.85/dm,sn"
        
        result = parser.parse_rule(toon)
        
        assert result.rule_id == "rule_001"
        assert result.confidence == 0.85
        assert result.matched is True
    
    def test_parse_rule_missing_factors(self, parser):
        """测试缺少因子的规则"""
        toon = "rule_002:W/0/0.50/"
        
        result = parser.parse_rule(toon)
        
        assert result.rule_id == "rule_002"
        assert result.confidence == 0.50
    
    def test_parse_fusion_basic(self, parser):
        """测试基本融合解析"""
        toon = """T:career|wealth|health
rule_001:C/+/0.85/dm,sn
XV:0.78
CF:0"""
        
        result = parser.parse_fusion(toon)
        
        assert result["themes"] == ["career", "wealth", "health"]
        assert result["cross_validation_score"] == 0.78
        assert result["conflicts_count"] == 0
        assert len(result["rules"]) == 1
    
    def test_parse_invalid_toon(self, parser):
        """测试无效 TOON 格式"""
        toon = "invalid format without proper structure"
        
        result = parser.parse_rule(toon)
        
        # 应返回降级结果
        assert result.matched is True
        assert result.confidence == 0.0


class TestTOONRoundTrip:
    """TOON 序列化/解析往返测试"""
    
    def test_rule_roundtrip(self):
        """测试规则往返"""
        serializer = TOONSerializer()
        parser = TOONParser()
        
        original = RuntimeRuleResult(
            rule_id="test_rule_123",
            matched=True,
            dimension="career",
            level="strong",
            confidence=0.88,
            weight=1.0,
            evidence_factors=["day_master", "season"],
            execution_time_ms=1.5,
        )
        
        # 序列化
        toon = serializer.serialize_rule(original)
        
        # 解析
        parsed = parser.parse_rule(toon)
        
        # 验证关键字段
        assert parsed.rule_id == original.rule_id
        assert abs(parsed.confidence - original.confidence) < 0.01
