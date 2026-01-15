"""
Tests for Test Data Generators

测试数据生成器测试。
"""

import pytest

from backend.testing.generators.rule_generator import RuleTestCaseGenerator
from backend.testing.generators.golden_generator import (
    GoldenCaseGenerator,
    ScenarioLibrary,
)


class TestRuleTestCaseGenerator:
    """RuleTestCaseGenerator 测试"""
    
    def test_generate_positive_case(self):
        """测试生成正向用例"""
        gen = RuleTestCaseGenerator()
        
        case = gen.generate_positive_case(
            rule_id="bazi_r001",
            engine="bazi",
            expected_dimension="事业",
            expected_level="high",
        )
        
        assert case.test_id.startswith("pos_bazi_r001_")
        assert case.target_rule_id == "bazi_r001"
        assert case.test_type == "positive"
        assert case.expect_hit is True
        assert case.expected_dimension == "事业"
        assert len(case.mock_factors) > 0
    
    def test_generate_negative_case(self):
        """测试生成负向用例"""
        gen = RuleTestCaseGenerator()
        
        case = gen.generate_negative_case(
            rule_id="bazi_r002",
            engine="bazi",
        )
        
        assert case.test_id.startswith("neg_bazi_r002_")
        assert case.test_type == "negative"
        assert case.expect_hit is False
    
    def test_generate_edge_case_boundary(self):
        """测试生成边界用例"""
        gen = RuleTestCaseGenerator()
        
        case = gen.generate_edge_case(
            rule_id="bazi_r003",
            engine="bazi",
            edge_type="boundary",
        )
        
        assert case.test_id.startswith("edge_bazi_r003_boundary_")
        assert case.test_type == "edge"
    
    def test_generate_edge_case_empty(self):
        """测试生成空值用例"""
        gen = RuleTestCaseGenerator()
        
        case = gen.generate_edge_case(
            rule_id="bazi_r004",
            engine="bazi",
            edge_type="empty",
        )
        
        assert case.test_type == "edge"
        # 检查因子值为空
        for v in case.mock_factors.values():
            assert v == ""
    
    def test_generate_pairwise_cases(self):
        """测试生成配对组合用例"""
        gen = RuleTestCaseGenerator()
        
        cases = gen.generate_pairwise_cases(
            rule_id="bazi_r005",
            engine="bazi",
            max_cases=10,
        )
        
        assert len(cases) == 10
        for case in cases:
            assert case.test_id.startswith("pair_bazi_r005_")
    
    def test_different_engines(self):
        """测试不同引擎"""
        gen = RuleTestCaseGenerator()
        
        bazi_case = gen.generate_positive_case("r001", engine="bazi")
        ziwei_case = gen.generate_positive_case("r002", engine="ziwei")
        astro_case = gen.generate_positive_case("r003", engine="astro")
        
        # 检查因子不同
        assert "day_master" in bazi_case.mock_factors
        assert "main_star" in ziwei_case.mock_factors
        assert "sun_sign" in astro_case.mock_factors


class TestGoldenCaseGenerator:
    """GoldenCaseGenerator 测试"""
    
    def test_generate_golden_case(self):
        """测试生成黄金用例"""
        gen = GoldenCaseGenerator()
        
        case = gen.generate_golden_case(scenario_name="career_analysis")
        
        assert case.case_id.startswith("golden_career_analysis_")
        assert "year" in case.birth_data
        assert "month" in case.birth_data
        assert len(case.expected_results) > 0
        assert "themes" in case.expected_fusion
        assert case.baseline_hash is not None
    
    def test_generate_with_custom_birth_data(self):
        """测试使用自定义出生数据"""
        gen = GoldenCaseGenerator()
        
        birth_data = {
            "year": 1990,
            "month": 6,
            "day": 15,
            "hour": 10,
            "minute": 30,
            "gender": "male",
        }
        
        case = gen.generate_golden_case(birth_data=birth_data)
        
        assert case.birth_data["year"] == 1990
        assert case.birth_data["month"] == 6
    
    def test_generate_narrative_golden(self):
        """测试生成叙事黄金标准"""
        gen = GoldenCaseGenerator()
        
        golden = gen.generate_narrative_golden(
            scenario_name="career_analysis",
            must_include_themes=["事业", "职场"],
        )
        
        assert golden.golden_id.startswith("narrative_career_analysis_")
        assert "事业" in golden.must_include_themes
        assert len(golden.forbidden_expressions) > 0
        assert golden.min_quality_score == 0.8
    
    def test_update_baseline(self):
        """测试更新基线"""
        gen = GoldenCaseGenerator()
        
        original = gen.generate_golden_case()
        
        new_results = {"bazi": {"status": "success", "rules_hit": 5}}
        new_fusion = {"themes": ["财运"], "cross_validation_score": 0.9}
        
        updated = gen.update_baseline(original, new_results, new_fusion)
        
        assert updated.case_id == original.case_id
        assert updated.expected_results == new_results
        assert updated.baseline_hash != original.baseline_hash
    
    def test_baseline_hash_consistency(self):
        """测试基线哈希一致性"""
        gen = GoldenCaseGenerator()
        
        results = {"bazi": {"rules_hit": 5}}
        fusion = {"themes": ["事业"]}
        
        hash1 = gen._compute_baseline_hash(results, fusion)
        hash2 = gen._compute_baseline_hash(results, fusion)
        
        assert hash1 == hash2


class TestScenarioLibrary:
    """ScenarioLibrary 测试"""
    
    def test_get_all_scenarios(self):
        """测试获取所有场景"""
        scenarios = ScenarioLibrary.get_all_scenarios()
        
        assert len(scenarios) > 0
        for s in scenarios:
            assert "query" in s
            assert "themes" in s
    
    def test_get_career_scenarios(self):
        """测试获取事业场景"""
        scenarios = ScenarioLibrary.get_scenario_by_category("career")
        
        assert len(scenarios) > 0
        for s in scenarios:
            assert any("事业" in t or "职场" in t or "工作" in t for t in s["themes"])
    
    def test_get_relationship_scenarios(self):
        """测试获取感情场景"""
        scenarios = ScenarioLibrary.get_scenario_by_category("relationship")
        
        assert len(scenarios) > 0
    
    def test_get_health_scenarios(self):
        """测试获取健康场景"""
        scenarios = ScenarioLibrary.get_scenario_by_category("health")
        
        assert len(scenarios) > 0
    
    def test_unknown_category(self):
        """测试未知类别"""
        scenarios = ScenarioLibrary.get_scenario_by_category("unknown")
        
        assert scenarios == []


class TestIntegration:
    """集成测试"""
    
    def test_module_exports(self):
        """测试模块导出"""
        from backend.testing.generators import (
            RuleTestCaseGenerator,
            GoldenCaseGenerator,
            ScenarioLibrary,
        )
        
        assert RuleTestCaseGenerator is not None
        assert GoldenCaseGenerator is not None
        assert ScenarioLibrary is not None
