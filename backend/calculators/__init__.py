# backend/calculators/__init__.py
"""
Layer 1 Calculators - Domain-specific factor computation.

This package contains pure calculation logic for various systems:
- bazi: Chinese Four Pillars (八字) calculation
- ziwei: Purple Star Astrology (紫微斗数) calculation
- astro: Western Astrology calculation
- tarot: Tarot interpretation
- dream: Dream symbol extraction
- yijing: I Ching (六爻/易经) calculation

All *Factors classes implement to_factor_matrix() method for Layer 2 RuleEngine consumption.

Note: Some calculators require optional dependencies (swisseph, sxtwl, etc.)
      If dependencies are missing, the calculator will not be available.
"""

import logging

_logger = logging.getLogger(__name__)

# 使用延迟导入处理可选依赖
__all__ = []

# BaZi (八字)
try:
    from backend.calculators.bazi import BaziCalculator, BaziInput, BaziFactors
    __all__.extend(["BaziCalculator", "BaziInput", "BaziFactors"])
except ImportError as e:
    _logger.debug(f"BaZi calculator not available: {e}")

# Ziwei (紫微斗数)
try:
    from backend.calculators.ziwei import ZiweiCalculator, ZiweiInput, ZiweiFactors
    __all__.extend(["ZiweiCalculator", "ZiweiInput", "ZiweiFactors"])
except ImportError as e:
    _logger.debug(f"Ziwei calculator not available: {e}")

# Astro (西洋占星) - 需要swisseph
try:
    from backend.calculators.astro import AstroCalculator, AstroInput, AstroFactors
    __all__.extend(["AstroCalculator", "AstroInput", "AstroFactors"])
except ImportError as e:
    _logger.debug(f"Astro calculator not available: {e}")

# Tarot (塔罗牌)
try:
    from backend.calculators.tarot import TarotInterpreter, TarotInput, TarotFactors
    __all__.extend(["TarotInterpreter", "TarotInput", "TarotFactors"])
except ImportError as e:
    _logger.debug(f"Tarot interpreter not available: {e}")

# Dream (解梦) - 基础功能，应该总是可用
try:
    from backend.calculators.dream import DreamExtractor, DreamInput, DreamFactors
    __all__.extend(["DreamExtractor", "DreamInput", "DreamFactors"])
except ImportError as e:
    _logger.warning(f"Dream extractor not available: {e}")

# YiJing (六爻/易经)
try:
    from backend.calculators.yijing import YijingCalculator, YijingInput, YijingFactors
    __all__.extend(["YijingCalculator", "YijingInput", "YijingFactors"])
except ImportError as e:
    _logger.debug(f"Yijing calculator not available: {e}")
