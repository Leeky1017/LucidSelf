# backend/calculators/astro/models.py
"""
Data models for AstroCalculator.

Follows:
- Architecture v3 §4.1 AstroInput/AstroFactors
- Data Contract §1.1 FactorValue/FactorMatrix
- Factor ID naming: astro_* (underscore format)
"""

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Any
from pydantic import BaseModel, ConfigDict, Field, model_validator

from backend.core.contracts import FactorValue, FactorMatrix


# =============================================================================
# Constants: Planets
# =============================================================================

PLANETS = [
    "sun", "moon", "mercury", "venus", "mars",
    "jupiter", "saturn", "uranus", "neptune", "pluto"
]
"""10 major celestial bodies for calculation."""

PLANET_NAMES_ZH = {
    "sun": "太阳", "moon": "月亮", "mercury": "水星", "venus": "金星",
    "mars": "火星", "jupiter": "木星", "saturn": "土星",
    "uranus": "天王星", "neptune": "海王星", "pluto": "冥王星"
}

# Swiss Ephemeris planet constants
# SE_SUN=0, SE_MOON=1, SE_MERCURY=2, SE_VENUS=3, SE_MARS=4,
# SE_JUPITER=5, SE_SATURN=6, SE_URANUS=7, SE_NEPTUNE=8, SE_PLUTO=9
PLANET_SE_IDS = {
    "sun": 0, "moon": 1, "mercury": 2, "venus": 3, "mars": 4,
    "jupiter": 5, "saturn": 6, "uranus": 7, "neptune": 8, "pluto": 9
}


# =============================================================================
# Constants: Signs
# =============================================================================

SIGNS = [
    "aries", "taurus", "gemini", "cancer", "leo", "virgo",
    "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"
]
"""12 zodiac signs in order."""

SIGN_NAMES_ZH = {
    "aries": "白羊座", "taurus": "金牛座", "gemini": "双子座",
    "cancer": "巨蟹座", "leo": "狮子座", "virgo": "处女座",
    "libra": "天秤座", "scorpio": "天蝎座", "sagittarius": "射手座",
    "capricorn": "摩羯座", "aquarius": "水瓶座", "pisces": "双鱼座"
}

SIGN_SYMBOLS = {
    "aries": "♈", "taurus": "♉", "gemini": "♊", "cancer": "♋",
    "leo": "♌", "virgo": "♍", "libra": "♎", "scorpio": "♏",
    "sagittarius": "♐", "capricorn": "♑", "aquarius": "♒", "pisces": "♓"
}


# =============================================================================
# Constants: Aspects
# =============================================================================

ASPECT_TYPES = ["conjunction", "opposition", "trine", "square", "sextile"]
"""Major aspects."""

ASPECT_ANGLES = {
    "conjunction": 0.0,
    "opposition": 180.0,
    "trine": 120.0,
    "square": 90.0,
    "sextile": 60.0,
}

ASPECT_ORBS = {
    "conjunction": 8.0,
    "opposition": 8.0,
    "trine": 8.0,
    "square": 7.0,
    "sextile": 6.0,
}
"""Default orbs for each aspect type (degrees)."""

ASPECT_NAMES_ZH = {
    "conjunction": "合相", "opposition": "冲相", "trine": "三合",
    "square": "四分", "sextile": "六合"
}


# =============================================================================
# Constants: House Systems
# =============================================================================

HOUSE_SYSTEMS = {
    "placidus": b'P',
    "koch": b'K',
    "equal": b'E',
    "whole_sign": b'W',
}
"""House system codes for Swiss Ephemeris."""


# =============================================================================
# Input Model
# =============================================================================

class AstroInput(BaseModel):
    """
    Western astrology calculation input model.
    
    Supports two location input methods:
    1. birth_location: Direct coordinates (backward compatible)
    2. birth_place: City name, resolved via GeocodingService
    
    Priority: birth_location > birth_place
    
    Attributes:
        birth_datetime: Birth date and time (Gregorian calendar)
        birth_place: Birth place name (Chinese or English)
        birth_location: (longitude, latitude) for house calculation
        timezone: Timezone identifier
        house_system: House system to use (default: Placidus)
    """
    birth_datetime: datetime = Field(..., description="出生日期时间 (公历)")
    birth_place: Optional[str] = Field(
        default=None,
        description="出生地名（中文或英文），如 '北京' 或 'New York, USA'"
    )
    birth_location: Optional[tuple[float, float]] = Field(
        default=None,
        description="(经度, 纬度)，经度范围-180~180，纬度范围-90~90"
    )
    timezone: Optional[str] = Field(
        default=None,
        description="时区标识，如 'Asia/Shanghai', 'America/New_York'"
    )
    house_system: Literal["placidus", "koch", "equal", "whole_sign"] = Field(
        default="placidus",
        description="宫位系统"
    )
    
    @model_validator(mode='after')
    def validate_location(self) -> 'AstroInput':
        """Validate that at least one location field is provided."""
        if not self.birth_place and not self.birth_location:
            raise ValueError("Either birth_place or birth_location must be provided")
        return self
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "birth_datetime": "1990-05-15T14:30:00",
                "birth_location": [116.4, 39.9],
                "timezone": "Asia/Shanghai",
                "house_system": "placidus"
            }
        }
    )


# =============================================================================
# Internal Data Structures
# =============================================================================

class PlanetPosition(BaseModel):
    """Planetary position data."""
    planet: str = Field(..., description="Planet name (lowercase)")
    longitude: float = Field(..., ge=0.0, lt=360.0, description="Ecliptic longitude 0-360°")
    latitude: float = Field(..., ge=-90.0, le=90.0, description="Ecliptic latitude")
    distance: float = Field(..., gt=0.0, description="Distance in AU")
    speed: float = Field(..., description="Daily motion in degrees/day")
    sign: str = Field(..., description="Zodiac sign")
    degree_in_sign: float = Field(..., ge=0.0, lt=30.0, description="Degree within sign 0-30°")
    house: int = Field(..., ge=1, le=12, description="House placement 1-12")
    retrograde: bool = Field(..., description="Whether planet is retrograde")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "planet": "sun",
                "longitude": 54.5,
                "latitude": 0.0,
                "distance": 1.01,
                "speed": 0.98,
                "sign": "taurus",
                "degree_in_sign": 24.5,
                "house": 10,
                "retrograde": False
            }
        }
    )


class Aspect(BaseModel):
    """Aspect between two planets."""
    planet1: str = Field(..., description="First planet")
    planet2: str = Field(..., description="Second planet")
    aspect_type: Literal["conjunction", "opposition", "trine", "square", "sextile"] = Field(
        ..., description="Aspect type"
    )
    exact_angle: float = Field(..., description="Exact angle between planets")
    orb: float = Field(..., ge=0.0, description="Actual orb (deviation from exact)")
    applying: bool = Field(..., description="Whether aspect is applying (forming)")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "planet1": "sun",
                "planet2": "moon",
                "aspect_type": "trine",
                "exact_angle": 118.5,
                "orb": 1.5,
                "applying": True
            }
        }
    )


# =============================================================================
# Output Model: AstroFactors
# =============================================================================

class AstroFactors(BaseModel):
    """
    Western astrology factors output model.
    
    Contains complete chart data and provides to_factor_matrix() method
    to convert to unified FactorMatrix format for Layer 2.
    
    Factor ID naming follows data contract: astro_*
    """
    
    # Planetary positions
    planets: Dict[str, PlanetPosition] = Field(
        ...,
        description="Planet positions keyed by planet name"
    )
    
    # House cusps
    houses: Dict[int, float] = Field(
        ...,
        description="House cusp degrees (1-12)"
    )
    
    # Angles
    ascendant: float = Field(..., ge=0.0, lt=360.0, description="Ascendant degree")
    midheaven: float = Field(..., ge=0.0, lt=360.0, description="Midheaven (MC) degree")
    ascendant_sign: str = Field(..., description="Ascendant sign")
    midheaven_sign: str = Field(..., description="Midheaven sign")
    
    # Aspects
    aspects: List[Aspect] = Field(default_factory=list, description="List of aspects")
    
    # Metadata
    julian_day: float = Field(..., description="Julian Day number (for debugging)")
    house_system: str = Field(default="placidus", description="House system used")
    calculation_time_ms: float = Field(default=0.0, description="Calculation time in ms")
    
    def to_factor_matrix(self) -> FactorMatrix:
        """
        Convert to unified FactorMatrix format.
        
        Factor ID naming follows data contract:
        - astro_sun_in_taurus: Planet in sign
        - astro_sun_house_10: Planet in house
        - astro_sun_retrograde: Planet retrograde status
        - astro_ascendant: Ascendant sign
        - astro_sun_trine_moon: Aspect between planets
        
        Returns:
            FactorMatrix: Unified factor matrix
        """
        factors: Dict[str, FactorValue] = {}
        
        # 1. Planet in sign factors
        for planet, pos in self.planets.items():
            factor_id = f"astro_{planet}_in_{pos.sign}"
            factors[factor_id] = FactorValue(
                factor_id=factor_id,
                value=True,
                confidence=1.0,
                source="calculator"
            )
            
            # 2. Planet in house factors
            factor_id = f"astro_{planet}_house_{pos.house}"
            factors[factor_id] = FactorValue(
                factor_id=factor_id,
                value=True,
                confidence=1.0,
                source="calculator"
            )
            
            # 3. Retrograde factors
            if pos.retrograde:
                factor_id = f"astro_{planet}_retrograde"
                factors[factor_id] = FactorValue(
                    factor_id=factor_id,
                    value=True,
                    confidence=1.0,
                    source="calculator"
                )
            
            # 4. Planet degree (numeric factor)
            factor_id = f"astro_{planet}_longitude"
            factors[factor_id] = FactorValue(
                factor_id=factor_id,
                value=pos.longitude,
                confidence=1.0,
                source="calculator"
            )
        
        # 5. Ascendant sign
        factors["astro_ascendant"] = FactorValue(
            factor_id="astro_ascendant",
            value=self.ascendant_sign,
            confidence=1.0,
            source="calculator"
        )
        
        # 6. Midheaven sign
        factors["astro_midheaven"] = FactorValue(
            factor_id="astro_midheaven",
            value=self.midheaven_sign,
            confidence=1.0,
            source="calculator"
        )
        
        # 7. Ascendant degree
        factors["astro_ascendant_degree"] = FactorValue(
            factor_id="astro_ascendant_degree",
            value=self.ascendant,
            confidence=1.0,
            source="calculator"
        )
        
        # 8. Midheaven degree
        factors["astro_midheaven_degree"] = FactorValue(
            factor_id="astro_midheaven_degree",
            value=self.midheaven,
            confidence=1.0,
            source="calculator"
        )
        
        # 9. Aspect factors
        for aspect in self.aspects:
            factor_id = f"astro_{aspect.planet1}_{aspect.aspect_type}_{aspect.planet2}"
            # Confidence based on orb tightness
            max_orb = ASPECT_ORBS.get(aspect.aspect_type, 8.0)
            confidence = max(0.0, 1.0 - (aspect.orb / max_orb))
            factors[factor_id] = FactorValue(
                factor_id=factor_id,
                value=True,
                confidence=confidence,
                source="calculator"
            )
        
        # 10. House cusp degrees
        for house_num, degree in self.houses.items():
            factor_id = f"astro_house_{house_num}_cusp"
            factors[factor_id] = FactorValue(
                factor_id=factor_id,
                value=degree,
                confidence=1.0,
                source="calculator"
            )
        
        # =============================================================
        # 规则兼容因子 (Rule-Compatible Factors)
        # 以下因子是为了兼容现有规则期望的命名约定
        # =============================================================
        
        # 11. 行星星座 (string factors) - 规则期望 sun_sign == "gemini"
        for planet, pos in self.planets.items():
            factor_id = f"{planet}_sign"
            factors[factor_id] = FactorValue(
                factor_id=factor_id,
                value=pos.sign,
                confidence=1.0,
                source="calculator"
            )
            
            # 12. 行星宫位 (int factors) - 规则期望 sun_house == 7
            factor_id = f"{planet}_house"
            factors[factor_id] = FactorValue(
                factor_id=factor_id,
                value=pos.house,
                confidence=1.0,
                source="calculator"
            )
            
            # 13. 行星度数 (float factors) - 规则期望 sun_degree
            factor_id = f"{planet}_degree"
            factors[factor_id] = FactorValue(
                factor_id=factor_id,
                value=pos.degree_in_sign,
                confidence=1.0,
                source="calculator"
            )
        
        # 14. 日月相位 (for common aspect rules)
        if "sun" in self.planets and "moon" in self.planets:
            sun_lon = self.planets["sun"].longitude
            moon_lon = self.planets["moon"].longitude
            diff = abs(sun_lon - moon_lon)
            if diff > 180:
                diff = 360 - diff
            
            factors["sun_moon_orb"] = FactorValue(
                factor_id="sun_moon_orb",
                value=diff,
                confidence=1.0,
                source="calculator"
            )
            
            # 判断相位类型
            aspect_type = None
            if diff <= 10:
                aspect_type = "conjunction"
            elif abs(diff - 60) <= 6:
                aspect_type = "sextile"
            elif abs(diff - 90) <= 7:
                aspect_type = "square"
            elif abs(diff - 120) <= 8:
                aspect_type = "trine"
            elif abs(diff - 180) <= 10:
                aspect_type = "opposition"
            
            if aspect_type:
                factors["sun_moon_aspect"] = FactorValue(
                    factor_id="sun_moon_aspect",
                    value=aspect_type,
                    confidence=1.0,
                    source="calculator"
                )
        
        # 15. 通用相位因子 (for aspect rules)
        for aspect in self.aspects:
            # aspect_type 因子
            factors[f"aspect_{aspect.planet1}_{aspect.planet2}_type"] = FactorValue(
                factor_id=f"aspect_{aspect.planet1}_{aspect.planet2}_type",
                value=aspect.aspect_type,
                confidence=1.0,
                source="calculator"
            )
            factors[f"aspect_{aspect.planet1}_{aspect.planet2}_orb"] = FactorValue(
                factor_id=f"aspect_{aspect.planet1}_{aspect.planet2}_orb",
                value=aspect.orb,
                confidence=1.0,
                source="calculator"
            )
        
        # 16. 通用相位因子 (规则期望 aspect_orb, aspect_type)
        if self.aspects:
            # 使用第一个（最强）相位作为默认
            first_aspect = self.aspects[0]
            factors["aspect_orb"] = FactorValue(
                factor_id="aspect_orb",
                value=first_aspect.orb,
                confidence=1.0,
                source="calculator"
            )
            factors["aspect_type"] = FactorValue(
                factor_id="aspect_type",
                value=first_aspect.aspect_type,
                confidence=1.0,
                source="calculator"
            )
        
        return FactorMatrix(
            factors=factors,
            timestamp=datetime.now(),
            engine_id="astro-calculator"
        )
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "planets": {
                    "sun": {
                        "planet": "sun",
                        "longitude": 54.5,
                        "latitude": 0.0,
                        "distance": 1.01,
                        "speed": 0.98,
                        "sign": "taurus",
                        "degree_in_sign": 24.5,
                        "house": 10,
                        "retrograde": False
                    }
                },
                "houses": {1: 120.5, 2: 150.3},
                "ascendant": 120.5,
                "midheaven": 30.2,
                "ascendant_sign": "leo",
                "midheaven_sign": "taurus",
                "aspects": [],
                "julian_day": 2448000.5,
                "house_system": "placidus",
                "calculation_time_ms": 15.5
            }
        }
    )
