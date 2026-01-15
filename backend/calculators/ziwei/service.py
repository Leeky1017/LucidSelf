# backend/calculators/ziwei/service.py
"""
ZiweiCalculator Service Layer - Geocoding 集成入口.

提供 calculate_with_geocoding() 异步方法，自动处理位置解析。

设计理由：
1. Calculator 核心计算保持同步，便于测试和复用
2. Geocoding 是 I/O 操作，在 Service 层异步处理
3. 向后兼容：支持 birth_location 直接输入

使用示例:
    >>> from backend.calculators.ziwei.service import calculate_with_geocoding
    >>> from backend.calculators.ziwei.models import ZiweiInput
    >>> from datetime import datetime
    >>> 
    >>> # 使用城市名
    >>> input_data = ZiweiInput(
    ...     birth_datetime=datetime(1990, 5, 15, 14, 30),
    ...     birth_place="北京",
    ...     gender="male"
    ... )
    >>> result = await calculate_with_geocoding(input_data)
    >>> 
    >>> # 使用坐标（向后兼容）
    >>> input_data = ZiweiInput(
    ...     birth_datetime=datetime(1990, 5, 15, 14, 30),
    ...     birth_location=(116.4, 39.9),
    ...     gender="male"
    ... )
    >>> result = await calculate_with_geocoding(input_data)
"""

from typing import Optional

from backend.calculators.ziwei.calculator import ZiweiCalculator
from backend.calculators.ziwei.models import ZiweiInput, ZiweiFactors
from backend.core.geocoding.resolver import LocationResolver
from backend.core.geocoding.service import GeocodingService


async def calculate_with_geocoding(
    input_data: ZiweiInput,
    geocoding_service: Optional[GeocodingService] = None,
    target_year: Optional[int] = None,
) -> ZiweiFactors:
    """
    执行紫微斗数计算，自动处理位置解析。
    
    此函数是 ZiweiCalculator 的 Geocoding 集成入口：
    1. 如果提供了 birth_location，直接使用
    2. 如果只提供了 birth_place，通过 GeocodingService 解析
    3. 解析后调用 ZiweiCalculator.calculate()
    
    Args:
        input_data: 紫微斗数计算输入，支持 birth_place 或 birth_location
        geocoding_service: 可选的 GeocodingService 实例，用于测试注入
        target_year: 目标流年（可选，默认为当前年）
        
    Returns:
        ZiweiFactors: 紫微斗数因子结果
        
    Raises:
        InvalidInputError: 当 birth_place 和 birth_location 都未提供时
        GeocodingError: 当 birth_place 无法解析时
        ValueError: 当输入参数无效时
        
    Example:
        >>> input_data = ZiweiInput(
        ...     birth_datetime=datetime(1990, 5, 15, 14, 30),
        ...     birth_place="北京",
        ...     gender="male"
        ... )
        >>> result = await calculate_with_geocoding(input_data)
        >>> print(result.five_element_type)
    """
    # 创建 LocationResolver
    resolver = LocationResolver(geocoding_service=geocoding_service)
    
    # 解析位置
    location, timezone = await resolver.resolve(
        birth_place=input_data.birth_place,
        birth_location=input_data.birth_location,
        timezone=input_data.timezone
    )
    
    # 创建内部输入（使用解析后的坐标）
    resolved_input = ZiweiInput(
        birth_datetime=input_data.birth_datetime,
        birth_location=location,
        gender=input_data.gender,
        timezone=timezone,
        calendar_type=input_data.calendar_type,
    )
    
    # 调用同步 Calculator
    calculator = ZiweiCalculator()
    return calculator.calculate(resolved_input, target_year=target_year)


def calculate_with_geocoding_sync(
    input_data: ZiweiInput,
    geocoding_service: Optional[GeocodingService] = None,
    target_year: Optional[int] = None,
) -> ZiweiFactors:
    """
    执行紫微斗数计算，同步版本。
    
    用于非异步上下文。如果需要 Geocoding 解析，内部会使用 asyncio.run()。
    
    Args:
        input_data: 紫微斗数计算输入，支持 birth_place 或 birth_location
        geocoding_service: 可选的 GeocodingService 实例，用于测试注入
        target_year: 目标流年（可选，默认为当前年）
        
    Returns:
        ZiweiFactors: 紫微斗数因子结果
        
    Example:
        >>> input_data = ZiweiInput(
        ...     birth_datetime=datetime(1990, 5, 15, 14, 30),
        ...     birth_location=(116.4, 39.9),
        ...     gender="male"
        ... )
        >>> result = calculate_with_geocoding_sync(input_data)
    """
    # 创建 LocationResolver
    resolver = LocationResolver(geocoding_service=geocoding_service)
    
    # 解析位置（同步版本）
    location, timezone = resolver.resolve_sync(
        birth_place=input_data.birth_place,
        birth_location=input_data.birth_location,
        timezone=input_data.timezone
    )
    
    # 创建内部输入（使用解析后的坐标）
    resolved_input = ZiweiInput(
        birth_datetime=input_data.birth_datetime,
        birth_location=location,
        gender=input_data.gender,
        timezone=timezone,
        calendar_type=input_data.calendar_type,
    )
    
    # 调用同步 Calculator
    calculator = ZiweiCalculator()
    return calculator.calculate(resolved_input, target_year=target_year)
