# backend/calculators/bazi/ten_gods.py
"""
十神推导模块.

十神是以日主（日柱天干）为中心，与其他天干的五行生克关系确定的。

十神分类：
- 同我：比肩（同阴阳）、劫财（异阴阳）
- 我生：食神（同阴阳）、伤官（异阴阳）
- 我克：偏财（同阴阳）、正财（异阴阳）
- 克我：七杀（同阴阳）、正官（异阴阳）
- 生我：偏印（同阴阳）、正印（异阴阳）
"""

from typing import Dict, List, Optional

from backend.calculators.bazi.models import (
    HEAVENLY_STEMS,
    STEM_ELEMENT,
    STEM_YINYANG,
    TenGod,
    Pillar,
    FourPillars,
    TEN_GOD_NAMES,
)
from backend.calculators.bazi.hidden_stems import extract_hidden_stems


# =============================================================================
# 五行生克关系
# =============================================================================

# 五行相生: 木生火, 火生土, 土生金, 金生水, 水生木
ELEMENT_GENERATES = {
    "wood": "fire",
    "fire": "earth",
    "earth": "metal",
    "metal": "water",
    "water": "wood",
}

# 五行相克: 木克土, 土克水, 水克火, 火克金, 金克木
ELEMENT_CONQUERS = {
    "wood": "earth",
    "earth": "water",
    "water": "fire",
    "fire": "metal",
    "metal": "wood",
}

# 反向查找：什么生我
ELEMENT_GENERATED_BY = {v: k for k, v in ELEMENT_GENERATES.items()}

# 反向查找：什么克我
ELEMENT_CONQUERED_BY = {v: k for k, v in ELEMENT_CONQUERS.items()}


def get_ten_god(day_master: str, target_stem: str) -> str:
    """
    计算某天干相对于日主的十神.
    
    Args:
        day_master: 日主天干
        target_stem: 目标天干
        
    Returns:
        str: 十神名称
        
    Raises:
        ValueError: 如果天干无效
    """
    if day_master not in HEAVENLY_STEMS:
        raise ValueError(f"Invalid day master: {day_master}")
    if target_stem not in HEAVENLY_STEMS:
        raise ValueError(f"Invalid target stem: {target_stem}")
    
    dm_element = STEM_ELEMENT[day_master]
    dm_yinyang = STEM_YINYANG[day_master]
    
    target_element = STEM_ELEMENT[target_stem]
    target_yinyang = STEM_YINYANG[target_stem]
    
    same_yinyang = (dm_yinyang == target_yinyang)
    
    # 判断五行关系
    if dm_element == target_element:
        # 同我
        return "比肩" if same_yinyang else "劫财"
    
    elif ELEMENT_GENERATES[dm_element] == target_element:
        # 我生
        return "食神" if same_yinyang else "伤官"
    
    elif ELEMENT_CONQUERS[dm_element] == target_element:
        # 我克
        return "偏财" if same_yinyang else "正财"
    
    elif ELEMENT_CONQUERED_BY[dm_element] == target_element:
        # 克我
        return "七杀" if same_yinyang else "正官"
    
    elif ELEMENT_GENERATED_BY[dm_element] == target_element:
        # 生我
        return "偏印" if same_yinyang else "正印"
    
    # 理论上不应该到这里
    raise ValueError(f"Cannot determine ten god relationship: {day_master} -> {target_stem}")


def analyze_ten_gods(four_pillars: FourPillars) -> tuple[List[TenGod], Dict[str, int]]:
    """
    分析四柱的十神分布.
    
    Args:
        four_pillars: 四柱信息
        
    Returns:
        tuple: (十神列表, 十神统计)
        
    Note:
        - 包含四柱天干的十神
        - 包含四柱地支藏干的十神
        - 日干（比肩）通常不计入统计
    """
    day_master = four_pillars.day.stem
    ten_gods: List[TenGod] = []
    ten_god_counts: Dict[str, int] = {name: 0 for name in TEN_GOD_NAMES}
    
    pillars = [
        ("year", four_pillars.year),
        ("month", four_pillars.month),
        ("day", four_pillars.day),
        ("hour", four_pillars.hour),
    ]
    
    for pillar_name, pillar in pillars:
        # 1. 天干的十神（日干除外）
        if pillar_name != "day":
            god_name = get_ten_god(day_master, pillar.stem)
            ten_gods.append(TenGod(
                name=god_name,
                stem=pillar.stem,
                pillar=pillar_name,
                is_hidden=False,
            ))
            ten_god_counts[god_name] += 1
        
        # 2. 藏干的十神
        hidden_stems = extract_hidden_stems(pillar.branch)
        for hs in hidden_stems:
            god_name = get_ten_god(day_master, hs.stem)
            ten_gods.append(TenGod(
                name=god_name,
                stem=hs.stem,
                pillar=pillar_name,
                is_hidden=True,
            ))
            # 藏干十神也计入统计（但权重可能不同，这里简化处理）
            ten_god_counts[god_name] += 1
    
    return ten_gods, ten_god_counts


def get_useful_god_candidates(
    day_master: str,
    element_scores: Dict[str, float],
    day_master_strength: float
) -> List[str]:
    """
    推断可能的用神候选.
    
    基于日主强弱判断用神方向：
    - 身强: 宜泄、宜克（食神、伤官、偏财、正财、七杀、正官）
    - 身弱: 宜帮、宜生（比肩、劫财、偏印、正印）
    
    Args:
        day_master: 日主天干
        element_scores: 五行强度
        day_master_strength: 日主强度 (0.0-1.0)
        
    Returns:
        List[str]: 用神候选的十神名称列表
    """
    candidates = []
    
    if day_master_strength > 0.6:
        # 身强：宜泄克
        candidates = ["食神", "伤官", "偏财", "正财", "七杀", "正官"]
    elif day_master_strength < 0.4:
        # 身弱：宜帮生
        candidates = ["比肩", "劫财", "偏印", "正印"]
    else:
        # 中等：具体分析
        dm_element = STEM_ELEMENT[day_master]
        dm_score = element_scores.get(dm_element, 0.0)
        
        # 找最弱的有利五行
        if dm_score < 0.5:
            candidates = ["比肩", "劫财", "偏印", "正印"]
        else:
            candidates = ["食神", "伤官", "偏财", "正财"]
    
    return candidates
