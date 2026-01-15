"""
Unit Tests for Geocoding Configuration

地理编码服务配置的单元测试。

Requirements: 11.1, 11.2, 11.3, 11.4
"""

import os
import pytest
from unittest.mock import patch

from backend.core.geocoding.config import (
    GeocodingConfig,
    get_config,
    reload_config,
    set_config,
    ENV_AMAP_API_KEY,
    ENV_GEOCODING_ENABLE_AMAP,
    ENV_GEOCODING_ENABLE_NOMINATIM,
    ENV_GEOCODING_NOMINATIM_BASE_URL,
    DEFAULT_NOMINATIM_URL,
)


class TestGeocodingConfig:
    """Tests for GeocodingConfig class."""
    
    def test_default_values(self):
        """Test default configuration values."""
        config = GeocodingConfig()
        
        assert config.amap_api_key is None
        assert config.enable_amap is True
        assert config.enable_nominatim is True
        assert config.nominatim_base_url == DEFAULT_NOMINATIM_URL
    
    def test_custom_values(self):
        """Test configuration with custom values."""
        config = GeocodingConfig(
            amap_api_key="test-key",
            enable_amap=False,
            enable_nominatim=False,
            nominatim_base_url="https://custom.nominatim.org"
        )
        
        assert config.amap_api_key == "test-key"
        assert config.enable_amap is False
        assert config.enable_nominatim is False
        assert config.nominatim_base_url == "https://custom.nominatim.org"


class TestConfigFromEnv:
    """Tests for loading configuration from environment variables."""
    
    def test_amap_api_key_from_env(self):
        """
        Test AMAP_API_KEY environment variable.
        
        Requirement 11.1
        """
        with patch.dict(os.environ, {ENV_AMAP_API_KEY: "my-amap-key"}):
            config = GeocodingConfig.from_env()
            assert config.amap_api_key == "my-amap-key"
    
    def test_amap_api_key_not_set(self):
        """
        Test when AMAP_API_KEY is not set.
        
        Requirement 11.1
        """
        env = {k: v for k, v in os.environ.items() if k != ENV_AMAP_API_KEY}
        with patch.dict(os.environ, env, clear=True):
            config = GeocodingConfig.from_env()
            assert config.amap_api_key is None
    
    def test_enable_amap_true_values(self):
        """
        Test GEOCODING_ENABLE_AMAP with various true values.
        
        Requirement 11.2
        """
        for value in ["true", "True", "TRUE", "1", "yes", "Yes", "YES"]:
            with patch.dict(os.environ, {ENV_GEOCODING_ENABLE_AMAP: value}):
                config = GeocodingConfig.from_env()
                assert config.enable_amap is True, f"Failed for value: {value}"
    
    def test_enable_amap_false_values(self):
        """
        Test GEOCODING_ENABLE_AMAP with various false values.
        
        Requirement 11.2
        """
        for value in ["false", "False", "FALSE", "0", "no", "No", "NO", "anything"]:
            with patch.dict(os.environ, {ENV_GEOCODING_ENABLE_AMAP: value}):
                config = GeocodingConfig.from_env()
                assert config.enable_amap is False, f"Failed for value: {value}"
    
    def test_enable_amap_default(self):
        """
        Test GEOCODING_ENABLE_AMAP default value when not set.
        
        Requirement 11.2
        """
        env = {k: v for k, v in os.environ.items() if k != ENV_GEOCODING_ENABLE_AMAP}
        with patch.dict(os.environ, env, clear=True):
            config = GeocodingConfig.from_env()
            assert config.enable_amap is True  # Default is True
    
    def test_enable_nominatim_true_values(self):
        """
        Test GEOCODING_ENABLE_NOMINATIM with various true values.
        
        Requirement 11.3
        """
        for value in ["true", "True", "TRUE", "1", "yes", "Yes", "YES"]:
            with patch.dict(os.environ, {ENV_GEOCODING_ENABLE_NOMINATIM: value}):
                config = GeocodingConfig.from_env()
                assert config.enable_nominatim is True, f"Failed for value: {value}"
    
    def test_enable_nominatim_false_values(self):
        """
        Test GEOCODING_ENABLE_NOMINATIM with various false values.
        
        Requirement 11.3
        """
        for value in ["false", "False", "FALSE", "0", "no", "No", "NO", "anything"]:
            with patch.dict(os.environ, {ENV_GEOCODING_ENABLE_NOMINATIM: value}):
                config = GeocodingConfig.from_env()
                assert config.enable_nominatim is False, f"Failed for value: {value}"
    
    def test_enable_nominatim_default(self):
        """
        Test GEOCODING_ENABLE_NOMINATIM default value when not set.
        
        Requirement 11.3
        """
        env = {k: v for k, v in os.environ.items() if k != ENV_GEOCODING_ENABLE_NOMINATIM}
        with patch.dict(os.environ, env, clear=True):
            config = GeocodingConfig.from_env()
            assert config.enable_nominatim is True  # Default is True
    
    def test_nominatim_base_url_from_env(self):
        """
        Test GEOCODING_NOMINATIM_BASE_URL environment variable.
        
        Requirement 11.4
        """
        custom_url = "https://my-nominatim.example.com"
        with patch.dict(os.environ, {ENV_GEOCODING_NOMINATIM_BASE_URL: custom_url}):
            config = GeocodingConfig.from_env()
            assert config.nominatim_base_url == custom_url
    
    def test_nominatim_base_url_default(self):
        """
        Test GEOCODING_NOMINATIM_BASE_URL default value when not set.
        
        Requirement 11.4
        """
        env = {k: v for k, v in os.environ.items() if k != ENV_GEOCODING_NOMINATIM_BASE_URL}
        with patch.dict(os.environ, env, clear=True):
            config = GeocodingConfig.from_env()
            assert config.nominatim_base_url == DEFAULT_NOMINATIM_URL


class TestIsAmapEnabled:
    """Tests for is_amap_enabled() method."""
    
    def test_enabled_with_api_key(self):
        """
        Test Amap is enabled when flag is true and API key is set.
        
        Requirements 11.1, 11.2
        """
        config = GeocodingConfig(
            amap_api_key="test-key",
            enable_amap=True
        )
        assert config.is_amap_enabled() is True
    
    def test_disabled_without_api_key(self):
        """
        Test Amap is disabled when API key is not set.
        
        Requirements 11.1, 11.2
        """
        config = GeocodingConfig(
            amap_api_key=None,
            enable_amap=True
        )
        assert config.is_amap_enabled() is False
    
    def test_disabled_with_flag_false(self):
        """
        Test Amap is disabled when flag is false even with API key.
        
        Requirement 11.2
        """
        config = GeocodingConfig(
            amap_api_key="test-key",
            enable_amap=False
        )
        assert config.is_amap_enabled() is False
    
    def test_disabled_with_empty_api_key(self):
        """
        Test Amap is disabled when API key is empty string.
        
        Requirements 11.1, 11.2
        """
        config = GeocodingConfig(
            amap_api_key="",
            enable_amap=True
        )
        assert config.is_amap_enabled() is False


class TestIsNominatimEnabled:
    """Tests for is_nominatim_enabled() method."""
    
    def test_enabled_when_flag_true(self):
        """
        Test Nominatim is enabled when flag is true.
        
        Requirement 11.3
        """
        config = GeocodingConfig(enable_nominatim=True)
        assert config.is_nominatim_enabled() is True
    
    def test_disabled_when_flag_false(self):
        """
        Test Nominatim is disabled when flag is false.
        
        Requirement 11.3
        """
        config = GeocodingConfig(enable_nominatim=False)
        assert config.is_nominatim_enabled() is False


class TestGlobalConfigFunctions:
    """Tests for global configuration functions."""
    
    def test_get_config_returns_singleton(self):
        """Test get_config returns the same instance."""
        # Reset first
        reload_config()
        
        config1 = get_config()
        config2 = get_config()
        
        assert config1 is config2
    
    def test_reload_config_creates_new_instance(self):
        """Test reload_config creates a new configuration instance."""
        config1 = get_config()
        config2 = reload_config()
        
        # Should be different instances
        assert config1 is not config2
    
    def test_set_config_overrides_global(self):
        """Test set_config allows setting custom configuration."""
        custom_config = GeocodingConfig(
            amap_api_key="custom-key",
            enable_amap=False
        )
        
        set_config(custom_config)
        
        retrieved = get_config()
        assert retrieved is custom_config
        assert retrieved.amap_api_key == "custom-key"
        assert retrieved.enable_amap is False
        
        # Clean up
        reload_config()
    
    def test_reload_config_reads_env(self):
        """Test reload_config reads from environment variables."""
        with patch.dict(os.environ, {
            ENV_AMAP_API_KEY: "reloaded-key",
            ENV_GEOCODING_ENABLE_AMAP: "false"
        }):
            config = reload_config()
            
            assert config.amap_api_key == "reloaded-key"
            assert config.enable_amap is False
