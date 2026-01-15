# backend/calculators/bazi/dayun.py
"""
八字大运计算模块（子平法）.

大运起运规则（三天折一年法）：
1. 顺逆方向：阳年男命、阴年女命 → 顺行；阴年男命、阳年女命 → 逆行
2. 起运时间：从出生时刻到上/下一个「节」的时间差
3. 换算规则：
   - 3天 = 1岁
   - 1天 = 4个月
   - 时辰折算（可选，当前版本不处理）
4. 只用12节（立春、惊蛰、清明...），不用12气
5. 精度：年+月级（不做日级）

公式：
  delta_hours = |boundary_dt - birth_dt|
  days = floor(delta_hours / 24)  # 舍弃不足1天的部分
  years = days // 3
  months = (days % 3) * 4  # 0/4/8 三种
"""

from datetime import datetime, timedelta
from typing import List, Literal, Tuple

from backend.calculators.bazi.models import (
    HEAVENLY_STEMS,
    EARTHLY_BRANCHES,
    STEM_YINYANG,
    Pillar,
    Dayun,
)
from backend.calculators.bazi.solar_terms import (
    get_solar_term_date,
    SOLAR_TERMS_FOR_MONTH,
)


# =============================================================================
# 12节列表（只用节，不用气）
# =============================================================================

# 12节：立春、惊蛰、清明、立夏、芒种、小暑、立秋、白露、寒露、立冬、大雪、小寒
JIE_ONLY = [
    "小寒", "立春", "惊蛰", "清明", "立夏", "芒种",
    "小暑", "立秋", "白露", "寒露", "立冬", "大雪",
]


def get_year_yinyang(year_stem: str) -> Literal["yang", "yin"]:
    """
    获取年份的阴阳属性.
    
    阳干：甲丙戊庚壬（索引0,2,4,6,8）
    阴干：乙丁己辛癸（索引1,3,5,7,9）
    
    Args:
        year_stem: 年柱天干
        
    Returns:
        str: "yang" 或 "yin"
    """
    return STEM_YINYANG[year_stem]


def get_dayun_direction(
    year_stem: str,
    gender: Literal["male", "female"]
) -> Literal["forward", "backward"]:
    """
    判断大运顺逆方向.
    
    规则：
    - 阳年男命：顺行（数到下一个节）
    - 阴年女命：顺行（数到下一个节）
    - 阴年男命：逆行（数到上一个节）
    - 阳年女命：逆行（数到上一个节）
    
    Args:
        year_stem: 年柱天干
        gender: 性别
        
    Returns:
        str: "forward" (顺行) 或 "backward" (逆行)
    """
    year_yinyang = get_year_yinyang(year_stem)
    
    if year_yinyang == "yang":
        return "forward" if gender == "male" else "backward"
    else:
        return "backward" if gender == "male" else "forward"


def calculate_start_dayun_age(
    birth_datetime: datetime,
    direction: Literal["forward", "backward"]
) -> Tuple[int, int]:
    """
    计算起运岁数（子平法，精确到年+月）.
    
    算法（三天折一年法）：
    1. 找到出生时刻前后的「节」（只用12节，不用气）
    2. 顺行：计算到下一个节的时间差
       逆行：计算到上一个节的时间差
    3. 换算：
       - delta_hours = |boundary_dt - birth_dt|
       - days = floor(delta_hours / 24)  # 舍弃不足1天
       - years = days // 3
       - months = (days % 3) * 4  # 余0天=0月，余1天=4月，余2天=8月
    
    Args:
        birth_datetime: 出生日期时间（精确到分钟）
        direction: 大运方向
        
    Returns:
        Tuple[int, int]: (起运岁数, 起运月数)
        例如：(2, 8) 表示 2岁8个月起运
    """
    from backend.calculators.bazi.solar_terms import _normalize_datetime_for_compare
    birth_naive = _normalize_datetime_for_compare(birth_datetime)
    year = birth_naive.year
    
    # 收集前后年份的所有「节」
    jie_list = []
    for jie_name in JIE_ONLY:
        for y in [year - 1, year, year + 1]:
            try:
                jie_dt = get_solar_term_date(y, jie_name)
                jie_list.append((jie_name, jie_dt))
            except:
                continue
    
    # 按日期排序
    jie_list.sort(key=lambda x: x[1])
    
    # 找到出生日期前后的节
    prev_jie = None
    next_jie = None
    
    for i, (name, dt) in enumerate(jie_list):
        if dt > birth_naive:
            next_jie = (name, dt)
            if i > 0:
                prev_jie = jie_list[i - 1]
            break
    
    # 边界处理
    if next_jie is None:
        next_jie = jie_list[-1]
    if prev_jie is None:
        prev_jie = jie_list[0]
    
    # 根据大运方向确定目标节
    if direction == "forward":
        boundary_dt = next_jie[1]
    else:
        boundary_dt = prev_jie[1]
    
    # 计算时间差（小时）
    delta = abs((boundary_dt - birth_naive).total_seconds())
    delta_hours = delta / 3600
    
    # 换算为天数（舍弃不足1天的部分，不做日级精度）
    days = int(delta_hours // 24)
    
    # 三天折一年法
    years = days // 3
    remaining_days = days % 3
    months = remaining_days * 4  # 0天=0月，1天=4月，2天=8月
    
    return (years, months)


def generate_dayun_list(
    month_pillar: Pillar,
    direction: Literal["forward", "backward"],
    start_age: int,
    count: int = 12
) -> List[Dayun]:
    """
    生成大运列表.
    
    Args:
        month_pillar: 月柱
        direction: 大运方向
        start_age: 起运岁数
        count: 生成的大运数量（默认12步，覆盖120岁）
        
    Returns:
        List[Dayun]: 大运列表
    """
    dayun_list = []
    
    # 获取月柱的干支索引
    stem_idx = HEAVENLY_STEMS.index(month_pillar.stem)
    branch_idx = EARTHLY_BRANCHES.index(month_pillar.branch)
    
    # 步进方向
    step = 1 if direction == "forward" else -1
    
    current_age = start_age
    
    for i in range(count):
        # 计算新的干支索引
        new_stem_idx = (stem_idx + step * (i + 1)) % 10
        new_branch_idx = (branch_idx + step * (i + 1)) % 12
        
        stem = HEAVENLY_STEMS[new_stem_idx]
        branch = EARTHLY_BRANCHES[new_branch_idx]
        
        dayun = Dayun(
            stem=stem,
            branch=branch,
            start_age=current_age,
            end_age=current_age + 9,
        )
        dayun_list.append(dayun)
        
        current_age += 10
    
    return dayun_list


def get_current_dayun(
    dayun_list: List[Dayun],
    current_age: int
) -> Dayun | None:
    """
    获取当前所在的大运.
    
    Args:
        dayun_list: 大运列表
        current_age: 当前年龄
        
    Returns:
        Dayun: 当前大运，如果年龄超出范围则返回 None
    """
    for dayun in dayun_list:
        if dayun.start_age <= current_age <= dayun.end_age:
            return dayun
    return None
