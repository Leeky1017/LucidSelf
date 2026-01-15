# backend/calculators/dream/models.py
"""
Data models for DreamExtractor.

Follows:
- Architecture v3 §4.1 DreamInput/DreamFactors
- Data Contract §1.1 FactorValue/FactorMatrix
- Factor ID naming: dream_* (underscore format)
"""

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional
from pydantic import BaseModel, ConfigDict, Field, field_validator

from backend.core.contracts import FactorValue, FactorMatrix


# =============================================================================
# Constants: Symbol Categories
# =============================================================================

SYMBOL_CATEGORIES = [
    "animal",   # 动物：狗、猫、蛇、鸟等
    "person",   # 人物：父母、陌生人、朋友等
    "scene",    # 场景：房屋、学校、森林等
    "object",   # 物品：钥匙、镜子、书等
    "nature",   # 自然：水、火、山、天空等
    "body",     # 身体：牙齿、头发、手等
]
"""Dream symbol categories."""

SymbolCategory = Literal["animal", "person", "scene", "object", "nature", "body"]


# =============================================================================
# Constants: Themes
# =============================================================================

THEMES = [
    "chase",      # 被追逐
    "falling",    # 坠落
    "flying",     # 飞翔
    "exam",       # 考试
    "death",      # 死亡
    "water",      # 水相关
    "lost",       # 迷路
    "naked",      # 裸露
    "teeth",      # 牙齿脱落
    "late",       # 迟到
    "trapped",    # 被困
    "reunion",    # 重逢
    "journey",    # 旅行
    "conflict",   # 冲突
    "transformation",  # 变形
]
"""Common dream themes."""


# =============================================================================
# Constants: Emotions
# =============================================================================

EMOTIONS = [
    "fear",       # 恐惧
    "joy",        # 喜悦
    "anxiety",    # 焦虑
    "calm",       # 平静
    "anger",      # 愤怒
    "sadness",    # 悲伤
    "confusion",  # 困惑
    "excitement", # 兴奋
    "peace",      # 安宁
    "surprise",   # 惊讶
]
"""Dream emotional tones."""


# =============================================================================
# Input Model
# =============================================================================

class DreamInput(BaseModel):
    """
    Dream extraction input model.
    
    Does NOT require location information.
    
    Attributes:
        dream_text: Dream description text (minimum 10 characters)
        language: Text language (zh for Chinese, en for English)
    """
    dream_text: str = Field(
        ..., 
        min_length=10, 
        description="梦境描述文本，至少10个字符"
    )
    language: Literal["zh", "en"] = Field(
        default="zh", 
        description="文本语言：zh=中文, en=英文"
    )
    
    @field_validator('dream_text')
    @classmethod
    def validate_dream_text(cls, v: str) -> str:
        """Strip whitespace and validate length."""
        v = v.strip()
        if len(v) < 10:
            raise ValueError("Dream text must be at least 10 characters after stripping whitespace")
        return v
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "dream_text": "我梦见自己在飞翔，下面是一片大海，感觉很自由",
                "language": "zh"
            }
        }
    )


# =============================================================================
# Internal Data Structures
# =============================================================================

class DreamSymbol(BaseModel):
    """A single dream symbol identified from text."""
    symbol: str = Field(..., description="Symbol name (normalized)")
    category: SymbolCategory = Field(..., description="Symbol category")
    confidence: float = Field(
        ..., 
        ge=0.0, 
        le=1.0, 
        description="Match confidence 0.0-1.0"
    )
    matched_text: str = Field(..., description="Original text that matched")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "symbol": "sea",
                "category": "nature",
                "confidence": 0.95,
                "matched_text": "大海"
            }
        }
    )


# =============================================================================
# Output Model: DreamFactors
# =============================================================================

class DreamFactors(BaseModel):
    """
    Dream factors output model.
    
    Contains extracted symbols, themes, and emotions, and provides 
    to_factor_matrix() method to convert to unified FactorMatrix format.
    
    Factor ID naming follows data contract: dream_*
    """
    
    symbols: List[DreamSymbol] = Field(
        default_factory=list, 
        description="Extracted dream symbols"
    )
    themes: List[str] = Field(
        default_factory=list, 
        description="Detected dream themes"
    )
    emotions: List[str] = Field(
        default_factory=list, 
        description="Detected emotional tones"
    )
    raw_tokens: List[str] = Field(
        default_factory=list, 
        description="Tokenization result (for debugging)"
    )
    language: str = Field(default="zh", description="Input language")
    calculation_time_ms: float = Field(default=0.0, description="Calculation time in ms")
    
    def to_factor_matrix(self) -> FactorMatrix:
        """
        Convert to unified FactorMatrix format.
        
        Factor ID naming follows data contract:
        - dream_symbol_{category}_{symbol}: Symbol factor
        - dream_theme_{theme}: Theme factor
        - dream_emotion_{emotion}: Emotion factor
        
        Returns:
            FactorMatrix: Unified factor matrix
        """
        factors: Dict[str, FactorValue] = {}
        
        # 1. Symbol factors
        for symbol in self.symbols:
            # Normalize symbol name for factor ID
            symbol_normalized = symbol.symbol.lower().replace(" ", "_").replace("-", "_")
            factor_id = f"dream_symbol_{symbol.category}_{symbol_normalized}"
            
            factors[factor_id] = FactorValue(
                factor_id=factor_id,
                value=True,
                confidence=symbol.confidence,
                source="calculator"
            )
        
        # 2. Theme factors
        for theme in self.themes:
            theme_normalized = theme.lower().replace(" ", "_")
            factor_id = f"dream_theme_{theme_normalized}"
            
            factors[factor_id] = FactorValue(
                factor_id=factor_id,
                value=True,
                confidence=0.8,  # Theme detection has moderate confidence
                source="calculator"
            )
        
        # 3. Emotion factors
        for emotion in self.emotions:
            emotion_normalized = emotion.lower().replace(" ", "_")
            factor_id = f"dream_emotion_{emotion_normalized}"
            
            factors[factor_id] = FactorValue(
                factor_id=factor_id,
                value=True,
                confidence=0.7,  # Emotion detection has lower confidence
                source="calculator"
            )
        
        # =============================================================
        # 规则兼容因子 (Rule-Compatible Factors)
        # 以下因子是为了兼容现有规则期望的命名约定
        # =============================================================
        
        # 4. 主符号因子 (规则期望 dream_symbol 单值)
        if self.symbols:
            primary_symbol = self.symbols[0]
            factors["dream_symbol"] = FactorValue(
                factor_id="dream_symbol",
                value=primary_symbol.symbol,
                confidence=primary_symbol.confidence,
                source="calculator"
            )
            # 符号数量
            factors["dream_symbol_count"] = FactorValue(
                factor_id="dream_symbol_count",
                value=len(self.symbols),
                confidence=1.0,
                source="calculator"
            )
            # 各类别符号列表
            for category in SYMBOL_CATEGORIES:
                cat_symbols = [s.symbol for s in self.symbols if s.category == category]
                factors[f"dream_{category}_symbols"] = FactorValue(
                    factor_id=f"dream_{category}_symbols",
                    value=cat_symbols,
                    confidence=0.9,
                    source="calculator"
                )
                factors[f"dream_has_{category}"] = FactorValue(
                    factor_id=f"dream_has_{category}",
                    value=len(cat_symbols) > 0,
                    confidence=0.9,
                    source="calculator"
                )
        else:
            factors["dream_symbol"] = FactorValue(
                factor_id="dream_symbol",
                value="",
                confidence=0.0,
                source="calculator"
            )
            factors["dream_symbol_count"] = FactorValue(
                factor_id="dream_symbol_count",
                value=0,
                confidence=1.0,
                source="calculator"
            )
        
        # 5. 主题因子 (规则期望 dream_theme 单值)
        if self.themes:
            factors["dream_theme"] = FactorValue(
                factor_id="dream_theme",
                value=self.themes[0],
                confidence=0.8,
                source="calculator"
            )
            factors["dream_theme_list"] = FactorValue(
                factor_id="dream_theme_list",
                value=self.themes,
                confidence=0.8,
                source="calculator"
            )
        else:
            factors["dream_theme"] = FactorValue(
                factor_id="dream_theme",
                value="",
                confidence=0.0,
                source="calculator"
            )
        
        # 6. 情绪因子 (规则期望 dream_emotion 单值)
        if self.emotions:
            factors["dream_emotion"] = FactorValue(
                factor_id="dream_emotion",
                value=self.emotions[0],
                confidence=0.7,
                source="calculator"
            )
            factors["dream_emotion_list"] = FactorValue(
                factor_id="dream_emotion_list",
                value=self.emotions,
                confidence=0.7,
                source="calculator"
            )
            # 常见情绪类型
            factors["dream_positive_emotion"] = FactorValue(
                factor_id="dream_positive_emotion",
                value=any(e in ["joy", "calm", "peace", "excitement"] for e in self.emotions),
                confidence=0.8,
                source="calculator"
            )
            factors["dream_negative_emotion"] = FactorValue(
                factor_id="dream_negative_emotion",
                value=any(e in ["fear", "anxiety", "anger", "sadness"] for e in self.emotions),
                confidence=0.8,
                source="calculator"
            )
        else:
            factors["dream_emotion"] = FactorValue(
                factor_id="dream_emotion",
                value="",
                confidence=0.0,
                source="calculator"
            )
        
        return FactorMatrix(
            factors=factors,
            timestamp=datetime.now(),
            engine_id="dream-extractor"
        )
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "symbols": [
                    {
                        "symbol": "sea",
                        "category": "nature",
                        "confidence": 0.95,
                        "matched_text": "大海"
                    },
                    {
                        "symbol": "flying",
                        "category": "scene",
                        "confidence": 0.9,
                        "matched_text": "飞翔"
                    }
                ],
                "themes": ["flying", "water"],
                "emotions": ["joy", "peace"],
                "raw_tokens": ["我", "梦见", "自己", "在", "飞翔"],
                "language": "zh",
                "calculation_time_ms": 15.5
            }
        }
    )
