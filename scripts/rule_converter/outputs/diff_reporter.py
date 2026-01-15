"""
Diff Reporter

比较转换运行之间的差异。

Feature: rule-converter
Requirement Refs: Req 11.1-11.5
"""

import json
import logging
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

logger = logging.getLogger(__name__)


@dataclass
class RuleDiff:
    """单个规则的差异"""
    rule_id: str
    diff_type: str  # added, modified, removed
    old_value: Optional[Dict] = None
    new_value: Optional[Dict] = None
    changed_fields: List[str] = field(default_factory=list)


@dataclass
class DiffReport:
    """差异报告"""
    old_path: str
    new_path: str
    generated_at: str
    
    added_count: int = 0
    modified_count: int = 0
    removed_count: int = 0
    
    diffs: List[RuleDiff] = field(default_factory=list)
    
    @property
    def total_changes(self) -> int:
        return self.added_count + self.modified_count + self.removed_count
    
    def to_dict(self) -> Dict:
        return {
            "old_path": self.old_path,
            "new_path": self.new_path,
            "generated_at": self.generated_at,
            "summary": {
                "added": self.added_count,
                "modified": self.modified_count,
                "removed": self.removed_count,
                "total": self.total_changes,
            },
            "diffs": [
                {
                    "rule_id": d.rule_id,
                    "type": d.diff_type,
                    "changed_fields": d.changed_fields,
                }
                for d in self.diffs[:100]  # 最多显示100个
            ],
        }
    
    def to_markdown(self) -> str:
        """生成 Markdown 格式报告"""
        lines = [
            "# Rule Conversion Diff Report",
            "",
            f"**Generated**: {self.generated_at}",
            f"**Old**: {self.old_path}",
            f"**New**: {self.new_path}",
            "",
            "## Summary",
            "",
            f"- **Added**: {self.added_count}",
            f"- **Modified**: {self.modified_count}",
            f"- **Removed**: {self.removed_count}",
            f"- **Total Changes**: {self.total_changes}",
            "",
        ]
        
        if self.diffs:
            lines.extend([
                "## Changes",
                "",
            ])
            
            # 按类型分组
            added = [d for d in self.diffs if d.diff_type == "added"]
            modified = [d for d in self.diffs if d.diff_type == "modified"]
            removed = [d for d in self.diffs if d.diff_type == "removed"]
            
            if added:
                lines.extend([
                    "### Added Rules",
                    "",
                ])
                for d in added[:20]:
                    lines.append(f"- `{d.rule_id}`")
                if len(added) > 20:
                    lines.append(f"- ... and {len(added) - 20} more")
                lines.append("")
            
            if modified:
                lines.extend([
                    "### Modified Rules",
                    "",
                ])
                for d in modified[:20]:
                    fields = ", ".join(d.changed_fields[:5])
                    if len(d.changed_fields) > 5:
                        fields += f" +{len(d.changed_fields) - 5} more"
                    lines.append(f"- `{d.rule_id}`: {fields}")
                if len(modified) > 20:
                    lines.append(f"- ... and {len(modified) - 20} more")
                lines.append("")
            
            if removed:
                lines.extend([
                    "### Removed Rules",
                    "",
                ])
                for d in removed[:20]:
                    lines.append(f"- `{d.rule_id}`")
                if len(removed) > 20:
                    lines.append(f"- ... and {len(removed) - 20} more")
                lines.append("")
        
        return "\n".join(lines)


class DiffReporter:
    """
    差异报告生成器
    
    比较两次转换运行的结果，生成差异报告。
    
    Requirement Refs: Req 11.1-11.5
    """
    
    # 比较时忽略的字段
    IGNORE_FIELDS = {"metadata.extraction_date"}
    
    def compare_files(self, old_path: Path, new_path: Path) -> DiffReport:
        """
        比较两个 JSONL 文件
        
        Args:
            old_path: 旧文件路径
            new_path: 新文件路径
            
        Returns:
            DiffReport
        """
        # 加载规则
        old_rules = self._load_rules(old_path) if old_path.exists() else {}
        new_rules = self._load_rules(new_path) if new_path.exists() else {}
        
        return self._compare_rules(old_rules, new_rules, str(old_path), str(new_path))
    
    def compare_directories(self, old_dir: Path, new_dir: Path) -> DiffReport:
        """
        比较两个目录下的所有规则文件
        
        Args:
            old_dir: 旧目录
            new_dir: 新目录
            
        Returns:
            合并的 DiffReport
        """
        # 收集所有规则
        old_rules: Dict[str, Dict] = {}
        new_rules: Dict[str, Dict] = {}
        
        if old_dir.exists():
            for jsonl_file in old_dir.rglob("*.jsonl"):
                old_rules.update(self._load_rules(jsonl_file))
        
        if new_dir.exists():
            for jsonl_file in new_dir.rglob("*.jsonl"):
                new_rules.update(self._load_rules(jsonl_file))
        
        return self._compare_rules(old_rules, new_rules, str(old_dir), str(new_dir))
    
    def _load_rules(self, path: Path) -> Dict[str, Dict]:
        """加载 JSONL 文件中的规则"""
        rules = {}
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        rule = json.loads(line)
                        rule_id = rule.get("rule_id")
                        if rule_id:
                            rules[rule_id] = rule
                    except json.JSONDecodeError:
                        logger.warning(f"Failed to parse line in {path}")
        return rules
    
    def _compare_rules(
        self,
        old_rules: Dict[str, Dict],
        new_rules: Dict[str, Dict],
        old_path: str,
        new_path: str,
    ) -> DiffReport:
        """比较两组规则"""
        report = DiffReport(
            old_path=old_path,
            new_path=new_path,
            generated_at=datetime.utcnow().isoformat(),
        )
        
        old_ids = set(old_rules.keys())
        new_ids = set(new_rules.keys())
        
        # 新增的规则
        added_ids = new_ids - old_ids
        for rule_id in added_ids:
            report.diffs.append(RuleDiff(
                rule_id=rule_id,
                diff_type="added",
                new_value=new_rules[rule_id],
            ))
        report.added_count = len(added_ids)
        
        # 删除的规则
        removed_ids = old_ids - new_ids
        for rule_id in removed_ids:
            report.diffs.append(RuleDiff(
                rule_id=rule_id,
                diff_type="removed",
                old_value=old_rules[rule_id],
            ))
        report.removed_count = len(removed_ids)
        
        # 修改的规则
        common_ids = old_ids & new_ids
        for rule_id in common_ids:
            changed_fields = self._get_changed_fields(
                old_rules[rule_id],
                new_rules[rule_id],
            )
            if changed_fields:
                report.diffs.append(RuleDiff(
                    rule_id=rule_id,
                    diff_type="modified",
                    old_value=old_rules[rule_id],
                    new_value=new_rules[rule_id],
                    changed_fields=changed_fields,
                ))
        report.modified_count = len([d for d in report.diffs if d.diff_type == "modified"])
        
        return report
    
    def _get_changed_fields(
        self,
        old_rule: Dict,
        new_rule: Dict,
        prefix: str = "",
    ) -> List[str]:
        """获取变化的字段"""
        changed = []
        
        all_keys = set(old_rule.keys()) | set(new_rule.keys())
        
        for key in all_keys:
            field_path = f"{prefix}.{key}" if prefix else key
            
            # 检查是否忽略
            if field_path in self.IGNORE_FIELDS:
                continue
            
            old_val = old_rule.get(key)
            new_val = new_rule.get(key)
            
            if old_val != new_val:
                if isinstance(old_val, dict) and isinstance(new_val, dict):
                    # 递归比较嵌套字典
                    nested_changed = self._get_changed_fields(old_val, new_val, field_path)
                    changed.extend(nested_changed)
                else:
                    changed.append(field_path)
        
        return changed
    
    def save_report(self, report: DiffReport, output_path: Path, format: str = "json") -> None:
        """
        保存差异报告
        
        Args:
            report: 差异报告
            output_path: 输出路径
            format: 格式（json 或 markdown）
        """
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        if format == "json":
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(report.to_dict(), f, ensure_ascii=False, indent=2)
        elif format == "markdown":
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(report.to_markdown())
        else:
            raise ValueError(f"Unknown format: {format}")
