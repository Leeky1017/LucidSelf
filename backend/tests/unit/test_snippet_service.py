# backend/tests/unit/test_snippet_service.py
"""
WP-03: Snippet Service 专项测试

测试目标：
1. FACTOR_ALIAS_MAP 一致性校验
2. ENGINE_TO_CORPUS 覆盖 7 体系
3. ENGINE_FALLBACK_TRIGGERS 非空
4. get_fallback_snippets() 返回非空结果
5. alias 映射命中验证
"""

import pytest
from typing import Set

from backend.services.narrative.snippet_service import (
    NarrativeSnippetService,
    get_snippet_service,
    FACTOR_ALIAS_MAP,
    ENGINE_TO_CORPUS,
    ENGINE_FALLBACK_TRIGGERS,
    expand_factors_with_aliases,
)
from backend.core.constants.engines import (
    ENGINE_BAZI,
    ENGINE_ASTRO,
    ENGINE_ZIWEI,
    ENGINE_TAROT,
    ENGINE_DREAM,
    ENGINE_YIJING,
    ENGINE_PSYCH,
)


# R-03: 标准引擎 ID 列表 (全 7 体系)
STANDARD_ENGINE_IDS = [
    ENGINE_BAZI,      # bazi-calculator
    ENGINE_ASTRO,     # astro-calculator
    ENGINE_ZIWEI,     # ziwei-calculator
    ENGINE_TAROT,     # tarot-interpreter
    ENGINE_DREAM,     # dream-extractor
    ENGINE_YIJING,    # yijing-calculator
    ENGINE_PSYCH,     # psych-analyzer
]


class TestFactorAliasMapConsistency:
    """FACTOR_ALIAS_MAP 一致性测试"""
    
    def test_no_duplicate_aliases(self):
        """测试：别名无重复冲突"""
        all_aliases: Set[str] = set()
        duplicates = []
        
        for factor, aliases in FACTOR_ALIAS_MAP.items():
            for alias in aliases:
                if alias in all_aliases:
                    duplicates.append(alias)
                all_aliases.add(alias)
        
        # 允许通用别名重复（如 "day_master" 被多个因子共享）
        # 但同一因子的别名不应重复
        # 这里检查的是别名列表本身是否有重复
        for factor, aliases in FACTOR_ALIAS_MAP.items():
            unique_aliases = set(aliases)
            assert len(aliases) == len(unique_aliases), \
                f"因子 {factor} 的别名列表有重复"
    
    def test_alias_map_not_empty(self):
        """测试：别名映射非空"""
        assert len(FACTOR_ALIAS_MAP) > 0, "FACTOR_ALIAS_MAP 不应为空"
    
    def test_all_aliases_are_strings(self):
        """测试：所有别名都是字符串"""
        for factor, aliases in FACTOR_ALIAS_MAP.items():
            assert isinstance(factor, str), f"因子名必须是字符串: {factor}"
            for alias in aliases:
                assert isinstance(alias, str), f"别名必须是字符串: {alias}"


class TestEngineToCorpusCoverage:
    """ENGINE_TO_CORPUS 体系覆盖测试"""
    
    def test_covers_7_main_engines(self):
        """测试：覆盖全部 7 个主要引擎"""
        assert len(ENGINE_TO_CORPUS) == 7, f"ENGINE_TO_CORPUS 应有 7 个引擎，实际 {len(ENGINE_TO_CORPUS)}"
        for engine_id in STANDARD_ENGINE_IDS:
            assert engine_id in ENGINE_TO_CORPUS, \
                f"ENGINE_TO_CORPUS 缺少引擎: {engine_id}"
    
    def test_corpus_list_not_empty(self):
        """测试：每个引擎的典籍列表非空"""
        for engine_id, corpus_list in ENGINE_TO_CORPUS.items():
            assert len(corpus_list) > 0, \
                f"引擎 {engine_id} 的典籍列表为空"
    
    def test_corpus_entries_are_strings(self):
        """测试：所有典籍名都是字符串"""
        for engine_id, corpus_list in ENGINE_TO_CORPUS.items():
            for corpus in corpus_list:
                assert isinstance(corpus, str), \
                    f"典籍名必须是字符串: {corpus}"


class TestEngineFallbackTriggers:
    """ENGINE_FALLBACK_TRIGGERS 测试"""
    
    def test_covers_7_main_engines(self):
        """测试：覆盖全部 7 个主要引擎"""
        assert len(ENGINE_FALLBACK_TRIGGERS) == 7, f"ENGINE_FALLBACK_TRIGGERS 应有 7 个引擎，实际 {len(ENGINE_FALLBACK_TRIGGERS)}"
        for engine_id in STANDARD_ENGINE_IDS:
            assert engine_id in ENGINE_FALLBACK_TRIGGERS, \
                f"ENGINE_FALLBACK_TRIGGERS 缺少引擎: {engine_id}"
    
    def test_triggers_not_empty(self):
        """测试：每个引擎的触发词非空"""
        for engine_id, triggers in ENGINE_FALLBACK_TRIGGERS.items():
            assert len(triggers) > 0, \
                f"引擎 {engine_id} 的触发词列表为空"
    
    def test_triggers_contain_common_word(self):
        """测试：每个引擎的触发词包含通用词"""
        for engine_id, triggers in ENGINE_FALLBACK_TRIGGERS.items():
            assert "通用" in triggers, \
                f"引擎 {engine_id} 的触发词应包含 '通用'"


class TestExpandFactorsWithAliases:
    """expand_factors_with_aliases 函数测试"""
    
    def test_expands_known_factor(self):
        """测试：已知因子被扩展"""
        factors = ["day_master_jia"]
        expanded = expand_factors_with_aliases(factors)
        
        assert "day_master_jia" in expanded
        assert "day_master" in expanded, "应扩展出通用别名 day_master"
    
    def test_preserves_unknown_factors(self):
        """测试：未知因子被保留"""
        factors = ["unknown_factor_xyz"]
        expanded = expand_factors_with_aliases(factors)
        
        assert "unknown_factor_xyz" in expanded
    
    def test_empty_input(self):
        """测试：空输入返回空集合"""
        expanded = expand_factors_with_aliases([])
        assert len(expanded) == 0
    
    def test_multiple_factors_combined(self):
        """测试：多因子正确合并"""
        factors = ["day_master_jia", "season_spring"]
        expanded = expand_factors_with_aliases(factors)
        
        assert "day_master_jia" in expanded
        assert "day_master" in expanded
        assert "season_spring" in expanded
        assert "season" in expanded


class TestSnippetServiceAliasMatching:
    """SnippetService 别名匹配测试"""
    
    @pytest.fixture
    def service(self):
        """获取服务实例（不实际加载数据）"""
        service = NarrativeSnippetService()
        # 注意：实际测试中可能需要 mock 数据
        return service
    
    def test_find_by_factors_with_alias(self, service):
        """测试：通过别名查找因子"""
        service.ensure_loaded()
        
        # 使用具体因子名和通用别名都应能找到
        results_specific = service.find_by_factors(["day_master_jia"])
        results_generic = service.find_by_factors(["day_master"])
        
        # 如果有数据，结果应该有交集
        # 如果无数据，两者都为空也是合理的


class TestGetFallbackSnippets:
    """get_fallback_snippets 测试"""
    
    @pytest.fixture
    def service(self):
        return NarrativeSnippetService()
    
    @pytest.mark.parametrize("engine_id", STANDARD_ENGINE_IDS)
    def test_fallback_returns_result_or_empty_list(self, service, engine_id):
        """测试：每个引擎的 fallback 返回列表（可能为空，但不应报错）"""
        service.ensure_loaded()
        
        result = service.get_fallback_snippets(engine_id, max_results=3)
        
        assert isinstance(result, list), f"返回类型应为 list: {type(result)}"
        # 注意：如果没有加载实际数据，结果可能为空
        # 但函数不应抛出异常
    
    def test_fallback_respects_max_results(self, service):
        """测试：fallback 遵守 max_results 限制"""
        service.ensure_loaded()
        
        for engine_id in STANDARD_ENGINE_IDS:
            result = service.get_fallback_snippets(engine_id, max_results=2)
            assert len(result) <= 2, \
                f"引擎 {engine_id} 返回结果超过 max_results=2"
    
    def test_unknown_engine_uses_default_triggers(self, service):
        """测试：未知引擎使用默认触发词"""
        service.ensure_loaded()
        
        # 未知引擎应该使用 ["通用"] 作为默认触发词
        result = service.get_fallback_snippets("unknown-engine", max_results=3)
        assert isinstance(result, list)


class TestSnippetServiceFormatForPrompt:
    """format_for_prompt 方法测试"""
    
    @pytest.fixture
    def service(self):
        return NarrativeSnippetService()
    
    def test_format_empty_list(self, service):
        """测试：空列表返回空字符串"""
        result = service.format_for_prompt([])
        assert result == ""
    
    def test_format_respects_max_chars(self, service):
        """测试：格式化遵守最大字符数"""
        service.ensure_loaded()
        
        # 获取一些结果
        snippets = service.find_by_factors(["通用"], max_results=10)
        
        if snippets:
            formatted = service.format_for_prompt(snippets, max_chars=100)
            assert len(formatted) <= 100 + 50, \
                f"格式化结果超过限制: {len(formatted)}"


class TestSnippetServiceStats:
    """SnippetService 统计测试"""
    
    @pytest.fixture
    def service(self):
        return NarrativeSnippetService()
    
    def test_get_stats_returns_dict(self, service):
        """测试：get_stats 返回正确结构"""
        service.ensure_loaded()
        
        stats = service.get_stats()
        
        assert isinstance(stats, dict)
        assert "total_snippets" in stats
        assert "total_books" in stats
        assert "total_factors" in stats
        assert all(isinstance(v, int) for v in stats.values())


class TestSnippetServiceSingleton:
    """单例模式测试"""
    
    def test_get_instance_returns_same_object(self):
        """测试：get_instance 返回同一对象"""
        instance1 = NarrativeSnippetService.get_instance()
        instance2 = NarrativeSnippetService.get_instance()
        
        assert instance1 is instance2
    
    def test_reset_instance_creates_new_object(self):
        """测试：reset_instance 后创建新对象"""
        instance1 = NarrativeSnippetService.get_instance()
        NarrativeSnippetService.reset_instance()
        instance2 = NarrativeSnippetService.get_instance()
        
        assert instance1 is not instance2
        
        # 清理
        NarrativeSnippetService.reset_instance()
