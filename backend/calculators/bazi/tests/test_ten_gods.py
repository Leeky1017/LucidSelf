# backend/calculators/bazi/tests/test_ten_gods.py
"""
Unit tests for ten gods module.
"""

import pytest

from backend.calculators.bazi.ten_gods import (
    get_ten_god,
    analyze_ten_gods,
    ELEMENT_GENERATES,
    ELEMENT_CONQUERS,
)
from backend.calculators.bazi.models import (
    Pillar,
    FourPillars,
    HEAVENLY_STEMS,
    TEN_GOD_NAMES,
)


class TestGetTenGod:
    """十神推导测试."""
    
    def test_same_element_same_yinyang(self):
        """同我同阴阳 = 比肩."""
        # 甲见甲
        assert get_ten_god("甲", "甲") == "比肩"
        # 乙见乙
        assert get_ten_god("乙", "乙") == "比肩"
    
    def test_same_element_diff_yinyang(self):
        """同我异阴阳 = 劫财."""
        # 甲见乙
        assert get_ten_god("甲", "乙") == "劫财"
        # 乙见甲
        assert get_ten_god("乙", "甲") == "劫财"
    
    def test_i_generate_same_yinyang(self):
        """我生同阴阳 = 食神."""
        # 甲木生丙火（同阳）
        assert get_ten_god("甲", "丙") == "食神"
        # 乙木生丁火（同阴）
        assert get_ten_god("乙", "丁") == "食神"
    
    def test_i_generate_diff_yinyang(self):
        """我生异阴阳 = 伤官."""
        # 甲木生丁火（阳生阴）
        assert get_ten_god("甲", "丁") == "伤官"
        # 乙木生丙火（阴生阳）
        assert get_ten_god("乙", "丙") == "伤官"
    
    def test_i_conquer_same_yinyang(self):
        """我克同阴阳 = 偏财."""
        # 甲木克戊土（同阳）
        assert get_ten_god("甲", "戊") == "偏财"
    
    def test_i_conquer_diff_yinyang(self):
        """我克异阴阳 = 正财."""
        # 甲木克己土（阳克阴）
        assert get_ten_god("甲", "己") == "正财"
    
    def test_conquers_me_same_yinyang(self):
        """克我同阴阳 = 七杀."""
        # 庚金克甲木（同阳）
        assert get_ten_god("甲", "庚") == "七杀"
    
    def test_conquers_me_diff_yinyang(self):
        """克我异阴阳 = 正官."""
        # 辛金克甲木（阴克阳）
        assert get_ten_god("甲", "辛") == "正官"
    
    def test_generates_me_same_yinyang(self):
        """生我同阴阳 = 偏印."""
        # 壬水生甲木（同阳）
        assert get_ten_god("甲", "壬") == "偏印"
    
    def test_generates_me_diff_yinyang(self):
        """生我异阴阳 = 正印."""
        # 癸水生甲木（阴生阳）
        assert get_ten_god("甲", "癸") == "正印"
    
    def test_all_ten_gods_covered(self):
        """测试甲日主对应的十神完整性."""
        day_master = "甲"
        ten_gods_found = set()
        
        for stem in HEAVENLY_STEMS:
            god = get_ten_god(day_master, stem)
            ten_gods_found.add(god)
        
        # 应该覆盖所有十神
        assert ten_gods_found == set(TEN_GOD_NAMES)


class TestAnalyzeTenGods:
    """四柱十神分析测试."""
    
    def test_basic_analysis(self):
        """基础分析测试."""
        four_pillars = FourPillars(
            year=Pillar(stem="庚", branch="午"),
            month=Pillar(stem="辛", branch="巳"),
            day=Pillar(stem="甲", branch="子"),
            hour=Pillar(stem="丙", branch="寅"),
        )
        
        ten_gods, counts = analyze_ten_gods(four_pillars)
        
        # 应该有十神列表
        assert len(ten_gods) > 0
        
        # 年干庚相对甲日主是七杀
        year_stem_god = next(tg for tg in ten_gods 
                            if tg.pillar == "year" and not tg.is_hidden)
        assert year_stem_god.name == "七杀"
        
        # 月干辛相对甲日主是正官
        month_stem_god = next(tg for tg in ten_gods 
                             if tg.pillar == "month" and not tg.is_hidden)
        assert month_stem_god.name == "正官"
        
        # 时干丙相对甲日主是食神
        hour_stem_god = next(tg for tg in ten_gods 
                            if tg.pillar == "hour" and not tg.is_hidden)
        assert hour_stem_god.name == "食神"
    
    def test_counts_structure(self):
        """测试十神统计结构."""
        four_pillars = FourPillars(
            year=Pillar(stem="庚", branch="午"),
            month=Pillar(stem="辛", branch="巳"),
            day=Pillar(stem="甲", branch="子"),
            hour=Pillar(stem="丙", branch="寅"),
        )
        
        _, counts = analyze_ten_gods(four_pillars)
        
        # 所有十神都应该有计数
        for god_name in TEN_GOD_NAMES:
            assert god_name in counts
            assert counts[god_name] >= 0
