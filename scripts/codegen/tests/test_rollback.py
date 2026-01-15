"""
Tests for rollback module
"""

import time
from datetime import datetime, timedelta
from pathlib import Path

import pytest

from scripts.codegen.rollback import RollbackManager, RollbackError


class TestRollbackManager:
    """RollbackManager 测试"""
    
    @pytest.fixture
    def manager(self):
        return RollbackManager()
    
    @pytest.fixture
    def sample_file(self, tmp_path):
        """创建测试文件"""
        path = tmp_path / "test.py"
        path.write_text("x = 1  # original")
        return path
    
    @pytest.fixture
    def sample_dir(self, tmp_path):
        """创建测试目录"""
        path = tmp_path / "test_dir"
        path.mkdir()
        (path / "file1.py").write_text("a = 1")
        (path / "file2.py").write_text("b = 2")
        return path
    
    # ===== save_last_good 测试 =====
    
    def test_save_last_good_file(self, manager, sample_file):
        """测试保存文件备份"""
        backup_path = manager.save_last_good(sample_file)
        
        assert backup_path.exists()
        assert ".bak" in backup_path.name
        assert backup_path.read_text() == "x = 1  # original"
    
    def test_save_last_good_dir(self, manager, sample_dir):
        """测试保存目录备份"""
        backup_path = manager.save_last_good(sample_dir)
        
        assert backup_path.exists()
        assert backup_path.is_dir()
        assert (backup_path / "file1.py").exists()
    
    def test_save_last_good_nonexistent(self, manager, tmp_path):
        """测试保存不存在的文件"""
        with pytest.raises(RollbackError):
            manager.save_last_good(tmp_path / "nonexistent.py")
    
    # ===== has_backup 测试 =====
    
    def test_has_backup_true(self, manager, sample_file):
        """测试存在备份"""
        manager.save_last_good(sample_file)
        assert manager.has_backup(sample_file) is True
    
    def test_has_backup_false(self, manager, sample_file):
        """测试不存在备份"""
        assert manager.has_backup(sample_file) is False
    
    # ===== rollback 测试 =====
    
    def test_rollback_file(self, manager, sample_file):
        """测试回退文件"""
        # 保存备份
        manager.save_last_good(sample_file)
        
        # 修改文件
        sample_file.write_text("x = 2  # modified")
        assert sample_file.read_text() == "x = 2  # modified"
        
        # 回退
        manager.rollback(sample_file)
        
        # 验证恢复
        assert sample_file.read_text() == "x = 1  # original"
    
    def test_rollback_deleted_file(self, manager, sample_file):
        """测试回退已删除的文件"""
        manager.save_last_good(sample_file)
        
        # 删除文件
        sample_file.unlink()
        assert not sample_file.exists()
        
        # 回退
        manager.rollback(sample_file)
        
        # 验证恢复
        assert sample_file.exists()
        assert sample_file.read_text() == "x = 1  # original"
    
    def test_rollback_no_backup(self, manager, sample_file):
        """测试没有备份时回退"""
        with pytest.raises(RollbackError):
            manager.rollback(sample_file)
    
    def test_rollback_dir(self, manager, sample_dir):
        """测试回退目录"""
        manager.save_last_good(sample_dir)
        
        # 修改目录内容
        (sample_dir / "file1.py").write_text("a = 999")
        (sample_dir / "file3.py").write_text("c = 3")
        
        # 回退
        manager.rollback(sample_dir)
        
        # 验证恢复
        assert (sample_dir / "file1.py").read_text() == "a = 1"
        assert not (sample_dir / "file3.py").exists()
    
    # ===== list_backups 测试 =====
    
    def test_list_backups(self, manager, sample_file):
        """测试列出备份"""
        # 创建多个备份（等待足够时间确保时间戳不同）
        manager.save_last_good(sample_file)
        time.sleep(1.1)  # 确保时间戳不同（秒级）
        sample_file.write_text("modified")
        manager.save_last_good(sample_file)
        
        backups = manager.list_backups(sample_file)
        
        assert len(backups) >= 1  # 至少有一个备份
        # 如果有多个，应该按时间倒序
        if len(backups) > 1:
            assert backups[0].stat().st_mtime >= backups[1].stat().st_mtime
    
    # ===== cleanup_backups 测试 =====
    
    def test_cleanup_backups_keeps_recent(self, manager, sample_file):
        """测试清理保留最近的备份"""
        manager.save_last_good(sample_file)
        
        deleted = manager.cleanup_backups(max_age_days=7, path=sample_file)
        
        assert deleted == 0  # 新备份不应被删除
        assert manager.has_backup(sample_file)
    
    def test_cleanup_backups_keeps_minimum(self, manager, sample_file):
        """测试清理保留最少 N 个备份"""
        # 创建备份
        manager.save_last_good(sample_file)
        
        # 清理但保留至少 1 个
        deleted = manager.cleanup_backups(max_age_days=0, path=sample_file, keep_latest=1)
        
        remaining = manager.list_backups(sample_file)
        # 至少保留一个最新的
        assert len(remaining) >= 1
    
    # ===== get_backup_info 测试 =====
    
    def test_get_backup_info(self, manager, sample_file):
        """测试获取备份信息"""
        manager.save_last_good(sample_file)
        
        info = manager.get_backup_info(sample_file)
        
        assert info is not None
        assert "path" in info
        assert "timestamp" in info
        assert info["is_directory"] is False
    
    def test_get_backup_info_no_backup(self, manager, sample_file):
        """测试无备份时获取信息"""
        info = manager.get_backup_info(sample_file)
        assert info is None


class TestRollbackManagerWithBackupDir:
    """使用指定备份目录的测试"""
    
    @pytest.fixture
    def backup_dir(self, tmp_path):
        path = tmp_path / "backups"
        path.mkdir()
        return path
    
    @pytest.fixture
    def manager(self, backup_dir):
        return RollbackManager(backup_dir=backup_dir)
    
    def test_backup_in_specified_dir(self, manager, backup_dir, tmp_path):
        """测试备份保存到指定目录"""
        source = tmp_path / "source.py"
        source.write_text("content")
        
        backup_path = manager.save_last_good(source)
        
        assert backup_path.parent == backup_dir
    
    def test_rollback_from_specified_dir(self, manager, backup_dir, tmp_path):
        """测试从指定目录回退"""
        source = tmp_path / "source.py"
        source.write_text("original")
        
        manager.save_last_good(source)
        source.write_text("modified")
        
        manager.rollback(source)
        
        assert source.read_text() == "original"
