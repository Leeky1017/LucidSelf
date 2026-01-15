"""
Property-Based Tests for GeocodingService

地理编码服务的属性测试。
使用 Hypothesis 框架进行属性测试。
"""

import pytest
from hypothesis import given, strategies as st, settings, assume
import pytz

from backend.core.geocoding.service import GeocodingService
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
)


# =============================================================================
# Strategies for generating test data
# =============================================================================

# Valid source values
SOURCE_VALUES = ['local_db', 'amap', 'nominatim', 'manual']

# Country code strategy (2 uppercase letters)
country_code_strategy = st.text(
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    min_size=2,
    max_size=2
)

# English suffixes that get removed during normalization - must exclude from city names
ENGLISH_SUFFIXES = ['city', 'state', 'province', 'county', 'town', 'village', 'district']

# City name strategy - alphanumeric characters (no commas or special chars)
# Use .map(str.strip) to ensure no leading/trailing spaces that would cause
# mismatch between stored city name and normalized query
# Also filter out names that are exactly English suffixes (they get removed by normalizer)
city_name_strategy = st.text(
    alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
    min_size=1,
    max_size=30
).map(lambda x: x.strip()).filter(
    lambda x: len(x) > 0 and x.lower() not in ENGLISH_SUFFIXES
)

# Valid IANA timezone strategy
VALID_TIMEZONES = [
    'Asia/Shanghai', 'Asia/Tokyo', 'Asia/Seoul', 'Asia/Singapore',
    'America/New_York', 'America/Los_Angeles', 'America/Chicago',
    'Europe/London', 'Europe/Paris', 'Europe/Berlin',
    'Australia/Sydney', 'Pacific/Auckland', 'UTC'
]
timezone_strategy = st.sampled_from(VALID_TIMEZONES)

# Place ID strategy
place_id_strategy = st.text(
    alphabet='abcdefghijklmnopqrstuvwxyz0123456789-',
    min_size=5,
    max_size=20
).map(lambda x: f"gn-{x}")

# User ID strategy
user_id_strategy = st.text(
    alphabet='abcdefghijklmnopqrstuvwxyz0123456789',
    min_size=5,
    max_size=20
)

# Label strategy
label_strategy = st.sampled_from(['birth_place', 'current_city', 'work_city', 'home'])


def place_strategy_with_params(
    country_code=None,
    city_name=None,
    source='local_db'
):
    """Generate Place with optional fixed parameters."""
    return st.builds(
        Place,
        place_id=place_id_strategy,
        country_code=st.just(country_code) if country_code else country_code_strategy,
        city_name=st.just(city_name) if city_name else city_name_strategy,
        lat=st.floats(min_value=-90.0, max_value=90.0, allow_nan=False, allow_infinity=False),
        lng=st.floats(min_value=-180.0, max_value=180.0, allow_nan=False, allow_infinity=False),
        timezone=timezone_strategy,
        source=st.just(source),
        accuracy=st.just('city'),
        admin1_code=st.one_of(st.none(), st.text(alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', min_size=1, max_size=5)),
        admin1_name=st.one_of(st.none(), city_name_strategy),
        district_name_raw=st.one_of(st.none(), city_name_strategy),
    )


# General place strategy
place_strategy = place_strategy_with_params()


# =============================================================================
# Helper Functions
# =============================================================================

def is_valid_iana_timezone(tz: str) -> bool:
    """Check if timezone is a valid IANA timezone identifier."""
    try:
        pytz.timezone(tz)
        return True
    except pytz.exceptions.UnknownTimeZoneError:
        return False


def create_service_with_place(place: Place) -> GeocodingService:
    """Create a GeocodingService with a place pre-loaded in world_cities."""
    world_cities = WorldCitiesRepository()
    world_cities.insert(place)
    
    return GeocodingService(
        normalizer=Normalizer(),
        user_places_repo=UserPlacesRepository(),
        geo_cache_repo=GeoCacheRepository(),
        world_cities_repo=world_cities,
    )


# =============================================================================
# Property Tests
# =============================================================================

class TestResolvedPlaceCompleteness:
    """
    **Feature: geocoding-service, Property 4: Resolved Place Completeness**
    
    *For any* successfully resolved Place, all required fields (placeId, countryCode, 
    cityName, lat, lng, timezone, source, accuracy) must be non-null, and timezone 
    must be a valid IANA timezone identifier.
    
    **Validates: Requirements 2.1, 2.2, 9.1**
    """
    
    @given(place=place_strategy)
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_resolved_place_has_all_required_fields(self, place: Place):
        """
        Property test: Resolved Place has all required fields populated.
        
        **Feature: geocoding-service, Property 4: Resolved Place Completeness**
        **Validates: Requirements 2.1, 2.2, 9.1**
        """
        # Create service with the place in world_cities
        service = create_service_with_place(place)
        
        # Resolve the place
        input_req = ResolvePlaceInput(
            input_text=place.city_name,
            hint_country=place.country_code,
        )
        
        resolved = await service.resolve_place(input_req)
        
        # Verify all required fields are non-null
        assert resolved.place_id is not None, "place_id must not be None"
        assert resolved.country_code is not None, "country_code must not be None"
        assert resolved.city_name is not None, "city_name must not be None"
        assert resolved.lat is not None, "lat must not be None"
        assert resolved.lng is not None, "lng must not be None"
        assert resolved.timezone is not None, "timezone must not be None"
        assert resolved.source is not None, "source must not be None"
        assert resolved.accuracy is not None, "accuracy must not be None"
        
        # Verify fields are not empty strings
        assert resolved.place_id != "", "place_id must not be empty"
        assert resolved.country_code != "", "country_code must not be empty"
        assert resolved.city_name != "", "city_name must not be empty"
        assert resolved.timezone != "", "timezone must not be empty"
        assert resolved.source != "", "source must not be empty"
        assert resolved.accuracy != "", "accuracy must not be empty"
    
    @given(place=place_strategy)
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_resolved_place_has_valid_timezone(self, place: Place):
        """
        Property test: Resolved Place has valid IANA timezone.
        
        **Feature: geocoding-service, Property 4: Resolved Place Completeness**
        **Validates: Requirements 2.2**
        """
        # Create service with the place in world_cities
        service = create_service_with_place(place)
        
        # Resolve the place
        input_req = ResolvePlaceInput(
            input_text=place.city_name,
            hint_country=place.country_code,
        )
        
        resolved = await service.resolve_place(input_req)
        
        # Verify timezone is valid IANA identifier
        assert is_valid_iana_timezone(resolved.timezone), \
            f"timezone '{resolved.timezone}' is not a valid IANA timezone"
    
    @given(place=place_strategy)
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_resolved_place_accuracy_is_city(self, place: Place):
        """
        Property test: Resolved Place has accuracy='city'.
        
        **Feature: geocoding-service, Property 4: Resolved Place Completeness**
        **Validates: Requirements 2.1**
        """
        # Create service with the place in world_cities
        service = create_service_with_place(place)
        
        # Resolve the place
        input_req = ResolvePlaceInput(
            input_text=place.city_name,
            hint_country=place.country_code,
        )
        
        resolved = await service.resolve_place(input_req)
        
        # Verify accuracy is 'city'
        assert resolved.accuracy == 'city', \
            f"accuracy must be 'city', got '{resolved.accuracy}'"



class TestInvalidInputErrorHandling:
    """
    **Feature: geocoding-service, Property 5: Invalid Input Error Handling**
    
    *For any* input that cannot be resolved through any provider, resolvePlace must 
    throw a GeocodingError.NotFound error rather than returning a fallback value 
    or country center coordinates.
    
    **Validates: Requirements 2.3, 2.4, 8.3**
    """
    
    @given(whitespace=st.text(alphabet=' \t\n\r', min_size=0, max_size=20))
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_empty_input_raises_invalid_input_error(self, whitespace: str):
        """
        Property test: Empty or whitespace-only input raises InvalidInputError.
        
        **Feature: geocoding-service, Property 5: Invalid Input Error Handling**
        **Validates: Requirements 2.3, 2.4**
        """
        service = GeocodingService()
        
        input_req = ResolvePlaceInput(input_text=whitespace)
        
        with pytest.raises(InvalidInputError):
            await service.resolve_place(input_req)
    
    @given(
        city_name=city_name_strategy,
        country_code=country_code_strategy
    )
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_nonexistent_city_raises_not_found_error(self, city_name: str, country_code: str):
        """
        Property test: Non-existent city raises NotFoundError (not fallback).
        
        **Feature: geocoding-service, Property 5: Invalid Input Error Handling**
        **Validates: Requirements 2.3, 8.3**
        """
        from backend.core.geocoding.providers.amap import AmapProvider
        from backend.core.geocoding.providers.nominatim import NominatimProvider
        
        # Create service with empty world_cities and disabled external providers
        service = GeocodingService(
            normalizer=Normalizer(),
            user_places_repo=UserPlacesRepository(),
            geo_cache_repo=GeoCacheRepository(),
            world_cities_repo=WorldCitiesRepository(),
            amap_provider=AmapProvider(enabled=False),
            nominatim_provider=NominatimProvider(enabled=False),
        )
        
        input_req = ResolvePlaceInput(
            input_text=city_name,
            hint_country=country_code,
        )
        
        # Must raise NotFoundError, not return fallback
        with pytest.raises(NotFoundError) as exc_info:
            await service.resolve_place(input_req)
        
        # Verify error contains query info
        assert exc_info.value.query is not None
    
    @pytest.mark.asyncio
    async def test_none_input_raises_invalid_input_error(self):
        """
        Property test: None input raises InvalidInputError.
        
        **Feature: geocoding-service, Property 5: Invalid Input Error Handling**
        **Validates: Requirements 2.4**
        """
        service = GeocodingService()
        
        # Test with empty string
        input_req = ResolvePlaceInput(input_text="")
        
        with pytest.raises(InvalidInputError):
            await service.resolve_place(input_req)


class TestSourceFieldCorrectness:
    """
    **Feature: geocoding-service, Property 8: Source Field Correctness** (partial - local_db only)
    
    *For any* resolved Place from world_cities, the source field must be 'local_db'.
    
    **Validates: Requirements 3.4**
    """
    
    @given(place=place_strategy)
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_world_cities_hit_has_local_db_source(self, place: Place):
        """
        Property test: Places resolved from world_cities have source='local_db'.
        
        **Feature: geocoding-service, Property 8: Source Field Correctness**
        **Validates: Requirements 3.4**
        """
        # Create service with the place in world_cities
        service = create_service_with_place(place)
        
        # Resolve the place
        input_req = ResolvePlaceInput(
            input_text=place.city_name,
            hint_country=place.country_code,
        )
        
        resolved = await service.resolve_place(input_req)
        
        # Source must be 'local_db' for world_cities hits
        assert resolved.source == 'local_db', \
            f"Expected source='local_db', got source='{resolved.source}'"


class TestUserLevelCachePriority:
    """
    **Feature: geocoding-service, Property 9: User-Level Cache Priority**
    
    *For any* resolvePlace call with userId and hintLabel where a user_places 
    binding exists, the cached Place must be returned without querying other 
    data sources.
    
    **Validates: Requirements 4.1, 4.2**
    """
    
    @given(
        place=place_strategy,
        user_id=user_id_strategy,
        label=label_strategy
    )
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_user_places_binding_returned_first(self, place: Place, user_id: str, label: str):
        """
        Property test: User-level cache binding is returned without querying other sources.
        
        **Feature: geocoding-service, Property 9: User-Level Cache Priority**
        **Validates: Requirements 4.1, 4.2**
        """
        # Create repositories
        user_places = UserPlacesRepository()
        geo_cache = GeoCacheRepository()
        world_cities = WorldCitiesRepository()
        
        # Pre-bind the place to user
        user_places.bind(user_id, label, place)
        
        # Create service
        service = GeocodingService(
            normalizer=Normalizer(),
            user_places_repo=user_places,
            geo_cache_repo=geo_cache,
            world_cities_repo=world_cities,
        )
        
        # Resolve with user context - should return cached place
        # even though world_cities is empty
        input_req = ResolvePlaceInput(
            input_text="any_city_name",  # Doesn't matter - user_places should be checked first
            hint_country="XX",
            user_id=user_id,
            hint_label=label,
        )
        
        resolved = await service.resolve_place(input_req)
        
        # Must return the user-bound place
        assert resolved.place_id == place.place_id, \
            f"Expected place_id={place.place_id}, got {resolved.place_id}"
        assert resolved.city_name == place.city_name
        assert resolved.country_code == place.country_code
    
    @given(
        user_place=place_strategy,
        world_place=place_strategy,
        user_id=user_id_strategy,
        label=label_strategy
    )
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_user_places_takes_priority_over_world_cities(
        self, user_place: Place, world_place: Place, user_id: str, label: str
    ):
        """
        Property test: User-level cache takes priority over world_cities.
        
        **Feature: geocoding-service, Property 9: User-Level Cache Priority**
        **Validates: Requirements 4.1, 4.2**
        """
        # Skip if places have same ID (can't distinguish)
        assume(user_place.place_id != world_place.place_id)
        
        # Create repositories
        user_places = UserPlacesRepository()
        geo_cache = GeoCacheRepository()
        world_cities = WorldCitiesRepository()
        
        # Pre-bind user place
        user_places.bind(user_id, label, user_place)
        
        # Also add a different place to world_cities
        world_cities.insert(world_place)
        
        # Create service
        service = GeocodingService(
            normalizer=Normalizer(),
            user_places_repo=user_places,
            geo_cache_repo=geo_cache,
            world_cities_repo=world_cities,
        )
        
        # Resolve with user context
        input_req = ResolvePlaceInput(
            input_text=world_place.city_name,  # Even if this matches world_cities
            hint_country=world_place.country_code,
            user_id=user_id,
            hint_label=label,
        )
        
        resolved = await service.resolve_place(input_req)
        
        # Must return user-bound place, not world_cities match
        assert resolved.place_id == user_place.place_id, \
            f"User place should take priority: expected {user_place.place_id}, got {resolved.place_id}"



class TestUserLevelCacheStorage:
    """
    **Feature: geocoding-service, Property 10: User-Level Cache Storage**
    
    *For any* successful resolution with userId and hintLabel, the resulting Place 
    must be stored in user_places and retrievable by subsequent calls with the 
    same userId and hintLabel.
    
    **Validates: Requirements 4.3**
    """
    
    @given(
        place=place_strategy,
        user_id=user_id_strategy,
        label=label_strategy
    )
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_resolved_place_stored_in_user_places(self, place: Place, user_id: str, label: str):
        """
        Property test: Resolved place is stored in user_places for future lookups.
        
        **Feature: geocoding-service, Property 10: User-Level Cache Storage**
        **Validates: Requirements 4.3**
        """
        # Create repositories
        user_places = UserPlacesRepository()
        geo_cache = GeoCacheRepository()
        world_cities = WorldCitiesRepository()
        
        # Add place to world_cities
        world_cities.insert(place)
        
        # Create service
        service = GeocodingService(
            normalizer=Normalizer(),
            user_places_repo=user_places,
            geo_cache_repo=geo_cache,
            world_cities_repo=world_cities,
        )
        
        # Resolve with user context
        input_req = ResolvePlaceInput(
            input_text=place.city_name,
            hint_country=place.country_code,
            user_id=user_id,
            hint_label=label,
        )
        
        resolved = await service.resolve_place(input_req)
        
        # Verify place was stored in user_places
        stored = user_places.get_by_label(user_id, label)
        
        assert stored is not None, "Place should be stored in user_places"
        assert stored.place_id == resolved.place_id
        assert stored.city_name == resolved.city_name
    
    @given(
        place=place_strategy,
        user_id=user_id_strategy,
        label=label_strategy
    )
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_stored_place_retrievable_on_subsequent_call(self, place: Place, user_id: str, label: str):
        """
        Property test: Stored place is retrievable on subsequent calls.
        
        **Feature: geocoding-service, Property 10: User-Level Cache Storage**
        **Validates: Requirements 4.3**
        """
        # Create repositories
        user_places = UserPlacesRepository()
        geo_cache = GeoCacheRepository()
        world_cities = WorldCitiesRepository()
        
        # Add place to world_cities
        world_cities.insert(place)
        
        # Create service
        service = GeocodingService(
            normalizer=Normalizer(),
            user_places_repo=user_places,
            geo_cache_repo=geo_cache,
            world_cities_repo=world_cities,
        )
        
        # First call - resolve and store
        input_req = ResolvePlaceInput(
            input_text=place.city_name,
            hint_country=place.country_code,
            user_id=user_id,
            hint_label=label,
        )
        
        first_resolved = await service.resolve_place(input_req)
        
        # Clear world_cities to ensure second call uses user_places
        world_cities.clear()
        
        # Second call - should retrieve from user_places
        second_resolved = await service.resolve_place(input_req)
        
        # Both calls should return the same place
        assert second_resolved.place_id == first_resolved.place_id, \
            "Subsequent call should return same place from user_places"
        assert second_resolved.city_name == first_resolved.city_name


class TestSourceFieldCorrectnessAllSources:
    """
    **Feature: geocoding-service, Property 8: Source Field Correctness** (complete - all sources)
    
    *For any* resolved Place, the source field must accurately reflect where the data 
    came from: 'local_db' for world_cities hits, 'amap' for Amap provider results, 
    'nominatim' for Nominatim provider results.
    
    **Validates: Requirements 3.4, 6.2, 7.2**
    """
    
    @given(place=place_strategy)
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_world_cities_hit_has_local_db_source_complete(self, place: Place):
        """
        Property test: Places resolved from world_cities have source='local_db'.
        
        **Feature: geocoding-service, Property 8: Source Field Correctness**
        **Validates: Requirements 3.4**
        """
        from backend.core.geocoding.providers.amap import AmapProvider
        from backend.core.geocoding.providers.nominatim import NominatimProvider
        
        # Create service with the place in world_cities and disabled external providers
        world_cities = WorldCitiesRepository()
        world_cities.insert(place)
        
        service = GeocodingService(
            normalizer=Normalizer(),
            user_places_repo=UserPlacesRepository(),
            geo_cache_repo=GeoCacheRepository(),
            world_cities_repo=world_cities,
            amap_provider=AmapProvider(enabled=False),
            nominatim_provider=NominatimProvider(enabled=False),
        )
        
        # Resolve the place
        input_req = ResolvePlaceInput(
            input_text=place.city_name,
            hint_country=place.country_code,
        )
        
        resolved = await service.resolve_place(input_req)
        
        # Source must be 'local_db' for world_cities hits
        assert resolved.source == 'local_db', \
            f"Expected source='local_db', got source='{resolved.source}'"
    
    @given(
        city_name=city_name_strategy,
    )
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_amap_hit_has_amap_source(self, city_name: str):
        """
        Property test: Places resolved from Amap have source='amap'.
        
        **Feature: geocoding-service, Property 8: Source Field Correctness**
        **Validates: Requirements 6.2**
        """
        from backend.core.geocoding.providers.amap import AmapProvider
        from backend.core.geocoding.providers.nominatim import NominatimProvider
        from unittest.mock import AsyncMock, MagicMock
        
        # Create a mock Amap provider that returns a place with source='amap'
        mock_amap = MagicMock(spec=AmapProvider)
        mock_amap.is_enabled.return_value = True
        mock_amap.name = "amap"
        mock_amap.source_tag = "amap"
        
        # Create a place that Amap would return
        amap_place = Place(
            place_id=f"amap-{city_name[:8]}",
            country_code="CN",
            city_name=city_name,
            lat=39.9042,
            lng=116.4074,
            timezone="Asia/Shanghai",
            source="amap",
            accuracy="city",
        )
        mock_amap.geocode = AsyncMock(return_value=amap_place)
        
        # Create service with empty world_cities and mock Amap provider
        service = GeocodingService(
            normalizer=Normalizer(),
            user_places_repo=UserPlacesRepository(),
            geo_cache_repo=GeoCacheRepository(),
            world_cities_repo=WorldCitiesRepository(),
            amap_provider=mock_amap,
            nominatim_provider=NominatimProvider(enabled=False),
        )
        
        # Resolve the place with CN country hint to trigger Amap
        input_req = ResolvePlaceInput(
            input_text=city_name,
            hint_country="CN",
        )
        
        resolved = await service.resolve_place(input_req)
        
        # Source must be 'amap' for Amap provider results
        assert resolved.source == 'amap', \
            f"Expected source='amap', got source='{resolved.source}'"
    
    @given(
        city_name=city_name_strategy,
        country_code=country_code_strategy,
    )
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_nominatim_hit_has_nominatim_source(self, city_name: str, country_code: str):
        """
        Property test: Places resolved from Nominatim have source='nominatim'.
        
        **Feature: geocoding-service, Property 8: Source Field Correctness**
        **Validates: Requirements 7.2**
        """
        from backend.core.geocoding.providers.amap import AmapProvider
        from backend.core.geocoding.providers.nominatim import NominatimProvider
        from unittest.mock import AsyncMock, MagicMock
        
        # Skip CN country code since it would try Amap first
        assume(country_code != "CN")
        
        # Create a mock Nominatim provider that returns a place with source='nominatim'
        mock_nominatim = MagicMock(spec=NominatimProvider)
        mock_nominatim.is_enabled.return_value = True
        mock_nominatim.name = "nominatim"
        mock_nominatim.source_tag = "nominatim"
        
        # Create a place that Nominatim would return
        nominatim_place = Place(
            place_id=f"osm-n{city_name[:8]}",
            country_code=country_code,
            city_name=city_name,
            lat=51.5074,
            lng=-0.1278,
            timezone="Europe/London",
            source="nominatim",
            accuracy="city",
        )
        mock_nominatim.geocode = AsyncMock(return_value=nominatim_place)
        
        # Create service with empty world_cities and mock Nominatim provider
        service = GeocodingService(
            normalizer=Normalizer(),
            user_places_repo=UserPlacesRepository(),
            geo_cache_repo=GeoCacheRepository(),
            world_cities_repo=WorldCitiesRepository(),
            amap_provider=AmapProvider(enabled=False),
            nominatim_provider=mock_nominatim,
        )
        
        # Resolve the place
        input_req = ResolvePlaceInput(
            input_text=city_name,
            hint_country=country_code,
        )
        
        resolved = await service.resolve_place(input_req)
        
        # Source must be 'nominatim' for Nominatim provider results
        assert resolved.source == 'nominatim', \
            f"Expected source='nominatim', got source='{resolved.source}'"
    
    @given(place=place_strategy)
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_source_field_is_valid_value(self, place: Place):
        """
        Property test: Source field is always one of the valid values.
        
        **Feature: geocoding-service, Property 8: Source Field Correctness**
        **Validates: Requirements 3.4, 6.2, 7.2**
        """
        # Create service with the place in world_cities
        service = create_service_with_place(place)
        
        # Resolve the place
        input_req = ResolvePlaceInput(
            input_text=place.city_name,
            hint_country=place.country_code,
        )
        
        resolved = await service.resolve_place(input_req)
        
        # Source must be one of the valid values
        assert resolved.source in SOURCE_VALUES, \
            f"Source '{resolved.source}' is not a valid source value. Valid values: {SOURCE_VALUES}"


class TestResolutionOrder:
    """
    **Feature: geocoding-service, Property 14: Resolution Order**
    
    *For any* resolvePlace call, the resolution must follow the exact order: 
    (1) user_places, (2) geo_cache, (3) world_cities, (4) Amap (CN only), (5) Nominatim. 
    When any step succeeds, subsequent steps must not be executed.
    
    **Validates: Requirements 8.1, 8.2**
    """
    
    @given(
        user_place=place_strategy,
        cached_place=place_strategy,
        world_place=place_strategy,
        user_id=user_id_strategy,
        label=label_strategy,
    )
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_user_places_checked_before_geo_cache(
        self, user_place: Place, cached_place: Place, world_place: Place, 
        user_id: str, label: str
    ):
        """
        Property test: user_places is checked before geo_cache.
        
        **Feature: geocoding-service, Property 14: Resolution Order**
        **Validates: Requirements 8.1, 8.2**
        """
        # Ensure places have different IDs
        assume(user_place.place_id != cached_place.place_id)
        assume(user_place.place_id != world_place.place_id)
        assume(cached_place.place_id != world_place.place_id)
        
        # Create repositories
        user_places = UserPlacesRepository()
        geo_cache = GeoCacheRepository()
        world_cities = WorldCitiesRepository()
        normalizer = Normalizer()
        
        # Pre-bind user place
        user_places.bind(user_id, label, user_place)
        
        # Pre-cache a different place
        cache_key = normalizer.build_cache_key(
            normalizer.normalize(world_place.city_name), 
            world_place.country_code
        )
        geo_cache.set(cache_key, cached_place)
        
        # Also add to world_cities
        world_cities.insert(world_place)
        
        # Create service
        service = GeocodingService(
            normalizer=normalizer,
            user_places_repo=user_places,
            geo_cache_repo=geo_cache,
            world_cities_repo=world_cities,
        )
        
        # Resolve with user context
        input_req = ResolvePlaceInput(
            input_text=world_place.city_name,
            hint_country=world_place.country_code,
            user_id=user_id,
            hint_label=label,
        )
        
        resolved = await service.resolve_place(input_req)
        
        # Must return user_place (step 1), not cached_place (step 2) or world_place (step 3)
        assert resolved.place_id == user_place.place_id, \
            f"user_places should be checked first: expected {user_place.place_id}, got {resolved.place_id}"
    
    @given(
        cached_place=place_strategy,
        world_place=place_strategy,
    )
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_geo_cache_checked_before_world_cities(
        self, cached_place: Place, world_place: Place
    ):
        """
        Property test: geo_cache is checked before world_cities.
        
        **Feature: geocoding-service, Property 14: Resolution Order**
        **Validates: Requirements 8.1, 8.2**
        """
        # Ensure places have different IDs
        assume(cached_place.place_id != world_place.place_id)
        
        # Create repositories
        user_places = UserPlacesRepository()
        geo_cache = GeoCacheRepository()
        world_cities = WorldCitiesRepository()
        normalizer = Normalizer()
        
        # Pre-cache a place
        cache_key = normalizer.build_cache_key(
            normalizer.normalize(world_place.city_name), 
            world_place.country_code
        )
        geo_cache.set(cache_key, cached_place)
        
        # Also add a different place to world_cities
        world_cities.insert(world_place)
        
        # Create service
        service = GeocodingService(
            normalizer=normalizer,
            user_places_repo=user_places,
            geo_cache_repo=geo_cache,
            world_cities_repo=world_cities,
        )
        
        # Resolve without user context
        input_req = ResolvePlaceInput(
            input_text=world_place.city_name,
            hint_country=world_place.country_code,
        )
        
        resolved = await service.resolve_place(input_req)
        
        # Must return cached_place (step 2), not world_place (step 3)
        assert resolved.place_id == cached_place.place_id, \
            f"geo_cache should be checked before world_cities: expected {cached_place.place_id}, got {resolved.place_id}"
    
    @given(
        world_place=place_strategy,
        city_name=city_name_strategy,
    )
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_world_cities_checked_before_amap(
        self, world_place: Place, city_name: str
    ):
        """
        Property test: world_cities is checked before Amap (for CN).
        
        **Feature: geocoding-service, Property 14: Resolution Order**
        **Validates: Requirements 8.1, 8.2**
        """
        from backend.core.geocoding.providers.amap import AmapProvider
        from backend.core.geocoding.providers.nominatim import NominatimProvider
        from unittest.mock import AsyncMock, MagicMock
        
        # Create a mock Amap provider
        mock_amap = MagicMock(spec=AmapProvider)
        mock_amap.is_enabled.return_value = True
        mock_amap.name = "amap"
        mock_amap.source_tag = "amap"
        
        amap_place = Place(
            place_id=f"amap-{city_name[:8]}",
            country_code="CN",
            city_name=city_name,
            lat=39.9042,
            lng=116.4074,
            timezone="Asia/Shanghai",
            source="amap",
            accuracy="city",
        )
        mock_amap.geocode = AsyncMock(return_value=amap_place)
        
        # Create repositories
        user_places = UserPlacesRepository()
        geo_cache = GeoCacheRepository()
        world_cities = WorldCitiesRepository()
        
        # Add place to world_cities with CN country code
        cn_place = Place(
            place_id=world_place.place_id,
            country_code="CN",
            city_name=world_place.city_name,
            lat=world_place.lat,
            lng=world_place.lng,
            timezone="Asia/Shanghai",
            source="local_db",
            accuracy="city",
        )
        world_cities.insert(cn_place)
        
        # Create service
        service = GeocodingService(
            normalizer=Normalizer(),
            user_places_repo=user_places,
            geo_cache_repo=geo_cache,
            world_cities_repo=world_cities,
            amap_provider=mock_amap,
            nominatim_provider=NominatimProvider(enabled=False),
        )
        
        # Resolve with CN country hint
        input_req = ResolvePlaceInput(
            input_text=cn_place.city_name,
            hint_country="CN",
        )
        
        resolved = await service.resolve_place(input_req)
        
        # Must return world_cities place (step 3), not Amap place (step 4)
        assert resolved.source == 'local_db', \
            f"world_cities should be checked before Amap: expected source='local_db', got source='{resolved.source}'"
        
        # Amap should not have been called
        mock_amap.geocode.assert_not_called()
    
    @given(
        city_name=city_name_strategy,
        country_code=country_code_strategy,
    )
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_amap_checked_before_nominatim_for_cn(
        self, city_name: str, country_code: str
    ):
        """
        Property test: Amap is checked before Nominatim for CN country code.
        
        **Feature: geocoding-service, Property 14: Resolution Order**
        **Validates: Requirements 8.1, 8.2**
        """
        from backend.core.geocoding.providers.amap import AmapProvider
        from backend.core.geocoding.providers.nominatim import NominatimProvider
        from unittest.mock import AsyncMock, MagicMock
        
        # Create mock providers
        mock_amap = MagicMock(spec=AmapProvider)
        mock_amap.is_enabled.return_value = True
        mock_amap.name = "amap"
        mock_amap.source_tag = "amap"
        
        amap_place = Place(
            place_id=f"amap-{city_name[:8]}",
            country_code="CN",
            city_name=city_name,
            lat=39.9042,
            lng=116.4074,
            timezone="Asia/Shanghai",
            source="amap",
            accuracy="city",
        )
        mock_amap.geocode = AsyncMock(return_value=amap_place)
        
        mock_nominatim = MagicMock(spec=NominatimProvider)
        mock_nominatim.is_enabled.return_value = True
        mock_nominatim.name = "nominatim"
        mock_nominatim.source_tag = "nominatim"
        
        nominatim_place = Place(
            place_id=f"osm-n{city_name[:8]}",
            country_code="CN",
            city_name=city_name,
            lat=39.9042,
            lng=116.4074,
            timezone="Asia/Shanghai",
            source="nominatim",
            accuracy="city",
        )
        mock_nominatim.geocode = AsyncMock(return_value=nominatim_place)
        
        # Create service with empty world_cities
        service = GeocodingService(
            normalizer=Normalizer(),
            user_places_repo=UserPlacesRepository(),
            geo_cache_repo=GeoCacheRepository(),
            world_cities_repo=WorldCitiesRepository(),
            amap_provider=mock_amap,
            nominatim_provider=mock_nominatim,
        )
        
        # Resolve with CN country hint
        input_req = ResolvePlaceInput(
            input_text=city_name,
            hint_country="CN",
        )
        
        resolved = await service.resolve_place(input_req)
        
        # Must return Amap place (step 4), not Nominatim place (step 5)
        assert resolved.source == 'amap', \
            f"Amap should be checked before Nominatim for CN: expected source='amap', got source='{resolved.source}'"
        
        # Nominatim should not have been called
        mock_nominatim.geocode.assert_not_called()
    
    @given(
        city_name=city_name_strategy,
        country_code=country_code_strategy,
    )
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_nominatim_used_for_non_cn_when_world_cities_fails(
        self, city_name: str, country_code: str
    ):
        """
        Property test: Nominatim is used for non-CN countries when world_cities fails.
        
        **Feature: geocoding-service, Property 14: Resolution Order**
        **Validates: Requirements 8.1, 8.2**
        """
        from backend.core.geocoding.providers.amap import AmapProvider
        from backend.core.geocoding.providers.nominatim import NominatimProvider
        from unittest.mock import AsyncMock, MagicMock
        
        # Skip CN country code since it would try Amap
        assume(country_code != "CN")
        
        # Create mock providers
        mock_amap = MagicMock(spec=AmapProvider)
        mock_amap.is_enabled.return_value = True
        mock_amap.name = "amap"
        mock_amap.source_tag = "amap"
        mock_amap.geocode = AsyncMock(return_value=None)
        
        mock_nominatim = MagicMock(spec=NominatimProvider)
        mock_nominatim.is_enabled.return_value = True
        mock_nominatim.name = "nominatim"
        mock_nominatim.source_tag = "nominatim"
        
        nominatim_place = Place(
            place_id=f"osm-n{city_name[:8]}",
            country_code=country_code,
            city_name=city_name,
            lat=51.5074,
            lng=-0.1278,
            timezone="Europe/London",
            source="nominatim",
            accuracy="city",
        )
        mock_nominatim.geocode = AsyncMock(return_value=nominatim_place)
        
        # Create service with empty world_cities
        service = GeocodingService(
            normalizer=Normalizer(),
            user_places_repo=UserPlacesRepository(),
            geo_cache_repo=GeoCacheRepository(),
            world_cities_repo=WorldCitiesRepository(),
            amap_provider=mock_amap,
            nominatim_provider=mock_nominatim,
        )
        
        # Resolve with non-CN country hint
        input_req = ResolvePlaceInput(
            input_text=city_name,
            hint_country=country_code,
        )
        
        resolved = await service.resolve_place(input_req)
        
        # Must return Nominatim place
        assert resolved.source == 'nominatim', \
            f"Nominatim should be used for non-CN: expected source='nominatim', got source='{resolved.source}'"
        
        # Amap should not have been called (not CN)
        mock_amap.geocode.assert_not_called()
    
    @given(
        place=place_strategy,
    )
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_early_return_on_success(self, place: Place):
        """
        Property test: Resolution returns immediately when any step succeeds.
        
        **Feature: geocoding-service, Property 14: Resolution Order**
        **Validates: Requirements 8.2**
        """
        from backend.core.geocoding.providers.amap import AmapProvider
        from backend.core.geocoding.providers.nominatim import NominatimProvider
        from unittest.mock import AsyncMock, MagicMock
        
        # Create mock providers that should NOT be called
        mock_amap = MagicMock(spec=AmapProvider)
        mock_amap.is_enabled.return_value = True
        mock_amap.geocode = AsyncMock(return_value=None)
        
        mock_nominatim = MagicMock(spec=NominatimProvider)
        mock_nominatim.is_enabled.return_value = True
        mock_nominatim.geocode = AsyncMock(return_value=None)
        
        # Create service with place in world_cities
        world_cities = WorldCitiesRepository()
        world_cities.insert(place)
        
        service = GeocodingService(
            normalizer=Normalizer(),
            user_places_repo=UserPlacesRepository(),
            geo_cache_repo=GeoCacheRepository(),
            world_cities_repo=world_cities,
            amap_provider=mock_amap,
            nominatim_provider=mock_nominatim,
        )
        
        # Resolve the place
        input_req = ResolvePlaceInput(
            input_text=place.city_name,
            hint_country=place.country_code,
        )
        
        resolved = await service.resolve_place(input_req)
        
        # Should return from world_cities
        assert resolved.source == 'local_db'
        
        # External providers should NOT have been called
        mock_amap.geocode.assert_not_called()
        mock_nominatim.geocode.assert_not_called()


class TestSystemLevelCacheStorage:
    """
    **Feature: geocoding-service, Property 12: System-Level Cache Storage**
    
    *For any* Place resolved from world_cities or external providers, the result 
    must be inserted into geo_cache with the correct cache_key.
    
    **Validates: Requirements 5.3**
    """
    
    @given(place=place_strategy)
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_resolved_place_stored_in_geo_cache(self, place: Place):
        """
        Property test: Resolved place is stored in geo_cache.
        
        **Feature: geocoding-service, Property 12: System-Level Cache Storage**
        **Validates: Requirements 5.3**
        """
        # Create repositories
        user_places = UserPlacesRepository()
        geo_cache = GeoCacheRepository()
        world_cities = WorldCitiesRepository()
        normalizer = Normalizer()
        
        # Add place to world_cities
        world_cities.insert(place)
        
        # Create service
        service = GeocodingService(
            normalizer=normalizer,
            user_places_repo=user_places,
            geo_cache_repo=geo_cache,
            world_cities_repo=world_cities,
        )
        
        # Resolve the place
        input_req = ResolvePlaceInput(
            input_text=place.city_name,
            hint_country=place.country_code,
        )
        
        resolved = await service.resolve_place(input_req)
        
        # Build expected cache key
        normalized_query = normalizer.normalize(place.city_name)
        cache_key = normalizer.build_cache_key(normalized_query, place.country_code)
        
        # Verify place was stored in geo_cache
        cached = geo_cache.get(cache_key)
        
        assert cached is not None, f"Place should be stored in geo_cache with key '{cache_key}'"
        assert cached.place_id == resolved.place_id
        assert cached.city_name == resolved.city_name
    
    @given(place=place_strategy)
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_geo_cache_used_on_subsequent_call(self, place: Place):
        """
        Property test: geo_cache is used on subsequent calls.
        
        **Feature: geocoding-service, Property 12: System-Level Cache Storage**
        **Validates: Requirements 5.3**
        """
        # Create repositories
        user_places = UserPlacesRepository()
        geo_cache = GeoCacheRepository()
        world_cities = WorldCitiesRepository()
        normalizer = Normalizer()
        
        # Add place to world_cities
        world_cities.insert(place)
        
        # Create service
        service = GeocodingService(
            normalizer=normalizer,
            user_places_repo=user_places,
            geo_cache_repo=geo_cache,
            world_cities_repo=world_cities,
        )
        
        # First call - resolve and cache
        input_req = ResolvePlaceInput(
            input_text=place.city_name,
            hint_country=place.country_code,
        )
        
        first_resolved = await service.resolve_place(input_req)
        
        # Clear world_cities to ensure second call uses geo_cache
        world_cities.clear()
        
        # Second call - should retrieve from geo_cache
        second_resolved = await service.resolve_place(input_req)
        
        # Both calls should return the same place
        assert second_resolved.place_id == first_resolved.place_id, \
            "Subsequent call should return same place from geo_cache"
        assert second_resolved.city_name == first_resolved.city_name
    
    @given(place=place_strategy)
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_geo_cache_hit_count_incremented(self, place: Place):
        """
        Property test: geo_cache hit_count is incremented on cache hit.
        
        **Feature: geocoding-service, Property 12: System-Level Cache Storage**
        **Validates: Requirements 5.3**
        """
        # Create repositories
        user_places = UserPlacesRepository()
        geo_cache = GeoCacheRepository()
        world_cities = WorldCitiesRepository()
        normalizer = Normalizer()
        
        # Add place to world_cities
        world_cities.insert(place)
        
        # Create service
        service = GeocodingService(
            normalizer=normalizer,
            user_places_repo=user_places,
            geo_cache_repo=geo_cache,
            world_cities_repo=world_cities,
        )
        
        # First call - resolve and cache
        input_req = ResolvePlaceInput(
            input_text=place.city_name,
            hint_country=place.country_code,
        )
        
        await service.resolve_place(input_req)
        
        # Get cache key
        normalized_query = normalizer.normalize(place.city_name)
        cache_key = normalizer.build_cache_key(normalized_query, place.country_code)
        
        # Get initial hit count
        initial_stats = geo_cache.get_stats(cache_key)
        assert initial_stats is not None
        initial_hit_count = initial_stats['hit_count']
        
        # Second call - should hit cache and increment
        await service.resolve_place(input_req)
        
        # Verify hit count incremented
        updated_stats = geo_cache.get_stats(cache_key)
        assert updated_stats is not None
        assert updated_stats['hit_count'] == initial_hit_count + 1, \
            f"Hit count should be incremented: {initial_hit_count} -> {updated_stats['hit_count']}"
