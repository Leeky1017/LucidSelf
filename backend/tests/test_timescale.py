# backend/tests/test_timescale.py
"""
TimescaleDB Integration Tests

测试 TimescaleDB 扩展功能。
"""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from datetime import datetime

from backend.db.timescale import (
    init_timescale,
    create_hypertable,
    add_retention_policy,
    enable_compression,
    setup_timescale_for_memory,
    is_timescale_available,
)


class TestInitTimescale:
    """TimescaleDB 初始化测试"""
    
    @pytest.mark.asyncio
    async def test_init_timescale_success(self):
        """测试成功初始化"""
        mock_conn = AsyncMock()
        mock_result = MagicMock()
        mock_result.fetchone.return_value = ("2.13.0",)
        mock_conn.execute.return_value = mock_result
        
        # 创建 async context manager mock
        mock_context = AsyncMock()
        mock_context.__aenter__.return_value = mock_conn
        mock_context.__aexit__.return_value = None
        
        mock_engine = MagicMock()
        mock_engine.begin.return_value = mock_context
        
        with patch("backend.db.timescale.engine", mock_engine):
            result = await init_timescale()
            assert result is True
            
            # 验证创建扩展被调用
            calls = mock_conn.execute.call_args_list
            assert len(calls) >= 1
    
    @pytest.mark.asyncio
    async def test_init_timescale_not_available(self):
        """测试扩展不可用"""
        mock_conn = AsyncMock()
        mock_result = MagicMock()
        mock_result.fetchone.return_value = None
        mock_conn.execute.return_value = mock_result
        
        mock_context = AsyncMock()
        mock_context.__aenter__.return_value = mock_conn
        mock_context.__aexit__.return_value = None
        
        mock_engine = MagicMock()
        mock_engine.begin.return_value = mock_context
        
        with patch("backend.db.timescale.engine", mock_engine):
            result = await init_timescale()
            assert result is False
    
    @pytest.mark.asyncio
    async def test_init_timescale_error(self):
        """测试初始化错误处理"""
        mock_engine = AsyncMock()
        mock_engine.begin.side_effect = Exception("Connection failed")
        
        with patch("backend.db.timescale.engine", mock_engine):
            result = await init_timescale()
            assert result is False


class TestCreateHypertable:
    """超表创建测试"""
    
    @pytest.mark.asyncio
    async def test_create_hypertable_new_table(self):
        """测试新表转超表"""
        mock_session = AsyncMock()
        mock_result = MagicMock()
        mock_result.scalar.return_value = False  # 不是超表
        mock_session.execute.return_value = mock_result
        
        mock_session_maker = MagicMock()
        mock_session_maker.return_value.__aenter__.return_value = mock_session
        
        with patch("backend.db.timescale.async_session_maker", mock_session_maker):
            result = await create_hypertable("memory_events", "created_at")
            assert result is True
            
            # 验证 commit 被调用
            mock_session.commit.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_create_hypertable_already_exists(self):
        """测试表已是超表时跳过"""
        mock_session = AsyncMock()
        mock_result = MagicMock()
        mock_result.scalar.return_value = True  # 已是超表
        mock_session.execute.return_value = mock_result
        
        mock_session_maker = MagicMock()
        mock_session_maker.return_value.__aenter__.return_value = mock_session
        
        with patch("backend.db.timescale.async_session_maker", mock_session_maker):
            result = await create_hypertable("memory_events", "created_at", if_not_exists=True)
            assert result is True
            
            # 验证只调用了检查，没有创建
            assert mock_session.execute.call_count == 1
    
    @pytest.mark.asyncio
    async def test_create_hypertable_custom_interval(self):
        """测试自定义分区间隔"""
        mock_session = AsyncMock()
        mock_result = MagicMock()
        mock_result.scalar.return_value = False
        mock_session.execute.return_value = mock_result
        
        mock_session_maker = MagicMock()
        mock_session_maker.return_value.__aenter__.return_value = mock_session
        
        with patch("backend.db.timescale.async_session_maker", mock_session_maker):
            result = await create_hypertable(
                "memory_events", 
                "created_at",
                chunk_interval="30 days"
            )
            assert result is True


class TestRetentionPolicy:
    """数据保留策略测试"""
    
    @pytest.mark.asyncio
    async def test_add_retention_policy_success(self):
        """测试添加保留策略"""
        mock_session = AsyncMock()
        mock_session_maker = MagicMock()
        mock_session_maker.return_value.__aenter__.return_value = mock_session
        
        with patch("backend.db.timescale.async_session_maker", mock_session_maker):
            result = await add_retention_policy("memory_events", "90 days")
            assert result is True
            mock_session.commit.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_add_retention_policy_error(self):
        """测试保留策略错误处理"""
        mock_session = AsyncMock()
        mock_session.execute.side_effect = Exception("Policy error")
        mock_session_maker = MagicMock()
        mock_session_maker.return_value.__aenter__.return_value = mock_session
        
        with patch("backend.db.timescale.async_session_maker", mock_session_maker):
            result = await add_retention_policy("nonexistent_table", "90 days")
            assert result is False


class TestCompression:
    """压缩功能测试"""
    
    @pytest.mark.asyncio
    async def test_enable_compression_success(self):
        """测试启用压缩"""
        mock_session = AsyncMock()
        mock_session_maker = MagicMock()
        mock_session_maker.return_value.__aenter__.return_value = mock_session
        
        with patch("backend.db.timescale.async_session_maker", mock_session_maker):
            result = await enable_compression(
                "memory_events",
                segment_by="user_id",
                compress_after="7 days"
            )
            assert result is True
            mock_session.commit.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_enable_compression_custom_orderby(self):
        """测试自定义排序"""
        mock_session = AsyncMock()
        mock_session_maker = MagicMock()
        mock_session_maker.return_value.__aenter__.return_value = mock_session
        
        with patch("backend.db.timescale.async_session_maker", mock_session_maker):
            result = await enable_compression(
                "memory_events",
                segment_by="user_id",
                order_by="created_at ASC",
                compress_after="14 days"
            )
            assert result is True


class TestSetupTimescaleForMemory:
    """记忆层 TimescaleDB 配置测试"""
    
    @pytest.mark.asyncio
    async def test_setup_full_success(self):
        """测试完整配置成功"""
        with patch("backend.db.timescale.init_timescale", return_value=True), \
             patch("backend.db.timescale.create_hypertable", return_value=True), \
             patch("backend.db.timescale.add_retention_policy", return_value=True), \
             patch("backend.db.timescale.enable_compression", return_value=True):
            
            report = await setup_timescale_for_memory()
            
            assert report["timescale_init"] is True
            assert report["memory_events"]["hypertable"] is True
            assert report["memory_events"]["retention"] is True
            assert report["memory_events"]["compression"] is True
            assert report["memory_insights"]["hypertable"] is True
            assert report["memory_insights"]["compression"] is True
    
    @pytest.mark.asyncio
    async def test_setup_timescale_unavailable(self):
        """测试 TimescaleDB 不可用时的处理"""
        with patch("backend.db.timescale.init_timescale", return_value=False):
            
            report = await setup_timescale_for_memory()
            
            assert report["timescale_init"] is False
            # 其他配置应该未执行 (保持默认 False)
            assert report["memory_events"]["hypertable"] is False
    
    @pytest.mark.asyncio
    async def test_setup_partial_failure(self):
        """测试部分失败"""
        with patch("backend.db.timescale.init_timescale", return_value=True), \
             patch("backend.db.timescale.create_hypertable", side_effect=[True, False]), \
             patch("backend.db.timescale.add_retention_policy", return_value=True), \
             patch("backend.db.timescale.enable_compression", return_value=True):
            
            report = await setup_timescale_for_memory()
            
            assert report["timescale_init"] is True
            assert report["memory_events"]["hypertable"] is True
            assert report["memory_insights"]["hypertable"] is False


class TestIsTimescaleAvailable:
    """TimescaleDB 可用性检查测试"""
    
    @pytest.mark.asyncio
    async def test_available(self):
        """测试扩展已安装"""
        mock_conn = AsyncMock()
        mock_result = MagicMock()
        mock_result.scalar.return_value = True
        mock_conn.execute.return_value = mock_result
        
        mock_context = AsyncMock()
        mock_context.__aenter__.return_value = mock_conn
        mock_context.__aexit__.return_value = None
        
        mock_engine = MagicMock()
        mock_engine.begin.return_value = mock_context
        
        with patch("backend.db.timescale.engine", mock_engine):
            result = await is_timescale_available()
            assert result is True
    
    @pytest.mark.asyncio
    async def test_not_available(self):
        """测试扩展未安装"""
        mock_conn = AsyncMock()
        mock_result = MagicMock()
        mock_result.scalar.return_value = False
        mock_conn.execute.return_value = mock_result
        
        mock_context = AsyncMock()
        mock_context.__aenter__.return_value = mock_conn
        mock_context.__aexit__.return_value = None
        
        mock_engine = MagicMock()
        mock_engine.begin.return_value = mock_context
        
        with patch("backend.db.timescale.engine", mock_engine):
            result = await is_timescale_available()
            assert result is False
    
    @pytest.mark.asyncio
    async def test_connection_error(self):
        """测试连接错误"""
        mock_engine = AsyncMock()
        mock_engine.begin.side_effect = Exception("Connection refused")
        
        with patch("backend.db.timescale.engine", mock_engine):
            result = await is_timescale_available()
            assert result is False


class TestSubscriptionIndex:
    """Subscription 复合索引测试"""
    
    def test_index_exists_in_model(self):
        """验证索引定义存在"""
        from backend.models.subscription import Subscription
        
        # 检查 __table_args__ 是否存在
        assert hasattr(Subscription, "__table_args__")
        
        # 检查索引名称
        table_args = Subscription.__table_args__
        index_names = [idx.name for idx in table_args if hasattr(idx, 'name')]
        assert 'ix_sub_status_tier_expires' in index_names
    
    def test_index_columns(self):
        """验证索引列"""
        from backend.models.subscription import Subscription
        
        table_args = Subscription.__table_args__
        for idx in table_args:
            if hasattr(idx, 'name') and idx.name == 'ix_sub_status_tier_expires':
                # 获取索引列名
                column_names = [col.name for col in idx.columns]
                assert 'status' in column_names
                assert 'tier' in column_names
                assert 'expires_at' in column_names
