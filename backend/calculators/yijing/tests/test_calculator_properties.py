# backend/calculators/yijing/tests/test_calculator_properties.py
"""
Property-based tests for YijingCalculator.

**Feature: calculator-integration, Property 8: YijingCalculator Hexagram Validity**
**Validates: Requirements 7.1, 7.2**

Tests that for any divination method, the generated hexagram number is in range 1-64
with valid upper and lower trigrams.

Uses Hypothesis for property-based testing with minimum 100 iterations.
"""

import pytest
from hypothesis import given, settings, strategies as st
from typing import List

from backend.calculators.yijing import YijingCalculator, YijingInput
from backend.calculators.yijing.models import TRIGRAM_DATA, VALID_LINE_VALUES


# =============================================================================
# Strategies for generating test data
# =============================================================================

# Strategy for valid line values (6, 7, 8, 9)
valid_line = st.sampled_from([6, 7, 8, 9])

# Strategy for 6 valid lines
valid_lines = st.lists(valid_line, min_size=6, max_size=6)

# Strategy for divination methods
divination_method = st.sampled_from(["coin", "yarrow", "time", "manual"])


# =============================================================================
# Property 8: YijingCalculator Hexagram Validity
# **Feature: calculator-integration, Property 8: YijingCalculator Hexagram Validity**
# **Validates: Requirements 7.1, 7.2**
# =============================================================================

class TestHexagramValidity:
    """
    Property 8: YijingCalculator Hexagram Validity
    
    *For any* divination method, the generated hexagram number must be in range 1-64
    with valid upper and lower trigrams.
    
    **Feature: calculator-integration, Property 8: YijingCalculator Hexagram Validity**
    **Validates: Requirements 7.1, 7.2**
    """
    
    @given(lines=valid_lines)
    @settings(max_examples=100)
    def test_manual_method_produces_valid_hexagram(self, lines: List[int]):
        """
        Property: For any valid manual line input, the hexagram number is 1-64.
        
        **Feature: calculator-integration, Property 8: YijingCalculator Hexagram Validity**
        **Validates: Requirements 7.1, 7.2**
        """
        calc = YijingCalculator()
        input_data = YijingInput(
            divination_method="manual",
            manual_lines=lines
        )
        
        result = calc.calculate(input_data)
        
        # Hexagram number must be in valid range
        assert 1 <= result.main_hexagram.number <= 64, \
            f"Hexagram number {result.main_hexagram.number} out of range 1-64"
        
        # Upper and lower trigrams must be valid
        assert result.main_hexagram.upper_trigram in TRIGRAM_DATA, \
            f"Invalid upper trigram: {result.main_hexagram.upper_trigram}"
        assert result.main_hexagram.lower_trigram in TRIGRAM_DATA, \
            f"Invalid lower trigram: {result.main_hexagram.lower_trigram}"
        
        # Lines must be exactly 6 binary values
        assert len(result.main_hexagram.lines) == 6, \
            f"Expected 6 lines, got {len(result.main_hexagram.lines)}"
        assert all(line in (0, 1) for line in result.main_hexagram.lines), \
            f"Lines must be 0 or 1, got {result.main_hexagram.lines}"
    
    @given(st.integers(min_value=0, max_value=1000))
    @settings(max_examples=100)
    def test_coin_method_produces_valid_hexagram(self, seed: int):
        """
        Property: For any random seed, coin method produces valid hexagram.
        
        **Feature: calculator-integration, Property 8: YijingCalculator Hexagram Validity**
        **Validates: Requirements 7.1, 7.2**
        """
        import random
        random.seed(seed)
        
        calc = YijingCalculator()
        input_data = YijingInput(divination_method="coin")
        
        result = calc.calculate(input_data)
        
        # Hexagram number must be in valid range
        assert 1 <= result.main_hexagram.number <= 64
        
        # Trigrams must be valid
        assert result.main_hexagram.upper_trigram in TRIGRAM_DATA
        assert result.main_hexagram.lower_trigram in TRIGRAM_DATA
    
    @given(st.integers(min_value=0, max_value=1000))
    @settings(max_examples=100)
    def test_yarrow_method_produces_valid_hexagram(self, seed: int):
        """
        Property: For any random seed, yarrow method produces valid hexagram.
        
        **Feature: calculator-integration, Property 8: YijingCalculator Hexagram Validity**
        **Validates: Requirements 7.1, 7.2**
        """
        import random
        random.seed(seed)
        
        calc = YijingCalculator()
        input_data = YijingInput(divination_method="yarrow")
        
        result = calc.calculate(input_data)
        
        # Hexagram number must be in valid range
        assert 1 <= result.main_hexagram.number <= 64
        
        # Trigrams must be valid
        assert result.main_hexagram.upper_trigram in TRIGRAM_DATA
        assert result.main_hexagram.lower_trigram in TRIGRAM_DATA
    
    @given(
        year=st.integers(min_value=1900, max_value=2100),
        month=st.integers(min_value=1, max_value=12),
        day=st.integers(min_value=1, max_value=28),
        hour=st.integers(min_value=0, max_value=23)
    )
    @settings(max_examples=100)
    def test_time_method_produces_valid_hexagram(
        self, year: int, month: int, day: int, hour: int
    ):
        """
        Property: For any valid datetime, time method produces valid hexagram.
        
        **Feature: calculator-integration, Property 8: YijingCalculator Hexagram Validity**
        **Validates: Requirements 7.1, 7.2**
        """
        from datetime import datetime
        
        query_time = datetime(year, month, day, hour, 0)
        
        calc = YijingCalculator()
        input_data = YijingInput(
            divination_method="time",
            query_time=query_time
        )
        
        result = calc.calculate(input_data)
        
        # Hexagram number must be in valid range
        assert 1 <= result.main_hexagram.number <= 64
        
        # Trigrams must be valid
        assert result.main_hexagram.upper_trigram in TRIGRAM_DATA
        assert result.main_hexagram.lower_trigram in TRIGRAM_DATA
    
    @given(lines=valid_lines)
    @settings(max_examples=100)
    def test_mutual_hexagram_is_valid(self, lines: List[int]):
        """
        Property: For any hexagram, the mutual hexagram is also valid.
        
        **Feature: calculator-integration, Property 8: YijingCalculator Hexagram Validity**
        **Validates: Requirements 7.1, 7.2**
        """
        calc = YijingCalculator()
        input_data = YijingInput(
            divination_method="manual",
            manual_lines=lines
        )
        
        result = calc.calculate(input_data)
        
        # Mutual hexagram must be valid
        assert 1 <= result.mutual_hexagram.number <= 64, \
            f"Mutual hexagram number {result.mutual_hexagram.number} out of range"
        assert result.mutual_hexagram.upper_trigram in TRIGRAM_DATA
        assert result.mutual_hexagram.lower_trigram in TRIGRAM_DATA
        assert len(result.mutual_hexagram.lines) == 6



# =============================================================================
# Property 9: YijingCalculator Changed Hexagram
# **Feature: calculator-integration, Property 9: YijingCalculator Changed Hexagram**
# **Validates: Requirements 7.4**
# =============================================================================

class TestChangedHexagram:
    """
    Property 9: YijingCalculator Changed Hexagram
    
    *For any* hexagram with moving lines (老阴=6 or 老阳=9), a valid changed
    hexagram must be calculated.
    
    **Feature: calculator-integration, Property 9: YijingCalculator Changed Hexagram**
    **Validates: Requirements 7.4**
    """
    
    @given(lines=valid_lines)
    @settings(max_examples=100)
    def test_moving_lines_produce_changed_hexagram(self, lines: List[int]):
        """
        Property: If any line is 6 or 9, a changed hexagram must exist.
        
        **Feature: calculator-integration, Property 9: YijingCalculator Changed Hexagram**
        **Validates: Requirements 7.4**
        """
        calc = YijingCalculator()
        input_data = YijingInput(
            divination_method="manual",
            manual_lines=lines
        )
        
        result = calc.calculate(input_data)
        
        # Check if there are moving lines (6 or 9)
        has_moving_lines = any(line in (6, 9) for line in lines)
        
        if has_moving_lines:
            # Changed hexagram must exist
            assert result.changed_hexagram is not None, \
                f"Moving lines {[i+1 for i, l in enumerate(lines) if l in (6,9)]} " \
                f"but no changed hexagram"
            
            # Changed hexagram must be valid
            assert 1 <= result.changed_hexagram.number <= 64, \
                f"Changed hexagram number {result.changed_hexagram.number} out of range"
            assert result.changed_hexagram.upper_trigram in TRIGRAM_DATA
            assert result.changed_hexagram.lower_trigram in TRIGRAM_DATA
            
            # Moving lines list must match
            expected_moving = [i + 1 for i, line in enumerate(lines) if line in (6, 9)]
            assert result.moving_lines == expected_moving, \
                f"Expected moving lines {expected_moving}, got {result.moving_lines}"
        else:
            # No moving lines means no changed hexagram
            assert result.changed_hexagram is None, \
                f"No moving lines but changed hexagram exists"
            assert result.moving_lines == [], \
                f"No moving lines but moving_lines is {result.moving_lines}"
    
    @given(
        static_lines=st.lists(st.sampled_from([7, 8]), min_size=6, max_size=6)
    )
    @settings(max_examples=100)
    def test_no_moving_lines_no_changed_hexagram(self, static_lines: List[int]):
        """
        Property: If no line is 6 or 9, no changed hexagram should exist.
        
        **Feature: calculator-integration, Property 9: YijingCalculator Changed Hexagram**
        **Validates: Requirements 7.4**
        """
        calc = YijingCalculator()
        input_data = YijingInput(
            divination_method="manual",
            manual_lines=static_lines
        )
        
        result = calc.calculate(input_data)
        
        # No moving lines
        assert result.moving_lines == [], \
            f"Expected no moving lines, got {result.moving_lines}"
        
        # No changed hexagram
        assert result.changed_hexagram is None, \
            f"Expected no changed hexagram, got {result.changed_hexagram}"
    
    @given(lines=valid_lines)
    @settings(max_examples=100)
    def test_changed_hexagram_differs_when_moving(self, lines: List[int]):
        """
        Property: Changed hexagram lines differ from main at moving positions.
        
        **Feature: calculator-integration, Property 9: YijingCalculator Changed Hexagram**
        **Validates: Requirements 7.4**
        """
        calc = YijingCalculator()
        input_data = YijingInput(
            divination_method="manual",
            manual_lines=lines
        )
        
        result = calc.calculate(input_data)
        
        if result.changed_hexagram:
            main_lines = result.main_hexagram.lines
            changed_lines = result.changed_hexagram.lines
            
            for i, (main, changed, raw) in enumerate(zip(main_lines, changed_lines, lines)):
                if raw in (6, 9):
                    # Moving line: should be different
                    assert main != changed, \
                        f"Line {i+1} is moving ({raw}) but didn't change: {main} -> {changed}"
                else:
                    # Static line: should be same
                    assert main == changed, \
                        f"Line {i+1} is static ({raw}) but changed: {main} -> {changed}"
    
    @given(
        moving_positions=st.lists(
            st.integers(min_value=0, max_value=5),
            min_size=1,
            max_size=6,
            unique=True
        )
    )
    @settings(max_examples=100)
    def test_specific_moving_positions(self, moving_positions: List[int]):
        """
        Property: Specific moving positions produce correct changed hexagram.
        
        **Feature: calculator-integration, Property 9: YijingCalculator Changed Hexagram**
        **Validates: Requirements 7.4**
        """
        # Create lines with specific moving positions
        lines = []
        for i in range(6):
            if i in moving_positions:
                # Use 9 (老阳) for moving yang, 6 (老阴) for moving yin
                lines.append(9 if i % 2 == 0 else 6)
            else:
                # Use 7 (少阳) for static yang, 8 (少阴) for static yin
                lines.append(7 if i % 2 == 0 else 8)
        
        calc = YijingCalculator()
        input_data = YijingInput(
            divination_method="manual",
            manual_lines=lines
        )
        
        result = calc.calculate(input_data)
        
        # Verify moving lines match expected positions (1-indexed)
        expected_moving = sorted([p + 1 for p in moving_positions])
        assert result.moving_lines == expected_moving, \
            f"Expected moving lines {expected_moving}, got {result.moving_lines}"
        
        # Changed hexagram must exist
        assert result.changed_hexagram is not None
        assert 1 <= result.changed_hexagram.number <= 64
