"""
Geocoding Service Configuration

地理编码服务的配置模块。
提供环境变量读取和功能标志管理。

Requirements: 11.1, 11.2, 11.3, 11.4
"""

import os
from dataclasses import dataclass
from typing import Optional


# Environment variable names
ENV_AMAP_API_KEY = "AMAP_API_KEY"
ENV_GEOCODING_ENABLE_AMAP = "GEOCODING_ENABLE_AMAP"
ENV_GEOCODING_ENABLE_NOMINATIM = "GEOCODING_ENABLE_NOMINATIM"
ENV_GEOCODING_NOMINATIM_BASE_URL = "GEOCODING_NOMINATIM_BASE_URL"

# Default values
DEFAULT_NOMINATIM_URL = "https://nominatim.openstreetmap.org"
DEFAULT_ENABLE_AMAP = True
DEFAULT_ENABLE_NOMINATIM = True


def _parse_bool_env(value: Optional[str], default: bool = True) -> bool:
    """
    Parse boolean from environment variable string.
    
    Args:
        value: Environment variable value
        default: Default value if not set
        
    Returns:
        Boolean value
    """
    if value is None:
        return default
    return value.lower() in ("true", "1", "yes")


@dataclass
class GeocodingConfig:
    """
    Configuration for geocoding service.
    
    地理编码服务配置。
    
    Requirements:
    - 11.1: AMAP_API_KEY for Amap authentication
    - 11.2: GEOCODING_ENABLE_AMAP feature flag
    - 11.3: GEOCODING_ENABLE_NOMINATIM feature flag
    - 11.4: GEOCODING_NOMINATIM_BASE_URL configuration
    """
    
    # Amap configuration (Requirements 11.1, 11.2)
    amap_api_key: Optional[str] = None
    enable_amap: bool = DEFAULT_ENABLE_AMAP
    
    # Nominatim configuration (Requirements 11.3, 11.4)
    enable_nominatim: bool = DEFAULT_ENABLE_NOMINATIM
    nominatim_base_url: str = DEFAULT_NOMINATIM_URL
    
    @classmethod
    def from_env(cls) -> "GeocodingConfig":
        """
        Create configuration from environment variables.
        
        Returns:
            GeocodingConfig instance populated from environment
            
        Requirements: 11.1, 11.2, 11.3, 11.4
        """
        return cls(
            # Requirement 11.1: AMAP_API_KEY
            amap_api_key=os.environ.get(ENV_AMAP_API_KEY),
            
            # Requirement 11.2: GEOCODING_ENABLE_AMAP
            enable_amap=_parse_bool_env(
                os.environ.get(ENV_GEOCODING_ENABLE_AMAP),
                DEFAULT_ENABLE_AMAP
            ),
            
            # Requirement 11.3: GEOCODING_ENABLE_NOMINATIM
            enable_nominatim=_parse_bool_env(
                os.environ.get(ENV_GEOCODING_ENABLE_NOMINATIM),
                DEFAULT_ENABLE_NOMINATIM
            ),
            
            # Requirement 11.4: GEOCODING_NOMINATIM_BASE_URL
            nominatim_base_url=os.environ.get(
                ENV_GEOCODING_NOMINATIM_BASE_URL,
                DEFAULT_NOMINATIM_URL
            ),
        )
    
    def is_amap_enabled(self) -> bool:
        """
        Check if Amap provider is enabled and configured.
        
        Returns:
            True if Amap is enabled AND API key is set
            
        Requirements: 11.1, 11.2
        """
        return self.enable_amap and bool(self.amap_api_key)
    
    def is_nominatim_enabled(self) -> bool:
        """
        Check if Nominatim provider is enabled.
        
        Returns:
            True if Nominatim is enabled
            
        Requirement 11.3
        """
        return self.enable_nominatim


# Global configuration instance
_config: Optional[GeocodingConfig] = None


def get_config() -> GeocodingConfig:
    """
    Get the global configuration instance.
    
    Returns:
        GeocodingConfig singleton instance
    """
    global _config
    if _config is None:
        _config = GeocodingConfig.from_env()
    return _config


def reload_config() -> GeocodingConfig:
    """
    Reload configuration from environment variables.
    
    Useful for testing or when environment changes.
    
    Returns:
        New GeocodingConfig instance
    """
    global _config
    _config = GeocodingConfig.from_env()
    return _config


def set_config(config: GeocodingConfig) -> None:
    """
    Set the global configuration instance.
    
    Useful for testing with custom configuration.
    
    Args:
        config: Configuration instance to use
    """
    global _config
    _config = config
