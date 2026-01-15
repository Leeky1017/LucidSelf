"""
Tests for Hot Reload

热重载功能的集成测试。

对照 T-6-3: Hot Reload
"""

import tempfile
import threading
import time
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from backend.rules.reloader import RuleReloader, ReloadEvent


class TestRuleReloaderBackup:
    """RuleReloader 备份回滚测试"""
    
    def test_backup_current_creates_backup(self, tmp_path):
        """测试备份创建"""
        reloader = RuleReloader(watch_dir=tmp_path)
        
        # 创建测试文件
        test_file = tmp_path / "test.jsonl"
        test_file.write_text('{"rule": "test"}')
        
        # 备份
        backup_hash = reloader._backup_current(test_file)
        
        assert backup_hash is not None
        assert len(backup_hash) == 16
        assert reloader.get_backup_count() == 1
    
    def test_backup_max_limit(self, tmp_path):
        """测试备份数量限制"""
        reloader = RuleReloader(watch_dir=tmp_path)
        reloader._max_backups = 3
        
        # 创建多个备份
        for i in range(5):
            test_file = tmp_path / f"test_{i}.jsonl"
            test_file.write_text(f'{{"rule": "test_{i}"}}')
            reloader._backup_current(test_file)
        
        # 应该只保留最近 3 个
        assert reloader.get_backup_count() <= 3
    
    def test_rollback_restores_content(self, tmp_path):
        """测试回滚恢复内容"""
        reloader = RuleReloader(watch_dir=tmp_path)
        
        # 创建原始文件
        test_file = tmp_path / "test.jsonl"
        original_content = '{"rule": "original"}'
        test_file.write_text(original_content)
        
        # 备份
        backup_hash = reloader._backup_current(test_file)
        
        # 修改文件
        test_file.write_text('{"rule": "modified"}')
        
        # 回滚
        success = reloader._rollback(test_file, backup_hash)
        
        assert success is True
        assert test_file.read_text() == original_content
    
    def test_rollback_nonexistent_backup(self, tmp_path):
        """测试回滚不存在的备份"""
        reloader = RuleReloader(watch_dir=tmp_path)
        test_file = tmp_path / "test.jsonl"
        
        success = reloader._rollback(test_file, "nonexistent_hash")
        
        assert success is False


class TestRuleReloaderEvents:
    """RuleReloader 事件测试"""
    
    def test_event_callback_registration(self, tmp_path):
        """测试事件回调注册"""
        reloader = RuleReloader(watch_dir=tmp_path)
        
        callback_called = []
        
        def on_reload(data):
            callback_called.append(data)
        
        reloader.on_event(ReloadEvent.RULE_RELOADED, on_reload)
        
        # 触发事件
        reloader._emit_event(ReloadEvent.RULE_RELOADED, {"file": "test.jsonl"})
        
        assert len(callback_called) == 1
        assert callback_called[0]["file"] == "test.jsonl"
    
    def test_reload_history(self, tmp_path):
        """测试重载历史记录"""
        reloader = RuleReloader(watch_dir=tmp_path)
        
        # 记录一些历史
        test_file = tmp_path / "test.jsonl"
        reloader._log_reload(test_file, True)
        reloader._log_reload(test_file, False, "Some error")
        
        history = reloader.get_reload_history()
        
        assert len(history) == 2
        assert history[0]["success"] is True
        assert history[1]["success"] is False
        assert history[1]["error"] == "Some error"


class TestRuleReloaderPythonModule:
    """RuleReloader Python 模块热重载测试"""
    
    def test_reload_python_module_success(self, tmp_path):
        """测试 Python 模块热重载成功"""
        reloader = RuleReloader(watch_dir=tmp_path)
        
        # 创建测试模块
        test_module = tmp_path / "test_module.py"
        test_module.write_text("VERSION = 1")
        
        # Mock _reload_module
        with patch.object(reloader, "_reload_module") as mock_reload:
            success = reloader.reload_python_module(test_module)
            
            assert success is True
            mock_reload.assert_called_once_with(test_module)
    
    def test_reload_python_module_failure(self, tmp_path):
        """测试 Python 模块热重载失败"""
        reloader = RuleReloader(watch_dir=tmp_path)
        
        test_module = tmp_path / "test_module.py"
        
        # Mock _reload_module 抛出异常
        with patch.object(reloader, "_reload_module", side_effect=ImportError("Module not found")):
            success = reloader.reload_python_module(test_module)
            
            assert success is False
            
            # 检查历史记录
            history = reloader.get_reload_history()
            assert len(history) == 1
            assert history[0]["success"] is False


class TestRuleReloaderWatchPatterns:
    """RuleReloader 文件模式测试"""
    
    def test_default_watch_patterns(self, tmp_path):
        """测试默认监控模式"""
        reloader = RuleReloader(watch_dir=tmp_path)
        
        assert ".jsonl" in reloader.watch_patterns
        assert ".py" in reloader.watch_patterns
    
    def test_custom_watch_patterns(self, tmp_path):
        """测试自定义监控模式"""
        reloader = RuleReloader(
            watch_dir=tmp_path,
            watch_patterns=[".yaml", ".json"]
        )
        
        assert ".yaml" in reloader.watch_patterns
        assert ".json" in reloader.watch_patterns
        assert ".jsonl" not in reloader.watch_patterns


# =============================================================================
# FileSystemHotReloadWatcher Tests
# =============================================================================

class TestFileSystemHotReloadWatcher:
    """FileSystemHotReloadWatcher 测试"""
    
    def test_import(self):
        """测试导入"""
        from scripts.codegen.hot_reload import (
            FileSystemHotReloadWatcher,
            HotReloadWatcher,
        )
        
        assert issubclass(FileSystemHotReloadWatcher, HotReloadWatcher)
    
    def test_initialization(self, tmp_path):
        """测试初始化"""
        from scripts.codegen.hot_reload import FileSystemHotReloadWatcher
        
        watcher = FileSystemHotReloadWatcher(
            watch_dir=tmp_path,
            patterns=["*.py"],
            debounce_seconds=0.5,
        )
        
        assert watcher.watch_dir == tmp_path
        assert watcher.patterns == ["*.py"]
        assert watcher.debounce_seconds == 0.5
        assert watcher.is_running is False
    
    def test_start_stop(self, tmp_path):
        """测试启动停止"""
        from scripts.codegen.hot_reload import FileSystemHotReloadWatcher
        
        watcher = FileSystemHotReloadWatcher(watch_dir=tmp_path)
        
        watcher.start()
        # 如果 watchdog 已安装则应该运行，否则跳过
        try:
            import watchdog
            assert watcher.is_running is True
        except ImportError:
            pytest.skip("watchdog not installed")
        
        watcher.stop()
        assert watcher.is_running is False
    
    def test_matches_pattern(self, tmp_path):
        """测试模式匹配"""
        from scripts.codegen.hot_reload import FileSystemHotReloadWatcher
        
        watcher = FileSystemHotReloadWatcher(
            watch_dir=tmp_path,
            patterns=["*.py", "*.jsonl"],
        )
        
        assert watcher._matches_pattern(Path("test.py")) is True
        assert watcher._matches_pattern(Path("test.jsonl")) is True
        assert watcher._matches_pattern(Path("test.txt")) is False
    
    def test_callback_on_file_changed(self, tmp_path):
        """测试文件变化回调"""
        from scripts.codegen.hot_reload import (
            FileSystemHotReloadWatcher,
            register_reload_listener,
            unregister_reload_listener,
        )
        
        watcher = FileSystemHotReloadWatcher(watch_dir=tmp_path)
        
        # 注册监听器
        changed_files = []
        
        def on_change(path):
            changed_files.append(path)
        
        register_reload_listener(on_change)
        
        try:
            # 触发回调
            test_file = tmp_path / "test.py"
            watcher.on_file_changed(test_file)
            
            assert len(changed_files) == 1
            assert changed_files[0] == test_file
        finally:
            unregister_reload_listener(on_change)


class TestReloadNotification:
    """重载通知测试"""
    
    def test_notify_reload(self):
        """测试重载通知"""
        from scripts.codegen.hot_reload import (
            notify_reload,
            register_reload_listener,
            unregister_reload_listener,
        )
        
        notified = []
        
        def listener(path):
            notified.append(path)
        
        register_reload_listener(listener)
        
        try:
            notify_reload(Path("/test/path.py"))
            
            assert len(notified) == 1
            assert notified[0] == Path("/test/path.py")
        finally:
            unregister_reload_listener(listener)
    
    def test_reload_module_helper(self):
        """测试模块重载辅助函数"""
        from scripts.codegen.hot_reload import reload_module
        
        # 尝试重载不存在的模块
        result = reload_module("nonexistent_module_12345")
        assert result is False
        
        # 尝试重载已存在的模块
        import json
        result = reload_module("json")
        assert result is True
