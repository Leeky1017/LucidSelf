# backend/calculators/tarot/tests/test_golden_set.py
"""
Golden Set Tests for TarotInterpreter.

Covers all 78 cards in the Tarot deck:
- 22 Major Arcana (0-21)
- 56 Minor Arcana (22-77)
  - 14 Wands (22-35)
  - 14 Cups (36-49)
  - 14 Swords (50-63)
  - 14 Pentacles (64-77)

**Validates: Requirements 10.5**
"""

import json
import pytest
from pathlib import Path
from typing import List, Dict, Any

from backend.calculators.tarot import (
    TarotInterpreter,
    TarotInput,
    CardInfo,
    ALL_CARDS,
    MAJOR_ARCANA,
    MINOR_ARCANA,
)
from backend.core.testing.golden_set import GoldenSetLoader, GoldenSetCase


# Load golden set cases
GOLDEN_SET_PATH = Path(__file__).parent / "golden_cases" / "tarot_golden_set.jsonl"


def load_golden_cases() -> List[GoldenSetCase]:
    """Load golden set cases from JSONL file."""
    loader = GoldenSetLoader()
    return loader.load_jsonl(GOLDEN_SET_PATH)


# Get all cases for parametrization
try:
    GOLDEN_CASES = load_golden_cases()
except FileNotFoundError:
    GOLDEN_CASES = []


class TestTarotGoldenSet:
    """
    Golden Set tests for TarotInterpreter.
    
    Covers all 78 cards in the Tarot deck.
    
    **Validates: Requirements 10.5**
    """
    
    @pytest.fixture
    def interpreter(self):
        """Create TarotInterpreter instance."""
        return TarotInterpreter()
    
    @pytest.mark.parametrize(
        "case",
        GOLDEN_CASES,
        ids=[c.case_id for c in GOLDEN_CASES],
    )
    def test_golden_case(self, interpreter, case: GoldenSetCase):
        """
        Test TarotInterpreter against golden set case.
        
        **Feature: calculator-accuracy-audit, Golden Set Test**
        **Validates: Requirements 10.5**
        """
        # Build input
        input_data = TarotInput(
            spread_type=case.input_data["spread_type"],
            cards=[CardInfo(**card) for card in case.input_data["cards"]],
        )
        
        # Run interpreter
        result = interpreter.interpret(input_data)
        
        # Verify output
        assert len(result.cards) == 1, f"Expected 1 card, got {len(result.cards)}"
        
        card = result.cards[0]
        expected = case.expected_output
        
        # Verify card number
        assert card.card_number == expected["card_number"], \
            f"Card number mismatch: got {card.card_number}, expected {expected['card_number']}"
        
        # Verify card name
        assert card.card_name == expected["card_name"], \
            f"Card name mismatch: got {card.card_name}, expected {expected['card_name']}"
        
        # Verify Chinese name
        assert card.card_name_zh == expected["card_name_zh"], \
            f"Chinese name mismatch: got {card.card_name_zh}, expected {expected['card_name_zh']}"
        
        # Verify is_major
        assert card.is_major == expected["is_major"], \
            f"is_major mismatch: got {card.is_major}, expected {expected['is_major']}"
        
        # Verify suit
        assert card.suit == expected["suit"], \
            f"Suit mismatch: got {card.suit}, expected {expected['suit']}"
        
        # Verify reversed status
        assert card.reversed == expected["reversed"], \
            f"Reversed mismatch: got {card.reversed}, expected {expected['reversed']}"
        
        # Verify position
        assert card.position == expected["position"], \
            f"Position mismatch: got {card.position}, expected {expected['position']}"
    
    def test_golden_set_coverage(self):
        """
        Test that golden set covers all 78 cards.
        
        **Feature: calculator-accuracy-audit, Golden Set Coverage**
        **Validates: Requirements 10.5**
        """
        assert len(GOLDEN_CASES) >= 78, \
            f"Golden set should have at least 78 cases (one per card), got {len(GOLDEN_CASES)}"
        
        # Check all card numbers are covered
        covered_cards = set()
        for case in GOLDEN_CASES:
            card_num = case.expected_output.get("card_number")
            if card_num is not None:
                covered_cards.add(card_num)
        
        assert len(covered_cards) == 78, \
            f"Golden set should cover all 78 cards, got {len(covered_cards)}"
        
        # Verify range 0-77
        assert min(covered_cards) == 0, "Missing card 0 (The Fool)"
        assert max(covered_cards) == 77, "Missing card 77 (King of Pentacles)"
    
    def test_major_arcana_coverage(self):
        """
        Test that golden set covers all 22 Major Arcana.
        
        **Feature: calculator-accuracy-audit, Golden Set Coverage**
        **Validates: Requirements 10.5**
        """
        major_cards = set()
        for case in GOLDEN_CASES:
            if case.expected_output.get("is_major"):
                major_cards.add(case.expected_output["card_number"])
        
        assert len(major_cards) == 22, \
            f"Golden set should cover all 22 Major Arcana, got {len(major_cards)}"
        
        # Verify range 0-21
        for i in range(22):
            assert i in major_cards, f"Missing Major Arcana card {i}"
    
    def test_minor_arcana_coverage(self):
        """
        Test that golden set covers all 56 Minor Arcana.
        
        **Feature: calculator-accuracy-audit, Golden Set Coverage**
        **Validates: Requirements 10.5**
        """
        minor_cards = set()
        suits_covered = set()
        
        for case in GOLDEN_CASES:
            if not case.expected_output.get("is_major"):
                minor_cards.add(case.expected_output["card_number"])
                suit = case.expected_output.get("suit")
                if suit:
                    suits_covered.add(suit)
        
        assert len(minor_cards) == 56, \
            f"Golden set should cover all 56 Minor Arcana, got {len(minor_cards)}"
        
        # Verify all suits are covered
        expected_suits = {"wands", "cups", "swords", "pentacles"}
        assert suits_covered == expected_suits, \
            f"Missing suits: {expected_suits - suits_covered}"
        
        # Verify 14 cards per suit
        for suit in expected_suits:
            suit_count = sum(
                1 for case in GOLDEN_CASES 
                if case.expected_output.get("suit") == suit
            )
            assert suit_count == 14, \
                f"Suit {suit} should have 14 cards, got {suit_count}"
    
    def test_all_cards_identifiable(self):
        """
        Test that all 78 cards can be identified by name.
        
        **Feature: calculator-accuracy-audit, Card Identification**
        **Validates: Requirements 10.5**
        """
        interpreter = TarotInterpreter()
        
        for card_num, card_data in ALL_CARDS.items():
            input_data = TarotInput(
                spread_type="single",
                cards=[CardInfo(
                    card_name=card_data["name"],
                    reversed=False,
                    position="answer"
                )],
            )
            
            result = interpreter.interpret(input_data)
            
            assert len(result.cards) == 1
            assert result.cards[0].card_number == card_num, \
                f"Card '{card_data['name']}' identified as #{result.cards[0].card_number}, expected #{card_num}"
