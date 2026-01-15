"""
L3 → L4 Integration Tests

Layer 3 Rule Engine → Layer 4 Fusion Engine 集成测试。

对照 tasks.md Task 13.4
对照 Requirements 6.4, 8.3
"""

import pytest
from datetime import datetime

from backend.core.contracts import RuntimeRuleResult, FusionResult
from backend.rules.engine import RuleEngine
from backend.rules.context import RuleContext
from backend.integration import FusionEngine


class TestL3L4Integration:
    """L3 → L4 集成测试"""
    
    @pytest.fixture
    def simulated_rule_engine_output(self) -> dict:
        """
        模拟 RuleEngine 的输出格式
        
        RuleEngine.execute() 返回 List[RuntimeRuleResult]
        """
        return {
            "bazi-calculator": [
                RuntimeRuleResult(
                    rule_id="bazi_career_success_001",
                    matched=True,
                    dimension="career",
                    level="吉",
                    description="官印相生，事业顺遂",
                    confidence=0.88,
                    weight=1.6,
                    tags=["官印相生", "事业"],
                    evidence_factors=["ten_god_zhengguan", "ten_god_zhengyin"],
                    semantic_refs=["bazi_v2_zhengguan_001"],
                    source_book="子平真诠",
                    l1_anchor="论官印相生",
                    execution_time_ms=1.2,
                ),
                RuntimeRuleResult(
                    rule_id="bazi_wealth_pattern_001",
                    matched=True,
                    dimension="wealth",
                    level="大吉",
                    description="身强财旺，财源广进",
                    confidence=0.92,
                    weight=1.8,
                    tags=["身强财旺", "财富"],
                    evidence_factors=["day_master", "wealth_star"],
                    semantic_refs=["bazi_v2_wealth_001"],
                    source_book="滴天髓",
                    l1_anchor="论财格",
                    execution_time_ms=0.9,
                ),
            ],
            "astro-calculator": [
                RuntimeRuleResult(
                    rule_id="astro_career_jupiter_001",
                    matched=True,
                    dimension="career",
                    level="吉",
                    description="木星入第十宫，事业有贵人扶持",
                    confidence=0.85,
                    weight=1.4,
                    tags=["木星", "第十宫", "事业"],
                    evidence_factors=["jupiter_position", "house_10"],
                    semantic_refs=["astro_v1_jupiter_001"],
                    source_book="Tetrabiblos",
                    l1_anchor="On the Quality of Action",
                    execution_time_ms=1.5,
                ),
            ],
            "tarot-interpreter": [
                RuntimeRuleResult(
                    rule_id="tarot_emperor_career_001",
                    matched=True,
                    dimension="career",
                    level="吉",
                    description="皇帝牌正位，权威与领导力",
                    confidence=0.78,
                    weight=1.2,
                    tags=["皇帝", "权威"],
                    evidence_factors=["major_arcana_emperor"],
                    semantic_refs=["tarot_v1_emperor_001"],
                    source_book="78 Degrees of Wisdom",
                    execution_time_ms=0.6,
                ),
            ],
        }
    
    def test_fusion_accepts_rule_engine_output(
        self,
        fusion_engine,
        simulated_rule_engine_output,
    ):
        """
        测试 FusionEngine 接受 RuleEngine 输出格式
        
        对照 Requirement 6.4
        """
        fusion_result = fusion_engine.fuse_results(simulated_rule_engine_output)
        
        assert isinstance(fusion_result, FusionResult)
        assert len(fusion_result.contributing_engines) == 3
    
    def test_evidence_chain_preserves_traceability(
        self,
        fusion_engine,
        simulated_rule_engine_output,
    ):
        """
        测试证据链保留 L1 溯源信息
        
        对照 Requirement 4.2
        """
        fusion_result = fusion_engine.fuse_results(simulated_rule_engine_output)
        
        # 检查证据链中的溯源信息
        for evidence in fusion_result.evidence_chain:
            if evidence.source_book:
                assert evidence.source_book in [
                    "子平真诠",
                    "滴天髓",
                    "Tetrabiblos",
                    "78 Degrees of Wisdom",
                ]
    
    def test_cross_validation_on_shared_dimension(
        self,
        fusion_engine,
        simulated_rule_engine_output,
    ):
        """
        测试共享维度的交叉验证
        
        career 维度有 3 个引擎的结果
        """
        fusion_result = fusion_engine.fuse_results(simulated_rule_engine_output)
        
        # career 维度应该在置信度矩阵中
        assert "career" in fusion_result.confidence_matrix or "事业" in fusion_result.confidence_matrix
        
        # 交叉验证分数应该 > 0
        assert fusion_result.cross_validation_score > 0
    
    def test_themes_extracted_from_multi_engine(
        self,
        fusion_engine,
        simulated_rule_engine_output,
    ):
        """测试从多引擎结果提取主题"""
        fusion_result = fusion_engine.fuse_results(simulated_rule_engine_output)
        
        # 应该有主题
        assert len(fusion_result.primary_themes) >= 1
        
        # 事业和财富应该是主要主题
        themes_str = " ".join(fusion_result.primary_themes)
        assert "事业" in themes_str or "财富" in themes_str
    
    def test_full_pipeline_produces_valid_result(
        self,
        fusion_engine,
        simulated_rule_engine_output,
    ):
        """
        端到端测试：完整管道产生有效结果
        
        对照 Requirement 8.3
        """
        fusion_result = fusion_engine.fuse_results(simulated_rule_engine_output)
        
        # 验证 FusionResult 契约
        assert fusion_result.fusion_id.startswith("fus_")
        assert 1 <= len(fusion_result.primary_themes) <= 5
        assert 1 <= len(fusion_result.evidence_chain) <= 20
        assert 0.0 <= fusion_result.cross_validation_score <= 1.0
        assert fusion_result.fusion_time_ms >= 0
        assert len(fusion_result.contributing_engines) == 3
        assert isinstance(fusion_result.conflicts, list)
        assert isinstance(fusion_result.confidence_matrix, dict)


class TestRegistryIntegration:
    """引擎注册表集成测试"""
    
    def test_fusion_engine_in_registry(self):
        """测试 FusionEngine 在注册表中 (Requirement 9.3, 9.4)"""
        import json
        from pathlib import Path
        
        registry_path = Path("data/engines/registry.json")
        with open(registry_path) as f:
            engines = json.load(f)
        
        fusion_engines = [e for e in engines if e["kind"] == "fusion"]
        
        assert len(fusion_engines) >= 1
        
        fusion = fusion_engines[0]
        assert fusion["engine_id"] == "cross-system-fusion"
        assert fusion["kind"] == "fusion"
        assert "bazi" in fusion["supported_systems"]
