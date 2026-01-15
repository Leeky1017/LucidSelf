# backend/calculators/ziwei/__init__.py
"""
Ziwei Doushu (紫微斗数) Calculator Module.

Provides accurate Purple Star Astrology chart calculation including:
- Twelve palaces (十二宫) placement
- Fourteen main stars (十四主星) placement
- Auxiliary stars (辅星) and sha stars (煞星)
- Four transformations (四化): natal, decade, annual
- Decade luck cycles (大限)

Follows:
- Architecture v3 Layer 1 Calculator standard
- Data Contract §4.4 factor naming conventions
"""

from backend.calculators.ziwei.models import (
    ZiweiInput,
    ZiweiFactors,
    Palace,
    Star,
    SiHua,
    Decade,
    ZiweiChart,
    LunarDate,
)
from backend.calculators.ziwei.calculator import ZiweiCalculator
from backend.calculators.ziwei.service import (
    calculate_with_geocoding,
    calculate_with_geocoding_sync,
)

__all__ = [
    "ZiweiCalculator",
    "ZiweiInput",
    "ZiweiFactors",
    "Palace",
    "Star",
    "SiHua",
    "Decade",
    "ZiweiChart",
    "LunarDate",
    # Geocoding integration
    "calculate_with_geocoding",
    "calculate_with_geocoding_sync",
]

__version__ = "0.1.0"
