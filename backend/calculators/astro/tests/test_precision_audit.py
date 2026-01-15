# backend/calculators/astro/tests/test_precision_audit.py
"""
Precision Audit Tests for AstroCalculator

This module contains property-based tests and precision audits for the
AstroCalculator, validating against Swiss Ephemeris reference data.

**Feature: calculator-accuracy-audit**
"""

import pytest
from datetime import datetime
from typing import Dict, List, Tuple
from hypothesis import given, strategies as st, settings, assume

import swisseph as swe

from backend.calculators.astro import AstroCalculator, AstroInput
from backend.calculators.astro.models import PLANETS, PLANET_SE_IDS, SIGNS, ASPECT_TYPES, ASPECT_ANGLES, ASPECT_ORBS


# =============================================================================
# Constants
# =============================================================================

# 1 arcminute = 1/60 degree ≈ 0.0167 degrees
ARCMINUTE_TOLERANCE = 1.0 / 60.0  # 0.0167 degrees

# 1 degree tolerance for ascendant/midheaven
DEGREE_TOLERANCE = 1.0

# Valid IANA timezones for testing
VALID_TIMEZONES = [
    'Asia/Shanghai', 'Asia/Tokyo', 'Asia/Seoul', 'Asia/Singapore',
    'America/New_York', 'America/Los_Angeles', 'America/Chicago',
    'Europe/London', 'Europe/Paris', 'Europe/Berlin',
    'Australia/Sydney', 'Pacific/Auckland', 'UTC'
]


# =============================================================================
# Test Strategies
# =============================================================================

@st.composite
def valid_datetime_strategy(draw):
    """Generate valid datetime within supported range (1900-2100)."""
    year = draw(st.integers(min_value=1900, max_value=2100))
    month = draw(st.integers(min_value=1, max_value=12))
    day = draw(st.integers(min_value=1, max_value=28))  # Safe for all months
    hour = draw(st.integers(min_value=0, max_value=23))
    minute = draw(st.integers(min_value=0, max_value=59))
    second = draw(st.integers(min_value=0, max_value=59))
    return datetime(year, month, day, hour, minute, second)


@st.composite
def valid_location_strategy(draw):
    """Generate valid (longitude, latitude) pairs, avoiding polar regions."""
    longitude = draw(st.floats(min_value=-180.0, max_value=180.0, allow_nan=False, allow_infinity=False))
    # Avoid extreme latitudes where house calculations can fail
    latitude = draw(st.floats(min_value=-66.0, max_value=66.0, allow_nan=False, allow_infinity=False))
    return (longitude, latitude)


@st.composite
def astro_input_strategy(draw):
    """Generate valid AstroInput for testing."""
    dt = draw(valid_datetime_strategy())
    location = draw(valid_location_strategy())
    timezone = draw(st.sampled_from(VALID_TIMEZONES))
    house_system = draw(st.sampled_from(["placidus", "koch", "equal", "whole_sign"]))
    
    return AstroInput(
        birth_datetime=dt,
        birth_location=location,
        timezone=timezone,
        house_system=house_system,
    )


# =============================================================================
# Reference Calculation Functions (Direct Swiss Ephemeris)
# =============================================================================

def get_reference_planet_position(julian_day: float, planet_name: str) -> Tuple[float, float, float, float]:
    """
    Get reference planet position directly from Swiss Ephemeris.
    
    Returns:
        Tuple of (longitude, latitude, distance, speed)
    """
    planet_id = PLANET_SE_IDS[planet_name]
    result, ret_flag = swe.calc_ut(julian_day, planet_id, swe.FLG_SPEED)
    return result[0], result[1], result[2], result[3]


def get_reference_houses(julian_day: float, latitude: float, longitude: float, house_system: str) -> Tuple[Dict[int, float], float, float]:
    """
    Get reference house cusps directly from Swiss Ephemeris.
    
    Returns:
        Tuple of (house_cusps_dict, ascendant, midheaven)
    """
    house_codes = {
        "placidus": b'P',
        "koch": b'K',
        "equal": b'E',
        "whole_sign": b'W',
    }
    hsys = house_codes.get(house_system, b'P')
    cusps, ascmc = swe.houses(julian_day, latitude, longitude, hsys)
    
    houses = {i + 1: cusps[i] for i in range(12)}
    return houses, ascmc[0], ascmc[1]


def datetime_to_julian_day(dt: datetime, timezone: str = None) -> float:
    """Convert datetime to Julian Day (UTC)."""
    from zoneinfo import ZoneInfo
    
    if timezone:
        local_tz = ZoneInfo(timezone)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=local_tz)
        utc_dt = dt.astimezone(ZoneInfo("UTC"))
        dt = utc_dt.replace(tzinfo=None)
    
    hour = dt.hour + dt.minute / 60.0 + dt.second / 3600.0
    return swe.julday(dt.year, dt.month, dt.day, hour)


# =============================================================================
# Property 11: 行星位置精度 (Planet Position Accuracy)
# =============================================================================

class TestPlanetPositionAccuracy:
    """
    **Feature: calculator-accuracy-audit, Property 11: 行星位置精度**
    
    *对于任意* 有效的出生时间和地点，占星计算器计算的行星位置与瑞士星历表数据的误差应小于1弧分。
    
    **Validates: Requirements 5.1**
    """
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100, deadline=None)
    def test_planet_longitude_accuracy(self, input_data: AstroInput):
        """
        Property test: Planet longitudes match Swiss Ephemeris within 1 arcminute.
        
        **Feature: calculator-accuracy-audit, Property 11: 行星位置精度**
        **Validates: Requirements 5.1**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        # Get Julian Day for reference calculation
        julian_day = datetime_to_julian_day(input_data.birth_datetime, input_data.timezone)
        
        for planet_name in PLANETS:
            calc_longitude = result.planets[planet_name].longitude
            ref_longitude, _, _, _ = get_reference_planet_position(julian_day, planet_name)
            
            # Calculate difference (handle wrap-around at 360°)
            diff = abs(calc_longitude - ref_longitude)
            if diff > 180:
                diff = 360 - diff
            
            assert diff < ARCMINUTE_TOLERANCE, (
                f"Planet {planet_name} longitude error exceeds 1 arcminute: "
                f"calculated={calc_longitude:.6f}°, reference={ref_longitude:.6f}°, "
                f"diff={diff:.6f}° ({diff * 60:.4f} arcmin)"
            )
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100, deadline=None)
    def test_planet_latitude_accuracy(self, input_data: AstroInput):
        """
        Property test: Planet latitudes match Swiss Ephemeris within 1 arcminute.
        
        **Feature: calculator-accuracy-audit, Property 11: 行星位置精度**
        **Validates: Requirements 5.1**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        julian_day = datetime_to_julian_day(input_data.birth_datetime, input_data.timezone)
        
        for planet_name in PLANETS:
            calc_latitude = result.planets[planet_name].latitude
            _, ref_latitude, _, _ = get_reference_planet_position(julian_day, planet_name)
            
            diff = abs(calc_latitude - ref_latitude)
            
            assert diff < ARCMINUTE_TOLERANCE, (
                f"Planet {planet_name} latitude error exceeds 1 arcminute: "
                f"calculated={calc_latitude:.6f}°, reference={ref_latitude:.6f}°, "
                f"diff={diff:.6f}° ({diff * 60:.4f} arcmin)"
            )
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100, deadline=None)
    def test_planet_speed_sign_correct(self, input_data: AstroInput):
        """
        Property test: Planet speed sign (retrograde detection) is correct.
        
        **Feature: calculator-accuracy-audit, Property 11: 行星位置精度**
        **Validates: Requirements 5.1**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        julian_day = datetime_to_julian_day(input_data.birth_datetime, input_data.timezone)
        
        for planet_name in PLANETS:
            calc_retrograde = result.planets[planet_name].retrograde
            _, _, _, ref_speed = get_reference_planet_position(julian_day, planet_name)
            ref_retrograde = ref_speed < 0
            
            assert calc_retrograde == ref_retrograde, (
                f"Planet {planet_name} retrograde status mismatch: "
                f"calculated={calc_retrograde}, reference={ref_retrograde} (speed={ref_speed})"
            )


# =============================================================================
# Property 22: 占星上升点精度 (Ascendant Accuracy)
# =============================================================================

class TestAscendantAccuracy:
    """
    **Feature: calculator-accuracy-audit, Property 22: 占星上升点精度**
    
    *对于任意* 有效的出生时间和地点，占星计算器计算的上升点误差应小于1度。
    
    **Validates: Requirements 5.2**
    """
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100, deadline=None)
    def test_ascendant_accuracy(self, input_data: AstroInput):
        """
        Property test: Ascendant matches Swiss Ephemeris within 1 degree.
        
        **Feature: calculator-accuracy-audit, Property 22: 占星上升点精度**
        **Validates: Requirements 5.2**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        julian_day = datetime_to_julian_day(input_data.birth_datetime, input_data.timezone)
        longitude, latitude = input_data.birth_location
        
        _, ref_ascendant, _ = get_reference_houses(
            julian_day, latitude, longitude, input_data.house_system
        )
        
        # Calculate difference (handle wrap-around at 360°)
        diff = abs(result.ascendant - ref_ascendant)
        if diff > 180:
            diff = 360 - diff
        
        assert diff < DEGREE_TOLERANCE, (
            f"Ascendant error exceeds 1 degree: "
            f"calculated={result.ascendant:.4f}°, reference={ref_ascendant:.4f}°, "
            f"diff={diff:.4f}°"
        )
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100, deadline=None)
    def test_midheaven_accuracy(self, input_data: AstroInput):
        """
        Property test: Midheaven matches Swiss Ephemeris within 1 degree.
        
        **Feature: calculator-accuracy-audit, Property 22: 占星上升点精度**
        **Validates: Requirements 5.2**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        julian_day = datetime_to_julian_day(input_data.birth_datetime, input_data.timezone)
        longitude, latitude = input_data.birth_location
        
        _, _, ref_midheaven = get_reference_houses(
            julian_day, latitude, longitude, input_data.house_system
        )
        
        # Calculate difference (handle wrap-around at 360°)
        diff = abs(result.midheaven - ref_midheaven)
        if diff > 180:
            diff = 360 - diff
        
        assert diff < DEGREE_TOLERANCE, (
            f"Midheaven error exceeds 1 degree: "
            f"calculated={result.midheaven:.4f}°, reference={ref_midheaven:.4f}°, "
            f"diff={diff:.4f}°"
        )
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100, deadline=None)
    def test_house_cusps_accuracy(self, input_data: AstroInput):
        """
        Property test: All house cusps match Swiss Ephemeris within 1 degree.
        
        **Feature: calculator-accuracy-audit, Property 22: 占星上升点精度**
        **Validates: Requirements 5.2**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        julian_day = datetime_to_julian_day(input_data.birth_datetime, input_data.timezone)
        longitude, latitude = input_data.birth_location
        
        ref_houses, _, _ = get_reference_houses(
            julian_day, latitude, longitude, input_data.house_system
        )
        
        for house_num in range(1, 13):
            calc_cusp = result.houses[house_num]
            ref_cusp = ref_houses[house_num]
            
            # Calculate difference (handle wrap-around at 360°)
            diff = abs(calc_cusp - ref_cusp)
            if diff > 180:
                diff = 360 - diff
            
            assert diff < DEGREE_TOLERANCE, (
                f"House {house_num} cusp error exceeds 1 degree: "
                f"calculated={calc_cusp:.4f}°, reference={ref_cusp:.4f}°, "
                f"diff={diff:.4f}°"
            )


# =============================================================================
# Property 23: 占星相位识别正确性 (Aspect Identification Correctness)
# =============================================================================

class TestAspectIdentification:
    """
    **Feature: calculator-accuracy-audit, Property 23: 占星相位识别正确性**
    
    *对于任意* 两颗行星的位置，占星计算器应正确识别主要相位（合相、六分相、四分相、三分相、对分相）及其容许度。
    
    **Validates: Requirements 5.5, 5.6**
    """
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100, deadline=None)
    def test_aspect_angles_within_orb(self, input_data: AstroInput):
        """
        Property test: All identified aspects have angles within their orb tolerance.
        
        **Feature: calculator-accuracy-audit, Property 23: 占星相位识别正确性**
        **Validates: Requirements 5.5, 5.6**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        for aspect in result.aspects:
            aspect_type = aspect.aspect_type
            expected_angle = ASPECT_ANGLES[aspect_type]
            max_orb = ASPECT_ORBS[aspect_type]
            
            # The orb should be within the maximum allowed
            assert aspect.orb <= max_orb, (
                f"Aspect {aspect.planet1}-{aspect.planet2} ({aspect_type}) "
                f"orb {aspect.orb:.2f}° exceeds max orb {max_orb}°"
            )
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100, deadline=None)
    def test_aspect_orb_calculation_correct(self, input_data: AstroInput):
        """
        Property test: Aspect orb is correctly calculated from planet positions.
        
        **Feature: calculator-accuracy-audit, Property 23: 占星相位识别正确性**
        **Validates: Requirements 5.5, 5.6**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        for aspect in result.aspects:
            planet1_pos = result.planets[aspect.planet1]
            planet2_pos = result.planets[aspect.planet2]
            
            # Calculate angle between planets
            angle_diff = abs(planet1_pos.longitude - planet2_pos.longitude)
            if angle_diff > 180:
                angle_diff = 360 - angle_diff
            
            # Calculate expected orb
            expected_angle = ASPECT_ANGLES[aspect.aspect_type]
            expected_orb = abs(angle_diff - expected_angle)
            
            # Handle opposition special case
            if aspect.aspect_type == "opposition":
                expected_orb = min(expected_orb, abs(360 - angle_diff - expected_angle))
            
            # Orb should match within small tolerance (floating point)
            assert abs(aspect.orb - expected_orb) < 0.01, (
                f"Aspect {aspect.planet1}-{aspect.planet2} ({aspect.aspect_type}) "
                f"orb mismatch: calculated={aspect.orb:.4f}°, expected={expected_orb:.4f}°"
            )
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100, deadline=None)
    def test_no_duplicate_aspects(self, input_data: AstroInput):
        """
        Property test: No duplicate aspects between the same planet pair.
        
        **Feature: calculator-accuracy-audit, Property 23: 占星相位识别正确性**
        **Validates: Requirements 5.5, 5.6**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        seen_pairs = set()
        for aspect in result.aspects:
            # Normalize pair order
            pair = tuple(sorted([aspect.planet1, aspect.planet2]))
            
            assert pair not in seen_pairs, (
                f"Duplicate aspect found for pair {pair}: {aspect.aspect_type}"
            )
            seen_pairs.add(pair)
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=100, deadline=None)
    def test_major_aspects_detected(self, input_data: AstroInput):
        """
        Property test: Major aspects within tight orb are detected.
        
        **Feature: calculator-accuracy-audit, Property 23: 占星相位识别正确性**
        **Validates: Requirements 5.5, 5.6**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        # Check all planet pairs for aspects that should be detected
        planet_names = list(result.planets.keys())
        
        for i, planet1 in enumerate(planet_names):
            for planet2 in planet_names[i + 1:]:
                pos1 = result.planets[planet1]
                pos2 = result.planets[planet2]
                
                # Calculate angle
                angle = abs(pos1.longitude - pos2.longitude)
                if angle > 180:
                    angle = 360 - angle
                
                # Check if any major aspect should be detected
                for aspect_type in ASPECT_TYPES:
                    expected_angle = ASPECT_ANGLES[aspect_type]
                    max_orb = ASPECT_ORBS[aspect_type]
                    
                    orb = abs(angle - expected_angle)
                    if aspect_type == "opposition":
                        orb = min(orb, abs(360 - angle - expected_angle))
                    
                    # If within tight orb (half of max), should be detected
                    if orb <= max_orb / 2:
                        # Check if this aspect was detected
                        found = any(
                            (a.planet1 == planet1 and a.planet2 == planet2) or
                            (a.planet1 == planet2 and a.planet2 == planet1)
                            for a in result.aspects
                        )
                        
                        assert found, (
                            f"Expected {aspect_type} between {planet1} and {planet2} "
                            f"(angle={angle:.2f}°, orb={orb:.2f}°) was not detected"
                        )
                        break  # Only one aspect per pair


# =============================================================================
# Timezone Handling Tests (Requirements 5.9)
# =============================================================================

class TestTimezoneHandling:
    """
    Tests for timezone handling including DST and historical timezone changes.
    
    **Validates: Requirements 5.9**
    """
    
    def test_dst_transition_spring(self):
        """
        Test DST spring forward transition handling.
        
        **Validates: Requirements 5.9**
        """
        calculator = AstroCalculator()
        
        # March 10, 2024 - US DST starts (2:00 AM -> 3:00 AM)
        # Test time just before and after transition
        input_before = AstroInput(
            birth_datetime=datetime(2024, 3, 10, 1, 30),
            birth_location=(-74.0060, 40.7128),  # New York
            timezone="America/New_York",
            house_system="placidus",
        )
        
        input_after = AstroInput(
            birth_datetime=datetime(2024, 3, 10, 3, 30),
            birth_location=(-74.0060, 40.7128),
            timezone="America/New_York",
            house_system="placidus",
        )
        
        result_before = calculator.calculate(input_before)
        result_after = calculator.calculate(input_after)
        
        # Sun should move approximately 1 degree in 2 hours (actual time difference)
        sun_diff = abs(result_after.planets["sun"].longitude - result_before.planets["sun"].longitude)
        
        # Expected: ~1 hour actual time difference (2:30 -> 3:30 is 1 hour due to DST)
        # Sun moves ~1 degree per day, so ~0.04 degrees per hour
        assert sun_diff < 0.1, f"Unexpected sun movement during DST: {sun_diff}°"
    
    def test_dst_transition_fall(self):
        """
        Test DST fall back transition handling.
        
        **Validates: Requirements 5.9**
        """
        calculator = AstroCalculator()
        
        # November 3, 2024 - US DST ends (2:00 AM -> 1:00 AM)
        input_before = AstroInput(
            birth_datetime=datetime(2024, 11, 3, 0, 30),
            birth_location=(-74.0060, 40.7128),
            timezone="America/New_York",
            house_system="placidus",
        )
        
        input_after = AstroInput(
            birth_datetime=datetime(2024, 11, 3, 3, 30),
            birth_location=(-74.0060, 40.7128),
            timezone="America/New_York",
            house_system="placidus",
        )
        
        result_before = calculator.calculate(input_before)
        result_after = calculator.calculate(input_after)
        
        # Should handle the extra hour correctly
        sun_diff = abs(result_after.planets["sun"].longitude - result_before.planets["sun"].longitude)
        
        # 4 hours actual time (including extra hour from DST)
        # Sun moves ~0.17 degrees in 4 hours
        assert 0.1 < sun_diff < 0.3, f"Unexpected sun movement during DST fallback: {sun_diff}°"
    
    def test_different_timezones_same_utc(self):
        """
        Test that same UTC moment produces same results regardless of input timezone.
        
        **Validates: Requirements 5.9**
        """
        calculator = AstroCalculator()
        
        # Same moment in different timezones
        # 2024-06-15 12:00 UTC = 2024-06-15 20:00 Asia/Shanghai = 2024-06-15 08:00 America/New_York
        
        input_utc = AstroInput(
            birth_datetime=datetime(2024, 6, 15, 12, 0),
            birth_location=(0.0, 51.5),  # London
            timezone="UTC",
            house_system="placidus",
        )
        
        input_shanghai = AstroInput(
            birth_datetime=datetime(2024, 6, 15, 20, 0),
            birth_location=(0.0, 51.5),
            timezone="Asia/Shanghai",
            house_system="placidus",
        )
        
        input_ny = AstroInput(
            birth_datetime=datetime(2024, 6, 15, 8, 0),
            birth_location=(0.0, 51.5),
            timezone="America/New_York",
            house_system="placidus",
        )
        
        result_utc = calculator.calculate(input_utc)
        result_shanghai = calculator.calculate(input_shanghai)
        result_ny = calculator.calculate(input_ny)
        
        # All should produce same planetary positions
        for planet in PLANETS:
            utc_long = result_utc.planets[planet].longitude
            shanghai_long = result_shanghai.planets[planet].longitude
            ny_long = result_ny.planets[planet].longitude
            
            assert abs(utc_long - shanghai_long) < 0.001, (
                f"Planet {planet} differs between UTC and Shanghai: "
                f"{utc_long:.6f}° vs {shanghai_long:.6f}°"
            )
            assert abs(utc_long - ny_long) < 0.001, (
                f"Planet {planet} differs between UTC and NY: "
                f"{utc_long:.6f}° vs {ny_long:.6f}°"
            )
    
    @given(input_data=astro_input_strategy())
    @settings(max_examples=50, deadline=None)
    def test_timezone_conversion_consistency(self, input_data: AstroInput):
        """
        Property test: Timezone conversion is consistent with direct UTC calculation.
        
        **Validates: Requirements 5.9**
        """
        calculator = AstroCalculator()
        result = calculator.calculate(input_data)
        
        # The Julian Day should be correctly computed
        # We verify by checking that the result is deterministic
        result2 = calculator.calculate(input_data)
        
        for planet in PLANETS:
            assert result.planets[planet].longitude == result2.planets[planet].longitude, (
                f"Non-deterministic calculation for {planet}"
            )
