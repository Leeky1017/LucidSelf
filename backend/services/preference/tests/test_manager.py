"""
Preference Manager Tests

对照 tasks.md 11:
- Requirements: 4.1.1-4.1.3, 8.1.1
"""

import pytest

from backend.services.preference.manager import (
    PreferenceManager,
    UserPreferences,
    PreferenceCategory,
)


class TestPreferenceManagerDefaults:
    """默认偏好测试"""
    
    def test_get_all_defaults(self):
        """测试获取所有默认值"""
        manager = PreferenceManager()
        defaults = manager.get_defaults()
        
        assert len(defaults) > 0
        assert "theme" in defaults
        assert "ui_language" in defaults
    
    def test_get_category_defaults(self):
        """测试获取分类默认值"""
        manager = PreferenceManager()
        
        display_defaults = manager.get_defaults(PreferenceCategory.DISPLAY)
        assert "theme" in display_defaults
        assert "ui_language" not in display_defaults
        
        language_defaults = manager.get_defaults(PreferenceCategory.LANGUAGE)
        assert "ui_language" in language_defaults


class TestPreferenceManagerBasic:
    """基础功能测试"""
    
    def test_get_user_preferences_new(self):
        """测试获取新用户偏好"""
        manager = PreferenceManager()
        prefs = manager.get_user_preferences("user_001")
        
        assert prefs.user_id == "user_001"
        assert len(prefs.preferences) == 0
    
    def test_set_preference(self):
        """测试设置偏好"""
        manager = PreferenceManager()
        
        manager.set_preference("user_001", "theme", "dark")
        
        prefs = manager.get_user_preferences("user_001")
        assert prefs.get("theme") == "dark"
    
    def test_set_preferences_batch(self):
        """测试批量设置偏好"""
        manager = PreferenceManager()
        
        manager.set_preferences("user_001", {
            "theme": "dark",
            "font_size": "large",
            "ui_language": "en",
        })
        
        prefs = manager.get_user_preferences("user_001")
        assert prefs.get("theme") == "dark"
        assert prefs.get("font_size") == "large"
        assert prefs.get("ui_language") == "en"


class TestPreferenceMerging:
    """偏好合并测试"""
    
    def test_get_preference_default(self):
        """测试获取默认偏好"""
        manager = PreferenceManager()
        
        # 用户没有设置，应返回默认值
        theme = manager.get_preference("user_001", "theme")
        assert theme == "light"  # 默认值
    
    def test_get_preference_user_override(self):
        """测试用户覆盖默认"""
        manager = PreferenceManager()
        
        manager.set_preference("user_001", "theme", "dark")
        
        theme = manager.get_preference("user_001", "theme")
        assert theme == "dark"  # 用户值
    
    def test_get_merged_preferences(self):
        """测试获取合并偏好"""
        manager = PreferenceManager()
        
        # 只设置部分偏好
        manager.set_preference("user_001", "theme", "dark")
        
        merged = manager.get_merged_preferences("user_001")
        
        # 用户设置的值
        assert merged["theme"] == "dark"
        # 默认值
        assert merged["font_size"] == "medium"
        assert merged["ui_language"] == "zh"
    
    def test_get_merged_by_category(self):
        """测试按分类获取合并偏好"""
        manager = PreferenceManager()
        
        manager.set_preference("user_001", "theme", "dark")
        
        display_merged = manager.get_merged_preferences(
            "user_001", PreferenceCategory.DISPLAY
        )
        
        assert "theme" in display_merged
        assert "ui_language" not in display_merged


class TestPreferenceReset:
    """偏好重置测试"""
    
    def test_reset_single_preference(self):
        """测试重置单个偏好"""
        manager = PreferenceManager()
        
        manager.set_preference("user_001", "theme", "dark")
        assert manager.get_preference("user_001", "theme") == "dark"
        
        manager.reset_preference("user_001", "theme")
        assert manager.get_preference("user_001", "theme") == "light"  # 回到默认
    
    def test_reset_all_preferences(self):
        """测试重置所有偏好"""
        manager = PreferenceManager()
        
        manager.set_preferences("user_001", {
            "theme": "dark",
            "font_size": "large",
        })
        
        manager.reset_all_preferences("user_001")
        
        prefs = manager.get_user_preferences("user_001")
        assert len(prefs.preferences) == 0


class TestPreferenceExportImport:
    """导出导入测试"""
    
    def test_export_preferences(self):
        """测试导出偏好"""
        manager = PreferenceManager()
        
        manager.set_preferences("user_001", {
            "theme": "dark",
            "ui_language": "en",
        })
        
        exported = manager.export_preferences("user_001")
        
        assert exported["user_id"] == "user_001"
        assert exported["preferences"]["theme"] == "dark"
        assert "created_at" in exported
        assert "updated_at" in exported
    
    def test_import_preferences(self):
        """测试导入偏好"""
        manager = PreferenceManager()
        
        data = {
            "user_id": "user_002",
            "preferences": {
                "theme": "dark",
                "ui_language": "en",
            },
        }
        
        manager.import_preferences(data)
        
        prefs = manager.get_user_preferences("user_002")
        assert prefs.get("theme") == "dark"


class TestUserPreferencesModel:
    """UserPreferences 模型测试"""
    
    def test_create_user_preferences(self):
        """测试创建用户偏好"""
        prefs = UserPreferences(user_id="test_user")
        
        assert prefs.user_id == "test_user"
        assert len(prefs.preferences) == 0
    
    def test_get_set_delete(self):
        """测试 get/set/delete"""
        prefs = UserPreferences(user_id="test_user")
        
        prefs.set("key1", "value1")
        assert prefs.get("key1") == "value1"
        
        prefs.delete("key1")
        assert prefs.get("key1") is None
