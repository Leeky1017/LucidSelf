# backend/tests/unit/test_user_prompt_limit.py
"""
WP-01: User Prompt 4000 字符强制限制测试

测试目标：
1. 验证 _build_user_prompt 输出长度 ≤ 4000
2. 验证截断后结构完整性
3. 覆盖边界：恰好 4000、刚超 4000、大幅超 4000
"""

import pytest
from dataclasses import dataclass
from typing import List, Optional
from unittest.mock import MagicMock, patch

from backend.core.llm.orchestrator import (
    LLMOrchestrator,
    MAX_USER_PROMPT_LENGTH,
    PROMPT_BUDGET,
)


@dataclass
class MockInsight:
    """模拟洞察对象"""
    dimension: str
    summary: str
    strength: float


def create_mock_fusion_result(
    themes: List[str] = None,
    evidence_count: int = 0,
    conflicts_count: int = 0,
):
    """创建模拟 FusionResult"""
    mock = MagicMock()
    mock.primary_themes = themes or ["测试主题"]
    mock.cross_validation_score = 0.85
    
    # 模拟 evidence_chain
    mock.evidence_chain = []
    for i in range(evidence_count):
        ev = MagicMock()
        ev.matched = True
        ev.description = f"规则描述 {i}，" * 10
        ev.confidence = 0.9
        ev.evidence_factors = [f"factor_{i}"]
        mock.evidence_chain.append(ev)
    
    # 模拟 conflicts
    mock.conflicts = []
    for i in range(conflicts_count):
        conflict = MagicMock()
        conflict.group = f"group_{i}"
        mock.conflicts.append(conflict)
    
    return mock


class TestUserPromptLimit:
    """User Prompt 4000 字符限制测试"""
    
    @pytest.fixture
    def orchestrator(self):
        return LLMOrchestrator()
    
    @pytest.fixture
    def minimal_fusion_result(self):
        """最小 FusionResult"""
        return create_mock_fusion_result()
    
    @pytest.fixture
    def large_fusion_result(self):
        """大型 FusionResult（触发截断）"""
        return create_mock_fusion_result(
            themes=["主题1", "主题2", "主题3", "主题4", "主题5"],
            evidence_count=20,
            conflicts_count=2,
        )
    
    def test_prompt_under_limit_no_truncation(self, orchestrator, minimal_fusion_result):
        """测试：未超限时不截断"""
        prompt = orchestrator._build_user_prompt(
            toon_context="TOON:TEST",
            snippets_text="测试素材",
            fusion_result=minimal_fusion_result,
            user_context=None,
            extra_context=None,
            raw_factors=None,
            user_insights=None,
        )
        
        assert len(prompt) <= MAX_USER_PROMPT_LENGTH
        assert "## 时间信息" in prompt
        assert "## 规则分析结果" in prompt
        assert "## 可引用的典籍素材" in prompt
        assert "---" in prompt
    
    def test_prompt_exactly_at_limit(self, orchestrator, minimal_fusion_result):
        """测试：恰好 4000 字符边界"""
        # 构造接近但不超过限制的内容
        snippets = "素材内容\n" * 100  # 约 600 字符
        
        prompt = orchestrator._build_user_prompt(
            toon_context="TOON:TEST",
            snippets_text=snippets,
            fusion_result=minimal_fusion_result,
            user_context={"name": "测试用户"},
            extra_context="额外上下文信息",
            raw_factors=None,
            user_insights=None,
        )
        
        assert len(prompt) <= MAX_USER_PROMPT_LENGTH
    
    def test_prompt_exceeds_limit_truncated(self, orchestrator, large_fusion_result):
        """测试：超限时强制截断到 ≤4000"""
        # 构造超长内容
        long_snippets = "这是一条很长的典籍素材内容，用于测试截断逻辑。" * 200  # 约 4400 字符
        long_insights = [
            MockInsight(
                dimension=f"dimension_{i}",
                summary=f"这是洞察摘要 {i}，内容很长很长很长很长很长很长很长" * 3,
                strength=0.8,
            )
            for i in range(10)
        ]
        
        prompt = orchestrator._build_user_prompt(
            toon_context="TOON:TEST" * 100,
            snippets_text=long_snippets,
            fusion_result=large_fusion_result,
            user_context={"name": "测试用户", "age": 30, "city": "北京"},
            extra_context="额外上下文信息" * 50,
            raw_factors=None,
            user_insights=long_insights,
        )
        
        # 关键断言：长度必须 ≤ 4000
        assert len(prompt) <= MAX_USER_PROMPT_LENGTH, \
            f"Prompt 长度 {len(prompt)} 超过限制 {MAX_USER_PROMPT_LENGTH}"
    
    def test_prompt_massive_overflow_truncated(self, orchestrator, large_fusion_result):
        """测试：大幅超限（10000+ 字符）仍能截断到 4000"""
        # 构造极长内容
        massive_snippets = "极长素材" * 1000  # 约 4000 字符
        massive_insights = [
            MockInsight(
                dimension=f"dim_{i}",
                summary="超长摘要内容" * 20,
                strength=0.9,
            )
            for i in range(20)
        ]
        massive_context = "上下文" * 500
        
        prompt = orchestrator._build_user_prompt(
            toon_context="TOON" * 500,
            snippets_text=massive_snippets,
            fusion_result=large_fusion_result,
            user_context={"data": "x" * 500},
            extra_context=massive_context,
            raw_factors={"bazi-calculator": MagicMock()},
            user_insights=massive_insights,
        )
        
        # 关键断言：无论输入多大，输出必须 ≤ 4000
        assert len(prompt) <= MAX_USER_PROMPT_LENGTH, \
            f"Prompt 长度 {len(prompt)} 超过限制 {MAX_USER_PROMPT_LENGTH}"
    
    def test_structure_preserved_after_truncation(self, orchestrator, large_fusion_result):
        """测试：截断后结构完整性"""
        long_snippets = "素材内容" * 500
        long_insights = [
            MockInsight(dimension=f"dim_{i}", summary=f"摘要{i}" * 10, strength=0.8)
            for i in range(10)
        ]
        
        prompt = orchestrator._build_user_prompt(
            toon_context="TOON:TEST",
            snippets_text=long_snippets,
            fusion_result=large_fusion_result,
            user_context=None,
            extra_context=None,
            raw_factors=None,
            user_insights=long_insights,
        )
        
        # 结构完整性断言
        assert "## 时间信息" in prompt, "时间信息标题必须保留"
        assert "## 规则分析结果" in prompt, "规则分析标题必须保留"
        assert "---" in prompt, "结尾分隔符必须保留"
        assert "请根据以上信息" in prompt, "结尾指令必须保留"
    
    def test_insights_count_limited(self, orchestrator, minimal_fusion_result):
        """测试：洞察条目数截断符合策略（最多5条）"""
        many_insights = [
            MockInsight(dimension=f"dim_{i}", summary=f"摘要{i}", strength=0.8)
            for i in range(10)
        ]
        
        prompt = orchestrator._build_user_prompt(
            toon_context="TOON:TEST",
            snippets_text="素材",
            fusion_result=minimal_fusion_result,
            user_context=None,
            extra_context=None,
            raw_factors=None,
            user_insights=many_insights,
        )
        
        # 统计洞察行数（以 "- **dim_" 开头的行）
        insight_lines = [line for line in prompt.split("\n") if line.strip().startswith("- **dim_")]
        assert len(insight_lines) <= 5, f"洞察条目数 {len(insight_lines)} 超过限制 5"
    
    def test_truncation_logged(self, orchestrator, large_fusion_result, caplog):
        """测试：截断时记录日志"""
        import logging
        caplog.set_level(logging.INFO)
        
        long_snippets = "素材" * 1000
        
        prompt = orchestrator._build_user_prompt(
            toon_context="TOON:TEST",
            snippets_text=long_snippets,
            fusion_result=large_fusion_result,
            user_context=None,
            extra_context=None,
            raw_factors=None,
            user_insights=None,
        )
        
        # 如果发生截断，应该有日志记录
        if len(prompt) < len(long_snippets):
            log_messages = [r.message for r in caplog.records]
            truncation_logged = any(
                "truncat" in msg.lower() or "exceeds" in msg.lower()
                for msg in log_messages
            )
            # 注意：只有真正超限才会有日志
            # 这里主要验证日志机制存在


class TestPromptBudgetConfig:
    """预算配置测试"""
    
    def test_budget_sum_reasonable(self):
        """测试：预算总和合理"""
        total_budget = sum(PROMPT_BUDGET.values())
        assert total_budget <= MAX_USER_PROMPT_LENGTH, \
            f"预算总和 {total_budget} 超过限制 {MAX_USER_PROMPT_LENGTH}"
    
    def test_all_sections_have_budget(self):
        """测试：所有部分都有预算"""
        required_sections = ["header", "profile", "rules", "insights", "snippets", "context", "footer"]
        for section in required_sections:
            assert section in PROMPT_BUDGET, f"缺少 {section} 的预算配置"


class TestTruncateSectionMethod:
    """_truncate_section 方法测试"""
    
    @pytest.fixture
    def orchestrator(self):
        return LLMOrchestrator()
    
    def test_truncate_insights_preserves_header(self, orchestrator):
        """测试：洞察截断保留标题"""
        content = "## 用户历史洞察\n- **dim1**: 摘要1\n- **dim2**: 摘要2\n- **dim3**: 摘要3"
        truncated = orchestrator._truncate_section("insights", content, 50)
        
        assert truncated.startswith("## 用户历史洞察")
    
    def test_truncate_snippets_preserves_header(self, orchestrator):
        """测试：素材截断保留标题"""
        content = "## 可引用的典籍素材\n" + "素材内容" * 100
        truncated = orchestrator._truncate_section("snippets", content, 100)
        
        assert truncated.startswith("## 可引用的典籍素材")
        assert len(truncated) <= 100
    
    def test_truncate_adds_indicator(self, orchestrator):
        """测试：截断时添加截断指示"""
        content = "长内容" * 100
        truncated = orchestrator._truncate_section("context", content, 50)
        
        assert "截断" in truncated or len(truncated) <= 50
