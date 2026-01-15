"""
Tests for Unified Dimensions Module

对照文档: docs/ls_roadmap_executable.md §2.5 验收标准
"""

import pytest

from backend.core.contracts.unified_dimensions import (
    AnalysisDimension,
    ANALYSIS_DIMENSION_LABELS,
    DecisionAxis,
    DimensionRegistry,
    DOMAIN_TO_DIMENSIONS,
    DIMENSION_TO_DOMAINS,
    LifeDomain,
    LIFE_DOMAIN_LABELS,
    CAREER_DECISION_AXES,
    RELATIONSHIP_DECISION_AXES,
    WEALTH_DECISION_AXES,
    HEALTH_DECISION_AXES,
)


class TestLifeDomain:
    """LifeDomain 枚举测试"""
    
    def test_all_domains_defined(self):
        """测试 7 个生活领域全部定义"""
        expected = {"career", "wealth", "relationship", "health", "family", "creativity", "spiritual"}
        actual = {d.value for d in LifeDomain}
        assert actual == expected
    
    def test_all_domains_have_labels(self):
        """测试所有领域都有中英文标签"""
        for domain in LifeDomain:
            assert domain in LIFE_DOMAIN_LABELS
            assert "zh" in LIFE_DOMAIN_LABELS[domain]
            assert "en" in LIFE_DOMAIN_LABELS[domain]
    
    def test_domain_is_string_enum(self):
        """测试领域是字符串枚举（可直接用于 JSON）"""
        assert LifeDomain.CAREER == "career"
        assert LifeDomain.CAREER.value == "career"



class TestAnalysisDimension:
    """AnalysisDimension 枚举测试"""
    
    def test_all_dimensions_defined(self):
        """测试 10 个分析维度全部定义"""
        expected = {
            "career", "health", "marriage", "wealth", "personality",
            "fortune", "omen", "guidance", "unconscious", "general"
        }
        actual = {d.value for d in AnalysisDimension}
        assert actual == expected
    
    def test_all_dimensions_have_labels(self):
        """测试所有维度都有中英文标签"""
        for dim in AnalysisDimension:
            assert dim in ANALYSIS_DIMENSION_LABELS
            assert "zh" in ANALYSIS_DIMENSION_LABELS[dim]
            assert "en" in ANALYSIS_DIMENSION_LABELS[dim]
    
    def test_compatible_with_dimension_py(self):
        """测试与 dimension.py 的 STANDARD_DIMENSIONS 兼容"""
        # dimension.py 定义的 10 个维度
        standard_dimensions = [
            "career", "health", "marriage", "wealth", "personality",
            "fortune", "omen", "guidance", "unconscious", "general"
        ]
        for dim_str in standard_dimensions:
            dim = AnalysisDimension(dim_str)
            assert dim.value == dim_str


class TestDomainDimensionMapping:
    """维度映射关系测试"""
    
    def test_all_domains_have_mapping(self):
        """测试所有领域都有对应的分析维度映射"""
        for domain in LifeDomain:
            assert domain in DOMAIN_TO_DIMENSIONS
            assert len(DOMAIN_TO_DIMENSIONS[domain]) >= 1
    
    def test_reverse_mapping_generated(self):
        """测试反向映射正确生成"""
        # career 维度应该归属于 CAREER 领域
        assert LifeDomain.CAREER in DIMENSION_TO_DOMAINS[AnalysisDimension.CAREER]
        # marriage 维度应该归属于 RELATIONSHIP 和 FAMILY 领域
        assert LifeDomain.RELATIONSHIP in DIMENSION_TO_DOMAINS[AnalysisDimension.MARRIAGE]
        assert LifeDomain.FAMILY in DIMENSION_TO_DOMAINS[AnalysisDimension.MARRIAGE]
    
    def test_general_dimension_has_no_domain(self):
        """测试 GENERAL 维度没有特定归属领域"""
        # general 是通用维度，不归属于任何特定领域
        assert DIMENSION_TO_DOMAINS[AnalysisDimension.GENERAL] == []


class TestDecisionAxis:
    """DecisionAxis 模型测试"""
    
    def test_valid_axis_creation(self):
        """测试有效决策维度创建"""
        axis = DecisionAxis(
            axis_id="income_ceiling",
            label_zh="收入上限",
            label_en="Income Ceiling",
            description="该路径的预期最高收入水平",
        )
        assert axis.axis_id == "income_ceiling"
        assert axis.value_type == "float"
        assert axis.value_range == (0.0, 1.0)
    
    def test_axis_id_pattern_validation(self):
        """测试 axis_id 格式验证"""
        # 有效格式
        DecisionAxis(axis_id="income_ceiling", label_zh="测试", label_en="Test")
        DecisionAxis(axis_id="a", label_zh="测试", label_en="Test")
        DecisionAxis(axis_id="test123", label_zh="测试", label_en="Test")
        
        # 无效格式
        with pytest.raises(ValueError):
            DecisionAxis(axis_id="1invalid", label_zh="测试", label_en="Test")
        with pytest.raises(ValueError):
            DecisionAxis(axis_id="Invalid", label_zh="测试", label_en="Test")
    
    def test_career_axes_defined(self):
        """测试事业决策维度定义"""
        assert len(CAREER_DECISION_AXES) >= 5
        axis_ids = [a.axis_id for a in CAREER_DECISION_AXES]
        assert "income_ceiling" in axis_ids
        assert "stability" in axis_ids
        assert "autonomy" in axis_ids
    
    def test_relationship_axes_defined(self):
        """测试感情决策维度定义"""
        assert len(RELATIONSHIP_DECISION_AXES) >= 4
        axis_ids = [a.axis_id for a in RELATIONSHIP_DECISION_AXES]
        assert "emotional_depth" in axis_ids
        assert "compatibility" in axis_ids


class TestDimensionRegistry:
    """DimensionRegistry 统一接口测试"""
    
    def test_get_life_domain_label_zh(self):
        """测试获取中文生活领域标签"""
        assert DimensionRegistry.get_life_domain_label(LifeDomain.CAREER, "zh") == "事业"
        assert DimensionRegistry.get_life_domain_label(LifeDomain.WEALTH, "zh") == "财富"
        assert DimensionRegistry.get_life_domain_label(LifeDomain.RELATIONSHIP, "zh") == "感情"
        assert DimensionRegistry.get_life_domain_label(LifeDomain.HEALTH, "zh") == "健康"
    
    def test_get_life_domain_label_en(self):
        """测试获取英文生活领域标签"""
        assert DimensionRegistry.get_life_domain_label(LifeDomain.CAREER, "en") == "Career"
        assert DimensionRegistry.get_life_domain_label(LifeDomain.WEALTH, "en") == "Wealth"
    
    def test_get_analysis_dimension_label(self):
        """测试获取分析维度标签"""
        assert DimensionRegistry.get_analysis_dimension_label(AnalysisDimension.CAREER, "zh") == "事业"
        assert DimensionRegistry.get_analysis_dimension_label(AnalysisDimension.MARRIAGE, "zh") == "婚姻"
    
    def test_get_dimensions_for_domain(self):
        """测试获取领域对应的维度"""
        dims = DimensionRegistry.get_dimensions_for_domain(LifeDomain.CAREER)
        assert AnalysisDimension.CAREER in dims
        assert AnalysisDimension.FORTUNE in dims
    
    def test_get_domains_for_dimension(self):
        """测试获取维度对应的领域"""
        domains = DimensionRegistry.get_domains_for_dimension(AnalysisDimension.MARRIAGE)
        assert LifeDomain.RELATIONSHIP in domains
        assert LifeDomain.FAMILY in domains
    
    def test_get_decision_axes_for_domain(self):
        """测试获取领域的决策维度"""
        axes = DimensionRegistry.get_decision_axes_for_domain(LifeDomain.CAREER)
        assert len(axes) >= 5
        assert axes[0].axis_id == "income_ceiling"
    
    def test_normalize_dimension_english(self):
        """测试英文维度名称标准化"""
        assert DimensionRegistry.normalize_dimension("career") == AnalysisDimension.CAREER
        assert DimensionRegistry.normalize_dimension("CAREER") == AnalysisDimension.CAREER
        assert DimensionRegistry.normalize_dimension("Career") == AnalysisDimension.CAREER
        assert DimensionRegistry.normalize_dimension(" career ") == AnalysisDimension.CAREER
    
    def test_normalize_dimension_chinese(self):
        """测试中文维度名称标准化"""
        assert DimensionRegistry.normalize_dimension("事业") == AnalysisDimension.CAREER
        assert DimensionRegistry.normalize_dimension("健康") == AnalysisDimension.HEALTH
        assert DimensionRegistry.normalize_dimension("婚姻") == AnalysisDimension.MARRIAGE
        assert DimensionRegistry.normalize_dimension("财富") == AnalysisDimension.WEALTH
    
    def test_normalize_dimension_unknown(self):
        """测试未知维度名称返回 GENERAL"""
        assert DimensionRegistry.normalize_dimension("unknown") == AnalysisDimension.GENERAL
        assert DimensionRegistry.normalize_dimension("未知维度") == AnalysisDimension.GENERAL
    
    def test_normalize_life_domain_english(self):
        """测试英文生活领域名称标准化"""
        assert DimensionRegistry.normalize_life_domain("career") == LifeDomain.CAREER
        assert DimensionRegistry.normalize_life_domain("wealth") == LifeDomain.WEALTH
    
    def test_normalize_life_domain_chinese(self):
        """测试中文生活领域名称标准化"""
        assert DimensionRegistry.normalize_life_domain("事业") == LifeDomain.CAREER
        assert DimensionRegistry.normalize_life_domain("财富") == LifeDomain.WEALTH
    
    def test_normalize_life_domain_unknown(self):
        """测试未知生活领域返回 None"""
        assert DimensionRegistry.normalize_life_domain("unknown") is None
    
    def test_get_all_life_domains(self):
        """测试获取所有生活领域"""
        domains = DimensionRegistry.get_all_life_domains()
        assert len(domains) == 7
        assert LifeDomain.CAREER in domains
    
    def test_get_all_analysis_dimensions(self):
        """测试获取所有分析维度"""
        dims = DimensionRegistry.get_all_analysis_dimensions()
        assert len(dims) == 10
        assert AnalysisDimension.CAREER in dims
    
    def test_get_playbook_dimensions(self):
        """测试获取 Playbook 维度列表"""
        zh_dims = DimensionRegistry.get_playbook_dimensions("zh")
        assert zh_dims == ["事业", "财富", "感情", "健康"]
        
        en_dims = DimensionRegistry.get_playbook_dimensions("en")
        assert en_dims == ["Career", "Wealth", "Relationship", "Health"]
