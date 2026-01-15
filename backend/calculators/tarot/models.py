# backend/calculators/tarot/models.py
"""
Data models for TarotInterpreter.

Follows:
- Architecture v3 §4.1 TarotInput/TarotFactors
- Data Contract §1.1 FactorValue/FactorMatrix
- Factor ID naming: tarot_* (underscore format)
"""

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Any
from pydantic import BaseModel, ConfigDict, Field, model_validator

from backend.core.contracts import FactorValue, FactorMatrix


# =============================================================================
# Constants: Major Arcana (22 cards)
# =============================================================================

MAJOR_ARCANA = {
    0: {"name": "The Fool", "name_zh": "愚者"},
    1: {"name": "The Magician", "name_zh": "魔术师"},
    2: {"name": "The High Priestess", "name_zh": "女祭司"},
    3: {"name": "The Empress", "name_zh": "女皇"},
    4: {"name": "The Emperor", "name_zh": "皇帝"},
    5: {"name": "The Hierophant", "name_zh": "教皇"},
    6: {"name": "The Lovers", "name_zh": "恋人"},
    7: {"name": "The Chariot", "name_zh": "战车"},
    8: {"name": "Strength", "name_zh": "力量"},
    9: {"name": "The Hermit", "name_zh": "隐士"},
    10: {"name": "Wheel of Fortune", "name_zh": "命运之轮"},
    11: {"name": "Justice", "name_zh": "正义"},
    12: {"name": "The Hanged Man", "name_zh": "倒吊人"},
    13: {"name": "Death", "name_zh": "死神"},
    14: {"name": "Temperance", "name_zh": "节制"},
    15: {"name": "The Devil", "name_zh": "恶魔"},
    16: {"name": "The Tower", "name_zh": "塔"},
    17: {"name": "The Star", "name_zh": "星星"},
    18: {"name": "The Moon", "name_zh": "月亮"},
    19: {"name": "The Sun", "name_zh": "太阳"},
    20: {"name": "Judgement", "name_zh": "审判"},
    21: {"name": "The World", "name_zh": "世界"},
}
"""22 Major Arcana cards (0-21)."""


# =============================================================================
# Constants: Minor Arcana (56 cards)
# =============================================================================

SUITS = ["wands", "cups", "swords", "pentacles"]
"""Four suits of Minor Arcana."""

SUIT_NAMES_ZH = {
    "wands": "权杖",
    "cups": "圣杯",
    "swords": "宝剑",
    "pentacles": "钱币",
}

COURT_CARDS = ["Page", "Knight", "Queen", "King"]
"""Court cards in each suit."""

COURT_CARDS_ZH = {
    "Page": "侍从",
    "Knight": "骑士",
    "Queen": "王后",
    "King": "国王",
}

# Generate Minor Arcana: Ace through 10 + Court cards for each suit
MINOR_ARCANA: Dict[int, Dict[str, Any]] = {}
_card_number = 22  # Start after Major Arcana

for suit in SUITS:
    suit_zh = SUIT_NAMES_ZH[suit]
    # Ace through 10
    for rank in range(1, 11):
        rank_name = "Ace" if rank == 1 else str(rank)
        MINOR_ARCANA[_card_number] = {
            "name": f"{rank_name} of {suit.capitalize()}",
            "name_zh": f"{suit_zh}{rank_name if rank > 1 else '王牌'}",
            "suit": suit,
            "rank": rank,
            "is_court": False,
        }
        _card_number += 1
    # Court cards
    for court in COURT_CARDS:
        MINOR_ARCANA[_card_number] = {
            "name": f"{court} of {suit.capitalize()}",
            "name_zh": f"{suit_zh}{COURT_CARDS_ZH[court]}",
            "suit": suit,
            "rank": court,
            "is_court": True,
        }
        _card_number += 1

# Combined card dictionary
ALL_CARDS: Dict[int, Dict[str, Any]] = {}
for num, card in MAJOR_ARCANA.items():
    ALL_CARDS[num] = {**card, "is_major": True, "suit": None}
for num, card in MINOR_ARCANA.items():
    ALL_CARDS[num] = {**card, "is_major": False}


# =============================================================================
# Constants: Spread Types
# =============================================================================

SPREAD_TYPES = {
    "single": {
        "name": "Single Card",
        "name_zh": "单牌",
        "positions": ["answer"],
    },
    "three_card": {
        "name": "Three Card Spread",
        "name_zh": "三牌阵",
        "positions": ["past", "present", "future"],
    },
    "celtic_cross": {
        "name": "Celtic Cross",
        "name_zh": "凯尔特十字",
        "positions": [
            "present", "challenge", "past", "future",
            "above", "below", "advice", "external",
            "hopes_fears", "outcome"
        ],
    },
    "custom": {
        "name": "Custom Spread",
        "name_zh": "自定义牌阵",
        "positions": [],  # User-defined
    },
}

POSITION_MEANINGS = {
    "answer": "The answer to your question",
    "past": "Past influences",
    "present": "Current situation",
    "future": "Future possibilities",
    "challenge": "The challenge or obstacle",
    "above": "Conscious goals",
    "below": "Subconscious influences",
    "advice": "Advice or guidance",
    "external": "External influences",
    "hopes_fears": "Hopes and fears",
    "outcome": "Potential outcome",
}

POSITION_MEANINGS_ZH = {
    "answer": "问题的答案",
    "past": "过去的影响",
    "present": "当前状况",
    "future": "未来可能",
    "challenge": "挑战或障碍",
    "above": "意识层面的目标",
    "below": "潜意识的影响",
    "advice": "建议或指引",
    "external": "外部影响",
    "hopes_fears": "希望与恐惧",
    "outcome": "可能的结果",
}


# =============================================================================
# Helper Models
# =============================================================================

class CardInfo(BaseModel):
    """Card information from input."""
    card_name: str = Field(..., description="Card name (English)")
    reversed: bool = Field(default=False, description="Whether card is reversed")
    position: Optional[str] = Field(None, description="Position in spread")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "card_name": "The Fool",
                "reversed": False,
                "position": "present"
            }
        }
    )


# =============================================================================
# Input Model
# =============================================================================

class TarotInput(BaseModel):
    """
    Tarot interpretation input model.
    
    Does NOT require location information.
    
    Attributes:
        spread_type: Type of spread (single, three_card, celtic_cross, custom)
        cards: List of cards in the spread
        question: Optional question for context
    """
    spread_type: Literal["single", "three_card", "celtic_cross", "custom"] = Field(
        ..., description="牌阵类型"
    )
    cards: List[CardInfo] = Field(
        ..., 
        min_length=1,
        description="牌阵中的牌列表"
    )
    question: Optional[str] = Field(None, description="问题（可选）")
    
    @model_validator(mode='after')
    def validate_spread(self) -> 'TarotInput':
        """Validate that card count matches spread type."""
        expected_counts = {
            "single": 1,
            "three_card": 3,
            "celtic_cross": 10,
            "custom": None,  # Any count allowed
        }
        expected = expected_counts.get(self.spread_type)
        if expected is not None and len(self.cards) != expected:
            raise ValueError(
                f"Spread type '{self.spread_type}' requires {expected} cards, "
                f"but {len(self.cards)} were provided"
            )
        return self
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "spread_type": "three_card",
                "cards": [
                    {"card_name": "The Fool", "reversed": False, "position": "past"},
                    {"card_name": "The Magician", "reversed": True, "position": "present"},
                    {"card_name": "The High Priestess", "reversed": False, "position": "future"},
                ],
                "question": "What should I focus on this month?"
            }
        }
    )


# =============================================================================
# Internal Data Structures
# =============================================================================

class CardInterpretation(BaseModel):
    """Interpretation for a single card."""
    card_name: str = Field(..., description="Card name (English)")
    card_name_zh: str = Field(..., description="Card name (Chinese)")
    card_number: int = Field(..., ge=0, le=77, description="Card number 0-77")
    suit: Optional[Literal["wands", "cups", "swords", "pentacles"]] = Field(
        None, description="Suit for Minor Arcana"
    )
    is_major: bool = Field(..., description="Whether card is Major Arcana")
    reversed: bool = Field(..., description="Whether card is reversed")
    position: str = Field(..., description="Position in spread")
    position_meaning: str = Field(..., description="Meaning of position")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "card_name": "The Fool",
                "card_name_zh": "愚者",
                "card_number": 0,
                "suit": None,
                "is_major": True,
                "reversed": False,
                "position": "present",
                "position_meaning": "Current situation"
            }
        }
    )


# =============================================================================
# Output Model: TarotFactors
# =============================================================================

class TarotFactors(BaseModel):
    """
    Tarot factors output model.
    
    Contains complete interpretation data and provides to_factor_matrix() method
    to convert to unified FactorMatrix format for Layer 2.
    
    Factor ID naming follows data contract: tarot_*
    """
    
    cards: List[CardInterpretation] = Field(
        ..., description="Interpreted cards"
    )
    spread_type: str = Field(..., description="Spread type used")
    question: Optional[str] = Field(None, description="Question asked")
    calculation_time_ms: float = Field(default=0.0, description="Calculation time in ms")
    
    def to_factor_matrix(self) -> FactorMatrix:
        """
        Convert to unified FactorMatrix format.
        
        Factor ID naming follows data contract:
        - tarot_major_the_fool_upright: Major Arcana card upright
        - tarot_major_the_fool_reversed: Major Arcana card reversed
        - tarot_wands_ace_upright: Minor Arcana card upright
        - tarot_spread_three_card: Spread type
        - tarot_position_past_the_fool: Card at position
        
        Returns:
            FactorMatrix: Unified factor matrix
        """
        factors: Dict[str, FactorValue] = {}
        
        # 1. Spread type factor
        factors[f"tarot_spread_{self.spread_type}"] = FactorValue(
            factor_id=f"tarot_spread_{self.spread_type}",
            value=True,
            confidence=1.0,
            source="calculator"
        )
        
        # 2. Card factors
        for card in self.cards:
            # Normalize card name for factor ID
            card_name_normalized = card.card_name.lower().replace(" ", "_").replace("'", "")
            orientation = "reversed" if card.reversed else "upright"
            
            if card.is_major:
                # Major Arcana: tarot_major_{card_name}_{orientation}
                factor_id = f"tarot_major_{card_name_normalized}_{orientation}"
            else:
                # Minor Arcana: tarot_{suit}_{card_name}_{orientation}
                factor_id = f"tarot_{card.suit}_{card_name_normalized}_{orientation}"
            
            factors[factor_id] = FactorValue(
                factor_id=factor_id,
                value=True,
                confidence=1.0,
                source="calculator"
            )
            
            # 3. Position factors
            position_normalized = card.position.lower().replace(" ", "_")
            position_factor_id = f"tarot_position_{position_normalized}_{card_name_normalized}"
            factors[position_factor_id] = FactorValue(
                factor_id=position_factor_id,
                value=True,
                confidence=1.0,
                source="calculator"
            )
            
            # 4. Card number factor
            factors[f"tarot_card_number_{card.card_number}"] = FactorValue(
                factor_id=f"tarot_card_number_{card.card_number}",
                value=True,
                confidence=1.0,
                source="calculator"
            )
        
        # =============================================================
        # 规则兼容因子 (Rule-Compatible Factors)
        # 以下因子是为了兼容现有规则期望的命名约定
        # =============================================================
        
        # 5. 简化卡牌因子 (规则期望 card_name, orientation 格式)
        for i, card in enumerate(self.cards):
            card_name_normalized = card.card_name.lower().replace(" ", "_").replace("'", "")
            orientation = "reversed" if card.reversed else "upright"
            position_normalized = card.position.lower().replace(" ", "_")
            
            # card_name 因子 (按位置)
            factors[f"card_{position_normalized}_name"] = FactorValue(
                factor_id=f"card_{position_normalized}_name",
                value=card_name_normalized,
                confidence=1.0,
                source="calculator"
            )
            
            # orientation 因子 (按位置)
            factors[f"card_{position_normalized}_orientation"] = FactorValue(
                factor_id=f"card_{position_normalized}_orientation",
                value=orientation,
                confidence=1.0,
                source="calculator"
            )
            
            # 按索引的因子
            factors[f"card_{i}_name"] = FactorValue(
                factor_id=f"card_{i}_name",
                value=card.card_name,
                confidence=1.0,
                source="calculator"
            )
            factors[f"card_{i}_reversed"] = FactorValue(
                factor_id=f"card_{i}_reversed",
                value=card.reversed,
                confidence=1.0,
                source="calculator"
            )
        
        # 6. 第一张卡牌主因子 (规则期望简单的 card_name)
        if self.cards:
            first_card = self.cards[0]
            factors["card_name"] = FactorValue(
                factor_id="card_name",
                value=first_card.card_name,
                confidence=1.0,
                source="calculator"
            )
            factors["orientation"] = FactorValue(
                factor_id="orientation",
                value="reversed" if first_card.reversed else "upright",
                confidence=1.0,
                source="calculator"
            )
            factors["position"] = FactorValue(
                factor_id="position",
                value=first_card.position,
                confidence=1.0,
                source="calculator"
            )
            factors["is_major_arcana"] = FactorValue(
                factor_id="is_major_arcana",
                value=first_card.is_major,
                confidence=1.0,
                source="calculator"
            )
        
        # 7. 牌阵统计因子
        factors["card_count"] = FactorValue(
            factor_id="card_count",
            value=len(self.cards),
            confidence=1.0,
            source="calculator"
        )
        factors["reversed_count"] = FactorValue(
            factor_id="reversed_count",
            value=sum(1 for c in self.cards if c.reversed),
            confidence=1.0,
            source="calculator"
        )
        factors["major_arcana_count"] = FactorValue(
            factor_id="major_arcana_count",
            value=sum(1 for c in self.cards if c.is_major),
            confidence=1.0,
            source="calculator"
        )
        
        return FactorMatrix(
            factors=factors,
            timestamp=datetime.now(),
            engine_id="tarot-interpreter"
        )
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "cards": [
                    {
                        "card_name": "The Fool",
                        "card_name_zh": "愚者",
                        "card_number": 0,
                        "suit": None,
                        "is_major": True,
                        "reversed": False,
                        "position": "present",
                        "position_meaning": "Current situation"
                    }
                ],
                "spread_type": "single",
                "question": "What should I focus on?",
                "calculation_time_ms": 1.5
            }
        }
    )
