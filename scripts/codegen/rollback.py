"""
Codegen Rollback Module

回退管理器，用于：
1. 保存成功编译的版本作为备份
2. 编译失败时回退到上次成功版本
3. 清理过期备份文件
"""

import shutil
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Optional

from .exceptions import CodegenError


class RollbackError(CodegenError):
    """回退操作异常"""
    pass


class RollbackManager:
    """
    回退管理器
    
    管理代码生成产物的备份与回退，确保编译失败时可以恢复到上次成功状态。
    
    备份策略：
    - 每次成功编译后保存 .bak 备份
    - 支持按文件或整个目录备份
    - 自动清理过期备份（默认7天）
    
    Example:
        manager = RollbackManager()
        
        # 编译前保存当前版本
        if output_path.exists():
            manager.save_last_good(output_path)
        
        try:
            # 执行编译
            compile_rules(input_path, output_path)
        except CompilationError:
            # 编译失败，回退
            if manager.has_backup(output_path):
                manager.rollback(output_path)
    """
    
    BACKUP_SUFFIX = ".bak"
    TIMESTAMP_FORMAT = "%Y%m%d_%H%M%S"
    
    def __init__(self, backup_dir: Optional[Path] = None):
        """
        初始化回退管理器
        
        Args:
            backup_dir: 备份目录，默认使用源文件同目录
        """
        self.backup_dir = backup_dir
    
    def _get_backup_path(self, path: Path) -> Path:
        """获取备份文件路径"""
        if self.backup_dir:
            backup_dir = self.backup_dir
        else:
            backup_dir = path.parent
        
        timestamp = datetime.now().strftime(self.TIMESTAMP_FORMAT)
        backup_name = f"{path.name}{self.BACKUP_SUFFIX}.{timestamp}"
        return backup_dir / backup_name
    
    def _get_latest_backup(self, path: Path) -> Optional[Path]:
        """获取最新的备份文件"""
        if self.backup_dir:
            search_dir = self.backup_dir
        else:
            search_dir = path.parent
        
        pattern = f"{path.name}{self.BACKUP_SUFFIX}.*"
        backups = sorted(search_dir.glob(pattern), reverse=True)
        
        return backups[0] if backups else None
    
    def save_last_good(self, path: Path) -> Path:
        """
        保存成功版本到备份
        
        将当前文件或目录保存为 .bak 备份，附带时间戳。
        
        Args:
            path: 要备份的文件或目录路径
            
        Returns:
            备份文件路径
            
        Raises:
            RollbackError: 备份操作失败
        """
        if not path.exists():
            raise RollbackError(
                f"Cannot backup non-existent path: {path}",
                source_file=str(path)
            )
        
        backup_path = self._get_backup_path(path)
        
        try:
            if path.is_dir():
                shutil.copytree(path, backup_path)
            else:
                shutil.copy2(path, backup_path)
            
            return backup_path
        except Exception as e:
            raise RollbackError(
                f"Failed to create backup: {e}",
                source_file=str(path),
                details={"backup_path": str(backup_path)}
            )
    
    def rollback(self, path: Path) -> bool:
        """
        回退到上次成功版本
        
        从最新备份恢复文件或目录。
        
        Args:
            path: 要恢复的目标路径
            
        Returns:
            True 如果回退成功
            
        Raises:
            RollbackError: 回退操作失败或无备份可用
        """
        backup_path = self._get_latest_backup(path)
        
        if not backup_path:
            raise RollbackError(
                f"No backup found for: {path}",
                source_file=str(path)
            )
        
        try:
            # 删除当前版本（如果存在）
            if path.exists():
                if path.is_dir():
                    shutil.rmtree(path)
                else:
                    path.unlink()
            
            # 恢复备份
            if backup_path.is_dir():
                shutil.copytree(backup_path, path)
            else:
                shutil.copy2(backup_path, path)
            
            return True
        except Exception as e:
            raise RollbackError(
                f"Failed to rollback: {e}",
                source_file=str(path),
                details={"backup_path": str(backup_path)}
            )
    
    def has_backup(self, path: Path) -> bool:
        """
        检查是否存在备份
        
        Args:
            path: 要检查的文件或目录路径
            
        Returns:
            True 如果存在备份
        """
        return self._get_latest_backup(path) is not None
    
    def list_backups(self, path: Path) -> List[Path]:
        """
        列出所有备份
        
        Args:
            path: 原始文件或目录路径
            
        Returns:
            备份文件列表，按时间倒序排列
        """
        if self.backup_dir:
            search_dir = self.backup_dir
        else:
            search_dir = path.parent
        
        pattern = f"{path.name}{self.BACKUP_SUFFIX}.*"
        return sorted(search_dir.glob(pattern), reverse=True)
    
    def cleanup_backups(
        self, 
        max_age_days: int = 7,
        path: Optional[Path] = None,
        keep_latest: int = 1
    ) -> int:
        """
        清理过期备份
        
        删除超过指定天数的备份文件，同时保留最近的 N 个备份。
        
        Args:
            max_age_days: 备份最大保留天数，默认7天
            path: 如果指定，只清理该路径的备份；否则清理备份目录下所有备份
            keep_latest: 至少保留最近的 N 个备份，默认1个
            
        Returns:
            删除的备份数量
        """
        cutoff_time = datetime.now() - timedelta(days=max_age_days)
        deleted_count = 0
        
        if path:
            backups = self.list_backups(path)
            # 保留最近的 N 个
            backups_to_check = backups[keep_latest:]
        else:
            if not self.backup_dir:
                return 0
            backups_to_check = list(self.backup_dir.glob(f"*{self.BACKUP_SUFFIX}.*"))
        
        for backup in backups_to_check:
            try:
                # 从文件名解析时间戳
                timestamp_str = backup.suffix.lstrip(".")
                backup_time = datetime.strptime(timestamp_str, self.TIMESTAMP_FORMAT)
                
                if backup_time < cutoff_time:
                    if backup.is_dir():
                        shutil.rmtree(backup)
                    else:
                        backup.unlink()
                    deleted_count += 1
            except (ValueError, OSError):
                # 无法解析时间戳或删除失败，跳过
                continue
        
        return deleted_count
    
    def get_backup_info(self, path: Path) -> Optional[dict]:
        """
        获取最新备份信息
        
        Args:
            path: 原始文件或目录路径
            
        Returns:
            包含备份信息的字典，如果无备份则返回 None
        """
        backup = self._get_latest_backup(path)
        if not backup:
            return None
        
        try:
            timestamp_str = backup.suffix.lstrip(".")
            backup_time = datetime.strptime(timestamp_str, self.TIMESTAMP_FORMAT)
        except ValueError:
            backup_time = None
        
        return {
            "path": backup,
            "size": backup.stat().st_size if backup.is_file() else None,
            "timestamp": backup_time,
            "is_directory": backup.is_dir(),
        }
