"""
Tests for Life Version Generator and Comparator

对照文档: docs/ls_roadmap_executable.md §四、Phase 3: Life Versions 核心
"""

import pytest

from backend.core.contracts.life_version_models import (
    LifeVersion,
    LifeVersionSet,
    VersionComparison,
)
from backend.core.contracts.unified_dimensions import LifeDomain
from backend.services.life_version.generator import LifeVersionGenerator
from backend.services.life_version.comparator import VersionComparator


class MockRuleResult:
    """模拟规则结果"""
    def __init__(
        self, 
        rule_id: str,
        matched: bool = True,
        score: float = 0.6,
        level: str = "中等",
        tags: str = "",
        description: str = "",
    ):
        self.rule_id = rule_id
        self.matched = matched
        self.score = score
        self.level = level
        self.tags = tags
        self.description = description


class TestLifeVersionGenerator:
    """LifeVersionGenerator 测试"""
    
    @pytest.fixture
    def generator(self):
        return LifeVersionGenerator()
    
    @pytest.fixture
    def sample_rules(self):
        """模拟规则结果"""
        return [
            MockRuleResult("rule_001", score=0.7, tags="稳", description="稳定发展"),
            MockRuleResult("rule_002", score=0.8, tags="进取", description="积极突破"),
            MockRuleResult("rule_003", score=0.6, tags="", description="平衡策略"),
            MockRuleResult("rule_004", score=0.5, level="吉"),
            MockRuleResult("rule_005", score=0.65, description="有变化机遇"),
        ]
    
    def test_generate_returns_version_set(self, generator, sample_rules):
        """测试生成返回版本集合"""
        result = generator.generate(
            sample_rules, 
            LifeDomain.CAREER,
            version_count=3,
        )
        
        assert isinstance(result, LifeVersionSet)
        assert result.domain == LifeDomain.CAREER
        assert len(result.versions) == 3
    
    def test_generate_creates_differentiated_versions(self, generator, sample_rules):
        """测试生成差异化版本"""
        result = generator.generate(
            sample_rules, 
            LifeDomain.CAREER,
        )
        
        # 各版本标题应不同
        titles = [v.title for v in result.versions]
        assert len(set(titles)) >= 2  # 至少2个不同标题
    
    def test_generate_includes_decision_axes(self, generator, sample_rules):
        """测试包含决策维度"""
        result = generator.generate(
            sample_rules, 
            LifeDomain.CAREER,
        )
        
        assert len(result.comparison_axes) >= 3  # 事业场景至少3个维度
        assert "income_ceiling" in result.comparison_axes or "stability" in result.comparison_axes
    
    def test_version_has_expected_outcomes(self, generator, sample_rules):
        """测试版本包含预期收益"""
        result = generator.generate(
            sample_rules, 
            LifeDomain.CAREER,
        )
        
        for version in result.versions:
            assert len(version.expected_outcomes) > 0
            for score in version.expected_outcomes.values():
                assert 0.0 <= score <= 1.0
    
    def test_version_has_strategy(self, generator, sample_rules):
        """测试版本包含策略"""
        result = generator.generate(
            sample_rules, 
            LifeDomain.CAREER,
        )
        
        for version in result.versions:
            assert len(version.strategy) >= 1
            assert version.subtitle
    
    def test_version_has_risks_and_costs(self, generator, sample_rules):
        """测试版本包含风险和代价"""
        result = generator.generate(
            sample_rules, 
            LifeDomain.CAREER,
        )
        
        for version in result.versions:
            assert isinstance(version.risks, list)
            assert isinstance(version.costs, list)
    
    def test_generate_with_empty_rules(self, generator):
        """测试空规则列表"""
        result = generator.generate(
            [], 
            LifeDomain.CAREER,
        )
        
        assert len(result.versions) == 3
        # 空规则时使用默认分数
        for version in result.versions:
            assert version.confidence <= 0.5
    
    def test_recommended_version_is_set(self, generator, sample_rules):
        """测试设置推荐版本"""
        result = generator.generate(
            sample_rules, 
            LifeDomain.CAREER,
        )
        
        assert result.recommended_version_id is not None
        # 推荐版本应在版本列表中
        version_ids = [v.version_id for v in result.versions]
        assert result.recommended_version_id in version_ids


class TestVersionComparator:
    """VersionComparator 测试"""
    
    @pytest.fixture
    def comparator(self):
        return VersionComparator()
    
    @pytest.fixture
    def sample_version_set(self):
        """模拟版本集合"""
        versions = [
            LifeVersion(
                version_id="ver_t1234567890a",
                title="稳健版",
                subtitle="稳定发展策略",
                strategy=["保持现有优势"],
                expected_outcomes={"income_ceiling": 0.5, "stability": 0.8},
                confidence=0.7,
            ),
            LifeVersion(
                version_id="ver_t2345678901b",
                title="进取版",
                subtitle="积极发展策略",
                strategy=["积极拓展"],
                expected_outcomes={"income_ceiling": 0.8, "stability": 0.4},
                confidence=0.7,
            ),
        ]
        
        return LifeVersionSet(
            set_id="vset_t123456789ab",
            user_id="user_001",
            scenario_id="scn_career",
            domain=LifeDomain.CAREER,
            versions=versions,
            comparison_axes=["income_ceiling", "stability"],
        )
    
    def test_compare_returns_comparison(self, comparator, sample_version_set):
        """测试对比返回对比结果"""
        result = comparator.compare(sample_version_set)
        
        assert isinstance(result, VersionComparison)
        assert result.set_id == sample_version_set.set_id
    
    def test_comparison_has_matrix(self, comparator, sample_version_set):
        """测试对比结果包含矩阵"""
        result = comparator.compare(sample_version_set)
        
        assert len(result.matrix) == 2  # 两个版本
        assert "ver_t1234567890a" in result.matrix
        assert "ver_t2345678901b" in result.matrix
    
    def test_differentiation_score_calculated(self, comparator, sample_version_set):
        """测试计算差异化得分"""
        result = comparator.compare(sample_version_set)
        
        assert 0.0 <= result.differentiation_score <= 1.0
        # 样本数据有明显差异
        assert result.differentiation_score > 0.1
    
    def test_summary_generated(self, comparator, sample_version_set):
        """测试生成摘要"""
        result = comparator.compare(sample_version_set)
        
        assert result.summary_zh
        assert "事业" in result.summary_zh
        assert "2" in result.summary_zh or "个" in result.summary_zh
    
    def test_version_ranking(self, comparator, sample_version_set):
        """测试版本排序"""
        ranking = comparator.get_version_ranking(
            sample_version_set,
            priority_axes=["income_ceiling"],
        )
        
        # 进取版收入上限更高
        assert ranking[0] == "ver_t2345678901b"
