"""
Geocoding Service

地理编码服务主类，实现城市级别的地理坐标解析。
"""

from typing import Optional

from backend.core.geocoding.models import Place, ResolvePlaceInput
from backend.core.geocoding.normalizer import Normalizer
from backend.core.geocoding.repository import (
    WorldCitiesRepository,
    GeoCacheRepository,
    UserPlacesRepository,
)
from backend.core.geocoding.exceptions import (
    NotFoundError,
    InvalidInputError,
    ProviderError,
)
from backend.core.geocoding.providers.amap import AmapProvider
from backend.core.geocoding.providers.nominatim import NominatimProvider
from backend.core.geocoding.providers.base import BaseProvider
from backend.core.geocoding.metrics import get_metrics, GeocodingMetrics
from backend.core.geocoding.logging import get_logger, GeocodingLogger


# Country name to ISO 3166-1 alpha-2 code mapping
COUNTRY_NAME_TO_CODE = {
    # English names
    'china': 'CN',
    'united states': 'US',
    'usa': 'US',
    'united kingdom': 'GB',
    'uk': 'GB',
    'japan': 'JP',
    'korea': 'KR',
    'south korea': 'KR',
    'germany': 'DE',
    'france': 'FR',
    'italy': 'IT',
    'spain': 'ES',
    'canada': 'CA',
    'australia': 'AU',
    'russia': 'RU',
    'india': 'IN',
    'brazil': 'BR',
    'mexico': 'MX',
    'singapore': 'SG',
    'taiwan': 'TW',
    'hong kong': 'HK',
    'macau': 'MO',
    # Chinese names
    '中国': 'CN',
    '美国': 'US',
    '英国': 'GB',
    '日本': 'JP',
    '韩国': 'KR',
    '德国': 'DE',
    '法国': 'FR',
    '意大利': 'IT',
    '西班牙': 'ES',
    '加拿大': 'CA',
    '澳大利亚': 'AU',
    '俄罗斯': 'RU',
    '印度': 'IN',
    '巴西': 'BR',
    '墨西哥': 'MX',
    '新加坡': 'SG',
    '台湾': 'TW',
    '香港': 'HK',
    '澳门': 'MO',
}


class GeocodingService:
    """
    Main geocoding service.
    
    地理编码服务主类，按以下顺序解析位置：
    1. user_places (用户级缓存)
    2. geo_cache (系统级缓存)
    3. world_cities (离线数据库)
    4. Amap (中国地区回退) - to be implemented in task 8
    5. Nominatim (全球回退) - to be implemented in task 9
    
    Requirements: 2.1, 3.4, 8.1, 8.2, 10.1, 10.2, 10.3
    """
    
    def __init__(
        self,
        normalizer: Optional[Normalizer] = None,
        user_places_repo: Optional[UserPlacesRepository] = None,
        geo_cache_repo: Optional[GeoCacheRepository] = None,
        world_cities_repo: Optional[WorldCitiesRepository] = None,
        amap_provider: Optional[BaseProvider] = None,
        nominatim_provider: Optional[BaseProvider] = None,
        metrics: Optional[GeocodingMetrics] = None,
        logger: Optional[GeocodingLogger] = None,
    ):
        """
        Initialize GeocodingService with dependencies.
        
        Args:
            normalizer: Input normalizer instance
            user_places_repo: User places repository
            geo_cache_repo: Geo cache repository
            world_cities_repo: World cities repository
            amap_provider: Amap provider for China fallback (Requirements 6.1, 6.2)
            nominatim_provider: Nominatim provider for global fallback (Requirements 7.1, 7.2)
            metrics: Metrics collector instance (Requirement 10.1, 10.2)
            logger: Structured logger instance (Requirement 10.3)
        """
        self._normalizer = normalizer or Normalizer()
        self._user_places = user_places_repo or UserPlacesRepository()
        self._geo_cache = geo_cache_repo or GeoCacheRepository()
        self._world_cities = world_cities_repo or WorldCitiesRepository()
        self._amap_provider = amap_provider or AmapProvider()
        self._nominatim_provider = nominatim_provider or NominatimProvider()
        self._metrics = metrics or get_metrics()
        self._logger = logger or get_logger()
    
    def _resolve_country_code(self, country_hint: Optional[str]) -> Optional[str]:
        """
        Resolve country hint to ISO 3166-1 alpha-2 code.
        
        Args:
            country_hint: Country name or code
            
        Returns:
            ISO 3166-1 alpha-2 code or None
        """
        if not country_hint:
            return None
        
        hint_lower = country_hint.lower().strip()
        
        # Check if it's already a 2-letter code
        if len(hint_lower) == 2 and hint_lower.isalpha():
            return hint_lower.upper()
        
        # Look up in mapping
        return COUNTRY_NAME_TO_CODE.get(hint_lower)
    
    async def resolve_place(self, input: ResolvePlaceInput) -> Place:
        """
        Resolve input text to a Place.
        
        Resolution order (Requirements 8.1, 8.2):
        1. user_places - if userId and hintLabel provided
        2. geo_cache - system-level cache
        3. world_cities - offline database
        4. Amap - China fallback (to be implemented)
        5. Nominatim - global fallback (to be implemented)
        
        Args:
            input: ResolvePlaceInput with input_text and optional hints
            
        Returns:
            Place object with all required fields
            
        Raises:
            InvalidInputError: When input cannot be parsed (Requirements 2.3, 2.4)
            NotFoundError: When no matching location found (Requirements 8.3)
        """
        # Increment request counter (Requirement 10.1)
        self._metrics.increment_request()
        
        # Log request start (Requirement 10.3)
        self._logger.log_request_start(
            input_text=input.input_text or '',
            country_code=input.hint_country,
            user_id=input.user_id,
            hint_label=input.hint_label
        )
        
        try:
            # Validate input
            if not input.input_text or not input.input_text.strip():
                raise InvalidInputError(
                    input.input_text or '',
                    reason="Input text is empty or contains only whitespace"
                )
            
            # Parse and normalize input
            city_name, parsed_country = self._normalizer.parse_city_country(input.input_text)
            
            if not city_name:
                raise InvalidInputError(
                    input.input_text,
                    reason="Could not extract city name from input"
                )
            
            # Determine country code from hint or parsed value
            country_code = self._resolve_country_code(input.hint_country)
            if not country_code and parsed_country:
                country_code = self._resolve_country_code(parsed_country)
            
            # Build cache key
            normalized_query = self._normalizer.normalize(city_name)
            cache_key = self._normalizer.build_cache_key(normalized_query, country_code)
            
            # Step 1: Check user_places (Requirements 4.1, 4.2)
            if input.user_id and input.hint_label:
                user_place = self._user_places.get_by_label(input.user_id, input.hint_label)
                if user_place is not None:
                    self._logger.log_cache_hit("user_places", f"{input.user_id}:{input.hint_label}", user_place.place_id)
                    return self._handle_success(user_place, input)
            
            # Step 2: Check geo_cache (Requirements 5.1, 5.2)
            cached_place = self._geo_cache.get(cache_key)
            if cached_place is not None:
                self._geo_cache.update_hit(cache_key)
                self._logger.log_cache_hit("geo_cache", cache_key, cached_place.place_id)
                return self._handle_success(cached_place, input)
            
            self._logger.log_cache_miss("geo_cache", cache_key)
            
            # Step 3: Query world_cities (Requirements 3.3, 3.4)
            place = self._query_world_cities(normalized_query, country_code)
            
            if place is not None:
                # Store in geo_cache (Requirements 5.3)
                self._geo_cache.set(cache_key, place)
                
                # Store in user_places if user context provided (Requirements 4.3)
                if input.user_id and input.hint_label:
                    self._user_places.bind(input.user_id, input.hint_label, place)
                
                return self._handle_success(place, input)
            
            # Step 4: Amap fallback for China (Requirements 6.1, 6.2, 6.4, 11.1, 11.2)
            if country_code == 'CN' and self._amap_provider.is_enabled():
                place = await self._try_amap(city_name, cache_key)
                if place is not None:
                    # Store in user_places if user context provided (Requirements 4.3)
                    if input.user_id and input.hint_label:
                        self._user_places.bind(input.user_id, input.hint_label, place)
                    return self._handle_success(place, input)
            
            # Step 5: Nominatim fallback (global) (Requirements 7.1, 7.2, 7.4, 11.3, 11.4)
            if self._nominatim_provider.is_enabled():
                place = await self._try_nominatim(city_name, country_code, cache_key)
                if place is not None:
                    # Store in user_places if user context provided (Requirements 4.3)
                    if input.user_id and input.hint_label:
                        self._user_places.bind(input.user_id, input.hint_label, place)
                    return self._handle_success(place, input)
            
            # All resolution steps failed (Requirements 2.3, 8.3)
            raise NotFoundError(input.input_text, country_code)
            
        except InvalidInputError as e:
            self._metrics.increment_error("InvalidInputError")
            self._logger.log_request_error(
                input_text=input.input_text or '',
                error_type="InvalidInputError",
                error_message=str(e),
                country_code=input.hint_country
            )
            raise
        except NotFoundError as e:
            self._metrics.increment_error("NotFoundError")
            self._logger.log_request_error(
                input_text=input.input_text or '',
                error_type="NotFoundError",
                error_message=str(e),
                country_code=input.hint_country
            )
            raise
        except Exception as e:
            self._metrics.increment_error(type(e).__name__)
            self._logger.log_request_error(
                input_text=input.input_text or '',
                error_type=type(e).__name__,
                error_message=str(e),
                country_code=input.hint_country,
                exc_info=True
            )
            raise
    
    def _handle_success(self, place: Place, input: ResolvePlaceInput) -> Place:
        """Handle successful resolution with metrics and logging."""
        self._metrics.increment_success()
        self._logger.log_request_success(
            input_text=input.input_text or '',
            place_id=place.place_id,
            source=place.source,
            country_code=place.country_code
        )
        return place
    
    def _query_world_cities(
        self,
        city_name: str,
        country_code: Optional[str]
    ) -> Optional[Place]:
        """
        Query world_cities database for matching place.
        
        Args:
            city_name: Normalized city name
            country_code: Optional ISO country code
            
        Returns:
            Place with source='local_db' if found, None otherwise
        """
        if country_code:
            # Query with country code constraint
            return self._world_cities.find_by_country_city(country_code, city_name)
        
        # Without country code, we need to search more broadly
        # For now, return None - in a full implementation, we might
        # search across all countries and return the most populous match
        return None
    
    async def _try_amap(
        self,
        city_name: str,
        cache_key: str
    ) -> Optional[Place]:
        """
        Try to resolve place using Amap provider.
        
        Args:
            city_name: City name to geocode
            cache_key: Cache key for storing result
            
        Returns:
            Place with source='amap' if found, None otherwise
            
        Requirements: 6.1, 6.2, 10.2
        """
        # Log provider call (Requirement 10.3)
        self._logger.log_provider_call("amap", city_name, "CN")
        
        # Increment external call counter (Requirement 10.2)
        self._metrics.increment_external_call("amap")
        
        try:
            place = await self._amap_provider.geocode(city_name, country="CN")
            
            if place is not None:
                # Insert into world_cities for future offline lookups (Requirement 6.2)
                self._world_cities.insert(place)
                
                # Insert into geo_cache (Requirement 5.3)
                self._geo_cache.set(cache_key, place)
                
                # Log success (Requirement 10.3)
                self._logger.log_provider_success("amap", place.place_id, city_name)
                
                return place
        except ProviderError as e:
            # Log provider error (Requirement 10.3)
            self._logger.log_provider_error(
                "amap",
                "ProviderError",
                str(e),
                city_name,
                exc_info=True
            )
        except Exception as e:
            # Log unexpected error (Requirement 10.3)
            self._logger.log_provider_error(
                "amap",
                type(e).__name__,
                str(e),
                city_name,
                exc_info=True
            )
        
        return None
    
    async def _try_nominatim(
        self,
        city_name: str,
        country_code: Optional[str],
        cache_key: str
    ) -> Optional[Place]:
        """
        Try to resolve place using Nominatim provider.
        
        Args:
            city_name: City name to geocode
            country_code: Optional country code hint
            cache_key: Cache key for storing result
            
        Returns:
            Place with source='nominatim' if found, None otherwise
            
        Requirements: 7.1, 7.2, 10.2
        """
        # Log provider call (Requirement 10.3)
        self._logger.log_provider_call("nominatim", city_name, country_code)
        
        # Increment external call counter (Requirement 10.2)
        self._metrics.increment_external_call("nominatim")
        
        try:
            place = await self._nominatim_provider.geocode(city_name, country=country_code)
            
            if place is not None:
                # Insert into world_cities for future offline lookups (Requirement 7.2)
                self._world_cities.insert(place)
                
                # Insert into geo_cache (Requirement 5.3)
                self._geo_cache.set(cache_key, place)
                
                # Log success (Requirement 10.3)
                self._logger.log_provider_success("nominatim", place.place_id, city_name)
                
                return place
        except ProviderError as e:
            # Log provider error (Requirement 10.3)
            self._logger.log_provider_error(
                "nominatim",
                "ProviderError",
                str(e),
                city_name,
                exc_info=True
            )
        except Exception as e:
            # Log unexpected error (Requirement 10.3)
            self._logger.log_provider_error(
                "nominatim",
                type(e).__name__,
                str(e),
                city_name,
                exc_info=True
            )
        
        return None

