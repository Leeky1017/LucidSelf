"""
Amap (高德地图) Geocoding Provider

高德地图地理编码提供商，用于中国地区的地址解析。

Requirements: 6.1, 6.2, 6.3, 6.4
"""

import asyncio
import os
import time
import uuid
from typing import Optional

import httpx

from backend.core.geocoding.models import Place
from backend.core.geocoding.providers.base import BaseProvider
from backend.core.geocoding.exceptions import ProviderError


# Amap API endpoint
AMAP_GEOCODE_URL = "https://restapi.amap.com/v3/geocode/geo"

# Environment variable names
ENV_AMAP_API_KEY = "AMAP_API_KEY"
ENV_GEOCODING_ENABLE_AMAP = "GEOCODING_ENABLE_AMAP"


class RateLimiter:
    """
    Simple rate limiter for API calls.
    
    简单的API调用速率限制器。
    """
    
    def __init__(self, max_qps: float):
        """
        Initialize rate limiter.
        
        Args:
            max_qps: Maximum queries per second
        """
        self._max_qps = max_qps
        self._min_interval = 1.0 / max_qps
        self._last_call_time: float = 0.0
        self._lock = asyncio.Lock()
    
    async def acquire(self) -> None:
        """
        Acquire permission to make an API call.
        
        Blocks until rate limit allows the call.
        """
        async with self._lock:
            now = time.monotonic()
            elapsed = now - self._last_call_time
            
            if elapsed < self._min_interval:
                wait_time = self._min_interval - elapsed
                await asyncio.sleep(wait_time)
            
            self._last_call_time = time.monotonic()


class AmapProvider(BaseProvider):
    """
    Amap geocoding provider for China.
    
    高德地图地理编码提供商，专用于中国大陆地区。
    
    Requirements:
    - 6.1: Call Amap when country_code='CN' and world_cities fails
    - 6.2: Map response to Place with source='amap'
    - 6.3: Enforce rate limiting of 5 QPS
    - 6.4: Skip if API key not configured
    """
    
    # Rate limit: 5 QPS maximum (Requirement 6.3)
    MAX_QPS = 5.0
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        enabled: Optional[bool] = None,
        http_client: Optional[httpx.AsyncClient] = None,
    ):
        """
        Initialize Amap provider.
        
        Args:
            api_key: Amap API key. If None, reads from AMAP_API_KEY env var.
            enabled: Whether provider is enabled. If None, reads from GEOCODING_ENABLE_AMAP env var.
            http_client: Optional HTTP client for testing.
        """
        self._api_key = api_key or os.environ.get(ENV_AMAP_API_KEY)
        
        # Determine enabled state (Requirement 11.2)
        if enabled is not None:
            self._enabled = enabled
        else:
            env_enabled = os.environ.get(ENV_GEOCODING_ENABLE_AMAP, "true").lower()
            self._enabled = env_enabled in ("true", "1", "yes")
        
        self._http_client = http_client
        self._rate_limiter = RateLimiter(self.MAX_QPS)
    
    @property
    def name(self) -> str:
        return "amap"
    
    @property
    def source_tag(self) -> str:
        return "amap"
    
    def is_enabled(self) -> bool:
        """
        Check if Amap provider is enabled and API key is configured.
        
        Requirements: 6.4, 11.1, 11.2
        """
        return self._enabled and bool(self._api_key)
    
    async def geocode(
        self,
        city: str,
        country: Optional[str] = None
    ) -> Optional[Place]:
        """
        Geocode a city name using Amap API.
        
        使用高德地图API解析城市名。
        
        Args:
            city: City name to geocode (Chinese preferred)
            country: Country hint (ignored, Amap is China-only)
            
        Returns:
            Place with source='amap' if found, None otherwise
            
        Raises:
            ProviderError: If API call fails
            
        Requirements: 6.1, 6.2
        """
        if not self.is_enabled():
            return None
        
        # Enforce rate limit (Requirement 6.3)
        await self._rate_limiter.acquire()
        
        try:
            result = await self._call_api(city)
            if result is None:
                return None
            
            return self._map_to_place(result, city)
        except httpx.HTTPError as e:
            raise ProviderError(self.name, e)
    
    async def _call_api(self, address: str) -> Optional[dict]:
        """
        Call Amap geocoding API.
        
        Args:
            address: Address string to geocode
            
        Returns:
            First geocode result dict, or None if no results
        """
        params = {
            "key": self._api_key,
            "address": address,
            "output": "json",
        }
        
        # Use provided client or create a new one
        if self._http_client:
            response = await self._http_client.get(AMAP_GEOCODE_URL, params=params)
        else:
            async with httpx.AsyncClient() as client:
                response = await client.get(AMAP_GEOCODE_URL, params=params)
        
        response.raise_for_status()
        data = response.json()
        
        # Check Amap response status
        # status=1 means success, status=0 means failure
        if data.get("status") != "1":
            return None
        
        geocodes = data.get("geocodes", [])
        if not geocodes:
            return None
        
        return geocodes[0]
    
    def _map_to_place(self, result: dict, original_query: str) -> Place:
        """
        Map Amap API result to Place object.
        
        Args:
            result: Amap geocode result dict
            original_query: Original query string for fallback
            
        Returns:
            Place with source='amap'
            
        Requirements: 6.2
        """
        # Parse location "lng,lat" format
        location = result.get("location", "")
        if location:
            lng_str, lat_str = location.split(",")
            lng = float(lng_str)
            lat = float(lat_str)
        else:
            # Fallback - should not happen with valid results
            lng, lat = 0.0, 0.0
        
        # Extract city name - Amap returns formatted_address and city
        city_name = result.get("city") or result.get("formatted_address") or original_query
        # Handle case where city is an empty list (happens for municipalities)
        if isinstance(city_name, list):
            city_name = result.get("province") or original_query
        
        # Extract province as admin1
        province = result.get("province", "")
        if isinstance(province, list):
            province = province[0] if province else ""
        
        # Extract adcode for place_id
        adcode = result.get("adcode", "")
        place_id = f"amap-{adcode}" if adcode else f"amap-{uuid.uuid4().hex[:12]}"
        
        # Determine timezone - China uses Asia/Shanghai
        timezone = "Asia/Shanghai"
        
        return Place(
            place_id=place_id,
            country_code="CN",
            city_name=str(city_name),
            lat=lat,
            lng=lng,
            timezone=timezone,
            source="amap",
            accuracy="city",
            admin1_code=adcode[:2] if adcode and len(adcode) >= 2 else None,
            admin1_name=str(province) if province else None,
            district_name_raw=result.get("district"),
        )
