# backend/calculators/ziwei/palace_system.py
"""
十二宫安置系统.

实现紫微斗数十二宫的安置算法：
- 命宫定位（根据农历月+时辰）
- 十二宫顺序排列
- 身宫定位
- 宫位天干地支分配

准确率目标: 100%
"""

from __future__ import annotations

from typing import List, Tuple

from backend.calculators.ziwei.models import (
    Palace,
    LunarDate,
    PALACE_NAMES,
    EARTHLY_BRANCHES,
    HEAVENLY_STEMS,
)


# =============================================================================
# 十二宫安置
# =============================================================================

def calculate_ming_palace_index(lunar_month: int, hour_branch: str) -> int:
    """
    计算命宫所在地支索引.
    
    命宫定位公式：
    - 从寅宫起正月，顺数至生月
    - 再从生月逆数至生时
    
    简化公式：命宫地支索引 = (14 - 月 - 时辰索引) % 12
    其中寅=2，时辰索引从子=0开始
    
    Args:
        lunar_month: 农历月份 (1-12)
        hour_branch: 时辰地支
        
    Returns:
        int: 命宫地支索引 (0-11, 0=子)
    """
    hour_idx = EARTHLY_BRANCHES.index(hour_branch)
    
    # 命宫地支索引 = (寅宫索引 + 月 - 1 - 时辰索引) % 12
    # 寅宫索引 = 2
    # 简化: (2 + month - 1 - hour_idx) % 12 = (1 + month - hour_idx) % 12
    # 为避免负数: (13 + month - hour_idx) % 12
    ming_branch_idx = (14 - lunar_month - hour_idx) % 12
    
    return ming_branch_idx


def calculate_body_palace_index(lunar_month: int, hour_branch: str) -> int:
    """
    计算身宫所在地支索引.
    
    身宫定位公式：
    - 从寅宫起正月，顺数至生月
    - 再从生月顺数至生时
    
    简化公式：身宫地支索引 = (月 + 时辰索引 + 2) % 12
    
    Args:
        lunar_month: 农历月份 (1-12)
        hour_branch: 时辰地支
        
    Returns:
        int: 身宫地支索引 (0-11, 0=子)
    """
    hour_idx = EARTHLY_BRANCHES.index(hour_branch)
    
    # 身宫地支索引 = (寅宫索引 + 月 - 1 + 时辰索引) % 12
    # = (2 + month - 1 + hour_idx) % 12
    # = (1 + month + hour_idx) % 12
    body_branch_idx = (lunar_month + hour_idx + 1) % 12
    
    return body_branch_idx


def get_palace_index_from_ming(ming_index: int, palace_name: str) -> int:
    """
    根据命宫位置获取指定宫位的地支索引.
    
    十二宫从命宫开始逆时针排列：
    命宫→兄弟→夫妻→子女→财帛→疾厄→迁移→交友→官禄→田宅→福德→父母
    
    Args:
        ming_index: 命宫地支索引
        palace_name: 宫位名称
        
    Returns:
        int: 该宫位的地支索引
    """
    palace_offset = PALACE_NAMES.index(palace_name)
    # 逆时针排列，所以是减法
    return (ming_index - palace_offset) % 12


def build_twelve_palaces(
    lunar_date: LunarDate,
    year_stem: str
) -> Tuple[List[Palace], int, int]:
    """
    构建十二宫.
    
    Args:
        lunar_date: 农历日期
        year_stem: 年干（用于计算宫位天干）
        
    Returns:
        Tuple[List[Palace], int, int]: (十二宫列表, 命宫索引, 身宫索引)
        宫列表按命宫→父母宫顺序排列
    """
    # 1. 计算命宫和身宫位置
    ming_branch_idx = calculate_ming_palace_index(
        lunar_date.month, 
        lunar_date.hour_branch
    )
    body_branch_idx = calculate_body_palace_index(
        lunar_date.month,
        lunar_date.hour_branch
    )
    
    # 2. 计算宫位天干起始（五虎遁）
    palace_stem_base = _get_palace_stem_base(year_stem)
    
    # 3. 构建十二宫
    palaces: List[Palace] = []
    body_palace_index = -1
    
    for i, palace_name in enumerate(PALACE_NAMES):
        # 宫位地支索引（逆时针排列）
        branch_idx = (ming_branch_idx - i) % 12
        branch = EARTHLY_BRANCHES[branch_idx]
        
        # 宫位天干
        stem = _get_palace_stem(palace_stem_base, branch_idx)
        
        palace = Palace(
            name=palace_name,
            index=i,
            branch=branch,
            stem=stem,
        )
        palaces.append(palace)
        
        # 检查是否为身宫
        if branch_idx == body_branch_idx:
            body_palace_index = i
    
    return palaces, 0, body_palace_index  # 命宫索引始终为0


def _get_palace_stem_base(year_stem: str) -> int:
    """
    获取宫位天干起始索引（五虎遁）.
    
    甲己年：丙寅起
    乙庚年：戊寅起
    丙辛年：庚寅起
    丁壬年：壬寅起
    戊癸年：甲寅起
    
    Args:
        year_stem: 年干
        
    Returns:
        int: 寅宫天干索引
    """
    stem_idx = HEAVENLY_STEMS.index(year_stem)
    # 甲己→丙(2), 乙庚→戊(4), 丙辛→庚(6), 丁壬→壬(8), 戊癸→甲(0)
    base_map = [2, 4, 6, 8, 0]  # 对应甲乙丙丁戊
    return base_map[stem_idx % 5]


def _get_palace_stem(stem_base: int, branch_idx: int) -> str:
    """
    获取指定地支宫位的天干.
    
    从寅宫开始，天干顺序排列。
    
    Args:
        stem_base: 寅宫天干索引
        branch_idx: 宫位地支索引
        
    Returns:
        str: 宫位天干
    """
    # 寅宫索引是2，计算相对偏移
    offset = (branch_idx - 2) % 12
    stem_idx = (stem_base + offset) % 10
    return HEAVENLY_STEMS[stem_idx]


# =============================================================================
# 宫位五行
# =============================================================================

PALACE_ELEMENT = {
    "子": "water", "丑": "earth", "寅": "wood", "卯": "wood",
    "辰": "earth", "巳": "fire", "午": "fire", "未": "earth",
    "申": "metal", "酉": "metal", "戌": "earth", "亥": "water",
}


def get_palace_element(branch: str) -> str:
    """获取宫位五行属性."""
    return PALACE_ELEMENT.get(branch, "unknown")


# =============================================================================
# 身宫判断
# =============================================================================

def get_body_palace_name(body_palace_index: int) -> str:
    """获取身宫名称."""
    return PALACE_NAMES[body_palace_index]


def is_body_palace_with_ming(body_palace_index: int) -> bool:
    """判断身宫是否与命宫同宫."""
    return body_palace_index == 0
