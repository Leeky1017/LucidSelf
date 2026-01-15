"""
JSONL Writer

将规则输出为 JSONL 文件。

Feature: rule-converter
Requirement Refs: Req 10.1-10.7
"""

import json
import logging
import shutil
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class WriteMode(Enum):
    """写入模式"""
    APPEND = "append"      # 追加到现有文件
    OVERWRITE = "overwrite"  # 覆盖现有文件
    MERGE = "merge"        # 合并，按 rule_id 去重


@dataclass
class WriteResult:
    """写入结果"""
    file_path: Path
    rules_written: int
    rules_skipped: int
    mode: WriteMode
    success: bool
    error: Optional[str] = None


class JSONLWriter:
    """
    JSONL 规则写入器
    
    将规则写入 `data/rules/{system}/{category}.jsonl` 格式的文件。
    
    特性：
    - 支持三种写入模式：append、overwrite、merge
    - 原子写入（先写临时文件再重命名）
    - 自动创建目录
    - 生成 manifest 文件
    
    Requirement Refs: Req 10.1-10.7
    """
    
    def __init__(self, output_dir: Optional[Path] = None):
        self.output_dir = Path(output_dir) if output_dir else Path("data/rules")
        self._manifest: Dict[str, Any] = {
            "generated_at": "",
            "files": [],
            "total_rules": 0,
        }
    
    def write_rules(
        self,
        rules: List[Dict],
        system: str,
        category: str,
        mode: WriteMode = WriteMode.OVERWRITE,
    ) -> WriteResult:
        """
        写入规则到指定文件
        
        Args:
            rules: 规则列表
            system: 体系（如 bazi, ziwei）
            category: 类别（如 career, wealth）
            mode: 写入模式
            
        Returns:
            WriteResult
        """
        # 构建文件路径
        file_path = self.output_dir / system / f"{category}.jsonl"
        
        # 确保目录存在
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            if mode == WriteMode.APPEND:
                result = self._write_append(file_path, rules, mode)
            elif mode == WriteMode.OVERWRITE:
                result = self._write_overwrite(file_path, rules, mode)
            elif mode == WriteMode.MERGE:
                result = self._write_merge(file_path, rules, mode)
            else:
                raise ValueError(f"Unknown write mode: {mode}")
            
            # 更新 manifest
            if result.success:
                self._manifest["files"].append({
                    "path": str(result.file_path),
                    "system": system,
                    "category": category,
                    "rules": result.rules_written,
                })
                self._manifest["total_rules"] += result.rules_written
            
            return result
        except Exception as e:
            logger.error(f"Failed to write {file_path}: {e}")
            return WriteResult(
                file_path=file_path,
                rules_written=0,
                rules_skipped=0,
                mode=mode,
                success=False,
                error=str(e),
            )
    
    def _write_append(self, file_path: Path, rules: List[Dict], mode: WriteMode) -> WriteResult:
        """追加模式"""
        with open(file_path, "a", encoding="utf-8") as f:
            for rule in rules:
                f.write(json.dumps(rule, ensure_ascii=False) + "\n")
        
        return WriteResult(
            file_path=file_path,
            rules_written=len(rules),
            rules_skipped=0,
            mode=mode,
            success=True,
        )
    
    def _write_overwrite(self, file_path: Path, rules: List[Dict], mode: WriteMode) -> WriteResult:
        """覆盖模式（原子写入）"""
        # 写入临时文件
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            suffix=".jsonl",
            delete=False,
        ) as tmp:
            for rule in rules:
                tmp.write(json.dumps(rule, ensure_ascii=False) + "\n")
            tmp_path = Path(tmp.name)
        
        # 原子重命名
        try:
            shutil.move(str(tmp_path), str(file_path))
        except Exception:
            tmp_path.unlink(missing_ok=True)
            raise
        
        return WriteResult(
            file_path=file_path,
            rules_written=len(rules),
            rules_skipped=0,
            mode=mode,
            success=True,
        )
    
    def _write_merge(self, file_path: Path, rules: List[Dict], mode: WriteMode) -> WriteResult:
        """合并模式（按 rule_id 去重，保留新版本）"""
        # 读取现有规则
        existing_rules: Dict[str, Dict] = {}
        if file_path.exists():
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        rule = json.loads(line)
                        rule_id = rule.get("rule_id")
                        if rule_id:
                            existing_rules[rule_id] = rule
        
        # 合并新规则
        skipped = 0
        for rule in rules:
            rule_id = rule.get("rule_id")
            if rule_id:
                if rule_id in existing_rules:
                    # 比较版本，保留新版本
                    existing_version = existing_rules[rule_id].get("version", "0.0.0")
                    new_version = rule.get("version", "1.0.0")
                    if self._compare_versions(new_version, existing_version) <= 0:
                        skipped += 1
                        continue
                existing_rules[rule_id] = rule
        
        # 写入
        all_rules = list(existing_rules.values())
        result = self._write_overwrite(file_path, all_rules, mode)
        result.rules_skipped = skipped
        result.rules_written = len(rules) - skipped
        
        return result
    
    def _compare_versions(self, v1: str, v2: str) -> int:
        """比较版本号，返回 1(v1>v2), 0(v1==v2), -1(v1<v2)"""
        try:
            parts1 = [int(x) for x in v1.split(".")]
            parts2 = [int(x) for x in v2.split(".")]
            
            for p1, p2 in zip(parts1, parts2):
                if p1 > p2:
                    return 1
                elif p1 < p2:
                    return -1
            return 0
        except Exception:
            return 0
    
    def write_batch(
        self,
        rules_by_system: Dict[str, Dict[str, List[Dict]]],
        mode: WriteMode = WriteMode.OVERWRITE,
    ) -> List[WriteResult]:
        """
        批量写入规则
        
        Args:
            rules_by_system: {system: {category: [rules]}} 格式
            mode: 写入模式
            
        Returns:
            写入结果列表
        """
        results = []
        
        for system, categories in rules_by_system.items():
            for category, rules in categories.items():
                result = self.write_rules(rules, system, category, mode)
                results.append(result)
                # manifest 已在 write_rules 中更新
        
        return results
    
    def write_manifest(self, manifest_path: Optional[Path] = None) -> Path:
        """
        写入 manifest 文件
        
        Args:
            manifest_path: manifest 文件路径
            
        Returns:
            manifest 文件路径
        """
        if manifest_path is None:
            manifest_path = self.output_dir / "conversion_manifest.json"
        
        self._manifest["generated_at"] = datetime.now(timezone.utc).isoformat()
        
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(self._manifest, f, ensure_ascii=False, indent=2)
        
        return manifest_path
    
    def group_rules_by_system_category(
        self,
        rules: List[Dict],
    ) -> Dict[str, Dict[str, List[Dict]]]:
        """
        将规则按体系和类别分组
        
        Args:
            rules: 规则列表
            
        Returns:
            {system: {category: [rules]}}
        """
        grouped: Dict[str, Dict[str, List[Dict]]] = {}
        
        for rule in rules:
            # 从 engine_id 提取体系
            engine_id = rule.get("engine_id", "unknown_rule_engine")
            system = engine_id.replace("_rule_engine", "")
            
            # 从 category 获取类别
            category = rule.get("category", "general")
            
            if system not in grouped:
                grouped[system] = {}
            if category not in grouped[system]:
                grouped[system][category] = []
            
            grouped[system][category].append(rule)
        
        return grouped
