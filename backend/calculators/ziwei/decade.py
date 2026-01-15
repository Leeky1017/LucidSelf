# backend/calculators/ziwei/decade.py
"""
大限计算模块.

实现紫微斗数大限的计算：
- 起运岁数计算（根据五行局和性别）
- 大限列表生成（覆盖120岁）
- 当前大限判定
- 大限四化计算

准确率目标: 100%
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional, Tuple
from datetime import datetime

from backend.calculators.ziwei.models import (
    Decade,
    Palace,
    SiHua,
    HEAVENLY_STEMS,
    EARTHLY_BRANCHES,
)
from backend.calculators.ziwei.sihua import calculate_decade_sihua


# =============================================================================
# 大限方向判定
# =============================================================================

def get_decade_direction(
    year_stem: str,
    gender: Literal["male", "female"]
) -> Literal["forward", "backward"]:
    """
    判定大限顺逆.
    
    规则：
    - 阳年男命、阴年女命：顺行
    - 阴年男命、阳年女命：逆行
    
    阳干：甲丙戊庚壬
    阴干：乙丁己辛癸
    
    Args:
        year_stem: 年干
        gender: 性别
        
    Returns:
        Literal["forward", "backward"]: 大限方向
    """
    stem_idx = HEAVENLY_STEMS.index(year_stem)
    is_yang_stem = (stem_idx % 2 == 0)  # 偶数索引为阳干
    is_male = (gender == "male")
    
    # 阳年男命或阴年女命：顺行
    if is_yang_stem == is_male:
        return "forward"
    else:
        return "backward"


# =============================================================================
# 起运岁数计算
# =============================================================================

def calculate_start_decade_age(five_element_num: int) -> int:
    """
    计算起运岁数（虚岁）.
    
    紫微斗数起运规则：
    - 水二局 → 2岁起运
    - 木三局 → 3岁起运
    - 金四局 → 4岁起运
    - 土五局 → 5岁起运
    - 火六局 → 6岁起运
    
    注意：紫微斗数起运只认岁级，不做月级修正。
    这与八字大运（子平法）的精确到月不同。
    
    Args:
        five_element_num: 五行局数字 (2,3,4,5,6)
        
    Returns:
        int: 起运岁数（虚岁）
    """
    # 五行局数 = 起运岁数
    return five_element_num


# =============================================================================
# 大限列表生成
# =============================================================================

def generate_decade_list(
    palaces: List[Palace],
    ming_palace_index: int,
    direction: Literal["forward", "backward"],
    start_age: int,
    count: int = 12
) -> List[Decade]:
    """
    生成大限列表.
    
    Args:
        palaces: 十二宫列表
        ming_palace_index: 命宫索引
        direction: 大限方向
        start_age: 起运岁数
        count: 生成大限数量（默认12个，覆盖120岁）
        
    Returns:
        List[Decade]: 大限列表
    """
    decades: List[Decade] = []
    
    for i in range(count):
        # 计算大限宫位索引
        if direction == "forward":
            # 顺行：从命宫开始，按宫位顺序（命→父母→福德→...）
            palace_idx = (ming_palace_index - i) % 12
        else:
            # 逆行：从命宫开始，按宫位逆序（命→兄弟→夫妻→...）
            palace_idx = (ming_palace_index + i) % 12
        
        palace = palaces[palace_idx]
        
        # 计算年龄范围
        age_start = start_age + i * 10
        age_end = age_start + 9
        
        # 计算大限四化
        sihua_list = calculate_decade_sihua(palace.stem)
        
        decade = Decade(
            palace_index=palace_idx,
            palace_name=palace.name,
            stem=palace.stem,
            branch=palace.branch,
            start_age=age_start,
            end_age=age_end,
            sihua_list=sihua_list,
        )
        decades.append(decade)
    
    return decades


def get_current_decade(
    decades: List[Decade],
    current_age: int
) -> Optional[Decade]:
    """
    获取当前大限.
    
    Args:
        decades: 大限列表
        current_age: 当前年龄
        
    Returns:
        Optional[Decade]: 当前大限，如果年龄超出范围返回None
    """
    for decade in decades:
        if decade.start_age <= current_age <= decade.end_age:
            return decade
    return None


def calculate_age(birth_datetime: datetime, reference_date: Optional[datetime] = None) -> int:
    """
    计算年龄.
    
    Args:
        birth_datetime: 出生日期时间
        reference_date: 参考日期（默认为当前日期）
        
    Returns:
        int: 年龄
    """
    if reference_date is None:
        reference_date = datetime.now()
    
    age = reference_date.year - birth_datetime.year
    
    # 检查是否已过生日
    birth_month_day = (birth_datetime.month, birth_datetime.day)
    ref_month_day = (reference_date.month, reference_date.day)
    
    if ref_month_day < birth_month_day:
        age -= 1
    
    return max(0, age)
