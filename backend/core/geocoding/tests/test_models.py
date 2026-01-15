"""
Property-Based Tests for Geocoding Models

地理编码数据模型的属性测试。
使用 Hypothesis 框架进行属性测试。
"""

import pytest
from hypothesis import given, strategies as st, settings

from backend.core.geocoding.models import Place


# =============================================================================
# Strategies for generating test data
# =============================================================================

# Valid source values
SOURCE_VALUES = ['local_db', 'amap', 'nominatim', 'manual']

# Valid accuracy values (currently only 'city')
ACCURACY_VALUES = ['city']

# Non-empty text strategy (more efficient than filtering)
non_empty_text = st.text(
    alphabet=st.characters(blacklist_categories=('Cs',), blacklist_characters='\x00'),
    min_size=1,
    max_size=50
).map(lambda x: x if x.strip() else 'default')

# Country code strategy (2 uppercase letters)
country_code_strategy = st.text(
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    min_size=2,
    max_size=2
)

# Timezone strategy - use realistic IANA timezone patterns
timezone_strategy = st.sampled_from([
    'Asia/Shanghai', 'Asia/Tokyo', 'Asia/Seoul', 'Asia/Singapore',
    'America/New_York', 'America/Los_Angeles', 'America/Chicago',
    'Europe/London', 'Europe/Paris', 'Europe/Berlin',
    'Australia/Sydney', 'Pacific/Auckland', 'UTC', 'GMT'
])

# Optional text strategy
optional_text = st.one_of(
    st.none(),
    st.text(
        alphabet=st.characters(blacklist_categories=('Cs',), blacklist_characters='\x00'),
        min_size=1,
        max_size=50
    )
)

# Strategy for generating valid Place objects
place_strategy = st.builds(
    Place,
    place_id=non_empty_text,
    country_code=country_code_strategy,
    city_name=non_empty_text,
    lat=st.floats(min_value=-90.0, max_value=90.0, allow_nan=False, allow_infinity=False),
    lng=st.floats(min_value=-180.0, max_value=180.0, allow_nan=False, allow_infinity=False),
    timezone=timezone_strategy,
    source=st.sampled_from(SOURCE_VALUES),
    accuracy=st.sampled_from(ACCURACY_VALUES),
    admin1_code=optional_text,
    admin1_name=optional_text,
    district_name_raw=optional_text,
)


# =============================================================================
# Property Tests
# =============================================================================

class TestPlaceSerializationRoundTrip:
    """
    **Feature: geocoding-service, Property 15: Place Serialization Round-Trip**
    
    *For any* valid Place object, serializing to JSON and deserializing back 
    must produce an equivalent Place object.
    
    **Validates: Requirements 9.3**
    """
    
    @given(place=place_strategy)
    @settings(max_examples=100)
    def test_place_json_round_trip(self, place: Place):
        """
        Property test: Place -> JSON -> Place produces equivalent object.
        
        **Feature: geocoding-service, Property 15: Place Serialization Round-Trip**
        **Validates: Requirements 9.3**
        """
        # Serialize to JSON
        json_str = place.to_json()
        
        # Deserialize back to Place
        restored = Place.from_json(json_str)
        
        # Verify all fields are equal
        assert restored.place_id == place.place_id
        assert restored.country_code == place.country_code
        assert restored.city_name == place.city_name
        assert restored.lat == place.lat
        assert restored.lng == place.lng
        assert restored.timezone == place.timezone
        assert restored.source == place.source
        assert restored.accuracy == place.accuracy
        assert restored.admin1_code == place.admin1_code
        assert restored.admin1_name == place.admin1_name
        assert restored.district_name_raw == place.district_name_raw
    
    @given(place=place_strategy)
    @settings(max_examples=100)
    def test_place_dict_round_trip(self, place: Place):
        """
        Property test: Place -> dict -> Place produces equivalent object.
        
        **Feature: geocoding-service, Property 15: Place Serialization Round-Trip**
        **Validates: Requirements 9.3**
        """
        # Convert to dict
        data = place.to_dict()
        
        # Restore from dict
        restored = Place.from_dict(data)
        
        # Verify all fields are equal
        assert restored.place_id == place.place_id
        assert restored.country_code == place.country_code
        assert restored.city_name == place.city_name
        assert restored.lat == place.lat
        assert restored.lng == place.lng
        assert restored.timezone == place.timezone
        assert restored.source == place.source
        assert restored.accuracy == place.accuracy
        assert restored.admin1_code == place.admin1_code
        assert restored.admin1_name == place.admin1_name
        assert restored.district_name_raw == place.district_name_raw
