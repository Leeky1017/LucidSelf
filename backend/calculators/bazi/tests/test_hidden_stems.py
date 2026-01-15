# backend/calculators/bazi/tests/test_hidden_stems.py
"""
Unit tests for hidden stems module.
"""

import pytest

from backend.calculators.bazi.hidden_stems import (
    extract_hidden_stems,
    get_main_hidden_stem,
    get_hidden_stem_weight,
    HIDDEN_STEM_MAP,
)
from backend.calculators.bazi.models import HiddenStem, EARTHLY_BRANCHES


class TestExtractHiddenStems:
    """藏干提取测试."""
    
    def test_single_hidden_stem(self):
        """测试单藏：子(癸)、卯(乙)、酉(辛)."""
        # 子
        result = extract_hidden_stems("子")
        assert len(result) == 1
        assert result[0].stem == "癸"
        assert result[0].weight == 1.0
        assert result[0].role == "main"
        
        # 卯
        result = extract_hidden_stems("卯")
        assert len(result) == 1
        assert result[0].stem == "乙"
        
        # 酉
        result = extract_hidden_stems("酉")
        assert len(result) == 1
        assert result[0].stem == "辛"
    
    def test_double_hidden_stem(self):
        """测试双藏：午、亥."""
        # 午
        result = extract_hidden_stems("午")
        assert len(result) == 2
        assert result[0].stem == "丁"
        assert result[0].weight == 0.7
        assert result[1].stem == "己"
        assert result[1].weight == 0.3
        
        # 亥
        result = extract_hidden_stems("亥")
        assert len(result) == 2
        assert result[0].stem == "壬"
        assert result[1].stem == "甲"
    
    def test_triple_hidden_stem(self):
        """测试三藏：丑、寅、辰、巳、未、申、戌."""
        # 寅
        result = extract_hidden_stems("寅")
        assert len(result) == 3
        assert result[0].stem == "甲"  # 本气
        assert result[0].role == "main"
        assert result[1].stem == "丙"  # 中气
        assert result[1].role == "middle"
        assert result[2].stem == "戊"  # 余气
        assert result[2].role == "residual"
        
        # 权重之和应该接近1
        total_weight = sum(hs.weight for hs in result)
        assert 0.99 <= total_weight <= 1.01
    
    def test_all_branches_have_hidden_stems(self):
        """测试所有地支都有藏干定义."""
        for branch in EARTHLY_BRANCHES:
            result = extract_hidden_stems(branch)
            assert len(result) >= 1
            assert all(isinstance(hs, HiddenStem) for hs in result)
    
    def test_invalid_branch(self):
        """测试无效地支."""
        with pytest.raises(ValueError, match="Invalid earthly branch"):
            extract_hidden_stems("X")


class TestGetMainHiddenStem:
    """获取本气测试."""
    
    def test_main_hidden_stems(self):
        """测试各地支本气."""
        cases = {
            "子": "癸", "丑": "己", "寅": "甲", "卯": "乙",
            "辰": "戊", "巳": "丙", "午": "丁", "未": "己",
            "申": "庚", "酉": "辛", "戌": "戊", "亥": "壬",
        }
        
        for branch, expected_main in cases.items():
            assert get_main_hidden_stem(branch) == expected_main


class TestGetHiddenStemWeight:
    """获取藏干权重测试."""
    
    def test_existing_hidden_stem(self):
        """测试存在的藏干."""
        # 寅中甲木本气
        assert get_hidden_stem_weight("寅", "甲") == 0.6
        # 寅中丙火中气
        assert get_hidden_stem_weight("寅", "丙") == 0.3
        # 寅中戊土余气
        assert get_hidden_stem_weight("寅", "戊") == 0.1
    
    def test_non_existing_hidden_stem(self):
        """测试不存在的藏干返回0."""
        # 寅中没有癸水
        assert get_hidden_stem_weight("寅", "癸") == 0.0
