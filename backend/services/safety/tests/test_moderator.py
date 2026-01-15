"""
Safety Moderator Tests

对照 tasks.md 7.2, 7.5:
- Requirements: 5.1.1-5.1.3, 8.1.1
- ⚠️ 陷阱: 不要过度过滤导致正常内容被拦截
"""

import pytest

from backend.services.safety.moderator import (
    SafetyModerator,
    SafetyResult,
    SafetyLevel,
    SensitiveTopic,
)


class TestSafetyModeratorBasic:
    """基础测试"""
    
    def test_safe_input(self, moderator_zh):
        """测试安全输入"""
        result = moderator_zh.check_input("今天天气真好")
        
        assert result.level == SafetyLevel.SAFE
        assert result.passed is True
        assert len(result.topics) == 0
    
    def test_empty_input(self, moderator_zh):
        """测试空输入"""
        result = moderator_zh.check_input("")
        
        assert result.level == SafetyLevel.SAFE
        assert result.passed is True
    
    def test_safe_output(self, moderator_zh):
        """测试安全输出"""
        result = moderator_zh.check_output("您今年的运势整体不错")
        
        assert result.level == SafetyLevel.SAFE
        assert result.passed is True


class TestSensitiveTopicDetection:
    """敏感话题检测测试"""
    
    def test_health_topic_detected(self, moderator_zh):
        """测试健康话题检测"""
        result = moderator_zh.check_input("我最近有些症状，想问问该吃什么药物")
        
        assert result.level == SafetyLevel.CAUTION
        assert result.passed is True  # 不拦截
        assert SensitiveTopic.HEALTH in result.topics
    
    def test_legal_topic_detected(self, moderator_zh):
        """测试法律话题检测"""
        result = moderator_zh.check_input("我想咨询一下合同的法律问题")
        
        assert result.level == SafetyLevel.CAUTION
        assert result.passed is True
        assert SensitiveTopic.LEGAL in result.topics
    
    def test_financial_topic_detected(self, moderator_zh):
        """测试财务话题检测"""
        result = moderator_zh.check_input("我应该投资股票还是基金？")
        
        assert result.level == SafetyLevel.CAUTION
        assert result.passed is True
        assert SensitiveTopic.FINANCIAL in result.topics
    
    def test_mental_health_topic_detected(self, moderator_zh):
        """测试心理健康话题检测"""
        result = moderator_zh.check_input("我最近感觉很焦虑，压力很大")
        
        assert result.level == SafetyLevel.CAUTION
        assert result.passed is True
        assert SensitiveTopic.MENTAL_HEALTH in result.topics
    
    def test_english_topic_detection(self, moderator_en):
        """测试英文话题检测"""
        result = moderator_en.check_input("I'm feeling stressed and anxious")
        
        assert result.passed is True
        assert SensitiveTopic.MENTAL_HEALTH in result.topics


class TestDisclaimerInjection:
    """Disclaimer 注入测试"""
    
    def test_output_with_disclaimer(self, moderator_zh):
        """测试输出带 disclaimer"""
        result = moderator_zh.check_output(
            "根据您的情况，您可能需要注意一下症状的变化"
        )
        
        assert result.level == SafetyLevel.CAUTION
        assert result.passed is True
        assert result.disclaimer is not None
        assert "医疗建议" in result.disclaimer
    
    def test_inject_disclaimer_manually(self, moderator_zh):
        """测试手动注入 disclaimer"""
        text = "您今年的财运不错，可以考虑理财"
        result = moderator_zh.check_output(text)
        
        if result.topics:
            with_disclaimer = moderator_zh.inject_disclaimer(text, result.topics)
            assert "---" in with_disclaimer


class TestNoOverFiltering:
    """避免过度过滤测试"""
    
    def test_normal_fortune_not_blocked(self, moderator_zh):
        """测试正常命理内容不被拦截"""
        texts = [
            "您的事业运势在下半年会有所提升",
            "今年感情方面需要注意沟通",
            "财运方面建议稳健为主",
            "您的性格比较内向，适合从事研究类工作",
        ]
        
        for text in texts:
            result = moderator_zh.check_input(text)
            assert result.passed is True, f"Wrongly blocked: {text}"
    
    def test_astrology_terms_not_blocked(self, moderator_zh):
        """测试命理术语不被拦截"""
        texts = [
            "您的日主是甲木，喜用神是水",
            "今年太岁与您的年柱相冲",
            "您的命盘中官星较旺",
        ]
        
        for text in texts:
            result = moderator_zh.check_input(text)
            assert result.passed is True, f"Wrongly blocked: {text}"


class TestBlockedContent:
    """有害内容拦截测试"""
    
    def test_harmful_content_blocked(self, moderator_en):
        """测试有害内容被拦截"""
        # 只有明确有害的内容才被拦截
        result = moderator_en.check_input(
            "how to make a bomb at home"
        )
        
        assert result.level == SafetyLevel.BLOCKED
        assert result.passed is False


class TestCrisisDetection:
    """危机内容检测测试"""
    
    def test_crisis_keywords_detected(self, moderator_zh):
        """测试危机关键词检测"""
        result = moderator_zh.check_input("我不想活了")
        
        assert result.level == SafetyLevel.SENSITIVE
        assert result.passed is True  # 不拦截，但标记
        assert SensitiveTopic.CRISIS in result.topics
