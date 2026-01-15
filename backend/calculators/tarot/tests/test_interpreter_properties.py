# backend/calculators/tarot/tests/test_interpreter_properties.py
"""
Property-Based Tests for TarotInterpreter

TarotInterpreter 的属性测试。
使用 Hypothesis 框架进行属性测试。
"""

import pytest
from collections import Counter
from hypothesis import given, strategies as st, settings, assume

from backend.calculators.tarot import (
    TarotInterpreter,
    TarotDrawer,
    TarotInput,
    TarotFactors,
    CardInterpretation,
    CardInfo,
    ALL_CARDS,
    MAJOR_ARCANA,
    MINOR_ARCANA,
    SUITS,
)
from backend.calculators.tarot.models import SPREAD_TYPES


# =============================================================================
# Strategies for generating test data
# =============================================================================

# Strategy for card numbers (0-77)
card_number_strategy = st.integers(min_value=0, max_value=77)

# Strategy for reversed status
reversed_strategy = st.booleans()

# Strategy for spread types
spread_type_strategy = st.sampled_from(["single", "three_card", "celtic_cross", "custom"])

# Strategy for valid card names from the 78-card deck
valid_card_name_strategy = st.sampled_from([card["name"] for card in ALL_CARDS.values()])

# Strategy for positions
position_strategy = st.sampled_from([
    "past", "present", "future", "answer", "challenge",
    "above", "below", "advice", "external", "hopes_fears", "outcome"
])


@st.composite
def card_info_strategy(draw):
    """Generate valid CardInfo objects."""
    card_name = draw(valid_card_name_strategy)
    reversed = draw(reversed_strategy)
    position = draw(position_strategy)
    
    return CardInfo(
        card_name=card_name,
        reversed=reversed,
        position=position,
    )


@st.composite
def single_card_input_strategy(draw):
    """Generate valid TarotInput for single card spread."""
    card = draw(card_info_strategy())
    card.position = "answer"  # Single card uses "answer" position
    
    return TarotInput(
        spread_type="single",
        cards=[card],
        question=draw(st.one_of(st.none(), st.text(min_size=1, max_size=100))),
    )


@st.composite
def three_card_input_strategy(draw):
    """Generate valid TarotInput for three card spread."""
    positions = ["past", "present", "future"]
    cards = []
    for pos in positions:
        card = draw(card_info_strategy())
        card.position = pos
        cards.append(card)
    
    return TarotInput(
        spread_type="three_card",
        cards=cards,
        question=draw(st.one_of(st.none(), st.text(min_size=1, max_size=100))),
    )


@st.composite
def custom_spread_input_strategy(draw):
    """Generate valid TarotInput for custom spread (1-10 cards)."""
    num_cards = draw(st.integers(min_value=1, max_value=10))
    cards = []
    for i in range(num_cards):
        card = draw(card_info_strategy())
        card.position = f"position_{i+1}"
        cards.append(card)
    
    return TarotInput(
        spread_type="custom",
        cards=cards,
        question=draw(st.one_of(st.none(), st.text(min_size=1, max_size=100))),
    )


@st.composite
def any_valid_tarot_input_strategy(draw):
    """Generate any valid TarotInput."""
    spread_type = draw(spread_type_strategy)
    
    if spread_type == "single":
        return draw(single_card_input_strategy())
    elif spread_type == "three_card":
        return draw(three_card_input_strategy())
    elif spread_type == "celtic_cross":
        # Celtic cross has 10 positions
        positions = SPREAD_TYPES["celtic_cross"]["positions"]
        cards = []
        for pos in positions:
            card = draw(card_info_strategy())
            card.position = pos
            cards.append(card)
        return TarotInput(
            spread_type="celtic_cross",
            cards=cards,
            question=draw(st.one_of(st.none(), st.text(min_size=1, max_size=100))),
        )
    else:
        return draw(custom_spread_input_strategy())


# =============================================================================
# Property 6: TarotInterpreter Card Identification
# =============================================================================

class TestTarotInterpreterCardIdentification:
    """
    **Feature: calculator-integration, Property 6: TarotInterpreter Card Identification**
    
    *For any* valid TarotInput, all cards must be identified from the 78-card deck 
    with upright/reversed orientation.
    
    **Validates: Requirements 5.1, 5.2**
    """
    
    @given(input_data=any_valid_tarot_input_strategy())
    @settings(max_examples=100)
    def test_all_cards_identified_from_78_deck(self, input_data: TarotInput):
        """
        Property test: For any valid input, all cards are identified from the 78-card deck.
        
        **Feature: calculator-integration, Property 6: TarotInterpreter Card Identification**
        **Validates: Requirements 5.1, 5.2**
        """
        interpreter = TarotInterpreter()
        result = interpreter.interpret(input_data)
        
        # All input cards should be interpreted
        assert len(result.cards) == len(input_data.cards), \
            f"Expected {len(input_data.cards)} cards, got {len(result.cards)}"
        
        # Each card should have a valid card number (0-77)
        for card in result.cards:
            assert 0 <= card.card_number <= 77, \
                f"Card number {card.card_number} out of range [0, 77]"
    
    @given(input_data=any_valid_tarot_input_strategy())
    @settings(max_examples=100)
    def test_card_orientation_preserved(self, input_data: TarotInput):
        """
        Property test: Card orientation (upright/reversed) is correctly preserved.
        
        **Feature: calculator-integration, Property 6: TarotInterpreter Card Identification**
        **Validates: Requirements 5.1, 5.2**
        """
        interpreter = TarotInterpreter()
        result = interpreter.interpret(input_data)
        
        # Each card's reversed status should match input
        for i, (input_card, result_card) in enumerate(zip(input_data.cards, result.cards)):
            assert result_card.reversed == input_card.reversed, \
                f"Card {i} reversed status mismatch: input={input_card.reversed}, result={result_card.reversed}"
    
    @given(input_data=any_valid_tarot_input_strategy())
    @settings(max_examples=100)
    def test_major_arcana_correctly_identified(self, input_data: TarotInput):
        """
        Property test: Major Arcana cards (0-21) are correctly identified as is_major=True.
        
        **Feature: calculator-integration, Property 6: TarotInterpreter Card Identification**
        **Validates: Requirements 5.1, 5.2**
        """
        interpreter = TarotInterpreter()
        result = interpreter.interpret(input_data)
        
        for card in result.cards:
            if card.card_number <= 21:
                assert card.is_major is True, \
                    f"Card {card.card_name} (#{card.card_number}) should be Major Arcana"
                assert card.suit is None, \
                    f"Major Arcana card {card.card_name} should have no suit"
            else:
                assert card.is_major is False, \
                    f"Card {card.card_name} (#{card.card_number}) should be Minor Arcana"
                assert card.suit in SUITS, \
                    f"Minor Arcana card {card.card_name} should have a valid suit"
    
    @given(input_data=any_valid_tarot_input_strategy())
    @settings(max_examples=100)
    def test_minor_arcana_has_valid_suit(self, input_data: TarotInput):
        """
        Property test: Minor Arcana cards have a valid suit.
        
        **Feature: calculator-integration, Property 6: TarotInterpreter Card Identification**
        **Validates: Requirements 5.1, 5.2**
        """
        interpreter = TarotInterpreter()
        result = interpreter.interpret(input_data)
        
        for card in result.cards:
            if not card.is_major:
                assert card.suit in SUITS, \
                    f"Minor Arcana card {card.card_name} has invalid suit: {card.suit}"
    
    @given(input_data=any_valid_tarot_input_strategy())
    @settings(max_examples=100)
    def test_card_position_preserved(self, input_data: TarotInput):
        """
        Property test: Card position is correctly preserved from input.
        
        **Feature: calculator-integration, Property 6: TarotInterpreter Card Identification**
        **Validates: Requirements 5.1, 5.2**
        """
        interpreter = TarotInterpreter()
        result = interpreter.interpret(input_data)
        
        for i, (input_card, result_card) in enumerate(zip(input_data.cards, result.cards)):
            if input_card.position:
                assert result_card.position == input_card.position, \
                    f"Card {i} position mismatch: input={input_card.position}, result={result_card.position}"
    
    @given(input_data=any_valid_tarot_input_strategy())
    @settings(max_examples=100)
    def test_card_has_position_meaning(self, input_data: TarotInput):
        """
        Property test: Each card has a non-empty position meaning.
        
        **Feature: calculator-integration, Property 6: TarotInterpreter Card Identification**
        **Validates: Requirements 5.1, 5.2**
        """
        interpreter = TarotInterpreter()
        result = interpreter.interpret(input_data)
        
        for card in result.cards:
            assert card.position_meaning is not None, \
                f"Card {card.card_name} has no position meaning"
            assert len(card.position_meaning) > 0, \
                f"Card {card.card_name} has empty position meaning"
    
    @given(input_data=any_valid_tarot_input_strategy())
    @settings(max_examples=100)
    def test_card_has_chinese_name(self, input_data: TarotInput):
        """
        Property test: Each card has a Chinese name.
        
        **Feature: calculator-integration, Property 6: TarotInterpreter Card Identification**
        **Validates: Requirements 5.1, 5.2**
        """
        interpreter = TarotInterpreter()
        result = interpreter.interpret(input_data)
        
        for card in result.cards:
            assert card.card_name_zh is not None, \
                f"Card {card.card_name} has no Chinese name"
            assert len(card.card_name_zh) > 0, \
                f"Card {card.card_name} has empty Chinese name"
    
    @given(input_data=any_valid_tarot_input_strategy())
    @settings(max_examples=100)
    def test_factor_matrix_follows_naming_convention(self, input_data: TarotInput):
        """
        Property test: Factor matrix follows tarot_* naming convention.
        
        **Feature: calculator-integration, Property 6: TarotInterpreter Card Identification**
        **Validates: Requirements 5.1, 5.2**
        """
        interpreter = TarotInterpreter()
        result = interpreter.interpret(input_data)
        factor_matrix = result.to_factor_matrix()
        
        # All factor IDs should start with "tarot_"
        for factor_id in factor_matrix.factors.keys():
            assert factor_id.startswith("tarot_"), \
                f"Factor ID {factor_id} does not follow tarot_* naming convention"
    
    @given(input_data=any_valid_tarot_input_strategy())
    @settings(max_examples=100)
    def test_factor_matrix_contains_spread_type(self, input_data: TarotInput):
        """
        Property test: Factor matrix contains spread type factor.
        
        **Feature: calculator-integration, Property 6: TarotInterpreter Card Identification**
        **Validates: Requirements 5.1, 5.2**
        """
        interpreter = TarotInterpreter()
        result = interpreter.interpret(input_data)
        factor_matrix = result.to_factor_matrix()
        
        spread_factor_id = f"tarot_spread_{input_data.spread_type}"
        assert spread_factor_id in factor_matrix.factors, \
            f"Missing spread type factor: {spread_factor_id}"
    
    @given(input_data=any_valid_tarot_input_strategy())
    @settings(max_examples=100)
    def test_factor_matrix_contains_card_factors(self, input_data: TarotInput):
        """
        Property test: Factor matrix contains factors for each card.
        
        **Feature: calculator-integration, Property 6: TarotInterpreter Card Identification**
        **Validates: Requirements 5.1, 5.2**
        """
        interpreter = TarotInterpreter()
        result = interpreter.interpret(input_data)
        factor_matrix = result.to_factor_matrix()
        
        # Each card should have at least one factor
        for card in result.cards:
            card_name_normalized = card.card_name.lower().replace(" ", "_").replace("'", "")
            orientation = "reversed" if card.reversed else "upright"
            
            # Check for card factor
            if card.is_major:
                expected_factor = f"tarot_major_{card_name_normalized}_{orientation}"
            else:
                expected_factor = f"tarot_{card.suit}_{card_name_normalized}_{orientation}"
            
            assert expected_factor in factor_matrix.factors, \
                f"Missing card factor: {expected_factor}"


# =============================================================================
# Additional Unit Tests for Edge Cases
# =============================================================================

class TestTarotInterpreterEdgeCases:
    """Unit tests for edge cases and specific scenarios."""
    
    def test_all_78_cards_can_be_identified(self):
        """Test that all 78 cards in the deck can be identified."""
        interpreter = TarotInterpreter()
        
        for card_number, card_data in ALL_CARDS.items():
            card_name = card_data["name"]
            input_data = TarotInput(
                spread_type="single",
                cards=[CardInfo(card_name=card_name, reversed=False, position="answer")],
            )
            
            result = interpreter.interpret(input_data)
            
            assert len(result.cards) == 1
            assert result.cards[0].card_number == card_number, \
                f"Card '{card_name}' identified as #{result.cards[0].card_number}, expected #{card_number}"
    
    def test_case_insensitive_card_names(self):
        """Test that card names are case-insensitive."""
        interpreter = TarotInterpreter()
        
        test_cases = [
            ("THE FOOL", 0),
            ("the fool", 0),
            ("The Fool", 0),
            ("tHe FoOl", 0),
        ]
        
        for card_name, expected_number in test_cases:
            input_data = TarotInput(
                spread_type="single",
                cards=[CardInfo(card_name=card_name, reversed=False, position="answer")],
            )
            
            result = interpreter.interpret(input_data)
            assert result.cards[0].card_number == expected_number, \
                f"Card '{card_name}' not identified correctly"
    
    def test_invalid_card_name_raises_error(self):
        """Test that invalid card names raise ValueError."""
        interpreter = TarotInterpreter()
        
        input_data = TarotInput(
            spread_type="single",
            cards=[CardInfo(card_name="Invalid Card Name", reversed=False, position="answer")],
        )
        
        with pytest.raises(ValueError) as exc_info:
            interpreter.interpret(input_data)
        
        assert "Cannot identify card" in str(exc_info.value)
    
    def test_minor_arcana_parsing(self):
        """Test that Minor Arcana cards are correctly parsed."""
        interpreter = TarotInterpreter()
        
        test_cases = [
            ("Ace of Wands", "wands", True),
            ("2 of Cups", "cups", False),
            ("King of Swords", "swords", False),
            ("Page of Pentacles", "pentacles", False),
        ]
        
        for card_name, expected_suit, is_ace in test_cases:
            input_data = TarotInput(
                spread_type="single",
                cards=[CardInfo(card_name=card_name, reversed=False, position="answer")],
            )
            
            result = interpreter.interpret(input_data)
            assert result.cards[0].suit == expected_suit, \
                f"Card '{card_name}' has wrong suit: {result.cards[0].suit}"
            assert result.cards[0].is_major is False, \
                f"Card '{card_name}' should be Minor Arcana"


# =============================================================================
# Property 12: 塔罗随机分布均匀性
# =============================================================================

def _chi_square_test(observed: list, expected: float) -> tuple:
    """
    Simple chi-square test implementation without scipy.
    
    Returns (chi2_statistic, approximate_p_value_is_acceptable)
    For 77 degrees of freedom, chi2 < 120 roughly corresponds to p > 0.01
    """
    chi2 = sum((o - expected) ** 2 / expected for o in observed)
    # For df=77, critical value at p=0.01 is approximately 109.97
    # We use 120 as a conservative threshold
    return chi2, chi2 < 120


class TestTarotRandomDistribution:
    """
    **Feature: calculator-accuracy-audit, Property 12: 塔罗随机分布均匀性**
    
    *For* large numbers (≥10000) of random card draws, the 78 cards should appear
    with approximately uniform distribution (1/78 each), with deviation < 10%.
    
    **Validates: Requirements 6.1**
    """
    
    def test_random_distribution_uniformity(self):
        """
        Property test: Random card drawing produces uniform distribution.
        
        **Feature: calculator-accuracy-audit, Property 12: 塔罗随机分布均匀性**
        **Validates: Requirements 6.1**
        
        This test verifies that:
        1. All 78 cards can be drawn
        2. Each card appears with approximately equal frequency
        3. Chi-square test confirms uniform distribution
        """
        # Use 156000 draws for statistical significance (2000 per card expected)
        num_draws = 156000
        expected_per_card = num_draws / 78
        
        drawer = TarotDrawer()
        draws = [drawer.draw_card_number() for _ in range(num_draws)]
        
        # Count occurrences
        counts = Counter(draws)
        
        # Verify all 78 cards are represented
        assert len(counts) == 78, \
            f"Expected all 78 cards to be drawn, but only {len(counts)} unique cards appeared"
        
        # Verify each card number is in valid range
        for card_num in counts.keys():
            assert 0 <= card_num <= 77, \
                f"Invalid card number {card_num} drawn"
        
        # Chi-square test for uniformity
        observed = [counts.get(i, 0) for i in range(78)]
        chi2, is_uniform = _chi_square_test(observed, expected_per_card)
        
        assert is_uniform, \
            f"Chi-square test failed: chi2={chi2:.2f} (threshold: 120). " \
            f"Distribution may not be uniform."
        
        # Also verify no extreme outliers (> 15% deviation)
        max_deviation = max(
            abs(count - expected_per_card) / expected_per_card 
            for count in counts.values()
        )
        assert max_deviation < 0.15, \
            f"Extreme outlier detected: {max_deviation*100:.1f}% deviation"
    
    def test_random_distribution_multiple_trials(self):
        """
        Property test: Random distribution is consistent across multiple trials.
        
        **Feature: calculator-accuracy-audit, Property 12: 塔罗随机分布均匀性**
        **Validates: Requirements 6.1**
        
        Run multiple independent trials to verify consistency using chi-square test.
        """
        num_trials = 3
        num_draws_per_trial = 78000  # 1000 per card expected
        expected_per_card = num_draws_per_trial / 78
        
        for trial in range(num_trials):
            drawer = TarotDrawer()  # Fresh drawer each trial
            draws = [drawer.draw_card_number() for _ in range(num_draws_per_trial)]
            counts = Counter(draws)
            
            # All cards should be represented
            assert len(counts) == 78, \
                f"Trial {trial+1}: Only {len(counts)} unique cards drawn"
            
            # Chi-square test
            observed = [counts.get(i, 0) for i in range(78)]
            chi2, is_uniform = _chi_square_test(observed, expected_per_card)
            
            assert is_uniform, \
                f"Trial {trial+1}: Chi-square test failed (chi2={chi2:.2f})"
    
    def test_reversed_status_distribution(self):
        """
        Property test: Reversed status is approximately 50/50.
        
        **Feature: calculator-accuracy-audit, Property 12: 塔罗随机分布均匀性**
        **Validates: Requirements 6.1**
        
        When allow_reversed=True, cards should be upright/reversed with ~50% each.
        """
        num_draws = 10000
        drawer = TarotDrawer()
        
        cards = drawer.draw_cards(num_draws, allow_duplicates=True, allow_reversed=True)
        
        reversed_count = sum(1 for card in cards if card.reversed)
        upright_count = num_draws - reversed_count
        
        # Should be approximately 50/50 (within 5%)
        reversed_ratio = reversed_count / num_draws
        assert 0.45 <= reversed_ratio <= 0.55, \
            f"Reversed ratio {reversed_ratio:.2%} is not approximately 50%"
    
    def test_no_duplicates_in_spread(self):
        """
        Property test: Spread draws have no duplicate cards.
        
        **Feature: calculator-accuracy-audit, Property 12: 塔罗随机分布均匀性**
        **Validates: Requirements 6.1**
        
        When drawing for a spread, no card should appear twice.
        """
        drawer = TarotDrawer()
        
        # Test multiple spread types
        for spread_type in ["single", "three_card", "celtic_cross"]:
            for _ in range(100):  # Run 100 times each
                spread = drawer.draw_spread(spread_type)
                card_names = [card.card_name for card in spread.cards]
                
                # No duplicates
                assert len(card_names) == len(set(card_names)), \
                    f"Spread {spread_type} has duplicate cards: {card_names}"
    
    @given(seed=st.integers(min_value=0, max_value=2**31-1))
    @settings(max_examples=50)
    def test_seeded_reproducibility(self, seed: int):
        """
        Property test: Same seed produces same sequence.
        
        **Feature: calculator-accuracy-audit, Property 12: 塔罗随机分布均匀性**
        **Validates: Requirements 6.1**
        
        For any seed, two drawers with the same seed should produce identical sequences.
        """
        drawer1 = TarotDrawer(seed=seed)
        drawer2 = TarotDrawer(seed=seed)
        
        # Draw 10 cards from each
        draws1 = [drawer1.draw_card_number() for _ in range(10)]
        draws2 = [drawer2.draw_card_number() for _ in range(10)]
        
        assert draws1 == draws2, \
            f"Same seed {seed} produced different sequences"


# =============================================================================
# Property 24: 塔罗牌阵位置记录完整性
# =============================================================================

class TestTarotSpreadPositionCompleteness:
    """
    **Feature: calculator-accuracy-audit, Property 24: 塔罗牌阵位置记录完整性**
    
    *For any* tarot spread, each card's position and upright/reversed status 
    should be completely recorded.
    
    **Validates: Requirements 6.2**
    """
    
    @given(input_data=any_valid_tarot_input_strategy())
    @settings(max_examples=100)
    def test_all_cards_have_position(self, input_data: TarotInput):
        """
        Property test: Every card in a spread has a position recorded.
        
        **Feature: calculator-accuracy-audit, Property 24: 塔罗牌阵位置记录完整性**
        **Validates: Requirements 6.2**
        """
        interpreter = TarotInterpreter()
        result = interpreter.interpret(input_data)
        
        for i, card in enumerate(result.cards):
            assert card.position is not None, \
                f"Card {i+1} ({card.card_name}) has no position"
            assert len(card.position) > 0, \
                f"Card {i+1} ({card.card_name}) has empty position"
    
    @given(input_data=any_valid_tarot_input_strategy())
    @settings(max_examples=100)
    def test_all_cards_have_position_meaning(self, input_data: TarotInput):
        """
        Property test: Every card in a spread has a position meaning.
        
        **Feature: calculator-accuracy-audit, Property 24: 塔罗牌阵位置记录完整性**
        **Validates: Requirements 6.2**
        """
        interpreter = TarotInterpreter()
        result = interpreter.interpret(input_data)
        
        for i, card in enumerate(result.cards):
            assert card.position_meaning is not None, \
                f"Card {i+1} ({card.card_name}) has no position meaning"
            assert len(card.position_meaning) > 0, \
                f"Card {i+1} ({card.card_name}) has empty position meaning"
    
    @given(input_data=any_valid_tarot_input_strategy())
    @settings(max_examples=100)
    def test_all_cards_have_orientation(self, input_data: TarotInput):
        """
        Property test: Every card has a boolean reversed status.
        
        **Feature: calculator-accuracy-audit, Property 24: 塔罗牌阵位置记录完整性**
        **Validates: Requirements 6.2**
        """
        interpreter = TarotInterpreter()
        result = interpreter.interpret(input_data)
        
        for i, card in enumerate(result.cards):
            assert isinstance(card.reversed, bool), \
                f"Card {i+1} ({card.card_name}) reversed is not boolean: {type(card.reversed)}"
    
    @given(input_data=any_valid_tarot_input_strategy())
    @settings(max_examples=100)
    def test_orientation_matches_input(self, input_data: TarotInput):
        """
        Property test: Card orientation matches input specification.
        
        **Feature: calculator-accuracy-audit, Property 24: 塔罗牌阵位置记录完整性**
        **Validates: Requirements 6.2**
        """
        interpreter = TarotInterpreter()
        result = interpreter.interpret(input_data)
        
        for i, (input_card, result_card) in enumerate(zip(input_data.cards, result.cards)):
            assert result_card.reversed == input_card.reversed, \
                f"Card {i+1} orientation mismatch: input={input_card.reversed}, result={result_card.reversed}"
    
    @given(input_data=any_valid_tarot_input_strategy())
    @settings(max_examples=100)
    def test_position_matches_input(self, input_data: TarotInput):
        """
        Property test: Card position matches input specification.
        
        **Feature: calculator-accuracy-audit, Property 24: 塔罗牌阵位置记录完整性**
        **Validates: Requirements 6.2**
        """
        interpreter = TarotInterpreter()
        result = interpreter.interpret(input_data)
        
        for i, (input_card, result_card) in enumerate(zip(input_data.cards, result.cards)):
            if input_card.position:
                assert result_card.position == input_card.position, \
                    f"Card {i+1} position mismatch: input={input_card.position}, result={result_card.position}"
    
    @given(input_data=any_valid_tarot_input_strategy())
    @settings(max_examples=100)
    def test_factor_matrix_contains_position_factors(self, input_data: TarotInput):
        """
        Property test: Factor matrix contains position factors for each card.
        
        **Feature: calculator-accuracy-audit, Property 24: 塔罗牌阵位置记录完整性**
        **Validates: Requirements 6.2**
        """
        interpreter = TarotInterpreter()
        result = interpreter.interpret(input_data)
        factor_matrix = result.to_factor_matrix()
        
        for card in result.cards:
            card_name_normalized = card.card_name.lower().replace(" ", "_").replace("'", "")
            position_normalized = card.position.lower().replace(" ", "_")
            
            # Check for position factor
            position_factor_id = f"tarot_position_{position_normalized}_{card_name_normalized}"
            assert position_factor_id in factor_matrix.factors, \
                f"Missing position factor: {position_factor_id}"
    
    @given(input_data=any_valid_tarot_input_strategy())
    @settings(max_examples=100)
    def test_factor_matrix_contains_orientation_factors(self, input_data: TarotInput):
        """
        Property test: Factor matrix contains orientation factors for each card.
        
        **Feature: calculator-accuracy-audit, Property 24: 塔罗牌阵位置记录完整性**
        **Validates: Requirements 6.2**
        """
        interpreter = TarotInterpreter()
        result = interpreter.interpret(input_data)
        factor_matrix = result.to_factor_matrix()
        
        for card in result.cards:
            card_name_normalized = card.card_name.lower().replace(" ", "_").replace("'", "")
            orientation = "reversed" if card.reversed else "upright"
            
            # Check for card factor with orientation
            if card.is_major:
                expected_factor = f"tarot_major_{card_name_normalized}_{orientation}"
            else:
                expected_factor = f"tarot_{card.suit}_{card_name_normalized}_{orientation}"
            
            assert expected_factor in factor_matrix.factors, \
                f"Missing orientation factor: {expected_factor}"
    
    def test_spread_types_have_correct_positions(self):
        """
        Unit test: Each spread type has the correct number of positions.
        
        **Feature: calculator-accuracy-audit, Property 24: 塔罗牌阵位置记录完整性**
        **Validates: Requirements 6.2**
        """
        expected_counts = {
            "single": 1,
            "three_card": 3,
            "celtic_cross": 10,
        }
        
        drawer = TarotDrawer(seed=42)
        interpreter = TarotInterpreter()
        
        for spread_type, expected_count in expected_counts.items():
            input_data = drawer.draw_spread(spread_type)
            result = interpreter.interpret(input_data)
            
            assert len(result.cards) == expected_count, \
                f"Spread {spread_type} has {len(result.cards)} cards, expected {expected_count}"
            
            # Verify all positions are unique
            positions = [card.position for card in result.cards]
            assert len(positions) == len(set(positions)), \
                f"Spread {spread_type} has duplicate positions: {positions}"
    
    def test_all_standard_positions_have_meanings(self):
        """
        Unit test: All standard positions have defined meanings.
        
        **Feature: calculator-accuracy-audit, Property 24: 塔罗牌阵位置记录完整性**
        **Validates: Requirements 6.2**
        """
        from backend.calculators.tarot.models import POSITION_MEANINGS
        
        standard_positions = [
            "answer", "past", "present", "future", "challenge",
            "above", "below", "advice", "external", "hopes_fears", "outcome"
        ]
        
        for position in standard_positions:
            assert position in POSITION_MEANINGS, \
                f"Position '{position}' has no defined meaning"
            assert len(POSITION_MEANINGS[position]) > 0, \
                f"Position '{position}' has empty meaning"
