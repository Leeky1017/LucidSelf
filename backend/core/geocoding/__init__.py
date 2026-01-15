"""
Geocoding Service Module

地理编码服务模块，提供城市级别的地理坐标解析。
支持中英文城市名输入，返回标准化的Place对象。
"""

from backend.core.geocoding.models import Place, ResolvePlaceInput
from backend.core.geocoding.exceptions import (
    GeocodingError,
    NotFoundError,
    InvalidInputError,
    ProviderError,
)
from backend.core.geocoding.repository import (
    WorldCitiesRepository,
    GeoCacheRepository,
    UserPlacesRepository,
)
from backend.core.geocoding.service import GeocodingService
from backend.core.geocoding.normalizer import Normalizer
from backend.core.geocoding.resolver import LocationResolver
from backend.core.geocoding.metrics import (
    GeocodingMetrics,
    get_metrics,
    reset_metrics,
)
from backend.core.geocoding.logging import (
    GeocodingLogger,
    LogContext,
    get_logger,
)
from backend.core.geocoding.config import (
    GeocodingConfig,
    get_config,
    reload_config,
    set_config,
)

__all__ = [
    # Models
    "Place",
    "ResolvePlaceInput",
    # Exceptions
    "GeocodingError",
    "NotFoundError",
    "InvalidInputError",
    "ProviderError",
    # Repositories
    "WorldCitiesRepository",
    "GeoCacheRepository",
    "UserPlacesRepository",
    # Service
    "GeocodingService",
    "Normalizer",
    "LocationResolver",
    # Metrics (Requirement 10.1, 10.2)
    "GeocodingMetrics",
    "get_metrics",
    "reset_metrics",
    # Logging (Requirement 10.3)
    "GeocodingLogger",
    "LogContext",
    "get_logger",
    # Configuration (Requirement 11.1, 11.2, 11.3, 11.4)
    "GeocodingConfig",
    "get_config",
    "reload_config",
    "set_config",
]
