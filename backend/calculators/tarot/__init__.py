# backend/calculators/tarot/__init__.py
"""
TarotInterpreter - Tarot Card Interpretation Module.

Provides tarot card identification and interpretation functionality.
Does NOT require location information.

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

from backend.calculators.tarot.models import (
    TarotInput,
    TarotFactors,
    CardInterpretation,
    CardInfo,
    MAJOR_ARCANA,
    MINOR_ARCANA,
    SUITS,
    ALL_CARDS,
)
from backend.calculators.tarot.interpreter import TarotInterpreter, TarotDrawer

__all__ = [
    "TarotInterpreter",
    "TarotDrawer",
    "TarotInput",
    "TarotFactors",
    "CardInterpretation",
    "CardInfo",
    "MAJOR_ARCANA",
    "MINOR_ARCANA",
    "SUITS",
    "ALL_CARDS",
]
