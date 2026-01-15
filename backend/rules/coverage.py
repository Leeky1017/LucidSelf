"""
Rule Coverage Report Generator

规则覆盖率报告生成器。

对照 Task 23: Integration and Coverage Report
对照 Requirement 14.8-14.10
"""

from __future__ import annotations

import json
import logging
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional

# 复用已有定义，避免冗余
from backend.core.contracts import SUPPORTED_SYSTEMS
from backend.rules.dimension import STANDARD_DIMENSIONS

logger = logging.getLogger(__name__)

# 使用 SUPPORTED_SYSTEMS 作为体系列表（统一命名）
SYSTEMS = SUPPORTED_SYSTEMS

# 最低覆盖率阈值
MIN_COVERAGE_THRESHOLD = 0.8


class CoverageReporter:
    """规则覆盖率报告生成器"""
    
    def __init__(self, rules_dir: Path = Path("data/rules")):
        self.rules_dir = Path(rules_dir)
        self._rules: Dict[str, List[Dict]] = {}
    
    def load_rules(self) -> None:
        """加载所有规则"""
        for system in SYSTEMS:
            system_dir = self.rules_dir / system
            if not system_dir.exists():
                continue
            
            self._rules[system] = []
            for jsonl_file in system_dir.glob("*.jsonl"):
                with open(jsonl_file, "r", encoding="utf-8") as f:
                    for line in f:
                        if line.strip():
                            try:
                                rule = json.loads(line)
                                self._rules[system].append(rule)
                            except json.JSONDecodeError:
                                continue
    
    def generate_report(self) -> Dict[str, Any]:
        """
        生成覆盖率报告
        
        Returns:
            {
                "summary": {...},
                "by_system": {...},
                "by_dimension": {...},
                "coverage_matrix": [...],
                "warnings": [...]
            }
        """
        self.load_rules()
        
        # 按体系统计
        by_system = {}
        for system, rules in self._rules.items():
            dims = defaultdict(int)
            for rule in rules:
                dim = rule.get("result", {}).get("dimension", "general")
                dims[dim] += 1
            
            by_system[system] = {
                "total_rules": len(rules),
                "dimensions": dict(dims),
                "dimension_count": len(dims),
            }
        
        # 按维度统计
        by_dimension = defaultdict(lambda: {"total": 0, "systems": defaultdict(int)})
        for system, rules in self._rules.items():
            for rule in rules:
                dim = rule.get("result", {}).get("dimension", "general")
                by_dimension[dim]["total"] += 1
                by_dimension[dim]["systems"][system] += 1
        
        # 覆盖率矩阵
        coverage_matrix = []
        for system in SYSTEMS:
            row = {"system": system}
            rules = self._rules.get(system, [])
            dims = set(r.get("result", {}).get("dimension", "general") for r in rules)
            
            for dim in STANDARD_DIMENSIONS:
                row[dim] = dim in dims
            
            coverage_matrix.append(row)
        
        # 警告（低覆盖率体系）
        warnings = []
        for system, data in by_system.items():
            coverage = data["dimension_count"] / len(STANDARD_DIMENSIONS)
            if coverage < MIN_COVERAGE_THRESHOLD:
                warnings.append({
                    "system": system,
                    "coverage": round(coverage * 100, 1),
                    "message": f"{system} coverage {coverage*100:.1f}% below threshold {MIN_COVERAGE_THRESHOLD*100}%"
                })
        
        # 汇总
        total_rules = sum(len(r) for r in self._rules.values())
        
        return {
            "summary": {
                "total_rules": total_rules,
                "total_systems": len(self._rules),
                "total_dimensions": len(by_dimension),
            },
            "by_system": by_system,
            "by_dimension": dict(by_dimension),
            "coverage_matrix": coverage_matrix,
            "warnings": warnings,
        }
    
    def print_report(self) -> None:
        """打印报告"""
        report = self.generate_report()
        
        print("=" * 60)
        print("Rule Coverage Report")
        print("=" * 60)
        
        print(f"\nTotal Rules: {report['summary']['total_rules']}")
        print(f"Systems: {report['summary']['total_systems']}")
        print(f"Dimensions: {report['summary']['total_dimensions']}")
        
        print("\n--- By System ---")
        for system, data in report["by_system"].items():
            print(f"  {system}: {data['total_rules']} rules, {data['dimension_count']} dimensions")
        
        if report["warnings"]:
            print("\n--- Warnings ---")
            for w in report["warnings"]:
                print(f"  ⚠️ {w['message']}")
        
        print("\n" + "=" * 60)
