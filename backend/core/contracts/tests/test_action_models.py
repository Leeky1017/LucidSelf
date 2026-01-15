"""
Action Models Tests

Phase 5.5-1 Action Contracts 单元测试

对照 tasks.md Task 1.8:
- Test ActionBase 不依赖 MemoryBase (V-01)
- Test ID 格式验证
- Test 字段长度限制
- Test 枚举值
"""

import re
from datetime import datetime

import pytest
from pydantic import ValidationError

from backend.core.contracts.action_models import (
    ACTION_PROJECT_ID_PATTERN,
    ACTION_ITEM_ID_PATTERN,
    ActionSourceKind,
    ActionTimeScope,
    ActionContext,
    ActionStatus,
    EffortEstimate,
    InsightCompileStatus,
    ActionBase,
    ActionSourceRef,
    ActionProject,
    ActionItem,
    InsightCompileRecord,
    AvoidanceInsight,
)


class TestEnums:
    """枚举测试"""
    
    def test_action_source_kind_values(self):
        """测试 ActionSourceKind 枚举值"""
        assert ActionSourceKind.PLAYBOOK.value == "playbook"
        assert ActionSourceKind.DREAM.value == "dream"
        assert ActionSourceKind.ASTRO.value == "astro"
        assert ActionSourceKind.HEALTH.value == "health"
        assert ActionSourceKind.MANUAL.value == "manual"
        assert ActionSourceKind.INSIGHT.value == "insight"
        assert len(ActionSourceKind) == 6
    
    def test_action_time_scope_values(self):
        """测试 ActionTimeScope 枚举值"""
        assert ActionTimeScope.TODAY.value == "today"
        assert ActionTimeScope.THIS_WEEK.value == "this_week"
        assert ActionTimeScope.THIS_MONTH.value == "this_month"
        assert len(ActionTimeScope) == 3
    
    def test_action_context_values(self):
        """测试 ActionContext 枚举值"""
        assert ActionContext.DESK.value == "desk"
        assert ActionContext.PHONE.value == "phone"
        assert ActionContext.OUTDOOR.value == "outdoor"
        assert ActionContext.TALK.value == "talk"
        assert ActionContext.REST.value == "rest"
        assert len(ActionContext) == 5
    
    def test_action_status_values(self):
        """测试 ActionStatus 枚举值"""
        assert ActionStatus.TODO.value == "todo"
        assert ActionStatus.DOING.value == "doing"
        assert ActionStatus.DONE.value == "done"
        assert ActionStatus.SKIPPED.value == "skipped"
        assert ActionStatus.EXPIRED.value == "expired"
        assert len(ActionStatus) == 5
    
    def test_effort_estimate_values(self):
        """测试 EffortEstimate 枚举值"""
        assert EffortEstimate.QUICK.value == "15min"
        assert EffortEstimate.SHORT.value == "30min"
        assert EffortEstimate.MEDIUM.value == "60min"
        assert EffortEstimate.LONG.value == "90min+"
        assert len(EffortEstimate) == 4
    
    def test_insight_compile_status_values(self):
        """测试 InsightCompileStatus 枚举值"""
        assert InsightCompileStatus.NEW.value == "new"
        assert InsightCompileStatus.COMPILED.value == "compiled"
        assert InsightCompileStatus.TEMPLATE_CREATED.value == "template"
        assert InsightCompileStatus.ARCHIVED.value == "archived"
        assert len(InsightCompileStatus) == 4


class TestActionBaseDecoupling:
    """
    ActionBase 与 MemoryBase 解耦测试 (V-01)
    
    验证: Action 系列不依赖 MemoryBase
    """
    
    def test_action_base_no_memory_base_import(self):
        """测试 ActionBase 不导入 MemoryBase"""
        import backend.core.contracts.action_models as action_module
        import backend.core.contracts.memory_models as memory_module
        
        # ActionBase 应该独立于 MemoryBase
        assert not issubclass(ActionBase, memory_module.MemoryBase)
    
    def test_action_base_fields(self):
        """测试 ActionBase 字段"""
        base = ActionBase(user_id="user_123")
        
        assert base.user_id == "user_123"
        assert isinstance(base.created_at, datetime)
        assert isinstance(base.updated_at, datetime)
        
        # 验证没有 id 字段（子类使用专用 ID）
        assert "id" not in base.model_fields
    
    def test_action_project_not_memory_base(self):
        """测试 ActionProject 不继承 MemoryBase"""
        from backend.core.contracts.memory_models import MemoryBase
        
        assert not issubclass(ActionProject, MemoryBase)
    
    def test_action_item_not_memory_base(self):
        """测试 ActionItem 不继承 MemoryBase"""
        from backend.core.contracts.memory_models import MemoryBase
        
        assert not issubclass(ActionItem, MemoryBase)


class TestIDPatterns:
    """ID 格式验证测试"""
    
    def test_project_id_pattern_valid(self):
        """测试有效的 project_id 格式"""
        valid_ids = [
            "proj_abc123456789",
            "proj_000000000000",
            "proj_zzzzzzzzzzzz",
            "proj_a1b2c3d4e5f6",
        ]
        for pid in valid_ids:
            assert re.match(ACTION_PROJECT_ID_PATTERN, pid), f"Should match: {pid}"
    
    def test_project_id_pattern_invalid(self):
        """测试无效的 project_id 格式"""
        invalid_ids = [
            "proj_",
            "proj_abc",
            "proj_ABC123456789",  # 大写
            "item_abc123456789",  # 错误前缀
            "abc123456789",       # 无前缀
        ]
        for pid in invalid_ids:
            assert not re.match(ACTION_PROJECT_ID_PATTERN, pid), f"Should not match: {pid}"
    
    def test_item_id_pattern_valid(self):
        """测试有效的 item_id 格式"""
        valid_ids = [
            "item_abc123456789",
            "item_000000000000",
            "item_zzzzzzzzzzzz",
        ]
        for iid in valid_ids:
            assert re.match(ACTION_ITEM_ID_PATTERN, iid), f"Should match: {iid}"
    
    def test_item_id_pattern_invalid(self):
        """测试无效的 item_id 格式"""
        invalid_ids = [
            "item_",
            "item_abc",
            "proj_abc123456789",  # 错误前缀
        ]
        for iid in invalid_ids:
            assert not re.match(ACTION_ITEM_ID_PATTERN, iid), f"Should not match: {iid}"


class TestActionSourceRef:
    """ActionSourceRef 测试"""
    
    def test_create_source_ref(self):
        """测试创建来源引用"""
        ref = ActionSourceRef(
            kind=ActionSourceKind.PLAYBOOK,
            source_id="pb_123",
            source_summary="每周运势建议加强沟通",
        )
        
        assert ref.kind == ActionSourceKind.PLAYBOOK
        assert ref.source_id == "pb_123"
        assert ref.source_summary == "每周运势建议加强沟通"
        assert ref.factor_ids == []
        assert ref.rule_ids == []
    
    def test_source_ref_with_traceability(self):
        """测试带追溯信息的来源引用"""
        ref = ActionSourceRef(
            kind=ActionSourceKind.INSIGHT,
            source_id="ins_xyz",
            source_summary="命盘显示沟通运强",
            factor_ids=["day_master_jia", "season_spring"],
            rule_ids=["dts_jia_spring_001"],
        )
        
        assert len(ref.factor_ids) == 2
        assert len(ref.rule_ids) == 1
    
    def test_source_summary_max_length(self):
        """测试 source_summary 长度限制"""
        # 100 字符应该可以
        ref = ActionSourceRef(
            kind=ActionSourceKind.MANUAL,
            source_id="manual_1",
            source_summary="a" * 100,
        )
        assert len(ref.source_summary) == 100
        
        # 超过 100 字符应该失败
        with pytest.raises(ValidationError):
            ActionSourceRef(
                kind=ActionSourceKind.MANUAL,
                source_id="manual_1",
                source_summary="a" * 101,
            )


class TestActionProject:
    """ActionProject 测试"""
    
    @pytest.fixture
    def sample_source_ref(self):
        return ActionSourceRef(
            kind=ActionSourceKind.PLAYBOOK,
            source_id="pb_123",
            source_summary="周报建议",
        )
    
    def test_create_project(self, sample_source_ref):
        """测试创建项目"""
        project = ActionProject(
            project_id="proj_abc123456789",
            user_id="user_001",
            title="本周沟通突破",
            time_scope=ActionTimeScope.THIS_WEEK,
            sources=[sample_source_ref],
        )
        
        assert project.project_id == "proj_abc123456789"
        assert project.user_id == "user_001"
        assert project.title == "本周沟通突破"
        assert project.time_scope == ActionTimeScope.THIS_WEEK
        assert len(project.sources) == 1
        assert project.status == "active"
        assert project.llm_generated is True
        assert project.llm_call_id is None
    
    def test_project_title_max_length(self):
        """测试项目标题长度限制"""
        # 50 字符应该可以
        project = ActionProject(
            project_id="proj_abc123456789",
            user_id="user_001",
            title="a" * 50,
            time_scope=ActionTimeScope.TODAY,
        )
        assert len(project.title) == 50
        
        # 超过 50 字符应该失败
        with pytest.raises(ValidationError):
            ActionProject(
                project_id="proj_abc123456789",
                user_id="user_001",
                title="a" * 51,
                time_scope=ActionTimeScope.TODAY,
            )
    
    def test_project_id_validation(self):
        """测试 project_id 格式验证"""
        with pytest.raises(ValidationError):
            ActionProject(
                project_id="invalid_id",
                user_id="user_001",
                title="Test",
                time_scope=ActionTimeScope.TODAY,
            )


class TestActionItem:
    """ActionItem 测试"""
    
    @pytest.fixture
    def sample_source_ref(self):
        return ActionSourceRef(
            kind=ActionSourceKind.PLAYBOOK,
            source_id="pb_123",
            source_summary="周报建议",
        )
    
    def test_create_item(self, sample_source_ref):
        """测试创建条目"""
        item = ActionItem(
            item_id="item_abc123456789",
            project_id="proj_abc123456789",
            user_id="user_001",
            title="联系张经理讨论合作",
            reason="命盘显示本周沟通运强",
            effort_estimate=EffortEstimate.SHORT,
            context=ActionContext.TALK,
            source=sample_source_ref,
        )
        
        assert item.item_id == "item_abc123456789"
        assert item.project_id == "proj_abc123456789"
        assert item.title == "联系张经理讨论合作"
        assert item.reason == "命盘显示本周沟通运强"
        assert item.effort_estimate == EffortEstimate.SHORT
        assert item.context == ActionContext.TALK
        assert item.status == ActionStatus.TODO
        assert item.priority == 5
        assert item.feedback_status is None
    
    def test_item_title_max_length(self, sample_source_ref):
        """测试条目标题长度限制"""
        # 60 字符应该可以
        item = ActionItem(
            item_id="item_abc123456789",
            project_id="proj_abc123456789",
            user_id="user_001",
            title="a" * 60,
            reason="test",
            effort_estimate=EffortEstimate.QUICK,
            context=ActionContext.PHONE,
            source=sample_source_ref,
        )
        assert len(item.title) == 60
        
        # 超过 60 字符应该失败
        with pytest.raises(ValidationError):
            ActionItem(
                item_id="item_abc123456789",
                project_id="proj_abc123456789",
                user_id="user_001",
                title="a" * 61,
                reason="test",
                effort_estimate=EffortEstimate.QUICK,
                context=ActionContext.PHONE,
                source=sample_source_ref,
            )
    
    def test_item_reason_max_length(self, sample_source_ref):
        """测试 reason 长度限制"""
        # 100 字符应该可以
        item = ActionItem(
            item_id="item_abc123456789",
            project_id="proj_abc123456789",
            user_id="user_001",
            title="Test",
            reason="a" * 100,
            effort_estimate=EffortEstimate.QUICK,
            context=ActionContext.PHONE,
            source=sample_source_ref,
        )
        assert len(item.reason) == 100
        
        # 超过 100 字符应该失败
        with pytest.raises(ValidationError):
            ActionItem(
                item_id="item_abc123456789",
                project_id="proj_abc123456789",
                user_id="user_001",
                title="Test",
                reason="a" * 101,
                effort_estimate=EffortEstimate.QUICK,
                context=ActionContext.PHONE,
                source=sample_source_ref,
            )
    
    def test_item_priority_range(self, sample_source_ref):
        """测试优先级范围限制"""
        # 1 和 10 应该可以
        for priority in [1, 5, 10]:
            item = ActionItem(
                item_id="item_abc123456789",
                project_id="proj_abc123456789",
                user_id="user_001",
                title="Test",
                reason="test",
                effort_estimate=EffortEstimate.QUICK,
                context=ActionContext.PHONE,
                source=sample_source_ref,
                priority=priority,
            )
            assert item.priority == priority
        
        # 0 和 11 应该失败
        for priority in [0, 11]:
            with pytest.raises(ValidationError):
                ActionItem(
                    item_id="item_abc123456789",
                    project_id="proj_abc123456789",
                    user_id="user_001",
                    title="Test",
                    reason="test",
                    effort_estimate=EffortEstimate.QUICK,
                    context=ActionContext.PHONE,
                    source=sample_source_ref,
                    priority=priority,
                )
    
    def test_item_inline_feedback(self, sample_source_ref):
        """测试内联反馈字段"""
        item = ActionItem(
            item_id="item_abc123456789",
            project_id="proj_abc123456789",
            user_id="user_001",
            title="Test",
            reason="test",
            effort_estimate=EffortEstimate.QUICK,
            context=ActionContext.PHONE,
            source=sample_source_ref,
            feedback_status="done",
            feedback_note="完成得很顺利",
            feedback_at=datetime.now(),
            actual_effort_minutes=25,
        )
        
        assert item.feedback_status == "done"
        assert item.feedback_note == "完成得很顺利"
        assert item.feedback_at is not None
        assert item.actual_effort_minutes == 25


class TestInsightCompileRecord:
    """InsightCompileRecord 测试"""
    
    def test_create_record(self):
        """测试创建编译记录"""
        record = InsightCompileRecord(
            insight_id="ins_xyz987654321",
        )
        
        assert record.insight_id == "ins_xyz987654321"
        assert record.status == InsightCompileStatus.NEW
        assert record.compiled_at is None
        assert record.compile_session_id is None
    
    def test_compiled_record(self):
        """测试已编译的记录"""
        now = datetime.now()
        record = InsightCompileRecord(
            insight_id="ins_xyz987654321",
            status=InsightCompileStatus.COMPILED,
            compiled_at=now,
            compile_session_id="sess_abc123",
        )
        
        assert record.status == InsightCompileStatus.COMPILED
        assert record.compiled_at == now
        assert record.compile_session_id == "sess_abc123"


class TestAvoidanceInsight:
    """AvoidanceInsight 测试"""
    
    def test_create_avoidance_insight(self):
        """测试创建回避洞察"""
        now = datetime.now()
        insight = AvoidanceInsight(
            insight_id="ins_avoid123456",
            user_id="user_001",
            pattern="desk_avoidance",
            confidence=0.85,
            affected_contexts=["desk"],
            sample_period_weeks=3,
            sample_count=12,
            completion_rate=0.25,
            detected_at=now,
        )
        
        assert insight.insight_id == "ins_avoid123456"
        assert insight.insight_type == "avoidance_pattern"
        assert insight.pattern == "desk_avoidance"
        assert insight.confidence == 0.85
        assert insight.affected_contexts == ["desk"]
        assert insight.playbook_consumable is True
    
    def test_confidence_range(self):
        """测试置信度范围"""
        now = datetime.now()
        
        # 0.0 和 1.0 应该可以
        for conf in [0.0, 0.5, 1.0]:
            insight = AvoidanceInsight(
                insight_id="ins_test",
                user_id="user_001",
                pattern="test",
                confidence=conf,
                sample_period_weeks=3,
                sample_count=5,
                completion_rate=0.3,
                detected_at=now,
            )
            assert insight.confidence == conf
        
        # 超出范围应该失败
        for conf in [-0.1, 1.1]:
            with pytest.raises(ValidationError):
                AvoidanceInsight(
                    insight_id="ins_test",
                    user_id="user_001",
                    pattern="test",
                    confidence=conf,
                    sample_period_weeks=3,
                    sample_count=5,
                    completion_rate=0.3,
                    detected_at=now,
                )


class TestModelSerialization:
    """模型序列化测试"""
    
    def test_action_project_json_roundtrip(self):
        """测试 ActionProject JSON 往返"""
        project = ActionProject(
            project_id="proj_abc123456789",
            user_id="user_001",
            title="测试项目",
            time_scope=ActionTimeScope.THIS_WEEK,
        )
        
        json_str = project.model_dump_json()
        restored = ActionProject.model_validate_json(json_str)
        
        assert restored.project_id == project.project_id
        assert restored.title == project.title
    
    def test_action_item_json_roundtrip(self):
        """测试 ActionItem JSON 往返"""
        item = ActionItem(
            item_id="item_abc123456789",
            project_id="proj_abc123456789",
            user_id="user_001",
            title="测试条目",
            reason="测试原因",
            effort_estimate=EffortEstimate.SHORT,
            context=ActionContext.DESK,
            source=ActionSourceRef(
                kind=ActionSourceKind.MANUAL,
                source_id="manual_1",
                source_summary="手动添加",
            ),
        )
        
        json_str = item.model_dump_json()
        restored = ActionItem.model_validate_json(json_str)
        
        assert restored.item_id == item.item_id
        assert restored.title == item.title
        assert restored.source.kind == item.source.kind
