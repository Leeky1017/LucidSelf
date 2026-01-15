# backend/calculators/ziwei/lunar_calendar.py
"""
农历转换模块 - 紫微斗数专用.

提供公历到农历的精确转换，支持：
- 1900-2100年范围
- 闰月检测和处理
- 年月日干支计算
- 时辰地支计算

紫微斗数完全基于农历，此模块是核心依赖。
使用 lunarcalendar 库进行农历转换，确保准确性。
"""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import Optional, Tuple
from zoneinfo import ZoneInfo

from lunarcalendar import Converter, Solar

from backend.calculators.ziwei.models import (
    LunarDate,
    HEAVENLY_STEMS,
    EARTHLY_BRANCHES,
)


# =============================================================================
# 公历转农历
# =============================================================================

def solar_to_lunar(dt: datetime) -> LunarDate:
    """
    公历转农历.
    
    Args:
        dt: 公历日期时间
        
    Returns:
        LunarDate: 农历日期信息
        
    Raises:
        ValueError: 如果日期超出支持范围
    """
    # 使用 lunarcalendar 库进行转换
    solar = Solar(dt.year, dt.month, dt.day)
    lunar = Converter.Solar2Lunar(solar)
    
    lunar_year = lunar.year
    lunar_month = lunar.month
    lunar_day = lunar.day
    is_leap_month = lunar.isleap
    
    # 计算干支
    year_stem, year_branch = _get_year_ganzhi(lunar_year)
    month_stem, month_branch = _get_month_ganzhi(lunar_year, lunar_month)
    day_stem, day_branch = _get_day_ganzhi(dt)
    hour_branch = _get_hour_branch(dt.hour)
    
    return LunarDate(
        year=lunar_year,
        month=lunar_month,
        day=lunar_day,
        is_leap_month=is_leap_month,
        year_stem=year_stem,
        year_branch=year_branch,
        month_stem=month_stem,
        month_branch=month_branch,
        day_stem=day_stem,
        day_branch=day_branch,
        hour_branch=hour_branch,
    )


# =============================================================================
# 干支计算
# =============================================================================

# 1900年是庚子年
BASE_YEAR_STEM_INDEX = 6   # 庚
BASE_YEAR_BRANCH_INDEX = 0  # 子


def _get_year_ganzhi(lunar_year: int) -> Tuple[str, str]:
    """获取农历年的干支."""
    # 1900年是庚子年
    offset = lunar_year - 1900
    stem_idx = (BASE_YEAR_STEM_INDEX + offset) % 10
    branch_idx = (BASE_YEAR_BRANCH_INDEX + offset) % 12
    return HEAVENLY_STEMS[stem_idx], EARTHLY_BRANCHES[branch_idx]


def _get_month_ganzhi(lunar_year: int, lunar_month: int) -> Tuple[str, str]:
    """
    获取农历月的干支.
    
    月支固定：正月寅、二月卯...
    月干由年干推算（五虎遁月）。
    """
    # 月支：正月=寅(2), 二月=卯(3), ...
    branch_idx = (lunar_month + 1) % 12
    branch = EARTHLY_BRANCHES[branch_idx]
    
    # 月干：五虎遁月
    year_stem, _ = _get_year_ganzhi(lunar_year)
    year_stem_idx = HEAVENLY_STEMS.index(year_stem)
    
    # 甲己年丙寅月起，乙庚年戊寅月起...
    base_stem_idx = ((year_stem_idx % 5) * 2 + 2) % 10
    stem_idx = (base_stem_idx + lunar_month - 1) % 10
    stem = HEAVENLY_STEMS[stem_idx]
    
    return stem, branch


def _get_day_ganzhi(dt: datetime) -> Tuple[str, str]:
    """
    获取日干支.
    
    使用儒略日计算。
    """
    year = dt.year
    month = dt.month
    day = dt.day
    
    # 子时(23:00-01:00)跨日处理
    if dt.hour >= 23:
        next_day = dt + timedelta(days=1)
        year = next_day.year
        month = next_day.month
        day = next_day.day
    
    # 计算儒略日
    if month <= 2:
        year -= 1
        month += 12
    
    a = year // 100
    b = 2 - a + a // 4
    jd = int(365.25 * (year + 4716)) + int(30.6001 * (month + 1)) + day + b - 1524
    
    # 1900年1月31日是甲子日
    base_jd = 2415021
    diff = jd - base_jd
    
    stem_idx = diff % 10
    branch_idx = diff % 12
    
    return HEAVENLY_STEMS[stem_idx], EARTHLY_BRANCHES[branch_idx]


def _get_hour_branch(hour: int) -> str:
    """
    获取时辰地支.
    
    子时(23-1), 丑时(1-3), ..., 亥时(21-23)
    """
    if hour == 23:
        branch_idx = 0  # 子
    else:
        branch_idx = (hour + 1) // 2
    return EARTHLY_BRANCHES[branch_idx]


# =============================================================================
# 时区转换
# =============================================================================

def convert_to_beijing_time(
    dt: datetime,
    timezone: Optional[str] = None
) -> datetime:
    """
    将输入时间转换为北京时间.
    
    Args:
        dt: 输入日期时间
        timezone: 时区标识，如 'America/New_York'。
                  为空则假定输入已是北京时间。
                  
    Returns:
        datetime: 北京时间（naive datetime）
    """
    if not timezone:
        return dt
    
    try:
        local_tz = ZoneInfo(timezone)
        beijing_tz = ZoneInfo("Asia/Shanghai")
        
        # 如果是naive datetime，附加本地时区
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=local_tz)
        
        # 转换为北京时间
        return dt.astimezone(beijing_tz).replace(tzinfo=None)
    except Exception as e:
        raise ValueError(f"Invalid timezone '{timezone}': {e}")


# =============================================================================
# 闰月相关
# =============================================================================

def is_valid_lunar_date(year: int, month: int, day: int, is_leap: bool = False) -> bool:
    """
    验证农历日期是否有效.
    
    Args:
        year: 农历年
        month: 农历月
        day: 农历日
        is_leap: 是否闰月
        
    Returns:
        bool: 是否有效
    """
    if year < 1900 or year > 2100:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 30:
        return False
    return True
