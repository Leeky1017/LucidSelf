"""
Geocoding Data Models

地理编码服务的数据模型定义。
"""

from dataclasses import dataclass, asdict, field
from typing import Optional, Literal
import json


@dataclass
class Place:
    """
    Canonical place object returned by geocoding service.
    
    地理编码服务返回的标准地点对象，包含坐标、时区和元数据。
    """
    place_id: str
    """Unique place identifier, e.g., 'gn-2038060'"""
    
    country_code: str
    """ISO 3166-1 alpha-2 country code"""
    
    city_name: str
    """Canonical city name"""
    
    lat: float
    """Latitude"""
    
    lng: float
    """Longitude"""
    
    timezone: str
    """IANA timezone identifier, e.g., 'Asia/Shanghai'"""
    
    source: Literal['local_db', 'amap', 'nominatim', 'manual']
    """Data source indicator"""
    
    accuracy: Literal['city'] = 'city'
    """Resolution accuracy level"""
    
    admin1_code: Optional[str] = None
    """First-level administrative division code"""
    
    admin1_name: Optional[str] = None
    """First-level administrative division name"""
    
    district_name_raw: Optional[str] = None
    """Raw district name for display only"""
    
    def to_dict(self) -> dict:
        """Convert Place to dictionary."""
        return asdict(self)
    
    def to_json(self) -> str:
        """Serialize Place to JSON string."""
        return json.dumps(self.to_dict(), ensure_ascii=False)
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Place':
        """Create Place from dictionary."""
        return cls(**data)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'Place':
        """Deserialize Place from JSON string."""
        data = json.loads(json_str)
        return cls.from_dict(data)


@dataclass
class ResolvePlaceInput:
    """
    Input for place resolution.
    
    地点解析请求的输入参数。
    """
    input_text: str
    """User-provided location text (Chinese or English)"""
    
    hint_country: Optional[str] = None
    """Optional ISO 3166-1 alpha-2 country code hint"""
    
    hint_label: Optional[str] = None
    """Semantic label, e.g., 'birth_place', 'current_city'"""
    
    user_id: Optional[str] = None
    """User identifier for user-level caching"""
