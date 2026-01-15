"""
Schema Extractor CLI - 命令行入口

使用方式:
    python -m schema_extractor extract <markdown_path> [--output <output_dir>]
    python -m schema_extractor batch <directory> [--output <output_dir>] [--exclude <book1,book2>]
    python -m schema_extractor validate <yaml_directory>
"""

import argparse
import sys
from pathlib import Path
from typing import List, Optional

from .extractors import extract_from_directory, extract_from_file
from .models import ExtractionResult
from .output import ReportGenerator, YAMLOutput


def cmd_extract(args):
    """提取单个文件"""
    file_path = Path(args.file)
    if not file_path.exists():
        print(f"❌ 文件不存在: {file_path}")
        sys.exit(1)
    
    output_dir = Path(args.output) if args.output else Path("data/semantics")
    
    print(f"📄 提取文件: {file_path}")
    result = extract_from_file(file_path, book_id=args.book_id)
    
    if result.errors:
        print(f"⚠️  发现 {len(result.errors)} 个错误")
        for error in result.errors[:5]:
            print(f"   - {error}")
    
    # 输出到YAML
    output = YAMLOutput(output_dir)
    written = output.write_result(result)
    
    print(f"✅ 提取完成:")
    print(f"   - 因子: {len(result.factors)}")
    print(f"   - 叙事素材: {len(result.snippets)}")
    print(f"   - 术语: {len(result.terms)}")
    print(f"   - 关系: {len(result.relations)}")
    print(f"   - 证据链: {len(result.evidence_chains)}")
    print(f"   - 跨体系映射: {len(result.cross_mappings)}")
    
    for category, path in written.items():
        print(f"   📁 {category}: {path}")


def cmd_batch(args):
    """批量提取目录"""
    directory = Path(args.directory)
    if not directory.exists():
        print(f"❌ 目录不存在: {directory}")
        sys.exit(1)
    
    output_dir = Path(args.output) if args.output else Path("data/semantics")
    
    # 解析排除列表
    exclude_books: List[str] = []
    if args.exclude:
        exclude_books = [b.strip() for b in args.exclude.split(",")]
    
    # 默认排除的书籍（只排除数据不完整的）
    default_excludes = [
        "记纂渊海",  # 内容不完整
        "collected works",  # 合集，不单独处理
        "the collected works",
        # 排除模板和说明文件
        "精校模板",
        "template",
        "readme",
        "审计报告",
        "schema工程说明",
        "典籍精校与结构化",
        "典籍结构化作业手册",
        "因子本体",
        "结构化提取",
    ]
    exclude_books.extend(default_excludes)
    
    print(f"📂 批量提取目录: {directory}")
    print(f"🚫 排除书籍: {', '.join(exclude_books)}")
    
    results = extract_from_directory(directory, exclude_books=exclude_books)
    
    if not results:
        print("⚠️  未找到可提取的文件")
        sys.exit(0)
    
    # 合并同一book_id的所有结果，然后输出YAML
    output = YAMLOutput(output_dir)
    total_written = 0
    
    for book_id, book_results in results.items():
        # 合并同一典籍的所有文件结果
        merged = ExtractionResult(
            source_file=", ".join(r.source_file for r in book_results),
            book_id=book_id,
        )
        
        # 使用set去重（仅对唯一标识去重，保留同ID不同标签的因子）
        seen_factor_keys = set()  # (factor_id, factor_label) 组合
        seen_snippet_ids = set()
        seen_term_keys = set()
        seen_relation_ids = set()
        seen_evidence_ids = set()
        seen_concept_ids = set()
        
        for result in book_results:
            # 合并因子（按factor_id+factor_label组合去重，保留同ID不同标签）
            for f in result.factors:
                key = (f.factor_id, f.factor_label)
                if key not in seen_factor_keys:
                    seen_factor_keys.add(key)
                    merged.factors.append(f)
            
            # 合并叙事素材（按snippet_id去重）
            for s in result.snippets:
                if s.snippet_id not in seen_snippet_ids:
                    seen_snippet_ids.add(s.snippet_id)
                    merged.snippets.append(s)
            
            # 合并术语（按中文术语+英文术语组合去重）
            for t in result.terms:
                key = (t.term_zh, t.term_en)
                if key not in seen_term_keys:
                    seen_term_keys.add(key)
                    merged.terms.append(t)
            
            # 合并关系（按relation_id去重）
            for r in result.relations:
                if r.relation_id not in seen_relation_ids:
                    seen_relation_ids.add(r.relation_id)
                    merged.relations.append(r)
            
            # 合并证据链（按evidence_id去重）
            for e in result.evidence_chains:
                if e.evidence_id not in seen_evidence_ids:
                    seen_evidence_ids.add(e.evidence_id)
                    merged.evidence_chains.append(e)
            
            # 合并跨体系映射（按concept_id去重）
            for c in result.cross_mappings:
                if c.concept_id not in seen_concept_ids:
                    seen_concept_ids.add(c.concept_id)
                    merged.cross_mappings.append(c)
            
            # 合并错误和警告
            merged.errors.extend(result.errors)
            merged.warnings.extend(result.warnings)
        
        # 写入合并后的结果
        written = output.write_result(merged)
        total_written += len(written)
    
    # 生成报告
    report_gen = ReportGenerator(output_dir)
    report_path = report_gen.write_report(results)
    
    # 统计
    total_factors = sum(len(r.factors) for rs in results.values() for r in rs)
    total_snippets = sum(len(r.snippets) for rs in results.values() for r in rs)
    total_terms = sum(len(r.terms) for rs in results.values() for r in rs)
    total_relations = sum(len(r.relations) for rs in results.values() for r in rs)
    total_evidence = sum(len(r.evidence_chains) for rs in results.values() for r in rs)
    total_cross = sum(len(r.cross_mappings) for rs in results.values() for r in rs)
    total_errors = sum(len(r.errors) for rs in results.values() for r in rs)
    
    print(f"\n✅ 批量提取完成!")
    print(f"   📚 典籍数: {len(results)}")
    print(f"   📄 文件数: {sum(len(rs) for rs in results.values())}")
    print(f"   ──────────────────")
    print(f"   🔹 因子: {total_factors}")
    print(f"   🔹 叙事素材: {total_snippets}")
    print(f"   🔹 术语: {total_terms}")
    print(f"   🔹 关系: {total_relations}")
    print(f"   🔹 证据链: {total_evidence}")
    print(f"   🔹 跨体系映射: {total_cross}")
    print(f"   ──────────────────")
    if total_errors > 0:
        print(f"   ⚠️  错误: {total_errors}")
    print(f"   📝 报告: {report_path}")


def cmd_validate(args):
    """验证YAML文件"""
    yaml_dir = Path(args.yaml_dir)
    if not yaml_dir.exists():
        print(f"❌ 目录不存在: {yaml_dir}")
        sys.exit(1)
    
    import yaml as yaml_lib
    from .models import (
        ConfigFactor,
        ConfigRelation,
        CrossSystemMapping,
        EvidenceChainEntry,
        NarrativeSnippet,
        TermGlossary,
    )
    
    errors = []
    validated = 0
    
    # 验证各类YAML文件
    for yaml_file in yaml_dir.rglob("*.yaml"):
        try:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                data = yaml_lib.safe_load(f)
            
            # 根据文件路径确定类型并验证
            if "factors" in str(yaml_file):
                for item in data.get("factors", []):
                    ConfigFactor(**item)
                    validated += 1
            elif "snippets" in str(yaml_file):
                for item in data.get("snippets", []):
                    NarrativeSnippet(**item)
                    validated += 1
            elif "terms" in str(yaml_file):
                for item in data.get("terms", []):
                    TermGlossary(**item)
                    validated += 1
            elif "relations" in str(yaml_file):
                for item in data.get("relations", []):
                    ConfigRelation(**item)
                    validated += 1
            elif "evidence" in str(yaml_file):
                for item in data.get("evidence_chains", []):
                    EvidenceChainEntry(**item)
                    validated += 1
            elif "cross_system" in str(yaml_file):
                for item in data.get("cross_mappings", []):
                    CrossSystemMapping(**item)
                    validated += 1
                    
        except Exception as e:
            errors.append(f"{yaml_file}: {str(e)}")
    
    if errors:
        print(f"❌ 验证失败! 发现 {len(errors)} 个错误:")
        for error in errors[:20]:
            print(f"   - {error}")
        if len(errors) > 20:
            print(f"   ... 还有 {len(errors) - 20} 个错误")
        sys.exit(1)
    else:
        print(f"✅ 验证通过! 共验证 {validated} 条记录")


def main():
    parser = argparse.ArgumentParser(
        description="Schema Extractor - 从精校Markdown提取结构化数据",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python -m schema_extractor extract 典籍/中文典籍/滴天髓/编辑/滴天髓_完整规范化_上卷.md
  python -m schema_extractor batch 典籍/中文典籍 --output data/semantics
  python -m schema_extractor batch 典籍/ --exclude "梦林玄解,记纂渊海"
  python -m schema_extractor validate data/semantics
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="子命令")
    
    # extract 命令
    extract_parser = subparsers.add_parser("extract", help="提取单个文件")
    extract_parser.add_argument("file", help="Markdown文件路径")
    extract_parser.add_argument("--output", "-o", help="输出目录", default="data/schema_staging")
    extract_parser.add_argument("--book-id", help="指定book_id（默认从路径推断）")
    extract_parser.set_defaults(func=cmd_extract)
    
    # batch 命令
    batch_parser = subparsers.add_parser("batch", help="批量提取目录")
    batch_parser.add_argument("directory", help="目录路径")
    batch_parser.add_argument("--output", "-o", help="输出目录", default="data/schema_staging")
    batch_parser.add_argument("--exclude", "-e", help="排除的书籍，逗号分隔")
    batch_parser.set_defaults(func=cmd_batch)
    
    # validate 命令
    validate_parser = subparsers.add_parser("validate", help="验证YAML文件")
    validate_parser.add_argument("yaml_dir", help="YAML目录路径")
    validate_parser.set_defaults(func=cmd_validate)
    
    args = parser.parse_args()
    
    if args.command is None:
        parser.print_help()
        sys.exit(0)
    
    args.func(args)


if __name__ == "__main__":
    main()
