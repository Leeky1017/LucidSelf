"""
TOON Serializer Tests

对照 requirements.md 2.1.1-2.3.3
对照 pitfalls.md 2.1, 2.2
"""

import pytest
from hypothesis import given, strategies as st, settings

from backend.core.contracts import RuntimeRuleResult, FusionResult
from backend.core.llm.toon_serializer import TOONSerializer, TOONParser


@pytest.fixture
def serializer():
    return TOONSerializer()


@pytest.fixture
def parser():
    return TOONParser()


@pytest.fixture
def sample_rule_result():
    return RuntimeRuleResult(
        rule_id="bazi_career_001",
        matched=True,
        dimension="事业",
        level="吉",
        confidence=0.85,
        weight=1.5,
        tags=["官印相生"],
        evidence_factors=["ten_god_zhengguan", "ten_god_zhengyin", "day_master"],
        execution_time_ms=1.2,
    )


@pytest.fixture
def sample_fusion_result(sample_rule_result):
    return FusionResult(
        fusion_id="fus_abc123456789",  # 12 位 hex
        primary_themes=["事业突破", "财富积累", "人际和谐"],
        evidence_chain=[sample_rule_result],
        cross_validation_score=0.87,
        confidence_matrix={"career": 0.85},
        conflicts=[],
        contributing_engines=["bazi", "astro"],
        fusion_time_ms=15.0,
    )


class TestTOONSerializerRule:
    """TOON 规则序列化测试"""
    
    def test_serialize_rule_basic(self, serializer, sample_rule_result):
        """测试基本规则序列化"""
        toon = serializer.serialize_rule(sample_rule_result)
        
        assert "bazi_career_001" in toon
        assert "C" in toon  # 事业 → C
        assert "+" in toon  # 吉 → +
        assert "0.85" in toon
    
    def test_serialize_rule_format(self, serializer, sample_rule_result):
        """测试规则格式"""
        toon = serializer.serialize_rule(sample_rule_result)
        
        # 格式: rid:dim/lvl/conf/factors
        parts = toon.split(":")
        assert len(parts) == 2
        assert parts[0] == "bazi_career_001"
        
        details = parts[1].split("/")
        assert len(details) >= 3
    
    def test_serialize_rule_with_missing_fields(self, serializer):
        """测试缺失字段的规则序列化"""
        result = RuntimeRuleResult(
            rule_id="test_001",
            matched=True,
            confidence=0.5,
            weight=1.0,
            execution_time_ms=0.0,
        )
        
        toon = serializer.serialize_rule(result)
        
        assert "test_001" in toon
        # 应该不会崩溃


class TestTOONSerializerFusion:
    """TOON 融合结果序列化测试"""
    
    def test_serialize_fusion_basic(self, serializer, sample_fusion_result):
        """测试基本融合序列化"""
        toon = serializer.serialize_fusion(sample_fusion_result)
        
        assert "T:" in toon  # 主题行
        assert "事业突破" in toon
        assert "XV:0.87" in toon  # 交叉验证
        assert "CF:0" in toon  # 冲突数
    
    def test_serialize_fusion_themes(self, serializer, sample_fusion_result):
        """测试主题序列化"""
        toon = serializer.serialize_fusion(sample_fusion_result)
        
        lines = toon.split("\n")
        theme_line = [l for l in lines if l.startswith("T:")][0]
        
        assert "|" in theme_line
        assert "事业突破" in theme_line
    
    def test_serialize_fusion_max_length(self, serializer):
        """测试最大长度限制"""
        # 创建很长的融合结果
        long_result = FusionResult(
            fusion_id="fus_abcdef123456",  # 12 位 hex
            primary_themes=["主题" * 100] * 5,
            evidence_chain=[
                RuntimeRuleResult(
                    rule_id=f"rule_{i:03d}",
                    matched=True,
                    confidence=0.5,
                    weight=1.0,
                    execution_time_ms=0.0,
                    evidence_factors=["factor"] * 20,
                )
                for i in range(20)  # FusionResult 最多 20 条证据
            ],
            cross_validation_score=0.5,
            confidence_matrix={},
            conflicts=[],
            contributing_engines=["test"],
            fusion_time_ms=1.0,
        )
        
        toon = serializer.serialize_fusion(long_result)
        
        # 应该被截断
        assert len(toon) <= serializer.MAX_BODY_LENGTH


class TestTOONSerializerFactorMatrix:
    """TOON 因子矩阵序列化测试"""
    
    def test_serialize_factor_matrix(self, serializer):
        """测试因子矩阵序列化"""
        factors = {
            "day_master": "jia",
            "season": "spring",
            "strength": 0.75,
        }
        
        toon = serializer.serialize_factor_matrix(factors)
        
        assert "dm" in toon or "day_master"[:3] in toon
        assert ":" in toon
        assert "," in toon


class TestTOONParser:
    """TOON 解析器测试"""
    
    def test_parse_rule_basic(self, parser):
        """测试基本规则解析"""
        toon = "bazi_career_001:C/+/0.85/zg,dm"
        
        result = parser.parse_rule(toon)
        
        assert result.rule_id == "bazi_career_001"
        assert result.confidence == 0.85
    
    def test_parse_rule_graceful_degradation(self, parser):
        """测试解析降级"""
        # 格式不完整
        toon = "broken_rule"
        
        result = parser.parse_rule(toon)
        
        # 应该返回降级结果，不崩溃
        assert result is not None
        assert result.matched is True
    
    def test_parse_fusion_basic(self, parser):
        """测试融合解析"""
        toon = """T:事业突破|财富积累
bazi_001:C/+/0.85/dm
XV:0.87
CF:0"""
        
        result = parser.parse_fusion(toon)
        
        assert "事业突破" in result["themes"]
        assert result["cross_validation_score"] == 0.87
        assert result["conflicts_count"] == 0


class TestTOONRoundTrip:
    """TOON 往返测试"""
    
    def test_rule_round_trip_key_fields(self, serializer, parser, sample_rule_result):
        """测试规则往返 - 关键字段"""
        toon = serializer.serialize_rule(sample_rule_result)
        parsed = parser.parse_rule(toon)
        
        # 关键字段必须精确
        assert parsed.rule_id == sample_rule_result.rule_id
        
        # 置信度允许精度损失
        assert abs(parsed.confidence - sample_rule_result.confidence) < 0.01
    
    @given(
        rule_id=st.text(min_size=1, max_size=50, alphabet="abcdefghijklmnopqrstuvwxyz0123456789_"),
        confidence=st.floats(min_value=0.0, max_value=1.0, allow_nan=False),
    )
    @settings(max_examples=20)
    def test_rule_round_trip_property(self, rule_id, confidence):
        """属性测试: 规则往返"""
        serializer = TOONSerializer()
        parser = TOONParser()
        
        result = RuntimeRuleResult(
            rule_id=rule_id,
            matched=True,
            confidence=confidence,
            weight=1.0,
            execution_time_ms=0.0,
        )
        
        toon = serializer.serialize_rule(result)
        parsed = parser.parse_rule(toon)
        
        # rule_id 必须精确
        assert parsed.rule_id == rule_id
        
        # 置信度允许精度损失 (2 位小数)
        assert abs(parsed.confidence - round(confidence, 2)) < 0.01


class TestTOONPayload:
    """ToonPayload 测试"""
    
    def test_to_payload_rule(self, serializer, sample_rule_result):
        """测试创建规则 Payload"""
        body = serializer.serialize_rule(sample_rule_result)
        payload = serializer.to_payload("rule", body)
        
        assert payload.version == "1"
        assert payload.kind == "rule"
        assert len(payload.body) <= 1000
    
    def test_to_payload_fusion(self, serializer, sample_fusion_result):
        """测试创建融合 Payload"""
        body = serializer.serialize_fusion(sample_fusion_result)
        payload = serializer.to_payload("fusion", body)
        
        assert payload.kind == "fusion"
    
    def test_serialize_to_payload_auto_detect(self, serializer, sample_rule_result):
        """测试自动检测类型"""
        payload = serializer.serialize_to_payload(sample_rule_result)
        
        assert payload.kind == "rule"
