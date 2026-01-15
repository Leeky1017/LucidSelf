"""
Constants - 常量定义

定义目标书籍列表、书籍类型映射等常量。
"""

from typing import Dict, List

# 目标书籍列表 (21本)
TARGET_BOOKS: List[str] = [
    # 中文典籍 (8本)
    "滴天髓",
    "子平真诠",
    "穷通宝鉴",
    "渊海子平",
    "三命通会",
    "紫微斗数全书",
    "周易",
    "周公解梦",
    # 西方典籍 (13本)
    "the_inner_sky",
    "planets_in_transit",
    "the_astrological_houses",
    "astrology_of_personality",
    "tetrabiblos",
    "christian_astrology,_vol._1_and_2",
    "the_book_of_thoth",
    "78_degrees_of_wisdom",
    "waite_pictorial_key_to_the_tarot",
    "learning_the_tarot",
    "the_interpretation_of_dreams",
    "llewellyns_complete_dictionary_of_dreams",
    "the_archetypes_and_the_collective_unconscious",
]

# 书籍类型映射
BOOK_TYPE_MAP: Dict[str, List[str]] = {
    "命理": [
        "滴天髓",
        "子平真诠",
        "穷通宝鉴",
        "渊海子平",
        "三命通会",
        "紫微斗数全书",
    ],
    "占卜": [
        "周易",
        "the_book_of_thoth",
        "78_degrees_of_wisdom",
        "waite_pictorial_key_to_the_tarot",
        "learning_the_tarot",
    ],
    "梦学": [
        "周公解梦",
        "the_interpretation_of_dreams",
        "llewellyns_complete_dictionary_of_dreams",
        "the_archetypes_and_the_collective_unconscious",
    ],
    "西方占星": [
        "the_inner_sky",
        "planets_in_transit",
        "the_astrological_houses",
        "astrology_of_personality",
        "tetrabiblos",
        "christian_astrology,_vol._1_and_2",
    ],
}

# 论证模式
ARGUMENT_PATTERNS: Dict[str, str] = {
    "命理": "格局→用神→吉凶",
    "占卜": "符号→意象→诠释",
    "梦学": "象征→心理→解析",
    "西方占星": "星体→宫位→相位→诠释",
}

# 角色优先级 (数字越小优先级越高)
ROLE_PRIORITY: Dict[str, int] = {
    "主干": 1,
    "主干依赖": 2,
    "条件分支": 3,
    "例外处理": 4,
    "总结": 5,
}

# 关系类型映射
RELATION_TYPE_MAPPING: Dict[str, str] = {
    "hierarchy": "depends_on",
    "dependency": "depends_on",
    "cooperation": "supports",
    "supports": "supports",
    "conditional": "leads_to",
    "gateway": "leads_to",
    "conflict": "conflicts_with",
}

# 路径常量
SCHEMA_STAGING_DIR = "data/schema_staging"
SNIPPETS_DIR = f"{SCHEMA_STAGING_DIR}/snippets"
RELATIONS_DIR = f"{SCHEMA_STAGING_DIR}/relations"
OUTPUT_DIR = "data/logic_chains"

# 摘要最大长度
MAX_SUMMARY_LENGTH = 50
