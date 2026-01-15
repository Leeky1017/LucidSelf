"""
Property-Based Tests for GeoNames Parser

Tests for the GeoNames cities500.txt parser to ensure data integrity.
Uses Hypothesis framework for property-based testing.
"""

import pytest
from hypothesis import given, strategies as st, settings, assume
import sys
from pathlib import Path

# Add scripts to path for importing
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent / 'scripts'))

from build_world_cities_from_geonames import parse_geonames_line


# =============================================================================
# Strategies for generating test data
# =============================================================================

# Valid feature classes in GeoNames
FEATURE_CLASSES = ['A', 'H', 'L', 'P', 'R', 'S', 'T', 'U', 'V']

# Non-empty text without tabs or newlines
safe_text = st.text(
    alphabet=st.characters(
        blacklist_categories=('Cs',),
        blacklist_characters='\t\n\r\x00'
    ),
    min_size=1,
    max_size=50
).filter(lambda x: x.strip())

# Country code strategy (2 uppercase letters)
country_code_strategy = st.text(
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    min_size=2,
    max_size=2
)

# Timezone strategy
timezone_strategy = st.sampled_from([
    'Asia/Shanghai', 'Asia/Tokyo', 'America/New_York',
    'Europe/London', 'Australia/Sydney', 'UTC'
])

# Optional admin code
optional_admin_code = st.one_of(st.just(''), st.text(
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',
    min_size=1,
    max_size=5
))

# Optional alternate names (comma-separated)
optional_alt_names = st.one_of(
    st.just(''),
    st.lists(safe_text, min_size=1, max_size=5).map(lambda x: ','.join(x))
)


def build_geonames_line(
    geonameid: str,
    name: str,
    asciiname: str,
    alternatenames: str,
    latitude: float,
    longitude: float,
    feature_class: str,
    feature_code: str,
    country_code: str,
    cc2: str,
    admin1_code: str,
    admin2_code: str,
    admin3_code: str,
    admin4_code: str,
    population: str,
    elevation: str,
    dem: str,
    timezone: str,
    modification_date: str
) -> str:
    """Build a GeoNames-format tab-separated line."""
    fields = [
        geonameid, name, asciiname, alternatenames,
        str(latitude), str(longitude),
        feature_class, feature_code,
        country_code, cc2,
        admin1_code, admin2_code, admin3_code, admin4_code,
        population, elevation, dem,
        timezone, modification_date
    ]
    return '\t'.join(fields)


# Strategy for generating valid GeoNames lines
geonames_line_strategy = st.builds(
    build_geonames_line,
    geonameid=st.integers(min_value=1, max_value=99999999).map(str),
    name=safe_text,
    asciiname=safe_text,
    alternatenames=optional_alt_names,
    latitude=st.floats(min_value=-90.0, max_value=90.0, allow_nan=False, allow_infinity=False),
    longitude=st.floats(min_value=-180.0, max_value=180.0, allow_nan=False, allow_infinity=False),
    feature_class=st.sampled_from(FEATURE_CLASSES),
    feature_code=st.text(alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', min_size=1, max_size=5),
    country_code=country_code_strategy,
    cc2=st.just(''),
    admin1_code=optional_admin_code,
    admin2_code=st.just(''),
    admin3_code=st.just(''),
    admin4_code=st.just(''),
    population=st.one_of(st.just(''), st.integers(min_value=0, max_value=50000000).map(str)),
    elevation=st.just(''),
    dem=st.just(''),
    timezone=timezone_strategy,
    modification_date=st.just('2024-01-01')
)


# =============================================================================
# Property Tests
# =============================================================================

class TestFeatureClassInvariant:
    """
    **Feature: geocoding-service, Property 6: world_cities Feature Class Invariant**
    
    *For any* record in the world_cities table, the original GeoNames 
    feature_class must have been 'P' (populated place).
    
    **Validates: Requirements 3.2**
    """
    
    @given(line=geonames_line_strategy)
    @settings(max_examples=100)
    def test_only_feature_class_p_records_are_parsed(self, line: str):
        """
        Property test: Only records with feature_class='P' are returned by parser.
        
        **Feature: geocoding-service, Property 6: world_cities Feature Class Invariant**
        **Validates: Requirements 3.2**
        """
        result = parse_geonames_line(line)
        
        # Extract feature_class from the line
        fields = line.split('\t')
        feature_class = fields[6] if len(fields) > 6 else ''
        
        if feature_class == 'P':
            # Records with feature_class='P' should be parsed (if valid)
            # Note: may still be None if other required fields are invalid
            if result is not None:
                assert result['feature_class'] == 'P', \
                    f"Parsed record should have feature_class='P', got {result.get('feature_class')}"
        else:
            # Records with feature_class != 'P' should be filtered out
            assert result is None, \
                f"Record with feature_class='{feature_class}' should be filtered out"
    
    @given(
        geonameid=st.integers(min_value=1, max_value=99999999).map(str),
        name=safe_text,
        latitude=st.floats(min_value=-90.0, max_value=90.0, allow_nan=False, allow_infinity=False),
        longitude=st.floats(min_value=-180.0, max_value=180.0, allow_nan=False, allow_infinity=False),
        country_code=country_code_strategy,
        timezone=timezone_strategy,
        non_p_feature_class=st.sampled_from(['A', 'H', 'L', 'R', 'S', 'T', 'U', 'V'])
    )
    @settings(max_examples=100)
    def test_non_p_feature_class_always_filtered(
        self,
        geonameid: str,
        name: str,
        latitude: float,
        longitude: float,
        country_code: str,
        timezone: str,
        non_p_feature_class: str
    ):
        """
        Property test: Records with feature_class != 'P' are always filtered out.
        
        **Feature: geocoding-service, Property 6: world_cities Feature Class Invariant**
        **Validates: Requirements 3.2**
        """
        line = build_geonames_line(
            geonameid=geonameid,
            name=name,
            asciiname=name,
            alternatenames='',
            latitude=latitude,
            longitude=longitude,
            feature_class=non_p_feature_class,
            feature_code='PPL',
            country_code=country_code,
            cc2='',
            admin1_code='',
            admin2_code='',
            admin3_code='',
            admin4_code='',
            population='1000',
            elevation='',
            dem='',
            timezone=timezone,
            modification_date='2024-01-01'
        )
        
        result = parse_geonames_line(line)
        
        assert result is None, \
            f"Record with feature_class='{non_p_feature_class}' should be filtered out"
    
    @given(
        geonameid=st.integers(min_value=1, max_value=99999999).map(str),
        name=safe_text,
        latitude=st.floats(min_value=-90.0, max_value=90.0, allow_nan=False, allow_infinity=False),
        longitude=st.floats(min_value=-180.0, max_value=180.0, allow_nan=False, allow_infinity=False),
        country_code=country_code_strategy,
        timezone=timezone_strategy
    )
    @settings(max_examples=100)
    def test_p_feature_class_records_are_parsed(
        self,
        geonameid: str,
        name: str,
        latitude: float,
        longitude: float,
        country_code: str,
        timezone: str
    ):
        """
        Property test: Valid records with feature_class='P' are successfully parsed.
        
        **Feature: geocoding-service, Property 6: world_cities Feature Class Invariant**
        **Validates: Requirements 3.2**
        """
        line = build_geonames_line(
            geonameid=geonameid,
            name=name,
            asciiname=name,
            alternatenames='',
            latitude=latitude,
            longitude=longitude,
            feature_class='P',
            feature_code='PPL',
            country_code=country_code,
            cc2='',
            admin1_code='',
            admin2_code='',
            admin3_code='',
            admin4_code='',
            population='1000',
            elevation='',
            dem='',
            timezone=timezone,
            modification_date='2024-01-01'
        )
        
        result = parse_geonames_line(line)
        
        assert result is not None, "Valid record with feature_class='P' should be parsed"
        assert result['feature_class'] == 'P', "Parsed record should have feature_class='P'"
        assert result['city_id'] == f'gn-{geonameid}'
        assert result['city_name'] == name
        assert result['country_code'] == country_code
        assert result['timezone'] == timezone
        assert result['source'] == 'geonames'
