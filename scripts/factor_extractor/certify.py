"""Factor Certification CLI - 因子认证命令行工具

用法:
    python -m scripts.factor_extractor.certify [OPTIONS]

选项:
    --candidates, -c  候选因子目录 (默认: data/factor_ontology/candidates/)
    --ontology, -o    因子本体目录 (默认: 典籍/因子本体/)
    --output, -O      认证结果输出目录 (默认: data/factor_ontology/certified/)
    --verbose, -v     详细输出
    --help, -h        显示帮助
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

import yaml

from .certifier import FactorCertifier


def main():
    parser = argparse.ArgumentParser(
        description="认证候选因子，分配符合规范的因子ID"
    )
    parser.add_argument(
        "-c", "--candidates",
        default="data/factor_ontology/candidates",
        help="候选因子目录"
    )
    parser.add_argument(
        "-o", "--ontology",
        default="典籍/因子本体",
        help="因子本体目录"
    )
    parser.add_argument(
        "-O", "--output",
        default="data/factor_ontology/certified",
        help="认证结果输出目录"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="详细输出"
    )
    
    args = parser.parse_args()
    
    # 确定项目根目录
    script_path = Path(__file__).resolve()
    project_root = script_path.parent.parent.parent
    
    candidates_dir = project_root / args.candidates
    ontology_dir = project_root / args.ontology
    output_dir = project_root / args.output
    
    if not candidates_dir.exists():
        print(f"错误: 候选因子目录不存在: {candidates_dir}", file=sys.stderr)
        sys.exit(1)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"开始认证因子...")
    print(f"候选因子目录: {candidates_dir}")
    print(f"因子本体目录: {ontology_dir}")
    print(f"输出目录: {output_dir}")
    print("-" * 60)
    
    # 初始化认证器
    certifier = FactorCertifier(ontology_dir)
    print(f"已加载 {len(certifier.existing_ids)} 个已存在因子ID")
    
    # 统计
    total_certified = 0
    total_skipped = 0
    total_errors = 0
    results_summary = []
    
    # 处理每个候选文件
    for candidates_file in sorted(candidates_dir.glob("*_candidates.yaml")):
        system = candidates_file.stem.replace("_candidates", "")
        print(f"\n处理: {system}")
        
        result = certifier.certify_candidates(candidates_file)
        
        # 保存认证结果
        output_file = certifier.save_certified_factors(result, output_dir)
        
        print(f"  总候选数: {result.total_candidates}")
        print(f"  认证成功: {result.certified_count}")
        print(f"  跳过数量: {result.skipped_count}")
        
        if result.errors and args.verbose:
            print(f"  错误数量: {len(result.errors)}")
            for err in result.errors[:5]:
                print(f"    - {err}")
        
        total_certified += result.certified_count
        total_skipped += result.skipped_count
        total_errors += len(result.errors)
        
        results_summary.append({
            "system": system,
            "total_candidates": result.total_candidates,
            "certified": result.certified_count,
            "skipped": result.skipped_count,
            "errors": len(result.errors),
            "output_file": str(output_file),
        })
    
    # 输出汇总
    print("\n" + "=" * 60)
    print("认证完成!")
    print("=" * 60)
    print(f"总认证数: {total_certified}")
    print(f"总跳过数: {total_skipped}")
    print(f"总错误数: {total_errors}")
    
    # 保存汇总报告
    summary_file = output_dir / "certification_summary.json"
    summary = {
        "certification_time": datetime.now().isoformat(),
        "total_certified": total_certified,
        "total_skipped": total_skipped,
        "total_errors": total_errors,
        "by_system": results_summary,
    }
    
    with open(summary_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    
    print(f"\n汇总报告: {summary_file}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
