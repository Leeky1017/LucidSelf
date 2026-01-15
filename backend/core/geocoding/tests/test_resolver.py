"""
Property-Based Tests for LocationResolver

LocationResolver 的属性测试。
使用 Hypothesis 框架进行属性测试。
"""

import pytest
from hypothesis import given, strategies as st, settings, assume
from unittest.mock import AsyncMock, MagicMock, patch

from backend.core.geocoding.resolver import LocationResolver
from backend.core.geocoding.service import GeocodingService
from backend.core.geocoding.models import Place, ResolvePlaceInput
from backend.core.geocoding.exceptions import InvalidInputError


# =============================================================================
# Strategies for generating test data
# =============================================================================

# Valid IANA timezone strategy
VALID_TIMEZONES = [
    'Asia/Shanghai', 'Asia/Tokyo', 'Asia/Seoul', 'Asia/Singapore',
    'America/New_York', 'America/Los_Angeles', 'America/Chicago',
    'Europe/London', 'Europe/Paris', 'Europe/Berlin',
    'Australia/Sydney', 'Pacific/Auckland', 'UTC'
]
timezone_strategy = st.sampled_from(VALID_TIMEZONES)

# Longitude strategy: -180 to 180
longitude_strategy = st.floats(
    min_value=-180.0, 
    max_value=180.0, 
    allow_nan=False, 
    allow_infinity=False
)

# Latitude strategy: -90 to 90
latitude_strategy = st.floats(
    min_value=-90.0, 
    max_value=90.0, 
    allow_nan=False, 
    allow_infinity=False
)

# Location tuple strategy (longitude, latitude)
location_strategy = st.tuples(longitude_strategy, latitude_strategy)

# City name strategy - non-empty alphanumeric strings
city_name_strategy = st.text(
    alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
    min_size=2,
    max_size=30
).filter(lambda x: len(x.strip()) > 0)

# Country code strategy (2 uppercase letters)
country_code_strategy = st.text(
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    min_size=2,
    max_size=2
)

# Place ID strategy
place_id_strategy = st.text(
    alphabet='abcdefghijklmnopqrstuvwxyz0123456789-',
    min_size=5,
    max_size=20
).map(lambda x: f"gn-{x}")


def create_mock_place(city_name: str, lng: float, lat: float, timezone: str) -> Place:
    """Create a mock Place object for testing."""
    return Place(
        place_id=f"gn-test-{city_name[:8]}",
        country_code="CN",
        city_name=city_name,
        lat=lat,
        lng=lng,
        timezone=timezone,
        source="local_db",
        accuracy="city",
    )


# =============================================================================
# Property 1: Geocoding Resolution Priority
# =============================================================================

class TestGeocodingResolutionPriority:
    """
    **Feature: calculator-integration, Property 1: Geocoding Resolution Priority**
    
    *For any* Calculator input with both birth_place and birth_location provided, 
    the Calculator must use birth_location and ignore birth_place.
    
    **Validates: Requirements 1.2, 2.2, 4.2**
    """
    
    @given(
        birth_place=city_name_strategy,
        birth_location=location_strategy,
        timezone=timezone_strategy,
    )
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_birth_location_takes_priority_over_birth_place(
        self, birth_place: str, birth_location: tuple, timezone: str
    ):
        """
        Property test: When both birth_place and birth_location are provided,
        birth_location is used and birth_place is ignored.
        
        **Feature: calculator-integration, Property 1: Geocoding Resolution Priority**
        **Validates: Requirements 1.2, 2.2, 4.2**
        """
        # Create a mock GeocodingService that should NOT be called
        mock_service = MagicMock(spec=GeocodingService)
        mock_service.resolve_place = AsyncMock()
        
        resolver = LocationResolver(geocoding_service=mock_service)
        
        # Resolve with both birth_place and birth_location
        result_location, result_timezone = await resolver.resolve(
            birth_place=birth_place,
            birth_location=birth_location,
            timezone=timezone
        )
        
        # birth_location should be used directly
        assert result_location == birth_location, \
            f"Expected birth_location {birth_location}, got {result_location}"
        
        # Provided timezone should be used
        assert result_timezone == timezone, \
            f"Expected timezone {timezone}, got {result_timezone}"
        
        # GeocodingService should NOT be called when birth_location is provided
        mock_service.resolve_place.assert_not_called()
    
    @given(
        birth_place=city_name_strategy,
        birth_location=location_strategy,
    )
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_birth_location_priority_without_explicit_timezone(
        self, birth_place: str, birth_location: tuple
    ):
        """
        Property test: When birth_location is provided without timezone,
        default timezone is used and GeocodingService is not called.
        
        **Feature: calculator-integration, Property 1: Geocoding Resolution Priority**
        **Validates: Requirements 1.2, 2.2, 4.2**
        """
        mock_service = MagicMock(spec=GeocodingService)
        mock_service.resolve_place = AsyncMock()
        
        resolver = LocationResolver(geocoding_service=mock_service)
        
        # Resolve with birth_location but no timezone
        result_location, result_timezone = await resolver.resolve(
            birth_place=birth_place,
            birth_location=birth_location,
            timezone=None
        )
        
        # birth_location should be used
        assert result_location == birth_location
        
        # Default timezone should be used
        assert result_timezone == "Asia/Shanghai"
        
        # GeocodingService should NOT be called
        mock_service.resolve_place.assert_not_called()
    
    @given(
        birth_location=location_strategy,
        timezone=timezone_strategy,
    )
    @settings(max_examples=100)
    def test_sync_birth_location_takes_priority(
        self, birth_location: tuple, timezone: str
    ):
        """
        Property test: Sync version also prioritizes birth_location over birth_place.
        
        **Feature: calculator-integration, Property 1: Geocoding Resolution Priority**
        **Validates: Requirements 1.2, 2.2, 4.2**
        """
        mock_service = MagicMock(spec=GeocodingService)
        
        resolver = LocationResolver(geocoding_service=mock_service)
        
        # Resolve synchronously with birth_location
        result_location, result_timezone = resolver.resolve_sync(
            birth_place="北京",  # Should be ignored
            birth_location=birth_location,
            timezone=timezone
        )
        
        # birth_location should be used
        assert result_location == birth_location
        assert result_timezone == timezone


# =============================================================================
# Property 2: Geocoding Fallback Timezone
# =============================================================================

class TestGeocodingFallbackTimezone:
    """
    **Feature: calculator-integration, Property 2: Geocoding Fallback Timezone**
    
    *For any* Calculator input with birth_place but no explicit timezone, 
    the resolved Place.timezone must be used for calculation.
    
    **Validates: Requirements 1.4, 2.4, 4.3**
    """
    
    @given(
        city_name=city_name_strategy,
        place_timezone=timezone_strategy,
        place_lng=longitude_strategy,
        place_lat=latitude_strategy,
    )
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_place_timezone_used_when_no_explicit_timezone(
        self, city_name: str, place_timezone: str, place_lng: float, place_lat: float
    ):
        """
        Property test: When birth_place is resolved and no timezone is provided,
        the Place.timezone from GeocodingService is used.
        
        **Feature: calculator-integration, Property 2: Geocoding Fallback Timezone**
        **Validates: Requirements 1.4, 2.4, 4.3**
        """
        # Create a mock Place with specific timezone
        mock_place = create_mock_place(city_name, place_lng, place_lat, place_timezone)
        
        # Create mock GeocodingService
        mock_service = MagicMock(spec=GeocodingService)
        mock_service.resolve_place = AsyncMock(return_value=mock_place)
        
        resolver = LocationResolver(geocoding_service=mock_service)
        
        # Resolve with birth_place only (no timezone)
        result_location, result_timezone = await resolver.resolve(
            birth_place=city_name,
            birth_location=None,
            timezone=None
        )
        
        # Place.timezone should be used
        assert result_timezone == place_timezone, \
            f"Expected Place.timezone {place_timezone}, got {result_timezone}"
        
        # Location should match Place coordinates
        assert result_location == (mock_place.lng, mock_place.lat)
    
    @given(
        city_name=city_name_strategy,
        place_timezone=timezone_strategy,
        explicit_timezone=timezone_strategy,
        place_lng=longitude_strategy,
        place_lat=latitude_strategy,
    )
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_explicit_timezone_overrides_place_timezone(
        self, city_name: str, place_timezone: str, explicit_timezone: str,
        place_lng: float, place_lat: float
    ):
        """
        Property test: When explicit timezone is provided, it overrides Place.timezone.
        
        **Feature: calculator-integration, Property 2: Geocoding Fallback Timezone**
        **Validates: Requirements 1.4, 2.4, 4.3**
        """
        # Skip if timezones are the same (can't distinguish override)
        assume(place_timezone != explicit_timezone)
        
        # Create a mock Place with different timezone
        mock_place = create_mock_place(city_name, place_lng, place_lat, place_timezone)
        
        # Create mock GeocodingService
        mock_service = MagicMock(spec=GeocodingService)
        mock_service.resolve_place = AsyncMock(return_value=mock_place)
        
        resolver = LocationResolver(geocoding_service=mock_service)
        
        # Resolve with birth_place and explicit timezone
        result_location, result_timezone = await resolver.resolve(
            birth_place=city_name,
            birth_location=None,
            timezone=explicit_timezone
        )
        
        # Explicit timezone should override Place.timezone
        assert result_timezone == explicit_timezone, \
            f"Expected explicit timezone {explicit_timezone}, got {result_timezone}"
    
    @given(
        city_name=city_name_strategy,
        place_timezone=timezone_strategy,
        place_lng=longitude_strategy,
        place_lat=latitude_strategy,
    )
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_geocoding_service_called_for_birth_place_only(
        self, city_name: str, place_timezone: str, place_lng: float, place_lat: float
    ):
        """
        Property test: GeocodingService is called when only birth_place is provided.
        
        **Feature: calculator-integration, Property 2: Geocoding Fallback Timezone**
        **Validates: Requirements 1.4, 2.4, 4.3**
        """
        mock_place = create_mock_place(city_name, place_lng, place_lat, place_timezone)
        
        mock_service = MagicMock(spec=GeocodingService)
        mock_service.resolve_place = AsyncMock(return_value=mock_place)
        
        resolver = LocationResolver(geocoding_service=mock_service)
        
        # Resolve with birth_place only
        await resolver.resolve(
            birth_place=city_name,
            birth_location=None,
            timezone=None
        )
        
        # GeocodingService should be called
        mock_service.resolve_place.assert_called_once()
        
        # Verify the input text matches
        call_args = mock_service.resolve_place.call_args
        assert call_args[0][0].input_text == city_name


# =============================================================================
# Property 3: Location Validation
# =============================================================================

class TestLocationValidation:
    """
    **Feature: calculator-integration, Property 3: Location Validation**
    
    *For any* location-dependent Calculator input with neither birth_place 
    nor birth_location, the Calculator must throw InvalidInputError.
    
    **Validates: Requirements 1.5, 2.5, 4.5**
    """
    
    @pytest.mark.asyncio
    async def test_neither_birth_place_nor_birth_location_raises_error(self):
        """
        Property test: When neither birth_place nor birth_location is provided,
        InvalidInputError is raised.
        
        **Feature: calculator-integration, Property 3: Location Validation**
        **Validates: Requirements 1.5, 2.5, 4.5**
        """
        resolver = LocationResolver()
        
        with pytest.raises(InvalidInputError) as exc_info:
            await resolver.resolve(
                birth_place=None,
                birth_location=None,
                timezone=None
            )
        
        # Verify error message mentions the requirement
        assert "birth_place" in str(exc_info.value) or "birth_location" in str(exc_info.value)
    
    @given(timezone=timezone_strategy)
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_only_timezone_provided_raises_error(self, timezone: str):
        """
        Property test: When only timezone is provided (no location info),
        InvalidInputError is raised.
        
        **Feature: calculator-integration, Property 3: Location Validation**
        **Validates: Requirements 1.5, 2.5, 4.5**
        """
        resolver = LocationResolver()
        
        with pytest.raises(InvalidInputError):
            await resolver.resolve(
                birth_place=None,
                birth_location=None,
                timezone=timezone
            )
    
    @given(whitespace=st.text(alphabet=' \t\n\r', min_size=0, max_size=10))
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_empty_or_whitespace_birth_place_raises_error(self, whitespace: str):
        """
        Property test: When birth_place is empty or whitespace-only,
        InvalidInputError is raised.
        
        **Feature: calculator-integration, Property 3: Location Validation**
        **Validates: Requirements 1.5, 2.5, 4.5**
        """
        resolver = LocationResolver()
        
        with pytest.raises(InvalidInputError):
            await resolver.resolve(
                birth_place=whitespace,
                birth_location=None,
                timezone=None
            )
    
    def test_sync_neither_location_raises_error(self):
        """
        Property test: Sync version also raises InvalidInputError when no location provided.
        
        **Feature: calculator-integration, Property 3: Location Validation**
        **Validates: Requirements 1.5, 2.5, 4.5**
        """
        resolver = LocationResolver()
        
        with pytest.raises(InvalidInputError):
            resolver.resolve_sync(
                birth_place=None,
                birth_location=None,
                timezone=None
            )
    
    @given(
        birth_location=location_strategy,
    )
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_valid_birth_location_does_not_raise_error(self, birth_location: tuple):
        """
        Property test: When valid birth_location is provided, no error is raised.
        
        **Feature: calculator-integration, Property 3: Location Validation**
        **Validates: Requirements 1.5, 2.5, 4.5**
        """
        resolver = LocationResolver()
        
        # Should not raise
        result_location, result_timezone = await resolver.resolve(
            birth_place=None,
            birth_location=birth_location,
            timezone=None
        )
        
        assert result_location == birth_location
    
    @given(
        city_name=city_name_strategy,
        place_timezone=timezone_strategy,
        place_lng=longitude_strategy,
        place_lat=latitude_strategy,
    )
    @settings(max_examples=100)
    @pytest.mark.asyncio
    async def test_valid_birth_place_does_not_raise_error(
        self, city_name: str, place_timezone: str, place_lng: float, place_lat: float
    ):
        """
        Property test: When valid birth_place is provided, no error is raised.
        
        **Feature: calculator-integration, Property 3: Location Validation**
        **Validates: Requirements 1.5, 2.5, 4.5**
        """
        mock_place = create_mock_place(city_name, place_lng, place_lat, place_timezone)
        
        mock_service = MagicMock(spec=GeocodingService)
        mock_service.resolve_place = AsyncMock(return_value=mock_place)
        
        resolver = LocationResolver(geocoding_service=mock_service)
        
        # Should not raise
        result_location, result_timezone = await resolver.resolve(
            birth_place=city_name,
            birth_location=None,
            timezone=None
        )
        
        assert result_location == (mock_place.lng, mock_place.lat)
