"""
Property-Based Tests for Input Normalizer

输入规范化器的属性测试。
使用 Hypothesis 框架进行属性测试。
"""

import pytest
from hypothesis import given, strategies as st, settings, assume

from backend.core.geocoding.normalizer import (
    Normalizer,
    CHINESE_SUFFIXES,
    ENGLISH_SUFFIXES,
)


# =============================================================================
# Strategies for generating test data
# =============================================================================

# Text strategy that includes various Unicode characters
# Excludes null characters and surrogate pairs
general_text = st.text(
    alphabet=st.characters(
        blacklist_categories=('Cs',),  # Exclude surrogates
        blacklist_characters='\x00'
    ),
    min_size=0,
    max_size=100
)

# Non-empty text for city names
non_empty_text = st.text(
    alphabet=st.characters(
        blacklist_categories=('Cs',),
        blacklist_characters='\x00,，|'  # Exclude delimiters
    ),
    min_size=1,
    max_size=50
).filter(lambda x: x.strip())  # Must have non-whitespace content

# City name strategy - alphanumeric and Chinese characters
# Exclude characters that are also suffixes to avoid test ambiguity
CHINESE_CITY_CHARS = '北京上海广深杭南武成西重天苏青大连厦包头呼和浩特'  # Removed 州/市/区 etc.

city_name_strategy = st.one_of(
    # English city names
    st.text(
        alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ',
        min_size=1,
        max_size=30
    ).filter(lambda x: x.strip()),
    # Chinese city names - using characters that are NOT suffixes
    st.text(
        alphabet=CHINESE_CITY_CHARS,
        min_size=1,
        max_size=10
    ).filter(lambda x: x.strip()),
)

# Country hint strategy
country_hint_strategy = st.one_of(
    st.none(),
    st.text(
        alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        min_size=2,
        max_size=2
    ),
    # Country names
    st.sampled_from(['china', 'China', 'CHINA', '中国', 'usa', 'USA', 'japan', 'Japan'])
)


# =============================================================================
# Property Tests
# =============================================================================

class TestNormalizationIdempotence:
    """
    **Feature: geocoding-service, Property 1: Normalization Idempotence**
    
    *For any* input string, normalizing it once should produce the same result 
    as normalizing it multiple times. Mathematically: normalize(x) == normalize(normalize(x)).
    
    **Validates: Requirements 1.1, 1.4**
    """
    
    @given(text=general_text)
    @settings(max_examples=100)
    def test_normalize_idempotence(self, text: str):
        """
        Property test: normalize(x) == normalize(normalize(x))
        
        **Feature: geocoding-service, Property 1: Normalization Idempotence**
        **Validates: Requirements 1.1, 1.4**
        """
        normalizer = Normalizer()
        
        # First normalization
        once = normalizer.normalize(text)
        
        # Second normalization
        twice = normalizer.normalize(once)
        
        # Should be identical
        assert once == twice, f"Idempotence failed: normalize('{text}') = '{once}', normalize('{once}') = '{twice}'"
    
    @given(text=general_text)
    @settings(max_examples=100)
    def test_normalize_triple_application(self, text: str):
        """
        Property test: normalize applied three times equals once.
        
        **Feature: geocoding-service, Property 1: Normalization Idempotence**
        **Validates: Requirements 1.1, 1.4**
        """
        normalizer = Normalizer()
        
        once = normalizer.normalize(text)
        thrice = normalizer.normalize(normalizer.normalize(normalizer.normalize(text)))
        
        assert once == thrice


class TestSuffixRemovalConsistency:
    """
    **Feature: geocoding-service, Property 2: Suffix Removal Consistency**
    
    *For any* city name and any valid geographic suffix, appending the suffix 
    and then normalizing should produce the original city name (after normalization).
    
    **Validates: Requirements 1.2**
    """
    
    @given(
        city=city_name_strategy,
        suffix=st.sampled_from(CHINESE_SUFFIXES)
    )
    @settings(max_examples=100)
    def test_chinese_suffix_removal(self, city: str, suffix: str):
        """
        Property test: Chinese suffix removal consistency.
        
        **Feature: geocoding-service, Property 2: Suffix Removal Consistency**
        **Validates: Requirements 1.2**
        """
        normalizer = Normalizer()
        
        # Normalize the base city name
        normalized_city = normalizer.normalize(city)
        assume(normalized_city)  # Skip if city normalizes to empty
        
        # Append suffix and normalize
        with_suffix = city + suffix
        normalized_with_suffix = normalizer.normalize(with_suffix)
        
        # Should produce the same result
        assert normalized_with_suffix == normalized_city, \
            f"Suffix removal failed: '{city}' + '{suffix}' -> '{normalized_with_suffix}', expected '{normalized_city}'"
    
    @given(
        city=st.text(
            alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
            min_size=1,
            max_size=20
        ).filter(lambda x: x.strip() and x.lower() not in ENGLISH_SUFFIXES),
        suffix=st.sampled_from(ENGLISH_SUFFIXES)
    )
    @settings(max_examples=100)
    def test_english_suffix_removal(self, city: str, suffix: str):
        """
        Property test: English suffix removal consistency.
        
        **Feature: geocoding-service, Property 2: Suffix Removal Consistency**
        **Validates: Requirements 1.2**
        """
        normalizer = Normalizer()
        
        # Normalize the base city name
        normalized_city = normalizer.normalize(city)
        assume(normalized_city)  # Skip if city normalizes to empty
        
        # Append suffix with space and normalize
        with_suffix = city + ' ' + suffix
        normalized_with_suffix = normalizer.normalize(with_suffix)
        
        # Should produce the same result
        assert normalized_with_suffix == normalized_city, \
            f"Suffix removal failed: '{city} {suffix}' -> '{normalized_with_suffix}', expected '{normalized_city}'"


class TestCityCountryParsingRoundTrip:
    """
    **Feature: geocoding-service, Property 3: City-Country Parsing Round-Trip**
    
    *For any* valid city name and country code, formatting them as "city, country" 
    and then parsing should recover the original city and country components.
    
    **Validates: Requirements 1.3**
    """
    
    @given(
        city=st.text(
            alphabet='abcdefghijklmnopqrstuvwxyz',
            min_size=1,
            max_size=20
        ).filter(lambda x: x.strip()),
        country=st.text(
            alphabet='abcdefghijklmnopqrstuvwxyz',
            min_size=1,
            max_size=20
        ).filter(lambda x: x.strip())
    )
    @settings(max_examples=100)
    def test_city_country_round_trip(self, city: str, country: str):
        """
        Property test: format("city, country") -> parse -> (city, country)
        
        **Feature: geocoding-service, Property 3: City-Country Parsing Round-Trip**
        **Validates: Requirements 1.3**
        """
        normalizer = Normalizer()
        
        # Format as "city, country"
        formatted = f"{city}, {country}"
        
        # Parse back
        parsed_city, parsed_country = normalizer.parse_city_country(formatted)
        
        # Normalize expected values for comparison
        expected_city = normalizer.normalize(city)
        expected_country = normalizer.normalize(country)
        
        assume(expected_city)  # Skip if city normalizes to empty
        assume(expected_country)  # Skip if country normalizes to empty
        
        assert parsed_city == expected_city, \
            f"City mismatch: parsed '{parsed_city}', expected '{expected_city}'"
        assert parsed_country == expected_country, \
            f"Country mismatch: parsed '{parsed_country}', expected '{expected_country}'"
    
    @given(
        city=st.text(
            alphabet=CHINESE_CITY_CHARS,  # Use chars that are NOT suffixes
            min_size=1,
            max_size=5
        ).filter(lambda x: x.strip()),
        country=st.sampled_from(['中国', '日本', '韩国'])
    )
    @settings(max_examples=100)
    def test_chinese_city_country_round_trip(self, city: str, country: str):
        """
        Property test: Chinese city-country parsing round-trip.
        
        **Feature: geocoding-service, Property 3: City-Country Parsing Round-Trip**
        **Validates: Requirements 1.3**
        """
        normalizer = Normalizer()
        
        # Format with Chinese comma
        formatted = f"{city}，{country}"
        
        # Parse back
        parsed_city, parsed_country = normalizer.parse_city_country(formatted)
        
        # Normalize expected values
        expected_city = normalizer.normalize(city)
        expected_country = normalizer.normalize(country)
        
        assume(expected_city)
        assume(expected_country)
        
        assert parsed_city == expected_city
        assert parsed_country == expected_country


class TestCacheKeyDeterminism:
    """
    **Feature: geocoding-service, Property 13: Cache Key Determinism**
    
    *For any* normalized_query and hint_country combination, the generated cache_key 
    must be deterministic and follow the format: normalized_query + '|' + (hint_country or '').
    
    **Validates: Requirements 5.4**
    """
    
    @given(
        query=non_empty_text,
        country=country_hint_strategy
    )
    @settings(max_examples=100)
    def test_cache_key_determinism(self, query: str, country):
        """
        Property test: Same inputs always produce same cache key.
        
        **Feature: geocoding-service, Property 13: Cache Key Determinism**
        **Validates: Requirements 5.4**
        """
        normalizer = Normalizer()
        
        # Generate cache key twice
        key1 = normalizer.build_cache_key(query, country)
        key2 = normalizer.build_cache_key(query, country)
        
        # Must be identical
        assert key1 == key2, f"Cache key not deterministic: '{key1}' != '{key2}'"
    
    @given(
        query=non_empty_text,
        country=country_hint_strategy
    )
    @settings(max_examples=100)
    def test_cache_key_format(self, query: str, country):
        """
        Property test: Cache key follows expected format.
        
        **Feature: geocoding-service, Property 13: Cache Key Determinism**
        **Validates: Requirements 5.4**
        """
        normalizer = Normalizer()
        
        key = normalizer.build_cache_key(query, country)
        
        # Key must contain exactly one pipe separator
        assert key.count('|') == 1, f"Cache key must have exactly one '|': '{key}'"
        
        # Split and verify structure
        parts = key.split('|')
        assert len(parts) == 2
        
        # Query part should be lowercase
        assert parts[0] == parts[0].lower()
        
        # Country part should be uppercase (if present)
        if parts[1]:
            assert parts[1] == parts[1].upper()
    
    @given(
        query1=non_empty_text,
        query2=non_empty_text,
        country=country_hint_strategy
    )
    @settings(max_examples=100)
    def test_different_queries_different_keys(self, query1: str, query2: str, country):
        """
        Property test: Different queries produce different cache keys.
        
        **Feature: geocoding-service, Property 13: Cache Key Determinism**
        **Validates: Requirements 5.4**
        """
        normalizer = Normalizer()
        
        # Normalize queries for comparison
        norm1 = normalizer.normalize(query1)
        norm2 = normalizer.normalize(query2)
        
        # Skip if queries normalize to the same value
        assume(norm1 != norm2)
        assume(norm1)
        assume(norm2)
        
        key1 = normalizer.build_cache_key(query1, country)
        key2 = normalizer.build_cache_key(query2, country)
        
        assert key1 != key2, f"Different queries should produce different keys"
