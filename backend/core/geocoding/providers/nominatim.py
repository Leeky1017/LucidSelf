"""
Nominatim (OpenStreetMap) Geocoding Provider

Nominatim地理编码提供商，用于全球地址解析。

Requirements: 7.1, 7.2, 7.3, 7.4
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


# Default Nominatim endpoint (public OSM instance)
DEFAULT_NOMINATIM_URL = "https://nominatim.openstreetmap.org"

# Environment variable names
ENV_GEOCODING_ENABLE_NOMINATIM = "GEOCODING_ENABLE_NOMINATIM"
ENV_GEOCODING_NOMINATIM_BASE_URL = "GEOCODING_NOMINATIM_BASE_URL"


class RateLimiter:
    """Simple rate limiter for API calls."""
    
    def __init__(self, max_qps: float):
        self._max_qps = max_qps
        self._min_interval = 1.0 / max_qps
        self._last_call_time: float = 0.0
        self._lock = asyncio.Lock()
    
    async def acquire(self) -> None:
        """Acquire permission to make an API call."""
        async with self._lock:
            now = time.monotonic()
            elapsed = now - self._last_call_time
            
            if elapsed < self._min_interval:
                wait_time = self._min_interval - elapsed
                await asyncio.sleep(wait_time)
            
            self._last_call_time = time.monotonic()


class NominatimProvider(BaseProvider):
    """
    Nominatim geocoding provider (global).
    
    Requirements:
    - 7.1: Call Nominatim as final fallback when all else fails
    - 7.2: Map response to Place with source='nominatim'
    - 7.3: Enforce rate limiting of 1 QPS
    - 7.4: Use configurable base URL or default public endpoint
    """
    
    MAX_QPS = 1.0
    
    def __init__(
        self,
        base_url: Optional[str] = None,
        enabled: Optional[bool] = None,
        http_client: Optional[httpx.AsyncClient] = None,
    ):
        self._base_url = (
            base_url
            or os.environ.get(ENV_GEOCODING_NOMINATIM_BASE_URL)
            or DEFAULT_NOMINATIM_URL
        )
        
        if enabled is not None:
            self._enabled = enabled
        else:
            env_enabled = os.environ.get(ENV_GEOCODING_ENABLE_NOMINATIM, "true").lower()
            self._enabled = env_enabled in ("true", "1", "yes")
        
        self._http_client = http_client
        self._rate_limiter = RateLimiter(self.MAX_QPS)
    
    @property
    def name(self) -> str:
        return "nominatim"
    
    @property
    def source_tag(self) -> str:
        return "nominatim"
    
    def is_enabled(self) -> bool:
        return self._enabled
    
    async def geocode(
        self,
        city: str,
        country: Optional[str] = None
    ) -> Optional[Place]:
        """Geocode a city name using Nominatim API."""
        if not self.is_enabled():
            return None
        
        await self._rate_limiter.acquire()
        
        try:
            result = await self._call_api(city, country)
            if result is None:
                return None
            return self._map_to_place(result, city)
        except httpx.HTTPError as e:
            raise ProviderError(self.name, e)
    
    async def _call_api(self, city: str, country: Optional[str] = None) -> Optional[dict]:
        """Call Nominatim geocoding API."""
        query = f"{city}, {country}" if country else city
        
        params = {
            "q": query,
            "format": "json",
            "limit": "1",
            "addressdetails": "1",
            "featuretype": "city",
        }
        
        if country:
            params["countrycodes"] = country.lower()
        
        url = f"{self._base_url}/search"
        headers = {"User-Agent": "LucidSelf-GeocodingService/1.0"}
        
        if self._http_client:
            response = await self._http_client.get(url, params=params, headers=headers)
        else:
            async with httpx.AsyncClient() as client:
                response = await client.get(url, params=params, headers=headers)
        
        response.raise_for_status()
        data = response.json()
        
        return data[0] if data else None
    
    def _map_to_place(self, result: dict, original_query: str) -> Place:
        """Map Nominatim API result to Place object."""
        lat = float(result.get("lat", 0))
        lng = float(result.get("lon", 0))
        
        address = result.get("address", {})
        
        city_name = (
            address.get("city")
            or address.get("town")
            or address.get("municipality")
            or address.get("village")
            or result.get("name")
            or original_query
        )
        
        country_code = address.get("country_code", "").upper() or "XX"
        admin1_name = address.get("state") or address.get("province")
        admin1_code = address.get("state_code")
        district_name = address.get("district") or address.get("suburb")
        
        osm_type = result.get("osm_type", "node")
        osm_id = result.get("osm_id", "")
        place_id = f"osm-{osm_type[0]}{osm_id}" if osm_id else f"nom-{uuid.uuid4().hex[:12]}"
        
        timezone = self._get_timezone_for_country(country_code, lng)
        
        return Place(
            place_id=place_id,
            country_code=country_code,
            city_name=str(city_name),
            lat=lat,
            lng=lng,
            timezone=timezone,
            source="nominatim",
            accuracy="city",
            admin1_code=admin1_code,
            admin1_name=admin1_name,
            district_name_raw=district_name,
        )
    
    def _get_timezone_for_country(self, country_code: str, lng: float) -> str:
        """Get approximate timezone for a country."""
        country_timezones = {
            "CN": "Asia/Shanghai",
            "JP": "Asia/Tokyo",
            "KR": "Asia/Seoul",
            "TW": "Asia/Taipei",
            "HK": "Asia/Hong_Kong",
            "SG": "Asia/Singapore",
            "IN": "Asia/Kolkata",
            "AU": "Australia/Sydney",
            "NZ": "Pacific/Auckland",
            "GB": "Europe/London",
            "DE": "Europe/Berlin",
            "FR": "Europe/Paris",
            "IT": "Europe/Rome",
            "ES": "Europe/Madrid",
            "RU": "Europe/Moscow",
            "BR": "America/Sao_Paulo",
            "MX": "America/Mexico_City",
            "CA": "America/Toronto",
            "US": self._get_us_timezone(lng),
        }
        
        if country_code in country_timezones:
            return country_timezones[country_code]
        
        return self._estimate_timezone_from_longitude(lng)
    
    def _get_us_timezone(self, lng: float) -> str:
        """Get US timezone based on longitude."""
        if lng < -115:
            return "America/Los_Angeles"
        elif lng < -100:
            return "America/Denver"
        elif lng < -85:
            return "America/Chicago"
        return "America/New_York"
    
    def _estimate_timezone_from_longitude(self, lng: float) -> str:
        """Estimate timezone from longitude."""
        offset_hours = round(lng / 15)
        
        offset_to_tz = {
            -12: "Etc/GMT+12", -11: "Pacific/Midway", -10: "Pacific/Honolulu",
            -9: "America/Anchorage", -8: "America/Los_Angeles", -7: "America/Denver",
            -6: "America/Chicago", -5: "America/New_York", -4: "America/Halifax",
            -3: "America/Sao_Paulo", -2: "Atlantic/South_Georgia", -1: "Atlantic/Azores",
            0: "UTC", 1: "Europe/Paris", 2: "Europe/Helsinki", 3: "Europe/Moscow",
            4: "Asia/Dubai", 5: "Asia/Karachi", 6: "Asia/Dhaka", 7: "Asia/Bangkok",
            8: "Asia/Shanghai", 9: "Asia/Tokyo", 10: "Australia/Sydney",
            11: "Pacific/Noumea", 12: "Pacific/Auckland",
        }
        
        return offset_to_tz.get(offset_hours, "UTC")
