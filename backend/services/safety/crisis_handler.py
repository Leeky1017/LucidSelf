"""
Crisis Handler

危机处理模块。

对照 tasks.md 7.3:
- Requirements: 5.2.1-5.2.3
- ⚠️ 陷阱: 这是法律风险点，必须有兜底

设计原则:
- 检测自伤/自杀等危机内容
- 注入危机资源信息
- 提供人工升级通道
- 必须有兜底方案
"""

import logging
from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, List, Optional

logger = logging.getLogger(__name__)


class CrisisType(str, Enum):
    """危机类型"""
    SELF_HARM = "self_harm"        # 自伤
    SUICIDE = "suicide"            # 自杀
    DOMESTIC_VIOLENCE = "domestic_violence"  # 家暴
    CHILD_ABUSE = "child_abuse"    # 虐童
    OTHER = "other"                # 其他


@dataclass
class CrisisResponse:
    """危机响应"""
    detected: bool
    crisis_type: Optional[CrisisType] = None
    severity: str = "low"  # low, medium, high, critical
    resources: List[str] = field(default_factory=list)
    response_text: str = ""
    escalate_to_human: bool = False


class CrisisHandler:
    """
    危机处理器
    
    功能:
    - 检测危机内容
    - 注入危机资源
    - 人工升级触发
    
    ⚠️ 重要:
    - 这是法律风险点
    - 必须提供危机资源
    - 高严重度必须有人工升级
    """
    
    # 危机关键词及严重度
    CRISIS_PATTERNS = {
        CrisisType.SUICIDE: {
            "zh": {
                "critical": ["我要自杀", "我想结束生命", "我要跳楼", "我要服毒"],
                "high": ["不想活了", "活着没意思", "想自杀", "想死"],
                "medium": ["轻生", "自尽", "寻死"],
            },
            "en": {
                "critical": ["i'm going to kill myself", "i want to end my life", "i'm going to jump"],
                "high": ["i don't want to live", "i want to die", "thinking about suicide"],
                "medium": ["suicidal thoughts", "end it all"],
            },
        },
        CrisisType.SELF_HARM: {
            "zh": {
                "high": ["我要自残", "我要割自己"],
                "medium": ["自残", "伤害自己", "划手"],
            },
            "en": {
                "high": ["i'm going to hurt myself", "i'm going to cut myself"],
                "medium": ["self-harm", "cutting myself"],
            },
        },
    }
    
    # 危机资源
    CRISIS_RESOURCES = {
        "zh": {
            "hotlines": [
                "🆘 全国心理援助热线：400-161-9995",
                "🆘 北京心理危机研究与干预中心：010-82951332",
                "🆘 生命热线：400-821-1215",
            ],
            "websites": [
                "🌐 中国心理危机干预: www.crisis.cn",
            ],
        },
        "en": {
            "hotlines": [
                "🆘 National Suicide Prevention Lifeline: 988 (US)",
                "🆘 Crisis Text Line: Text HOME to 741741",
                "🆘 International Association for Suicide Prevention: https://www.iasp.info/resources/Crisis_Centres/",
            ],
            "websites": [
                "🌐 SAMHSA: www.samhsa.gov",
            ],
        },
    }
    
    # 危机响应消息
    CRISIS_MESSAGES = {
        "zh": {
            "critical": """
⚠️ 我非常担心您现在的状态。

如果您正在考虑伤害自己，请立即寻求帮助：

{resources}

您的生命很重要。请现在就拨打上述热线，会有专业人员帮助您。

如果您处于紧急危险中，请立即拨打 120 或前往最近的医院急诊。
""",
            "high": """
💙 我听到了您的痛苦。

如果您正在经历困难的想法，请知道有人愿意倾听和帮助您：

{resources}

您不必独自面对这些。专业的帮助可以帮到您。
""",
            "medium": """
💙 如果您正在经历困难，请记住有支持资源可以帮助您：

{resources}

与专业人士交谈可能会有所帮助。
""",
        },
        "en": {
            "critical": """
⚠️ I'm very concerned about what you're sharing.

If you're thinking about harming yourself, please reach out for help immediately:

{resources}

Your life matters. Please call one of these hotlines now - trained counselors are available 24/7.

If you're in immediate danger, please call emergency services (911) or go to your nearest emergency room.
""",
            "high": """
💙 I hear your pain.

If you're having difficult thoughts, please know that help is available:

{resources}

You don't have to face this alone. Professional support can help.
""",
            "medium": """
💙 If you're going through a difficult time, please remember that support is available:

{resources}

Talking to a professional may help.
""",
        },
    }
    
    def __init__(
        self,
        language: str = "zh",
        escalation_callback: Optional[Callable[[CrisisResponse], None]] = None,
    ):
        """
        初始化危机处理器
        
        Args:
            language: 语言
            escalation_callback: 人工升级回调
        """
        self.language = language
        self.escalation_callback = escalation_callback
    
    def check(self, text: str) -> CrisisResponse:
        """
        检查危机内容
        
        Args:
            text: 输入文本
            
        Returns:
            CrisisResponse
        """
        if not text:
            return CrisisResponse(detected=False)
        
        text_lower = text.lower()
        
        for crisis_type, patterns_dict in self.CRISIS_PATTERNS.items():
            patterns_by_lang = patterns_dict.get(self.language, {})
            
            for severity in ["critical", "high", "medium"]:
                patterns = patterns_by_lang.get(severity, [])
                for pattern in patterns:
                    if pattern in text_lower:
                        response = self._create_response(crisis_type, severity)
                        
                        # 高严重度自动触发人工升级
                        if severity in ["critical", "high"]:
                            response.escalate_to_human = True
                            self._trigger_escalation(response)
                        
                        return response
        
        return CrisisResponse(detected=False)
    
    def get_resources(self) -> List[str]:
        """获取危机资源列表"""
        resources = self.CRISIS_RESOURCES.get(self.language, {})
        result = []
        result.extend(resources.get("hotlines", []))
        result.extend(resources.get("websites", []))
        return result
    
    def _create_response(
        self,
        crisis_type: CrisisType,
        severity: str,
    ) -> CrisisResponse:
        """创建危机响应"""
        resources = self.get_resources()
        resources_text = "\n".join(resources)
        
        messages = self.CRISIS_MESSAGES.get(self.language, {})
        message_template = messages.get(severity, messages.get("medium", ""))
        response_text = message_template.format(resources=resources_text).strip()
        
        logger.warning(
            "Crisis detected: type=%s, severity=%s",
            crisis_type.value, severity,
        )
        
        return CrisisResponse(
            detected=True,
            crisis_type=crisis_type,
            severity=severity,
            resources=resources,
            response_text=response_text,
            escalate_to_human=(severity in ["critical", "high"]),
        )
    
    def _trigger_escalation(self, response: CrisisResponse) -> None:
        """触发人工升级"""
        logger.warning(
            "ESCALATION TRIGGERED: type=%s, severity=%s",
            response.crisis_type.value if response.crisis_type else "unknown",
            response.severity,
        )
        
        if self.escalation_callback:
            try:
                self.escalation_callback(response)
            except Exception as e:
                logger.error("Escalation callback failed: %s", e)
                # ⚠️ 即使回调失败，也不能阻止响应返回
