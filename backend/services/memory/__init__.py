"""
Memory Service Module

三层记忆架构:
- Event: 原始事件记录
- Insight: 归纳洞察
- Profile: 用户画像

对照 design.md 2.4 和 tasks.md 5-4
"""

from backend.services.memory.models import (
    PrivacyLevel,
    MemoryEvent,
    MemoryInsight,
    UserProfile,
)
from backend.services.memory.service import MemoryService
from backend.services.memory.service import get_memory_service
from backend.services.memory.encryption import EncryptionHelper

__all__ = [
    "PrivacyLevel",
    "MemoryEvent",
    "MemoryInsight",
    "UserProfile",
    "MemoryService",
    "get_memory_service",
    "EncryptionHelper",
]
