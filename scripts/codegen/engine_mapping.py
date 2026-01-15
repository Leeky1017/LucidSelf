"""
Engine Mapping Configuration

体系与典籍映射配置，对齐 design.md Components and Interfaces §3

核心映射:
- ENGINE_BOOK_MAPPING: 7 个体系到 24 本书籍的映射
- SOURCE_PATH_MAPPING: book_id 到实际目录路径的映射
- FACTOR_ID_PREFIXES: 各体系的 factor_id 前缀列表
"""

from typing import Dict, List

# -----------------------------------------------------------------------------
# 7 体系 → 24 本典籍映射 (对齐 design.md §3, tasks.md 1.1)
# -----------------------------------------------------------------------------

ENGINE_BOOK_MAPPING: Dict[str, List[str]] = {
    # 八字体系 (5 本)
    "bazi": [
        "dts",              # 滴天髓
        "sanming",          # 三命通会
        "zipingzhenquan",   # 子平真诠
        "yuanhaiziping",    # 渊海子平
        "qiongtongbaojian", # 穷通宝鉴
        # 注：记纂渊海已归档，不在当前迁移范围
    ],
    # 紫微体系 (1 本)
    "ziwei": [
        "ziwei",            # 紫微斗数全书
    ],
    # 塔罗体系 (4 本)
    "tarot": [
        "waite_tarot",      # Waite Pictorial Key to the Tarot
        "pollack_tarot",    # 78 Degrees of Wisdom
        "learning_tarot",   # Learning the Tarot
        "book_of_thoth",    # The Book of Thoth
    ],
    # 西占体系 (6 本)
    "astro": [
        "the_inner_sky",        # The Inner Sky
        "christian_astrology",  # Christian Astrology
        "tetrabiblos",          # Tetrabiblos
        "planets_in_transit",   # Planets in Transit
        "astrological_houses",  # The Astrological Houses
        "astrology_personality",# Astrology of Personality
    ],
    # 梦境体系 (5 本)
    "dream": [
        "mlxj",                 # 梦林玄解
        "zhougong",             # 周公解梦
        "llewellyns_dreams",    # Llewellyn's Complete Dictionary of Dreams
        "dreams_visions_dict",  # The Dreams & Visions Symbol Dictionary
        "interpretation_dreams",# The Interpretation of Dreams
    ],
    # 易经体系 (1 本)
    "yijing": [
        "zhouyi",               # 周易
    ],
    # 心理学体系 (2 本)
    "psych": [
        "archetypes_unconscious",  # The Archetypes and the Collective Unconscious
        "collected_works",         # The Collected Works of C.G. Jung
    ],
}

# -----------------------------------------------------------------------------
# book_id → 源目录路径映射 (对齐 design.md §3, tasks.md 1.1)
# -----------------------------------------------------------------------------

SOURCE_PATH_MAPPING: Dict[str, str] = {
    # 中文典籍 (9 本)
    "dts": "典籍/中文典籍/滴天髓",
    "sanming": "典籍/中文典籍/三命通会",
    "zipingzhenquan": "典籍/中文典籍/子平真诠",
    "yuanhaiziping": "典籍/中文典籍/渊海子平",
    "qiongtongbaojian": "典籍/中文典籍/穷通宝鉴",
    "ziwei": "典籍/中文典籍/紫微斗数全书",
    "mlxj": "典籍/中文典籍/梦林玄解",
    "zhougong": "典籍/中文典籍/周公解梦",
    "zhouyi": "典籍/中文典籍/周易",
    # 注：记纂渊海已归档到 典籍/中文典籍/archive/
    
    # 英文典籍 (15 本) - 路径对齐实际目录结构
    "waite_tarot": "典籍/texts/Waite Pictorial Key to the Tarot",
    "pollack_tarot": "典籍/texts/78 Degrees of Wisdom",
    "learning_tarot": "典籍/texts/Learning the Tarot",
    "book_of_thoth": "典籍/texts/The book of Thoth",
    "the_inner_sky": "典籍/texts/The Inner Sky",
    "christian_astrology": "典籍/texts/Christian Astrology, vol. 1 and 2",
    "tetrabiblos": "典籍/texts/Tetrabiblos",
    "planets_in_transit": "典籍/texts/Planets in Transit",
    "astrological_houses": "典籍/texts/The Astrological Houses",
    "astrology_personality": "典籍/texts/astrology of personality",
    "llewellyns_dreams": "典籍/texts/Llewellyns Complete Dictionary of Dreams",
    "dreams_visions_dict": "典籍/texts/The Dreams & Visions Symbol Dictionary",
    "interpretation_dreams": "典籍/texts/The Interpretation of Dreams",
    "archetypes_unconscious": "典籍/texts/The Archetypes and the Collective Unconscious",
    "collected_works": "典籍/texts/the collected works",
}

# 总计: 24 本典籍 (9 中文 + 15 英文，不含已归档的记纂渊海)

# -----------------------------------------------------------------------------
# book_id → book_abbr 映射 (用于 semantic_id 生成)
# 格式: 2-4 位小写字母缩写
# -----------------------------------------------------------------------------

BOOK_ABBR: Dict[str, str] = {
    # 中文典籍
    "dts": "dts",           # 滴天髓
    "sanming": "smth",      # 三命通会
    "zipingzhenquan": "zpzq",  # 子平真诠
    "yuanhaiziping": "yhzp",   # 渊海子平
    "qiongtongbaojian": "qtbj", # 穷通宝鉴
    "ziwei": "zw",          # 紫微斗数全书
    "mlxj": "mlxj",         # 梦林玄解
    "zhougong": "zgjm",     # 周公解梦
    "zhouyi": "zy",         # 周易
    # 英文典籍
    "waite_tarot": "wt",    # Waite Pictorial Key to the Tarot
    "pollack_tarot": "pt",  # 78 Degrees of Wisdom
    "learning_tarot": "lt", # Learning the Tarot
    "book_of_thoth": "bot", # The Book of Thoth
    "the_inner_sky": "tis", # The Inner Sky
    "christian_astrology": "ca", # Christian Astrology
    "tetrabiblos": "tb",    # Tetrabiblos
    "planets_in_transit": "pit", # Planets in Transit
    "astrological_houses": "ah", # The Astrological Houses
    "astrology_personality": "ap", # Astrology of Personality
    "llewellyns_dreams": "ld", # Llewellyn's Complete Dictionary of Dreams
    "dreams_visions_dict": "dvd", # The Dreams & Visions Symbol Dictionary
    "interpretation_dreams": "iod", # The Interpretation of Dreams
    "archetypes_unconscious": "acu", # The Archetypes and the Collective Unconscious
    "collected_works": "cw", # The Collected Works of C.G. Jung
}


def get_book_abbr(book_id: str) -> str:
    """获取书籍缩写，用于 semantic_id 生成"""
    return BOOK_ABBR.get(book_id, book_id[:4])


# -----------------------------------------------------------------------------
# 各体系 factor_id 前缀映射 (对齐 design.md Data Models §2)
# -----------------------------------------------------------------------------

FACTOR_ID_PREFIXES: Dict[str, List[str]] = {
    "bazi": [
        "day_master_",      # 日主: day_master_jia, day_master_yi, ...
        "season_",          # 季节: season_spring, season_summer, ...
        "ten_god_",         # 十神: ten_god_zhengguan, ten_god_qisha, ...
        "strength_",        # 身强弱: strength_strong, strength_weak
        "element_",         # 五行: element_wood, element_fire, ...
        "stem_",            # 天干: stem_jia, stem_yi, ...
        "branch_",          # 地支: branch_zi, branch_chou, ...
        "bazi_",            # 通用八字前缀
    ],
    "ziwei": [
        "ziwei_star_",      # 主星: ziwei_star_ziwei, ziwei_star_tianji, ...
        "ziwei_palace_",    # 宫位: ziwei_palace_ming, ziwei_palace_xiongdi, ...
        "ziwei_transform_", # 四化: ziwei_transform_lu, ziwei_transform_quan, ...
        "ziwei_aux_",       # 辅星: ziwei_aux_zuofu, ziwei_aux_youbi, ...
    ],
    "tarot": [
        "tarot_major_",     # 大阿卡纳: tarot_major_the_fool, ...
        "tarot_wands_",     # 权杖: tarot_wands_ace, ...
        "tarot_cups_",      # 圣杯: tarot_cups_ace, ...
        "tarot_swords_",    # 宝剑: tarot_swords_ace, ...
        "tarot_pentacles_", # 钱币: tarot_pentacles_ace, ...
        "tarot_position_",  # 位置: tarot_position_past, ...
        "suit_",            # 花色: suit_wands, suit_cups, ...
        "orientation_",     # 方向: orientation_upright, orientation_reversed
    ],
    "astro": [
        "astro_planet_",    # 行星: astro_planet_sun, astro_planet_moon, ...
        "astro_sign_",      # 星座: astro_sign_aries, astro_sign_taurus, ...
        "astro_house_",     # 宫位: astro_house_1, astro_house_2, ...
        "astro_aspect_",    # 相位: astro_aspect_conjunction, ...
        "astro_ascendant",  # 上升点
        "astro_midheaven",  # 中天
        "astro_",           # 通用西占前缀
    ],
    "dream": [
        "dream_symbol_",    # 符号: dream_symbol_animal_dog, ...
        "dream_theme_",     # 主题: dream_theme_chase, dream_theme_falling, ...
        "dream_emotion_",   # 情绪: dream_emotion_fear, dream_emotion_joy, ...
    ],
    "yijing": [
        "yijing_gua_",      # 卦: yijing_gua_qian, yijing_gua_kun, ...
        "yijing_yao_",      # 爻: yijing_yao_1, yijing_yao_2, ...
        "yijing_upper_",    # 上卦
        "yijing_lower_",    # 下卦
        "yijing_mutual_",   # 互卦
        "yijing_changed_",  # 变卦
        "yijing_yang_",     # 阳爻
        "yijing_yin_",      # 阴爻
        "yijing_moving_",   # 动爻
    ],
    "psych": [
        "psych_archetype_", # 原型: psych_archetype_shadow, ...
        "psych_function_",  # 功能: psych_function_thinking, ...
        "psych_attitude_",  # 态度: psych_attitude_introvert, ...
        "psych_process_",   # 进程: psych_process_individuation, ...
    ],
}

# -----------------------------------------------------------------------------
# 有效引擎 ID 列表
# -----------------------------------------------------------------------------

VALID_ENGINE_IDS = list(ENGINE_BOOK_MAPPING.keys())


# -----------------------------------------------------------------------------
# 工具函数 (对齐 tasks.md 1.1)
# -----------------------------------------------------------------------------

def infer_engine_id(book_id: str) -> str:
    """
    从 book_id 推断 engine_id
    
    遍历 ENGINE_BOOK_MAPPING，返回包含该 book_id 的 engine_id
    
    Args:
        book_id: 书籍 ID
    
    Returns:
        engine_id，未找到则返回 "bazi" (默认)
    """
    for engine_id, books in ENGINE_BOOK_MAPPING.items():
        if book_id in books:
            return engine_id
    return "bazi"  # 默认


def infer_primary_lang(book_id: str) -> str:
    """
    从 book_id 推断 primary_lang
    
    检查 SOURCE_PATH_MAPPING[book_id]，若包含 "中文典籍" 返回 "zh-CN"，否则返回 "en-US"
    
    Args:
        book_id: 书籍 ID
    
    Returns:
        "zh-CN" 或 "en-US"
    """
    source_path = SOURCE_PATH_MAPPING.get(book_id, "")
    if "中文典籍" in source_path:
        return "zh-CN"
    return "en-US"


def get_all_book_ids() -> List[str]:
    """获取所有 24 本书籍的 book_id 列表"""
    all_books = []
    for books in ENGINE_BOOK_MAPPING.values():
        all_books.extend(books)
    return all_books


def get_books_by_engine(engine_id: str) -> List[str]:
    """获取指定引擎的书籍列表"""
    return ENGINE_BOOK_MAPPING.get(engine_id, [])


def validate_factor_prefix(factor_id: str, engine_id: str) -> bool:
    """
    验证 factor_id 是否使用正确的引擎前缀
    
    Args:
        factor_id: 因子 ID
        engine_id: 引擎 ID
    
    Returns:
        True 如果 factor_id 以 engine_id 的有效前缀开头
    """
    prefixes = FACTOR_ID_PREFIXES.get(engine_id, [])
    return any(factor_id.startswith(prefix) for prefix in prefixes)


# -----------------------------------------------------------------------------
# 统计信息
# -----------------------------------------------------------------------------

TOTAL_BOOKS = sum(len(books) for books in ENGINE_BOOK_MAPPING.values())  # 24
CHINESE_BOOKS = sum(1 for book_id in SOURCE_PATH_MAPPING if "中文典籍" in SOURCE_PATH_MAPPING[book_id])  # 9
ENGLISH_BOOKS = TOTAL_BOOKS - CHINESE_BOOKS  # 15
