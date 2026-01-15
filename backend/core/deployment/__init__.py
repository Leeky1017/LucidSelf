"""
LucidSelf Deployment

零停机部署模块，包含：
- BlueGreenManager: 蓝绿部署管理
- HealthChecker: 健康检查
- GracefulShutdown: 优雅关闭
- DeploymentConfig: 部署配置

对照 .kiro/specs/testing-ops/design.md §7 零停机设计
对照 Requirements R-6-4-01 ~ R-6-4-08, R-6-7-01 ~ R-6-7-06
"""

from backend.core.deployment.blue_green import BlueGreenManager, DeploymentSlot
from backend.core.deployment.health import HealthChecker, HealthStatus
from backend.core.deployment.graceful import GracefulShutdown
from backend.core.deployment.config import (
    DeploymentConfig,
    ConfigLoader,
    ConfigValidator,
    Environment,
    DatabaseConfig,
    RedisConfig,
    LLMConfig,
    CacheConfig,
    ObservabilityConfig,
    get_config,
    set_config,
    reset_config,
)

__all__ = [
    # Blue-Green
    "BlueGreenManager",
    "DeploymentSlot",
    # Health
    "HealthChecker",
    "HealthStatus",
    # Graceful Shutdown
    "GracefulShutdown",
    # Config
    "DeploymentConfig",
    "ConfigLoader",
    "ConfigValidator",
    "Environment",
    "DatabaseConfig",
    "RedisConfig",
    "LLMConfig",
    "CacheConfig",
    "ObservabilityConfig",
    "get_config",
    "set_config",
    "reset_config",
]
