"""
Safety Moderator

内容安全审核器。

对照 tasks.md 7.1-7.2:
- Requirements: 5.1.1-5.1.3
- ⚠️ 陷阱: 不要过度过滤导致正常内容被拦截

设计原则:
- 白名单模式: 优先允许，只拦截明确有害内容
- 敏感话题标记: 不拦截但添加提示
- 分级处理: 不同级别不同处理方式
"""

import logging
import re
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Set

logger = logging.getLogger(__name__)


class SafetyLevel(str, Enum):
    """安全级别"""
    SAFE = "safe"              # 完全安全
    CAUTION = "caution"        # 需要注意，添加提示
    SENSITIVE = "sensitive"    # 敏感话题，需要 disclaimer
    BLOCKED = "blocked"        # 被拦截


class SensitiveTopic(str, Enum):
    """敏感话题类型"""
    HEALTH = "health"          # 健康/医疗
    LEGAL = "legal"            # 法律
    FINANCIAL = "financial"    # 财务/投资
    MENTAL_HEALTH = "mental_health"  # 心理健康
    CRISIS = "crisis"          # 危机 (自伤/自杀)


@dataclass
class SafetyResult:
    """安全检查结果"""
    level: SafetyLevel
    passed: bool
    topics: List[SensitiveTopic] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    filtered_content: Optional[str] = None
    disclaimer: Optional[str] = None


class SafetyModerator:
    """
    安全审核器
    
    功能:
    - 输入内容检查
    - 输出内容检查
    - 敏感话题检测
    - Disclaimer 注入
    
    ⚠️ 重要:
    - 使用白名单模式，避免过度过滤
    - 敏感话题不直接拦截，而是添加 disclaimer
    - 只有明确有害内容才被拦截
    """
    
    # 敏感话题关键词 (用于标记，不拦截)
    SENSITIVE_KEYWORDS = {
        SensitiveTopic.HEALTH: {
            "zh": ["疾病", "治疗", "药物", "医院", "诊断", "症状", "手术"],
            "en": ["disease", "treatment", "medicine", "hospital", "diagnosis", "symptoms", "surgery"],
        },
        SensitiveTopic.LEGAL: {
            "zh": ["法律", "诉讼", "合同", "律师", "判决", "起诉"],
            "en": ["legal", "lawsuit", "contract", "lawyer", "verdict", "sue"],
        },
        SensitiveTopic.FINANCIAL: {
            "zh": ["投资", "股票", "基金", "理财", "贷款", "信用卡"],
            "en": ["invest", "stock", "fund", "finance", "loan", "credit"],
        },
        SensitiveTopic.MENTAL_HEALTH: {
            "zh": ["抑郁", "焦虑", "压力", "情绪低落", "失眠"],
            "en": ["depression", "anxiety", "stress", "emotional", "insomnia"],
        },
    }
    
    # 危机关键词 (需要特殊处理)
    CRISIS_KEYWORDS = {
        "zh": ["自杀", "自残", "不想活", "结束生命", "轻生", "自尽"],
        "en": ["suicide", "self-harm", "end my life", "kill myself", "don't want to live"],
    }
    
    # 明确有害内容 (直接拦截)
    BLOCKED_PATTERNS = [
        # 仅拦截明确有害的内容
        r"(?i)(how\s+to\s+make\s+a\s+bomb)",
        r"(?i)(instructions\s+for\s+illegal)",
    ]
    
    # Disclaimer 模板
    DISCLAIMERS = {
        SensitiveTopic.HEALTH: {
            "zh": "⚕️ 温馨提示：以上内容仅供参考，不构成医疗建议。如有健康问题，请咨询专业医生。",
            "en": "⚕️ Disclaimer: This content is for reference only and does not constitute medical advice. Please consult a healthcare professional for health concerns.",
        },
        SensitiveTopic.LEGAL: {
            "zh": "⚖️ 温馨提示：以上内容仅供参考，不构成法律建议。如有法律问题，请咨询专业律师。",
            "en": "⚖️ Disclaimer: This content is for reference only and does not constitute legal advice. Please consult a qualified lawyer for legal matters.",
        },
        SensitiveTopic.FINANCIAL: {
            "zh": "💰 温馨提示：以上内容仅供参考，不构成投资建议。投资有风险，请谨慎决策。",
            "en": "💰 Disclaimer: This content is for reference only and does not constitute investment advice. Investments carry risks, please make decisions carefully.",
        },
        SensitiveTopic.MENTAL_HEALTH: {
            "zh": "🧠 温馨提示：如果您正在经历困难，请记住您并不孤单。如需帮助，请联系专业心理咨询师。",
            "en": "🧠 Reminder: If you are going through a difficult time, remember you are not alone. Please reach out to a mental health professional if needed.",
        },
    }
    
    def __init__(self, language: str = "zh"):
        """
        初始化审核器
        
        Args:
            language: 语言 ("zh" 或 "en")
        """
        self.language = language
        self._blocked_patterns = [re.compile(p) for p in self.BLOCKED_PATTERNS]
    
    def check_input(self, text: str) -> SafetyResult:
        """
        检查输入内容
        
        Args:
            text: 输入文本
            
        Returns:
            SafetyResult
        """
        if not text:
            return SafetyResult(level=SafetyLevel.SAFE, passed=True)
        
        # 1. 检查是否包含明确有害内容
        for pattern in self._blocked_patterns:
            if pattern.search(text):
                logger.warning("Blocked harmful input content")
                return SafetyResult(
                    level=SafetyLevel.BLOCKED,
                    passed=False,
                    warnings=["Input contains harmful content"],
                )
        
        # 2. 检查危机关键词
        crisis_keywords = self.CRISIS_KEYWORDS.get(self.language, [])
        for keyword in crisis_keywords:
            if keyword in text.lower():
                return SafetyResult(
                    level=SafetyLevel.SENSITIVE,
                    passed=True,  # 不拦截，但标记
                    topics=[SensitiveTopic.CRISIS],
                    warnings=["Crisis-related content detected"],
                )
        
        # 3. 检查敏感话题
        detected_topics = self._detect_topics(text)
        
        if detected_topics:
            return SafetyResult(
                level=SafetyLevel.CAUTION,
                passed=True,
                topics=detected_topics,
            )
        
        return SafetyResult(level=SafetyLevel.SAFE, passed=True)
    
    def check_output(self, text: str) -> SafetyResult:
        """
        检查输出内容
        
        Args:
            text: 输出文本
            
        Returns:
            SafetyResult (包含可能的 disclaimer)
        """
        if not text:
            return SafetyResult(level=SafetyLevel.SAFE, passed=True)
        
        # 1. 检查是否包含明确有害内容
        for pattern in self._blocked_patterns:
            if pattern.search(text):
                logger.warning("Blocked harmful output content")
                return SafetyResult(
                    level=SafetyLevel.BLOCKED,
                    passed=False,
                    warnings=["Output contains harmful content"],
                    filtered_content="[内容已过滤]" if self.language == "zh" else "[Content filtered]",
                )
        
        # 2. 检查敏感话题并添加 disclaimer
        detected_topics = self._detect_topics(text)
        
        if detected_topics:
            disclaimers = []
            for topic in detected_topics:
                if topic in self.DISCLAIMERS:
                    disclaimer = self.DISCLAIMERS[topic].get(self.language, "")
                    if disclaimer:
                        disclaimers.append(disclaimer)
            
            combined_disclaimer = "\n".join(disclaimers) if disclaimers else None
            
            return SafetyResult(
                level=SafetyLevel.CAUTION,
                passed=True,
                topics=detected_topics,
                disclaimer=combined_disclaimer,
            )
        
        return SafetyResult(level=SafetyLevel.SAFE, passed=True)
    
    def _detect_topics(self, text: str) -> List[SensitiveTopic]:
        """检测敏感话题"""
        detected = []
        text_lower = text.lower()
        
        for topic, keywords_dict in self.SENSITIVE_KEYWORDS.items():
            keywords = keywords_dict.get(self.language, [])
            for keyword in keywords:
                if keyword in text_lower:
                    if topic not in detected:
                        detected.append(topic)
                    break
        
        return detected
    
    def inject_disclaimer(self, text: str, topics: List[SensitiveTopic]) -> str:
        """
        注入 disclaimer
        
        Args:
            text: 原始文本
            topics: 敏感话题列表
            
        Returns:
            带 disclaimer 的文本
        """
        if not topics:
            return text
        
        disclaimers = []
        for topic in topics:
            if topic in self.DISCLAIMERS:
                disclaimer = self.DISCLAIMERS[topic].get(self.language, "")
                if disclaimer and disclaimer not in disclaimers:
                    disclaimers.append(disclaimer)
        
        if disclaimers:
            separator = "\n\n---\n\n"
            return text + separator + "\n".join(disclaimers)
        
        return text
