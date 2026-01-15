"""
Codegen Hot Reload Module

热重载接口预留，用于：
1. 定义 HotReloadable Protocol
2. 提供模块重载通知机制
3. 预留 HotReloadWatcher 类框架（6-3热重载时实现）

注意：此模块为接口预留，完整实现将在 Change 6-3: add-hot-reload-impl 中完成。
"""

import importlib
import sys
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Callable, List, Optional, Protocol, Set


class HotReloadable(Protocol):
    """
    热重载接口协议
    
    任何需要支持热重载的模块加载器都应实现此协议。
    
    Example:
        class RuleLoader:
            def reload(self, module_path: Path) -> bool:
                # 重新加载规则模块
                ...
                return True
    """
    
    def reload(self, module_path: Path) -> bool:
        """
        重新加载指定模块
        
        Args:
            module_path: 模块文件路径
            
        Returns:
            True 如果重载成功，False 否则
        """
        ...


# 全局重载监听器列表
_reload_listeners: List[Callable[[Path], None]] = []


def register_reload_listener(callback: Callable[[Path], None]) -> None:
    """
    注册重载监听器
    
    当模块被重载时，所有注册的监听器都会收到通知。
    
    Args:
        callback: 回调函数，接收模块路径作为参数
    """
    if callback not in _reload_listeners:
        _reload_listeners.append(callback)


def unregister_reload_listener(callback: Callable[[Path], None]) -> None:
    """
    取消注册重载监听器
    
    Args:
        callback: 要移除的回调函数
    """
    if callback in _reload_listeners:
        _reload_listeners.remove(callback)


def notify_reload(module_path: Path) -> None:
    """
    通知所有监听器模块已重载
    
    当代码生成器成功生成或更新模块后，调用此函数通知框架进行热重载。
    
    Args:
        module_path: 被重载的模块路径
        
    Example:
        # 编译完成后通知热重载
        output_path = generator.save(code, filename)
        notify_reload(output_path)
    """
    for listener in _reload_listeners:
        try:
            listener(module_path)
        except Exception:
            # 忽略监听器错误，继续通知其他监听器
            pass


def reload_module(module_name: str) -> bool:
    """
    重新加载已导入的 Python 模块
    
    这是一个辅助函数，用于重新加载 sys.modules 中的模块。
    
    Args:
        module_name: 模块的完整名称，如 "backend.generated.bazi_rules_v1"
        
    Returns:
        True 如果重载成功，False 如果模块未找到
    """
    if module_name not in sys.modules:
        return False
    
    try:
        module = sys.modules[module_name]
        importlib.reload(module)
        return True
    except Exception:
        return False


class HotReloadWatcher(ABC):
    """
    热重载观察者基类（预留框架）
    
    用于监控生成目录的文件变化，并触发自动重载。
    完整实现将在 Change 6-3: add-hot-reload-impl 中完成。
    
    预期功能：
    - 监控 backend/generated/ 目录
    - 检测 .py 文件变化
    - 自动触发模块重载
    - 支持防抖（debounce）避免频繁重载
    
    Example (预期用法):
        watcher = FileSystemHotReloadWatcher(
            watch_dir=Path("backend/generated"),
            debounce_seconds=1.0
        )
        watcher.start()
        
        # ... 应用运行中 ...
        
        watcher.stop()
    """
    
    def __init__(
        self, 
        watch_dir: Path,
        patterns: Optional[List[str]] = None,
        debounce_seconds: float = 1.0
    ):
        """
        初始化观察者
        
        Args:
            watch_dir: 要监控的目录
            patterns: 文件模式列表，默认 ["*.py"]
            debounce_seconds: 防抖时间（秒）
        """
        self.watch_dir = watch_dir
        self.patterns = patterns or ["*.py"]
        self.debounce_seconds = debounce_seconds
        self._running = False
        self._watched_files: Set[Path] = set()
    
    @abstractmethod
    def start(self) -> None:
        """
        启动文件监控
        
        子类需实现具体的文件系统监控逻辑。
        可使用 watchdog 或 inotify 等库。
        """
        raise NotImplementedError(
            "HotReloadWatcher.start() 将在 Change 6-3 中实现"
        )
    
    @abstractmethod
    def stop(self) -> None:
        """
        停止文件监控
        """
        raise NotImplementedError(
            "HotReloadWatcher.stop() 将在 Change 6-3 中实现"
        )
    
    @property
    def is_running(self) -> bool:
        """是否正在运行"""
        return self._running
    
    def on_file_changed(self, path: Path) -> None:
        """
        文件变化回调（子类调用）
        
        Args:
            path: 变化的文件路径
        """
        notify_reload(path)


class FileSystemHotReloadWatcher(HotReloadWatcher):
    """
    基于 watchdog 的热重载观察者
    
    对照 design.md §4.3 HotReloadWatcher 实现
    对照 Requirements R-6-3-01, R-6-3-03
    """
    
    def __init__(
        self,
        watch_dir: Path,
        patterns: Optional[List[str]] = None,
        debounce_seconds: float = 1.0,
    ):
        super().__init__(watch_dir, patterns, debounce_seconds)
        self._observer = None
        self._debounce_timer = None
        self._pending_files: Set[Path] = set()
        self._lock = None
    
    def start(self) -> None:
        """启动文件监控"""
        if self._running:
            return
        
        import threading
        self._lock = threading.Lock()
        
        try:
            from watchdog.observers import Observer
            from watchdog.events import FileSystemEventHandler, FileModifiedEvent
            
            watcher_self = self  # 避免闭包问题
            
            class Handler(FileSystemEventHandler):
                def on_modified(self, event):
                    if event.is_directory:
                        return
                    path = Path(event.src_path)
                    if watcher_self._matches_pattern(path):
                        watcher_self._queue_reload(path)
                
                def on_created(self, event):
                    if event.is_directory:
                        return
                    path = Path(event.src_path)
                    if watcher_self._matches_pattern(path):
                        watcher_self._queue_reload(path)
            
            self._observer = Observer()
            self._observer.schedule(Handler(), str(self.watch_dir), recursive=True)
            self._observer.start()
            self._running = True
            
        except ImportError:
            import logging
            logging.getLogger(__name__).warning(
                "watchdog not installed, hot reload disabled. "
                "Install with: pip install watchdog"
            )
    
    def stop(self) -> None:
        """停止文件监控"""
        if self._debounce_timer:
            self._debounce_timer.cancel()
            self._debounce_timer = None
        
        if self._observer:
            self._observer.stop()
            self._observer.join(timeout=2.0)
            self._observer = None
        
        self._running = False
        self._pending_files.clear()
    
    def _matches_pattern(self, path: Path) -> bool:
        """检查文件是否匹配模式"""
        import fnmatch
        name = path.name
        return any(fnmatch.fnmatch(name, pattern) for pattern in self.patterns)
    
    def _queue_reload(self, path: Path) -> None:
        """带防抖的重载队列"""
        import threading
        
        with self._lock:
            self._pending_files.add(path)
            
            if self._debounce_timer:
                self._debounce_timer.cancel()
            
            self._debounce_timer = threading.Timer(
                self.debounce_seconds,
                self._flush_pending
            )
            self._debounce_timer.start()
    
    def _flush_pending(self) -> None:
        """刷新待处理文件"""
        with self._lock:
            for path in self._pending_files:
                self.on_file_changed(path)
            self._pending_files.clear()
            self._debounce_timer = None


# 保留向后兼容的别名
PlaceholderHotReloadWatcher = FileSystemHotReloadWatcher


# 导出的公开 API
__all__ = [
    "HotReloadable",
    "HotReloadWatcher",
    "FileSystemHotReloadWatcher",
    "PlaceholderHotReloadWatcher",  # 向后兼容
    "register_reload_listener",
    "unregister_reload_listener",
    "notify_reload",
    "reload_module",
]
