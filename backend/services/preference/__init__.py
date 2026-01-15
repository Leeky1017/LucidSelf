"""
Preference Manager Module

用户偏好管理模块:
- PreferenceManager: 偏好存储与检索
- 默认值 + 用户覆盖机制

对照 design.md, tasks.md 5-6
"""

from backend.services.preference.manager import (
    PreferenceManager,
    UserPreferences,
    PreferenceCategory,
)

__all__ = [
    "PreferenceManager",
    "UserPreferences",
    "PreferenceCategory",
]
