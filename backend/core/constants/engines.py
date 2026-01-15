# backend/core/constants/engines.py
"""
引擎 ID 常量和标准化

所有 7 个体系的引擎 ID 定义和别名映射。
用于解决 API 请求中的简写（如 'bazi'）与内部 engine_id（如 'bazi-calculator'）不匹配的问题。

Usage:
    from backend.core.constants import normalize_engine_id, normalize_engine_ids
    
    # 单个标准化
    engine_id = normalize_engine_id("bazi")  # -> "bazi-calculator"
    
    # 批量标准化
    engine_ids = normalize_engine_ids(["bazi", "astro"])  # -> ["bazi-calculator", "astro-calculator"]
"""

from typing import List, Optional

# =============================================================================
# 标准引擎 ID (内部使用，与各 Calculator 的 to_factor_matrix() 中的 engine_id 一致)
# =============================================================================

ENGINE_BAZI = "bazi-calculator"
ENGINE_ASTRO = "astro-calculator"
ENGINE_ZIWEI = "ziwei-calculator"
ENGINE_TAROT = "tarot-interpreter"
ENGINE_DREAM = "dream-extractor"
ENGINE_YIJING = "yijing-calculator"
ENGINE_PSYCH = "psych-analyzer"

ALL_ENGINE_IDS = [
    ENGINE_BAZI,
    ENGINE_ASTRO,
    ENGINE_ZIWEI,
    ENGINE_TAROT,
    ENGINE_DREAM,
    ENGINE_YIJING,
    ENGINE_PSYCH,
]

# =============================================================================
# 别名映射表
# 包含：简写、中文、全称（自身映射，确保幂等性）
# =============================================================================

ENGINE_ALIAS_MAP = {
    # 八字
    "bazi": ENGINE_BAZI,
    "bazi-calculator": ENGINE_BAZI,
    "八字": ENGINE_BAZI,
    "bz": ENGINE_BAZI,
    
    # 占星
    "astro": ENGINE_ASTRO,
    "astro-calculator": ENGINE_ASTRO,
    "astrology": ENGINE_ASTRO,  # 前端使用
    "星盘": ENGINE_ASTRO,
    "西占": ENGINE_ASTRO,
    "as": ENGINE_ASTRO,
    
    # 紫微
    "ziwei": ENGINE_ZIWEI,
    "ziwei-calculator": ENGINE_ZIWEI,
    "紫微": ENGINE_ZIWEI,
    "zw": ENGINE_ZIWEI,
    
    # 塔罗
    "tarot": ENGINE_TAROT,
    "tarot-interpreter": ENGINE_TAROT,
    "塔罗": ENGINE_TAROT,
    "tr": ENGINE_TAROT,
    
    # 解梦
    "dream": ENGINE_DREAM,
    "dream-extractor": ENGINE_DREAM,
    "解梦": ENGINE_DREAM,
    "dr": ENGINE_DREAM,
    
    # 易经
    "yijing": ENGINE_YIJING,
    "yijing-calculator": ENGINE_YIJING,
    "iching": ENGINE_YIJING,  # 前端使用
    "i ching": ENGINE_YIJING,
    "易经": ENGINE_YIJING,
    "周易": ENGINE_YIJING,
    "yj": ENGINE_YIJING,
    
    # 心理
    "psych": ENGINE_PSYCH,
    "psych-analyzer": ENGINE_PSYCH,
    "心理": ENGINE_PSYCH,
    "ps": ENGINE_PSYCH,
}


def normalize_engine_id(engine_id: Optional[str]) -> Optional[str]:
    """
    将引擎简写/别名转换为标准 ID
    
    Args:
        engine_id: 输入的引擎 ID（可能是简写、中文或标准 ID）
        
    Returns:
        标准化的引擎 ID，未知 ID 原样返回，空值返回空值
        
    Examples:
        >>> normalize_engine_id("bazi")
        'bazi-calculator'
        >>> normalize_engine_id("八字")
        'bazi-calculator'
        >>> normalize_engine_id("BAZI")
        'bazi-calculator'
        >>> normalize_engine_id(" bazi ")
        'bazi-calculator'
        >>> normalize_engine_id("bazi-calculator")
        'bazi-calculator'
        >>> normalize_engine_id("unknown")
        'unknown'
    """
    if not engine_id:
        return engine_id
    normalized_key = engine_id.lower().strip()
    return ENGINE_ALIAS_MAP.get(normalized_key, engine_id)


def normalize_engine_ids(engine_ids: Optional[List[str]]) -> Optional[List[str]]:
    """
    批量标准化引擎 ID
    
    Args:
        engine_ids: 引擎 ID 列表
        
    Returns:
        标准化后的引擎 ID 列表，None 返回 None
    """
    if engine_ids is None:
        return None
    return [normalize_engine_id(eid) for eid in engine_ids]


def is_valid_engine_id(engine_id: str) -> bool:
    """
    检查是否为有效的引擎 ID（标准或别名）
    
    Args:
        engine_id: 待检查的引擎 ID
        
    Returns:
        True 如果是已知的引擎 ID 或别名
    """
    if not engine_id:
        return False
    return engine_id.lower().strip() in ENGINE_ALIAS_MAP
