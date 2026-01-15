"""
Deployment Configuration

部署配置管理。

对照 design.md §7.4 配置管理
对照 Requirements R-6-7-01 ~ R-6-7-06
"""

from __future__ import annotations

import json
import logging
import os
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

logger = logging.getLogger(__name__)


class Environment(str, Enum):
    """部署环境"""
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    TEST = "test"


@dataclass
class DatabaseConfig:
    """数据库配置"""
    host: str = "localhost"
    port: int = 5432
    database: str = "lucidself"
    username: str = "postgres"
    password: str = ""
    pool_size: int = 10
    ssl_mode: str = "prefer"
    
    @property
    def connection_string(self) -> str:
        """获取连接字符串"""
        return (
            f"postgresql://{self.username}:{self.password}@"
            f"{self.host}:{self.port}/{self.database}?sslmode={self.ssl_mode}"
        )


@dataclass
class RedisConfig:
    """Redis 配置"""
    host: str = "localhost"
    port: int = 6379
    db: int = 0
    password: Optional[str] = None
    ssl: bool = False
    
    @property
    def connection_string(self) -> str:
        """获取连接字符串"""
        scheme = "rediss" if self.ssl else "redis"
        auth = f":{self.password}@" if self.password else ""
        return f"{scheme}://{auth}{self.host}:{self.port}/{self.db}"


@dataclass
class LLMConfig:
    """LLM 配置"""
    provider: str = "openai"
    model: str = "gpt-4o-mini"
    api_key: str = ""
    base_url: Optional[str] = None
    max_tokens: int = 4096
    temperature: float = 0.7
    timeout_seconds: float = 60.0
    retry_count: int = 3


@dataclass
class CacheConfig:
    """缓存配置"""
    semantic_cache_size: int = 10000
    semantic_cache_ttl: int = 3600
    rule_cache_size: int = 5000
    rule_cache_ttl: int = 1800
    enable_redis: bool = True


@dataclass
class ObservabilityConfig:
    """可观测性配置"""
    enable_metrics: bool = True
    enable_tracing: bool = True
    enable_structured_logging: bool = True
    log_level: str = "INFO"
    metrics_port: int = 9090
    tracing_endpoint: Optional[str] = None


@dataclass
class DeploymentConfig:
    """
    部署配置
    
    对照 R-6-7-01: 环境配置分离
    对照 R-6-7-02: 密钥管理
    """
    
    environment: Environment = Environment.DEVELOPMENT
    debug: bool = False
    
    # 服务配置
    host: str = "0.0.0.0"
    port: int = 8000
    workers: int = 4
    
    # 子配置
    database: DatabaseConfig = field(default_factory=DatabaseConfig)
    redis: RedisConfig = field(default_factory=RedisConfig)
    llm: LLMConfig = field(default_factory=LLMConfig)
    cache: CacheConfig = field(default_factory=CacheConfig)
    observability: ObservabilityConfig = field(default_factory=ObservabilityConfig)
    
    # 元数据
    version: str = "0.0.0"
    build_id: Optional[str] = None


class ConfigLoader:
    """
    配置加载器
    
    对照 R-6-7-03: 配置文件加载
    对照 R-6-7-04: 环境变量覆盖
    """
    
    ENV_PREFIX = "LS_"
    
    def __init__(self, config_dir: Optional[Path] = None):
        """
        初始化配置加载器
        
        Args:
            config_dir: 配置文件目录
        """
        self._config_dir = config_dir or Path("config")
    
    def load(self, environment: Optional[str] = None) -> DeploymentConfig:
        """
        加载配置
        
        优先级: 环境变量 > 环境配置文件 > 默认配置
        
        Args:
            environment: 环境名称 (不提供则从 LS_ENVIRONMENT 获取)
        """
        # 确定环境
        env_name = environment or os.getenv(f"{self.ENV_PREFIX}ENVIRONMENT", "development")
        
        try:
            env = Environment(env_name.lower())
        except ValueError:
            logger.warning(f"Unknown environment: {env_name}, using development")
            env = Environment.DEVELOPMENT
        
        # 加载基础配置
        config = self._load_base_config()
        config.environment = env
        
        # 加载环境特定配置
        env_config = self._load_env_config(env)
        self._merge_config(config, env_config)
        
        # 环境变量覆盖
        self._apply_env_overrides(config)
        
        logger.info(f"Loaded config for environment: {env.value}")
        return config
    
    def _load_base_config(self) -> DeploymentConfig:
        """加载基础配置"""
        base_path = self._config_dir / "base.json"
        
        if base_path.exists():
            try:
                with open(base_path) as f:
                    data = json.load(f)
                return self._dict_to_config(data)
            except Exception as e:
                logger.warning(f"Failed to load base config: {e}")
        
        return DeploymentConfig()
    
    def _load_env_config(self, env: Environment) -> Dict[str, Any]:
        """加载环境特定配置"""
        env_path = self._config_dir / f"{env.value}.json"
        
        if env_path.exists():
            try:
                with open(env_path) as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Failed to load env config: {e}")
        
        return {}
    
    def _merge_config(self, config: DeploymentConfig, overrides: Dict[str, Any]) -> None:
        """合并配置覆盖"""
        for key, value in overrides.items():
            if hasattr(config, key):
                current = getattr(config, key)
                if isinstance(current, (DatabaseConfig, RedisConfig, LLMConfig, 
                                       CacheConfig, ObservabilityConfig)):
                    # 子配置
                    for sub_key, sub_value in value.items():
                        if hasattr(current, sub_key):
                            setattr(current, sub_key, sub_value)
                else:
                    setattr(config, key, value)
    
    def _apply_env_overrides(self, config: DeploymentConfig) -> None:
        """应用环境变量覆盖"""
        # 基础配置
        if v := os.getenv(f"{self.ENV_PREFIX}DEBUG"):
            config.debug = v.lower() in ("true", "1", "yes")
        if v := os.getenv(f"{self.ENV_PREFIX}HOST"):
            config.host = v
        if v := os.getenv(f"{self.ENV_PREFIX}PORT"):
            config.port = int(v)
        if v := os.getenv(f"{self.ENV_PREFIX}WORKERS"):
            config.workers = int(v)
        
        # 数据库
        if v := os.getenv(f"{self.ENV_PREFIX}DB_HOST"):
            config.database.host = v
        if v := os.getenv(f"{self.ENV_PREFIX}DB_PORT"):
            config.database.port = int(v)
        if v := os.getenv(f"{self.ENV_PREFIX}DB_NAME"):
            config.database.database = v
        if v := os.getenv(f"{self.ENV_PREFIX}DB_USER"):
            config.database.username = v
        if v := os.getenv(f"{self.ENV_PREFIX}DB_PASSWORD"):
            config.database.password = v
        
        # Redis
        if v := os.getenv(f"{self.ENV_PREFIX}REDIS_HOST"):
            config.redis.host = v
        if v := os.getenv(f"{self.ENV_PREFIX}REDIS_PORT"):
            config.redis.port = int(v)
        if v := os.getenv(f"{self.ENV_PREFIX}REDIS_PASSWORD"):
            config.redis.password = v
        
        # LLM
        if v := os.getenv(f"{self.ENV_PREFIX}LLM_PROVIDER"):
            config.llm.provider = v
        if v := os.getenv(f"{self.ENV_PREFIX}LLM_MODEL"):
            config.llm.model = v
        if v := os.getenv(f"{self.ENV_PREFIX}LLM_API_KEY"):
            config.llm.api_key = v
        if v := os.getenv(f"{self.ENV_PREFIX}LLM_BASE_URL"):
            config.llm.base_url = v
    
    def _dict_to_config(self, data: Dict[str, Any]) -> DeploymentConfig:
        """字典转配置对象"""
        config = DeploymentConfig()
        
        for key, value in data.items():
            if key == "database":
                config.database = DatabaseConfig(**value)
            elif key == "redis":
                config.redis = RedisConfig(**value)
            elif key == "llm":
                config.llm = LLMConfig(**value)
            elif key == "cache":
                config.cache = CacheConfig(**value)
            elif key == "observability":
                config.observability = ObservabilityConfig(**value)
            elif key == "environment":
                config.environment = Environment(value)
            elif hasattr(config, key):
                setattr(config, key, value)
        
        return config


class ConfigValidator:
    """
    配置验证器
    
    对照 R-6-7-05: 配置验证
    """
    
    @staticmethod
    def validate(config: DeploymentConfig) -> List[str]:
        """
        验证配置
        
        Returns:
            错误列表（空列表表示验证通过）
        """
        errors = []
        
        # 基础验证
        if config.port < 1 or config.port > 65535:
            errors.append(f"Invalid port: {config.port}")
        
        if config.workers < 1:
            errors.append(f"Invalid workers count: {config.workers}")
        
        # 数据库验证
        if not config.database.host:
            errors.append("Database host is required")
        
        if config.database.pool_size < 1:
            errors.append(f"Invalid database pool size: {config.database.pool_size}")
        
        # 生产环境特定验证
        if config.environment == Environment.PRODUCTION:
            if config.debug:
                errors.append("Debug mode should be disabled in production")
            
            if not config.llm.api_key:
                errors.append("LLM API key is required in production")
            
            if not config.database.password:
                errors.append("Database password is required in production")
        
        return errors


# 全局配置单例
_config: Optional[DeploymentConfig] = None


def get_config() -> DeploymentConfig:
    """获取全局配置"""
    global _config
    if _config is None:
        loader = ConfigLoader()
        _config = loader.load()
    return _config


def set_config(config: DeploymentConfig) -> None:
    """设置全局配置"""
    global _config
    _config = config


def reset_config() -> None:
    """重置全局配置"""
    global _config
    _config = None
