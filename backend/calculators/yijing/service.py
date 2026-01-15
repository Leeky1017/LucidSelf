# backend/calculators/yijing/service.py
"""
YijingCalculator Service Layer - Geocoding 集成入口.

提供 calculate_with_geocoding() 异步方法，自动处理位置解析。

设计理由：
1. Calculator 核心计算保持同步，便于测试和复用
2. Geocoding 是 I/O 操作，在 Service 层异步处理
3. 仅 time 方法需要位置信息（用于真太阳时计算）
4. 其他方法（coin, yarrow, manual）不需要位置

使用示例:
    >>> from backend.calculators.yijing.service import calculate_with_geocoding
    >>> from backend.calculators.yijing.models import YijingInput
    >>> from datetime import datetime
    >>> 
    >>> # 时间起卦 - 使用城市名
    >>> input_data = YijingInput(
    ...     divination_method="time",
    ...     birth_place="北京",
    ...     query_time=datetime.now()
    ... )
    >>> result = await calculate_with_geocoding(input_data)
    >>> 
    >>> # 铜钱法 - 不需要位置
    >>> input_data = YijingInput(divination_method="coin")
    >>> result = await calculate_with_geocoding(input_data)
"""

import logging
from datetime import datetime, timedelta
from typing import Optional, Tuple

from backend.calculators.yijing.calculator import YijingCalculator
from backend.calculators.yijing.models import YijingInput, YijingFactors
from backend.core.geocoding.resolver import LocationResolver
from backend.core.geocoding.service import GeocodingService
from backend.core.geocoding.exceptions import GeocodingError, NotFoundError, InvalidInputError


logger = logging.getLogger(__name__)


def _calculate_true_solar_time(
    query_time: datetime,
    longitude: float,
    timezone_offset_hours: float = 8.0
) -> datetime:
    """
    计算真太阳时。
    
    真太阳时 = 地方平太阳时 + 时差修正
    地方平太阳时 = 标准时 + (经度 - 标准时区中央经线) * 4分钟/度
    
    简化计算：仅考虑经度修正，忽略均时差（equation of time）
    
    Args:
        query_time: 查询时间（标准时区时间）
        longitude: 经度（-180 到 180）
        timezone_offset_hours: 时区偏移小时数（默认 8 = UTC+8）
        
    Returns:
        真太阳时
    """
    # 标准时区中央经线（每个时区 15 度）
    standard_meridian = timezone_offset_hours * 15.0
    
    # 经度差（度）
    longitude_diff = longitude - standard_meridian
    
    # 时间修正（每度 4 分钟）
    time_correction_minutes = longitude_diff * 4.0
    
    # 应用修正
    true_solar_time = query_time + timedelta(minutes=time_correction_minutes)
    
    return true_solar_time


def _get_timezone_offset(timezone: str) -> float:
    """
    获取时区偏移小时数。
    
    Args:
        timezone: 时区标识，如 'Asia/Shanghai'
        
    Returns:
        UTC 偏移小时数
    """
    # 常见时区映射
    timezone_offsets = {
        "Asia/Shanghai": 8.0,
        "Asia/Hong_Kong": 8.0,
        "Asia/Taipei": 8.0,
        "Asia/Tokyo": 9.0,
        "Asia/Seoul": 9.0,
        "Asia/Singapore": 8.0,
        "America/New_York": -5.0,
        "America/Los_Angeles": -8.0,
        "Europe/London": 0.0,
        "Europe/Paris": 1.0,
        "UTC": 0.0,
    }
    
    return timezone_offsets.get(timezone, 8.0)  # 默认 UTC+8


async def calculate_with_geocoding(
    input_data: YijingInput,
    geocoding_service: Optional[GeocodingService] = None,
) -> YijingFactors:
    """
    执行六爻计算，自动处理位置解析（仅 time 方法需要）。
    
    此函数是 YijingCalculator 的 Geocoding 集成入口：
    1. 对于 time 方法：如果提供了 birth_place，解析位置并计算真太阳时
    2. 对于其他方法（coin, yarrow, manual）：直接调用 Calculator
    3. 位置解析失败时，降级使用系统时区并记录警告
    
    Args:
        input_data: 六爻计算输入
        geocoding_service: 可选的 GeocodingService 实例，用于测试注入
        
    Returns:
        YijingFactors: 六爻因子结果
        
    Raises:
        ValueError: 当输入参数无效时（如 manual 方法缺少 lines）
        
    Example:
        >>> # 时间起卦 - 使用城市名
        >>> input_data = YijingInput(
        ...     divination_method="time",
        ...     birth_place="北京",
        ...     query_time=datetime.now()
        ... )
        >>> result = await calculate_with_geocoding(input_data)
        >>> 
        >>> # 铜钱法 - 不需要位置
        >>> input_data = YijingInput(divination_method="coin")
        >>> result = await calculate_with_geocoding(input_data)
    """
    calculator = YijingCalculator()
    
    # 非 time 方法不需要位置解析
    if input_data.divination_method != "time":
        return calculator.calculate(input_data)
    
    # time 方法：尝试解析位置并计算真太阳时
    query_time = input_data.query_time or datetime.now()
    adjusted_time = query_time
    
    if input_data.birth_place:
        try:
            # 创建 LocationResolver
            resolver = LocationResolver(geocoding_service=geocoding_service)
            
            # 解析位置
            location, timezone = await resolver.resolve(
                birth_place=input_data.birth_place,
                birth_location=None,
                timezone=None
            )
            
            longitude = location[0]
            timezone_offset = _get_timezone_offset(timezone)
            
            # 计算真太阳时
            adjusted_time = _calculate_true_solar_time(
                query_time=query_time,
                longitude=longitude,
                timezone_offset_hours=timezone_offset
            )
            
            logger.info(
                f"Time divination: location={input_data.birth_place}, "
                f"longitude={longitude:.2f}, timezone={timezone}, "
                f"original_time={query_time}, true_solar_time={adjusted_time}"
            )
            
        except (GeocodingError, NotFoundError, InvalidInputError) as e:
            # 位置解析失败，降级使用原始时间
            logger.warning(
                f"Geocoding failed for time divination, using system timezone: {e}"
            )
            adjusted_time = query_time
    
    # 创建调整后的输入
    resolved_input = YijingInput(
        divination_method="time",
        query_time=adjusted_time,
        question=input_data.question,
    )
    
    return calculator.calculate(resolved_input)


def calculate_with_geocoding_sync(
    input_data: YijingInput,
    geocoding_service: Optional[GeocodingService] = None,
) -> YijingFactors:
    """
    执行六爻计算，同步版本。
    
    用于非异步上下文。如果需要 Geocoding 解析，内部会使用 asyncio.run()。
    
    Args:
        input_data: 六爻计算输入
        geocoding_service: 可选的 GeocodingService 实例，用于测试注入
        
    Returns:
        YijingFactors: 六爻因子结果
        
    Example:
        >>> input_data = YijingInput(divination_method="coin")
        >>> result = calculate_with_geocoding_sync(input_data)
    """
    import asyncio
    
    calculator = YijingCalculator()
    
    # 非 time 方法不需要位置解析
    if input_data.divination_method != "time":
        return calculator.calculate(input_data)
    
    # time 方法：需要异步解析
    return asyncio.run(calculate_with_geocoding(input_data, geocoding_service))
