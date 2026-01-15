"""
Tests for Outputs (JSONLWriter, DiffReporter, ReviewQueue)

Requirement Refs: Req 10-12
"""

import json
import tempfile
from pathlib import Path

import pytest

from scripts.rule_converter.outputs.jsonl_writer import (
    JSONLWriter,
    WriteMode,
)
from scripts.rule_converter.outputs.diff_reporter import (
    DiffReporter,
    DiffReport,
)
from scripts.rule_converter.outputs.review_queue import (
    ReviewQueue,
    ReviewItem,
    ReviewStatus,
)


# ===========================================================================
# Test JSONLWriter
# ===========================================================================

class TestJSONLWriter:
    """测试 JSONLWriter"""
    
    @pytest.fixture
    def temp_dir(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            yield Path(tmpdir)
    
    @pytest.fixture
    def sample_rules(self):
        return [
            {
                "rule_id": "bazi_dts_career_001",
                "human_label": "规则1",
                "category": "career",
                "engine_id": "bazi_rule_engine",
                "version": "1.0.0",
            },
            {
                "rule_id": "bazi_dts_career_002",
                "human_label": "规则2",
                "category": "career",
                "engine_id": "bazi_rule_engine",
                "version": "1.0.0",
            },
        ]
    
    def test_write_overwrite_mode(self, temp_dir, sample_rules):
        """测试覆盖写入模式"""
        writer = JSONLWriter(temp_dir)
        
        result = writer.write_rules(sample_rules, "bazi", "career", WriteMode.OVERWRITE)
        
        assert result.success is True
        assert result.rules_written == 2
        assert result.file_path.exists()
        
        # 验证文件内容
        with open(result.file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        assert len(lines) == 2
    
    def test_write_append_mode(self, temp_dir, sample_rules):
        """测试追加写入模式"""
        writer = JSONLWriter(temp_dir)
        
        # 先写入
        writer.write_rules(sample_rules[:1], "bazi", "career", WriteMode.OVERWRITE)
        
        # 追加
        result = writer.write_rules(sample_rules[1:], "bazi", "career", WriteMode.APPEND)
        
        assert result.success is True
        
        # 验证文件内容
        with open(result.file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        assert len(lines) == 2
    
    def test_write_merge_mode(self, temp_dir, sample_rules):
        """测试合并写入模式"""
        writer = JSONLWriter(temp_dir)
        
        # 先写入
        writer.write_rules(sample_rules, "bazi", "career", WriteMode.OVERWRITE)
        
        # 合并（同ID新版本覆盖，旧版本跳过）
        new_rules = [
            {
                "rule_id": "bazi_dts_career_001",
                "human_label": "更新的规则1",
                "version": "1.0.1",  # 新版本
            },
            {
                "rule_id": "bazi_dts_career_003",  # 新ID
                "human_label": "规则3",
                "version": "1.0.0",
            },
        ]
        
        result = writer.write_rules(new_rules, "bazi", "career", WriteMode.MERGE)
        
        assert result.success is True
        
        # 验证文件内容（应该有3条）
        with open(result.file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        assert len(lines) == 3
    
    def test_group_rules_by_system_category(self, sample_rules):
        """测试规则分组"""
        writer = JSONLWriter()
        
        grouped = writer.group_rules_by_system_category(sample_rules)
        
        assert "bazi" in grouped
        assert "career" in grouped["bazi"]
        assert len(grouped["bazi"]["career"]) == 2
    
    def test_write_batch(self, temp_dir, sample_rules):
        """测试批量写入"""
        writer = JSONLWriter(temp_dir)
        
        # 添加更多不同类别的规则
        all_rules = sample_rules + [
            {
                "rule_id": "bazi_dts_wealth_001",
                "human_label": "财运规则",
                "category": "wealth",
                "engine_id": "bazi_rule_engine",
            },
        ]
        
        grouped = writer.group_rules_by_system_category(all_rules)
        results = writer.write_batch(grouped)
        
        assert len(results) == 2
        assert all(r.success for r in results)
    
    def test_write_manifest(self, temp_dir, sample_rules):
        """测试写入 manifest"""
        writer = JSONLWriter(temp_dir)
        
        writer.write_rules(sample_rules, "bazi", "career", WriteMode.OVERWRITE)
        manifest_path = writer.write_manifest()
        
        assert manifest_path.exists()
        
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)
        
        assert manifest["total_rules"] == 2
        assert len(manifest["files"]) == 1


# ===========================================================================
# Test DiffReporter
# ===========================================================================

class TestDiffReporter:
    """测试 DiffReporter"""
    
    @pytest.fixture
    def temp_dir(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            yield Path(tmpdir)
    
    def _write_jsonl(self, path: Path, rules: list):
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            for rule in rules:
                f.write(json.dumps(rule, ensure_ascii=False) + "\n")
    
    def test_compare_files_added(self, temp_dir):
        """测试检测新增规则"""
        reporter = DiffReporter()
        
        old_path = temp_dir / "old.jsonl"
        new_path = temp_dir / "new.jsonl"
        
        old_rules = [{"rule_id": "rule_001", "version": "1.0.0"}]
        new_rules = [
            {"rule_id": "rule_001", "version": "1.0.0"},
            {"rule_id": "rule_002", "version": "1.0.0"},  # 新增
        ]
        
        self._write_jsonl(old_path, old_rules)
        self._write_jsonl(new_path, new_rules)
        
        report = reporter.compare_files(old_path, new_path)
        
        assert report.added_count == 1
        assert report.removed_count == 0
        assert report.modified_count == 0
    
    def test_compare_files_removed(self, temp_dir):
        """测试检测删除规则"""
        reporter = DiffReporter()
        
        old_path = temp_dir / "old.jsonl"
        new_path = temp_dir / "new.jsonl"
        
        old_rules = [
            {"rule_id": "rule_001", "version": "1.0.0"},
            {"rule_id": "rule_002", "version": "1.0.0"},
        ]
        new_rules = [{"rule_id": "rule_001", "version": "1.0.0"}]
        
        self._write_jsonl(old_path, old_rules)
        self._write_jsonl(new_path, new_rules)
        
        report = reporter.compare_files(old_path, new_path)
        
        assert report.added_count == 0
        assert report.removed_count == 1
        assert report.modified_count == 0
    
    def test_compare_files_modified(self, temp_dir):
        """测试检测修改规则"""
        reporter = DiffReporter()
        
        old_path = temp_dir / "old.jsonl"
        new_path = temp_dir / "new.jsonl"
        
        old_rules = [{"rule_id": "rule_001", "version": "1.0.0", "human_label": "旧标签"}]
        new_rules = [{"rule_id": "rule_001", "version": "1.0.0", "human_label": "新标签"}]
        
        self._write_jsonl(old_path, old_rules)
        self._write_jsonl(new_path, new_rules)
        
        report = reporter.compare_files(old_path, new_path)
        
        assert report.added_count == 0
        assert report.removed_count == 0
        assert report.modified_count == 1
        assert "human_label" in report.diffs[0].changed_fields
    
    def test_to_markdown(self, temp_dir):
        """测试生成 Markdown 报告"""
        reporter = DiffReporter()
        
        old_path = temp_dir / "old.jsonl"
        new_path = temp_dir / "new.jsonl"
        
        self._write_jsonl(old_path, [{"rule_id": "rule_001"}])
        self._write_jsonl(new_path, [{"rule_id": "rule_002"}])
        
        report = reporter.compare_files(old_path, new_path)
        markdown = report.to_markdown()
        
        assert "# Rule Conversion Diff Report" in markdown
        assert "Added" in markdown
        assert "Removed" in markdown


# ===========================================================================
# Test ReviewQueue
# ===========================================================================

class TestReviewQueue:
    """测试 ReviewQueue"""
    
    @pytest.fixture
    def temp_dir(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            yield Path(tmpdir)
    
    @pytest.fixture
    def sample_rule(self):
        return {
            "rule_id": "bazi_dts_career_001",
            "human_label": "测试规则",
            "category": "career",
        }
    
    def test_add_and_get(self, temp_dir, sample_rule):
        """测试添加和获取"""
        queue = ReviewQueue(temp_dir / "queue.json")
        
        item = queue.add(sample_rule, classification_score=0.6, classification_reasons=["测试"])
        
        assert item.rule_id == "bazi_dts_career_001"
        assert item.status == ReviewStatus.PENDING
        
        retrieved = queue.get("bazi_dts_career_001")
        assert retrieved is not None
        assert retrieved.classification_score == 0.6
    
    def test_approve(self, temp_dir, sample_rule):
        """测试批准"""
        queue = ReviewQueue(temp_dir / "queue.json")
        queue.add(sample_rule)
        
        result = queue.approve("bazi_dts_career_001", comment="OK")
        
        assert result is True
        
        item = queue.get("bazi_dts_career_001")
        assert item.status == ReviewStatus.APPROVED
        assert item.reviewer_comment == "OK"
    
    def test_reject(self, temp_dir, sample_rule):
        """测试拒绝"""
        queue = ReviewQueue(temp_dir / "queue.json")
        queue.add(sample_rule)
        
        result = queue.reject("bazi_dts_career_001", comment="质量不佳")
        
        assert result is True
        
        item = queue.get("bazi_dts_career_001")
        assert item.status == ReviewStatus.REJECTED
    
    def test_modify(self, temp_dir, sample_rule):
        """测试修改"""
        queue = ReviewQueue(temp_dir / "queue.json")
        queue.add(sample_rule)
        
        modified_rule = sample_rule.copy()
        modified_rule["human_label"] = "修改后的标签"
        
        result = queue.modify("bazi_dts_career_001", modified_rule, comment="修正标签")
        
        assert result is True
        
        item = queue.get("bazi_dts_career_001")
        assert item.status == ReviewStatus.MODIFIED
        assert item.modified_rule["human_label"] == "修改后的标签"
    
    def test_get_pending(self, temp_dir, sample_rule):
        """测试获取待审核项"""
        queue = ReviewQueue(temp_dir / "queue.json")
        
        queue.add(sample_rule)
        queue.add({**sample_rule, "rule_id": "rule_002"})
        queue.approve("bazi_dts_career_001")
        
        pending = queue.get_pending()
        
        assert len(pending) == 1
        assert pending[0].rule_id == "rule_002"
    
    def test_get_approved_rules(self, temp_dir, sample_rule):
        """测试获取已批准的规则"""
        queue = ReviewQueue(temp_dir / "queue.json")
        
        queue.add(sample_rule)
        queue.add({**sample_rule, "rule_id": "rule_002"})
        
        queue.approve("bazi_dts_career_001")
        queue.modify("rule_002", {**sample_rule, "rule_id": "rule_002", "human_label": "修改"})
        
        rules = queue.get_approved_rules()
        
        assert len(rules) == 2
    
    def test_save_and_load(self, temp_dir, sample_rule):
        """测试保存和加载"""
        queue_path = temp_dir / "queue.json"
        
        # 创建队列并添加项目
        queue = ReviewQueue(queue_path)
        queue.add(sample_rule)
        queue.approve("bazi_dts_career_001")
        queue.save()
        
        # 重新加载
        queue2 = ReviewQueue(queue_path)
        queue2.load()
        
        item = queue2.get("bazi_dts_career_001")
        assert item is not None
        assert item.status == ReviewStatus.APPROVED
    
    def test_stats(self, temp_dir, sample_rule):
        """测试统计"""
        queue = ReviewQueue(temp_dir / "queue.json")
        
        queue.add(sample_rule)
        queue.add({**sample_rule, "rule_id": "rule_002"})
        queue.add({**sample_rule, "rule_id": "rule_003"})
        
        queue.approve("bazi_dts_career_001")
        queue.reject("rule_002")
        
        stats = queue.stats
        
        assert stats["total"] == 3
        assert stats["pending"] == 1
        assert stats["approved"] == 1
        assert stats["rejected"] == 1
