# backend/calculators/yijing/models.py
"""
Data models for YijingCalculator.

Follows:
- Architecture v3 §4.1 YijingInput/YijingFactors
- Data Contract §1.1 FactorValue/FactorMatrix
- Factor ID naming: yijing_* (underscore format)

Line Values:
- 6 = 老阴 (Old Yin, moving line, yin changes to yang)
- 7 = 少阳 (Young Yang, static line, yang)
- 8 = 少阴 (Young Yin, static line, yin)
- 9 = 老阳 (Old Yang, moving line, yang changes to yin)
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator

from backend.core.contracts import FactorMatrix, FactorValue


# =============================================================================
# Constants: 八卦 (Trigrams)
# =============================================================================

TRIGRAM_DATA = {
    "乾": {"pinyin": "qian", "lines": (1, 1, 1), "element": "天", "nature": "heaven"},
    "坤": {"pinyin": "kun", "lines": (0, 0, 0), "element": "地", "nature": "earth"},
    "震": {"pinyin": "zhen", "lines": (0, 0, 1), "element": "雷", "nature": "thunder"},
    "巽": {"pinyin": "xun", "lines": (1, 1, 0), "element": "风", "nature": "wind"},
    "坎": {"pinyin": "kan", "lines": (0, 1, 0), "element": "水", "nature": "water"},
    "离": {"pinyin": "li", "lines": (1, 0, 1), "element": "火", "nature": "fire"},
    "艮": {"pinyin": "gen", "lines": (1, 0, 0), "element": "山", "nature": "mountain"},
    "兑": {"pinyin": "dui", "lines": (0, 1, 1), "element": "泽", "nature": "lake"},
}

# Reverse lookup: lines tuple -> trigram name
LINES_TO_TRIGRAM = {v["lines"]: k for k, v in TRIGRAM_DATA.items()}

# Valid line values for divination
VALID_LINE_VALUES = {6, 7, 8, 9}

# Moving line values (老阴 and 老阳)
MOVING_LINE_VALUES = {6, 9}


# =============================================================================
# Input Model
# =============================================================================

class YijingInput(BaseModel):
    """
    六爻计算输入模型.
    
    Supports multiple divination methods:
    - coin: Three-coin toss simulation
    - yarrow: Traditional yarrow stalk method
    - time: Time-based hexagram generation
    - manual: Direct line value input
    
    Attributes:
        divination_method: Method to generate hexagram
        manual_lines: Required for 'manual' method, 6 line values (6/7/8/9)
        birth_place: Optional location for 'time' method (true solar time)
        query_time: Time for 'time' method, defaults to current time
        question: Optional question for context
    """
    divination_method: Literal["coin", "yarrow", "time", "manual"] = Field(
        ..., description="起卦方法"
    )
    manual_lines: Optional[List[int]] = Field(
        default=None,
        description="手动输入的六爻值 (6=老阴, 7=少阳, 8=少阴, 9=老阳)，从初爻到上爻"
    )
    birth_place: Optional[str] = Field(
        default=None,
        description="位置（用于时间起卦的真太阳时计算）"
    )
    query_time: Optional[datetime] = Field(
        default=None,
        description="起卦时间，默认当前时间"
    )
    question: Optional[str] = Field(
        default=None,
        description="所问问题（可选，用于记录）"
    )
    
    @model_validator(mode='after')
    def validate_manual_lines(self) -> 'YijingInput':
        """Validate manual_lines when divination_method is 'manual'."""
        if self.divination_method == 'manual':
            if not self.manual_lines or len(self.manual_lines) != 6:
                raise ValueError("manual method requires exactly 6 line values")
            for i, line in enumerate(self.manual_lines):
                if line not in VALID_LINE_VALUES:
                    raise ValueError(
                        f"Invalid line value at position {i+1}: {line}, "
                        f"must be 6 (老阴), 7 (少阳), 8 (少阴), or 9 (老阳)"
                    )
        return self
    
    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "description": "铜钱法起卦",
                    "divination_method": "coin",
                    "question": "事业发展如何？"
                },
                {
                    "description": "手动输入",
                    "divination_method": "manual",
                    "manual_lines": [7, 8, 9, 7, 6, 8]
                },
                {
                    "description": "时间起卦",
                    "divination_method": "time",
                    "birth_place": "北京",
                    "query_time": "2025-11-29T14:30:00"
                }
            ]
        }
    )


# =============================================================================
# Data Structures
# =============================================================================

class Trigram(BaseModel):
    """八卦 (Trigram) model."""
    name_zh: str = Field(..., description="中文名称")
    name_pinyin: str = Field(..., description="拼音")
    lines: tuple[int, int, int] = Field(
        ..., description="三爻值 (0=阴, 1=阳)，从下到上"
    )
    element: str = Field(..., description="象征元素")
    nature: str = Field(..., description="自然属性")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name_zh": "乾",
                "name_pinyin": "qian",
                "lines": [1, 1, 1],
                "element": "天",
                "nature": "heaven"
            }
        }
    )


class Hexagram(BaseModel):
    """
    卦象 (Hexagram) model.
    
    Represents a complete hexagram with its components.
    """
    number: int = Field(..., ge=1, le=64, description="卦序号 1-64")
    name_zh: str = Field(..., description="中文名称")
    name_pinyin: str = Field(..., description="拼音")
    upper_trigram: str = Field(..., description="上卦名")
    lower_trigram: str = Field(..., description="下卦名")
    lines: List[int] = Field(
        ..., 
        min_length=6, 
        max_length=6,
        description="六爻值 (0=阴, 1=阳)，从初爻到上爻"
    )
    raw_lines: Optional[List[int]] = Field(
        default=None,
        description="原始六爻值 (6/7/8/9)，用于识别动爻"
    )
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "number": 1,
                "name_zh": "乾",
                "name_pinyin": "qian",
                "upper_trigram": "乾",
                "lower_trigram": "乾",
                "lines": [1, 1, 1, 1, 1, 1],
                "raw_lines": [7, 9, 7, 7, 7, 7]
            }
        }
    )


# =============================================================================
# Output Model: YijingFactors
# =============================================================================

class YijingFactors(BaseModel):
    """
    六爻因子输出模型 - Calculator 层计算产出.
    
    包含完整的卦象信息，并提供 to_factor_matrix() 方法
    将结果转换为统一的 FactorMatrix 格式供 Layer 2 使用。
    
    Factor ID 命名符合数据契约规范（yijing_* 前缀）。
    """
    main_hexagram: Hexagram = Field(..., description="主卦")
    mutual_hexagram: Hexagram = Field(..., description="互卦（取2-5爻组成）")
    changed_hexagram: Optional[Hexagram] = Field(
        default=None, 
        description="变卦（动爻变化后），无动爻时为 None"
    )
    moving_lines: List[int] = Field(
        default_factory=list,
        description="动爻位置 (1-6)，空列表表示无动爻"
    )
    divination_method: str = Field(..., description="起卦方法")
    query_time: Optional[datetime] = Field(
        default=None, description="起卦时间"
    )
    question: Optional[str] = Field(default=None, description="所问问题")
    calculation_time_ms: float = Field(default=0.0, description="计算耗时(ms)")
    
    def to_factor_matrix(self) -> FactorMatrix:
        """
        转换为统一的 FactorMatrix 格式.
        
        Factor ID 命名规范:
        - yijing_gua_{pinyin}: 主卦
        - yijing_upper_trigram: 上卦名
        - yijing_lower_trigram: 下卦名
        - yijing_mutual_{pinyin}: 互卦
        - yijing_changed_{pinyin}: 变卦
        - yijing_moving_yao_{n}: 动爻位置
        - yijing_method_{method}: 起卦方法
        
        Returns:
            FactorMatrix: 统一因子矩阵
        """
        factors: Dict[str, FactorValue] = {}
        
        # 1. 主卦因子
        main_factor_id = f"yijing_gua_{self.main_hexagram.name_pinyin}"
        factors[main_factor_id] = FactorValue(
            factor_id=main_factor_id,
            value=True,
            confidence=1.0,
            source="calculator"
        )
        
        # 2. 主卦序号
        factors["yijing_gua_number"] = FactorValue(
            factor_id="yijing_gua_number",
            value=self.main_hexagram.number,
            confidence=1.0,
            source="calculator"
        )
        
        # 3. 上卦/下卦因子
        factors["yijing_upper_trigram"] = FactorValue(
            factor_id="yijing_upper_trigram",
            value=self.main_hexagram.upper_trigram,
            confidence=1.0,
            source="calculator"
        )
        factors["yijing_lower_trigram"] = FactorValue(
            factor_id="yijing_lower_trigram",
            value=self.main_hexagram.lower_trigram,
            confidence=1.0,
            source="calculator"
        )
        
        # 4. 互卦因子
        mutual_factor_id = f"yijing_mutual_{self.mutual_hexagram.name_pinyin}"
        factors[mutual_factor_id] = FactorValue(
            factor_id=mutual_factor_id,
            value=True,
            confidence=1.0,
            source="calculator"
        )
        
        # 5. 动爻因子
        for pos in self.moving_lines:
            factor_id = f"yijing_moving_yao_{pos}"
            factors[factor_id] = FactorValue(
                factor_id=factor_id,
                value=True,
                confidence=1.0,
                source="calculator"
            )
        
        # 6. 变卦因子（仅当有动爻时）
        if self.changed_hexagram:
            changed_factor_id = f"yijing_changed_{self.changed_hexagram.name_pinyin}"
            factors[changed_factor_id] = FactorValue(
                factor_id=changed_factor_id,
                value=True,
                confidence=1.0,
                source="calculator"
            )
        
        # 7. 起卦方法因子
        method_factor_id = f"yijing_method_{self.divination_method}"
        factors[method_factor_id] = FactorValue(
            factor_id=method_factor_id,
            value=True,
            confidence=1.0,
            source="calculator"
        )
        
        # 8. 六爻值因子
        for i, line in enumerate(self.main_hexagram.lines, 1):
            factor_id = f"yijing_line_{i}"
            factors[factor_id] = FactorValue(
                factor_id=factor_id,
                value="yang" if line == 1 else "yin",
                confidence=1.0,
                source="calculator"
            )
        
        # =============================================================
        # 规则兼容因子 (Rule-Compatible Factors)
        # 以下因子是为了兼容现有规则期望的命名约定
        # =============================================================
        
        # 9. 卦序号 (规则期望 hexagram_number)
        factors["hexagram_number"] = FactorValue(
            factor_id="hexagram_number",
            value=self.main_hexagram.number,
            confidence=1.0,
            source="calculator"
        )
        
        # 10. 动爻数量与位置 (规则期望 moving_yao)
        factors["moving_yao"] = FactorValue(
            factor_id="moving_yao",
            value=self.moving_lines[0] if len(self.moving_lines) == 1 else (
                self.moving_lines if self.moving_lines else 0
            ),
            confidence=1.0,
            source="calculator"
        )
        factors["moving_yao_count"] = FactorValue(
            factor_id="moving_yao_count",
            value=len(self.moving_lines),
            confidence=1.0,
            source="calculator"
        )
        
        # 11. 上卦下卦简化名 (规则期望无前缀)
        upper_data = TRIGRAM_DATA.get(self.main_hexagram.upper_trigram, {})
        lower_data = TRIGRAM_DATA.get(self.main_hexagram.lower_trigram, {})
        
        factors["upper_trigram"] = FactorValue(
            factor_id="upper_trigram",
            value=upper_data.get("pinyin", self.main_hexagram.upper_trigram),
            confidence=1.0,
            source="calculator"
        )
        factors["lower_trigram"] = FactorValue(
            factor_id="lower_trigram",
            value=lower_data.get("pinyin", self.main_hexagram.lower_trigram),
            confidence=1.0,
            source="calculator"
        )
        
        # 12. 主卦名称
        factors["hexagram_name"] = FactorValue(
            factor_id="hexagram_name",
            value=self.main_hexagram.name_pinyin,
            confidence=1.0,
            source="calculator"
        )
        
        # 13. 变卦信息
        if self.changed_hexagram:
            factors["changed_hexagram_number"] = FactorValue(
                factor_id="changed_hexagram_number",
                value=self.changed_hexagram.number,
                confidence=1.0,
                source="calculator"
            )
            factors["changed_hexagram_name"] = FactorValue(
                factor_id="changed_hexagram_name",
                value=self.changed_hexagram.name_pinyin,
                confidence=1.0,
                source="calculator"
            )
        else:
            factors["changed_hexagram_number"] = FactorValue(
                factor_id="changed_hexagram_number",
                value=0,
                confidence=1.0,
                source="calculator"
            )
        
        # 14. 是否有动爻
        factors["has_moving_yao"] = FactorValue(
            factor_id="has_moving_yao",
            value=len(self.moving_lines) > 0,
            confidence=1.0,
            source="calculator"
        )
        
        return FactorMatrix(
            factors=factors,
            timestamp=datetime.now(),
            engine_id="yijing-calculator"
        )
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "main_hexagram": {
                    "number": 1,
                    "name_zh": "乾",
                    "name_pinyin": "qian",
                    "upper_trigram": "乾",
                    "lower_trigram": "乾",
                    "lines": [1, 1, 1, 1, 1, 1]
                },
                "mutual_hexagram": {
                    "number": 1,
                    "name_zh": "乾",
                    "name_pinyin": "qian",
                    "upper_trigram": "乾",
                    "lower_trigram": "乾",
                    "lines": [1, 1, 1, 1, 1, 1]
                },
                "changed_hexagram": None,
                "moving_lines": [],
                "divination_method": "coin",
                "calculation_time_ms": 1.5
            }
        }
    )
