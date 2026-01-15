"""
Preference Manager

用户偏好管理器。

对照 tasks.md 11:
- Requirements: 4.1.1-4.1.3
- 默认值 + 用户覆盖机制
- 分类管理
"""

import logging
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class PreferenceCategory(str, Enum):
    """偏好分类"""
    DISPLAY = "display"          # 显示偏好
    ANALYSIS = "analysis"        # 分析偏好
    NOTIFICATION = "notification"  # 通知偏好
    PRIVACY = "privacy"          # 隐私偏好
    LANGUAGE = "language"        # 语言偏好


@dataclass
class UserPreferences:
    """用户偏好"""
    user_id: str
    preferences: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    
    def get(self, key: str, default: Any = None) -> Any:
        """获取偏好值"""
        return self.preferences.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """设置偏好值"""
        self.preferences[key] = value
        self.updated_at = datetime.utcnow()
    
    def delete(self, key: str) -> bool:
        """删除偏好值"""
        if key in self.preferences:
            del self.preferences[key]
            self.updated_at = datetime.utcnow()
            return True
        return False


class PreferenceManager:
    """
    偏好管理器
    
    功能:
    - 默认偏好管理
    - 用户偏好存储与检索
    - 偏好合并 (用户覆盖默认)
    - 分类管理
    """
    
    # 默认偏好值
    DEFAULT_PREFERENCES: Dict[str, Dict[str, Any]] = {
        PreferenceCategory.DISPLAY: {
            "theme": "light",
            "font_size": "medium",
            "show_evidence": True,
            "compact_mode": False,
        },
        PreferenceCategory.ANALYSIS: {
            "default_engines": ["bazi"],
            "include_narrative": True,
            "detail_level": "standard",  # brief, standard, detailed
            "show_confidence": True,
        },
        PreferenceCategory.NOTIFICATION: {
            "email_enabled": False,
            "push_enabled": False,
            "daily_reminder": False,
            "weekly_report": False,
        },
        PreferenceCategory.PRIVACY: {
            "share_anonymous_data": False,
            "save_history": True,
            "history_retention_days": 90,
        },
        PreferenceCategory.LANGUAGE: {
            "ui_language": "zh",
            "analysis_language": "zh",
            "date_format": "YYYY-MM-DD",
        },
    }
    
    def __init__(self, storage: Optional[Dict[str, UserPreferences]] = None):
        """
        初始化偏好管理器
        
        Args:
            storage: 可选的存储后端 (默认使用内存)
        """
        self._storage: Dict[str, UserPreferences] = storage or {}
    
    def get_defaults(self, category: Optional[PreferenceCategory] = None) -> Dict[str, Any]:
        """
        获取默认偏好
        
        Args:
            category: 可选的分类过滤
            
        Returns:
            默认偏好字典
        """
        if category:
            return dict(self.DEFAULT_PREFERENCES.get(category, {}))
        
        # 合并所有分类
        result = {}
        for cat_prefs in self.DEFAULT_PREFERENCES.values():
            result.update(cat_prefs)
        return result
    
    def get_user_preferences(self, user_id: str) -> UserPreferences:
        """
        获取用户偏好
        
        Args:
            user_id: 用户 ID
            
        Returns:
            UserPreferences (如不存在则创建新的)
        """
        if user_id not in self._storage:
            self._storage[user_id] = UserPreferences(user_id=user_id)
        return self._storage[user_id]
    
    def get_preference(
        self,
        user_id: str,
        key: str,
        category: Optional[PreferenceCategory] = None,
    ) -> Any:
        """
        获取单个偏好值 (用户覆盖默认)
        
        Args:
            user_id: 用户 ID
            key: 偏好键
            category: 可选的分类
            
        Returns:
            偏好值
        """
        # 先检查用户偏好
        user_prefs = self.get_user_preferences(user_id)
        if key in user_prefs.preferences:
            return user_prefs.preferences[key]
        
        # 回退到默认值
        if category:
            return self.DEFAULT_PREFERENCES.get(category, {}).get(key)
        
        # 在所有分类中查找默认值
        for cat_prefs in self.DEFAULT_PREFERENCES.values():
            if key in cat_prefs:
                return cat_prefs[key]
        
        return None
    
    def get_merged_preferences(
        self,
        user_id: str,
        category: Optional[PreferenceCategory] = None,
    ) -> Dict[str, Any]:
        """
        获取合并后的偏好 (默认 + 用户覆盖)
        
        Args:
            user_id: 用户 ID
            category: 可选的分类过滤
            
        Returns:
            合并后的偏好字典
        """
        # 获取默认值
        defaults = self.get_defaults(category)
        
        # 获取用户偏好
        user_prefs = self.get_user_preferences(user_id)
        
        # 合并 (用户覆盖默认)
        merged = dict(defaults)
        merged.update(user_prefs.preferences)
        
        return merged
    
    def set_preference(
        self,
        user_id: str,
        key: str,
        value: Any,
    ) -> None:
        """
        设置用户偏好
        
        Args:
            user_id: 用户 ID
            key: 偏好键
            value: 偏好值
        """
        user_prefs = self.get_user_preferences(user_id)
        user_prefs.set(key, value)
        
        logger.debug("Preference set: user=%s, key=%s", user_id, key)
    
    def set_preferences(
        self,
        user_id: str,
        preferences: Dict[str, Any],
    ) -> None:
        """
        批量设置用户偏好
        
        Args:
            user_id: 用户 ID
            preferences: 偏好字典
        """
        user_prefs = self.get_user_preferences(user_id)
        for key, value in preferences.items():
            user_prefs.set(key, value)
        
        logger.debug("Preferences updated: user=%s, count=%d", user_id, len(preferences))
    
    def reset_preference(self, user_id: str, key: str) -> bool:
        """
        重置用户偏好到默认值
        
        Args:
            user_id: 用户 ID
            key: 偏好键
            
        Returns:
            是否成功
        """
        user_prefs = self.get_user_preferences(user_id)
        return user_prefs.delete(key)
    
    def reset_all_preferences(self, user_id: str) -> None:
        """
        重置用户所有偏好到默认值
        
        Args:
            user_id: 用户 ID
        """
        if user_id in self._storage:
            self._storage[user_id] = UserPreferences(user_id=user_id)
            logger.info("All preferences reset: user=%s", user_id)
    
    def list_users(self) -> List[str]:
        """列出所有有偏好设置的用户"""
        return list(self._storage.keys())
    
    def export_preferences(self, user_id: str) -> Dict[str, Any]:
        """
        导出用户偏好 (用于备份)
        
        Args:
            user_id: 用户 ID
            
        Returns:
            可序列化的偏好数据
        """
        user_prefs = self.get_user_preferences(user_id)
        return {
            "user_id": user_prefs.user_id,
            "preferences": user_prefs.preferences,
            "created_at": user_prefs.created_at.isoformat(),
            "updated_at": user_prefs.updated_at.isoformat(),
        }
    
    def import_preferences(self, data: Dict[str, Any]) -> None:
        """
        导入用户偏好 (用于恢复)
        
        Args:
            data: 导出的偏好数据
        """
        user_id = data["user_id"]
        prefs = UserPreferences(
            user_id=user_id,
            preferences=data.get("preferences", {}),
        )
        self._storage[user_id] = prefs
        logger.info("Preferences imported: user=%s", user_id)
