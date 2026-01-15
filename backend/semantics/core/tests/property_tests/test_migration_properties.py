"""
Migration Property Tests

属性测试 - 迁移工具正确性
对齐 tasks.md 1.7~1.9, 3.7, 23.2~23.6

Properties:
- Property 1: Migration Completeness
- Property 4: Engine-Specific Factor Prefixes
- Property 5: Incremental Compilation Consistency
- Property 6: Dry-Run No Side Effects
- Property 7: Source Path to Language Mapping
- Property 8: Engine ID Inference Correctness
- Property 15: Migration Success Rate
"""

from pathlib import Path
from typing import List

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from scripts.codegen.engine_mapping import (
    ENGINE_BOOK_MAPPING,
    FACTOR_ID_PREFIXES,
    SOURCE_PATH_MAPPING,
    TOTAL_BOOKS,
    VALID_ENGINE_IDS,
    get_all_book_ids,
    infer_engine_id,
    infer_primary_lang,
    validate_factor_prefix,
)


# -----------------------------------------------------------------------------
# Hypothesis Strategies
# -----------------------------------------------------------------------------

# 从 SOURCE_PATH_MAPPING 采样有效的 book_id
valid_book_id = st.sampled_from(list(SOURCE_PATH_MAPPING.keys()))

# 从 ENGINE_BOOK_MAPPING 采样有效的 engine_id
valid_engine_id = st.sampled_from(VALID_ENGINE_IDS)


# -----------------------------------------------------------------------------
# Property 6: Dry-Run No Side Effects
# **Feature: semantic-layer-phase2, Property 6: Dry-Run No Side Effects**
# **Validates: Requirements 8.4**
# -----------------------------------------------------------------------------

class TestDryRunNoSideEffects:
    """Property 6: dry-run 模式不应产生副作用"""
    
    @given(book_id=valid_book_id)
    @settings(max_examples=10)
    def test_dry_run_does_not_create_files(self, book_id: str):
        """
        **Feature: semantic-layer-phase2, Property 6: Dry-Run No Side Effects**
        
        dry-run 模式下不应创建新文件
        """
        from scripts.codegen.semantic_generator import SemanticMigrationTool
        
        output_dir = Path("backend/semantics") / book_id
        
        # 记录执行前的文件状态
        files_before = set()
        if output_dir.exists():
            files_before = set(f.name for f in output_dir.glob("*.py"))
        
        # 执行 dry-run
        tool = SemanticMigrationTool()
        result = tool.migrate_book(book_id, dry_run=True)
        
        # 验证文件状态未变
        files_after = set()
        if output_dir.exists():
            files_after = set(f.name for f in output_dir.glob("*.py"))
        
        # dry-run 不应创建新文件
        new_files = files_after - files_before
        assert len(new_files) == 0, f"dry-run created files: {new_files}"


# -----------------------------------------------------------------------------
# Property 7: Source Path to Language Mapping
# **Feature: semantic-layer-phase2, Property 7: Source Path to Language Mapping**
# **Validates: Requirements 8.6**
# -----------------------------------------------------------------------------

class TestSourcePathToLanguageMapping:
    """Property 7: 源路径到语言映射"""
    
    @given(book_id=valid_book_id)
    @settings(max_examples=50)
    def test_infer_primary_lang_correctness(self, book_id: str):
        """
        **Feature: semantic-layer-phase2, Property 7: Source Path to Language Mapping**
        
        若 SOURCE_PATH_MAPPING[book_id] 包含 "中文典籍"，返回 "zh-CN"；否则返回 "en-US"
        """
        result = infer_primary_lang(book_id)
        source_path = SOURCE_PATH_MAPPING.get(book_id, "")
        
        if "中文典籍" in source_path:
            assert result == "zh-CN", f"{book_id}: expected zh-CN, got {result}"
        else:
            assert result == "en-US", f"{book_id}: expected en-US, got {result}"
    
    def test_chinese_books_have_zh_cn(self):
        """中文典籍应该返回 zh-CN"""
        chinese_books = ["dts", "sanming", "ziwei", "mlxj", "zhougong", "zhouyi"]
        for book_id in chinese_books:
            if book_id in SOURCE_PATH_MAPPING:
                assert infer_primary_lang(book_id) == "zh-CN"
    
    def test_english_books_have_en_us(self):
        """英文典籍应该返回 en-US"""
        english_books = ["waite_tarot", "the_inner_sky", "archetypes_unconscious"]
        for book_id in english_books:
            if book_id in SOURCE_PATH_MAPPING:
                assert infer_primary_lang(book_id) == "en-US"


# -----------------------------------------------------------------------------
# Property 8: Engine ID Inference Correctness
# **Feature: semantic-layer-phase2, Property 8: Engine ID Inference Correctness**
# **Validates: Requirements 8.7**
# -----------------------------------------------------------------------------

class TestEngineIDInference:
    """Property 8: engine_id 推断正确性"""
    
    @given(book_id=valid_book_id)
    @settings(max_examples=50)
    def test_infer_engine_id_correctness(self, book_id: str):
        """
        **Feature: semantic-layer-phase2, Property 8: Engine ID Inference Correctness**
        
        infer_engine_id(book_id) 返回值应与 ENGINE_BOOK_MAPPING 中该 book_id 所属的 engine_id 一致
        """
        result = infer_engine_id(book_id)
        
        # 找到预期的 engine_id
        expected = None
        for engine_id, books in ENGINE_BOOK_MAPPING.items():
            if book_id in books:
                expected = engine_id
                break
        
        if expected:
            assert result == expected, f"{book_id}: expected {expected}, got {result}"
    
    def test_all_books_have_valid_engine(self):
        """所有 24 本书籍都应该有有效的 engine_id"""
        all_books = get_all_book_ids()
        assert len(all_books) == TOTAL_BOOKS, f"Expected {TOTAL_BOOKS} books, got {len(all_books)}"
        
        for book_id in all_books:
            engine_id = infer_engine_id(book_id)
            assert engine_id in VALID_ENGINE_IDS, f"{book_id} has invalid engine: {engine_id}"
    
    def test_engine_book_mapping_coverage(self):
        """ENGINE_BOOK_MAPPING 应该覆盖所有 7 个引擎"""
        assert set(ENGINE_BOOK_MAPPING.keys()) == set(VALID_ENGINE_IDS)
        
        # 每个引擎至少有 1 本书
        for engine_id in VALID_ENGINE_IDS:
            assert len(ENGINE_BOOK_MAPPING[engine_id]) >= 1


# -----------------------------------------------------------------------------
# Property 4: Engine-Specific Factor Prefixes
# **Feature: semantic-layer-phase2, Property 4: Engine-Specific Factor Prefixes**
# **Validates: Requirements 1.7, 2.3, 3.3, 4.3, 5.3, 6.3, 7.3**
# -----------------------------------------------------------------------------

class TestEngineSpecificFactorPrefixes:
    """Property 4: 引擎特定因子前缀"""
    
    def test_bazi_factor_prefixes(self):
        """
        **Feature: semantic-layer-phase2, Property 4: Engine-Specific Factor Prefixes (bazi)**
        
        bazi 因子应该使用正确的前缀
        """
        valid_factors = [
            "day_master_jia", "day_master_yi",
            "season_spring", "season_summer",
            "ten_god_zhengguan", "ten_god_qisha",
            "strength_strong", "strength_weak",
            "element_wood", "element_fire",
            "stem_jia", "stem_yi",
            "branch_zi", "branch_chou",
        ]
        
        for factor_id in valid_factors:
            assert validate_factor_prefix(factor_id, "bazi"), f"{factor_id} should be valid for bazi"
    
    def test_ziwei_factor_prefixes(self):
        """
        **Feature: semantic-layer-phase2, Property 4: Engine-Specific Factor Prefixes (ziwei)**
        
        ziwei 因子应该使用正确的前缀
        """
        valid_factors = [
            "ziwei_star_ziwei", "ziwei_star_tianji",
            "ziwei_palace_ming", "ziwei_palace_xiongdi",
            "ziwei_transform_lu", "ziwei_transform_quan",
            "ziwei_aux_zuofu", "ziwei_aux_youbi",
        ]
        
        for factor_id in valid_factors:
            assert validate_factor_prefix(factor_id, "ziwei"), f"{factor_id} should be valid for ziwei"
    
    def test_tarot_factor_prefixes(self):
        """
        **Feature: semantic-layer-phase2, Property 4: Engine-Specific Factor Prefixes (tarot)**
        
        tarot 因子应该使用正确的前缀
        """
        valid_factors = [
            "tarot_major_the_fool", "tarot_major_the_magician",
            "tarot_wands_ace", "tarot_cups_ace",
            "suit_wands", "suit_cups",
            "orientation_upright", "orientation_reversed",
        ]
        
        for factor_id in valid_factors:
            assert validate_factor_prefix(factor_id, "tarot"), f"{factor_id} should be valid for tarot"
    
    def test_astro_factor_prefixes(self):
        """
        **Feature: semantic-layer-phase2, Property 4: Engine-Specific Factor Prefixes (astro)**
        
        astro 因子应该使用正确的前缀
        """
        valid_factors = [
            "astro_planet_sun", "astro_planet_moon",
            "astro_sign_aries", "astro_sign_taurus",
            "astro_house_1", "astro_house_12",
            "astro_aspect_conjunction", "astro_aspect_trine",
        ]
        
        for factor_id in valid_factors:
            assert validate_factor_prefix(factor_id, "astro"), f"{factor_id} should be valid for astro"
    
    def test_dream_factor_prefixes(self):
        """
        **Feature: semantic-layer-phase2, Property 4: Engine-Specific Factor Prefixes (dream)**
        
        dream 因子应该使用正确的前缀
        """
        valid_factors = [
            "dream_symbol_animal", "dream_symbol_water",
            "dream_theme_chase", "dream_theme_falling",
            "dream_emotion_fear", "dream_emotion_joy",
        ]
        
        for factor_id in valid_factors:
            assert validate_factor_prefix(factor_id, "dream"), f"{factor_id} should be valid for dream"
    
    def test_yijing_factor_prefixes(self):
        """
        **Feature: semantic-layer-phase2, Property 4: Engine-Specific Factor Prefixes (yijing)**
        
        yijing 因子应该使用正确的前缀
        """
        valid_factors = [
            "yijing_gua_qian", "yijing_gua_kun",
            "yijing_yao_1", "yijing_yao_6",
            "yijing_upper_trigram", "yijing_lower_trigram",
        ]
        
        for factor_id in valid_factors:
            assert validate_factor_prefix(factor_id, "yijing"), f"{factor_id} should be valid for yijing"
    
    def test_psych_factor_prefixes(self):
        """
        **Feature: semantic-layer-phase2, Property 4: Engine-Specific Factor Prefixes (psych)**
        
        psych 因子应该使用正确的前缀
        """
        valid_factors = [
            "psych_archetype_shadow", "psych_archetype_anima",
            "psych_function_thinking", "psych_function_feeling",
            "psych_attitude_introvert", "psych_attitude_extravert",
            "psych_process_individuation",
        ]
        
        for factor_id in valid_factors:
            assert validate_factor_prefix(factor_id, "psych"), f"{factor_id} should be valid for psych"


# -----------------------------------------------------------------------------
# Property 1: Migration Completeness
# **Feature: semantic-layer-phase2, Property 1: Migration Completeness**
# **Validates: Requirements 1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1**
# -----------------------------------------------------------------------------

class TestMigrationCompleteness:
    """Property 1: 迁移完整性"""
    
    def test_all_engines_have_books_mapped(self):
        """
        **Feature: semantic-layer-phase2, Property 1: Migration Completeness**
        
        所有 7 个引擎都应该有书籍映射
        """
        for engine_id in VALID_ENGINE_IDS:
            assert engine_id in ENGINE_BOOK_MAPPING
            assert len(ENGINE_BOOK_MAPPING[engine_id]) > 0
    
    def test_total_books_count(self):
        """
        **Feature: semantic-layer-phase2, Property 1: Migration Completeness**
        
        总共应该有 24 本书籍
        """
        total = sum(len(books) for books in ENGINE_BOOK_MAPPING.values())
        assert total == 24, f"Expected 24 books, got {total}"
    
    def test_all_books_have_source_path(self):
        """
        **Feature: semantic-layer-phase2, Property 1: Migration Completeness**
        
        所有书籍都应该有源路径映射
        """
        for engine_id, books in ENGINE_BOOK_MAPPING.items():
            for book_id in books:
                assert book_id in SOURCE_PATH_MAPPING, f"{book_id} missing from SOURCE_PATH_MAPPING"


# -----------------------------------------------------------------------------
# Property 5: Incremental Compilation Consistency
# **Feature: semantic-layer-phase2, Property 5: Incremental Compilation Consistency**
# **Validates: Requirements 8.2**
# -----------------------------------------------------------------------------

class TestIncrementalCompilation:
    """Property 5: 增量编译一致性"""
    
    def test_hash_consistency(self):
        """
        **Feature: semantic-layer-phase2, Property 5: Incremental Compilation Consistency**
        
        相同内容的哈希应该一致
        """
        from scripts.codegen.semantic_generator import SemanticCodeGenerator
        
        gen = SemanticCodeGenerator()
        content = "test content for hashing"
        
        hash1 = gen._compute_hash(content)
        hash2 = gen._compute_hash(content)
        
        assert hash1 == hash2, "Same content should have same hash"
    
    def test_different_content_different_hash(self):
        """
        **Feature: semantic-layer-phase2, Property 5: Incremental Compilation Consistency**
        
        不同内容的哈希应该不同
        """
        from scripts.codegen.semantic_generator import SemanticCodeGenerator
        
        gen = SemanticCodeGenerator()
        content1 = "content version 1"
        content2 = "content version 2"
        
        hash1 = gen._compute_hash(content1)
        hash2 = gen._compute_hash(content2)
        
        assert hash1 != hash2, "Different content should have different hash"


# -----------------------------------------------------------------------------
# Property 15: Migration Success Rate
# **Feature: semantic-layer-phase2, Property 15: Migration Success Rate**
# **Validates: Requirements 1.8, 2.5, 3.6, 4.6, 5.6, 6.6, 7.7, 9.5**
# -----------------------------------------------------------------------------

class TestMigrationSuccessRate:
    """Property 15: 迁移成功率"""
    
    def test_success_rate_calculation(self):
        """
        **Feature: semantic-layer-phase2, Property 15: Migration Success Rate**
        
        成功率计算应该正确
        """
        from scripts.codegen.models import MigrationResult, MigrationStatus
        
        result = MigrationResult(
            book_id="test",
            engine_id="bazi",
            status=MigrationStatus.PARTIAL,
            entries_total=100,
            entries_success=95,
            entries_failed=5,
        )
        
        assert result.success_rate == 0.95
    
    def test_zero_entries_success_rate(self):
        """
        **Feature: semantic-layer-phase2, Property 15: Migration Success Rate**
        
        零条目时成功率应该为 0
        """
        from scripts.codegen.models import MigrationResult, MigrationStatus
        
        result = MigrationResult(
            book_id="test",
            engine_id="bazi",
            status=MigrationStatus.SKIPPED,
            entries_total=0,
            entries_success=0,
            entries_failed=0,
        )
        
        assert result.success_rate == 0.0
