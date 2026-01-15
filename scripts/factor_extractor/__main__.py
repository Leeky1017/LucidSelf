"""Factor Extractor CLI - 因子提取命令行工具

用法:
    python -m scripts.factor_extractor [OPTIONS] [ROOT_DIR]

选项:
    --output, -o     输出目录 (默认: data/factor_ontology/candidates/)
    --verbose, -v    详细输出
    --json           同时输出JSON格式报告
    --help, -h       显示帮助
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

import yaml

from .extractor import FactorExtractor
from .models import DivinationSystem


def main():
    parser = argparse.ArgumentParser(
        description="从精校文档中提取因子表格"
    )
    parser.add_argument(
        "root_dir",
        nargs="?",
        default="典籍",
        help="根目录路径 (默认: 典籍)"
    )
    parser.add_argument(
        "-o", "--output",
        default="data/factor_ontology/candidates",
        help="输出目录 (默认: data/factor_ontology/candidates/)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="详细输出"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="同时输出JSON格式报告"
    )
    
    args = parser.parse_args()
    
    # 确定项目根目录
    script_path = Path(__file__).resolve()
    project_root = script_path.parent.parent.parent
    
    root_dir = project_root / args.root_dir
    output_dir = project_root / args.output
    
    if not root_dir.exists():
        print(f"错误: 目录不存在: {root_dir}", file=sys.stderr)
        sys.exit(1)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"开始提取因子...")
    print(f"根目录: {root_dir}")
    print(f"输出目录: {output_dir}")
    print("-" * 60)
    
    # 执行提取
    extractor = FactorExtractor(verbose=args.verbose)
    report = extractor.extract_all(root_dir)
    
    # 输出统计
    print("\n" + "=" * 60)
    print("提取完成!")
    print("=" * 60)
    print(f"处理文件数: {report.processed_files}")
    print(f"因子块数: {report.total_blocks}")
    print(f"总因子数: {report.total_factors}")
    print(f"  - existing: {report.existing_factors}")
    print(f"  - new_candidate: {report.new_candidate_factors}")
    
    if report.errors:
        print(f"\n警告: {len(report.errors)} 个解析错误")
    
    # 按体系分类输出
    print("\n按体系分类:")
    for system, count in sorted(report.factors_by_system.items(), key=lambda x: -x[1]):
        print(f"  - {system}: {count}")
    
    # 高频new_candidate类型
    print("\n高频new_candidate类型 (Top 20):")
    for ftype, count in list(report.new_candidate_by_type.items())[:20]:
        print(f"  - {ftype}: {count}")
    
    # 收集所有因子
    all_factors = []
    for result in report.results:
        all_factors.extend(result.factors)
    
    # 按体系分类并输出YAML
    by_system = extractor.classify_by_system(all_factors)
    for system, factors in by_system.items():
        if system == "unknown":
            continue
        
        # 分离existing和new_candidate
        by_status = extractor.classify_by_status(factors)
        
        # 只输出new_candidate
        candidates = by_status["new_candidate"]
        if not candidates:
            continue
        
        output_file = output_dir / f"{system}_candidates.yaml"
        
        # 转换为字典列表
        candidates_data = [f.to_dict() for f in candidates]
        
        # 按类型分组
        by_type = {}
        for c in candidates_data:
            ftype = c["factor_type"]
            if ftype not in by_type:
                by_type[ftype] = []
            by_type[ftype].append(c)
        
        output_data = {
            "system": system,
            "total_candidates": len(candidates),
            "extraction_time": report.extraction_time,
            "by_type": by_type,
        }
        
        with open(output_file, "w", encoding="utf-8") as f:
            yaml.dump(
                output_data,
                f,
                allow_unicode=True,
                default_flow_style=False,
                sort_keys=False
            )
        
        print(f"\n已输出: {output_file} ({len(candidates)} 个候选)")
    
    # 输出提取报告
    report_file = output_dir / "extraction_report.json"
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(report.to_dict(), f, ensure_ascii=False, indent=2)
    
    print(f"\n提取报告: {report_file}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
