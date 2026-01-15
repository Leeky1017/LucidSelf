"""
Memory Service Tests

对照 tasks.md 5.5, 5.6:
- Requirements: 4.3.1-4.3.3, 8.1.1
- ⚠️ 陷阱: 所有访问必须经过 service，不能直接访问存储
"""

import pytest
from datetime import datetime, timedelta
from hypothesis import given, strategies as st, settings

from backend.services.memory.models import PrivacyLevel, MemoryEvent
from backend.services.memory.service import (
    MemoryService,
    AccessDeniedError,
    RecordNotFoundError,
)


class TestEventOperations:
    """事件操作测试"""
    
    @pytest.mark.asyncio
    async def test_record_event_basic(self, memory_service):
        """测试基本事件记录"""
        event_id = await memory_service.record_event(
            user_id="user_001",
            event_type="analysis",
            data={"birth_data": "1990-01-01"},
        )
        
        assert event_id.startswith("evt_")
    
    @pytest.mark.asyncio
    async def test_get_event(self, memory_service):
        """测试获取事件"""
        event_id = await memory_service.record_event(
            user_id="user_001",
            event_type="analysis",
            data={"key": "value"},
        )
        
        event = await memory_service.get_event(event_id, user_id="user_001")
        
        assert event.event_id == event_id
        assert event.user_id == "user_001"
        assert event.event_type == "analysis"
        assert event.data["key"] == "value"
    
    @pytest.mark.asyncio
    async def test_get_event_not_found(self, memory_service):
        """测试获取不存在的事件"""
        with pytest.raises(RecordNotFoundError):
            await memory_service.get_event("evt_nonexistent", user_id="user_001")
    
    @pytest.mark.asyncio
    async def test_get_events_by_user(self, memory_service):
        """测试按用户获取事件"""
        # 记录多个事件
        await memory_service.record_event(
            user_id="user_001",
            event_type="analysis",
            data={"index": 1},
        )
        await memory_service.record_event(
            user_id="user_001",
            event_type="playbook",
            data={"index": 2},
        )
        await memory_service.record_event(
            user_id="user_002",
            event_type="analysis",
            data={"index": 3},
        )
        
        events = await memory_service.get_events(user_id="user_001")
        
        assert len(events) == 2
        assert all(e.user_id == "user_001" for e in events)
    
    @pytest.mark.asyncio
    async def test_get_events_by_type(self, memory_service):
        """测试按类型过滤事件"""
        await memory_service.record_event(
            user_id="user_001",
            event_type="analysis",
            data={},
        )
        await memory_service.record_event(
            user_id="user_001",
            event_type="playbook",
            data={},
        )
        
        events = await memory_service.get_events(
            user_id="user_001",
            event_type="analysis",
        )
        
        assert len(events) == 1
        assert events[0].event_type == "analysis"


class TestPrivacyLevel:
    """隐私级别测试"""
    
    @pytest.mark.asyncio
    async def test_public_event_accessible(self, memory_service):
        """测试 PUBLIC 事件可访问"""
        event_id = await memory_service.record_event(
            user_id="user_001",
            event_type="analysis",
            data={"public_data": True},
            privacy_level=PrivacyLevel.PUBLIC,
        )
        
        # 其他用户也可访问 PUBLIC 数据
        # (在当前实现中只是标记，实际访问控制依赖业务逻辑)
        event = await memory_service.get_event(event_id, user_id="user_001")
        assert event.privacy_level == PrivacyLevel.PUBLIC
    
    @pytest.mark.asyncio
    async def test_private_event_owner_only(self, memory_service):
        """测试 PRIVATE 事件仅 owner 可访问"""
        event_id = await memory_service.record_event(
            user_id="user_001",
            event_type="analysis",
            data={"private_data": True},
            privacy_level=PrivacyLevel.PRIVATE,
        )
        
        # Owner 可以访问
        event = await memory_service.get_event(event_id, user_id="user_001")
        assert event is not None
        
        # 其他用户不能访问
        with pytest.raises(AccessDeniedError):
            await memory_service.get_event(event_id, user_id="user_002")
    
    @pytest.mark.asyncio
    async def test_sensitive_event_encrypted(self, memory_service):
        """测试 SENSITIVE 事件被加密"""
        sensitive_data = {"secret": "password123", "ssn": "123-45-6789"}
        
        event_id = await memory_service.record_event(
            user_id="user_001",
            event_type="analysis",
            data=sensitive_data,
            privacy_level=PrivacyLevel.SENSITIVE,
        )
        
        # 内部存储应该是加密的
        raw_event = memory_service._events[event_id]
        assert "__encrypted__" in raw_event.data
        
        # 但通过 service 获取时会解密
        event = await memory_service.get_event(event_id, user_id="user_001")
        assert event.data["secret"] == "password123"


class TestInsightOperations:
    """洞察操作测试"""
    
    @pytest.mark.asyncio
    async def test_create_insight(self, memory_service):
        """测试创建洞察"""
        insight_id = await memory_service.create_insight(
            user_id="user_001",
            summary="用户在事业方面表现出较强的进取心",
            source_events=["evt_001", "evt_002"],
            confidence=0.85,
            dimension="career",
        )
        
        assert insight_id.startswith("ins_")
    
    @pytest.mark.asyncio
    async def test_get_insights(self, memory_service):
        """测试获取洞察"""
        await memory_service.create_insight(
            user_id="user_001",
            summary="Career insight",
            source_events=[],
            dimension="career",
            confidence=0.9,
        )
        await memory_service.create_insight(
            user_id="user_001",
            summary="Emotion insight",
            source_events=[],
            dimension="emotion",
            confidence=0.7,
        )
        
        insights = await memory_service.get_insights(user_id="user_001")
        
        assert len(insights) == 2
    
    @pytest.mark.asyncio
    async def test_get_insights_by_dimension(self, memory_service):
        """测试按维度过滤洞察"""
        await memory_service.create_insight(
            user_id="user_001",
            summary="Career insight",
            source_events=[],
            dimension="career",
        )
        await memory_service.create_insight(
            user_id="user_001",
            summary="Emotion insight",
            source_events=[],
            dimension="emotion",
        )
        
        insights = await memory_service.get_insights(
            user_id="user_001",
            dimension="career",
        )
        
        assert len(insights) == 1
        assert insights[0].dimension == "career"
    
    @pytest.mark.asyncio
    async def test_get_insights_by_confidence(self, memory_service):
        """测试按置信度过滤洞察"""
        await memory_service.create_insight(
            user_id="user_001",
            summary="High confidence",
            source_events=[],
            confidence=0.9,
        )
        await memory_service.create_insight(
            user_id="user_001",
            summary="Low confidence",
            source_events=[],
            confidence=0.3,
        )
        
        insights = await memory_service.get_insights(
            user_id="user_001",
            min_confidence=0.5,
        )
        
        assert len(insights) == 1
        assert insights[0].confidence == 0.9


class TestProfileOperations:
    """画像操作测试"""
    
    @pytest.mark.asyncio
    async def test_update_profile_create(self, memory_service):
        """测试创建画像"""
        await memory_service.update_profile(
            user_id="user_001",
            traits={"career_focus": 0.8},
            preferences={"language": "zh-CN"},
        )
        
        profile = await memory_service.get_profile(user_id="user_001")
        
        assert profile is not None
        assert profile.traits["career_focus"] == 0.8
        assert profile.preferences["language"] == "zh-CN"
    
    @pytest.mark.asyncio
    async def test_update_profile_merge(self, memory_service):
        """测试更新画像 (合并)"""
        await memory_service.update_profile(
            user_id="user_001",
            traits={"trait_a": 0.5},
        )
        
        await memory_service.update_profile(
            user_id="user_001",
            traits={"trait_b": 0.7},
        )
        
        profile = await memory_service.get_profile(user_id="user_001")
        
        assert profile.traits["trait_a"] == 0.5
        assert profile.traits["trait_b"] == 0.7
    
    @pytest.mark.asyncio
    async def test_get_profile_not_found(self, memory_service):
        """测试获取不存在的画像"""
        profile = await memory_service.get_profile(user_id="nonexistent")
        
        assert profile is None


class TestMemoryServiceProperty:
    """属性测试"""
    
    @given(
        user_id=st.text(min_size=1, max_size=20, alphabet="abcdefghijklmnopqrstuvwxyz0123456789_"),
        event_type=st.sampled_from(["analysis", "playbook", "qa"]),
    )
    @settings(max_examples=20)
    @pytest.mark.asyncio
    async def test_event_round_trip(self, user_id, event_type):
        """属性测试: 事件往返一致性"""
        # 创建本地实例避免 fixture 问题
        service = MemoryService(encryption_helper=None)
        
        data = {"test_key": "test_value"}
        
        event_id = await service.record_event(
            user_id=user_id,
            event_type=event_type,
            data=data,
        )
        
        event = await service.get_event(event_id, user_id=user_id)
        
        assert event.user_id == user_id
        assert event.event_type == event_type
        assert event.data["test_key"] == "test_value"
