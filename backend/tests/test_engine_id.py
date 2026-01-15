# backend/tests/test_engine_id.py
"""
引擎 ID 标准化测试

覆盖 R1.1-R1.4 需求:
- R1.1: 7 个标准 ENGINE_ID 常量
- R1.2: ENGINE_ALIAS_MAP 映射表
- R1.3: normalize_engine_id(str) -> str
- R1.4: normalize_engine_ids(List[str]) -> List[str]
"""

import pytest
from backend.core.constants.engines import (
    normalize_engine_id,
    normalize_engine_ids,
    is_valid_engine_id,
    ENGINE_BAZI,
    ENGINE_ASTRO,
    ENGINE_ZIWEI,
    ENGINE_TAROT,
    ENGINE_DREAM,
    ENGINE_YIJING,
    ENGINE_PSYCH,
    ALL_ENGINE_IDS,
)


class TestEngineConstants:
    """引擎常量定义测试"""
    
    def test_all_7_engines_defined(self):
        """验证全部 7 个引擎 ID 常量存在"""
        assert ENGINE_BAZI == "bazi-calculator"
        assert ENGINE_ASTRO == "astro-calculator"
        assert ENGINE_ZIWEI == "ziwei-calculator"
        assert ENGINE_TAROT == "tarot-interpreter"
        assert ENGINE_DREAM == "dream-extractor"
        assert ENGINE_YIJING == "yijing-calculator"
        assert ENGINE_PSYCH == "psych-analyzer"
    
    def test_all_engine_ids_list(self):
        """验证 ALL_ENGINE_IDS 列表"""
        assert len(ALL_ENGINE_IDS) == 7
        assert ENGINE_BAZI in ALL_ENGINE_IDS
        assert ENGINE_ASTRO in ALL_ENGINE_IDS
        assert ENGINE_ZIWEI in ALL_ENGINE_IDS
        assert ENGINE_TAROT in ALL_ENGINE_IDS
        assert ENGINE_DREAM in ALL_ENGINE_IDS
        assert ENGINE_YIJING in ALL_ENGINE_IDS
        assert ENGINE_PSYCH in ALL_ENGINE_IDS


class TestNormalizeEngineId:
    """引擎 ID 标准化测试"""
    
    @pytest.mark.parametrize("input_id,expected", [
        # 八字各种别名
        ("bazi", "bazi-calculator"),
        ("八字", "bazi-calculator"),
        ("BAZI", "bazi-calculator"),
        ("BaZi", "bazi-calculator"),
        (" bazi ", "bazi-calculator"),
        ("bz", "bazi-calculator"),
        ("bazi-calculator", "bazi-calculator"),
    ])
    def test_bazi_variants(self, input_id, expected):
        """八字各种别名"""
        assert normalize_engine_id(input_id) == expected
    
    @pytest.mark.parametrize("input_id,expected", [
        # 占星各种别名
        ("astro", "astro-calculator"),
        ("astrology", "astro-calculator"),  # 前端使用
        ("星盘", "astro-calculator"),
        ("西占", "astro-calculator"),
        ("as", "astro-calculator"),
        ("astro-calculator", "astro-calculator"),
    ])
    def test_astro_variants(self, input_id, expected):
        """占星各种别名"""
        assert normalize_engine_id(input_id) == expected
    
    @pytest.mark.parametrize("input_id,expected", [
        # 紫微各种别名
        ("ziwei", "ziwei-calculator"),
        ("紫微", "ziwei-calculator"),
        ("zw", "ziwei-calculator"),
    ])
    def test_ziwei_variants(self, input_id, expected):
        """紫微各种别名"""
        assert normalize_engine_id(input_id) == expected
    
    @pytest.mark.parametrize("input_id,expected", [
        # 塔罗各种别名
        ("tarot", "tarot-interpreter"),
        ("塔罗", "tarot-interpreter"),
        ("tr", "tarot-interpreter"),
    ])
    def test_tarot_variants(self, input_id, expected):
        """塔罗各种别名"""
        assert normalize_engine_id(input_id) == expected
    
    @pytest.mark.parametrize("input_id,expected", [
        # 解梦各种别名
        ("dream", "dream-extractor"),
        ("解梦", "dream-extractor"),
        ("dr", "dream-extractor"),
    ])
    def test_dream_variants(self, input_id, expected):
        """解梦各种别名"""
        assert normalize_engine_id(input_id) == expected
    
    @pytest.mark.parametrize("input_id,expected", [
        # 易经各种别名
        ("yijing", "yijing-calculator"),
        ("iching", "yijing-calculator"),  # 前端使用
        ("i ching", "yijing-calculator"),
        ("易经", "yijing-calculator"),
        ("周易", "yijing-calculator"),
        ("yj", "yijing-calculator"),
    ])
    def test_yijing_variants(self, input_id, expected):
        """易经各种别名"""
        assert normalize_engine_id(input_id) == expected
    
    @pytest.mark.parametrize("input_id,expected", [
        # 心理各种别名
        ("psych", "psych-analyzer"),
        ("心理", "psych-analyzer"),
        ("ps", "psych-analyzer"),
    ])
    def test_psych_variants(self, input_id, expected):
        """心理各种别名"""
        assert normalize_engine_id(input_id) == expected
    
    def test_all_7_engines_simple(self):
        """全部 7 个体系简写"""
        assert normalize_engine_id("bazi") == ENGINE_BAZI
        assert normalize_engine_id("astro") == ENGINE_ASTRO
        assert normalize_engine_id("ziwei") == ENGINE_ZIWEI
        assert normalize_engine_id("tarot") == ENGINE_TAROT
        assert normalize_engine_id("dream") == ENGINE_DREAM
        assert normalize_engine_id("yijing") == ENGINE_YIJING
        assert normalize_engine_id("psych") == ENGINE_PSYCH
    
    def test_idempotent(self):
        """幂等性: 标准 ID 再次标准化返回自身"""
        for engine_id in ALL_ENGINE_IDS:
            assert normalize_engine_id(engine_id) == engine_id
    
    def test_unknown_preserved(self):
        """未知 ID 保留原样"""
        assert normalize_engine_id("unknown-engine") == "unknown-engine"
        assert normalize_engine_id("custom") == "custom"
    
    def test_empty_and_none(self):
        """空值处理"""
        assert normalize_engine_id("") == ""
        assert normalize_engine_id(None) is None


class TestNormalizeEngineIds:
    """批量标准化测试"""
    
    def test_normalize_list(self):
        """批量标准化"""
        result = normalize_engine_ids(["bazi", "astro", "紫微"])
        assert result == ["bazi-calculator", "astro-calculator", "ziwei-calculator"]
    
    def test_frontend_engines(self):
        """前端传入的引擎 ID"""
        # 模拟前端 config.ts 中的 engines
        frontend_ids = ["bazi", "ziwei", "tarot", "astrology", "iching"]
        result = normalize_engine_ids(frontend_ids)
        assert "bazi-calculator" in result
        assert "ziwei-calculator" in result
        assert "tarot-interpreter" in result
        assert "astro-calculator" in result
        assert "yijing-calculator" in result
    
    def test_empty_list(self):
        """空列表"""
        assert normalize_engine_ids([]) == []
    
    def test_none_input(self):
        """None 输入"""
        assert normalize_engine_ids(None) is None
    
    def test_mixed_known_unknown(self):
        """混合已知和未知 ID"""
        result = normalize_engine_ids(["bazi", "unknown", "astro"])
        assert result == ["bazi-calculator", "unknown", "astro-calculator"]


class TestIsValidEngineId:
    """引擎 ID 有效性检查测试"""
    
    def test_valid_standard_ids(self):
        """标准 ID 有效"""
        for engine_id in ALL_ENGINE_IDS:
            assert is_valid_engine_id(engine_id) is True
    
    def test_valid_aliases(self):
        """别名有效"""
        assert is_valid_engine_id("bazi") is True
        assert is_valid_engine_id("八字") is True
        assert is_valid_engine_id("astrology") is True
        assert is_valid_engine_id("iching") is True
    
    def test_invalid_ids(self):
        """无效 ID"""
        assert is_valid_engine_id("unknown") is False
        assert is_valid_engine_id("custom-engine") is False
        assert is_valid_engine_id("") is False
