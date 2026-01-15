"""Factor Document Updater CLI - 精校文档更新命令行工具

用法:
    python -m scripts.factor_extractor.update_docs [OPTIONS]

选项:
    --root, -r        根目录 (默认: 典籍)
    --certified, -c   认证因子目录 (默认: data/factor_ontology/certified/)
    --dry-run         模拟运行，不实际修改文件
    --verbose, -v     详细输出
    --help, -h        显示帮助
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

from .updater import FactorUpdater


def main():
    parser = argparse.ArgumentParser(
        description="更新精校文档中的因子状态"
    )
    parser.add_argument(
        "-r", "--root",
        default="典籍",
        help="根目录"
    )
    parser.add_argument(
        "-c", "--certified",
        default="data/factor_ontology/certified",
        help="认证因子目录"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="模拟运行，不实际修改文件"
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
    
    root_dir = project_root / args.root
    certified_dir = project_root / args.certified
    
    if not root_dir.exists():
        print(f"错误: 根目录不存在: {root_dir}", file=sys.stderr)
        sys.exit(1)
    
    if not certified_dir.exists():
        print(f"错误: 认证因子目录不存在: {certified_dir}", file=sys.stderr)
        sys.exit(1)
    
    mode = "[模拟运行]" if args.dry_run else ""
    print(f"开始更新精校文档 {mode}")
    print(f"根目录: {root_dir}")
    print(f"认证因子目录: {certified_dir}")
    print("-" * 60)
    
    # 初始化更新器
    updater = FactorUpdater(certified_dir, dry_run=args.dry_run)
    print(f"已加载 {len(updater.factor_mapping)} 个因子映射")
    
    # 执行更新
    report = updater.update_all(root_dir)
    
    # 输出结果
    print("\n" + "=" * 60)
    print("更新完成!")
    print("=" * 60)
    print(f"处理文件数: {len(report.results)}")
    print(f"更新文件数: {report.files_updated}")
    print(f"更新因子块: {report.total_blocks}")
    print(f"更新因子数: {report.total_factors_updated}")
    
    if args.verbose and report.results:
        print("\n更新详情:")
        for result in report.results:
            if result.factors_updated > 0:
                print(f"  {Path(result.file_path).name}: {result.factors_updated} 因子")
    
    if report.errors:
        print(f"\n警告: {len(report.errors)} 个错误")
        for err in report.errors[:10]:
            print(f"  - {err}")
    
    if args.dry_run:
        print("\n[模拟运行] 未实际修改文件")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
