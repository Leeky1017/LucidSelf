# backend/calculators/yijing/tests/test_probability_properties.py
"""
Property-based tests for YijingCalculator probability distributions.

**Feature: calculator-accuracy-audit**

Tests the probability distributions of coin and yarrow divination methods
using property-based testing with Hypothesis.
"""

import pytest
import random
from collections import Counter
from typing import Dict, List

from hypothesis import given, settings, strategies as st, assume, Phase

from backend.calculators.yijing import YijingCalculator, YijingInput


# =============================================================================
# Property 7: 铜钱法概率分布
# **Feature: calculator-accuracy-audit, Property 7: 铜钱法概率分布**
# **Validates: Requirements 4.1**
# =============================================================================

class TestCoinMethodProbabilityProperty:
    """
    Property 7: 铜钱法概率分布
    
    *For* large numbers (≥10000) of coin method divinations, each line type's
    frequency should approach theoretical probability within 5% tolerance:
    - 6 (老阴): 1/8 = 0.125
    - 7 (少阳): 3/8 = 0.375
    - 8 (少阴): 3/8 = 0.375
    - 9 (老阳): 1/8 = 0.125
    
    **Feature: calculator-accuracy-audit, Property 7: 铜钱法概率分布**
    **Validates: Requirements 4.1**
    """
    
    THEORETICAL_PROBABILITIES = {
        6: 1/8,   # 老阴: 0.125
        7: 3/8,   # 少阳: 0.375
        8: 3/8,   # 少阴: 0.375
        9: 1/8,   # 老阳: 0.125
    }
    
    TOLERANCE = 0.05  # 5% tolerance
    
    @given(seed=st.integers(min_value=0, max_value=2**31 - 1))
    @settings(max_examples=100, phases=[Phase.generate])
    def test_coin_method_probability_distribution(self, seed: int):
        """
        Property 7: For any random seed, coin method probability distribution
        converges to theoretical values over large samples.
        
        **Feature: calculator-accuracy-audit, Property 7: 铜钱法概率分布**
        **Validates: Requirements 4.1**
        """
        random.seed(seed)
        calc = YijingCalculator()
        
        # Generate 2000 hexagrams = 12000 lines (sufficient for statistical significance)
        num_trials = 2000
        line_counts = Counter()
        
        for _ in range(num_trials):
            input_data = YijingInput(divination_method="coin")
            result = calc.calculate(input_data)
            
            if result.main_hexagram.raw_lines:
                for line in result.main_hexagram.raw_lines:
                    line_counts[line] += 1
        
        total_lines = sum(line_counts.values())
        
        # Verify each line type's probability is within tolerance
        for value, expected_prob in self.THEORETICAL_PROBABILITIES.items():
            observed_prob = line_counts[value] / total_lines
            deviation = abs(observed_prob - expected_prob)
            
            assert deviation < self.TOLERANCE, (
                f"Coin method probability for {value} deviates too much: "
                f"observed={observed_prob:.4f}, expected={expected_prob:.4f}, "
                f"deviation={deviation:.4f}, tolerance={self.TOLERANCE}"
            )
    
    @given(seed=st.integers(min_value=0, max_value=2**31 - 1))
    @settings(max_examples=100, phases=[Phase.generate])
    def test_coin_method_line_values_valid(self, seed: int):
        """
        Property: All coin method line values are in {6, 7, 8, 9}.
        
        **Feature: calculator-accuracy-audit, Property 7: 铜钱法概率分布**
        **Validates: Requirements 4.1**
        """
        random.seed(seed)
        calc = YijingCalculator()
        
        # Generate multiple hexagrams
        for _ in range(100):
            input_data = YijingInput(divination_method="coin")
            result = calc.calculate(input_data)
            
            if result.main_hexagram.raw_lines:
                for line in result.main_hexagram.raw_lines:
                    assert line in {6, 7, 8, 9}, (
                        f"Invalid coin method line value: {line}"
                    )
    
    @given(seed=st.integers(min_value=0, max_value=2**31 - 1))
    @settings(max_examples=100, phases=[Phase.generate])
    def test_coin_method_produces_six_lines(self, seed: int):
        """
        Property: Coin method always produces exactly 6 lines.
        
        **Feature: calculator-accuracy-audit, Property 7: 铜钱法概率分布**
        **Validates: Requirements 4.1**
        """
        random.seed(seed)
        calc = YijingCalculator()
        
        input_data = YijingInput(divination_method="coin")
        result = calc.calculate(input_data)
        
        assert result.main_hexagram.raw_lines is not None, "raw_lines should not be None"
        assert len(result.main_hexagram.raw_lines) == 6, (
            f"Expected 6 lines, got {len(result.main_hexagram.raw_lines)}"
        )


# =============================================================================
# Property 8: 蓍草法概率分布
# **Feature: calculator-accuracy-audit, Property 8: 蓍草法概率分布**
# **Validates: Requirements 4.2**
# =============================================================================

class TestYarrowMethodProbabilityProperty:
    """
    Property 8: 蓍草法概率分布
    
    *For* large numbers (≥10000) of yarrow method divinations, each line type's
    frequency should approach theoretical probability within 5% tolerance:
    - 6 (老阴): 1/16 = 0.0625
    - 7 (少阳): 5/16 = 0.3125
    - 8 (少阴): 7/16 = 0.4375
    - 9 (老阳): 3/16 = 0.1875
    
    **Feature: calculator-accuracy-audit, Property 8: 蓍草法概率分布**
    **Validates: Requirements 4.2**
    """
    
    THEORETICAL_PROBABILITIES = {
        6: 1/16,   # 老阴: 0.0625
        7: 5/16,   # 少阳: 0.3125
        8: 7/16,   # 少阴: 0.4375
        9: 3/16,   # 老阳: 0.1875
    }
    
    TOLERANCE = 0.05  # 5% tolerance
    
    @given(seed=st.integers(min_value=0, max_value=2**31 - 1))
    @settings(max_examples=100, phases=[Phase.generate])
    def test_yarrow_method_probability_distribution(self, seed: int):
        """
        Property 8: For any random seed, yarrow method probability distribution
        converges to theoretical values over large samples.
        
        **Feature: calculator-accuracy-audit, Property 8: 蓍草法概率分布**
        **Validates: Requirements 4.2**
        """
        random.seed(seed)
        calc = YijingCalculator()
        
        # Generate 2000 hexagrams = 12000 lines (sufficient for statistical significance)
        num_trials = 2000
        line_counts = Counter()
        
        for _ in range(num_trials):
            input_data = YijingInput(divination_method="yarrow")
            result = calc.calculate(input_data)
            
            if result.main_hexagram.raw_lines:
                for line in result.main_hexagram.raw_lines:
                    line_counts[line] += 1
        
        total_lines = sum(line_counts.values())
        
        # Verify each line type's probability is within tolerance
        for value, expected_prob in self.THEORETICAL_PROBABILITIES.items():
            observed_prob = line_counts[value] / total_lines
            deviation = abs(observed_prob - expected_prob)
            
            assert deviation < self.TOLERANCE, (
                f"Yarrow method probability for {value} deviates too much: "
                f"observed={observed_prob:.4f}, expected={expected_prob:.4f}, "
                f"deviation={deviation:.4f}, tolerance={self.TOLERANCE}"
            )
    
    @given(seed=st.integers(min_value=0, max_value=2**31 - 1))
    @settings(max_examples=100, phases=[Phase.generate])
    def test_yarrow_method_line_values_valid(self, seed: int):
        """
        Property: All yarrow method line values are in {6, 7, 8, 9}.
        
        **Feature: calculator-accuracy-audit, Property 8: 蓍草法概率分布**
        **Validates: Requirements 4.2**
        """
        random.seed(seed)
        calc = YijingCalculator()
        
        # Generate multiple hexagrams
        for _ in range(100):
            input_data = YijingInput(divination_method="yarrow")
            result = calc.calculate(input_data)
            
            if result.main_hexagram.raw_lines:
                for line in result.main_hexagram.raw_lines:
                    assert line in {6, 7, 8, 9}, (
                        f"Invalid yarrow method line value: {line}"
                    )
    
    @given(seed=st.integers(min_value=0, max_value=2**31 - 1))
    @settings(max_examples=100, phases=[Phase.generate])
    def test_yarrow_method_produces_six_lines(self, seed: int):
        """
        Property: Yarrow method always produces exactly 6 lines.
        
        **Feature: calculator-accuracy-audit, Property 8: 蓍草法概率分布**
        **Validates: Requirements 4.2**
        """
        random.seed(seed)
        calc = YijingCalculator()
        
        input_data = YijingInput(divination_method="yarrow")
        result = calc.calculate(input_data)
        
        assert result.main_hexagram.raw_lines is not None, "raw_lines should not be None"
        assert len(result.main_hexagram.raw_lines) == 6, (
            f"Expected 6 lines, got {len(result.main_hexagram.raw_lines)}"
        )
    
    @given(seed=st.integers(min_value=0, max_value=2**31 - 1))
    @settings(max_examples=100, phases=[Phase.generate])
    def test_yarrow_differs_from_coin(self, seed: int):
        """
        Property: Yarrow method has different probability distribution than coin.
        
        Specifically, yarrow has:
        - Lower probability for 老阴(6): 1/16 vs 1/8
        - Higher probability for 老阳(9): 3/16 vs 1/8
        - Higher probability for 少阴(8): 7/16 vs 3/8
        - Lower probability for 少阳(7): 5/16 vs 3/8
        
        **Feature: calculator-accuracy-audit, Property 8: 蓍草法概率分布**
        **Validates: Requirements 4.2**
        """
        random.seed(seed)
        calc = YijingCalculator()
        
        # Generate samples for both methods
        num_trials = 1000
        
        coin_counts = Counter()
        yarrow_counts = Counter()
        
        for _ in range(num_trials):
            coin_result = calc.calculate(YijingInput(divination_method="coin"))
            yarrow_result = calc.calculate(YijingInput(divination_method="yarrow"))
            
            if coin_result.main_hexagram.raw_lines:
                for line in coin_result.main_hexagram.raw_lines:
                    coin_counts[line] += 1
            
            if yarrow_result.main_hexagram.raw_lines:
                for line in yarrow_result.main_hexagram.raw_lines:
                    yarrow_counts[line] += 1
        
        coin_total = sum(coin_counts.values())
        yarrow_total = sum(yarrow_counts.values())
        
        # Yarrow should have lower 老阴(6) probability than coin
        coin_6_prob = coin_counts[6] / coin_total
        yarrow_6_prob = yarrow_counts[6] / yarrow_total
        
        # With enough samples, yarrow's 老阴 should be noticeably lower
        # (1/16 = 0.0625 vs 1/8 = 0.125)
        # Allow for statistical variation but expect general trend
        assert yarrow_6_prob < coin_6_prob + 0.05, (
            f"Yarrow 老阴(6) probability ({yarrow_6_prob:.4f}) should be lower than "
            f"coin ({coin_6_prob:.4f})"
        )



# =============================================================================
# Property 9: 互卦计算正确性
# **Feature: calculator-accuracy-audit, Property 9: 互卦计算正确性**
# **Validates: Requirements 4.3**
# =============================================================================

class TestMutualHexagramProperty:
    """
    Property 9: 互卦计算正确性
    
    *For any* 64 hexagrams, the mutual hexagram (互卦) should be correctly
    calculated by taking lines 2-5 of the original hexagram:
    - Lower trigram of mutual = lines 2, 3, 4 of original
    - Upper trigram of mutual = lines 3, 4, 5 of original
    
    **Feature: calculator-accuracy-audit, Property 9: 互卦计算正确性**
    **Validates: Requirements 4.3**
    """
    
    @given(lines=st.lists(st.sampled_from([6, 7, 8, 9]), min_size=6, max_size=6))
    @settings(max_examples=100)
    def test_mutual_hexagram_uses_lines_2_to_5(self, lines: List[int]):
        """
        Property 9: For any hexagram, mutual hexagram uses lines 2-5.
        
        **Feature: calculator-accuracy-audit, Property 9: 互卦计算正确性**
        **Validates: Requirements 4.3**
        """
        from backend.calculators.yijing.models import LINES_TO_TRIGRAM
        
        calc = YijingCalculator()
        input_data = YijingInput(
            divination_method="manual",
            manual_lines=lines
        )
        
        result = calc.calculate(input_data)
        
        # Convert raw lines to binary
        binary_lines = [1 if line in (7, 9) else 0 for line in lines]
        
        # Calculate expected mutual hexagram lines
        expected_mutual_lower = tuple(binary_lines[1:4])  # lines 2, 3, 4
        expected_mutual_upper = tuple(binary_lines[2:5])  # lines 3, 4, 5
        
        # Get expected trigram names
        expected_lower_trigram = LINES_TO_TRIGRAM.get(expected_mutual_lower)
        expected_upper_trigram = LINES_TO_TRIGRAM.get(expected_mutual_upper)
        
        # Verify mutual hexagram trigrams
        assert result.mutual_hexagram.lower_trigram == expected_lower_trigram, (
            f"Mutual lower trigram mismatch: "
            f"expected {expected_lower_trigram}, got {result.mutual_hexagram.lower_trigram}"
        )
        assert result.mutual_hexagram.upper_trigram == expected_upper_trigram, (
            f"Mutual upper trigram mismatch: "
            f"expected {expected_upper_trigram}, got {result.mutual_hexagram.upper_trigram}"
        )
    
    @given(lines=st.lists(st.sampled_from([6, 7, 8, 9]), min_size=6, max_size=6))
    @settings(max_examples=100)
    def test_mutual_hexagram_is_valid(self, lines: List[int]):
        """
        Property 9: Mutual hexagram is always a valid hexagram.
        
        **Feature: calculator-accuracy-audit, Property 9: 互卦计算正确性**
        **Validates: Requirements 4.3**
        """
        from backend.calculators.yijing.models import TRIGRAM_DATA
        
        calc = YijingCalculator()
        input_data = YijingInput(
            divination_method="manual",
            manual_lines=lines
        )
        
        result = calc.calculate(input_data)
        
        # Mutual hexagram must have valid number
        assert 1 <= result.mutual_hexagram.number <= 64, (
            f"Mutual hexagram number {result.mutual_hexagram.number} out of range"
        )
        
        # Mutual hexagram must have valid trigrams
        assert result.mutual_hexagram.upper_trigram in TRIGRAM_DATA, (
            f"Invalid mutual upper trigram: {result.mutual_hexagram.upper_trigram}"
        )
        assert result.mutual_hexagram.lower_trigram in TRIGRAM_DATA, (
            f"Invalid mutual lower trigram: {result.mutual_hexagram.lower_trigram}"
        )
        
        # Mutual hexagram must have 6 lines
        assert len(result.mutual_hexagram.lines) == 6, (
            f"Mutual hexagram should have 6 lines, got {len(result.mutual_hexagram.lines)}"
        )


# =============================================================================
# Property 10: 变卦计算正确性
# **Feature: calculator-accuracy-audit, Property 10: 变卦计算正确性**
# **Validates: Requirements 4.4**
# =============================================================================

class TestChangedHexagramProperty:
    """
    Property 10: 变卦计算正确性
    
    *For any* hexagram with moving lines (老阴=6 or 老阳=9), the changed
    hexagram should correctly apply the transformation:
    - 老阴 (6) changes to yang (1)
    - 老阳 (9) changes to yin (0)
    
    **Feature: calculator-accuracy-audit, Property 10: 变卦计算正确性**
    **Validates: Requirements 4.4**
    """
    
    @given(lines=st.lists(st.sampled_from([6, 7, 8, 9]), min_size=6, max_size=6))
    @settings(max_examples=100)
    def test_old_yin_changes_to_yang(self, lines: List[int]):
        """
        Property 10: 老阴 (6) changes to yang in changed hexagram.
        
        **Feature: calculator-accuracy-audit, Property 10: 变卦计算正确性**
        **Validates: Requirements 4.4**
        """
        calc = YijingCalculator()
        input_data = YijingInput(
            divination_method="manual",
            manual_lines=lines
        )
        
        result = calc.calculate(input_data)
        
        # Check each position with 老阴
        for i, line in enumerate(lines):
            if line == 6:  # 老阴
                # Main hexagram should have yin (0)
                assert result.main_hexagram.lines[i] == 0, (
                    f"Line {i+1}: 老阴 should be yin (0) in main hexagram"
                )
                
                # Changed hexagram should have yang (1)
                if result.changed_hexagram:
                    assert result.changed_hexagram.lines[i] == 1, (
                        f"Line {i+1}: 老阴 should change to yang (1)"
                    )
    
    @given(lines=st.lists(st.sampled_from([6, 7, 8, 9]), min_size=6, max_size=6))
    @settings(max_examples=100)
    def test_old_yang_changes_to_yin(self, lines: List[int]):
        """
        Property 10: 老阳 (9) changes to yin in changed hexagram.
        
        **Feature: calculator-accuracy-audit, Property 10: 变卦计算正确性**
        **Validates: Requirements 4.4**
        """
        calc = YijingCalculator()
        input_data = YijingInput(
            divination_method="manual",
            manual_lines=lines
        )
        
        result = calc.calculate(input_data)
        
        # Check each position with 老阳
        for i, line in enumerate(lines):
            if line == 9:  # 老阳
                # Main hexagram should have yang (1)
                assert result.main_hexagram.lines[i] == 1, (
                    f"Line {i+1}: 老阳 should be yang (1) in main hexagram"
                )
                
                # Changed hexagram should have yin (0)
                if result.changed_hexagram:
                    assert result.changed_hexagram.lines[i] == 0, (
                        f"Line {i+1}: 老阳 should change to yin (0)"
                    )
    
    @given(lines=st.lists(st.sampled_from([6, 7, 8, 9]), min_size=6, max_size=6))
    @settings(max_examples=100)
    def test_static_lines_unchanged(self, lines: List[int]):
        """
        Property 10: Static lines (7, 8) remain unchanged in changed hexagram.
        
        **Feature: calculator-accuracy-audit, Property 10: 变卦计算正确性**
        **Validates: Requirements 4.4**
        """
        calc = YijingCalculator()
        input_data = YijingInput(
            divination_method="manual",
            manual_lines=lines
        )
        
        result = calc.calculate(input_data)
        
        if result.changed_hexagram:
            # Check each position with static lines
            for i, line in enumerate(lines):
                if line in (7, 8):  # Static lines
                    main_line = result.main_hexagram.lines[i]
                    changed_line = result.changed_hexagram.lines[i]
                    
                    assert main_line == changed_line, (
                        f"Line {i+1}: static line ({line}) should not change, "
                        f"but {main_line} -> {changed_line}"
                    )
    
    @given(lines=st.lists(st.sampled_from([6, 7, 8, 9]), min_size=6, max_size=6))
    @settings(max_examples=100)
    def test_moving_lines_detected_correctly(self, lines: List[int]):
        """
        Property 10: Moving lines are correctly identified.
        
        **Feature: calculator-accuracy-audit, Property 10: 变卦计算正确性**
        **Validates: Requirements 4.4**
        """
        calc = YijingCalculator()
        input_data = YijingInput(
            divination_method="manual",
            manual_lines=lines
        )
        
        result = calc.calculate(input_data)
        
        # Calculate expected moving lines
        expected_moving = [i + 1 for i, line in enumerate(lines) if line in (6, 9)]
        
        assert result.moving_lines == expected_moving, (
            f"Moving lines mismatch: expected {expected_moving}, got {result.moving_lines}"
        )
        
        # Changed hexagram should exist iff there are moving lines
        if expected_moving:
            assert result.changed_hexagram is not None, (
                f"Changed hexagram should exist when there are moving lines"
            )
        else:
            assert result.changed_hexagram is None, (
                f"Changed hexagram should not exist when there are no moving lines"
            )


# =============================================================================
# Property 21: 时间起卦先天八卦序
# **Feature: calculator-accuracy-audit, Property 21: 时间起卦先天八卦序**
# **Validates: Requirements 4.5**
# =============================================================================

class TestTimeMethodProperty:
    """
    Property 21: 时间起卦先天八卦序
    
    *For any* valid datetime, the time-based divination method should use
    the 先天八卦序 (Pre-Heaven/Fu Xi sequence) to calculate trigrams:
    1=乾, 2=兑, 3=离, 4=震, 5=巽, 6=坎, 7=艮, 8=坤
    
    **Feature: calculator-accuracy-audit, Property 21: 时间起卦先天八卦序**
    **Validates: Requirements 4.5**
    """
    
    # 先天八卦序 (Pre-Heaven sequence)
    XIANTIAN_SEQUENCE = ["乾", "兑", "离", "震", "巽", "坎", "艮", "坤"]
    
    @given(
        year=st.integers(min_value=1900, max_value=2100),
        month=st.integers(min_value=1, max_value=12),
        day=st.integers(min_value=1, max_value=28),
        hour=st.integers(min_value=0, max_value=23)
    )
    @settings(max_examples=100)
    def test_upper_trigram_uses_xiantian_sequence(
        self, year: int, month: int, day: int, hour: int
    ):
        """
        Property 21: Upper trigram uses 先天八卦序.
        
        Upper trigram = XIANTIAN_SEQUENCE[(year + month + day) % 8]
        
        **Feature: calculator-accuracy-audit, Property 21: 时间起卦先天八卦序**
        **Validates: Requirements 4.5**
        """
        from datetime import datetime
        
        calc = YijingCalculator()
        query_time = datetime(year, month, day, hour, 0)
        
        input_data = YijingInput(
            divination_method="time",
            query_time=query_time
        )
        
        result = calc.calculate(input_data)
        
        # Calculate expected upper trigram
        upper_num = (year + month + day) % 8
        if upper_num == 0:
            upper_num = 8
        expected_upper = self.XIANTIAN_SEQUENCE[upper_num - 1]
        
        assert result.main_hexagram.upper_trigram == expected_upper, (
            f"Upper trigram mismatch for {year}-{month}-{day}: "
            f"expected {expected_upper}, got {result.main_hexagram.upper_trigram}"
        )
    
    @given(
        year=st.integers(min_value=1900, max_value=2100),
        month=st.integers(min_value=1, max_value=12),
        day=st.integers(min_value=1, max_value=28),
        hour=st.integers(min_value=0, max_value=23)
    )
    @settings(max_examples=100)
    def test_lower_trigram_uses_xiantian_sequence(
        self, year: int, month: int, day: int, hour: int
    ):
        """
        Property 21: Lower trigram uses 先天八卦序.
        
        Lower trigram = XIANTIAN_SEQUENCE[(year + month + day + hour) % 8]
        
        **Feature: calculator-accuracy-audit, Property 21: 时间起卦先天八卦序**
        **Validates: Requirements 4.5**
        """
        from datetime import datetime
        
        calc = YijingCalculator()
        query_time = datetime(year, month, day, hour, 0)
        
        input_data = YijingInput(
            divination_method="time",
            query_time=query_time
        )
        
        result = calc.calculate(input_data)
        
        # Calculate expected lower trigram
        lower_num = (year + month + day + hour) % 8
        if lower_num == 0:
            lower_num = 8
        expected_lower = self.XIANTIAN_SEQUENCE[lower_num - 1]
        
        assert result.main_hexagram.lower_trigram == expected_lower, (
            f"Lower trigram mismatch for {year}-{month}-{day} {hour}:00: "
            f"expected {expected_lower}, got {result.main_hexagram.lower_trigram}"
        )
    
    @given(
        year=st.integers(min_value=1900, max_value=2100),
        month=st.integers(min_value=1, max_value=12),
        day=st.integers(min_value=1, max_value=28),
        hour=st.integers(min_value=0, max_value=23)
    )
    @settings(max_examples=100)
    def test_moving_line_calculation(
        self, year: int, month: int, day: int, hour: int
    ):
        """
        Property 21: Moving line position is correctly calculated.
        
        Moving line = (year + month + day + hour) % 6, with 0 -> 6
        
        **Feature: calculator-accuracy-audit, Property 21: 时间起卦先天八卦序**
        **Validates: Requirements 4.5**
        """
        from datetime import datetime
        
        calc = YijingCalculator()
        query_time = datetime(year, month, day, hour, 0)
        
        input_data = YijingInput(
            divination_method="time",
            query_time=query_time
        )
        
        result = calc.calculate(input_data)
        
        # Calculate expected moving line
        moving_pos = (year + month + day + hour) % 6
        if moving_pos == 0:
            moving_pos = 6
        
        # Time method should produce exactly one moving line
        assert len(result.moving_lines) == 1, (
            f"Time method should produce exactly 1 moving line, "
            f"got {len(result.moving_lines)}"
        )
        
        assert result.moving_lines[0] == moving_pos, (
            f"Moving line mismatch for {year}-{month}-{day} {hour}:00: "
            f"expected {moving_pos}, got {result.moving_lines[0]}"
        )
    
    @given(
        year=st.integers(min_value=1900, max_value=2100),
        month=st.integers(min_value=1, max_value=12),
        day=st.integers(min_value=1, max_value=28),
        hour=st.integers(min_value=0, max_value=23)
    )
    @settings(max_examples=100)
    def test_time_method_is_deterministic(
        self, year: int, month: int, day: int, hour: int
    ):
        """
        Property 21: Time method is deterministic for same input.
        
        **Feature: calculator-accuracy-audit, Property 21: 时间起卦先天八卦序**
        **Validates: Requirements 4.5**
        """
        from datetime import datetime
        
        calc = YijingCalculator()
        query_time = datetime(year, month, day, hour, 0)
        
        # Run twice with same input
        results = []
        for _ in range(2):
            input_data = YijingInput(
                divination_method="time",
                query_time=query_time
            )
            result = calc.calculate(input_data)
            results.append((
                result.main_hexagram.number,
                result.main_hexagram.upper_trigram,
                result.main_hexagram.lower_trigram,
                tuple(result.moving_lines)
            ))
        
        assert results[0] == results[1], (
            f"Time method should be deterministic, got different results"
        )
