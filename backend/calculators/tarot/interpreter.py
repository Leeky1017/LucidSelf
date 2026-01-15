# backend/calculators/tarot/interpreter.py
"""
TarotInterpreter - Tarot Card Interpreter.

Implements Layer 1 Calculator standard interface, providing:
- Card identification from 78-card deck
- Upright/reversed orientation detection
- Spread position interpretation
- Random card drawing with uniform distribution

Does NOT require location information.

Performance target: < 5ms/interpretation (P95)
Accuracy target: 78 card identification 100%
"""

from __future__ import annotations

import random
import time
from typing import Dict, List, Optional, Tuple

from backend.calculators.tarot.models import (
    TarotInput,
    TarotFactors,
    CardInterpretation,
    CardInfo,
    ALL_CARDS,
    MAJOR_ARCANA,
    MINOR_ARCANA,
    SPREAD_TYPES,
    POSITION_MEANINGS,
)


class TarotInterpreter:
    """
    Tarot Card Interpreter.
    
    Conforms to Architecture v3 §4.1 Layer 1 Calculator standard.
    
    Example:
        >>> from backend.calculators.tarot import TarotInterpreter, TarotInput
        >>> 
        >>> interpreter = TarotInterpreter()
        >>> input_data = TarotInput(
        ...     spread_type="three_card",
        ...     cards=[
        ...         {"card_name": "The Fool", "reversed": False, "position": "past"},
        ...         {"card_name": "The Magician", "reversed": True, "position": "present"},
        ...         {"card_name": "The High Priestess", "reversed": False, "position": "future"},
        ...     ]
        ... )
        >>> tarot_factors = interpreter.interpret(input_data)
        >>> factor_matrix = tarot_factors.to_factor_matrix()
    """
    
    def __init__(self):
        """Initialize interpreter with card lookup tables."""
        # Build name-to-number lookup (case-insensitive)
        self._name_to_number: Dict[str, int] = {}
        for num, card in ALL_CARDS.items():
            # Add English name
            self._name_to_number[card["name"].lower()] = num
            # Add Chinese name if available
            if "name_zh" in card:
                self._name_to_number[card["name_zh"]] = num
        
        # Add common aliases
        self._add_aliases()
    
    def _add_aliases(self) -> None:
        """Add common card name aliases."""
        aliases = {
            # Major Arcana aliases
            "fool": 0,
            "magician": 1,
            "high priestess": 2,
            "priestess": 2,
            "empress": 3,
            "emperor": 4,
            "hierophant": 5,
            "pope": 5,
            "lovers": 6,
            "chariot": 7,
            "strength": 8,
            "hermit": 9,
            "wheel": 10,
            "wheel of fortune": 10,
            "fortune": 10,
            "justice": 11,
            "hanged man": 12,
            "death": 13,
            "temperance": 14,
            "devil": 15,
            "tower": 16,
            "star": 17,
            "moon": 18,
            "sun": 19,
            "judgement": 20,
            "judgment": 20,  # Alternative spelling
            "world": 21,
        }
        for alias, num in aliases.items():
            self._name_to_number[alias] = num
    
    def interpret(self, input_data: TarotInput) -> TarotFactors:
        """
        Interpret a tarot spread.
        
        Args:
            input_data: Input parameters
            
        Returns:
            TarotFactors: Interpretation result
            
        Raises:
            ValueError: If card cannot be identified
        """
        start_time = time.perf_counter()
        
        # Get spread positions
        spread_info = SPREAD_TYPES.get(input_data.spread_type, SPREAD_TYPES["custom"])
        default_positions = spread_info["positions"]
        
        # Interpret each card
        interpretations: List[CardInterpretation] = []
        for i, card_info in enumerate(input_data.cards):
            interpretation = self._interpret_card(
                card_info,
                default_position=default_positions[i] if i < len(default_positions) else f"position_{i+1}"
            )
            interpretations.append(interpretation)
        
        calculation_time = (time.perf_counter() - start_time) * 1000
        
        return TarotFactors(
            cards=interpretations,
            spread_type=input_data.spread_type,
            question=input_data.question,
            calculation_time_ms=calculation_time,
        )
    
    def _interpret_card(
        self,
        card_info: CardInfo,
        default_position: str
    ) -> CardInterpretation:
        """
        Interpret a single card.
        
        Args:
            card_info: Card information from input
            default_position: Default position if not specified
            
        Returns:
            CardInterpretation: Interpreted card
            
        Raises:
            ValueError: If card cannot be identified
        """
        # Identify card
        card_number = self._identify_card(card_info.card_name)
        card_data = ALL_CARDS[card_number]
        
        # Get position
        position = card_info.position or default_position
        position_meaning = POSITION_MEANINGS.get(position, f"Position: {position}")
        
        return CardInterpretation(
            card_name=card_data["name"],
            card_name_zh=card_data.get("name_zh", card_data["name"]),
            card_number=card_number,
            suit=card_data.get("suit"),
            is_major=card_data["is_major"],
            reversed=card_info.reversed,
            position=position,
            position_meaning=position_meaning,
        )
    
    def _identify_card(self, card_name: str) -> int:
        """
        Identify a card by name.
        
        Args:
            card_name: Card name (English or Chinese)
            
        Returns:
            int: Card number (0-77)
            
        Raises:
            ValueError: If card cannot be identified
        """
        # Try exact match (case-insensitive)
        normalized = card_name.lower().strip()
        if normalized in self._name_to_number:
            return self._name_to_number[normalized]
        
        # Try partial match for Minor Arcana
        # e.g., "Ace of Wands", "2 of Cups", "King of Swords"
        card_number = self._parse_minor_arcana(normalized)
        if card_number is not None:
            return card_number
        
        # Card not found
        raise ValueError(
            f"Cannot identify card: '{card_name}'. "
            f"Please use standard card names like 'The Fool', 'Ace of Wands', etc."
        )
    
    def _parse_minor_arcana(self, name: str) -> Optional[int]:
        """
        Parse Minor Arcana card name.
        
        Handles formats like:
        - "Ace of Wands"
        - "2 of Cups"
        - "King of Swords"
        - "权杖王牌"
        
        Args:
            name: Normalized card name
            
        Returns:
            Card number or None if not a valid Minor Arcana
        """
        # Try English format: "{rank} of {suit}"
        if " of " in name:
            parts = name.split(" of ")
            if len(parts) == 2:
                rank_str, suit_str = parts
                rank_str = rank_str.strip()
                suit_str = suit_str.strip()
                
                # Parse suit
                suit = self._parse_suit(suit_str)
                if suit is None:
                    return None
                
                # Parse rank
                rank = self._parse_rank(rank_str)
                if rank is None:
                    return None
                
                # Find card number
                return self._find_minor_arcana_number(suit, rank)
        
        return None
    
    def _parse_suit(self, suit_str: str) -> Optional[str]:
        """Parse suit name."""
        suit_map = {
            "wands": "wands",
            "wand": "wands",
            "cups": "cups",
            "cup": "cups",
            "swords": "swords",
            "sword": "swords",
            "pentacles": "pentacles",
            "pentacle": "pentacles",
            "coins": "pentacles",
            "coin": "pentacles",
        }
        return suit_map.get(suit_str.lower())
    
    def _parse_rank(self, rank_str: str) -> Optional[str]:
        """Parse rank (Ace, 2-10, Page, Knight, Queen, King)."""
        rank_str = rank_str.lower()
        
        # Number ranks
        if rank_str.isdigit():
            num = int(rank_str)
            if 1 <= num <= 10:
                return "Ace" if num == 1 else str(num)
        
        # Named ranks
        rank_map = {
            "ace": "Ace",
            "one": "Ace",
            "1": "Ace",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
            "ten": "10",
            "page": "Page",
            "knight": "Knight",
            "queen": "Queen",
            "king": "King",
        }
        return rank_map.get(rank_str)
    
    def _find_minor_arcana_number(self, suit: str, rank: str) -> Optional[int]:
        """Find card number for Minor Arcana."""
        for num, card in MINOR_ARCANA.items():
            if card["suit"] == suit:
                card_rank = card["rank"]
                if isinstance(card_rank, int):
                    card_rank = "Ace" if card_rank == 1 else str(card_rank)
                if card_rank == rank:
                    return num
        return None
    
    def get_all_card_names(self) -> List[str]:
        """
        Get list of all valid card names.
        
        Returns:
            List of card names
        """
        return [card["name"] for card in ALL_CARDS.values()]
    
    def get_card_info(self, card_number: int) -> Optional[Dict]:
        """
        Get card information by number.
        
        Args:
            card_number: Card number (0-77)
            
        Returns:
            Card information dict or None
        """
        return ALL_CARDS.get(card_number)


class TarotDrawer:
    """
    Random Tarot Card Drawer.
    
    Provides uniform random card drawing from the 78-card deck.
    Uses Python's random module with proper shuffling for uniform distribution.
    
    Example:
        >>> drawer = TarotDrawer()
        >>> cards = drawer.draw_spread("three_card")
        >>> # Returns 3 randomly drawn cards with positions
    """
    
    def __init__(self, seed: Optional[int] = None):
        """
        Initialize drawer with optional random seed.
        
        Args:
            seed: Optional random seed for reproducibility (testing)
        """
        self._rng = random.Random(seed)
        self._all_card_numbers = list(ALL_CARDS.keys())  # 0-77
    
    def draw_single_card(self, allow_reversed: bool = True) -> CardInfo:
        """
        Draw a single random card.
        
        Args:
            allow_reversed: Whether to randomly determine reversed status
            
        Returns:
            CardInfo: Randomly drawn card
        """
        card_number = self._rng.choice(self._all_card_numbers)
        card_data = ALL_CARDS[card_number]
        reversed_status = self._rng.choice([True, False]) if allow_reversed else False
        
        return CardInfo(
            card_name=card_data["name"],
            reversed=reversed_status,
            position=None,
        )
    
    def draw_cards(
        self, 
        count: int, 
        allow_duplicates: bool = False,
        allow_reversed: bool = True
    ) -> List[CardInfo]:
        """
        Draw multiple random cards.
        
        Args:
            count: Number of cards to draw
            allow_duplicates: Whether to allow the same card multiple times
            allow_reversed: Whether to randomly determine reversed status
            
        Returns:
            List of CardInfo objects
            
        Raises:
            ValueError: If count > 78 and duplicates not allowed
        """
        if not allow_duplicates and count > 78:
            raise ValueError(
                f"Cannot draw {count} unique cards from a 78-card deck"
            )
        
        if allow_duplicates:
            card_numbers = [
                self._rng.choice(self._all_card_numbers) 
                for _ in range(count)
            ]
        else:
            # Shuffle and take first 'count' cards for uniform distribution
            shuffled = self._all_card_numbers.copy()
            self._rng.shuffle(shuffled)
            card_numbers = shuffled[:count]
        
        cards = []
        for card_number in card_numbers:
            card_data = ALL_CARDS[card_number]
            reversed_status = self._rng.choice([True, False]) if allow_reversed else False
            cards.append(CardInfo(
                card_name=card_data["name"],
                reversed=reversed_status,
                position=None,
            ))
        
        return cards
    
    def draw_spread(
        self, 
        spread_type: str,
        allow_reversed: bool = True
    ) -> TarotInput:
        """
        Draw cards for a specific spread type.
        
        Args:
            spread_type: Type of spread (single, three_card, celtic_cross, custom)
            allow_reversed: Whether to randomly determine reversed status
            
        Returns:
            TarotInput: Complete input with randomly drawn cards and positions
            
        Raises:
            ValueError: If spread_type is invalid
        """
        if spread_type not in SPREAD_TYPES:
            raise ValueError(f"Unknown spread type: {spread_type}")
        
        spread_info = SPREAD_TYPES[spread_type]
        positions = spread_info["positions"]
        
        if spread_type == "custom":
            # For custom, draw 1-10 cards
            count = self._rng.randint(1, 10)
            positions = [f"position_{i+1}" for i in range(count)]
        
        count = len(positions)
        cards = self.draw_cards(count, allow_duplicates=False, allow_reversed=allow_reversed)
        
        # Assign positions
        for i, card in enumerate(cards):
            card.position = positions[i]
        
        return TarotInput(
            spread_type=spread_type,
            cards=cards,
            question=None,
        )
    
    def draw_card_number(self) -> int:
        """
        Draw a single random card number (0-77).
        
        This is the core random function used for statistical testing.
        Uses uniform random selection.
        
        Returns:
            int: Card number 0-77
        """
        return self._rng.choice(self._all_card_numbers)
    
    def set_seed(self, seed: int) -> None:
        """
        Set random seed for reproducibility.
        
        Args:
            seed: Random seed
        """
        self._rng.seed(seed)
