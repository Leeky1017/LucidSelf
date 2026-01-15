"""
Tests for Memory Models

对照文档: docs/数据契约_Schema定义规范_v1.md §9.6
"""

import pytest
from datetime import datetime
from pydantic import ValidationError

from backend.core.contracts import (
    Event,
    Insight,
    PrivacyLevel,
    SENSITIVE_FIELDS,
    UserProfile,
)


# =============================================================================
# PrivacyLevel 测试
# =============================================================================


class TestPrivacyLevel:
    """PrivacyLevel 枚举测试"""

    def test_all_levels(self):
        """测试所有隐私级别"""
        assert PrivacyLevel.PUBLIC.value == "public"
        assert PrivacyLevel.PRIVATE.value == "private"
        assert PrivacyLevel.SENSITIVE.value == "sensitive"

    def test_enum_from_string(self):
        """测试从字符串创建枚举"""
        assert PrivacyLevel("public") == PrivacyLevel.PUBLIC
        assert PrivacyLevel("private") == PrivacyLevel.PRIVATE
        assert PrivacyLevel("sensitive") == PrivacyLevel.SENSITIVE


# =============================================================================
# SENSITIVE_FIELDS 测试
# =============================================================================


class TestSensitiveFields:
    """敏感字段常量测试"""

    def test_user_profile_fields(self):
        """测试 UserProfile 敏感字段"""
        assert "UserProfile" in SENSITIVE_FIELDS
        profile_fields = SENSITIVE_FIELDS["UserProfile"]
        assert "real_name" in profile_fields
        assert "phone_number" in profile_fields
        assert "email" in profile_fields

    def test_event_payload_fields(self):
        """测试 Event.payload 敏感字段"""
        assert "Event.payload" in SENSITIVE_FIELDS
        payload_fields = SENSITIVE_FIELDS["Event.payload"]
        assert "location_detail" in payload_fields
        assert "medical_history" in payload_fields


# =============================================================================
# Event 测试
# =============================================================================


class TestEvent:
    """Event 模型测试"""

    def test_valid_event(self):
        """测试有效的事件"""
        event = Event(
            event_id="evt_abc123456789",
            user_id="user_12345",
            timestamp=datetime.now(),
            kind="dream_record",
            payload={"dream_text": "梦到飞在天空"},
            source_channel="app",
        )
        assert event.event_id == "evt_abc123456789"
        assert event.kind == "dream_record"
        assert event.privacy == PrivacyLevel.PRIVATE  # 默认值

    def test_invalid_event_id_pattern(self):
        """测试无效的 event_id 格式"""
        with pytest.raises(ValidationError):
            Event(
                event_id="invalid_id",  # 应该是 evt_xxxxxxxxxxxx 格式
                user_id="user_12345",
                timestamp=datetime.now(),
                kind="dream_record",
                payload={},
                source_channel="app",
            )

    def test_valid_event_id_formats(self):
        """测试有效的 event_id 格式"""
        valid_ids = ["evt_abc123456789", "evt_000000000000", "evt_abcdefghij12"]
        for eid in valid_ids:
            event = Event(
                event_id=eid,
                user_id="user_12345",
                timestamp=datetime.now(),
                kind="dream_record",
                payload={},
                source_channel="app",
            )
            assert event.event_id == eid

    def test_all_event_kinds(self):
        """测试所有事件类型"""
        kinds = [
            "dream_record",
            "reading_request",
            "feedback",
            "profile_edit",
            "preference_change",
            "system_action",
        ]
        for kind in kinds:
            event = Event(
                event_id="evt_abc123456789",
                user_id="user_12345",
                timestamp=datetime.now(),
                kind=kind,
                payload={},
                source_channel="app",
            )
            assert event.kind == kind

    def test_all_source_channels(self):
        """测试所有来源渠道"""
        channels = ["app", "web", "miniapp", "partner_api"]
        for channel in channels:
            event = Event(
                event_id="evt_abc123456789",
                user_id="user_12345",
                timestamp=datetime.now(),
                kind="dream_record",
                payload={},
                source_channel=channel,
            )
            assert event.source_channel == channel

    def test_all_privacy_levels(self):
        """测试所有隐私级别"""
        for level in PrivacyLevel:
            event = Event(
                event_id="evt_abc123456789",
                user_id="user_12345",
                timestamp=datetime.now(),
                kind="dream_record",
                payload={},
                source_channel="app",
                privacy=level,
            )
            assert event.privacy == level

    def test_sensitive_flag(self):
        """测试敏感信息标记"""
        # 默认 False
        event = Event(
            event_id="evt_abc123456789",
            user_id="user_12345",
            timestamp=datetime.now(),
            kind="dream_record",
            payload={},
            source_channel="app",
        )
        assert event.sensitive is False

        # 设置为 True
        event = Event(
            event_id="evt_abc123456789",
            user_id="user_12345",
            timestamp=datetime.now(),
            kind="dream_record",
            payload={"medical_info": "..."},
            source_channel="app",
            sensitive=True,
        )
        assert event.sensitive is True

    def test_complex_payload(self):
        """测试复杂的 payload"""
        event = Event(
            event_id="evt_abc123456789",
            user_id="user_12345",
            timestamp=datetime.now(),
            kind="reading_request",
            payload={
                "request_type": "bazi",
                "birth_date": "1990-01-01",
                "birth_time": "12:00",
                "questions": ["事业", "婚姻"],
            },
            source_channel="app",
        )
        assert event.payload["request_type"] == "bazi"
        assert len(event.payload["questions"]) == 2


# =============================================================================
# Insight 测试
# =============================================================================


class TestInsight:
    """Insight 模型测试"""

    def test_valid_insight(self):
        """测试有效的洞察"""
        insight = Insight(
            insight_id="ins_xyz987654321",
            user_id="user_12345",
            created_at=datetime.now(),
            factors=["day_master_jia", "season_spring"],
            rules=["dts_jia_spring_001"],
            themes=["事业突破", "领导力提升"],
            summary_zh="事业发展进入突破期",
            strength=0.85,
            time_scope="near_future",
        )
        assert insight.insight_id == "ins_xyz987654321"
        assert len(insight.factors) == 2

    def test_invalid_insight_id_pattern(self):
        """测试无效的 insight_id 格式"""
        with pytest.raises(ValidationError):
            Insight(
                insight_id="invalid_id",  # 应该是 ins_xxxxxxxxxxxx 格式
                user_id="user_12345",
                created_at=datetime.now(),
                summary_zh="测试",
                strength=0.8,
                time_scope="present",
            )

    def test_valid_insight_id_formats(self):
        """测试有效的 insight_id 格式"""
        valid_ids = ["ins_abc123456789", "ins_000000000000", "ins_abcdefghij12"]
        for iid in valid_ids:
            insight = Insight(
                insight_id=iid,
                user_id="user_12345",
                created_at=datetime.now(),
                summary_zh="测试",
                strength=0.8,
                time_scope="present",
            )
            assert insight.insight_id == iid

    def test_summary_max_length(self):
        """测试 summary_zh 最大长度"""
        # 100 字符以内有效
        insight = Insight(
            insight_id="ins_abc123456789",
            user_id="user_12345",
            created_at=datetime.now(),
            summary_zh="x" * 100,
            strength=0.8,
            time_scope="present",
        )
        assert len(insight.summary_zh) == 100

        # 超过 100 字符失败
        with pytest.raises(ValidationError):
            Insight(
                insight_id="ins_abc123456789",
                user_id="user_12345",
                created_at=datetime.now(),
                summary_zh="x" * 101,
                strength=0.8,
                time_scope="present",
            )

    def test_strength_bounds(self):
        """测试 strength 边界"""
        # 有效边界
        insight = Insight(
            insight_id="ins_abc123456789",
            user_id="user_12345",
            created_at=datetime.now(),
            summary_zh="测试",
            strength=0.0,
            time_scope="present",
        )
        assert insight.strength == 0.0

        insight = Insight(
            insight_id="ins_abc123456789",
            user_id="user_12345",
            created_at=datetime.now(),
            summary_zh="测试",
            strength=1.0,
            time_scope="present",
        )
        assert insight.strength == 1.0

        # 超出边界
        with pytest.raises(ValidationError):
            Insight(
                insight_id="ins_abc123456789",
                user_id="user_12345",
                created_at=datetime.now(),
                summary_zh="测试",
                strength=1.5,
                time_scope="present",
            )

    def test_all_time_scopes(self):
        """测试所有时间范围"""
        scopes = ["past", "present", "near_future", "long_term"]
        for scope in scopes:
            insight = Insight(
                insight_id="ins_abc123456789",
                user_id="user_12345",
                created_at=datetime.now(),
                summary_zh="测试",
                strength=0.8,
                time_scope=scope,
            )
            assert insight.time_scope == scope

    def test_empty_lists_by_default(self):
        """测试列表字段默认为空"""
        insight = Insight(
            insight_id="ins_abc123456789",
            user_id="user_12345",
            created_at=datetime.now(),
            summary_zh="测试",
            strength=0.8,
            time_scope="present",
        )
        assert insight.factors == []
        assert insight.rules == []
        assert insight.themes == []


# =============================================================================
# UserProfile 测试
# =============================================================================


class TestUserProfile:
    """UserProfile 模型测试"""

    def test_valid_profile(self):
        """测试有效的用户画像"""
        profile = UserProfile(
            user_id="user_12345",
            traits={"risk_tolerance": 0.7, "creativity": 0.9},
            preferences={"language": "zh", "tone": "friendly"},
            long_term_themes=["事业发展", "家庭平衡"],
            last_updated=datetime.now(),
            update_count=5,
        )
        assert profile.user_id == "user_12345"
        assert profile.traits["risk_tolerance"] == 0.7
        assert profile.privacy == PrivacyLevel.PRIVATE  # 默认值

    def test_empty_profile(self):
        """测试最小化的用户画像"""
        profile = UserProfile(
            user_id="user_12345",
            last_updated=datetime.now(),
        )
        assert profile.traits == {}
        assert profile.preferences == {}
        assert profile.long_term_themes == []
        assert profile.update_count == 0

    def test_traits_dict(self):
        """测试 traits 字典"""
        profile = UserProfile(
            user_id="user_12345",
            traits={
                "risk_tolerance": 0.7,
                "creativity": 0.9,
                "analytical": 0.8,
                "emotional": 0.6,
            },
            last_updated=datetime.now(),
        )
        assert len(profile.traits) == 4
        assert all(0 <= v <= 1 for v in profile.traits.values())

    def test_preferences_dict(self):
        """测试 preferences 字典"""
        profile = UserProfile(
            user_id="user_12345",
            preferences={
                "language": "zh",
                "tone": "friendly",
                "preferred_engines": ["bazi", "tarot"],
                "notification_enabled": True,
            },
            last_updated=datetime.now(),
        )
        assert profile.preferences["language"] == "zh"
        assert isinstance(profile.preferences["preferred_engines"], list)

    def test_long_term_themes(self):
        """测试长期主题"""
        profile = UserProfile(
            user_id="user_12345",
            long_term_themes=["事业发展", "家庭平衡", "健康管理", "财富积累"],
            last_updated=datetime.now(),
        )
        assert len(profile.long_term_themes) == 4
        assert "事业发展" in profile.long_term_themes

    def test_update_count_increment(self):
        """测试更新次数"""
        profile = UserProfile(
            user_id="user_12345",
            last_updated=datetime.now(),
            update_count=0,
        )
        assert profile.update_count == 0

        # 模拟更新
        profile = UserProfile(
            user_id="user_12345",
            last_updated=datetime.now(),
            update_count=10,
        )
        assert profile.update_count == 10

    def test_all_privacy_levels(self):
        """测试所有隐私级别"""
        for level in PrivacyLevel:
            profile = UserProfile(
                user_id="user_12345",
                last_updated=datetime.now(),
                privacy=level,
            )
            assert profile.privacy == level
