"""
Tests for Deployment Module

部署模块测试。
"""

import threading
import time
from unittest.mock import MagicMock

import pytest

from backend.core.deployment.blue_green import (
    BlueGreenManager,
    DeploymentSlot,
    VersionManager,
)
from backend.core.deployment.health import (
    HealthChecker,
    HealthStatus,
    HealthCheckResult,
    create_memory_check,
)
from backend.core.deployment.graceful import (
    GracefulShutdown,
    ShutdownPhase,
    RequestGuard,
)


class TestBlueGreenManager:
    """BlueGreenManager 测试"""
    
    def test_initial_state(self):
        """测试初始状态"""
        manager = BlueGreenManager()
        
        assert manager.active_slot == DeploymentSlot.BLUE
        assert manager.standby_slot == DeploymentSlot.GREEN
    
    def test_prepare_deployment(self):
        """测试准备部署"""
        manager = BlueGreenManager()
        
        slot = manager.prepare_deployment(
            version="v2.0.0",
            metadata={"commit": "abc123"},
        )
        
        assert slot == DeploymentSlot.GREEN
        
        state = manager.get_slot_state(slot)
        assert state.version == "v2.0.0"
        assert state.healthy is False
    
    def test_mark_healthy(self):
        """测试标记健康"""
        manager = BlueGreenManager()
        
        manager.prepare_deployment(version="v2.0.0")
        
        result = manager.mark_healthy(DeploymentSlot.GREEN)
        
        assert result is True
        assert manager.get_slot_state(DeploymentSlot.GREEN).healthy is True
    
    def test_switch_success(self):
        """测试成功切换"""
        manager = BlueGreenManager()
        
        manager.prepare_deployment(version="v2.0.0")
        manager.mark_healthy(DeploymentSlot.GREEN)
        
        result = manager.switch()
        
        assert result.success is True
        assert result.from_slot == DeploymentSlot.BLUE
        assert result.to_slot == DeploymentSlot.GREEN
        assert manager.active_slot == DeploymentSlot.GREEN
    
    def test_switch_unhealthy_fails(self):
        """测试不健康时切换失败"""
        manager = BlueGreenManager()
        
        manager.prepare_deployment(version="v2.0.0")
        # 不标记健康
        
        result = manager.switch()
        
        assert result.success is False
        assert "not healthy" in result.error
        assert manager.active_slot == DeploymentSlot.BLUE
    
    def test_rollback(self):
        """测试回滚"""
        manager = BlueGreenManager()
        
        # 先切换到 GREEN
        manager.prepare_deployment(version="v2.0.0")
        manager.mark_healthy(DeploymentSlot.GREEN)
        manager.switch()
        
        assert manager.active_slot == DeploymentSlot.GREEN
        
        # 回滚到 BLUE
        manager.mark_healthy(DeploymentSlot.BLUE)
        result = manager.rollback()
        
        assert result.success is True
        assert manager.active_slot == DeploymentSlot.BLUE
    
    def test_switch_history(self):
        """测试切换历史"""
        manager = BlueGreenManager()
        
        manager.prepare_deployment(version="v2.0.0")
        manager.mark_healthy(DeploymentSlot.GREEN)
        manager.switch()
        
        history = manager.get_switch_history()
        
        assert len(history) == 1
        assert history[0].success is True


class TestVersionManager:
    """VersionManager 测试"""
    
    def test_register_version(self):
        """测试注册版本"""
        vm = VersionManager(max_versions=3)
        
        vm.register_version("v1.0.0")
        vm.register_version("v1.1.0")
        
        versions = vm.list_versions()
        assert len(versions) == 2
    
    def test_max_versions(self):
        """测试最大版本数"""
        vm = VersionManager(max_versions=2)
        
        vm.register_version("v1.0.0")
        vm.register_version("v1.1.0")
        vm.register_version("v1.2.0")
        
        versions = vm.list_versions()
        assert len(versions) == 2
        assert versions[0]["version"] == "v1.1.0"
    
    def test_set_current(self):
        """测试设置当前版本"""
        vm = VersionManager()
        
        vm.register_version("v1.0.0")
        vm.register_version("v1.1.0")
        
        result = vm.set_current("v1.1.0")
        
        assert result is True
        assert vm.get_current() == "v1.1.0"
    
    def test_get_previous(self):
        """测试获取上一版本"""
        vm = VersionManager()
        
        vm.register_version("v1.0.0")
        vm.register_version("v1.1.0")
        vm.set_current("v1.1.0")
        
        assert vm.get_previous() == "v1.0.0"


class TestHealthChecker:
    """HealthChecker 测试"""
    
    def test_register_check(self):
        """测试注册检查"""
        checker = HealthChecker()
        
        def my_check():
            return HealthCheckResult(
                name="test",
                status=HealthStatus.HEALTHY,
                duration_ms=1.0,
            )
        
        checker.register_check("test", my_check)
        
        result = checker.run_check("test")
        
        assert result is not None
        assert result.status == HealthStatus.HEALTHY
    
    def test_run_all_checks(self):
        """测试运行所有检查"""
        checker = HealthChecker()
        
        checker.register_check("check1", lambda: HealthCheckResult(
            name="check1", status=HealthStatus.HEALTHY, duration_ms=1.0
        ))
        checker.register_check("check2", lambda: HealthCheckResult(
            name="check2", status=HealthStatus.DEGRADED, duration_ms=1.0
        ))
        
        overall = checker.run_all_checks()
        
        assert overall.healthy_count == 1
        assert overall.degraded_count == 1
        assert overall.status == HealthStatus.DEGRADED
    
    def test_unhealthy_threshold(self):
        """测试不健康阈值"""
        recovery_called = []
        
        def recovery():
            recovery_called.append(True)
        
        checker = HealthChecker(unhealthy_threshold=2, recovery_callback=recovery)
        
        checker.register_check("failing", lambda: HealthCheckResult(
            name="failing", status=HealthStatus.UNHEALTHY, duration_ms=1.0
        ))
        
        checker.run_check("failing")
        assert len(recovery_called) == 0
        
        checker.run_check("failing")
        assert len(recovery_called) == 1
    
    def test_unregister_check(self):
        """测试取消注册"""
        checker = HealthChecker()
        
        checker.register_check("test", lambda: HealthCheckResult(
            name="test", status=HealthStatus.HEALTHY, duration_ms=1.0
        ))
        
        result = checker.unregister_check("test")
        
        assert result is True
        assert checker.run_check("test") is None


class TestGracefulShutdown:
    """GracefulShutdown 测试"""
    
    def test_initial_state(self):
        """测试初始状态"""
        shutdown = GracefulShutdown(register_signals=False)
        
        assert shutdown.phase == ShutdownPhase.RUNNING
        assert shutdown.is_shutting_down is False
    
    def test_register_hook(self):
        """测试注册钩子"""
        shutdown = GracefulShutdown(register_signals=False)
        
        called = []
        shutdown.register_hook("test", lambda: called.append(True))
        
        result = shutdown.shutdown()
        
        assert "test" in result.hooks_executed
        assert len(called) == 1
    
    def test_hook_priority(self):
        """测试钩子优先级"""
        shutdown = GracefulShutdown(register_signals=False)
        
        order = []
        shutdown.register_hook("last", lambda: order.append("last"), priority=10)
        shutdown.register_hook("first", lambda: order.append("first"), priority=1)
        shutdown.register_hook("middle", lambda: order.append("middle"), priority=5)
        
        shutdown.shutdown()
        
        assert order == ["first", "middle", "last"]
    
    def test_request_guard(self):
        """测试请求守卫"""
        shutdown = GracefulShutdown(register_signals=False)
        
        with RequestGuard(shutdown) as accepted:
            assert accepted is True
            assert shutdown.active_requests == 1
        
        assert shutdown.active_requests == 0
    
    def test_request_rejected_during_shutdown(self):
        """测试关闭时拒绝请求"""
        shutdown = GracefulShutdown(register_signals=False)
        
        # 开始关闭
        def slow_shutdown():
            time.sleep(0.1)
        
        shutdown.register_hook("slow", slow_shutdown)
        
        # 在另一线程中开始关闭
        thread = threading.Thread(target=shutdown.shutdown)
        thread.start()
        
        time.sleep(0.05)  # 等待进入关闭状态
        
        # 尝试新请求
        with RequestGuard(shutdown) as accepted:
            assert accepted is False
        
        thread.join()
    
    def test_drain_requests(self):
        """测试请求排空"""
        shutdown = GracefulShutdown(
            drain_timeout_seconds=1.0,
            register_signals=False,
        )
        
        # 模拟活跃请求
        shutdown.request_start()
        
        # 在另一线程中结束请求
        def end_request():
            time.sleep(0.1)
            shutdown.request_end()
        
        thread = threading.Thread(target=end_request)
        thread.start()
        
        result = shutdown.shutdown()
        thread.join()
        
        assert result.success is True
        assert result.phase == ShutdownPhase.STOPPED


class TestIntegration:
    """集成测试"""
    
    def test_module_exports(self):
        """测试模块导出"""
        from backend.core.deployment import (
            BlueGreenManager,
            DeploymentSlot,
            HealthChecker,
            HealthStatus,
            GracefulShutdown,
        )
        
        assert BlueGreenManager is not None
        assert DeploymentSlot is not None
        assert HealthChecker is not None
        assert HealthStatus is not None
        assert GracefulShutdown is not None
    
    def test_blue_green_with_health_check(self):
        """测试蓝绿部署与健康检查集成"""
        checker = HealthChecker()
        
        def slot_health_check(slot):
            return True
        
        manager = BlueGreenManager(health_check_fn=slot_health_check)
        
        manager.prepare_deployment(version="v2.0.0")
        manager.mark_healthy(DeploymentSlot.GREEN)
        
        result = manager.switch()
        
        assert result.success is True
