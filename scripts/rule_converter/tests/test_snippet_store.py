"""
Tests for SnippetStore

Requirement Refs: Req 2.1-2.10
"""

import tempfile
from pathlib import Path

import pytest

from scripts.rule_converter.loaders.snippet_store import Snippet, SnippetStore


class TestSnippet:
    """测试 Snippet 数据类"""
    
    def test_create_snippet(self):
        """测试创建 Snippet"""
        snippet = Snippet(
            snippet_id="ns_dts_001",
            trigger="论命起手",
            factor_trigger="dizai_shengong",
            role="主干",
            content="欲断命先观月令",
            source_ref="《滴天髓·通天论》#第1条",
        )
        
        assert snippet.snippet_id == "ns_dts_001"
        assert snippet.trigger == "论命起手"
        assert snippet.factor_trigger == "dizai_shengong"
        assert snippet.role == "主干"
        assert snippet.content == "欲断命先观月令"
        assert snippet.source_ref == "《滴天髓·通天论》#第1条"


class TestSnippetStore:
    """测试 SnippetStore"""
    
    @pytest.fixture
    def sample_md_content(self):
        """示例精校文档内容"""
        return """# 测试文档

## 第一章

<!-- L1_BEGIN -->

- 叙事素材（L1）：
  - `[ns_test_001]` `[trigger: 测试触发]` `[factor_trigger: test_factor]` `[role: 主干]` 这是测试内容1 → 《测试书》#第1章
  - `[ns_test_002]` `[trigger: 另一个触发]` `[factor_trigger: another_factor]` `[role: 条件分支]` 这是测试内容2 → 《测试书》#第2章

<!-- L1_END -->

## 第二章

<!-- L1_BEGIN -->

  - `[ns_test_003]` `[trigger: 第三个]` `[factor_trigger: third_factor]` `[role: 总结]` 这是测试内容3 → 《测试书》#第3章

<!-- L1_END -->
"""
    
    @pytest.fixture
    def legacy_md_content(self):
        """旧格式精校文档内容（没有 factor_trigger）"""
        return """# 旧格式文档

<!-- L1_BEGIN -->

  - `[ns_old_001]` `[trigger: 旧触发]` `[role: 主干]` 旧格式内容 → 《旧书》#第1章

<!-- L1_END -->
"""
    
    @pytest.fixture
    def temp_dir(self):
        """创建临时目录"""
        with tempfile.TemporaryDirectory() as tmpdir:
            yield Path(tmpdir)
    
    def _create_book_structure(self, temp_dir: Path, book_name: str, content: str):
        """创建书籍目录结构"""
        book_dir = temp_dir / book_name / "编辑"
        book_dir.mkdir(parents=True)
        
        md_file = book_dir / f"{book_name}_完整规范化.md"
        md_file.write_text(content, encoding="utf-8")
        return md_file
    
    def test_load_from_dir(self, temp_dir, sample_md_content):
        """测试从目录加载"""
        self._create_book_structure(temp_dir, "测试书", sample_md_content)
        
        store = SnippetStore(temp_dir, lazy_load=False)
        store.load_from_dir()
        
        assert len(store) == 3
        
        # 验证统计
        stats = store.stats
        assert stats["total_snippets"] == 3
        assert stats["snippets_with_factor_trigger"] == 3
    
    def test_get_snippet(self, temp_dir, sample_md_content):
        """测试获取单个叙事素材"""
        self._create_book_structure(temp_dir, "测试书", sample_md_content)
        
        store = SnippetStore(temp_dir, lazy_load=False)
        store.load_from_dir()
        
        snippet = store.get("ns_test_001")
        assert snippet is not None
        assert snippet.snippet_id == "ns_test_001"
        assert snippet.trigger == "测试触发"
        assert snippet.factor_trigger == "test_factor"
        assert snippet.role == "主干"
        assert "测试内容1" in snippet.content
        assert "《测试书》" in snippet.source_ref
    
    def test_get_nonexistent(self, temp_dir, sample_md_content):
        """测试获取不存在的叙事素材"""
        self._create_book_structure(temp_dir, "测试书", sample_md_content)
        
        store = SnippetStore(temp_dir, lazy_load=False)
        store.load_from_dir()
        
        snippet = store.get("nonexistent")
        assert snippet is None
    
    def test_get_batch(self, temp_dir, sample_md_content):
        """测试批量获取"""
        self._create_book_structure(temp_dir, "测试书", sample_md_content)
        
        store = SnippetStore(temp_dir, lazy_load=False)
        store.load_from_dir()
        
        snippets = store.get_batch(["ns_test_001", "ns_test_002", "nonexistent"])
        assert len(snippets) == 2
        assert snippets[0].snippet_id == "ns_test_001"
        assert snippets[1].snippet_id == "ns_test_002"
    
    def test_has(self, temp_dir, sample_md_content):
        """测试检查存在性"""
        self._create_book_structure(temp_dir, "测试书", sample_md_content)
        
        store = SnippetStore(temp_dir, lazy_load=False)
        store.load_from_dir()
        
        assert store.has("ns_test_001") is True
        assert store.has("nonexistent") is False
        assert "ns_test_001" in store
    
    def test_get_by_book(self, temp_dir, sample_md_content):
        """测试按书籍获取"""
        self._create_book_structure(temp_dir, "测试书", sample_md_content)
        
        store = SnippetStore(temp_dir, lazy_load=False)
        store.load_from_dir()
        
        snippets = store.get_by_book("测试书")
        assert len(snippets) == 3
    
    def test_snippets_by_book(self, temp_dir, sample_md_content):
        """测试统计每本书的数量"""
        self._create_book_structure(temp_dir, "测试书", sample_md_content)
        
        store = SnippetStore(temp_dir, lazy_load=False)
        store.load_from_dir()
        
        by_book = store.snippets_by_book
        assert "测试书" in by_book
        assert by_book["测试书"] == 3
    
    def test_legacy_format(self, temp_dir, legacy_md_content):
        """测试解析旧格式（没有 factor_trigger）"""
        self._create_book_structure(temp_dir, "旧书", legacy_md_content)
        
        store = SnippetStore(temp_dir, lazy_load=False)
        store.load_from_dir()
        
        assert len(store) == 1
        
        snippet = store.get("ns_old_001")
        assert snippet is not None
        assert snippet.trigger == "旧触发"
        assert snippet.factor_trigger == ""  # 旧格式没有
        assert snippet.role == "主干"
    
    def test_lazy_load(self, temp_dir, sample_md_content):
        """测试懒加载"""
        self._create_book_structure(temp_dir, "测试书", sample_md_content)
        
        store = SnippetStore(temp_dir, lazy_load=True)
        
        # 访问时应该自动加载
        snippet = store.get("ns_test_001")
        assert snippet is not None
    
    def test_multiple_books(self, temp_dir, sample_md_content, legacy_md_content):
        """测试多本书"""
        self._create_book_structure(temp_dir, "测试书", sample_md_content)
        self._create_book_structure(temp_dir, "旧书", legacy_md_content)
        
        store = SnippetStore(temp_dir, lazy_load=False)
        store.load_from_dir()
        
        assert len(store) == 4
        
        by_book = store.snippets_by_book
        assert by_book["测试书"] == 3
        assert by_book["旧书"] == 1


class TestSnippetStoreIntegration:
    """集成测试：使用实际的精校文档"""
    
    @pytest.mark.skipif(
        not Path("典籍/中文典籍").exists(),
        reason="需要实际的精校文档数据"
    )
    def test_load_real_data(self):
        """测试加载实际数据"""
        store = SnippetStore(lazy_load=False)
        store.load_from_dir()
        
        stats = store.stats
        print(f"\n=== SnippetStore 加载统计 ===")
        print(f"总文件数: {stats['total_files']}")
        print(f"解析成功: {stats['parsed_files']}")
        print(f"解析失败: {stats['failed_files']}")
        print(f"总叙事素材数: {stats['total_snippets']}")
        print(f"有factor_trigger的: {stats['snippets_with_factor_trigger']}")
        
        print(f"\n按书籍统计:")
        for book, count in sorted(store.snippets_by_book.items()):
            print(f"  {book}: {count}")
        
        # 验证加载成功
        assert stats["total_snippets"] > 0
