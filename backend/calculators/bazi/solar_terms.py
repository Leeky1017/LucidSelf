# backend/calculators/bazi/solar_terms.py
"""
节气计算模块.

支持的节气（二十四节气中用于八字月柱判断的十二节）：
立春、惊蛰、清明、立夏、芒种、小暑、立秋、白露、寒露、立冬、大雪、小寒

日期范围: 1900-2100 年

节气数据来源：预计算的天文数据（data/solar_terms/solar_terms_1900_2100.json）
精度：< 1分钟（使用预计算数据时）
"""

from datetime import datetime, timedelta
from typing import Literal, Optional, Tuple, Dict
from pathlib import Path
from zoneinfo import ZoneInfo
import json
import math


def _normalize_datetime_for_compare(dt: datetime) -> datetime:
    """
    将datetime标准化为北京时间naive datetime用于比较.
    
    节气时间都是北京时间的naive datetime，
    为了正确比较，需要将aware datetime转换为北京时间的naive datetime。
    
    Args:
        dt: 可能是aware或naive的datetime
        
    Returns:
        北京时间的naive datetime
    """
    if dt.tzinfo is not None:
        # 转换到北京时间，然后移除时区信息
        dt_beijing = dt.astimezone(ZoneInfo('Asia/Shanghai'))
        return dt_beijing.replace(tzinfo=None)
    return dt


# =============================================================================
# 预计算节气数据加载
# =============================================================================

# 缓存预计算的节气数据
_PRECOMPUTED_SOLAR_TERMS: Optional[Dict[str, Dict[str, datetime]]] = None

# JSON文件中的拼音名称到中文名称的映射
# 注意：JSON文件中的名称有偏移，需要修正
_PINYIN_TO_CHINESE_CORRECTED = {
    "Dahan": "小寒",      # JSON "Dahan" 实际是小寒 (Jan 6)
    "Lichun": "大寒",     # JSON "Lichun" 实际是大寒 (Jan 20)
    "Yushui": "立春",     # JSON "Yushui" 实际是立春 (Feb 4)
    "Jingzhe": "雨水",    # JSON "Jingzhe" 实际是雨水 (Feb 19)
    "Chunfen": "惊蛰",    # JSON "Chunfen" 实际是惊蛰 (Mar 5)
    "Qingming": "春分",   # JSON "Qingming" 实际是春分 (Mar 20)
    "Guyu": "清明",       # JSON "Guyu" 实际是清明 (Apr 4)
    "Lixia": "谷雨",      # JSON "Lixia" 实际是谷雨 (Apr 19)
    "Xiaoman": "立夏",    # JSON "Xiaoman" 实际是立夏 (May 5)
    "Mangzhong": "小满",  # JSON "Mangzhong" 实际是小满 (May 20)
    "Xiazhi": "芒种",     # JSON "Xiazhi" 实际是芒种 (Jun 5)
    "Xiaoshu": "夏至",    # JSON "Xiaoshu" 实际是夏至 (Jun 21)
    "Dashu": "小暑",      # JSON "Dashu" 实际是小暑 (Jul 6)
    "Liqiu": "大暑",      # JSON "Liqiu" 实际是大暑 (Jul 22)
    "Chushu": "立秋",     # JSON "Chushu" 实际是立秋 (Aug 7)
    "Bailu": "处暑",      # JSON "Bailu" 实际是处暑 (Aug 22)
    "Qiufen": "白露",     # JSON "Qiufen" 实际是白露 (Sep 7)
    "Hanlu": "秋分",      # JSON "Hanlu" 实际是秋分 (Sep 22)
    "Shuangjiang": "寒露", # JSON "Shuangjiang" 实际是寒露 (Oct 8)
    "Lidong": "霜降",     # JSON "Lidong" 实际是霜降 (Oct 23)
    "Xiaoxue": "立冬",    # JSON "Xiaoxue" 实际是立冬 (Nov 7)
    "Daxue": "小雪",      # JSON "Daxue" 实际是小雪 (Nov 22)
    "Dongzhi": "大雪",    # JSON "Dongzhi" 实际是大雪 (Dec 6)
    "Xiaohan": "冬至",    # JSON "Xiaohan" 实际是冬至 (Dec 21)
}

# 中文名称到JSON拼音名称的反向映射
_CHINESE_TO_PINYIN = {v: k for k, v in _PINYIN_TO_CHINESE_CORRECTED.items()}


def _load_precomputed_solar_terms() -> Dict[str, Dict[str, datetime]]:
    """加载预计算的节气数据."""
    global _PRECOMPUTED_SOLAR_TERMS
    
    if _PRECOMPUTED_SOLAR_TERMS is not None:
        return _PRECOMPUTED_SOLAR_TERMS
    
    json_path = Path(__file__).parent.parent.parent.parent / "data" / "solar_terms" / "solar_terms_1900_2100.json"
    
    if not json_path.exists():
        # 如果文件不存在，返回空字典，将回退到算法计算
        _PRECOMPUTED_SOLAR_TERMS = {}
        return _PRECOMPUTED_SOLAR_TERMS
    
    with open(json_path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)
    
    # 解析并转换为中文名称
    result: Dict[str, Dict[str, datetime]] = {}
    for year_str, terms in raw_data.items():
        year_data: Dict[str, datetime] = {}
        for pinyin_name, dt_str in terms.items():
            # 解析ISO格式日期时间
            dt = datetime.fromisoformat(dt_str.replace("+08:00", ""))
            # 转换为中文名称
            chinese_name = _PINYIN_TO_CHINESE_CORRECTED.get(pinyin_name)
            if chinese_name:
                year_data[chinese_name] = dt
        result[year_str] = year_data
    
    _PRECOMPUTED_SOLAR_TERMS = result
    return _PRECOMPUTED_SOLAR_TERMS


def _get_precomputed_solar_term(year: int, term_name: str) -> Optional[datetime]:
    """从预计算数据获取节气时间."""
    data = _load_precomputed_solar_terms()
    year_str = str(year)
    
    if year_str not in data:
        return None
    
    return data[year_str].get(term_name)


# =============================================================================
# 节气常量
# =============================================================================

# 十二节（用于月柱判断）
SOLAR_TERMS_FOR_MONTH = [
    "小寒", "立春", "惊蛰", "清明", "立夏", "芒种",
    "小暑", "立秋", "白露", "寒露", "立冬", "大雪",
]

# 节气对应的月份（农历月）
SOLAR_TERM_TO_MONTH = {
    "立春": 1, "惊蛰": 2, "清明": 3, "立夏": 4, "芒种": 5, "小暑": 6,
    "立秋": 7, "白露": 8, "寒露": 9, "立冬": 10, "大雪": 11, "小寒": 12,
}

# 节气对应的季节
SOLAR_TERM_TO_SEASON = {
    "立春": "spring", "惊蛰": "spring", "清明": "spring",
    "立夏": "summer", "芒种": "summer", "小暑": "summer",
    "立秋": "autumn", "白露": "autumn", "寒露": "autumn",
    "立冬": "winter", "大雪": "winter", "小寒": "winter",
}

# 月份对应的季节（简化版）
MONTH_TO_SEASON = {
    1: "winter", 2: "spring", 3: "spring", 4: "spring",
    5: "summer", 6: "summer", 7: "summer", 8: "autumn",
    9: "autumn", 10: "autumn", 11: "winter", 12: "winter",
}


# =============================================================================
# 天文算法计算节气
# =============================================================================

def _julian_day(year: int, month: int, day: float) -> float:
    """计算儒略日."""
    if month <= 2:
        year -= 1
        month += 12
    
    a = int(year / 100)
    b = 2 - a + int(a / 4)
    
    return int(365.25 * (year + 4716)) + int(30.6001 * (month + 1)) + day + b - 1524.5


def _solar_longitude(jd: float) -> float:
    """计算太阳黄经（度）."""
    t = (jd - 2451545.0) / 36525.0
    
    # 太阳平黄经
    l0 = 280.46646 + 36000.76983 * t + 0.0003032 * t * t
    
    # 太阳平近点角
    m = 357.52911 + 35999.05029 * t - 0.0001537 * t * t
    m_rad = math.radians(m)
    
    # 太阳方程式
    c = (1.914602 - 0.004817 * t - 0.000014 * t * t) * math.sin(m_rad)
    c += (0.019993 - 0.000101 * t) * math.sin(2 * m_rad)
    c += 0.000289 * math.sin(3 * m_rad)
    
    # 太阳真黄经
    sun_lon = l0 + c
    
    # 归一化到 0-360
    sun_lon = sun_lon % 360
    
    return sun_lon


def _find_solar_term_jd(year: int, term_index: int) -> float:
    """
    计算指定节气的儒略日.
    
    Args:
        year: 年份
        term_index: 节气索引 (0=小寒, 1=大寒, ..., 23=冬至)
        
    Returns:
        float: 儒略日
    """
    # 目标黄经（每个节气间隔15度）
    target_lon = (term_index * 15 + 285) % 360
    
    # 估算日期
    # 小寒大约在1月5日，每个节气间隔约15.2天
    estimated_day = 5 + term_index * 15.2
    
    if estimated_day > 365:
        year += 1
        estimated_day -= 365
    
    # 估算月日
    month = int(estimated_day / 30) + 1
    day = estimated_day - (month - 1) * 30
    
    jd = _julian_day(year, month, day)
    
    # 牛顿迭代法求解
    for _ in range(50):
        lon = _solar_longitude(jd)
        diff = target_lon - lon
        
        # 处理跨 0/360 度的情况
        if diff > 180:
            diff -= 360
        elif diff < -180:
            diff += 360
        
        if abs(diff) < 0.0001:
            break
        
        # 太阳每天移动约1度
        jd += diff / 1.0
    
    return jd


def _jd_to_datetime(jd: float) -> datetime:
    """儒略日转换为日期时间."""
    jd = jd + 0.5
    z = int(jd)
    f = jd - z
    
    if z < 2299161:
        a = z
    else:
        alpha = int((z - 1867216.25) / 36524.25)
        a = z + 1 + alpha - int(alpha / 4)
    
    b = a + 1524
    c = int((b - 122.1) / 365.25)
    d = int(365.25 * c)
    e = int((b - d) / 30.6001)
    
    day = b - d - int(30.6001 * e) + f
    
    if e < 14:
        month = e - 1
    else:
        month = e - 13
    
    if month > 2:
        year = c - 4716
    else:
        year = c - 4715
    
    day_int = int(day)
    day_frac = day - day_int
    
    hours = day_frac * 24
    hour = int(hours)
    minutes = (hours - hour) * 60
    minute = int(minutes)
    seconds = (minutes - minute) * 60
    second = int(seconds)
    
    return datetime(year, month, day_int, hour, minute, second)


def get_solar_term_date(year: int, term_name: str) -> datetime:
    """
    获取指定年份某节气的日期时间.
    
    优先使用预计算的天文数据（精度 < 1分钟），
    如果预计算数据不可用则回退到算法计算。
    
    Args:
        year: 年份
        term_name: 节气名称
        
    Returns:
        datetime: 节气日期时间（北京时间）
        
    Raises:
        ValueError: 如果节气名称无效
    """
    term_names = [
        "小寒", "大寒", "立春", "雨水", "惊蛰", "春分",
        "清明", "谷雨", "立夏", "小满", "芒种", "夏至",
        "小暑", "大暑", "立秋", "处暑", "白露", "秋分",
        "寒露", "霜降", "立冬", "小雪", "大雪", "冬至",
    ]
    
    if term_name not in term_names:
        raise ValueError(f"Invalid solar term name: {term_name}")
    
    # 优先使用预计算数据
    precomputed = _get_precomputed_solar_term(year, term_name)
    if precomputed is not None:
        return precomputed
    
    # 回退到算法计算
    term_index = term_names.index(term_name)
    
    # 小寒属于上一年的节气周期
    if term_name in ["小寒", "大寒"]:
        jd = _find_solar_term_jd(year, term_index)
    else:
        jd = _find_solar_term_jd(year, term_index)
    
    # 转换为北京时间 (UTC+8)
    dt = _jd_to_datetime(jd)
    return dt + timedelta(hours=8)


def get_month_from_solar_term(dt: datetime) -> int:
    """
    根据日期获取八字月份（基于节气）.
    
    Args:
        dt: 日期时间 (可以是aware或naive datetime)
        
    Returns:
        int: 八字月份 (1-12)
    """
    dt_naive = _normalize_datetime_for_compare(dt)
    year = dt_naive.year
    
    # 检查是否在立春之前（属于上一年）
    lichun = get_solar_term_date(year, "立春")
    if dt_naive < lichun:
        year -= 1
    
    # 找到当前所在的月份
    for i, term_name in enumerate(SOLAR_TERMS_FOR_MONTH[1:], 1):
        term_date = get_solar_term_date(year if term_name != "小寒" else year + 1, term_name)
        if dt_naive < term_date:
            # 返回上一个节气对应的月份
            prev_term = SOLAR_TERMS_FOR_MONTH[i - 1] if i > 0 else "小寒"
            return SOLAR_TERM_TO_MONTH.get(prev_term, 1)
    
    return 12


def get_season_from_date(dt: datetime) -> Literal["spring", "summer", "autumn", "winter"]:
    """
    根据日期获取季节（基于节气）.
    
    Args:
        dt: 日期时间 (可以是aware或naive datetime)
        
    Returns:
        str: 季节 (spring/summer/autumn/winter)
    """
    dt_naive = _normalize_datetime_for_compare(dt)
    year = dt_naive.year
    
    # 节气边界
    lichun = get_solar_term_date(year, "立春")
    lixia = get_solar_term_date(year, "立夏")
    liqiu = get_solar_term_date(year, "立秋")
    lidong = get_solar_term_date(year, "立冬")
    
    # 判断上一年的立春
    if dt_naive < lichun:
        return "winter"
    
    if dt_naive < lixia:
        return "spring"
    elif dt_naive < liqiu:
        return "summer"
    elif dt_naive < lidong:
        return "autumn"
    else:
        return "winter"


def is_before_lichun(dt: datetime) -> bool:
    """
    判断日期是否在当年立春之前.
    
    Args:
        dt: 日期时间 (可以是aware或naive datetime)
        
    Returns:
        bool: True 表示在立春之前
    """
    lichun = get_solar_term_date(dt.year, "立春")
    dt_naive = _normalize_datetime_for_compare(dt)
    return dt_naive < lichun
