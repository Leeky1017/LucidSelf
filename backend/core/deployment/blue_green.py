"""
Blue-Green Deployment Manager

蓝绿部署管理。

对照 design.md §7.1 蓝绿部署
对照 Requirements R-6-4-01, R-6-4-02, R-6-4-03
"""

from __future__ import annotations

import asyncio
import logging
import threading
import time
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)


class DeploymentSlot(str, Enum):
    """部署槽位"""
    BLUE = "blue"
    GREEN = "green"


@dataclass
class SlotState:
    """槽位状态"""
    slot: DeploymentSlot
    version: str
    active: bool = False
    healthy: bool = True
    started_at: Optional[datetime] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class SwitchResult:
    """切换结果"""
    success: bool
    from_slot: DeploymentSlot
    to_slot: DeploymentSlot
    duration_ms: float
    error: Optional[str] = None


class BlueGreenManager:
    """
    蓝绿部署管理器
    
    对照 R-6-4-01: 蓝绿切换
    对照 R-6-4-02: 版本回滚
    对照 R-6-4-03: 健康检查联动
    """
    
    def __init__(
        self,
        health_check_fn: Optional[Callable[[DeploymentSlot], bool]] = None,
        switch_timeout_seconds: float = 30.0,
    ):
        """
        初始化蓝绿部署管理器
        
        Args:
            health_check_fn: 健康检查函数
            switch_timeout_seconds: 切换超时秒数
        """
        self._health_check_fn = health_check_fn or self._default_health_check
        self._switch_timeout = switch_timeout_seconds
        
        self._slots: Dict[DeploymentSlot, SlotState] = {
            DeploymentSlot.BLUE: SlotState(slot=DeploymentSlot.BLUE, version="initial"),
            DeploymentSlot.GREEN: SlotState(slot=DeploymentSlot.GREEN, version="initial"),
        }
        
        self._active_slot = DeploymentSlot.BLUE
        self._slots[DeploymentSlot.BLUE].active = True
        self._slots[DeploymentSlot.BLUE].started_at = datetime.now()
        
        self._lock = threading.RLock()
        self._switch_history: List[SwitchResult] = []
    
    @property
    def active_slot(self) -> DeploymentSlot:
        """获取当前活跃槽位"""
        return self._active_slot
    
    @property
    def standby_slot(self) -> DeploymentSlot:
        """获取备用槽位"""
        return (
            DeploymentSlot.GREEN
            if self._active_slot == DeploymentSlot.BLUE
            else DeploymentSlot.BLUE
        )
    
    def get_slot_state(self, slot: DeploymentSlot) -> SlotState:
        """获取槽位状态"""
        return self._slots[slot]
    
    def prepare_deployment(
        self,
        version: str,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> DeploymentSlot:
        """
        准备部署到备用槽位
        
        Args:
            version: 新版本号
            metadata: 部署元数据
            
        Returns:
            准备好的槽位
        """
        with self._lock:
            standby = self.standby_slot
            state = self._slots[standby]
            
            state.version = version
            state.metadata = metadata or {}
            state.healthy = False  # 待验证
            state.started_at = datetime.now()
            
            logger.info(f"Prepared deployment: slot={standby}, version={version}")
            return standby
    
    def mark_healthy(self, slot: DeploymentSlot) -> bool:
        """
        标记槽位为健康
        
        Args:
            slot: 槽位
            
        Returns:
            True 如果成功
        """
        with self._lock:
            if slot not in self._slots:
                return False
            
            self._slots[slot].healthy = True
            logger.info(f"Slot marked healthy: {slot}")
            return True
    
    def switch(self) -> SwitchResult:
        """
        切换到备用槽位
        
        对照 R-6-4-01
        
        Returns:
            切换结果
        """
        start_time = time.perf_counter()
        
        with self._lock:
            from_slot = self._active_slot
            to_slot = self.standby_slot
            
            # 检查目标槽位是否健康
            if not self._slots[to_slot].healthy:
                error = f"Target slot {to_slot} is not healthy"
                logger.warning(error)
                return SwitchResult(
                    success=False,
                    from_slot=from_slot,
                    to_slot=to_slot,
                    duration_ms=(time.perf_counter() - start_time) * 1000,
                    error=error,
                )
            
            # 执行健康检查
            if not self._health_check_fn(to_slot):
                error = f"Health check failed for slot {to_slot}"
                logger.warning(error)
                return SwitchResult(
                    success=False,
                    from_slot=from_slot,
                    to_slot=to_slot,
                    duration_ms=(time.perf_counter() - start_time) * 1000,
                    error=error,
                )
            
            # 执行切换
            self._slots[from_slot].active = False
            self._slots[to_slot].active = True
            self._active_slot = to_slot
            
            duration_ms = (time.perf_counter() - start_time) * 1000
            
            result = SwitchResult(
                success=True,
                from_slot=from_slot,
                to_slot=to_slot,
                duration_ms=duration_ms,
            )
            
            self._switch_history.append(result)
            logger.info(f"Switched: {from_slot} -> {to_slot} ({duration_ms:.2f}ms)")
            
            return result
    
    def rollback(self) -> SwitchResult:
        """
        回滚到上一个槽位
        
        对照 R-6-4-02
        """
        return self.switch()  # 蓝绿切换本身就是回滚
    
    def get_switch_history(self) -> List[SwitchResult]:
        """获取切换历史"""
        return self._switch_history.copy()
    
    def _default_health_check(self, slot: DeploymentSlot) -> bool:
        """默认健康检查（始终通过）"""
        return True


class VersionManager:
    """
    版本管理器
    
    管理多版本共存。
    """
    
    def __init__(self, max_versions: int = 3):
        self._max_versions = max_versions
        self._versions: List[Dict[str, Any]] = []
        self._current_version: Optional[str] = None
    
    def register_version(
        self,
        version: str,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        """注册新版本"""
        version_info = {
            "version": version,
            "registered_at": datetime.now().isoformat(),
            "metadata": metadata or {},
        }
        
        self._versions.append(version_info)
        
        # 保留最近 N 个版本
        while len(self._versions) > self._max_versions:
            self._versions.pop(0)
    
    def set_current(self, version: str) -> bool:
        """设置当前版本"""
        for v in self._versions:
            if v["version"] == version:
                self._current_version = version
                return True
        return False
    
    def get_current(self) -> Optional[str]:
        """获取当前版本"""
        return self._current_version
    
    def get_previous(self) -> Optional[str]:
        """获取上一个版本"""
        if len(self._versions) < 2:
            return None
        
        for i, v in enumerate(self._versions):
            if v["version"] == self._current_version and i > 0:
                return self._versions[i - 1]["version"]
        
        return None
    
    def list_versions(self) -> List[Dict[str, Any]]:
        """列出所有版本"""
        return self._versions.copy()
