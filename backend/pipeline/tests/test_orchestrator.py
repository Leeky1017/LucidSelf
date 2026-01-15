"""
Pipeline Orchestrator Tests

L1-L5 集成测试
"""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from backend.pipeline.orchestrator import (
    Pipeline,
    PipelineInput,
    PipelineOutput,
    BirthDataInput,
    TarotInput,
    get_pipeline,
)
from backend.core.contracts import FusionResult, RuntimeRuleResult, FactorMatrix, FactorValue


@pytest.fixture
def sample_birth_data():
    """示例出生数据"""
    return BirthDataInput(
        year=1990,
        month=6,
        day=15,
        hour=10,
        minute=30,
        timezone="Asia/Shanghai",
    )


@pytest.fixture
def sample_pipeline_input(sample_birth_data):
    """示例 Pipeline 输入"""
    return PipelineInput(
        user_id="test_user_001",
        birth_data=sample_birth_data,
        include_narrative=False,
        language="zh",
    )


@pytest.fixture
def mock_factor_matrix():
    """Mock FactorMatrix"""
    return FactorMatrix(
        engine_id="bazi-calculator",
        factors={
            "day_master": FactorValue(factor_id="day_master", value="甲", confidence=1.0, source="calculator"),
            "season": FactorValue(factor_id="season", value="夏", confidence=1.0, source="calculator"),
        },
    )


@pytest.fixture
def mock_rule_result():
    """Mock RuntimeRuleResult"""
    return RuntimeRuleResult(
        rule_id="test_rule_001",
        matched=True,
        dimension="事业",
        level="吉",
        confidence=0.85,
        weight=1.5,
        execution_time_ms=1.0,
    )


@pytest.fixture
def mock_fusion_result(mock_rule_result):
    """Mock FusionResult"""
    return FusionResult(
        fusion_id="fus_test12345678",
        primary_themes=["事业突破", "财富积累"],
        evidence_chain=[mock_rule_result],
        cross_validation_score=0.85,
        confidence_matrix={"bazi-calculator": 0.85},
        conflicts=[],
        contributing_engines=["bazi-calculator"],
        fusion_time_ms=10.0,
    )


class TestPipelineBasic:
    """Pipeline 基础测试"""
    
    def test_pipeline_creation(self):
        """测试 Pipeline 创建"""
        pipeline = Pipeline()
        assert pipeline is not None
    
    def test_get_pipeline_singleton(self):
        """测试全局 Pipeline 单例"""
        p1 = get_pipeline()
        p2 = get_pipeline()
        assert p1 is p2


class TestPipelineExecution:
    """Pipeline 执行测试"""
    
    @pytest.mark.asyncio
    async def test_execute_with_mocked_components(
        self,
        sample_pipeline_input,
        mock_factor_matrix,
        mock_rule_result,
        mock_fusion_result,
    ):
        """测试使用 Mock 组件执行"""
        # Mock 各组件
        mock_rule_engine = MagicMock()
        mock_rule_engine.execute_batch.return_value = {
            "bazi-calculator": [mock_rule_result],
        }
        
        mock_fusion_engine = MagicMock()
        mock_fusion_engine.fuse_results.return_value = mock_fusion_result
        
        mock_narrative_gen = MagicMock()
        mock_safety = MagicMock()
        
        # 创建 Pipeline
        pipeline = Pipeline(
            rule_engine=mock_rule_engine,
            fusion_engine=mock_fusion_engine,
            narrative_generator=mock_narrative_gen,
            safety_moderator=mock_safety,
        )
        pipeline._initialized = True
        
        # Mock 因子计算
        with patch.object(pipeline, "_calculate_bazi", return_value=(mock_factor_matrix, object())):
            output = await pipeline.execute(sample_pipeline_input)
        
        assert output.request_id.startswith("req_")
        assert output.fusion_result.fusion_id == mock_fusion_result.fusion_id
        assert output.processing_time_ms > 0
    
    @pytest.mark.asyncio
    async def test_execute_empty_input(self):
        """测试空输入"""
        pipeline = Pipeline()
        pipeline._initialized = True
        
        # Mock 组件
        mock_rule_engine = MagicMock()
        mock_rule_engine.execute_batch.return_value = {}
        
        mock_fusion_engine = MagicMock()
        mock_fusion_engine.fuse_results.return_value = FusionResult(
            fusion_id="fus_empty1234567",
            primary_themes=["通用"],
            evidence_chain=[RuntimeRuleResult(
                rule_id="placeholder",
                matched=False,
                confidence=0.0,
                weight=0.0,
                execution_time_ms=0.0,
            )],
            cross_validation_score=0.0,
            confidence_matrix={},
            conflicts=[],
            contributing_engines=[],
            fusion_time_ms=1.0,
        )
        
        pipeline._rule_engine = mock_rule_engine
        pipeline._fusion_engine = mock_fusion_engine
        pipeline._narrative_generator = MagicMock()
        pipeline._safety_moderator = MagicMock()
        
        input_data = PipelineInput(
            user_id="test_user",
            include_narrative=False,
        )
        
        output = await pipeline.execute(input_data)
        
        assert output is not None
        assert output.fusion_result is not None


class TestPipelineInputModels:
    """输入模型测试"""
    
    def test_birth_data_input(self, sample_birth_data):
        """测试出生数据输入"""
        assert sample_birth_data.year == 1990
        assert sample_birth_data.month == 6
        assert sample_birth_data.timezone == "Asia/Shanghai"
    
    def test_tarot_input(self):
        """测试塔罗输入"""
        tarot = TarotInput(
            cards=["The Fool", "The Magician"],
            spread_type="two_card",
        )
        
        assert len(tarot.cards) == 2
        assert tarot.spread_type == "two_card"
    
    def test_pipeline_input_minimal(self):
        """测试最小 Pipeline 输入"""
        input_data = PipelineInput(user_id="user123")
        
        assert input_data.user_id == "user123"
        assert input_data.birth_data is None
        assert input_data.dream_text is None
        assert input_data.include_narrative is True  # 默认


class TestPipelineOutputModel:
    """输出模型测试"""
    
    def test_pipeline_output(self, mock_fusion_result):
        """测试 Pipeline 输出"""
        output = PipelineOutput(
            request_id="req_test12345678",
            version_id="ver_test12345678",
            corpus_release_id="cr_test12345678",
            fusion_result=mock_fusion_result,
            narrative="测试叙事",
            processing_time_ms=100.0,
        )
        
        assert output.request_id.startswith("req_")
        assert output.fusion_result.fusion_id == mock_fusion_result.fusion_id
        assert output.narrative == "测试叙事"
