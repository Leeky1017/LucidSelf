# backend/calculators/yijing/tests/test_probability_audit.py
"""
Probability distribution audit tests for YijingCalculator.

This module audits the probability distributions of the coin and yarrow
divination methods to ensure they match theoretical expectations.

**Feature: calculator-accuracy-audit**
**Validates: Requirements 4.1, 4.2**
"""

import pytest
import random
from collections import Counter
from typing import Dict, List, Tuple

from backend.calculators.yijing import YijingCalculator, YijingInput


# =============================================================================
# Task 4.1: 审计铜钱法概率分布
# =============================================================================

class TestCoinMethodProbabilityAudit:
    """
    Audit the coin method (铜钱法) probability distribution.
    
    Theoretical probabilities:
    - 6 (老阴, 2+2+2): 1/8 = 0.125
    - 7 (少阳, 2+2+3 combinations): 3/8 = 0.375
    - 8 (少阴, 2+3+3 combinations): 3/8 = 0.375
    - 9 (老阳, 3+3+3): 1/8 = 0.125
    
    _Requirements: 4.1_
    """
    
    THEORETICAL_PROBABILITIES = {
        6: 1/8,   # 老阴: 0.125
        7: 3/8,   # 少阳: 0.375
        8: 3/8,   # 少阴: 0.375
        9: 1/8,   # 老阳: 0.125
    }
    
    def _run_coin_method_trials(self, num_trials: int = 10000, seed: int = 42) -> Counter:
        """
        Run multiple coin method trials and count line value occurrences.
        
        Args:
            num_trials: Number of hexagrams to generate
            seed: Random seed for reproducibility
            
        Returns:
            Counter of line values (6, 7, 8, 9)
        """
        random.seed(seed)
        calc = YijingCalculator()
        
        line_counts = Counter()
        
        for _ in range(num_trials):
            input_data = YijingInput(divination_method="coin")
            result = calc.calculate(input_data)
            
            # Count each line value from raw_lines
            if result.main_hexagram.raw_lines:
                for line in result.main_hexagram.raw_lines:
                    line_counts[line] += 1
        
        return line_counts
    
    def _calculate_observed_probabilities(self, counts: Counter) -> Dict[int, float]:
        """Calculate observed probabilities from counts."""
        total = sum(counts.values())
        return {value: count / total for value, count in counts.items()}
    
    def test_coin_method_probability_distribution(self):
        """
        Audit: Verify coin method produces correct probability distribution.
        
        Runs 10000+ trials and verifies each line type's frequency
        is within acceptable tolerance of theoretical probability.
        
        _Requirements: 4.1_
        """
        # Run 10000 hexagrams = 60000 individual lines
        num_trials = 10000
        counts = self._run_coin_method_trials(num_trials=num_trials)
        observed = self._calculate_observed_probabilities(counts)
        
        total_lines = sum(counts.values())
        print(f"\n=== Coin Method Probability Audit ===")
        print(f"Total lines generated: {total_lines}")
        print(f"\nLine Value | Count  | Observed | Expected | Deviation")
        print("-" * 60)
        
        max_deviation = 0.0
        for value in [6, 7, 8, 9]:
            expected = self.THEORETICAL_PROBABILITIES[value]
            obs = observed.get(value, 0)
            deviation = abs(obs - expected)
            max_deviation = max(max_deviation, deviation)
            
            line_name = {6: "老阴", 7: "少阳", 8: "少阴", 9: "老阳"}[value]
            print(f"  {value} ({line_name}) | {counts[value]:6d} | {obs:.4f}   | {expected:.4f}   | {deviation:.4f}")
        
        print(f"\nMax deviation: {max_deviation:.4f}")
        print(f"Tolerance: 0.05 (5%)")
        
        # Verify all probabilities are within 5% tolerance
        for value in [6, 7, 8, 9]:
            expected = self.THEORETICAL_PROBABILITIES[value]
            obs = observed.get(value, 0)
            deviation = abs(obs - expected)
            
            assert deviation < 0.05, (
                f"Coin method probability for {value} deviates too much: "
                f"observed={obs:.4f}, expected={expected:.4f}, deviation={deviation:.4f}"
            )
        
        print("\n✓ All probabilities within tolerance")
    
    def test_coin_method_implementation_correctness(self):
        """
        Verify the coin method implementation logic is correct.
        
        Each coin toss should be 2 (tails) or 3 (heads) with equal probability.
        Sum of 3 coins gives values 6, 7, 8, or 9.
        """
        # Test that the implementation uses correct coin values
        calc = YijingCalculator()
        
        # Run many single-line generations to verify coin logic
        random.seed(12345)
        
        # Directly test the _coin_method
        all_lines = []
        for _ in range(1000):
            lines = calc._coin_method()
            all_lines.extend(lines)
        
        # All values should be 6, 7, 8, or 9
        for line in all_lines:
            assert line in {6, 7, 8, 9}, f"Invalid line value: {line}"
        
        # Count distribution
        counts = Counter(all_lines)
        total = len(all_lines)
        
        # Verify rough distribution (with wider tolerance for smaller sample)
        for value, expected_prob in self.THEORETICAL_PROBABILITIES.items():
            observed_prob = counts[value] / total
            assert abs(observed_prob - expected_prob) < 0.1, (
                f"Line value {value}: observed={observed_prob:.3f}, expected={expected_prob:.3f}"
            )


# =============================================================================
# Task 4.3: 审计蓍草法概率分布
# =============================================================================

class TestYarrowMethodProbabilityAudit:
    """
    Audit the yarrow stalk method (蓍草法) probability distribution.
    
    Theoretical probabilities:
    - 6 (老阴): 1/16 = 0.0625
    - 7 (少阳): 5/16 = 0.3125
    - 8 (少阴): 7/16 = 0.4375
    - 9 (老阳): 3/16 = 0.1875
    
    _Requirements: 4.2_
    """
    
    THEORETICAL_PROBABILITIES = {
        6: 1/16,   # 老阴: 0.0625
        7: 5/16,   # 少阳: 0.3125
        8: 7/16,   # 少阴: 0.4375
        9: 3/16,   # 老阳: 0.1875
    }
    
    def _run_yarrow_method_trials(self, num_trials: int = 10000, seed: int = 42) -> Counter:
        """
        Run multiple yarrow method trials and count line value occurrences.
        
        Args:
            num_trials: Number of hexagrams to generate
            seed: Random seed for reproducibility
            
        Returns:
            Counter of line values (6, 7, 8, 9)
        """
        random.seed(seed)
        calc = YijingCalculator()
        
        line_counts = Counter()
        
        for _ in range(num_trials):
            input_data = YijingInput(divination_method="yarrow")
            result = calc.calculate(input_data)
            
            # Count each line value from raw_lines
            if result.main_hexagram.raw_lines:
                for line in result.main_hexagram.raw_lines:
                    line_counts[line] += 1
        
        return line_counts
    
    def _calculate_observed_probabilities(self, counts: Counter) -> Dict[int, float]:
        """Calculate observed probabilities from counts."""
        total = sum(counts.values())
        return {value: count / total for value, count in counts.items()}
    
    def test_yarrow_method_probability_distribution(self):
        """
        Audit: Verify yarrow method produces correct probability distribution.
        
        Runs 10000+ trials and verifies each line type's frequency
        is within acceptable tolerance of theoretical probability.
        
        _Requirements: 4.2_
        """
        # Run 10000 hexagrams = 60000 individual lines
        num_trials = 10000
        counts = self._run_yarrow_method_trials(num_trials=num_trials)
        observed = self._calculate_observed_probabilities(counts)
        
        total_lines = sum(counts.values())
        print(f"\n=== Yarrow Method Probability Audit ===")
        print(f"Total lines generated: {total_lines}")
        print(f"\nLine Value | Count  | Observed | Expected | Deviation")
        print("-" * 60)
        
        max_deviation = 0.0
        for value in [6, 7, 8, 9]:
            expected = self.THEORETICAL_PROBABILITIES[value]
            obs = observed.get(value, 0)
            deviation = abs(obs - expected)
            max_deviation = max(max_deviation, deviation)
            
            line_name = {6: "老阴", 7: "少阳", 8: "少阴", 9: "老阳"}[value]
            print(f"  {value} ({line_name}) | {counts[value]:6d} | {obs:.4f}   | {expected:.4f}   | {deviation:.4f}")
        
        print(f"\nMax deviation: {max_deviation:.4f}")
        print(f"Tolerance: 0.05 (5%)")
        
        # Verify all probabilities are within 5% tolerance
        for value in [6, 7, 8, 9]:
            expected = self.THEORETICAL_PROBABILITIES[value]
            obs = observed.get(value, 0)
            deviation = abs(obs - expected)
            
            assert deviation < 0.05, (
                f"Yarrow method probability for {value} deviates too much: "
                f"observed={obs:.4f}, expected={expected:.4f}, deviation={deviation:.4f}"
            )
        
        print("\n✓ All probabilities within tolerance")
    
    def test_yarrow_method_implementation_correctness(self):
        """
        Verify the yarrow method implementation logic is correct.
        
        The implementation should use cumulative probability thresholds:
        - r < 1/16: 6 (老阴)
        - r < 6/16: 7 (少阳)
        - r < 13/16: 8 (少阴)
        - r >= 13/16: 9 (老阳)
        """
        calc = YijingCalculator()
        
        # Run many single-line generations
        random.seed(54321)
        
        all_lines = []
        for _ in range(1000):
            lines = calc._yarrow_method()
            all_lines.extend(lines)
        
        # All values should be 6, 7, 8, or 9
        for line in all_lines:
            assert line in {6, 7, 8, 9}, f"Invalid line value: {line}"
        
        # Count distribution
        counts = Counter(all_lines)
        total = len(all_lines)
        
        # Verify rough distribution (with wider tolerance for smaller sample)
        for value, expected_prob in self.THEORETICAL_PROBABILITIES.items():
            observed_prob = counts[value] / total
            assert abs(observed_prob - expected_prob) < 0.1, (
                f"Line value {value}: observed={observed_prob:.3f}, expected={expected_prob:.3f}"
            )


# =============================================================================
# Combined Audit Report
# =============================================================================

class TestProbabilityAuditReport:
    """Generate a combined audit report for both methods."""
    
    def test_generate_audit_report(self):
        """
        Generate a comprehensive audit report comparing both methods.
        """
        random.seed(42)
        calc = YijingCalculator()
        
        # Run trials for both methods
        coin_counts = Counter()
        yarrow_counts = Counter()
        
        num_trials = 5000
        
        for _ in range(num_trials):
            # Coin method
            coin_result = calc.calculate(YijingInput(divination_method="coin"))
            if coin_result.main_hexagram.raw_lines:
                for line in coin_result.main_hexagram.raw_lines:
                    coin_counts[line] += 1
            
            # Yarrow method
            yarrow_result = calc.calculate(YijingInput(divination_method="yarrow"))
            if yarrow_result.main_hexagram.raw_lines:
                for line in yarrow_result.main_hexagram.raw_lines:
                    yarrow_counts[line] += 1
        
        print("\n" + "=" * 70)
        print("YIJING CALCULATOR PROBABILITY AUDIT REPORT")
        print("=" * 70)
        
        print("\n--- Coin Method (铜钱法) ---")
        coin_total = sum(coin_counts.values())
        print(f"Total lines: {coin_total}")
        
        coin_expected = {6: 1/8, 7: 3/8, 8: 3/8, 9: 1/8}
        for value in [6, 7, 8, 9]:
            obs = coin_counts[value] / coin_total
            exp = coin_expected[value]
            status = "✓" if abs(obs - exp) < 0.05 else "✗"
            print(f"  {value}: {obs:.4f} (expected {exp:.4f}) {status}")
        
        print("\n--- Yarrow Method (蓍草法) ---")
        yarrow_total = sum(yarrow_counts.values())
        print(f"Total lines: {yarrow_total}")
        
        yarrow_expected = {6: 1/16, 7: 5/16, 8: 7/16, 9: 3/16}
        for value in [6, 7, 8, 9]:
            obs = yarrow_counts[value] / yarrow_total
            exp = yarrow_expected[value]
            status = "✓" if abs(obs - exp) < 0.05 else "✗"
            print(f"  {value}: {obs:.4f} (expected {exp:.4f}) {status}")
        
        print("\n--- Key Differences ---")
        print("Coin method has equal probability for 老阴(6) and 老阳(9): 1/8 each")
        print("Yarrow method favors 少阴(8) and has unequal moving line probabilities")
        print("  - 老阴(6): 1/16 (rarer)")
        print("  - 老阳(9): 3/16 (more common)")
        
        print("\n" + "=" * 70)


# =============================================================================
# Task 4.5: 审计互卦计算
# =============================================================================

class TestMutualHexagramAudit:
    """
    Audit the mutual hexagram (互卦) calculation.
    
    Mutual hexagram is formed by:
    - Lower trigram: lines 2, 3, 4 of the original hexagram
    - Upper trigram: lines 3, 4, 5 of the original hexagram
    
    _Requirements: 4.3_
    """
    
    def _get_all_64_hexagram_lines(self) -> List[Tuple[int, List[int]]]:
        """
        Generate all 64 hexagram line combinations.
        
        Returns list of (hexagram_number, binary_lines) tuples.
        """
        from backend.calculators.yijing.models import TRIGRAM_DATA
        
        trigrams = ["乾", "坤", "震", "巽", "坎", "离", "艮", "兑"]
        hexagrams = []
        
        for i, upper in enumerate(trigrams):
            for j, lower in enumerate(trigrams):
                # Get trigram lines
                upper_lines = list(TRIGRAM_DATA[upper]["lines"])
                lower_lines = list(TRIGRAM_DATA[lower]["lines"])
                
                # Combine: lower first (1-3), then upper (4-6)
                binary_lines = lower_lines + upper_lines
                
                # Calculate hexagram number (simplified, not King Wen sequence)
                hex_num = i * 8 + j + 1
                
                hexagrams.append((hex_num, binary_lines, upper, lower))
        
        return hexagrams
    
    def test_mutual_hexagram_uses_correct_lines(self):
        """
        Audit: Verify mutual hexagram uses lines 2-5 correctly.
        
        For each of the 64 hexagrams, verify that:
        - Mutual lower trigram = lines 2, 3, 4 of original
        - Mutual upper trigram = lines 3, 4, 5 of original
        
        _Requirements: 4.3_
        """
        from backend.calculators.yijing.models import TRIGRAM_DATA, LINES_TO_TRIGRAM
        
        calc = YijingCalculator()
        
        print("\n=== Mutual Hexagram Audit ===")
        print("Verifying all 64 hexagrams...")
        
        errors = []
        
        for hex_num, binary_lines, upper, lower in self._get_all_64_hexagram_lines():
            # Calculate expected mutual hexagram lines
            expected_mutual_lower = tuple(binary_lines[1:4])  # lines 2, 3, 4 (0-indexed: 1, 2, 3)
            expected_mutual_upper = tuple(binary_lines[2:5])  # lines 3, 4, 5 (0-indexed: 2, 3, 4)
            
            # Get expected trigram names
            expected_lower_trigram = LINES_TO_TRIGRAM.get(expected_mutual_lower)
            expected_upper_trigram = LINES_TO_TRIGRAM.get(expected_mutual_upper)
            
            # Create input with static lines (7 for yang, 8 for yin)
            raw_lines = [7 if line == 1 else 8 for line in binary_lines]
            
            input_data = YijingInput(
                divination_method="manual",
                manual_lines=raw_lines
            )
            
            result = calc.calculate(input_data)
            
            # Verify mutual hexagram trigrams
            actual_lower = result.mutual_hexagram.lower_trigram
            actual_upper = result.mutual_hexagram.upper_trigram
            
            if actual_lower != expected_lower_trigram:
                errors.append(
                    f"Hexagram {hex_num} ({upper}/{lower}): "
                    f"mutual lower trigram mismatch - "
                    f"expected {expected_lower_trigram}, got {actual_lower}"
                )
            
            if actual_upper != expected_upper_trigram:
                errors.append(
                    f"Hexagram {hex_num} ({upper}/{lower}): "
                    f"mutual upper trigram mismatch - "
                    f"expected {expected_upper_trigram}, got {actual_upper}"
                )
        
        if errors:
            print(f"\n❌ Found {len(errors)} errors:")
            for error in errors[:10]:  # Show first 10 errors
                print(f"  - {error}")
            if len(errors) > 10:
                print(f"  ... and {len(errors) - 10} more errors")
            pytest.fail(f"Mutual hexagram calculation has {len(errors)} errors")
        else:
            print(f"\n✓ All 64 hexagrams have correct mutual hexagram calculation")
    
    def test_mutual_hexagram_specific_examples(self):
        """
        Audit: Verify specific known mutual hexagram examples.
        
        Examples:
        - 乾 (111111) -> 互卦 = 乾 (lines 2-5 are all yang)
        - 坤 (000000) -> 互卦 = 坤 (lines 2-5 are all yin)
        - 泰 (111000) -> 互卦 = 归妹 (震/兑)
        
        _Requirements: 4.3_
        """
        calc = YijingCalculator()
        
        test_cases = [
            # (name, raw_lines, expected_mutual_upper, expected_mutual_lower)
            ("乾", [7, 7, 7, 7, 7, 7], "乾", "乾"),  # All yang -> mutual is also 乾
            ("坤", [8, 8, 8, 8, 8, 8], "坤", "坤"),  # All yin -> mutual is also 坤
            # 泰 = 坤上乾下 = 000111 (lines 1-6)
            # Mutual: lower = lines 2,3,4 = 001 = 震, upper = lines 3,4,5 = 010 = 坎
            # Wait, let me recalculate...
            # 泰 lines (bottom to top): 1,1,1,0,0,0
            # Mutual lower = lines 2,3,4 = 1,1,0 = 巽
            # Mutual upper = lines 3,4,5 = 1,0,0 = 艮
            ("泰", [7, 7, 7, 8, 8, 8], "艮", "巽"),
        ]
        
        print("\n=== Specific Mutual Hexagram Examples ===")
        
        for name, raw_lines, expected_upper, expected_lower in test_cases:
            input_data = YijingInput(
                divination_method="manual",
                manual_lines=raw_lines
            )
            
            result = calc.calculate(input_data)
            
            print(f"\n{name}: lines={raw_lines}")
            print(f"  Main hexagram: {result.main_hexagram.upper_trigram}/{result.main_hexagram.lower_trigram}")
            print(f"  Mutual hexagram: {result.mutual_hexagram.upper_trigram}/{result.mutual_hexagram.lower_trigram}")
            print(f"  Expected: {expected_upper}/{expected_lower}")
            
            assert result.mutual_hexagram.upper_trigram == expected_upper, (
                f"{name}: mutual upper trigram mismatch - "
                f"expected {expected_upper}, got {result.mutual_hexagram.upper_trigram}"
            )
            assert result.mutual_hexagram.lower_trigram == expected_lower, (
                f"{name}: mutual lower trigram mismatch - "
                f"expected {expected_lower}, got {result.mutual_hexagram.lower_trigram}"
            )
        
        print("\n✓ All specific examples verified")


# =============================================================================
# Task 4.7: 审计变卦计算
# =============================================================================

class TestChangedHexagramAudit:
    """
    Audit the changed hexagram (变卦) calculation.
    
    Rules:
    - 老阴 (6) changes to yang (1)
    - 老阳 (9) changes to yin (0)
    - 少阴 (8) stays yin (0)
    - 少阳 (7) stays yang (1)
    
    _Requirements: 4.4_
    """
    
    def test_old_yin_changes_to_yang(self):
        """
        Audit: Verify 老阴 (6) changes to yang in changed hexagram.
        
        _Requirements: 4.4_
        """
        calc = YijingCalculator()
        
        # Create hexagram with 老阴 at position 1
        # All other lines are static yang (7)
        raw_lines = [6, 7, 7, 7, 7, 7]  # 老阴 at line 1
        
        input_data = YijingInput(
            divination_method="manual",
            manual_lines=raw_lines
        )
        
        result = calc.calculate(input_data)
        
        # Main hexagram line 1 should be yin (0)
        assert result.main_hexagram.lines[0] == 0, (
            f"Main hexagram line 1 should be yin (0), got {result.main_hexagram.lines[0]}"
        )
        
        # Changed hexagram line 1 should be yang (1)
        assert result.changed_hexagram is not None, "Changed hexagram should exist"
        assert result.changed_hexagram.lines[0] == 1, (
            f"Changed hexagram line 1 should be yang (1), got {result.changed_hexagram.lines[0]}"
        )
        
        # Moving lines should include position 1
        assert 1 in result.moving_lines, f"Moving lines should include 1, got {result.moving_lines}"
        
        print("✓ 老阴 (6) correctly changes to yang")
    
    def test_old_yang_changes_to_yin(self):
        """
        Audit: Verify 老阳 (9) changes to yin in changed hexagram.
        
        _Requirements: 4.4_
        """
        calc = YijingCalculator()
        
        # Create hexagram with 老阳 at position 1
        # All other lines are static yin (8)
        raw_lines = [9, 8, 8, 8, 8, 8]  # 老阳 at line 1
        
        input_data = YijingInput(
            divination_method="manual",
            manual_lines=raw_lines
        )
        
        result = calc.calculate(input_data)
        
        # Main hexagram line 1 should be yang (1)
        assert result.main_hexagram.lines[0] == 1, (
            f"Main hexagram line 1 should be yang (1), got {result.main_hexagram.lines[0]}"
        )
        
        # Changed hexagram line 1 should be yin (0)
        assert result.changed_hexagram is not None, "Changed hexagram should exist"
        assert result.changed_hexagram.lines[0] == 0, (
            f"Changed hexagram line 1 should be yin (0), got {result.changed_hexagram.lines[0]}"
        )
        
        # Moving lines should include position 1
        assert 1 in result.moving_lines, f"Moving lines should include 1, got {result.moving_lines}"
        
        print("✓ 老阳 (9) correctly changes to yin")
    
    def test_all_moving_line_combinations(self):
        """
        Audit: Verify all combinations of moving lines work correctly.
        
        _Requirements: 4.4_
        """
        calc = YijingCalculator()
        
        print("\n=== Changed Hexagram Audit ===")
        
        # Test each position with 老阴 and 老阳
        for pos in range(6):
            for moving_value in [6, 9]:
                # Create lines with one moving line
                raw_lines = [7] * 6  # All static yang
                raw_lines[pos] = moving_value
                
                input_data = YijingInput(
                    divination_method="manual",
                    manual_lines=raw_lines
                )
                
                result = calc.calculate(input_data)
                
                # Verify moving line is detected
                assert (pos + 1) in result.moving_lines, (
                    f"Position {pos + 1} with value {moving_value} should be moving"
                )
                
                # Verify changed hexagram exists
                assert result.changed_hexagram is not None, (
                    f"Changed hexagram should exist for moving line at position {pos + 1}"
                )
                
                # Verify the line changed correctly
                main_line = result.main_hexagram.lines[pos]
                changed_line = result.changed_hexagram.lines[pos]
                
                if moving_value == 6:  # 老阴 -> yang
                    assert main_line == 0, f"老阴 should be yin in main hexagram"
                    assert changed_line == 1, f"老阴 should change to yang"
                else:  # 老阳 -> yin
                    assert main_line == 1, f"老阳 should be yang in main hexagram"
                    assert changed_line == 0, f"老阳 should change to yin"
        
        print("✓ All moving line positions and values work correctly")
    
    def test_multiple_moving_lines(self):
        """
        Audit: Verify multiple moving lines are handled correctly.
        
        _Requirements: 4.4_
        """
        calc = YijingCalculator()
        
        # Create hexagram with multiple moving lines
        # 老阴 at positions 1, 3, 5 and 老阳 at positions 2, 4, 6
        raw_lines = [6, 9, 6, 9, 6, 9]
        
        input_data = YijingInput(
            divination_method="manual",
            manual_lines=raw_lines
        )
        
        result = calc.calculate(input_data)
        
        # All 6 lines should be moving
        assert result.moving_lines == [1, 2, 3, 4, 5, 6], (
            f"All 6 lines should be moving, got {result.moving_lines}"
        )
        
        # Verify each line changed correctly
        for i, (main, changed, raw) in enumerate(zip(
            result.main_hexagram.lines,
            result.changed_hexagram.lines,
            raw_lines
        )):
            if raw == 6:  # 老阴
                assert main == 0 and changed == 1, (
                    f"Line {i+1}: 老阴 should be 0->1, got {main}->{changed}"
                )
            else:  # 老阳
                assert main == 1 and changed == 0, (
                    f"Line {i+1}: 老阳 should be 1->0, got {main}->{changed}"
                )
        
        print("✓ Multiple moving lines handled correctly")


# =============================================================================
# Task 4.9: 审计时间起卦
# =============================================================================

class TestTimeMethodAudit:
    """
    Audit the time-based divination method (时间起卦).
    
    Uses 先天八卦序 (Pre-Heaven/Fu Xi sequence):
    1=乾, 2=兑, 3=离, 4=震, 5=巽, 6=坎, 7=艮, 8=坤
    
    Calculation:
    - Upper trigram: (year + month + day) % 8
    - Lower trigram: (year + month + day + hour) % 8
    - Moving line: (year + month + day + hour) % 6 + 1
    
    _Requirements: 4.5_
    """
    
    # 先天八卦序 (Pre-Heaven sequence)
    XIANTIAN_SEQUENCE = ["乾", "兑", "离", "震", "巽", "坎", "艮", "坤"]
    
    def test_xiantian_sequence_mapping(self):
        """
        Audit: Verify the 先天八卦序 mapping is correct.
        
        _Requirements: 4.5_
        """
        from backend.calculators.yijing.calculator import YijingCalculator
        
        # The calculator should use this sequence
        expected_sequence = ["乾", "兑", "离", "震", "巽", "坎", "艮", "坤"]
        
        # Verify by checking the _time_method implementation
        calc = YijingCalculator()
        
        # Test specific datetime values that should produce known trigrams
        test_cases = [
            # (year, month, day, hour, expected_upper_num, expected_lower_num)
            (2000, 1, 1, 0, (2000+1+1) % 8, (2000+1+1+0) % 8),
            (2025, 11, 29, 14, (2025+11+29) % 8, (2025+11+29+14) % 8),
        ]
        
        print("\n=== Time Method 先天八卦序 Audit ===")
        
        for year, month, day, hour, expected_upper_num, expected_lower_num in test_cases:
            from datetime import datetime
            
            # Adjust for 0 -> 8 mapping
            if expected_upper_num == 0:
                expected_upper_num = 8
            if expected_lower_num == 0:
                expected_lower_num = 8
            
            expected_upper = expected_sequence[expected_upper_num - 1]
            expected_lower = expected_sequence[expected_lower_num - 1]
            
            query_time = datetime(year, month, day, hour, 0)
            input_data = YijingInput(
                divination_method="time",
                query_time=query_time
            )
            
            result = calc.calculate(input_data)
            
            print(f"\nDatetime: {year}-{month:02d}-{day:02d} {hour:02d}:00")
            print(f"  Upper calc: ({year}+{month}+{day}) % 8 = {(year+month+day) % 8} -> {expected_upper}")
            print(f"  Lower calc: ({year}+{month}+{day}+{hour}) % 8 = {(year+month+day+hour) % 8} -> {expected_lower}")
            print(f"  Result: {result.main_hexagram.upper_trigram}/{result.main_hexagram.lower_trigram}")
            
            assert result.main_hexagram.upper_trigram == expected_upper, (
                f"Upper trigram mismatch: expected {expected_upper}, "
                f"got {result.main_hexagram.upper_trigram}"
            )
            assert result.main_hexagram.lower_trigram == expected_lower, (
                f"Lower trigram mismatch: expected {expected_lower}, "
                f"got {result.main_hexagram.lower_trigram}"
            )
        
        print("\n✓ 先天八卦序 mapping verified")
    
    def test_moving_line_calculation(self):
        """
        Audit: Verify moving line position calculation.
        
        Moving line = (year + month + day + hour) % 6
        If result is 0, use 6.
        
        _Requirements: 4.5_
        """
        from datetime import datetime
        
        calc = YijingCalculator()
        
        print("\n=== Time Method Moving Line Audit ===")
        
        # Calculate expected values correctly
        # (2000+1+1+0) % 6 = 2002 % 6 = 4
        # (2000+1+1+1) % 6 = 2003 % 6 = 5
        # (2000+1+1+2) % 6 = 2004 % 6 = 0 -> 6
        # (2025+11+29+14) % 6 = 2079 % 6 = 3
        test_cases = [
            # (year, month, day, hour, expected_moving_line)
            (2000, 1, 1, 0, 4),  # (2000+1+1+0) % 6 = 4
            (2000, 1, 1, 1, 5),  # (2000+1+1+1) % 6 = 5
            (2000, 1, 1, 2, 6),  # (2000+1+1+2) % 6 = 0 -> 6
            (2025, 11, 29, 14, 3),  # (2025+11+29+14) % 6 = 3
        ]
        
        for year, month, day, hour, expected_moving in test_cases:
            query_time = datetime(year, month, day, hour, 0)
            input_data = YijingInput(
                divination_method="time",
                query_time=query_time
            )
            
            result = calc.calculate(input_data)
            
            # Time method should produce exactly one moving line
            assert len(result.moving_lines) == 1, (
                f"Time method should produce exactly 1 moving line, "
                f"got {len(result.moving_lines)}: {result.moving_lines}"
            )
            
            actual_moving = result.moving_lines[0]
            
            print(f"Datetime: {year}-{month:02d}-{day:02d} {hour:02d}:00")
            print(f"  Moving line calc: ({year}+{month}+{day}+{hour}) % 6 = {(year+month+day+hour) % 6}")
            print(f"  Expected: {expected_moving}, Actual: {actual_moving}")
            
            assert actual_moving == expected_moving, (
                f"Moving line mismatch: expected {expected_moving}, got {actual_moving}"
            )
        
        print("\n✓ Moving line calculation verified")
    
    def test_time_method_deterministic(self):
        """
        Audit: Verify time method is deterministic for same input.
        
        _Requirements: 4.5_
        """
        from datetime import datetime
        
        calc = YijingCalculator()
        
        query_time = datetime(2025, 11, 29, 14, 30)
        
        results = []
        for _ in range(10):
            input_data = YijingInput(
                divination_method="time",
                query_time=query_time
            )
            result = calc.calculate(input_data)
            results.append((
                result.main_hexagram.number,
                result.main_hexagram.upper_trigram,
                result.main_hexagram.lower_trigram,
                result.moving_lines
            ))
        
        # All results should be identical
        assert all(r == results[0] for r in results), (
            f"Time method should be deterministic, got different results: {results}"
        )
        
        print("✓ Time method is deterministic")
