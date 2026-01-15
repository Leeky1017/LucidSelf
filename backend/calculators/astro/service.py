# backend/calculators/astro/service.py
"""
AstroCalculator Service Layer - Geocoding 集成入口.

提供 calculate_with_geocoding() 异步方法，自动处理位置解析。

设计理由：
1. Calculator 核心计算保持同步，便于测试和复用
2. Geocoding 是 I/O 操作，在 Service 层异步处理
3. 向后兼容：支持 birth_location 直接输入

使用示例:
    >>> from backend.calculators.astro.service import calculate_with_geocoding
    >>> from backend.calculators.astro.models import AstroInput
    >>> from datetime import datetime
    >>> 
    >>> # 使用城市名
    >>> input_data = AstroInput(
    ...     birth_datetime=datetime(1990, 5, 15, 14, 30),
    ...     birth_place="北京",
    ... )
    >>> result = await calculate_with_geocoding(input_data)
    >>> 
    >>> # 使用坐标（向后兼容）
    >>> input_data = AstroInput(
    ...     birth_datetime=datetime(1990, 5, 15, 14, 30),
    ...     birth_location=(116.4, 39.9),
    ... )
    >>> result = await calculate_with_geocoding(input_data)
"""

from typing import Optional

from backend.calculators.astro.calculator import AstroCalculator
from backend.calculators.astro.models import AstroInput, AstroFactors
from backend.core.geocoding.resolver import LocationResolver
from backend.core.geocoding.service import GeocodingService


async def calculate_with_geocoding(
    input_data: AstroInput,
    geocoding_service: Optional[GeocodingService] = None,
) -> AstroFactors:
    """
    执行西洋占星计算，自动处理位置解析。
    
    此函数是 AstroCalculator 的 Geocoding 集成入口：
    1. 如果提供了 birth_location，直接使用
    2. 如果只提供了 birth_place，通过 GeocodingService 解析
    3. 解析后调用 AstroCalculator.calculate()
    
    Args:
        input_data: 西洋占星计算输入，支持 birth_place 或 birth_location
        geocoding_service: 可选的 GeocodingService 实例，用于测试注入
        
    Returns:
        AstroFactors: 西洋占星因子结果
        
    Raises:
        InvalidInputError: 当 birth_place 和 birth_location 都未提供时
        GeocodingError: 当 birth_place 无法解析时
        ValueError: 当输入参数无效时
        
    Example:
        >>> input_data = AstroInput(
        ...     birth_datetime=datetime(1990, 5, 15, 14, 30),
        ...     birth_place="北京",
        ... )
        >>> result = await calculate_with_geocoding(input_data)
        >>> print(result.ascendant_sign)
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
    resolved_input = AstroInput(
        birth_datetime=input_data.birth_datetime,
        birth_location=location,
        timezone=timezone,
        house_system=input_data.house_system,
    )
    
    # 调用同步 Calculator
    calculator = AstroCalculator()
    return calculator.calculate(resolved_input)


def calculate_with_geocoding_sync(
    input_data: AstroInput,
    geocoding_service: Optional[GeocodingService] = None,
) -> AstroFactors:
    """
    执行西洋占星计算，同步版本。
    
    用于非异步上下文。如果需要 Geocoding 解析，内部会使用 asyncio.run()。
    
    Args:
        input_data: 西洋占星计算输入，支持 birth_place 或 birth_location
        geocoding_service: 可选的 GeocodingService 实例，用于测试注入
        
    Returns:
        AstroFactors: 西洋占星因子结果
        
    Example:
        >>> input_data = AstroInput(
        ...     birth_datetime=datetime(1990, 5, 15, 14, 30),
        ...     birth_location=(116.4, 39.9),
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
    resolved_input = AstroInput(
        birth_datetime=input_data.birth_datetime,
        birth_location=location,
        timezone=timezone,
        house_system=input_data.house_system,
    )
    
    # 调用同步 Calculator
    calculator = AstroCalculator()
    return calculator.calculate(resolved_input)
