"""
Tests for hot_reload module
"""

from pathlib import Path

import pytest

from scripts.codegen.hot_reload import (
    HotReloadable,
    HotReloadWatcher,
    PlaceholderHotReloadWatcher,
    register_reload_listener,
    unregister_reload_listener,
    notify_reload,
    reload_module,
    _reload_listeners,
)


class TestHotReloadableProtocol:
    """HotReloadable Protocol 测试"""
    
    def test_protocol_definition(self):
        """测试协议定义"""
        # 创建实现协议的类
        class TestLoader:
            def reload(self, module_path: Path) -> bool:
                return True
        
        loader = TestLoader()
        result = loader.reload(Path("/test/module.py"))
        assert result is True
    
    def test_protocol_with_custom_logic(self):
        """测试带自定义逻辑的实现"""
        class CustomLoader:
            def __init__(self):
                self.reload_count = 0
            
            def reload(self, module_path: Path) -> bool:
                self.reload_count += 1
                return module_path.suffix == ".py"
        
        loader = CustomLoader()
        assert loader.reload(Path("test.py")) is True
        assert loader.reload(Path("test.js")) is False
        assert loader.reload_count == 2


class TestReloadListeners:
    """重载监听器测试"""
    
    @pytest.fixture(autouse=True)
    def cleanup_listeners(self):
        """测试前后清理监听器"""
        original = _reload_listeners.copy()
        _reload_listeners.clear()
        yield
        _reload_listeners.clear()
        _reload_listeners.extend(original)
    
    def test_register_listener(self):
        """测试注册监听器"""
        calls = []
        
        def listener(path):
            calls.append(path)
        
        register_reload_listener(listener)
        assert listener in _reload_listeners
    
    def test_unregister_listener(self):
        """测试取消注册"""
        def listener(path):
            pass
        
        register_reload_listener(listener)
        unregister_reload_listener(listener)
        
        assert listener not in _reload_listeners
    
    def test_unregister_nonexistent(self):
        """测试取消注册不存在的监听器"""
        def listener(path):
            pass
        
        # 不应该抛出异常
        unregister_reload_listener(listener)
    
    def test_duplicate_registration(self):
        """测试重复注册"""
        def listener(path):
            pass
        
        register_reload_listener(listener)
        register_reload_listener(listener)
        
        # 不应该重复添加
        count = _reload_listeners.count(listener)
        assert count == 1


class TestNotifyReload:
    """notify_reload 测试"""
    
    @pytest.fixture(autouse=True)
    def cleanup_listeners(self):
        original = _reload_listeners.copy()
        _reload_listeners.clear()
        yield
        _reload_listeners.clear()
        _reload_listeners.extend(original)
    
    def test_notify_single_listener(self):
        """测试通知单个监听器"""
        calls = []
        
        def listener(path):
            calls.append(path)
        
        register_reload_listener(listener)
        notify_reload(Path("/test/module.py"))
        
        assert len(calls) == 1
        assert calls[0] == Path("/test/module.py")
    
    def test_notify_multiple_listeners(self):
        """测试通知多个监听器"""
        calls1 = []
        calls2 = []
        
        def listener1(path):
            calls1.append(path)
        
        def listener2(path):
            calls2.append(path)
        
        register_reload_listener(listener1)
        register_reload_listener(listener2)
        notify_reload(Path("/test/module.py"))
        
        assert len(calls1) == 1
        assert len(calls2) == 1
    
    def test_notify_handles_error(self):
        """测试监听器错误不影响其他监听器"""
        calls = []
        
        def bad_listener(path):
            raise RuntimeError("Listener error")
        
        def good_listener(path):
            calls.append(path)
        
        register_reload_listener(bad_listener)
        register_reload_listener(good_listener)
        
        # 不应该抛出异常
        notify_reload(Path("/test/module.py"))
        
        # good_listener 应该被调用
        assert len(calls) == 1
    
    def test_notify_no_listeners(self):
        """测试没有监听器时通知"""
        # 不应该抛出异常
        notify_reload(Path("/test/module.py"))


class TestReloadModule:
    """reload_module 测试"""
    
    def test_reload_nonexistent_module(self):
        """测试重载不存在的模块"""
        result = reload_module("nonexistent.module.that.does.not.exist")
        assert result is False
    
    def test_reload_existing_module(self):
        """测试重载已存在的模块"""
        import json
        result = reload_module("json")
        assert result is True


class TestHotReloadWatcher:
    """HotReloadWatcher 测试"""
    
    def test_placeholder_start_raises(self):
        """测试占位实现的 start 抛出异常"""
        watcher = PlaceholderHotReloadWatcher(
            watch_dir=Path("/test"),
            patterns=["*.py"]
        )
        
        with pytest.raises(NotImplementedError):
            watcher.start()
    
    def test_placeholder_stop_raises(self):
        """测试占位实现的 stop 抛出异常"""
        watcher = PlaceholderHotReloadWatcher(
            watch_dir=Path("/test")
        )
        
        with pytest.raises(NotImplementedError):
            watcher.stop()
    
    def test_watcher_init_defaults(self):
        """测试观察者默认参数"""
        watcher = PlaceholderHotReloadWatcher(
            watch_dir=Path("/test")
        )
        
        assert watcher.watch_dir == Path("/test")
        assert watcher.patterns == ["*.py"]
        assert watcher.debounce_seconds == 1.0
        assert watcher.is_running is False
    
    def test_watcher_custom_params(self):
        """测试自定义参数"""
        watcher = PlaceholderHotReloadWatcher(
            watch_dir=Path("/custom"),
            patterns=["*.json", "*.yaml"],
            debounce_seconds=0.5
        )
        
        assert watcher.patterns == ["*.json", "*.yaml"]
        assert watcher.debounce_seconds == 0.5


class TestHotReloadIntegration:
    """集成测试"""
    
    @pytest.fixture(autouse=True)
    def cleanup_listeners(self):
        original = _reload_listeners.copy()
        _reload_listeners.clear()
        yield
        _reload_listeners.clear()
        _reload_listeners.extend(original)
    
    def test_watcher_on_file_changed(self):
        """测试文件变化回调触发通知"""
        calls = []
        
        def listener(path):
            calls.append(path)
        
        register_reload_listener(listener)
        
        watcher = PlaceholderHotReloadWatcher(watch_dir=Path("/test"))
        watcher.on_file_changed(Path("/test/module.py"))
        
        assert len(calls) == 1
        assert calls[0] == Path("/test/module.py")
