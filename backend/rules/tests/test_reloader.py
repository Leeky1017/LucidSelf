"""
Test Rule Reloader

规则热重载器测试 - 验证文件监控、重新编译、事件回调。

对照 tasks.md Task 9:
- Validates: Requirements 13.1-13.4
"""

import json
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from backend.rules.reloader import RuleReloader, ReloadEvent


@pytest.fixture
def sample_rule_json():
    """创建示例规则 JSON"""
    return {
        "rule_id": "test_reload_rule",
        "human_label": "测试重载规则",
        "category": "test",
        "condition": {
            "factor_id": "day_master",
            "operator": "==",
            "value": "甲",
        },
        "required_factors": ["day_master"],
        "is_complex_logic": False,
        "result": {
            "dimension": "personality",
            "level": "吉",
            "conclusion_template_zh": "测试结论",
            "weight": 1.0,
            "confidence": 0.8,
            "tags": ["test"],
            "evidence_factors": ["day_master"],
        },
        "priority": 100,
        "version": "1.0.0",
        "status": "active",
        "engine_id": "bazi_rule_engine",
        "metadata": {
            "book_id": "test_book",
            "chapter": "chapter1",
            "l1_anchor": "TEST_L1_001",
        }
    }


class TestRuleReloaderBasic:
    """基础功能测试"""
    
    def test_reloader_init(self):
        """测试初始化"""
        with tempfile.TemporaryDirectory() as tmpdir:
            reloader = RuleReloader(watch_dir=Path(tmpdir))
            
            assert reloader.watch_dir == Path(tmpdir)
            assert len(reloader.get_reload_history()) == 0
    
    def test_reload_file_success(self, sample_rule_json):
        """测试成功重载文件"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir = Path(tmpdir)
            
            # 创建 JSONL 文件
            rules_file = tmpdir / "test_rules.jsonl"
            with open(rules_file, "w", encoding="utf-8") as f:
                f.write(json.dumps(sample_rule_json, ensure_ascii=False) + "\n")
            
            # 创建 reloader
            reloader = RuleReloader(watch_dir=tmpdir)
            
            # Mock codegen
            mock_codegen = MagicMock()
            mock_codegen.compile_jsonl.return_value = {
                "source_file": str(rules_file),
                "rules_compiled": 1,
                "rules_skipped": 0,
                "errors": [],
                "output_files": [],
            }
            reloader._codegen = mock_codegen
            
            # 重载
            result = reloader.reload_file(rules_file)
            
            assert result is True
            mock_codegen.compile_jsonl.assert_called_once()
            
            # 检查历史记录
            history = reloader.get_reload_history()
            assert len(history) == 1
            assert history[0]["success"] is True
    
    def test_reload_file_failure(self, sample_rule_json):
        """测试重载失败"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir = Path(tmpdir)
            rules_file = tmpdir / "bad_rules.jsonl"
            rules_file.write_text("{invalid json}")
            
            reloader = RuleReloader(watch_dir=tmpdir)
            
            # Mock codegen 返回错误
            mock_codegen = MagicMock()
            mock_codegen.compile_jsonl.return_value = {
                "source_file": str(rules_file),
                "rules_compiled": 0,
                "rules_skipped": 0,
                "errors": [{"error": "Invalid JSON"}],
                "output_files": [],
            }
            reloader._codegen = mock_codegen
            
            result = reloader.reload_file(rules_file)
            
            assert result is False
            
            history = reloader.get_reload_history()
            assert len(history) == 1
            assert history[0]["success"] is False


class TestRuleReloaderEvents:
    """事件回调测试"""
    
    def test_event_callback_success(self, sample_rule_json):
        """测试成功事件回调"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir = Path(tmpdir)
            rules_file = tmpdir / "test_rules.jsonl"
            rules_file.write_text(json.dumps(sample_rule_json, ensure_ascii=False))
            
            reloader = RuleReloader(watch_dir=tmpdir)
            
            # Mock codegen
            mock_codegen = MagicMock()
            mock_codegen.compile_jsonl.return_value = {
                "source_file": str(rules_file),
                "rules_compiled": 1,
                "rules_skipped": 0,
                "errors": [],
                "output_files": [],
            }
            reloader._codegen = mock_codegen
            
            # 注册回调
            callback_data = []
            def on_reload(data):
                callback_data.append(data)
            
            reloader.on_event(ReloadEvent.RULE_RELOADED, on_reload)
            
            # 重载
            reloader.reload_file(rules_file)
            
            # 验证回调被调用
            assert len(callback_data) == 1
            assert callback_data[0]["rules"] == 1
    
    def test_event_callback_failure(self, sample_rule_json):
        """测试失败事件回调"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir = Path(tmpdir)
            rules_file = tmpdir / "bad_rules.jsonl"
            rules_file.write_text("{bad json}")
            
            reloader = RuleReloader(watch_dir=tmpdir)
            
            # Mock codegen 返回错误
            mock_codegen = MagicMock()
            mock_codegen.compile_jsonl.return_value = {
                "source_file": str(rules_file),
                "rules_compiled": 0,
                "rules_skipped": 0,
                "errors": [{"error": "Parse error"}],
                "output_files": [],
            }
            reloader._codegen = mock_codegen
            
            # 注册回调
            callback_data = []
            def on_fail(data):
                callback_data.append(data)
            
            reloader.on_event(ReloadEvent.RULE_RELOAD_FAILED, on_fail)
            
            # 重载
            reloader.reload_file(rules_file)
            
            # 验证失败回调被调用
            assert len(callback_data) == 1
            assert "errors" in callback_data[0]


class TestRuleReloaderHistory:
    """历史记录测试"""
    
    def test_reload_history_limit(self):
        """测试历史记录限制（最多100条）"""
        with tempfile.TemporaryDirectory() as tmpdir:
            reloader = RuleReloader(watch_dir=Path(tmpdir))
            
            # 直接添加记录来测试限制
            for i in range(120):
                reloader._log_reload(Path(f"file_{i}.jsonl"), success=True)
            
            history = reloader.get_reload_history()
            assert len(history) == 100
            
            # 应该保留最新的记录
            assert "file_119.jsonl" in history[-1]["file"]


class TestReloadEventTypes:
    """事件类型测试"""
    
    def test_event_types(self):
        """测试事件类型常量"""
        assert ReloadEvent.RULE_RELOADED == "rule_reloaded"
        assert ReloadEvent.RULE_RELOAD_FAILED == "rule_reload_failed"
