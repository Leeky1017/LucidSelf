"""
BackupManager - 备份与回滚管理器

自动备份和回滚逻辑链构建结果。
"""

import os
import shutil
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Optional

from scripts.logic_chain_builder.logging_config import get_logger

logger = get_logger(__name__)


class BackupManager:
    """
    备份与回滚管理器
    
    负责:
    - 创建时间戳备份
    - 失败时自动回滚
    - 清理旧备份
    """
    
    MAX_BACKUPS_PER_BOOK = 3
    RETENTION_DAYS = 7
    LOGIC_CHAINS_DIR = "data/logic_chains"
    ARCHIVE_DIR = "data/logic_chains/archive"
    
    def __init__(
        self,
        logic_chains_dir: str = None,
        archive_dir: str = None
    ):
        """
        初始化备份管理器
        
        Args:
            logic_chains_dir: 逻辑链目录
            archive_dir: 归档目录
        """
        self.logic_chains_dir = Path(logic_chains_dir or self.LOGIC_CHAINS_DIR)
        self.archive_dir = Path(archive_dir or self.ARCHIVE_DIR)
    
    def create_backup(self, book_id: str) -> Optional[str]:
        """
        创建备份
        
        Args:
            book_id: 书籍ID
            
        Returns:
            备份文件路径，如果源文件不存在则返回None
        """
        source_path = self.logic_chains_dir / f"{book_id}.yaml"
        
        if not source_path.exists():
            logger.debug(f"No existing file to backup for {book_id}")
            return None
        
        # 创建时间戳备份
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = self.logic_chains_dir / f"{book_id}.{timestamp}.bak"
        
        try:
            shutil.copy2(str(source_path), str(backup_path))
            logger.info(f"Created backup: {backup_path}")
        except Exception as e:
            logger.error(f"Failed to create backup for {book_id}: {e}")
            return None
        
        # 清理旧备份
        self._cleanup_old_backups(book_id)
        
        return str(backup_path)
    
    def rollback(self, book_id: str, reason: str) -> bool:
        """
        回滚到最近的备份
        
        Args:
            book_id: 书籍ID
            reason: 回滚原因
            
        Returns:
            是否成功回滚
        """
        backups = self._find_backups(book_id)
        if not backups:
            logger.warning(f"No backups found for {book_id}")
            return False
        
        # 获取最新备份
        latest_backup = max(backups, key=lambda p: p.stat().st_mtime)
        
        # 保留失败的构建用于调试
        current_path = self.logic_chains_dir / f"{book_id}.yaml"
        failed_path = self.logic_chains_dir / f"{book_id}.failed.yaml"
        
        try:
            if current_path.exists():
                shutil.move(str(current_path), str(failed_path))
            
            # 恢复备份
            shutil.copy2(str(latest_backup), str(current_path))
            
            logger.warning(f"Rolled back {book_id}: {reason}")
            return True
        except Exception as e:
            logger.error(f"Failed to rollback {book_id}: {e}")
            return False
    
    def _find_backups(self, book_id: str) -> List[Path]:
        """查找所有备份文件"""
        pattern = f"{book_id}.*.bak"
        return list(self.logic_chains_dir.glob(pattern))
    
    def _cleanup_old_backups(self, book_id: str):
        """清理旧备份"""
        backups = self._find_backups(book_id)
        
        if not backups:
            return
        
        # 只保留最新的MAX_BACKUPS_PER_BOOK个
        if len(backups) > self.MAX_BACKUPS_PER_BOOK:
            sorted_backups = sorted(
                backups,
                key=lambda p: p.stat().st_mtime,
                reverse=True
            )
            for old_backup in sorted_backups[self.MAX_BACKUPS_PER_BOOK:]:
                self._archive_backup(old_backup)
        
        # 归档超过RETENTION_DAYS的备份
        cutoff = datetime.now() - timedelta(days=self.RETENTION_DAYS)
        for backup in backups:
            mtime = datetime.fromtimestamp(backup.stat().st_mtime)
            if mtime < cutoff:
                self._archive_backup(backup)
    
    def _archive_backup(self, backup_path: Path):
        """移动备份到归档目录"""
        try:
            self.archive_dir.mkdir(parents=True, exist_ok=True)
            dest = self.archive_dir / backup_path.name
            shutil.move(str(backup_path), str(dest))
            logger.info(f"Archived backup: {backup_path.name}")
        except Exception as e:
            logger.error(f"Failed to archive {backup_path}: {e}")
    
    def cleanup_all_old_backups(self):
        """
        清理所有旧备份文件
        
        将所有现有.bak文件移动到archive目录
        """
        self.archive_dir.mkdir(parents=True, exist_ok=True)
        
        bak_files = list(self.logic_chains_dir.glob("*.bak"))
        archived_count = 0
        
        for bak_file in bak_files:
            try:
                dest = self.archive_dir / bak_file.name
                shutil.move(str(bak_file), str(dest))
                archived_count += 1
            except Exception as e:
                logger.error(f"Failed to archive {bak_file}: {e}")
        
        logger.info(f"Archived {archived_count} backup files to {self.archive_dir}")
        return archived_count


# 导出
__all__ = ["BackupManager"]
