"""
Tests for Deployment Config

部署配置测试。
"""

import json
import os
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

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


class TestDatabaseConfig:
    """DatabaseConfig 测试"""
    
    def test_default_values(self):
        """测试默认值"""
        config = DatabaseConfig()
        
        assert config.host == "localhost"
        assert config.port == 5432
        assert config.database == "lucidself"
    
    def test_connection_string(self):
        """测试连接字符串"""
        config = DatabaseConfig(
            host="db.example.com",
            port=5432,
            database="mydb",
            username="user",
            password="pass",
        )
        
        conn = config.connection_string
        
        assert "db.example.com" in conn
        assert "5432" in conn
        assert "mydb" in conn
        assert "user:pass" in conn


class TestRedisConfig:
    """RedisConfig 测试"""
    
    def test_connection_string(self):
        """测试连接字符串"""
        config = RedisConfig(host="redis.example.com", port=6379)
        
        assert "redis://redis.example.com:6379/0" == config.connection_string
    
    def test_connection_string_with_password(self):
        """测试带密码的连接字符串"""
        config = RedisConfig(host="redis.example.com", password="secret")
        
        assert ":secret@" in config.connection_string
    
    def test_ssl_connection_string(self):
        """测试 SSL 连接字符串"""
        config = RedisConfig(host="redis.example.com", ssl=True)
        
        assert config.connection_string.startswith("rediss://")


class TestDeploymentConfig:
    """DeploymentConfig 测试"""
    
    def test_default_values(self):
        """测试默认值"""
        config = DeploymentConfig()
        
        assert config.environment == Environment.DEVELOPMENT
        assert config.debug is False
        assert config.port == 8000
        assert config.workers == 4
    
    def test_sub_configs(self):
        """测试子配置"""
        config = DeploymentConfig()
        
        assert isinstance(config.database, DatabaseConfig)
        assert isinstance(config.redis, RedisConfig)
        assert isinstance(config.llm, LLMConfig)
        assert isinstance(config.cache, CacheConfig)
        assert isinstance(config.observability, ObservabilityConfig)


class TestConfigLoader:
    """ConfigLoader 测试"""
    
    def test_load_default(self):
        """测试加载默认配置"""
        loader = ConfigLoader(config_dir=Path("/nonexistent"))
        
        config = loader.load()
        
        assert config.environment == Environment.DEVELOPMENT
    
    def test_load_from_env_variable(self):
        """测试从环境变量加载"""
        with patch.dict(os.environ, {"LS_ENVIRONMENT": "production"}):
            loader = ConfigLoader(config_dir=Path("/nonexistent"))
            config = loader.load()
            
            assert config.environment == Environment.PRODUCTION
    
    def test_load_with_explicit_environment(self):
        """测试显式指定环境"""
        loader = ConfigLoader(config_dir=Path("/nonexistent"))
        
        config = loader.load(environment="staging")
        
        assert config.environment == Environment.STAGING
    
    def test_env_overrides(self):
        """测试环境变量覆盖"""
        env_vars = {
            "LS_DEBUG": "true",
            "LS_PORT": "9000",
            "LS_DB_HOST": "db.prod.com",
            "LS_REDIS_HOST": "redis.prod.com",
            "LS_LLM_API_KEY": "sk-test-key",
        }
        
        with patch.dict(os.environ, env_vars):
            loader = ConfigLoader(config_dir=Path("/nonexistent"))
            config = loader.load()
            
            assert config.debug is True
            assert config.port == 9000
            assert config.database.host == "db.prod.com"
            assert config.redis.host == "redis.prod.com"
            assert config.llm.api_key == "sk-test-key"
    
    def test_load_from_file(self):
        """测试从文件加载"""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_dir = Path(tmpdir)
            
            # 创建基础配置
            base_config = {
                "host": "0.0.0.0",
                "port": 8080,
                "database": {
                    "host": "localhost",
                    "port": 5432,
                },
            }
            
            with open(config_dir / "base.json", "w") as f:
                json.dump(base_config, f)
            
            loader = ConfigLoader(config_dir=config_dir)
            config = loader.load()
            
            assert config.port == 8080
            assert config.database.host == "localhost"
    
    def test_load_env_specific_file(self):
        """测试加载环境特定文件"""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_dir = Path(tmpdir)
            
            # 创建生产环境配置
            prod_config = {
                "debug": False,
                "workers": 8,
            }
            
            with open(config_dir / "production.json", "w") as f:
                json.dump(prod_config, f)
            
            loader = ConfigLoader(config_dir=config_dir)
            config = loader.load(environment="production")
            
            assert config.workers == 8


class TestConfigValidator:
    """ConfigValidator 测试"""
    
    def test_valid_config(self):
        """测试有效配置"""
        config = DeploymentConfig()
        
        errors = ConfigValidator.validate(config)
        
        assert errors == []
    
    def test_invalid_port(self):
        """测试无效端口"""
        config = DeploymentConfig(port=70000)
        
        errors = ConfigValidator.validate(config)
        
        assert any("port" in e.lower() for e in errors)
    
    def test_invalid_workers(self):
        """测试无效工作进程数"""
        config = DeploymentConfig(workers=0)
        
        errors = ConfigValidator.validate(config)
        
        assert any("workers" in e.lower() for e in errors)
    
    def test_production_requires_no_debug(self):
        """测试生产环境要求关闭 debug"""
        config = DeploymentConfig(
            environment=Environment.PRODUCTION,
            debug=True,
        )
        
        errors = ConfigValidator.validate(config)
        
        assert any("debug" in e.lower() for e in errors)
    
    def test_production_requires_api_key(self):
        """测试生产环境要求 API key"""
        config = DeploymentConfig(
            environment=Environment.PRODUCTION,
            debug=False,
        )
        config.llm.api_key = ""
        
        errors = ConfigValidator.validate(config)
        
        assert any("api key" in e.lower() for e in errors)


class TestGlobalConfig:
    """全局配置测试"""
    
    def setup_method(self):
        """每个测试前重置"""
        reset_config()
    
    def test_get_config(self):
        """测试获取配置"""
        config = get_config()
        
        assert isinstance(config, DeploymentConfig)
    
    def test_set_config(self):
        """测试设置配置"""
        custom = DeploymentConfig(port=9999)
        set_config(custom)
        
        config = get_config()
        
        assert config.port == 9999
    
    def test_reset_config(self):
        """测试重置配置"""
        custom = DeploymentConfig(port=9999)
        set_config(custom)
        reset_config()
        
        config = get_config()
        
        assert config.port == 8000  # 默认值


class TestIntegration:
    """集成测试"""
    
    def test_module_exports(self):
        """测试模块导出"""
        from backend.core.deployment import (
            DeploymentConfig,
            ConfigLoader,
            ConfigValidator,
            Environment,
            get_config,
            set_config,
            reset_config,
        )
        
        assert DeploymentConfig is not None
        assert ConfigLoader is not None
        assert ConfigValidator is not None
        assert Environment is not None
