# backend/calculators/astro/tests/test_calculator_properties.py
"""
Property-Based Tests for AstroCalculator

AstroCalculator 的属性测试。
使用 Hypothesis 框架进行属性测试。
"""

import pytest
from datetime import datetime
from hypothesis import given, strategies as st, settings, assume

from backend.calculators.astro import (
    AstroCalculator,
    AstroInput,
    AstroFactors,
    PLANETS,
    SIGNS,
)


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

# Latitude strategy: -90 to 90 (excluding extreme poles for house calculation)
latitude_strategy = st.floats(
    min_value=-66.0,  # Avoid polar regions where house systems fail
    max_value=66.0, 
    allow_nan=False, 
    allow_infinity=False
)

# Location tuple strategy (longitude, latitude)
location_strategy = st.tuples(longitude_strategy, latitude_strategy)

# Year strategy: within supported range
year_strategy = st.integers(min_value=1900, max_value=2100)

# Month strategy
month_strategy = st.integers(min_value=1, max_value=12)

# Day strategy (simplified - not accounting for month lengths)
day_strategy = st.integers(min_value=1, max_value=28)

# Hour strategy
hour_strategy = st.integers(min_value=0, max_value=23)

# Minute strategy
minute_strategy = st.integers(min_value=0, max_value=59)

# House system strategy
house_system_strategy = st.sampled_from(["placidus", "koch", "equal", "whole_sign"])


@st.composite
def datetime_strategy(draw):
    """Generate valid datetime objects within supported range."""
    year = draw(year_strategy)
    month = draw(month_strategy)
    day = draw(day_strategy)
    hour = draw(hour_strategy)
    minute = draw(minute_strategy)
    return datetime(year, month, day, hour, minute)


@st.composite
def astro_input_strategy(draw):
    """Generate valid AstroInput objects."""
    dt = draw(datetime_strategy())
    location = draw(location_strategy)
    timezone = draw(timezone_strategy)
    house_system = draw(house_system_strategy)
    
    return AstroInput(
        birth_datetime=dt,
        birth_location=location,
        timezone=timezone,
        house_system=house_system,
    )


# =============================================================================
# Property 4: AstroCalculator Planet Coverage
# =============================================================================

class TestAstroCalculatorPlanetCoverage:
    """
    **Feature: calculator-integration, Property 4: AstroCalculator Planet Coverage**
    
    *For any* valid AstroInput, the AstroCalculator must return positions 
    for all 10 major celestial bodies (Sun through Pluto).
    
    **Validates: Requirements 3.1**
    """
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100)
    def test_all_planets_calculated(self, input_data: AstroInput):
        """
        Property test: For any valid input, all 10 planets are calculated.
        
        **Feature: calculator-integration, Property 4: AstroCalculator Planet Coverage**
        **Validates: Requirements 3.1**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        # All 10 planets must be present
        assert len(result.planets) == 10, \
            f"Expected 10 planets, got {len(result.planets)}"
        
        # Each expected planet must be present
        for planet in PLANETS:
            assert planet in result.planets, \
                f"Missing planet: {planet}"
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100)
    def test_planet_positions_have_valid_longitude(self, input_data: AstroInput):
        """
        Property test: All planet longitudes are in valid range [0, 360).
        
        **Feature: calculator-integration, Property 4: AstroCalculator Planet Coverage**
        **Validates: Requirements 3.1**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        for planet_name, pos in result.planets.items():
            assert 0.0 <= pos.longitude < 360.0, \
                f"{planet_name} longitude {pos.longitude} out of range [0, 360)"
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100)
    def test_planet_positions_have_valid_sign(self, input_data: AstroInput):
        """
        Property test: All planets have a valid zodiac sign.
        
        **Feature: calculator-integration, Property 4: AstroCalculator Planet Coverage**
        **Validates: Requirements 3.1**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        for planet_name, pos in result.planets.items():
            assert pos.sign in SIGNS, \
                f"{planet_name} has invalid sign: {pos.sign}"
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100)
    def test_planet_degree_in_sign_valid(self, input_data: AstroInput):
        """
        Property test: All planet degrees within sign are in valid range [0, 30).
        
        **Feature: calculator-integration, Property 4: AstroCalculator Planet Coverage**
        **Validates: Requirements 3.1**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        for planet_name, pos in result.planets.items():
            assert 0.0 <= pos.degree_in_sign < 30.0, \
                f"{planet_name} degree_in_sign {pos.degree_in_sign} out of range [0, 30)"
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100)
    def test_planet_sign_matches_longitude(self, input_data: AstroInput):
        """
        Property test: Planet sign is consistent with longitude.
        
        **Feature: calculator-integration, Property 4: AstroCalculator Planet Coverage**
        **Validates: Requirements 3.1**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        for planet_name, pos in result.planets.items():
            # Calculate expected sign from longitude
            expected_sign_index = int(pos.longitude / 30.0)
            expected_sign = SIGNS[expected_sign_index]
            
            assert pos.sign == expected_sign, \
                f"{planet_name} sign mismatch: {pos.sign} != {expected_sign} (longitude: {pos.longitude})"
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100)
    def test_planet_house_valid(self, input_data: AstroInput):
        """
        Property test: All planets have valid house placement (1-12).
        
        **Feature: calculator-integration, Property 4: AstroCalculator Planet Coverage**
        **Validates: Requirements 3.1**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        for planet_name, pos in result.planets.items():
            assert 1 <= pos.house <= 12, \
                f"{planet_name} house {pos.house} out of range [1, 12]"
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100)
    def test_factor_matrix_contains_all_planets(self, input_data: AstroInput):
        """
        Property test: Factor matrix contains factors for all planets.
        
        **Feature: calculator-integration, Property 4: AstroCalculator Planet Coverage**
        **Validates: Requirements 3.1**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        factor_matrix = result.to_factor_matrix()
        
        # Each planet should have at least sign and house factors
        for planet in PLANETS:
            # Check for planet in sign factor
            sign_factors = [fid for fid in factor_matrix.factors.keys() 
                          if fid.startswith(f"astro_{planet}_in_")]
            assert len(sign_factors) == 1, \
                f"Expected 1 sign factor for {planet}, got {len(sign_factors)}"
            
            # Check for planet in house factor
            house_factors = [fid for fid in factor_matrix.factors.keys() 
                           if fid.startswith(f"astro_{planet}_house_")]
            assert len(house_factors) == 1, \
                f"Expected 1 house factor for {planet}, got {len(house_factors)}"


# =============================================================================
# Property 5: AstroCalculator House Coverage
# =============================================================================

class TestAstroCalculatorHouseCoverage:
    """
    **Feature: calculator-integration, Property 5: AstroCalculator House Coverage**
    
    *For any* valid AstroInput with location, the AstroCalculator must return 
    all 12 house cusps.
    
    **Validates: Requirements 3.3**
    """
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100)
    def test_all_houses_calculated(self, input_data: AstroInput):
        """
        Property test: For any valid input, all 12 house cusps are calculated.
        
        **Feature: calculator-integration, Property 5: AstroCalculator House Coverage**
        **Validates: Requirements 3.3**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        # All 12 houses must be present
        assert len(result.houses) == 12, \
            f"Expected 12 houses, got {len(result.houses)}"
        
        # Each house 1-12 must be present
        for house_num in range(1, 13):
            assert house_num in result.houses, \
                f"Missing house: {house_num}"
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100)
    def test_house_cusps_have_valid_longitude(self, input_data: AstroInput):
        """
        Property test: All house cusps are in valid range [0, 360).
        
        **Feature: calculator-integration, Property 5: AstroCalculator House Coverage**
        **Validates: Requirements 3.3**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        for house_num, cusp in result.houses.items():
            assert 0.0 <= cusp < 360.0, \
                f"House {house_num} cusp {cusp} out of range [0, 360)"
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100)
    def test_ascendant_valid(self, input_data: AstroInput):
        """
        Property test: Ascendant is in valid range [0, 360).
        
        **Feature: calculator-integration, Property 5: AstroCalculator House Coverage**
        **Validates: Requirements 3.3**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        assert 0.0 <= result.ascendant < 360.0, \
            f"Ascendant {result.ascendant} out of range [0, 360)"
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100)
    def test_midheaven_valid(self, input_data: AstroInput):
        """
        Property test: Midheaven is in valid range [0, 360).
        
        **Feature: calculator-integration, Property 5: AstroCalculator House Coverage**
        **Validates: Requirements 3.3**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        assert 0.0 <= result.midheaven < 360.0, \
            f"Midheaven {result.midheaven} out of range [0, 360)"
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100)
    def test_ascendant_sign_valid(self, input_data: AstroInput):
        """
        Property test: Ascendant sign is a valid zodiac sign.
        
        **Feature: calculator-integration, Property 5: AstroCalculator House Coverage**
        **Validates: Requirements 3.3**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        assert result.ascendant_sign in SIGNS, \
            f"Invalid ascendant sign: {result.ascendant_sign}"
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100)
    def test_midheaven_sign_valid(self, input_data: AstroInput):
        """
        Property test: Midheaven sign is a valid zodiac sign.
        
        **Feature: calculator-integration, Property 5: AstroCalculator House Coverage**
        **Validates: Requirements 3.3**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        assert result.midheaven_sign in SIGNS, \
            f"Invalid midheaven sign: {result.midheaven_sign}"
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100)
    def test_ascendant_sign_matches_degree(self, input_data: AstroInput):
        """
        Property test: Ascendant sign is consistent with ascendant degree.
        
        **Feature: calculator-integration, Property 5: AstroCalculator House Coverage**
        **Validates: Requirements 3.3**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        # Calculate expected sign from ascendant degree
        expected_sign_index = int(result.ascendant / 30.0)
        expected_sign = SIGNS[expected_sign_index]
        
        assert result.ascendant_sign == expected_sign, \
            f"Ascendant sign mismatch: {result.ascendant_sign} != {expected_sign}"
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100)
    def test_midheaven_sign_matches_degree(self, input_data: AstroInput):
        """
        Property test: Midheaven sign is consistent with midheaven degree.
        
        **Feature: calculator-integration, Property 5: AstroCalculator House Coverage**
        **Validates: Requirements 3.3**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        # Calculate expected sign from midheaven degree
        expected_sign_index = int(result.midheaven / 30.0)
        expected_sign = SIGNS[expected_sign_index]
        
        assert result.midheaven_sign == expected_sign, \
            f"Midheaven sign mismatch: {result.midheaven_sign} != {expected_sign}"
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100)
    def test_house_1_cusp_relationship_to_ascendant(self, input_data: AstroInput):
        """
        Property test: House 1 cusp has correct relationship to ascendant.
        
        For Placidus/Koch: House 1 cusp equals the ascendant.
        For Whole Sign: House 1 cusp is at the start of the ascendant's sign.
        For Equal: House 1 cusp equals the ascendant.
        
        **Feature: calculator-integration, Property 5: AstroCalculator House Coverage**
        **Validates: Requirements 3.3**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        if input_data.house_system == "whole_sign":
            # For whole sign, house 1 starts at 0° of the ascendant's sign
            expected_cusp = int(result.ascendant / 30.0) * 30.0
            assert abs(result.houses[1] - expected_cusp) < 0.001, \
                f"House 1 cusp {result.houses[1]} != expected {expected_cusp} for whole sign"
        else:
            # For other systems, house 1 cusp equals ascendant
            assert abs(result.houses[1] - result.ascendant) < 0.001, \
                f"House 1 cusp {result.houses[1]} != Ascendant {result.ascendant}"
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100)
    def test_factor_matrix_contains_all_houses(self, input_data: AstroInput):
        """
        Property test: Factor matrix contains factors for all house cusps.
        
        **Feature: calculator-integration, Property 5: AstroCalculator House Coverage**
        **Validates: Requirements 3.3**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        factor_matrix = result.to_factor_matrix()
        
        # Each house should have a cusp factor
        for house_num in range(1, 13):
            factor_id = f"astro_house_{house_num}_cusp"
            assert factor_id in factor_matrix.factors, \
                f"Missing house cusp factor: {factor_id}"
        
        # Ascendant and midheaven factors should exist
        assert "astro_ascendant" in factor_matrix.factors, \
            "Missing astro_ascendant factor"
        assert "astro_midheaven" in factor_matrix.factors, \
            "Missing astro_midheaven factor"
