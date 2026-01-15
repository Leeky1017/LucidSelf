"""
Property-Based Tests for Geocoding Repositories

地理编码数据访问层的属性测试。
使用 Hypothesis 框架进行属性测试。
"""

import pytest
from hypothesis import given, strategies as st, settings, assume
from datetime import datetime
import time

from backend.core.geocoding.models import Place
from backend.core.geocoding.repository import (
    WorldCitiesRepository,
    GeoCacheRepository,
    UserPlacesRepository,
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

# City name strategy - alphanumeric characters
city_name_strategy = st.text(
    alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ',
    min_size=1,
    max_size=30
).filter(lambda x: x.strip())

# Admin1 code strategy
admin1_code_strategy = st.one_of(
    st.none(),
    st.text(
        alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',
        min_size=1,
        max_size=5
    )
)

# Timezone strategy
timezone_strategy = st.sampled_from([
    'Asia/Shanghai', 'Asia/Tokyo', 'Asia/Seoul', 'Asia/Singapore',
    'America/New_York', 'America/Los_Angeles', 'America/Chicago',
    'Europe/London', 'Europe/Paris', 'Europe/Berlin',
    'Australia/Sydney', 'Pacific/Auckland', 'UTC', 'GMT'
])

# Place ID strategy
place_id_strategy = st.text(
    alphabet='abcdefghijklmnopqrstuvwxyz0123456789-',
    min_size=5,
    max_size=20
).map(lambda x: f"gn-{x}")

# Strategy for generating valid Place objects
def place_strategy_with_params(
    country_code=None,
    city_name=None,
    admin1_code=None
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
        source=st.sampled_from(SOURCE_VALUES),
        accuracy=st.just('city'),
        admin1_code=st.just(admin1_code) if admin1_code is not None else admin1_code_strategy,
        admin1_name=st.one_of(st.none(), city_name_strategy),
        district_name_raw=st.one_of(st.none(), city_name_strategy),
    )

# General place strategy
place_strategy = place_strategy_with_params()


# =============================================================================
# Property Tests for WorldCitiesRepository
# =============================================================================

class TestWorldCitiesQueryMatching:
    """
    **Feature: geocoding-service, Property 7: world_cities Query Matching**
    
    *For any* query with (country_code, city_name), if a matching record exists 
    in world_cities, it must be returned. If admin1_code is also provided, 
    the match must include that constraint.
    
    **Validates: Requirements 3.3**
    """
    
    @given(place=place_strategy)
    @settings(max_examples=100)
    def test_inserted_place_is_findable(self, place: Place):
        """
        Property test: Any inserted place can be found by country_code and city_name.
        
        **Feature: geocoding-service, Property 7: world_cities Query Matching**
        **Validates: Requirements 3.3**
        """
        repo = WorldCitiesRepository()
        
        # Insert the place
        repo.insert(place)
        
        # Find by country_code and city_name
        found = repo.find_by_country_city(place.country_code, place.city_name)
        
        # Must be found
        assert found is not None, \
            f"Place not found: country={place.country_code}, city={place.city_name}"
        
        # Verify key fields match
        assert found.country_code.upper() == place.country_code.upper()
        assert found.city_name.lower() == place.city_name.lower()
        assert found.lat == place.lat
        assert found.lng == place.lng
        assert found.timezone == place.timezone
    
    @given(place=place_strategy)
    @settings(max_examples=100)
    def test_admin1_code_refinement(self, place: Place):
        """
        Property test: When admin1_code is provided, match must include that constraint.
        
        **Feature: geocoding-service, Property 7: world_cities Query Matching**
        **Validates: Requirements 3.3**
        """
        # Skip if place has no admin1_code
        assume(place.admin1_code is not None)
        
        repo = WorldCitiesRepository()
        
        # Insert the place
        repo.insert(place)
        
        # Find with admin1_code constraint
        found = repo.find_by_country_city(
            place.country_code, 
            place.city_name, 
            admin1_code=place.admin1_code
        )
        
        # Must be found
        assert found is not None, \
            f"Place not found with admin1: country={place.country_code}, city={place.city_name}, admin1={place.admin1_code}"
        
        # admin1_code must match
        assert found.admin1_code == place.admin1_code
    
    @given(place=place_strategy)
    @settings(max_examples=100)
    def test_wrong_admin1_code_not_found(self, place: Place):
        """
        Property test: Wrong admin1_code should not match.
        
        **Feature: geocoding-service, Property 7: world_cities Query Matching**
        **Validates: Requirements 3.3**
        """
        # Skip if place has no admin1_code
        assume(place.admin1_code is not None)
        
        repo = WorldCitiesRepository()
        
        # Insert the place
        repo.insert(place)
        
        # Try to find with wrong admin1_code
        wrong_admin1 = place.admin1_code + "X"
        found = repo.find_by_country_city(
            place.country_code, 
            place.city_name, 
            admin1_code=wrong_admin1
        )
        
        # Should NOT be found
        assert found is None, \
            f"Place found with wrong admin1: expected None, got {found}"
    
    @given(
        place=place_strategy,
        wrong_country=country_code_strategy
    )
    @settings(max_examples=100)
    def test_wrong_country_not_found(self, place: Place, wrong_country: str):
        """
        Property test: Wrong country_code should not match.
        
        **Feature: geocoding-service, Property 7: world_cities Query Matching**
        **Validates: Requirements 3.3**
        """
        # Skip if wrong_country happens to match
        assume(wrong_country.upper() != place.country_code.upper())
        
        repo = WorldCitiesRepository()
        
        # Insert the place
        repo.insert(place)
        
        # Try to find with wrong country
        found = repo.find_by_country_city(wrong_country, place.city_name)
        
        # Should NOT be found
        assert found is None, \
            f"Place found with wrong country: expected None, got {found}"
    
    @given(place=place_strategy)
    @settings(max_examples=100)
    def test_source_field_is_local_db(self, place: Place):
        """
        Property test: Places found in world_cities have source='local_db'.
        
        **Feature: geocoding-service, Property 8: Source Field Correctness** (partial)
        **Validates: Requirements 3.4**
        """
        repo = WorldCitiesRepository()
        
        # Insert the place (may have any source)
        repo.insert(place)
        
        # Find the place
        found = repo.find_by_country_city(place.country_code, place.city_name)
        
        # Source must be 'local_db' for world_cities hits
        assert found is not None
        assert found.source == 'local_db', \
            f"Expected source='local_db', got source='{found.source}'"


# =============================================================================
# Property Tests for GeoCacheRepository
# =============================================================================

class TestSystemLevelCacheHitBehavior:
    """
    **Feature: geocoding-service, Property 11: System-Level Cache Hit Behavior**
    
    *For any* geo_cache hit, the returned Place must match the cached value, 
    and the hit_count must be incremented and last_used_at updated.
    
    **Validates: Requirements 5.2**
    """
    
    @given(
        place=place_strategy,
        cache_key=st.text(
            alphabet='abcdefghijklmnopqrstuvwxyz|',
            min_size=3,
            max_size=50
        ).filter(lambda x: '|' in x)
    )
    @settings(max_examples=100)
    def test_cached_place_is_retrievable(self, place: Place, cache_key: str):
        """
        Property test: Any cached place can be retrieved by cache_key.
        
        **Feature: geocoding-service, Property 11: System-Level Cache Hit Behavior**
        **Validates: Requirements 5.2**
        """
        repo = GeoCacheRepository()
        
        # Store in cache
        repo.set(cache_key, place)
        
        # Retrieve from cache
        found = repo.get(cache_key)
        
        # Must be found
        assert found is not None, f"Cached place not found: key={cache_key}"
        
        # Verify all fields match
        assert found.place_id == place.place_id
        assert found.country_code == place.country_code
        assert found.city_name == place.city_name
        assert found.lat == place.lat
        assert found.lng == place.lng
        assert found.timezone == place.timezone
        assert found.source == place.source
    
    @given(
        place=place_strategy,
        cache_key=st.text(
            alphabet='abcdefghijklmnopqrstuvwxyz|',
            min_size=3,
            max_size=50
        ).filter(lambda x: '|' in x)
    )
    @settings(max_examples=100)
    def test_hit_count_increments(self, place: Place, cache_key: str):
        """
        Property test: update_hit() increments hit_count.
        
        **Feature: geocoding-service, Property 11: System-Level Cache Hit Behavior**
        **Validates: Requirements 5.2**
        """
        repo = GeoCacheRepository()
        
        # Store in cache
        repo.set(cache_key, place)
        
        # Get initial stats
        initial_stats = repo.get_stats(cache_key)
        assert initial_stats is not None
        initial_hit_count = initial_stats['hit_count']
        
        # Update hit
        repo.update_hit(cache_key)
        
        # Get updated stats
        updated_stats = repo.get_stats(cache_key)
        assert updated_stats is not None
        
        # Hit count must be incremented
        assert updated_stats['hit_count'] == initial_hit_count + 1, \
            f"Hit count not incremented: {initial_hit_count} -> {updated_stats['hit_count']}"
    
    @given(
        place=place_strategy,
        cache_key=st.text(
            alphabet='abcdefghijklmnopqrstuvwxyz|',
            min_size=3,
            max_size=50
        ).filter(lambda x: '|' in x)
    )
    @settings(max_examples=100)
    def test_last_used_at_updates(self, place: Place, cache_key: str):
        """
        Property test: update_hit() updates last_used_at.
        
        **Feature: geocoding-service, Property 11: System-Level Cache Hit Behavior**
        **Validates: Requirements 5.2**
        """
        repo = GeoCacheRepository()
        
        # Store in cache
        repo.set(cache_key, place)
        
        # Get initial stats
        initial_stats = repo.get_stats(cache_key)
        assert initial_stats is not None
        initial_last_used = initial_stats['last_used_at']
        
        # Small delay to ensure time difference
        time.sleep(0.01)
        
        # Update hit
        repo.update_hit(cache_key)
        
        # Get updated stats
        updated_stats = repo.get_stats(cache_key)
        assert updated_stats is not None
        
        # last_used_at must be updated (should be >= initial)
        assert updated_stats['last_used_at'] >= initial_last_used, \
            f"last_used_at not updated: {initial_last_used} -> {updated_stats['last_used_at']}"
    
    @given(
        cache_key=st.text(
            alphabet='abcdefghijklmnopqrstuvwxyz|',
            min_size=3,
            max_size=50
        ).filter(lambda x: '|' in x)
    )
    @settings(max_examples=100)
    def test_nonexistent_key_returns_none(self, cache_key: str):
        """
        Property test: Non-existent cache key returns None.
        
        **Feature: geocoding-service, Property 11: System-Level Cache Hit Behavior**
        **Validates: Requirements 5.2**
        """
        repo = GeoCacheRepository()
        
        # Try to get non-existent key
        found = repo.get(cache_key)
        
        # Must be None
        assert found is None, f"Expected None for non-existent key, got {found}"


# =============================================================================
# Unit Tests for UserPlacesRepository
# =============================================================================

class TestUserPlacesRepository:
    """Unit tests for UserPlacesRepository."""
    
    @given(
        place=place_strategy,
        user_id=st.text(alphabet='abcdefghijklmnopqrstuvwxyz0123456789', min_size=5, max_size=20),
        label=st.sampled_from(['birth_place', 'current_city', 'work_city', 'home'])
    )
    @settings(max_examples=100)
    def test_bind_and_retrieve(self, place: Place, user_id: str, label: str):
        """Test binding and retrieving a place."""
        repo = UserPlacesRepository()
        
        # Bind place to user
        repo.bind(user_id, label, place)
        
        # Retrieve by label
        found = repo.get_by_label(user_id, label)
        
        # Must be found
        assert found is not None
        assert found.place_id == place.place_id
        assert found.city_name == place.city_name
    
    @given(
        user_id=st.text(alphabet='abcdefghijklmnopqrstuvwxyz0123456789', min_size=5, max_size=20),
        label=st.sampled_from(['birth_place', 'current_city'])
    )
    @settings(max_examples=100)
    def test_nonexistent_binding_returns_none(self, user_id: str, label: str):
        """Test that non-existent binding returns None."""
        repo = UserPlacesRepository()
        
        # Try to get non-existent binding
        found = repo.get_by_label(user_id, label)
        
        # Must be None
        assert found is None
