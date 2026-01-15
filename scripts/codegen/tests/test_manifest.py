"""
Tests for CodegenManifest

对照实际 API:
- CodegenManifest(generated_dir: Path)
- add_entry(source_file, output_file, source_hash, output_hash, generator_type, engine_id, version)
- get_entry(source_file) -> ManifestEntry
- needs_recompile(source_file, current_hash) -> bool
- find_orphans() -> List[Path]
- clean_orphans(dry_run=True) -> List[Path]
"""

import hashlib
import json
from datetime import datetime
from pathlib import Path

import pytest

from scripts.codegen.manifest import CodegenManifest, ManifestEntry


def compute_hash(content: str) -> str:
    """计算内容的 SHA256 哈希"""
    return hashlib.sha256(content.encode()).hexdigest()


class TestManifestEntry:
    """ManifestEntry 测试"""
    
    def test_create_entry(self):
        """测试创建清单条目"""
        entry = ManifestEntry(
            source_file="data/rules/test.json",
            output_file="backend/generated/rules/test.py",
            source_hash="abc123",
            output_hash="def456",
            generator_type="rule",
            engine_id="bazi",
            version="1.0.0"
        )
        assert entry.source_file == "data/rules/test.json"
        assert entry.source_hash == "abc123"
        assert entry.generator_type == "rule"
    
    def test_entry_is_stale(self):
        """测试条目过时检测"""
        entry = ManifestEntry(
            source_file="test.json",
            output_file="test.py",
            source_hash="original_hash",
            output_hash="output_hash",
            generator_type="rule",
            engine_id="test",
            version="1.0.0"
        )
        
        # 相同哈希不过时
        assert entry.is_stale("original_hash") is False
        
        # 不同哈希过时
        assert entry.is_stale("new_hash") is True
    
    def test_entry_serialization(self):
        """测试条目序列化"""
        entry = ManifestEntry(
            source_file="test.json",
            output_file="test.py",
            source_hash="abc",
            output_hash="def",
            generator_type="factor",
            engine_id="test",
            version="1.0.0"
        )
        data = entry.model_dump()
        assert "source_file" in data
        assert "compiled_at" in data
        assert data["generator_type"] == "factor"


class TestCodegenManifest:
    """CodegenManifest 测试"""
    
    @pytest.fixture
    def manifest(self, tmp_path):
        """创建临时 manifest"""
        generated_dir = tmp_path / "generated"
        generated_dir.mkdir()
        return CodegenManifest(generated_dir=generated_dir)
    
    @pytest.fixture
    def sample_files(self, tmp_path):
        """创建测试用源文件和输出文件"""
        source = tmp_path / "source.json"
        source.write_text('{"id": "test"}')
        
        output = tmp_path / "generated" / "rules" / "output.py"
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text("# Generated\nx = 1")
        
        return source, output
    
    # ===== 基本操作测试 =====
    
    def test_add_entry(self, manifest, sample_files):
        """测试添加条目"""
        source, output = sample_files
        source_content = source.read_text()
        output_content = output.read_text()
        
        entry = manifest.add_entry(
            source_file=str(source),
            output_file=str(output),
            source_hash=compute_hash(source_content),
            output_hash=compute_hash(output_content),
            generator_type="rule",
            engine_id="test",
            version="1.0.0"
        )
        
        assert entry.source_file == str(source)
        assert entry.output_file == str(output)
        
        # 应该能获取到
        retrieved = manifest.get_entry(str(source))
        assert retrieved is not None
        assert retrieved.source_file == str(source)
    
    def test_get_entry_not_found(self, manifest, tmp_path):
        """测试获取不存在的条目"""
        entry = manifest.get_entry(str(tmp_path / "nonexistent.json"))
        assert entry is None
    
    def test_remove_entry(self, manifest, sample_files):
        """测试移除条目"""
        source, output = sample_files
        source_content = source.read_text()
        output_content = output.read_text()
        
        manifest.add_entry(
            source_file=str(source),
            output_file=str(output),
            source_hash=compute_hash(source_content),
            output_hash=compute_hash(output_content),
            generator_type="rule",
            engine_id="test",
            version="1.0.0"
        )
        
        # 移除
        result = manifest.remove_entry(str(source))
        assert result is True
        
        # 应该找不到了
        assert manifest.get_entry(str(source)) is None
        
        # 再次移除应该返回 False
        assert manifest.remove_entry(str(source)) is False
    
    # ===== Hash 对比测试 =====
    
    def test_needs_recompile_source_changed(self, manifest, sample_files):
        """测试源文件变化后需要重新编译"""
        source, output = sample_files
        original_hash = compute_hash(source.read_text())
        
        manifest.add_entry(
            source_file=str(source),
            output_file=str(output),
            source_hash=original_hash,
            output_hash=compute_hash(output.read_text()),
            generator_type="rule",
            engine_id="test",
            version="1.0.0"
        )
        
        # 原始哈希不需要重新编译
        assert manifest.needs_recompile(str(source), original_hash) is False
        
        # 新哈希需要重新编译
        new_hash = compute_hash('{"id": "changed"}')
        assert manifest.needs_recompile(str(source), new_hash) is True
    
    def test_needs_recompile_not_tracked(self, manifest, tmp_path):
        """测试未跟踪的文件需要编译"""
        source = tmp_path / "untracked.json"
        source.write_text("{}")
        
        # 未跟踪的文件应该需要编译
        assert manifest.needs_recompile(str(source), compute_hash("{}")) is True
    
    # ===== 按类型/引擎查询测试 =====
    
    def test_get_entries_by_type(self, manifest, tmp_path):
        """测试按类型获取条目"""
        # 添加不同类型的条目
        for i, gen_type in enumerate(["rule", "factor", "semantic", "rule"]):
            manifest.add_entry(
                source_file=f"source_{i}.json",
                output_file=f"output_{i}.py",
                source_hash=f"hash_{i}",
                output_hash=f"out_hash_{i}",
                generator_type=gen_type,
                engine_id="test",
                version="1.0.0"
            )
        
        rules = manifest.get_entries_by_type("rule")
        assert len(rules) == 2
        
        factors = manifest.get_entries_by_type("factor")
        assert len(factors) == 1
    
    def test_get_entries_by_engine(self, manifest, tmp_path):
        """测试按引擎获取条目"""
        for i, engine in enumerate(["bazi", "bazi", "astro"]):
            manifest.add_entry(
                source_file=f"source_{i}.json",
                output_file=f"output_{i}.py",
                source_hash=f"hash_{i}",
                output_hash=f"out_hash_{i}",
                generator_type="rule",
                engine_id=engine,
                version="1.0.0"
            )
        
        bazi_entries = manifest.get_entries_by_engine("bazi")
        assert len(bazi_entries) == 2
        
        astro_entries = manifest.get_entries_by_engine("astro")
        assert len(astro_entries) == 1
    
    # ===== 状态查询测试 =====
    
    def test_get_status(self, manifest, tmp_path):
        """测试获取清单状态"""
        manifest.add_entry(
            source_file="rule1.json",
            output_file="rule1.py",
            source_hash="h1",
            output_hash="oh1",
            generator_type="rule",
            engine_id="test",
            version="1.0.0"
        )
        manifest.add_entry(
            source_file="factor1.json",
            output_file="factor1.py",
            source_hash="h2",
            output_hash="oh2",
            generator_type="factor",
            engine_id="test",
            version="1.0.0"
        )
        
        status = manifest.get_status()
        assert status["total_entries"] == 2
        assert status["by_type"]["rule"] == 1
        assert status["by_type"]["factor"] == 1
    
    # ===== 多条目测试 =====
    
    def test_multiple_entries(self, manifest, tmp_path):
        """测试多个条目"""
        for i in range(5):
            manifest.add_entry(
                source_file=f"source_{i}.json",
                output_file=f"output_{i}.py",
                source_hash=f"hash_{i}",
                output_hash=f"out_hash_{i}",
                generator_type="rule",
                engine_id="test",
                version="1.0.0"
            )
        
        all_entries = manifest.get_all_entries()
        assert len(all_entries) == 5
        
        # 验证每个都可以获取
        for i in range(5):
            entry = manifest.get_entry(f"source_{i}.json")
            assert entry is not None
    
    def test_update_existing_entry(self, manifest):
        """测试更新已存在的条目"""
        # 第一次添加
        manifest.add_entry(
            source_file="test.json",
            output_file="test.py",
            source_hash="hash_v1",
            output_hash="out_v1",
            generator_type="rule",
            engine_id="test",
            version="1.0.0"
        )
        
        # 更新同一源文件
        manifest.add_entry(
            source_file="test.json",
            output_file="test.py",
            source_hash="hash_v2",
            output_hash="out_v2",
            generator_type="rule",
            engine_id="test",
            version="1.1.0"
        )
        
        # 应该只有一个条目
        assert len(manifest.get_all_entries()) == 1
        
        # 应该是更新后的版本
        entry = manifest.get_entry("test.json")
        assert entry.source_hash == "hash_v2"
        assert entry.version == "1.1.0"


class TestCodegenManifestPersistence:
    """持久化测试"""
    
    def test_manifest_persists_to_file(self, tmp_path):
        """测试清单持久化到文件"""
        generated_dir = tmp_path / "generated"
        generated_dir.mkdir()
        
        # 创建并添加条目
        manifest1 = CodegenManifest(generated_dir=generated_dir)
        manifest1.add_entry(
            source_file="test.json",
            output_file="test.py",
            source_hash="abc",
            output_hash="def",
            generator_type="rule",
            engine_id="test",
            version="1.0.0"
        )
        
        # 创建新实例，应该能加载之前的数据
        manifest2 = CodegenManifest(generated_dir=generated_dir)
        entry = manifest2.get_entry("test.json")
        
        assert entry is not None
        assert entry.source_hash == "abc"
    
    def test_manifest_file_format(self, tmp_path):
        """测试清单文件格式"""
        generated_dir = tmp_path / "generated"
        generated_dir.mkdir()
        
        manifest = CodegenManifest(generated_dir=generated_dir)
        manifest.add_entry(
            source_file="test.json",
            output_file="test.py",
            source_hash="abc",
            output_hash="def",
            generator_type="rule",
            engine_id="test",
            version="1.0.0"
        )
        
        # 验证文件存在并是有效 JSON
        manifest_file = generated_dir / ".codegen_manifest.json"
        assert manifest_file.exists()
        
        data = json.loads(manifest_file.read_text())
        assert "version" in data
        assert "entries" in data
        assert "test.json" in data["entries"]
