"""
Crisis Handler Tests

对照 tasks.md 7.3, 7.5:
- Requirements: 5.2.1-5.2.3, 8.1.1
- ⚠️ 陷阱: 这是法律风险点，必须有兜底
"""

import pytest

from backend.services.safety.crisis_handler import (
    CrisisHandler,
    CrisisType,
    CrisisResponse,
)


class TestCrisisDetection:
    """危机检测测试"""
    
    def test_no_crisis(self, crisis_handler_zh):
        """测试无危机内容"""
        result = crisis_handler_zh.check("今天天气真好")
        
        assert result.detected is False
        assert result.crisis_type is None
    
    def test_suicide_critical_detected(self, crisis_handler_zh):
        """测试 critical 级别自杀关键词"""
        result = crisis_handler_zh.check("我要自杀")
        
        assert result.detected is True
        assert result.crisis_type == CrisisType.SUICIDE
        assert result.severity == "critical"
        assert result.escalate_to_human is True
    
    def test_suicide_high_detected(self, crisis_handler_zh):
        """测试 high 级别自杀关键词"""
        result = crisis_handler_zh.check("不想活了")
        
        assert result.detected is True
        assert result.crisis_type == CrisisType.SUICIDE
        assert result.severity == "high"
        assert result.escalate_to_human is True
    
    def test_suicide_medium_detected(self, crisis_handler_zh):
        """测试 medium 级别自杀关键词"""
        result = crisis_handler_zh.check("最近有些轻生的念头")
        
        assert result.detected is True
        assert result.crisis_type == CrisisType.SUICIDE
        assert result.severity == "medium"
        assert result.escalate_to_human is False  # medium 不自动升级
    
    def test_self_harm_detected(self, crisis_handler_zh):
        """测试自残关键词"""
        result = crisis_handler_zh.check("我想伤害自己")
        
        assert result.detected is True
        assert result.crisis_type == CrisisType.SELF_HARM


class TestCrisisResources:
    """危机资源测试"""
    
    def test_resources_included(self, crisis_handler_zh):
        """测试响应包含资源"""
        result = crisis_handler_zh.check("我不想活了")
        
        assert len(result.resources) > 0
        assert any("热线" in r for r in result.resources)
    
    def test_response_text_includes_resources(self, crisis_handler_zh):
        """测试响应文本包含资源"""
        result = crisis_handler_zh.check("我要自杀")
        
        assert result.response_text
        assert "120" in result.response_text or "热线" in result.response_text
    
    def test_get_resources(self, crisis_handler_zh):
        """测试获取资源列表"""
        resources = crisis_handler_zh.get_resources()
        
        assert len(resources) > 0


class TestEscalation:
    """人工升级测试"""
    
    def test_critical_triggers_escalation(self, crisis_handler_zh):
        """测试 critical 触发升级"""
        result = crisis_handler_zh.check("我要自杀")
        
        assert result.escalate_to_human is True
    
    def test_high_triggers_escalation(self, crisis_handler_zh):
        """测试 high 触发升级"""
        result = crisis_handler_zh.check("不想活了")
        
        assert result.escalate_to_human is True
    
    def test_medium_no_auto_escalation(self, crisis_handler_zh):
        """测试 medium 不自动升级"""
        result = crisis_handler_zh.check("有些轻生")
        
        assert result.escalate_to_human is False
    
    def test_escalation_callback_called(self):
        """测试升级回调被调用"""
        escalation_data = []
        
        def on_escalation(response: CrisisResponse):
            escalation_data.append(response)
        
        handler = CrisisHandler(language="zh", escalation_callback=on_escalation)
        handler.check("我要自杀")
        
        assert len(escalation_data) == 1
        assert escalation_data[0].crisis_type == CrisisType.SUICIDE


class TestEnglishSupport:
    """英文支持测试"""
    
    def test_english_crisis_detected(self, crisis_handler_en):
        """测试英文危机检测"""
        result = crisis_handler_en.check("i want to die")
        
        assert result.detected is True
        assert result.crisis_type == CrisisType.SUICIDE
    
    def test_english_resources(self, crisis_handler_en):
        """测试英文资源"""
        resources = crisis_handler_en.get_resources()
        
        assert len(resources) > 0
        assert any("988" in r or "Lifeline" in r for r in resources)
