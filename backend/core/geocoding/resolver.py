"""
Location Resolver

位置解析器 - 在 Calculator 外部处理 Geocoding。

设计理由：
1. Calculator 保持纯同步计算，便于测试和复用
2. Geocoding 是 I/O 操作，应在调用层处理
3. 支持批量解析和缓存优化
"""

from typing import Optional, Tuple
import asyncio

from backend.core.geocoding.service import GeocodingService
from backend.core.geocoding.models import Place, ResolvePlaceInput
from backend.core.geocoding.exceptions import InvalidInputError


class LocationResolver:
    """
    位置解析器 - 在 Calculator 外部处理 Geocoding。
    
    设计理由：
    1. Calculator 保持纯同步计算，便于测试和复用
    2. Geocoding 是 I/O 操作，应在调用层处理
    3. 支持批量解析和缓存优化
    
    优先级逻辑：
    - birth_location > birth_place
    - 如果提供了 birth_location，直接使用
    - 如果只提供了 birth_place，通过 GeocodingService 解析
    """
    
    def __init__(self, geocoding_service: Optional[GeocodingService] = None):
        """
        Initialize LocationResolver with optional GeocodingService.
        
        Args:
            geocoding_service: Optional GeocodingService instance.
                              If not provided, a default instance will be created.
        """
        self._geocoding_service = geocoding_service
    
    @property
    def geocoding_service(self) -> GeocodingService:
        """Lazy initialization of GeocodingService."""
        if self._geocoding_service is None:
            self._geocoding_service = GeocodingService()
        return self._geocoding_service
    
    async def resolve(
        self,
        birth_place: Optional[str],
        birth_location: Optional[Tuple[float, float]],
        timezone: Optional[str] = None
    ) -> Tuple[Tuple[float, float], str]:
        """
        解析位置信息（异步版本）。
        
        优先级：birth_location > birth_place
        
        Args:
            birth_place: 出生地名（中文或英文），如 '北京' 或 'New York'
            birth_location: (经度, 纬度) 坐标元组
            timezone: 可选的时区标识，如 'Asia/Shanghai'
        
        Returns:
            Tuple of ((longitude, latitude), timezone)
            
        Raises:
            InvalidInputError: 当 birth_place 和 birth_location 都未提供时
        """
        # 如果已有坐标，直接使用（优先级最高）
        if birth_location is not None:
            # 使用提供的时区，或默认时区
            tz = timezone or "Asia/Shanghai"
            return birth_location, tz
        
        # 通过 Geocoding 解析
        if birth_place is not None and birth_place.strip():
            place = await self.geocoding_service.resolve_place(
                ResolvePlaceInput(input_text=birth_place)
            )
            # 使用提供的时区，或从 Place 获取的时区
            tz = timezone or place.timezone
            return (place.lng, place.lat), tz
        
        # 两者都未提供，抛出错误
        raise InvalidInputError(
            birth_place or "", 
            reason="Either birth_place or birth_location must be provided"
        )
    
    def resolve_sync(
        self,
        birth_place: Optional[str],
        birth_location: Optional[Tuple[float, float]],
        timezone: Optional[str] = None
    ) -> Tuple[Tuple[float, float], str]:
        """
        解析位置信息（同步版本）。
        
        用于非异步上下文。内部使用 asyncio.run() 调用异步版本。
        
        优先级：birth_location > birth_place
        
        Args:
            birth_place: 出生地名（中文或英文），如 '北京' 或 'New York'
            birth_location: (经度, 纬度) 坐标元组
            timezone: 可选的时区标识，如 'Asia/Shanghai'
        
        Returns:
            Tuple of ((longitude, latitude), timezone)
            
        Raises:
            InvalidInputError: 当 birth_place 和 birth_location 都未提供时
        """
        # 如果已有坐标，直接使用（不需要异步调用）
        if birth_location is not None:
            tz = timezone or "Asia/Shanghai"
            return birth_location, tz
        
        # 需要 Geocoding 解析，使用 asyncio.run
        return asyncio.run(self.resolve(birth_place, birth_location, timezone))
