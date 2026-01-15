# backend/calculators/ziwei/sihua.py
"""
四化飞星计算模块.

实现紫微斗数四化飞星的完整计算：
- 生年四化（根据出生年干）
- 大限四化（根据大限宫位天干）
- 流年四化（根据流年天干）
- 四化叠加查询

准确率目标: 100%
"""

from __future__ import annotations

from typing import Dict, List, Tuple, Optional

from backend.calculators.ziwei.models import (
    SiHua,
    HEAVENLY_STEMS,
    SIHUA_TYPES,
)


# =============================================================================
# 四化对照表
# =============================================================================

# 四化对照表：SIHUA_TABLE[天干] = (化禄星, 化权星, 化科星, 化忌星)
# 采用最广泛认可的版本
SIHUA_TABLE: Dict[str, Tuple[str, str, str, str]] = {
    "甲": ("廉贞", "破军", "武曲", "太阳"),
    "乙": ("天机", "天梁", "紫微", "太阴"),
    "丙": ("天同", "天机", "文昌", "廉贞"),
    "丁": ("太阴", "天同", "天机", "巨门"),
    "戊": ("贪狼", "太阴", "右弼", "天机"),
    "己": ("武曲", "贪狼", "天梁", "文曲"),
    "庚": ("太阳", "武曲", "太阴", "天同"),
    "辛": ("巨门", "太阳", "文曲", "文昌"),
    "壬": ("天梁", "紫微", "左辅", "武曲"),
    "癸": ("破军", "巨门", "太阴", "贪狼"),
}


# =============================================================================
# 四化计算
# =============================================================================

def get_sihua_stars(stem: str) -> Dict[str, str]:
    """
    根据天干获取四化星曜.
    
    Args:
        stem: 天干
        
    Returns:
        Dict[str, str]: {四化类型: 星曜名称}
    """
    if stem not in SIHUA_TABLE:
        raise ValueError(f"Invalid stem: {stem}")
    
    stars = SIHUA_TABLE[stem]
    return {
        "化禄": stars[0],
        "化权": stars[1],
        "化科": stars[2],
        "化忌": stars[3],
    }


def calculate_natal_sihua(year_stem: str) -> List[SiHua]:
    """
    计算生年四化.
    
    Args:
        year_stem: 年干
        
    Returns:
        List[SiHua]: 生年四化列表
    """
    stars = get_sihua_stars(year_stem)
    result = []
    
    for sihua_type, star_name in stars.items():
        sihua = SiHua(
            sihua_type=sihua_type,
            star_name=star_name,
            source="natal",
            source_stem=year_stem,
        )
        result.append(sihua)
    
    return result


def calculate_decade_sihua(decade_stem: str) -> List[SiHua]:
    """
    计算大限四化.
    
    Args:
        decade_stem: 大限天干
        
    Returns:
        List[SiHua]: 大限四化列表
    """
    stars = get_sihua_stars(decade_stem)
    result = []
    
    for sihua_type, star_name in stars.items():
        sihua = SiHua(
            sihua_type=sihua_type,
            star_name=star_name,
            source="decade",
            source_stem=decade_stem,
        )
        result.append(sihua)
    
    return result


def calculate_annual_sihua(annual_stem: str) -> List[SiHua]:
    """
    计算流年四化.
    
    Args:
        annual_stem: 流年天干
        
    Returns:
        List[SiHua]: 流年四化列表
    """
    stars = get_sihua_stars(annual_stem)
    result = []
    
    for sihua_type, star_name in stars.items():
        sihua = SiHua(
            sihua_type=sihua_type,
            star_name=star_name,
            source="annual",
            source_stem=annual_stem,
        )
        result.append(sihua)
    
    return result


# =============================================================================
# 四化叠加查询
# =============================================================================

def get_sihua_for_star(
    star_name: str,
    natal_sihua: List[SiHua],
    decade_sihua: Optional[List[SiHua]] = None,
    annual_sihua: Optional[List[SiHua]] = None
) -> List[SiHua]:
    """
    查询某星曜的所有四化.
    
    Args:
        star_name: 星曜名称
        natal_sihua: 生年四化列表
        decade_sihua: 大限四化列表（可选）
        annual_sihua: 流年四化列表（可选）
        
    Returns:
        List[SiHua]: 该星曜的所有四化
    """
    result = []
    
    # 生年四化
    for sihua in natal_sihua:
        if sihua.star_name == star_name:
            result.append(sihua)
    
    # 大限四化
    if decade_sihua:
        for sihua in decade_sihua:
            if sihua.star_name == star_name:
                result.append(sihua)
    
    # 流年四化
    if annual_sihua:
        for sihua in annual_sihua:
            if sihua.star_name == star_name:
                result.append(sihua)
    
    return result


def get_sihua_for_palace(
    palace_stars: List[str],
    natal_sihua: List[SiHua],
    decade_sihua: Optional[List[SiHua]] = None,
    annual_sihua: Optional[List[SiHua]] = None
) -> List[SiHua]:
    """
    查询某宫位的所有四化.
    
    Args:
        palace_stars: 宫位内的星曜列表
        natal_sihua: 生年四化列表
        decade_sihua: 大限四化列表（可选）
        annual_sihua: 流年四化列表（可选）
        
    Returns:
        List[SiHua]: 该宫位的所有四化
    """
    result = []
    
    for star_name in palace_stars:
        star_sihua = get_sihua_for_star(
            star_name, natal_sihua, decade_sihua, annual_sihua
        )
        result.extend(star_sihua)
    
    return result


def sihua_to_dict(sihua_list: List[SiHua]) -> Dict[str, str]:
    """
    将四化列表转换为字典格式.
    
    Args:
        sihua_list: 四化列表
        
    Returns:
        Dict[str, str]: {四化类型: 星曜名称}
    """
    return {sihua.sihua_type: sihua.star_name for sihua in sihua_list}


# =============================================================================
# 流年天干计算
# =============================================================================

def get_annual_stem(year: int) -> str:
    """
    获取流年天干.
    
    Args:
        year: 公历年份
        
    Returns:
        str: 流年天干
    """
    # 1984年是甲子年
    stem_idx = (year - 4) % 10
    return HEAVENLY_STEMS[stem_idx]
