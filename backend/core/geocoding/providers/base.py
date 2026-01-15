"""
Base Provider Interface

地理编码提供商基类定义。
"""

from abc import ABC, abstractmethod
from typing import Optional
from backend.core.geocoding.models import Place


class BaseProvider(ABC):
    """
    Abstract base class for geocoding providers.
    
    地理编码提供商抽象基类。
    """
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Provider name for logging and metrics."""
        ...
    
    @property
    @abstractmethod
    def source_tag(self) -> str:
        """Source tag to use in Place.source field."""
        ...
    
    @abstractmethod
    async def geocode(
        self,
        city: str,
        country: Optional[str] = None
    ) -> Optional[Place]:
        """
        Geocode a city name to a Place.
        
        Args:
            city: City name to geocode
            country: Optional country hint (ISO 3166-1 alpha-2)
            
        Returns:
            Place if found, None otherwise
        """
        ...
    
    @abstractmethod
    def is_enabled(self) -> bool:
        """Check if this provider is enabled and configured."""
        ...
