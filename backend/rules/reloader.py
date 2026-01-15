"""
Rule Reloader - 规则热重载器

对照 design.md §6 RuleReloader
对照 Requirement 13: Hot Reload
"""

from __future__ import annotations

import hashlib
import importlib
import logging
import sys
import threading
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING, Any, Callable, Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from scripts.codegen.rule_generator import RuleCodeGenerator
    from backend.rules.engine import RuleEngine


class ReloadEvent:
    """重载事件类型"""
    RULE_RELOADED = "rule_reloaded"
    RULE_RELOAD_FAILED = "rule_reload_failed"


class RuleReloader:
    """
    规则热重载器
    
    监控规则文件变更，自动触发重新编译和加载。
    """
    
    def __init__(
        self,
        watch_dir: Path = Path("data/rules"),
        codegen: Optional["RuleCodeGenerator"] = None,
        engine: Optional["RuleEngine"] = None,
        watch_patterns: Optional[List[str]] = None,
    ):
        self.watch_dir = Path(watch_dir)
        self._codegen = codegen
        self.engine = engine
        
        # T-6-3-03: 支持多种文件类型监控
        self.watch_patterns = watch_patterns or [".jsonl", ".py"]
        
        self._observer = None
        self._reload_history: List[Dict] = []
        self._previous_versions: Dict[str, str] = {}  # file_path -> content_hash
        self._event_callbacks: Dict[str, List[Callable]] = {
            ReloadEvent.RULE_RELOADED: [],
            ReloadEvent.RULE_RELOAD_FAILED: [],
        }
        self._reload_lock = threading.RLock()
        
        # T-6-3-02: 回滚机制
        self._version_backups: Dict[str, bytes] = {}  # backup_hash -> content
        self._file_to_backup: Dict[str, str] = {}  # file_path -> backup_hash
        self._max_backups = 5
    
    @property
    def codegen(self) -> "RuleCodeGenerator":
        if self._codegen is None:
            from scripts.codegen.rule_generator import RuleCodeGenerator
            self._codegen = RuleCodeGenerator()
        return self._codegen
    
    def start(self) -> None:
        """启动文件监控"""
        if self._observer is not None:
            return
        
        try:
            from watchdog.observers import Observer
            from watchdog.events import FileSystemEventHandler
            
            class Handler(FileSystemEventHandler):
                def __init__(inner_self, reloader):
                    inner_self.reloader = reloader
                
                def on_modified(inner_self, event):
                    if event.is_directory:
                        return
                    path = Path(event.src_path)
                    # T-6-3-03: 支持多种文件类型
                    if path.suffix in inner_self.reloader.watch_patterns:
                        if path.suffix == ".jsonl":
                            inner_self.reloader.reload_file(path)
                        elif path.suffix == ".py":
                            inner_self.reloader.reload_python_module(path)
            
            self._observer = Observer()
            self._observer.schedule(Handler(self), str(self.watch_dir), recursive=True)
            self._observer.start()
            logger.info(f"RuleReloader started: {self.watch_dir}")
        except ImportError:
            logger.warning("watchdog not installed, hot reload disabled")
    
    def stop(self) -> None:
        """停止文件监控"""
        if self._observer:
            self._observer.stop()
            self._observer.join()
            self._observer = None
            logger.info("RuleReloader stopped")
    
    def reload_file(self, file_path: Path) -> bool:
        """
        重载单个规则文件
        
        T-6-3-02: 添加回滚支持
        """
        with self._reload_lock:
            backup_hash = None
            
            try:
                # 1. 备份当前版本
                backup_hash = self._backup_current(file_path)
                
                # 2. 编译规则
                report = self.codegen.compile_jsonl(file_path)
                
                if report["errors"]:
                    self._log_reload(file_path, False, str(report["errors"]))
                    self._emit_event(ReloadEvent.RULE_RELOAD_FAILED, {
                        "file": str(file_path), "errors": report["errors"]
                    })
                    return False
                
                # 3. 重新加载模块
                for output in report.get("output_files", []):
                    self._reload_module(Path(output))
                
                # 4. 成功，清除旧备份
                self._log_reload(file_path, True)
                self._emit_event(ReloadEvent.RULE_RELOADED, {
                    "file": str(file_path), "rules": report["rules_compiled"]
                })
                return True
                
            except Exception as e:
                logger.error(f"Reload failed: {file_path}: {e}")
                
                # 回滚到上一版本
                if backup_hash:
                    rollback_success = self._rollback(file_path, backup_hash)
                    if rollback_success:
                        logger.info(f"Rolled back to previous version: {file_path}")
                
                self._log_reload(file_path, False, str(e))
                return False
    
    def _backup_current(self, file_path: Path) -> Optional[str]:
        """
        备份当前版本到内存
        
        Returns:
            backup_hash: 备份的哈希值
        """
        if not file_path.exists():
            return None
        
        try:
            content = file_path.read_bytes()
            hash_key = hashlib.sha256(content).hexdigest()[:16]
            
            # 存储备份
            self._version_backups[hash_key] = content
            self._file_to_backup[str(file_path)] = hash_key
            
            # 保留最近 N 个版本
            while len(self._version_backups) > self._max_backups:
                oldest_key = next(iter(self._version_backups))
                del self._version_backups[oldest_key]
                # 清理映射
                for fp, bh in list(self._file_to_backup.items()):
                    if bh == oldest_key:
                        del self._file_to_backup[fp]
            
            return hash_key
        except Exception as e:
            logger.warning(f"Failed to backup: {file_path}: {e}")
            return None
    
    def _rollback(self, file_path: Path, backup_hash: str) -> bool:
        """
        回滚到指定版本
        
        Args:
            file_path: 要回滚的文件
            backup_hash: 备份哈希
            
        Returns:
            True 如果回滚成功
        """
        if backup_hash not in self._version_backups:
            logger.warning(f"Backup not found: {backup_hash}")
            return False
        
        try:
            content = self._version_backups[backup_hash]
            file_path.write_bytes(content)
            logger.info(f"Restored backup: {file_path}")
            return True
        except Exception as e:
            logger.error(f"Rollback failed: {file_path}: {e}")
            return False
    
    def get_backup_count(self) -> int:
        """获取当前备份数量"""
        return len(self._version_backups)
    
    def reload_python_module(self, file_path: Path) -> bool:
        """
        热重载 Python 模块
        
        T-6-3-03: 支持 .py 文件热重载
        """
        with self._reload_lock:
            try:
                self._reload_module(file_path)
                
                self._log_reload(file_path, True)
                self._emit_event(ReloadEvent.RULE_RELOADED, {
                    "file": str(file_path), "type": "python_module"
                })
                logger.info(f"Python module reloaded: {file_path}")
                return True
                
            except Exception as e:
                logger.error(f"Python module reload failed: {file_path}: {e}")
                self._log_reload(file_path, False, str(e))
                self._emit_event(ReloadEvent.RULE_RELOAD_FAILED, {
                    "file": str(file_path), "error": str(e)
                })
                return False
    
    def _reload_module(self, module_path: Path) -> None:
        """重新加载Python模块"""
        try:
            relative = module_path.relative_to(Path.cwd())
            module_name = str(relative.with_suffix("")).replace("/", ".").replace("\\", ".")
            
            if module_name in sys.modules:
                importlib.reload(sys.modules[module_name])
            else:
                importlib.import_module(module_name)
        except Exception as e:
            logger.warning(f"Module reload failed: {e}")
    
    def _log_reload(self, file_path: Path, success: bool, error: Optional[str] = None):
        """记录重载历史"""
        self._reload_history.append({
            "file": str(file_path),
            "timestamp": datetime.now().isoformat(),
            "success": success,
            "error": error,
        })
        if len(self._reload_history) > 100:
            self._reload_history = self._reload_history[-100:]
    
    def get_reload_history(self) -> List[Dict]:
        """获取重载历史"""
        return self._reload_history.copy()
    
    def on_event(self, event_type: str, callback: Callable) -> None:
        """注册事件回调"""
        if event_type in self._event_callbacks:
            self._event_callbacks[event_type].append(callback)
    
    def _emit_event(self, event_type: str, data: Dict) -> None:
        """触发事件"""
        for cb in self._event_callbacks.get(event_type, []):
            try:
                cb(data)
            except Exception as e:
                logger.error(f"Callback error: {e}")
