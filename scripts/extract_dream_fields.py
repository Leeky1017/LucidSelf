#!/usr/bin/env python3
"""
提取梦境规则中的所有字段，与因子字典对比，生成缺失字段清单。
仅用于 add-dream-factors-and-cross-domain-axes change 的步骤 1。
"""

import json
import re
from pathlib import Path
from collections import defaultdict
from typing import Set, Dict, List, Tuple


def extract_fields_from_condition(cond: dict, fields: Set[str]) -> None:
    """递归提取条件中的 field"""
    if isinstance(cond, dict):
        if "field" in cond:
            fields.add(cond["field"])
        if "operands" in cond:
            for op in cond["operands"]:
                extract_fields_from_condition(op, fields)
        if "clauses" in cond:
            for cl in cond["clauses"]:
                extract_fields_from_condition(cl, fields)
        if "sub_clauses" in cond:
            for sc in cond["sub_clauses"]:
                extract_fields_from_condition(sc, fields)


def extract_fields_from_jsonl(file_path: Path) -> List[Tuple[str, str, Set[str]]]:
    """从 JSONL 文件提取 (rule_id, 文件名, 字段集)"""
    results = []
    
    if not file_path.exists():
        return results
    
    with open(file_path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            
            try:
                rule = json.loads(line)
                rule_id = rule.get("rule_id", f"unknown_{line_num}")
                fields = set()
                
                if "conditions" in rule:
                    extract_fields_from_condition(rule["conditions"], fields)
                
                if fields:
                    results.append((rule_id, file_path.name, fields))
            except json.JSONDecodeError:
                continue
    
    return results


def load_known_factors(factors_dict_path: Path) -> Set[str]:
    """加载已知因子字段"""
    if not factors_dict_path.exists():
        return set()
    
    with open(factors_dict_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    return set(data.get("factors", {}).keys())


def main():
    # 项目根目录
    root = Path(__file__).parent.parent
    rules_dir = root / "data" / "rules"
    factors_dict = root / "backend" / "schemas" / "factors.dictionary.json"
    output_dir = root / "openspec" / "changes" / "add-dream-factors-and-cross-domain-axes" / "notes"
    
    # 加载已知因子
    known_factors = load_known_factors(factors_dict)
    
    # 目标前缀
    target_prefixes = ["dream.", "dreamer.", "interpreter.", "evaluation.", "current_step.", "structural_event."]
    
    # 扫描所有规则文件
    all_fields_by_rule = []
    
    # 1. 明确的梦境规则
    for pattern in ["mlxj_*rules*.jsonl", "*dream*.jsonl"]:
        for jsonl_file in rules_dir.glob(f"**/{pattern}"):
            all_fields_by_rule.extend(extract_fields_from_jsonl(jsonl_file))
    
    # 2. 其他可能含梦境字段的规则
    for jsonl_file in rules_dir.glob("**/*.jsonl"):
        if jsonl_file.name.startswith("mlxj_"):
            continue  # 已处理
        
        # 快速扫描是否含目标前缀
        content = jsonl_file.read_text(encoding="utf-8")
        if any(prefix in content for prefix in target_prefixes):
            all_fields_by_rule.extend(extract_fields_from_jsonl(jsonl_file))
    
    # 按前缀分组并统计
    missing_by_prefix = defaultdict(list)
    
    for rule_id, file_name, fields in all_fields_by_rule:
        for field in fields:
            # 检查是否为目标前缀
            is_target = any(field.startswith(prefix) for prefix in target_prefixes)
            if not is_target:
                continue
            
            # 检查是否在字典中
            if field not in known_factors:
                prefix = field.split(".")[0] + "."
                missing_by_prefix[prefix].append({
                    "field": field,
                    "rule_id": rule_id,
                    "file": file_name
                })
    
    # 去重并排序
    for prefix in missing_by_prefix:
        seen = set()
        unique = []
        for item in missing_by_prefix[prefix]:
            key = (item["field"], item["rule_id"], item["file"])
            if key not in seen:
                seen.add(key)
                unique.append(item)
        missing_by_prefix[prefix] = sorted(unique, key=lambda x: (x["field"], x["rule_id"]))
    
    # 生成 Markdown 报告
    output_file = output_dir / "missing_factors_dream.md"
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# 梦境相关字段盘点：缺失因子清单\n\n")
        f.write("> 本文档由 `scripts/extract_dream_fields.py` 自动生成\n")
        f.write("> 用于 OpenSpec change: `add-dream-factors-and-cross-domain-axes` 步骤 1\n\n")
        
        f.write("## 概要统计\n\n")
        total_missing = sum(len(items) for items in missing_by_prefix.values())
        f.write(f"- **缺失字段总数（去重后）**: {total_missing}\n")
        f.write(f"- **涉及前缀**: {', '.join(sorted(missing_by_prefix.keys()))}\n\n")
        
        # 按前缀详细列出
        for prefix in sorted(missing_by_prefix.keys()):
            items = missing_by_prefix[prefix]
            f.write(f"## {prefix} 前缀\n\n")
            f.write(f"缺失字段数: **{len(items)}**\n\n")
            
            # 按字段名分组
            fields_dict = defaultdict(list)
            for item in items:
                fields_dict[item["field"]].append((item["rule_id"], item["file"]))
            
            for field_name in sorted(fields_dict.keys()):
                usages = fields_dict[field_name]
                f.write(f"### `{field_name}`\n\n")
                f.write(f"- **使用次数**: {len(usages)}\n")
                f.write(f"- **规则示例**:\n")
                
                # 最多列 5 个示例
                for rule_id, file_name in usages[:5]:
                    f.write(f"  - `{rule_id}` (文件: `{file_name}`)\n")
                
                if len(usages) > 5:
                    f.write(f"  - ... 及其他 {len(usages) - 5} 条规则\n")
                
                f.write("\n")
        
        f.write("---\n\n")
        f.write("## 后续步骤\n\n")
        f.write("1. 为每个前缀设计 Pydantic 模型（步骤 2）\n")
        f.write("2. 在 `docs/schema_deep_audit.md` 中定义字段语义\n")
        f.write("3. 更新 `backend/schemas/factors.dictionary.json`\n")
        f.write("4. 编写测试验证字段可访问性\n")
    
    print(f"✅ 报告已生成: {output_file}")
    print(f"   缺失字段总数: {total_missing}")
    print(f"   涉及前缀: {', '.join(sorted(missing_by_prefix.keys()))}")


if __name__ == "__main__":
    main()
