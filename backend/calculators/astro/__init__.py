# backend/calculators/astro/__init__.py
"""
AstroCalculator - Western Astrology Calculator Module.

Provides planetary positions, house cusps, and aspect calculations
using Swiss Ephemeris for high-precision astronomical data.

符合架构文档 §4.1 Layer 1 Calculator 标准。
"""

from backend.calculators.astro.models import (
    AstroInput,
    AstroFactors,
    PlanetPosition,
    Aspect,
    PLANETS,
    SIGNS,
    ASPECT_ORBS,
)
from backend.calculators.astro.calculator import AstroCalculator
from backend.calculators.astro.service import (
    calculate_with_geocoding,
    calculate_with_geocoding_sync,
)

__all__ = [
    "AstroCalculator",
    "AstroInput",
    "AstroFactors",
    "PlanetPosition",
    "Aspect",
    "PLANETS",
    "SIGNS",
    "ASPECT_ORBS",
    "calculate_with_geocoding",
    "calculate_with_geocoding_sync",
]
