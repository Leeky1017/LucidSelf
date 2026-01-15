# backend/calculators/bazi/__init__.py
"""
BaziCalculator - Chinese Four Pillars (八字) Calculation Engine.

This module provides accurate calculation of:
- Four Pillars (年月日时四柱)
- Hidden Stems (藏干)
- Ten Gods (十神)
- Five Elements strength (五行强弱)
- Luck Cycles (大运)

Conforms to:
- Architecture v3 Layer 1 Calculator standard
- Data Contract Schema v1.0
- Engine Registry specification

Geocoding Integration:
- Supports birth_place (city name) input via GeocodingService
- Use calculate_with_geocoding() for automatic location resolution
"""

from backend.calculators.bazi.models import (
    BaziInput,
    BaziFactors,
    Pillar,
    FourPillars,
    Dayun,
    HiddenStem,
    TenGod,
)
from backend.calculators.bazi.calculator import BaziCalculator
from backend.calculators.bazi.service import (
    calculate_with_geocoding,
    calculate_with_geocoding_sync,
)

__all__ = [
    "BaziCalculator",
    "BaziInput",
    "BaziFactors",
    "Pillar",
    "FourPillars",
    "Dayun",
    "HiddenStem",
    "TenGod",
    # Geocoding integration
    "calculate_with_geocoding",
    "calculate_with_geocoding_sync",
]
