# backend/tests/unit/test_toon_ins_line.py
"""
WP-02: TOON v2 INS 行测试

测试目标：
1. INS 行最多 5 条
2. 格式严格：INS:{dimension}/{strength}/{summary}/{factors_count}
3. / 字符转义不破坏解析
"""

import re
import pytest
from dataclasses import dataclass
from typing import List, Optional
from unittest.mock import MagicMock

from backend.core.llm.toon_serializer import TOONSerializer


@dataclass
class MockInsight:
    """模拟洞察对象"""
    dimension: str
    strength: float
    summary: str
    related_factors: List[str]


# INS 行正则解析器
INS_LINE_PATTERN = re.compile(
    r'^INS:([^/]+)/(\d+\.\d{2})/([^/]*)/(\d+)$'
)


def parse_ins_line(line: str) -> Optional[dict]:
    """解析 INS 行，返回字段字典或 None"""
    match = INS_LINE_PATTERN.match(line)
    if match:
        return {
            "dimension": match.group(1),
            "strength": float(match.group(2)),
            "summary": match.group(3),
            "factors_count": int(match.group(4)),
        }
    return None


class TestTOONInsLineCount:
    """INS 行数量测试"""
    
    @pytest.fixture
    def serializer(self):
        return TOONSerializer()
    
    def test_ins_line_max_5(self, serializer):
        """测试：传入 7 条洞察，输出 INS 行数量=5"""
        insights = [
            MockInsight(
                dimension=f"dim_{i}",
                strength=0.8,
                summary=f"摘要{i}",
                related_factors=[f"factor_{i}"],
            )
            for i in range(7)
        ]
        
        # 创建最小 fusion mock
        fusion = MagicMock()
        fusion.primary_themes = ["主题"]
        fusion.evidence_chain = []
        fusion.cross_validation_score = 0.85
        fusion.conflicts = []
        
        toon_str = serializer.serialize_full_v2(
            fusion=fusion,
            raw_factors={},
            insights=insights,
        )
        
        # 统计 INS 行数量
        ins_lines = [line for line in toon_str.split("\n") if line.startswith("INS:")]
        assert len(ins_lines) == 5, f"INS 行数量应为 5，实际为 {len(ins_lines)}"
    
    def test_ins_line_fewer_than_5(self, serializer):
        """测试：传入少于 5 条洞察时全部输出"""
        insights = [
            MockInsight(
                dimension=f"dim_{i}",
                strength=0.7,
                summary=f"摘要{i}",
                related_factors=[],
            )
            for i in range(3)
        ]
        
        fusion = MagicMock()
        fusion.primary_themes = ["主题"]
        fusion.evidence_chain = []
        fusion.cross_validation_score = 0.85
        fusion.conflicts = []
        
        toon_str = serializer.serialize_full_v2(
            fusion=fusion,
            raw_factors={},
            insights=insights,
        )
        
        ins_lines = [line for line in toon_str.split("\n") if line.startswith("INS:")]
        assert len(ins_lines) == 3, f"INS 行数量应为 3，实际为 {len(ins_lines)}"
    
    def test_no_insights_no_ins_lines(self, serializer):
        """测试：无洞察时无 INS 行"""
        fusion = MagicMock()
        fusion.primary_themes = ["主题"]
        fusion.evidence_chain = []
        fusion.cross_validation_score = 0.85
        fusion.conflicts = []
        
        toon_str = serializer.serialize_full_v2(
            fusion=fusion,
            raw_factors={},
            insights=None,
        )
        
        ins_lines = [line for line in toon_str.split("\n") if line.startswith("INS:")]
        assert len(ins_lines) == 0, f"无洞察时 INS 行数量应为 0，实际为 {len(ins_lines)}"


class TestTOONInsLineFormat:
    """INS 行格式测试"""
    
    @pytest.fixture
    def serializer(self):
        return TOONSerializer()
    
    def test_ins_line_parseable(self, serializer):
        """测试：每条 INS 行可被正则解析"""
        insights = [
            MockInsight(
                dimension="behavior",
                strength=0.85,
                summary="用户行为模式",
                related_factors=["factor_1", "factor_2"],
            ),
            MockInsight(
                dimension="emotion",
                strength=0.72,
                summary="情绪倾向积极",
                related_factors=["factor_3"],
            ),
        ]
        
        fusion = MagicMock()
        fusion.primary_themes = ["主题"]
        fusion.evidence_chain = []
        fusion.cross_validation_score = 0.85
        fusion.conflicts = []
        
        toon_str = serializer.serialize_full_v2(
            fusion=fusion,
            raw_factors={},
            insights=insights,
        )
        
        ins_lines = [line for line in toon_str.split("\n") if line.startswith("INS:")]
        
        for line in ins_lines:
            parsed = parse_ins_line(line)
            assert parsed is not None, f"INS 行解析失败: {line}"
            assert "dimension" in parsed
            assert "strength" in parsed
            assert "summary" in parsed
            assert "factors_count" in parsed
    
    def test_ins_line_field_count(self, serializer):
        """测试：每条 INS 行字段数量=4"""
        insight = MockInsight(
            dimension="test_dim",
            strength=0.9,
            summary="测试摘要",
            related_factors=["f1", "f2", "f3"],
        )
        
        ins_line = serializer._serialize_insight(insight)
        
        # 去掉 INS: 前缀后，应该有 4 个字段
        fields = ins_line.replace("INS:", "").split("/")
        assert len(fields) == 4, f"字段数量应为 4，实际为 {len(fields)}: {fields}"
    
    def test_slash_in_dimension_escaped(self, serializer):
        """测试：dimension 中的 / 字符被转义"""
        insight = MockInsight(
            dimension="work/life",  # 包含 /
            strength=0.8,
            summary="工作生活平衡",
            related_factors=[],
        )
        
        ins_line = serializer._serialize_insight(insight)
        
        # 解析应该成功（/ 被替换为 |）
        parsed = parse_ins_line(ins_line)
        assert parsed is not None, f"包含 / 的 dimension 解析失败: {ins_line}"
        assert "work|life" in parsed["dimension"]
    
    def test_slash_in_summary_escaped(self, serializer):
        """测试：summary 中的 / 字符被转义"""
        insight = MockInsight(
            dimension="behavior",
            strength=0.75,
            summary="工作/生活平衡困难",  # 包含 /
            related_factors=["f1"],
        )
        
        ins_line = serializer._serialize_insight(insight)
        
        # 解析应该成功（/ 被替换为 |）
        parsed = parse_ins_line(ins_line)
        assert parsed is not None, f"包含 / 的 summary 解析失败: {ins_line}"
        assert "/" not in parsed["summary"], f"summary 中仍有 /: {parsed['summary']}"
    
    def test_strength_clamped_to_range(self, serializer):
        """测试：strength 被限制在 0-1 范围"""
        # 超过 1.0
        insight_high = MockInsight(
            dimension="test",
            strength=1.5,
            summary="测试",
            related_factors=[],
        )
        ins_line_high = serializer._serialize_insight(insight_high)
        parsed_high = parse_ins_line(ins_line_high)
        assert parsed_high["strength"] <= 1.0, f"strength 应 ≤1.0: {parsed_high['strength']}"
        
        # 低于 0.0
        insight_low = MockInsight(
            dimension="test",
            strength=-0.5,
            summary="测试",
            related_factors=[],
        )
        ins_line_low = serializer._serialize_insight(insight_low)
        parsed_low = parse_ins_line(ins_line_low)
        assert parsed_low["strength"] >= 0.0, f"strength 应 ≥0.0: {parsed_low['strength']}"
    
    def test_summary_truncated_to_20_chars(self, serializer):
        """测试：summary 被截断到 20 字符"""
        insight = MockInsight(
            dimension="test",
            strength=0.8,
            summary="这是一个很长很长很长很长很长的摘要内容超过二十个字符",
            related_factors=[],
        )
        
        ins_line = serializer._serialize_insight(insight)
        parsed = parse_ins_line(ins_line)
        
        assert len(parsed["summary"]) <= 20, \
            f"summary 长度应 ≤20: {len(parsed['summary'])} ({parsed['summary']})"
    
    def test_factors_count_correct(self, serializer):
        """测试：factors_count 正确反映因子数量"""
        insight = MockInsight(
            dimension="test",
            strength=0.8,
            summary="测试",
            related_factors=["f1", "f2", "f3", "f4", "f5"],
        )
        
        ins_line = serializer._serialize_insight(insight)
        parsed = parse_ins_line(ins_line)
        
        assert parsed["factors_count"] == 5, \
            f"factors_count 应为 5: {parsed['factors_count']}"


class TestSerializeInsightEdgeCases:
    """_serialize_insight 边界情况测试"""
    
    @pytest.fixture
    def serializer(self):
        return TOONSerializer()
    
    def test_empty_summary(self, serializer):
        """测试：空摘要"""
        insight = MockInsight(
            dimension="test",
            strength=0.8,
            summary="",
            related_factors=[],
        )
        
        ins_line = serializer._serialize_insight(insight)
        assert ins_line is not None
        parsed = parse_ins_line(ins_line)
        assert parsed is not None
    
    def test_none_related_factors(self, serializer):
        """测试：related_factors 为 None"""
        insight = MagicMock()
        insight.dimension = "test"
        insight.strength = 0.8
        insight.summary = "测试"
        insight.related_factors = None
        
        ins_line = serializer._serialize_insight(insight)
        assert ins_line is not None
        parsed = parse_ins_line(ins_line)
        assert parsed["factors_count"] == 0
    
    def test_missing_attributes_uses_defaults(self, serializer):
        """测试：缺失属性使用默认值"""
        insight = MagicMock(spec=[])  # 无任何属性
        
        ins_line = serializer._serialize_insight(insight)
        assert ins_line is not None
        parsed = parse_ins_line(ins_line)
        assert parsed["dimension"] == "unknown"
        assert parsed["strength"] == 0.0
