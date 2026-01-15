# backend/calculators/ziwei/models.py
"""
Data models for ZiweiCalculator.

Follows:
- Architecture v3 §4.1 ZiweiInput/ZiweiResult
- Data Contract §1.1 FactorValue/FactorMatrix
- Factor ID naming: §4.4 (underscore format: ziwei_star_ziwei)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Literal, Optional, Any
from enum import Enum
from pydantic import BaseModel, ConfigDict, Field, model_validator

# Import from core contracts
from backend.core.contracts import FactorValue, FactorMatrix


# =============================================================================
# Constants: 天干地支
# =============================================================================

HEAVENLY_STEMS = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
EARTHLY_BRANCHES = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

STEM_PINYIN = {
    "甲": "jia", "乙": "yi", "丙": "bing", "丁": "ding", "戊": "wu",
    "己": "ji", "庚": "geng", "辛": "xin", "壬": "ren", "癸": "gui"
}

BRANCH_PINYIN = {
    "子": "zi", "丑": "chou", "寅": "yin", "卯": "mao", "辰": "chen", "巳": "si",
    "午": "wu", "未": "wei", "申": "shen", "酉": "you", "戌": "xu", "亥": "hai"
}

# =============================================================================
# Constants: 十二宫
# =============================================================================

PALACE_NAMES = [
    "命宫", "兄弟宫", "夫妻宫", "子女宫", "财帛宫", "疾厄宫",
    "迁移宫", "交友宫", "官禄宫", "田宅宫", "福德宫", "父母宫"
]

PALACE_PINYIN = {
    "命宫": "ming", "兄弟宫": "xiongdi", "夫妻宫": "fuqi", "子女宫": "zinv",
    "财帛宫": "caibo", "疾厄宫": "jie", "迁移宫": "qianyi", "交友宫": "jiaoyou",
    "官禄宫": "guanlu", "田宅宫": "tianzhai", "福德宫": "fude", "父母宫": "fumu"
}

# 身宫可能落入的宫位
BODY_PALACE_OPTIONS = ["命宫", "夫妻宫", "财帛宫", "迁移宫", "官禄宫", "福德宫"]

# =============================================================================
# Constants: 十四主星
# =============================================================================

# 紫微星系 (6星)
ZIWEI_STAR_GROUP = ["紫微", "天机", "太阳", "武曲", "天同", "廉贞"]

# 天府星系 (8星)
TIANFU_STAR_GROUP = ["天府", "太阴", "贪狼", "巨门", "天相", "天梁", "七杀", "破军"]

MAIN_STARS = ZIWEI_STAR_GROUP + TIANFU_STAR_GROUP

STAR_PINYIN = {
    "紫微": "ziwei", "天机": "tianji", "太阳": "taiyang", "武曲": "wuqu",
    "天同": "tiantong", "廉贞": "lianzhen", "天府": "tianfu", "太阴": "taiyin",
    "贪狼": "tanlang", "巨门": "jumen", "天相": "tianxiang", "天梁": "tianliang",
    "七杀": "qisha", "破军": "pojun",
    # 辅星
    "左辅": "zuofu", "右弼": "youbi", "文昌": "wenchang", "文曲": "wenqu",
    "天魁": "tiankui", "天钺": "tianyue", "禄存": "lucun", "天马": "tianma",
    # 煞星
    "擎羊": "qingyang", "陀罗": "tuoluo", "火星": "huoxing", "铃星": "lingxing",
    "地空": "dikong", "地劫": "dijie",
}

# =============================================================================
# Constants: 辅星与煞星
# =============================================================================

AUXILIARY_STARS = ["左辅", "右弼", "文昌", "文曲", "天魁", "天钺", "禄存", "天马"]
SHA_STARS = ["擎羊", "陀罗", "火星", "铃星", "地空", "地劫"]

# =============================================================================
# Constants: 四化
# =============================================================================

SIHUA_TYPES = ["化禄", "化权", "化科", "化忌"]
SIHUA_PINYIN = {"化禄": "lu", "化权": "quan", "化科": "ke", "化忌": "ji"}

# =============================================================================
# Constants: 五行局
# =============================================================================

FIVE_ELEMENT_TYPES = {
    "水二局": ("water", 2),
    "木三局": ("wood", 3),
    "金四局": ("metal", 4),
    "土五局": ("earth", 5),
    "火六局": ("fire", 6),
}

# =============================================================================
# Constants: 星曜亮度
# =============================================================================

class StarBrightness(str, Enum):
    """星曜亮度等级"""
    MIAO = "庙"      # 最强
    WANG = "旺"
    DEDI = "得地"
    LI = "利"
    PING = "平"
    BUDEDI = "不得地"
    LUOXIAN = "落陷"  # 最弱


# =============================================================================
# Input Model
# =============================================================================

class ZiweiInput(BaseModel):
    """
    紫微斗数计算输入模型 - 符合架构文档 §4.1 定义，支持 Geocoding 集成.
    
    支持两种位置输入方式：
    1. birth_location: 直接提供经纬度坐标（向后兼容）
    2. birth_place: 提供城市名，通过 GeocodingService 解析
    
    优先级：birth_location > birth_place
    
    Attributes:
        birth_datetime: 出生日期时间 (公历)
        birth_place: 出生地名（中文或英文），如 '北京' 或 'New York'
        birth_location: (经度, 纬度) 用于真太阳时计算
        gender: 性别，用于大限顺逆判断
        timezone: 时区标识
        calendar_type: 历法类型，默认公历
    """
    birth_datetime: datetime = Field(..., description="出生日期时间 (公历)")
    birth_place: Optional[str] = Field(
        default=None,
        description="出生地名（中文或英文），如 '北京' 或 'New York, USA'"
    )
    birth_location: Optional[tuple[float, float]] = Field(
        default=None, 
        description="(经度, 纬度)，经度范围-180~180，纬度范围-90~90。向后兼容字段"
    )
    gender: Literal["male", "female"] = Field(..., description="性别")
    timezone: Optional[str] = Field(
        default=None,
        description="时区标识，如 'Asia/Shanghai', 'America/New_York'。为空则从位置自动推断"
    )
    calendar_type: str = Field(default="gregorian", description="历法类型")
    
    @model_validator(mode='after')
    def validate_location(self) -> 'ZiweiInput':
        """
        验证位置字段：至少需要提供 birth_place 或 birth_location 之一。
        
        Raises:
            ValueError: 当两者都未提供时
        """
        if not self.birth_place and not self.birth_location:
            raise ValueError("Either birth_place or birth_location must be provided")
        return self
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "birth_datetime": "1990-05-15T14:30:00",
                "birth_location": [116.4, 39.9],
                "gender": "male",
                "timezone": "Asia/Shanghai",
                "calendar_type": "gregorian"
            },
            "examples": [
                {
                    "description": "使用坐标（向后兼容）",
                    "birth_datetime": "1990-05-15T14:30:00",
                    "birth_location": [116.4, 39.9],
                    "gender": "male"
                },
                {
                    "description": "使用城市名（新方式）",
                    "birth_datetime": "1990-05-15T14:30:00",
                    "birth_place": "北京",
                    "gender": "male"
                }
            ]
        }
    )


# =============================================================================
# Internal Data Structures
# =============================================================================

@dataclass
class Star:
    """星曜信息"""
    name: str                                    # 星曜名称
    star_type: Literal["main", "auxiliary", "sha"]  # 星曜类型
    palace_index: int                            # 所在宫位索引 (0-11)
    brightness: Optional[StarBrightness] = None  # 亮度
    
    @property
    def pinyin(self) -> str:
        return STAR_PINYIN.get(self.name, self.name)


@dataclass
class SiHua:
    """四化信息"""
    sihua_type: Literal["化禄", "化权", "化科", "化忌"]
    star_name: str                               # 所落星曜
    source: Literal["natal", "decade", "annual"] # 来源：生年/大限/流年
    source_stem: str                             # 来源天干
    
    @property
    def pinyin(self) -> str:
        return SIHUA_PINYIN.get(self.sihua_type, "")


@dataclass
class Palace:
    """宫位信息"""
    name: str                                    # 宫位名称
    index: int                                   # 宫位索引 (0-11, 0=命宫)
    branch: str                                  # 地支
    stem: str                                    # 天干
    main_stars: List[str] = field(default_factory=list)      # 主星列表
    auxiliary_stars: List[str] = field(default_factory=list) # 辅星列表
    sha_stars: List[str] = field(default_factory=list)       # 煞星列表
    sihua_list: List[SiHua] = field(default_factory=list)    # 四化列表
    
    @property
    def pinyin(self) -> str:
        return PALACE_PINYIN.get(self.name, self.name)
    
    @property
    def all_stars(self) -> List[str]:
        return self.main_stars + self.auxiliary_stars + self.sha_stars


@dataclass
class Decade:
    """大限信息"""
    palace_index: int                            # 大限宫位索引
    palace_name: str                             # 大限宫位名称
    stem: str                                    # 大限天干
    branch: str                                  # 大限地支
    start_age: int                               # 起始年龄（虚岁）
    end_age: int                                 # 结束年龄（虚岁）
    sihua_list: List[SiHua] = field(default_factory=list)  # 大限四化
    
    def __str__(self) -> str:
        return f"{self.palace_name} ({self.start_age}-{self.end_age}岁)"


@dataclass
class LunarDate:
    """农历日期"""
    year: int
    month: int
    day: int
    is_leap_month: bool = False
    year_stem: str = ""      # 年干
    year_branch: str = ""    # 年支
    month_stem: str = ""     # 月干
    month_branch: str = ""   # 月支
    day_stem: str = ""       # 日干
    day_branch: str = ""     # 日支
    hour_branch: str = ""    # 时支


@dataclass
class ZiweiChart:
    """完整紫微斗数命盘"""
    # 基础信息
    lunar_date: LunarDate
    gender: Literal["male", "female"]
    
    # 五行局
    five_element_type: str                       # 如 "水二局"
    five_element_number: int                     # 如 2
    
    # 十二宫
    palaces: List[Palace]                        # 12个宫位
    ming_palace_index: int                       # 命宫索引
    body_palace_index: int                       # 身宫索引
    
    # 星曜
    stars: List[Star]                            # 所有星曜
    
    # 四化
    natal_sihua: List[SiHua]                     # 生年四化
    
    # 大限
    decade_list: List[Decade]                    # 大限列表
    decade_direction: Literal["forward", "backward"]  # 大限顺逆
    start_decade_age: int                        # 起运岁数


# =============================================================================
# Output Model: ZiweiFactors
# =============================================================================

class ZiweiFactors(BaseModel):
    """
    紫微斗数因子输出模型 - Calculator 层计算产出.
    
    包含完整的紫微斗数命盘信息，并提供 to_factor_matrix() 方法
    将结果转换为统一的 FactorMatrix 格式供 Layer 2 使用。
    
    Factor ID 命名符合数据契约 §4.4 规范（下划线格式）。
    """
    
    # 基础信息
    lunar_year: int = Field(..., description="农历年")
    lunar_month: int = Field(..., description="农历月")
    lunar_day: int = Field(..., description="农历日")
    is_leap_month: bool = Field(default=False, description="是否闰月")
    year_stem: str = Field(..., description="年干")
    year_branch: str = Field(..., description="年支")
    hour_branch: str = Field(..., description="时支")
    gender: Literal["male", "female"] = Field(..., description="性别")
    
    # 五行局
    five_element_type: str = Field(..., description="五行局名称，如'水二局'")
    five_element_number: int = Field(..., description="五行局数字，如2")
    
    # 宫位信息
    palaces: Dict[str, Dict[str, Any]] = Field(
        ..., 
        description="十二宫信息，格式: {宫名: {branch, stem, main_stars, ...}}"
    )
    ming_palace_branch: str = Field(..., description="命宫地支")
    body_palace_name: str = Field(..., description="身宫名称")
    
    # 星曜分布
    main_stars: Dict[str, str] = Field(
        ..., 
        description="主星所在宫位，格式: {星名: 宫名}"
    )
    auxiliary_stars: Dict[str, str] = Field(
        default_factory=dict,
        description="辅星所在宫位"
    )
    sha_stars: Dict[str, str] = Field(
        default_factory=dict,
        description="煞星所在宫位"
    )
    
    # 星曜亮度
    star_brightness: Dict[str, str] = Field(
        default_factory=dict,
        description="星曜亮度，格式: {星名: 亮度}"
    )
    
    # 四化信息
    sihua_natal: Dict[str, str] = Field(
        ..., 
        description="生年四化，格式: {化禄: 星名, 化权: 星名, ...}"
    )
    sihua_decade: Dict[str, str] = Field(
        default_factory=dict,
        description="大限四化（当前大限）"
    )
    sihua_annual: Dict[str, str] = Field(
        default_factory=dict,
        description="流年四化（当前流年或指定流年）"
    )
    
    # 大限信息
    decade_list: List[Dict[str, Any]] = Field(
        default_factory=list,
        description="大限列表"
    )
    current_decade: Optional[Dict[str, Any]] = Field(
        default=None,
        description="当前大限信息"
    )
    decade_direction: Literal["forward", "backward"] = Field(
        ...,
        description="大限顺逆"
    )
    start_decade_age: int = Field(..., description="起运岁数（虚岁），等于五行局数")
    
    # 元数据
    calculation_time_ms: float = Field(default=0.0, description="计算耗时(ms)")
    
    def to_factor_matrix(self) -> FactorMatrix:
        """
        转换为统一的 FactorMatrix 格式.
        
        Factor ID 命名符合数据契约 §4.4:
        - ziwei_star_ziwei_palace: "ming" (紫微星所在宫位)
        - ziwei_palace_ming_main_star: "ziwei,tianfu" (命宫主星)
        - ziwei_transform_lu_star: "lianzhen" (化禄所落星曜)
        - ziwei_five_element_type: "water_2" (五行局)
        
        Returns:
            FactorMatrix: 统一因子矩阵
        """
        factors: Dict[str, FactorValue] = {}
        
        # 1. 五行局
        element, number = FIVE_ELEMENT_TYPES.get(
            self.five_element_type, ("unknown", 0)
        )
        factors["ziwei_five_element_type"] = FactorValue(
            factor_id="ziwei_five_element_type",
            value=f"{element}_{number}",
            confidence=1.0,
            source="calculator"
        )
        
        # 2. 主星所在宫位
        for star_name, palace_name in self.main_stars.items():
            pinyin = STAR_PINYIN.get(star_name, star_name)
            palace_pinyin = PALACE_PINYIN.get(palace_name, palace_name)
            factor_id = f"ziwei_star_{pinyin}_palace"
            factors[factor_id] = FactorValue(
                factor_id=factor_id,
                value=palace_pinyin,
                confidence=1.0,
                source="calculator"
            )
        
        # 3. 各宫主星
        for palace_name, palace_info in self.palaces.items():
            palace_pinyin = PALACE_PINYIN.get(palace_name, palace_name)
            main_stars = palace_info.get("main_stars", [])
            if main_stars:
                star_pinyins = [STAR_PINYIN.get(s, s) for s in main_stars]
                factor_id = f"ziwei_palace_{palace_pinyin}_main_star"
                factors[factor_id] = FactorValue(
                    factor_id=factor_id,
                    value=",".join(star_pinyins),
                    confidence=1.0,
                    source="calculator"
                )
        
        # 4. 生年四化
        for sihua_type, star_name in self.sihua_natal.items():
            sihua_pinyin = SIHUA_PINYIN.get(sihua_type, sihua_type)
            star_pinyin = STAR_PINYIN.get(star_name, star_name)
            factor_id = f"ziwei_transform_{sihua_pinyin}_star"
            factors[factor_id] = FactorValue(
                factor_id=factor_id,
                value=star_pinyin,
                confidence=1.0,
                source="calculator"
            )
        
        # 5. 大限四化（如果有）
        for sihua_type, star_name in self.sihua_decade.items():
            sihua_pinyin = SIHUA_PINYIN.get(sihua_type, sihua_type)
            star_pinyin = STAR_PINYIN.get(star_name, star_name)
            factor_id = f"ziwei_decade_transform_{sihua_pinyin}_star"
            factors[factor_id] = FactorValue(
                factor_id=factor_id,
                value=star_pinyin,
                confidence=1.0,
                source="calculator"
            )
        
        # 6. 流年四化（如果有）
        for sihua_type, star_name in self.sihua_annual.items():
            sihua_pinyin = SIHUA_PINYIN.get(sihua_type, sihua_type)
            star_pinyin = STAR_PINYIN.get(star_name, star_name)
            factor_id = f"ziwei_annual_transform_{sihua_pinyin}_star"
            factors[factor_id] = FactorValue(
                factor_id=factor_id,
                value=star_pinyin,
                confidence=1.0,
                source="calculator"
            )
        
        # 7. 命宫地支
        factors["ziwei_ming_palace_branch"] = FactorValue(
            factor_id="ziwei_ming_palace_branch",
            value=BRANCH_PINYIN.get(self.ming_palace_branch, self.ming_palace_branch),
            confidence=1.0,
            source="calculator"
        )
        
        # 8. 身宫位置
        factors["ziwei_body_palace"] = FactorValue(
            factor_id="ziwei_body_palace",
            value=PALACE_PINYIN.get(self.body_palace_name, self.body_palace_name),
            confidence=1.0,
            source="calculator"
        )
        
        # 9. 大限方向
        factors["ziwei_decade_forward"] = FactorValue(
            factor_id="ziwei_decade_forward",
            value=(self.decade_direction == "forward"),
            confidence=1.0,
            source="calculator"
        )
        
        # 10. 起运岁数
        factors["ziwei_start_decade_age"] = FactorValue(
            factor_id="ziwei_start_decade_age",
            value=self.start_decade_age,
            confidence=1.0,
            source="calculator"
        )
        
        # 11. 星曜亮度
        for star_name, brightness in self.star_brightness.items():
            star_pinyin = STAR_PINYIN.get(star_name, star_name)
            factor_id = f"ziwei_star_{star_pinyin}_brightness"
            factors[factor_id] = FactorValue(
                factor_id=factor_id,
                value=brightness,
                confidence=1.0,
                source="calculator"
            )
        
        # =============================================================
        # 规则兼容因子 (Rule-Compatible Factors)
        # 以下因子是为了兼容现有规则期望的命名约定
        # =============================================================
        
        # 12. 主星存在性与宫位因子 (规则期望 xxx_present, xxx_palace 格式)
        for star_name in MAIN_STARS:
            star_pinyin = STAR_PINYIN.get(star_name, star_name)
            palace_name = self.main_stars.get(star_name, "")
            palace_pinyin = PALACE_PINYIN.get(palace_name, palace_name)
            
            # xxx_present 因子
            factors[f"{star_pinyin}_present"] = FactorValue(
                factor_id=f"{star_pinyin}_present",
                value=bool(palace_name),
                confidence=1.0,
                source="calculator"
            )
            
            # xxx_palace 因子 (不带 ziwei_ 前缀的简化版)
            if palace_name:
                factors[f"{star_pinyin}_palace"] = FactorValue(
                    factor_id=f"{star_pinyin}_palace",
                    value=palace_pinyin,
                    confidence=1.0,
                    source="calculator"
                )
        
        # 13. 主星亮度因子 (规则期望 xxx_brightness 格式)
        for star_name in MAIN_STARS:
            star_pinyin = STAR_PINYIN.get(star_name, star_name)
            brightness = self.star_brightness.get(star_name, "")
            
            factors[f"{star_pinyin}_brightness"] = FactorValue(
                factor_id=f"{star_pinyin}_brightness",
                value=brightness,
                confidence=1.0,
                source="calculator"
            )
        
        # 14. 辅星存在性因子
        for star_name in AUXILIARY_STARS:
            star_pinyin = STAR_PINYIN.get(star_name, star_name)
            palace_name = self.auxiliary_stars.get(star_name, "")
            
            factors[f"{star_pinyin}_present"] = FactorValue(
                factor_id=f"{star_pinyin}_present",
                value=bool(palace_name),
                confidence=1.0,
                source="calculator"
            )
        
        # 15. 煞星存在性因子
        for star_name in SHA_STARS:
            star_pinyin = STAR_PINYIN.get(star_name, star_name)
            palace_name = self.sha_stars.get(star_name, "")
            
            factors[f"{star_pinyin}_present"] = FactorValue(
                factor_id=f"{star_pinyin}_present",
                value=bool(palace_name),
                confidence=1.0,
                source="calculator"
            )
        
        # 16. 宫位是否有煞星/忌星 (规则期望 xxx_gong_ji_xing 格式)
        palace_ji_map = {}  # 宫位 -> 是否有化忌
        
        # 找化忌落在哪个宫位
        ji_star_name = self.sihua_natal.get("化忌", "")
        if ji_star_name:
            ji_palace = self.main_stars.get(ji_star_name) or self.auxiliary_stars.get(ji_star_name, "")
            if ji_palace:
                palace_ji_map[ji_palace] = True
        
        for palace_name in PALACE_NAMES:
            palace_pinyin = PALACE_PINYIN.get(palace_name, palace_name)
            # xxx_gong_ji_xing 因子
            factors[f"{palace_pinyin}_gong_ji_xing"] = FactorValue(
                factor_id=f"{palace_pinyin}_gong_ji_xing",
                value=palace_ji_map.get(palace_name, False),
                confidence=1.0,
                source="calculator"
            )
            
            # 宫位是否有煞星
            palace_info = self.palaces.get(palace_name, {})
            sha_list = palace_info.get("sha_stars", [])
            factors[f"{palace_pinyin}_gong_sha_xing"] = FactorValue(
                factor_id=f"{palace_pinyin}_gong_sha_xing",
                value=len(sha_list) > 0,
                confidence=1.0,
                source="calculator"
            )
        
        # 17. 命宫主星因子 (方便规则直接检查)
        ming_palace_info = self.palaces.get("命宫", {})
        ming_main_stars = ming_palace_info.get("main_stars", [])
        factors["ming_gong_main_star"] = FactorValue(
            factor_id="ming_gong_main_star",
            value=",".join([STAR_PINYIN.get(s, s) for s in ming_main_stars]) if ming_main_stars else "",
            confidence=1.0,
            source="calculator"
        )
        
        # 18. 命宫是否无主星
        factors["ming_gong_empty"] = FactorValue(
            factor_id="ming_gong_empty",
            value=len(ming_main_stars) == 0,
            confidence=1.0,
            source="calculator"
        )
        
        # =============================================================
        # 规则兼容因子扩展 (完整覆盖规则期望的所有因子)
        # =============================================================
        
        # 19. 命宫星曜与亮度 (规则期望 ming_gong_star, ming_gong_brightness)
        factors["ming_gong_star"] = FactorValue(
            factor_id="ming_gong_star",
            value=",".join([STAR_PINYIN.get(s, s) for s in ming_main_stars]) if ming_main_stars else "",
            confidence=1.0, source="calculator"
        )
        # 命宫亮度 - 取第一个主星亮度
        ming_brightness = ""
        if ming_main_stars:
            ming_brightness = self.star_brightness.get(ming_main_stars[0], "")
        factors["ming_gong_brightness"] = FactorValue(
            factor_id="ming_gong_brightness",
            value=ming_brightness,
            confidence=1.0, source="calculator"
        )
        
        # 20. 四化落宫/星 (规则期望 hua_lu_palace, hua_lu_star, hua_ji_palace, hua_ji_star)
        for sihua_type, sihua_pinyin in [("化禄", "hua_lu"), ("化权", "hua_quan"), 
                                          ("化科", "hua_ke"), ("化忌", "hua_ji")]:
            star_name = self.sihua_natal.get(sihua_type, "")
            star_pinyin = STAR_PINYIN.get(star_name, star_name) if star_name else ""
            palace_name = self.main_stars.get(star_name) or self.auxiliary_stars.get(star_name, "")
            palace_pinyin = PALACE_PINYIN.get(palace_name, palace_name) if palace_name else ""
            
            factors[f"{sihua_pinyin}_star"] = FactorValue(
                factor_id=f"{sihua_pinyin}_star",
                value=star_pinyin,
                confidence=1.0, source="calculator"
            )
            factors[f"{sihua_pinyin}_palace"] = FactorValue(
                factor_id=f"{sihua_pinyin}_palace",
                value=palace_pinyin,
                confidence=1.0, source="calculator"
            )
        
        # 21. 煞星存在性 (规则期望 huo_xing_present, ling_xing_present 等)
        sha_star_names = {
            "火星": "huo_xing", "铃星": "ling_xing", 
            "擎羊": "qing_yang", "陀罗": "tuo_luo"
        }
        for zh_name, en_name in sha_star_names.items():
            is_present = zh_name in self.sha_stars
            factors[f"{en_name}_present"] = FactorValue(
                factor_id=f"{en_name}_present",
                value=is_present,
                confidence=1.0, source="calculator"
            )
        
        # 22. 主星详细因子 (规则期望 xxx_present, xxx_palace 格式)
        # 注意：规则使用带下划线的格式如 tan_lang_palace, wu_qu_present
        main_star_mapping = {
            "紫微": "ziwei", "天机": "tian_ji", "太阳": "tai_yang", "武曲": "wu_qu",
            "天同": "tian_tong", "廉贞": "lian_zhen", "天府": "tian_fu", "太阴": "tai_yin",
            "贪狼": "tan_lang", "巨门": "ju_men", "天相": "tian_xiang", "天梁": "tian_liang",
            "七杀": "qi_sha", "破军": "po_jun"
        }
        for zh_name, en_name in main_star_mapping.items():
            palace_name = self.main_stars.get(zh_name, "")
            palace_pinyin = PALACE_PINYIN.get(palace_name, palace_name) if palace_name else ""
            brightness = self.star_brightness.get(zh_name, "")
            
            # xxx_present 因子
            factors[f"{en_name}_present"] = FactorValue(
                factor_id=f"{en_name}_present",
                value=bool(palace_name),
                confidence=1.0, source="calculator"
            )
            # xxx_palace 因子
            factors[f"{en_name}_palace"] = FactorValue(
                factor_id=f"{en_name}_palace",
                value=palace_pinyin,
                confidence=1.0, source="calculator"
            )
            # xxx_brightness 因子
            factors[f"{en_name}_brightness"] = FactorValue(
                factor_id=f"{en_name}_brightness",
                value=brightness,
                confidence=1.0, source="calculator"
            )
        
        # 23. 官禄宫相关 (规则期望 guan_lu_gong_star, guan_lu_gong_brightness, guan_lu_gong_ji_xing)
        guan_lu_info = self.palaces.get("官禄宫", {})
        guan_lu_stars = guan_lu_info.get("main_stars", [])
        factors["guan_lu_gong_star"] = FactorValue(
            factor_id="guan_lu_gong_star",
            value=",".join([STAR_PINYIN.get(s, s) for s in guan_lu_stars]) if guan_lu_stars else "",
            confidence=1.0, source="calculator"
        )
        guan_lu_brightness = self.star_brightness.get(guan_lu_stars[0], "") if guan_lu_stars else ""
        factors["guan_lu_gong_brightness"] = FactorValue(
            factor_id="guan_lu_gong_brightness",
            value=guan_lu_brightness,
            confidence=1.0, source="calculator"
        )
        
        # 添加官禄宫忌星因子
        factors["guan_lu_gong_ji_xing"] = FactorValue(
            factor_id="guan_lu_gong_ji_xing",
            value=palace_ji_map.get("官禄宫", False),
            confidence=1.0, source="calculator"
        )
        
        # 24. 其他宫位因子 (疾厄、迁移、仆役)
        for palace_zh, palace_en in [("疾厄宫", "ji_e"), ("迁移宫", "qian_yi"), 
                                      ("仆役宫", "pu_yi"), ("兄弟宫", "xiong_di"),
                                      ("子女宫", "zi_nv"), ("田宅宫", "tian_zhai"),
                                      ("财帛宫", "cai_bo"), ("福德宫", "fu_de"),
                                      ("父母宫", "fu_mu"), ("夫妻宫", "fu_qi"),
                                      ("官禄宫", "guan_lu")]:  # 添加官禄宫
            p_info = self.palaces.get(palace_zh, {})
            sha_list = p_info.get("sha_stars", [])
            
            # xxx_gong_sha_xing
            factors[f"{palace_en}_gong_sha_xing"] = FactorValue(
                factor_id=f"{palace_en}_gong_sha_xing",
                value=len(sha_list) > 0,
                confidence=1.0, source="calculator"
            )
            # xxx_gong_ji_xing
            factors[f"{palace_en}_gong_ji_xing"] = FactorValue(
                factor_id=f"{palace_en}_gong_ji_xing",
                value=palace_ji_map.get(palace_zh, False),
                confidence=1.0, source="calculator"
            )
        
        # 25. 辅星存在性补充
        aux_star_mapping = {
            "左辅": "zuo_fu", "右弼": "you_bi", 
            "文昌": "wen_chang", "文曲": "wen_qu",
            "天魁": "tian_kui", "天钺": "tian_yue"
        }
        for zh_name, en_name in aux_star_mapping.items():
            is_present = zh_name in self.auxiliary_stars
            factors[f"{en_name}_present"] = FactorValue(
                factor_id=f"{en_name}_present",
                value=is_present,
                confidence=1.0, source="calculator"
            )
        
        # 太阳因子别名 (规则期望 taiyang_xxx)
        taiyang_palace = self.main_stars.get("太阳", "")
        factors["taiyang_palace"] = FactorValue(
            factor_id="taiyang_palace",
            value=PALACE_PINYIN.get(taiyang_palace, taiyang_palace) if taiyang_palace else "",
            confidence=1.0, source="calculator"
        )
        factors["taiyang_brightness"] = FactorValue(
            factor_id="taiyang_brightness",
            value=self.star_brightness.get("太阳", ""),
            confidence=1.0, source="calculator"
        )
        
        # 太阴因子 (tai_yin_xxx)
        taiyin_palace = self.main_stars.get("太阴", "")
        factors["tai_yin_present"] = FactorValue(
            factor_id="tai_yin_present",
            value=bool(taiyin_palace),
            confidence=1.0, source="calculator"
        )
        factors["tai_yin_palace"] = FactorValue(
            factor_id="tai_yin_palace",
            value=PALACE_PINYIN.get(taiyin_palace, taiyin_palace) if taiyin_palace else "",
            confidence=1.0, source="calculator"
        )
        factors["tai_yin_brightness"] = FactorValue(
            factor_id="tai_yin_brightness",
            value=self.star_brightness.get("太阴", ""),
            confidence=1.0, source="calculator"
        )
        
        # 太阳变体 (tai_yang_xxx)
        factors["tai_yang_palace"] = FactorValue(
            factor_id="tai_yang_palace",
            value=PALACE_PINYIN.get(taiyang_palace, taiyang_palace) if taiyang_palace else "",
            confidence=1.0, source="calculator"
        )
        factors["tai_yang_brightness"] = FactorValue(
            factor_id="tai_yang_brightness",
            value=self.star_brightness.get("太阳", ""),
            confidence=1.0, source="calculator"
        )
        
        return FactorMatrix(
            factors=factors,
            timestamp=datetime.now(),
            engine_id="ziwei-calculator"
        )
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "lunar_year": 1990,
                "lunar_month": 4,
                "lunar_day": 21,
                "year_stem": "庚",
                "year_branch": "午",
                "hour_branch": "未",
                "gender": "male",
                "five_element_type": "金四局",
                "five_element_number": 4,
                "ming_palace_branch": "辰",
                "body_palace_name": "迁移宫",
                "sihua_natal": {
                    "化禄": "太阳",
                    "化权": "武曲",
                    "化科": "太阴",
                    "化忌": "天同"
                },
                "decade_direction": "forward",
                "start_decade_age": 4
            }
        }
    )
