# backend/calculators/ziwei/star_placement.py
"""
星曜安置系统.

实现紫微斗数星曜的安置算法：
- 紫微星系（6星）安置
- 天府星系（8星）安置
- 辅星安置
- 煞星安置
- 星曜亮度判定

准确率目标: ≥ 99%
"""

from __future__ import annotations

from typing import Dict, List, Tuple, Optional

from backend.calculators.ziwei.models import (
    Star,
    StarBrightness,
    LunarDate,
    EARTHLY_BRANCHES,
    MAIN_STARS,
    ZIWEI_STAR_GROUP,
    TIANFU_STAR_GROUP,
    AUXILIARY_STARS,
    SHA_STARS,
)


# =============================================================================
# 五行局计算
# =============================================================================

# 五行局对照表：根据命宫地支和年干确定
# 格式：FIVE_ELEMENT_TABLE[命宫地支索引][年干索引 % 5]
FIVE_ELEMENT_TABLE = {
    # 子丑寅卯辰巳午未申酉戌亥
    0: [2, 6, 4, 3, 5],   # 子
    1: [2, 6, 4, 3, 5],   # 丑
    2: [4, 3, 5, 2, 6],   # 寅
    3: [4, 3, 5, 2, 6],   # 卯
    4: [5, 2, 6, 4, 3],   # 辰
    5: [5, 2, 6, 4, 3],   # 巳
    6: [6, 4, 3, 5, 2],   # 午
    7: [6, 4, 3, 5, 2],   # 未
    8: [3, 5, 2, 6, 4],   # 申
    9: [3, 5, 2, 6, 4],   # 酉
    10: [2, 6, 4, 3, 5],  # 戌
    11: [2, 6, 4, 3, 5],  # 亥
}

FIVE_ELEMENT_NAMES = {
    2: "水二局",
    3: "木三局",
    4: "金四局",
    5: "土五局",
    6: "火六局",
}


def calculate_five_element(
    ming_branch_idx: int,
    year_stem: str
) -> Tuple[str, int]:
    """
    计算五行局.
    
    Args:
        ming_branch_idx: 命宫地支索引
        year_stem: 年干
        
    Returns:
        Tuple[str, int]: (五行局名称, 五行局数字)
    """
    from backend.calculators.ziwei.models import HEAVENLY_STEMS
    
    stem_idx = HEAVENLY_STEMS.index(year_stem)
    element_num = FIVE_ELEMENT_TABLE[ming_branch_idx][stem_idx % 5]
    element_name = FIVE_ELEMENT_NAMES[element_num]
    
    return element_name, element_num


# =============================================================================
# 紫微星定位
# =============================================================================

# 紫微星安置表：根据农历日和五行局数确定紫微星所在地支
# ZIWEI_TABLE[五行局数][农历日] = 紫微星地支索引
ZIWEI_TABLE = {
    2: {  # 水二局
        1: 2, 2: 3, 3: 1, 4: 2, 5: 3, 6: 4, 7: 2, 8: 3, 9: 4, 10: 5,
        11: 3, 12: 4, 13: 5, 14: 6, 15: 4, 16: 5, 17: 6, 18: 7, 19: 5, 20: 6,
        21: 7, 22: 8, 23: 6, 24: 7, 25: 8, 26: 9, 27: 7, 28: 8, 29: 9, 30: 10,
    },
    3: {  # 木三局
        1: 2, 2: 2, 3: 3, 4: 1, 5: 2, 6: 2, 7: 3, 8: 4, 9: 2, 10: 2,
        11: 3, 12: 4, 13: 5, 14: 3, 15: 3, 16: 4, 17: 5, 18: 6, 19: 4, 20: 4,
        21: 5, 22: 6, 23: 7, 24: 5, 25: 5, 26: 6, 27: 7, 28: 8, 29: 6, 30: 6,
    },
    4: {  # 金四局
        1: 2, 2: 2, 3: 2, 4: 3, 5: 1, 6: 2, 7: 2, 8: 2, 9: 3, 10: 4,
        11: 2, 12: 2, 13: 2, 14: 3, 15: 4, 16: 5, 17: 3, 18: 3, 19: 3, 20: 4,
        21: 5, 22: 6, 23: 4, 24: 4, 25: 4, 26: 5, 27: 6, 28: 7, 29: 5, 30: 5,
    },
    5: {  # 土五局
        1: 2, 2: 2, 3: 2, 4: 2, 5: 3, 6: 1, 7: 2, 8: 2, 9: 2, 10: 2,
        11: 3, 12: 4, 13: 2, 14: 2, 15: 2, 16: 2, 17: 3, 18: 4, 19: 5, 20: 3,
        21: 3, 22: 3, 23: 3, 24: 4, 25: 5, 26: 6, 27: 4, 28: 4, 29: 4, 30: 4,
    },
    6: {  # 火六局
        1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 3, 7: 1, 8: 2, 9: 2, 10: 2,
        11: 2, 12: 2, 13: 3, 14: 4, 15: 2, 16: 2, 17: 2, 18: 2, 19: 2, 20: 3,
        21: 4, 22: 5, 23: 3, 24: 3, 25: 3, 26: 3, 27: 3, 28: 4, 29: 5, 30: 6,
    },
}


def calculate_ziwei_position(lunar_day: int, five_element_num: int) -> int:
    """
    计算紫微星所在地支索引.
    
    Args:
        lunar_day: 农历日 (1-30)
        five_element_num: 五行局数字 (2,3,4,5,6)
        
    Returns:
        int: 紫微星地支索引 (0-11)
    """
    if five_element_num not in ZIWEI_TABLE:
        raise ValueError(f"Invalid five element number: {five_element_num}")
    
    day = min(lunar_day, 30)  # 最多30天
    return ZIWEI_TABLE[five_element_num].get(day, 2) % 12


# =============================================================================
# 紫微星系安置
# =============================================================================

# 紫微星系相对位置（相对于紫微星）
# 紫微、天机、太阳、武曲、天同、廉贞
ZIWEI_GROUP_OFFSETS = {
    "紫微": 0,
    "天机": -1,   # 紫微逆一位
    "太阳": -3,   # 紫微逆三位
    "武曲": -4,   # 紫微逆四位
    "天同": -5,   # 紫微逆五位
    "廉贞": -8,   # 紫微逆八位
}


def place_ziwei_group(ziwei_position: int) -> Dict[str, int]:
    """
    安置紫微星系六星.
    
    Args:
        ziwei_position: 紫微星地支索引
        
    Returns:
        Dict[str, int]: {星名: 地支索引}
    """
    result = {}
    for star, offset in ZIWEI_GROUP_OFFSETS.items():
        result[star] = (ziwei_position + offset) % 12
    return result


# =============================================================================
# 天府星系安置
# =============================================================================

# 天府星位置：与紫微星对称
# 天府在紫微的对宫位置，具体公式：天府 = (12 - 紫微 + 4) % 12
def calculate_tianfu_position(ziwei_position: int) -> int:
    """计算天府星位置."""
    return (12 - ziwei_position + 4) % 12


# 天府星系相对位置（相对于天府星）
# 天府、太阴、贪狼、巨门、天相、天梁、七杀、破军
TIANFU_GROUP_OFFSETS = {
    "天府": 0,
    "太阴": 1,    # 天府顺一位
    "贪狼": 2,    # 天府顺二位
    "巨门": 3,    # 天府顺三位
    "天相": 4,    # 天府顺四位
    "天梁": 5,    # 天府顺五位
    "七杀": 6,    # 天府顺六位
    "破军": 10,   # 天府顺十位
}


def place_tianfu_group(tianfu_position: int) -> Dict[str, int]:
    """
    安置天府星系八星.
    
    Args:
        tianfu_position: 天府星地支索引
        
    Returns:
        Dict[str, int]: {星名: 地支索引}
    """
    result = {}
    for star, offset in TIANFU_GROUP_OFFSETS.items():
        result[star] = (tianfu_position + offset) % 12
    return result


# =============================================================================
# 辅星安置
# =============================================================================

def place_auxiliary_stars(
    lunar_month: int,
    hour_branch: str,
    year_stem: str,
    year_branch: str
) -> Dict[str, int]:
    """
    安置辅星.
    
    Args:
        lunar_month: 农历月
        hour_branch: 时辰地支
        year_stem: 年干
        year_branch: 年支
        
    Returns:
        Dict[str, int]: {星名: 地支索引}
    """
    result = {}
    
    # 左辅：从辰宫起正月，顺数至生月
    result["左辅"] = (4 + lunar_month - 1) % 12
    
    # 右弼：从戌宫起正月，逆数至生月
    result["右弼"] = (10 - lunar_month + 1) % 12
    
    # 文昌：从戌宫起子时，逆数至生时
    hour_idx = EARTHLY_BRANCHES.index(hour_branch)
    result["文昌"] = (10 - hour_idx) % 12
    
    # 文曲：从辰宫起子时，顺数至生时
    result["文曲"] = (4 + hour_idx) % 12
    
    # 天魁、天钺：根据年干
    tiankui, tianyue = _get_tiankui_tianyue(year_stem)
    result["天魁"] = tiankui
    result["天钺"] = tianyue
    
    # 禄存：根据年干
    result["禄存"] = _get_lucun_position(year_stem)
    
    # 天马：根据年支
    result["天马"] = _get_tianma_position(year_branch)
    
    return result


def _get_tiankui_tianyue(year_stem: str) -> Tuple[int, int]:
    """
    获取天魁天钺位置.
    
    天魁天钺对照表（根据年干）：
    甲戊庚：天魁丑，天钺未
    乙己：天魁子，天钺申
    丙丁：天魁亥，天钺酉
    壬癸：天魁卯，天钺巳
    辛：天魁午，天钺寅
    """
    table = {
        "甲": (1, 7),   # 丑、未
        "乙": (0, 8),   # 子、申
        "丙": (11, 9),  # 亥、酉
        "丁": (11, 9),  # 亥、酉
        "戊": (1, 7),   # 丑、未
        "己": (0, 8),   # 子、申
        "庚": (1, 7),   # 丑、未
        "辛": (6, 2),   # 午、寅
        "壬": (3, 5),   # 卯、巳
        "癸": (3, 5),   # 卯、巳
    }
    return table.get(year_stem, (0, 0))


def _get_lucun_position(year_stem: str) -> int:
    """
    获取禄存位置.
    
    禄存对照表（根据年干）：
    甲→寅，乙→卯，丙戊→巳，丁己→午，庚→申，辛→酉，壬→亥，癸→子
    """
    table = {
        "甲": 2, "乙": 3, "丙": 5, "丁": 6, "戊": 5,
        "己": 6, "庚": 8, "辛": 9, "壬": 11, "癸": 0,
    }
    return table.get(year_stem, 0)


def _get_tianma_position(year_branch: str) -> int:
    """
    获取天马位置.
    
    天马对照表（根据年支）：
    寅午戌→申，申子辰→寅，巳酉丑→亥，亥卯未→巳
    """
    branch_idx = EARTHLY_BRANCHES.index(year_branch)
    # 三合局对应天马
    if branch_idx in [2, 6, 10]:   # 寅午戌
        return 8  # 申
    elif branch_idx in [8, 0, 4]:  # 申子辰
        return 2  # 寅
    elif branch_idx in [5, 9, 1]:  # 巳酉丑
        return 11  # 亥
    else:  # 亥卯未
        return 5  # 巳


# =============================================================================
# 煞星安置
# =============================================================================

def place_sha_stars(
    year_stem: str,
    year_branch: str
) -> Dict[str, int]:
    """
    安置煞星.
    
    Args:
        year_stem: 年干
        year_branch: 年支
        
    Returns:
        Dict[str, int]: {星名: 地支索引}
    """
    result = {}
    
    # 擎羊、陀罗：根据年干（禄存前后）
    lucun = _get_lucun_position(year_stem)
    result["擎羊"] = (lucun + 1) % 12  # 禄存顺一位
    result["陀罗"] = (lucun - 1) % 12  # 禄存逆一位
    
    # 火星、铃星：根据年支
    huoxing, lingxing = _get_huoxing_lingxing(year_branch)
    result["火星"] = huoxing
    result["铃星"] = lingxing
    
    # 地空、地劫：根据年支
    dikong, dijie = _get_dikong_dijie(year_branch)
    result["地空"] = dikong
    result["地劫"] = dijie
    
    return result


def _get_huoxing_lingxing(year_branch: str) -> Tuple[int, int]:
    """
    获取火星铃星位置.
    
    火星铃星对照表（根据年支）：
    寅午戌年：火星丑起，铃星卯起
    申子辰年：火星寅起，铃星戌起
    巳酉丑年：火星卯起，铃星戌起
    亥卯未年：火星酉起，铃星戌起
    """
    branch_idx = EARTHLY_BRANCHES.index(year_branch)
    
    if branch_idx in [2, 6, 10]:   # 寅午戌
        return (1, 3)   # 丑、卯
    elif branch_idx in [8, 0, 4]:  # 申子辰
        return (2, 10)  # 寅、戌
    elif branch_idx in [5, 9, 1]:  # 巳酉丑
        return (3, 10)  # 卯、戌
    else:  # 亥卯未
        return (9, 10)  # 酉、戌


def _get_dikong_dijie(year_branch: str) -> Tuple[int, int]:
    """
    获取地空地劫位置.
    
    地空地劫对照表（根据年支）：
    从亥宫起子年，顺数至生年为地劫
    从亥宫起子年，逆数至生年为地空
    """
    branch_idx = EARTHLY_BRANCHES.index(year_branch)
    
    # 地劫：从亥(11)起子年，顺数
    dijie = (11 + branch_idx) % 12
    
    # 地空：从亥(11)起子年，逆数
    dikong = (11 - branch_idx) % 12
    
    return (dikong, dijie)


# =============================================================================
# 星曜亮度
# =============================================================================

# 星曜亮度表：BRIGHTNESS_TABLE[星名][地支索引] = 亮度
# 庙(M)、旺(W)、得地(D)、利(L)、平(P)、不得地(B)、落陷(X)
BRIGHTNESS_TABLE = {
    "紫微": {
        0: "旺", 1: "庙", 2: "落陷", 3: "庙", 4: "旺", 5: "庙",
        6: "庙", 7: "庙", 8: "旺", 9: "庙", 10: "落陷", 11: "庙"
    },
    "天机": {
        0: "庙", 1: "庙", 2: "庙", 3: "旺", 4: "平", 5: "旺",
        6: "庙", 7: "庙", 8: "庙", 9: "旺", 10: "平", 11: "旺"
    },
    "太阳": {
        0: "落陷", 1: "落陷", 2: "庙", 3: "旺", 4: "旺", 5: "庙",
        6: "旺", 7: "得地", 8: "平", 9: "落陷", 10: "落陷", 11: "落陷"
    },
    "武曲": {
        0: "旺", 1: "庙", 2: "平", 3: "平", 4: "庙", 5: "庙",
        6: "旺", 7: "庙", 8: "平", 9: "平", 10: "庙", 11: "庙"
    },
    "天同": {
        0: "旺", 1: "落陷", 2: "平", 3: "庙", 4: "落陷", 5: "庙",
        6: "平", 7: "落陷", 8: "平", 9: "庙", 10: "落陷", 11: "庙"
    },
    "廉贞": {
        0: "平", 1: "庙", 2: "庙", 3: "平", 4: "落陷", 5: "落陷",
        6: "平", 7: "庙", 8: "庙", 9: "平", 10: "落陷", 11: "落陷"
    },
    "天府": {
        0: "庙", 1: "庙", 2: "庙", 3: "得地", 4: "庙", 5: "旺",
        6: "庙", 7: "庙", 8: "庙", 9: "得地", 10: "庙", 11: "旺"
    },
    "太阴": {
        0: "旺", 1: "庙", 2: "落陷", 3: "落陷", 4: "落陷", 5: "平",
        6: "落陷", 7: "得地", 8: "庙", 9: "旺", 10: "庙", 11: "庙"
    },
    "贪狼": {
        0: "旺", 1: "平", 2: "庙", 3: "旺", 4: "庙", 5: "平",
        6: "旺", 7: "平", 8: "庙", 9: "旺", 10: "庙", 11: "平"
    },
    "巨门": {
        0: "旺", 1: "落陷", 2: "庙", 3: "庙", 4: "落陷", 5: "庙",
        6: "旺", 7: "落陷", 8: "庙", 9: "庙", 10: "落陷", 11: "庙"
    },
    "天相": {
        0: "庙", 1: "庙", 2: "庙", 3: "落陷", 4: "庙", 5: "庙",
        6: "庙", 7: "庙", 8: "庙", 9: "落陷", 10: "庙", 11: "庙"
    },
    "天梁": {
        0: "庙", 1: "庙", 2: "庙", 3: "旺", 4: "落陷", 5: "庙",
        6: "庙", 7: "庙", 8: "庙", 9: "旺", 10: "落陷", 11: "庙"
    },
    "七杀": {
        0: "旺", 1: "庙", 2: "庙", 3: "落陷", 4: "旺", 5: "平",
        6: "旺", 7: "庙", 8: "庙", 9: "落陷", 10: "旺", 11: "平"
    },
    "破军": {
        0: "旺", 1: "落陷", 2: "庙", 3: "落陷", 4: "庙", 5: "落陷",
        6: "旺", 7: "落陷", 8: "庙", 9: "落陷", 10: "庙", 11: "落陷"
    },
}


def get_star_brightness(star_name: str, branch_idx: int) -> Optional[str]:
    """
    获取星曜亮度.
    
    Args:
        star_name: 星曜名称
        branch_idx: 所在地支索引
        
    Returns:
        Optional[str]: 亮度等级，如果星曜不在表中返回None
    """
    if star_name not in BRIGHTNESS_TABLE:
        return None
    return BRIGHTNESS_TABLE[star_name].get(branch_idx)


# =============================================================================
# 完整星曜安置
# =============================================================================

def place_all_stars(
    lunar_date: LunarDate,
    five_element_num: int
) -> Tuple[Dict[str, int], Dict[str, str]]:
    """
    安置所有星曜.
    
    Args:
        lunar_date: 农历日期
        five_element_num: 五行局数字
        
    Returns:
        Tuple[Dict[str, int], Dict[str, str]]: 
            (星曜位置字典, 星曜亮度字典)
    """
    positions: Dict[str, int] = {}
    brightness: Dict[str, str] = {}
    
    # 1. 紫微星系
    ziwei_pos = calculate_ziwei_position(lunar_date.day, five_element_num)
    ziwei_group = place_ziwei_group(ziwei_pos)
    positions.update(ziwei_group)
    
    # 2. 天府星系
    tianfu_pos = calculate_tianfu_position(ziwei_pos)
    tianfu_group = place_tianfu_group(tianfu_pos)
    positions.update(tianfu_group)
    
    # 3. 辅星
    auxiliary = place_auxiliary_stars(
        lunar_date.month,
        lunar_date.hour_branch,
        lunar_date.year_stem,
        lunar_date.year_branch
    )
    positions.update(auxiliary)
    
    # 4. 煞星
    sha = place_sha_stars(
        lunar_date.year_stem,
        lunar_date.year_branch
    )
    positions.update(sha)
    
    # 5. 计算亮度
    for star_name, branch_idx in positions.items():
        b = get_star_brightness(star_name, branch_idx)
        if b:
            brightness[star_name] = b
    
    return positions, brightness


def create_star_objects(
    positions: Dict[str, int],
    brightness: Dict[str, str]
) -> List[Star]:
    """
    创建Star对象列表.
    
    Args:
        positions: 星曜位置字典
        brightness: 星曜亮度字典
        
    Returns:
        List[Star]: Star对象列表
    """
    stars: List[Star] = []
    
    for star_name, branch_idx in positions.items():
        # 判断星曜类型
        if star_name in MAIN_STARS:
            star_type = "main"
        elif star_name in AUXILIARY_STARS:
            star_type = "auxiliary"
        elif star_name in SHA_STARS:
            star_type = "sha"
        else:
            star_type = "auxiliary"  # 默认
        
        # 获取亮度
        b = brightness.get(star_name)
        star_brightness = None
        if b:
            try:
                star_brightness = StarBrightness(b)
            except:
                pass
        
        star = Star(
            name=star_name,
            star_type=star_type,
            palace_index=branch_idx,
            brightness=star_brightness,
        )
        stars.append(star)
    
    return stars
