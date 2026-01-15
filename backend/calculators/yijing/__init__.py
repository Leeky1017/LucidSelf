# backend/calculators/yijing/__init__.py
"""
YijingCalculator - I Ching (六爻/易经) Divination Engine.

This module provides calculation of:
- Hexagram generation (卦象生成) via multiple methods
- Upper and lower trigrams (上卦/下卦)
- Mutual hexagram (互卦)
- Changed hexagram (变卦)
- Moving lines (动爻)

Divination Methods:
- coin: Three-coin toss method (铜钱法)
- yarrow: Traditional yarrow stalk method (蓍草法)
- time: Time-based divination (时间起卦)
- manual: Direct line input (手动输入)

Conforms to:
- Architecture v3 Layer 1 Calculator standard
- Data Contract Schema v1.0
- Engine Registry specification

Geocoding Integration:
- Time-based divination optionally uses location for true solar time
- Use calculate_with_geocoding() for automatic location resolution
"""

from backend.calculators.yijing.models import (
    YijingInput,
    YijingFactors,
    Hexagram,
    Trigram,
)
from backend.calculators.yijing.calculator import YijingCalculator
from backend.calculators.yijing.service import (
    calculate_with_geocoding,
    calculate_with_geocoding_sync,
)

__all__ = [
    "YijingCalculator",
    "YijingInput",
    "YijingFactors",
    "Hexagram",
    "Trigram",
    "calculate_with_geocoding",
    "calculate_with_geocoding_sync",
]
