# backend/calculators/dream/__init__.py
"""
DreamExtractor - Dream Symbol Extraction Module.

Provides dream symbol identification and extraction functionality.
Does NOT require location information.

Example:
    >>> from backend.calculators.dream import DreamExtractor, DreamInput
    >>> 
    >>> extractor = DreamExtractor()
    >>> input_data = DreamInput(
    ...     dream_text="我梦见自己在飞翔，下面是一片大海",
    ...     language="zh"
    ... )
    >>> dream_factors = extractor.extract(input_data)
    >>> factor_matrix = dream_factors.to_factor_matrix()
"""

from backend.calculators.dream.models import (
    DreamInput,
    DreamFactors,
    DreamSymbol,
    SYMBOL_CATEGORIES,
    THEMES,
    EMOTIONS,
)
from backend.calculators.dream.extractor import DreamExtractor

__all__ = [
    "DreamExtractor",
    "DreamInput",
    "DreamFactors",
    "DreamSymbol",
    "SYMBOL_CATEGORIES",
    "THEMES",
    "EMOTIONS",
]
