# backend/calculators/bazi/hidden_stems.py
"""
藏干映射模块 - 子平派标准.

地支藏干规则：
- 本气 (main): 地支本身所藏的主气天干，权重最高
- 中气 (middle): 地支中藏的次要天干，权重中等
- 余气 (residual): 地支中藏的残余天干，权重最低

权重分配采用子平派标准：
- 单藏: 本气 1.0
- 双藏: 本气 0.7, 余气 0.3
- 三藏: 本气 0.6, 中气 0.3, 余气 0.1
"""

from typing import List, Tuple

from backend.calculators.bazi.models import HiddenStem


# =============================================================================
# 藏干映射表（子平派标准）
# =============================================================================

# 格式: 地支 -> [(天干, 权重, 角色), ...]
HIDDEN_STEM_MAP: dict[str, List[Tuple[str, float, str]]] = {
    # 子: 癸水（单藏）
    "子": [("癸", 1.0, "main")],
    
    # 丑: 己土本气，癸水中气，辛金余气（三藏）
    "丑": [
        ("己", 0.6, "main"),
        ("癸", 0.3, "middle"),
        ("辛", 0.1, "residual"),
    ],
    
    # 寅: 甲木本气，丙火中气，戊土余气（三藏）
    "寅": [
        ("甲", 0.6, "main"),
        ("丙", 0.3, "middle"),
        ("戊", 0.1, "residual"),
    ],
    
    # 卯: 乙木（单藏）
    "卯": [("乙", 1.0, "main")],
    
    # 辰: 戊土本气，乙木中气，癸水余气（三藏）
    "辰": [
        ("戊", 0.6, "main"),
        ("乙", 0.3, "middle"),
        ("癸", 0.1, "residual"),
    ],
    
    # 巳: 丙火本气，庚金中气，戊土余气（三藏）
    "巳": [
        ("丙", 0.6, "main"),
        ("庚", 0.3, "middle"),
        ("戊", 0.1, "residual"),
    ],
    
    # 午: 丁火本气，己土余气（双藏）
    "午": [
        ("丁", 0.7, "main"),
        ("己", 0.3, "residual"),
    ],
    
    # 未: 己土本气，丁火中气，乙木余气（三藏）
    "未": [
        ("己", 0.6, "main"),
        ("丁", 0.3, "middle"),
        ("乙", 0.1, "residual"),
    ],
    
    # 申: 庚金本气，壬水中气，戊土余气（三藏）
    "申": [
        ("庚", 0.6, "main"),
        ("壬", 0.3, "middle"),
        ("戊", 0.1, "residual"),
    ],
    
    # 酉: 辛金（单藏）
    "酉": [("辛", 1.0, "main")],
    
    # 戌: 戊土本气，辛金中气，丁火余气（三藏）
    "戌": [
        ("戊", 0.6, "main"),
        ("辛", 0.3, "middle"),
        ("丁", 0.1, "residual"),
    ],
    
    # 亥: 壬水本气，甲木余气（双藏）
    "亥": [
        ("壬", 0.7, "main"),
        ("甲", 0.3, "residual"),
    ],
}


def extract_hidden_stems(branch: str) -> List[HiddenStem]:
    """
    提取地支中的藏干.
    
    Args:
        branch: 地支字符
        
    Returns:
        List[HiddenStem]: 藏干列表，按权重降序排列
        
    Raises:
        ValueError: 如果地支无效
        
    Example:
        >>> extract_hidden_stems("寅")
        [HiddenStem(stem='甲', weight=0.6, role='main'),
         HiddenStem(stem='丙', weight=0.3, role='middle'),
         HiddenStem(stem='戊', weight=0.1, role='residual')]
    """
    if branch not in HIDDEN_STEM_MAP:
        raise ValueError(f"Invalid earthly branch: {branch}")
    
    return [
        HiddenStem(stem=stem, weight=weight, role=role)  # type: ignore
        for stem, weight, role in HIDDEN_STEM_MAP[branch]
    ]


def get_main_hidden_stem(branch: str) -> str:
    """
    获取地支的本气（主藏干）.
    
    Args:
        branch: 地支字符
        
    Returns:
        str: 本气天干
        
    Raises:
        ValueError: 如果地支无效
    """
    if branch not in HIDDEN_STEM_MAP:
        raise ValueError(f"Invalid earthly branch: {branch}")
    
    return HIDDEN_STEM_MAP[branch][0][0]


def get_hidden_stem_weight(branch: str, stem: str) -> float:
    """
    获取特定藏干在地支中的权重.
    
    Args:
        branch: 地支字符
        stem: 天干字符
        
    Returns:
        float: 权重值，如果该天干不在藏干中则返回 0.0
    """
    if branch not in HIDDEN_STEM_MAP:
        return 0.0
    
    for hidden_stem, weight, _ in HIDDEN_STEM_MAP[branch]:
        if hidden_stem == stem:
            return weight
    
    return 0.0
