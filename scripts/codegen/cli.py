"""
Codegen CLI - 代码生成命令行接口

支持命令:
- compile: 编译配置文件
- validate: 校验配置文件
- clean: 清理孤儿文件
- status: 查看编译状态
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import List, Optional

from scripts.codegen.base import BaseCodeGenerator
from scripts.codegen.exceptions import CodegenError, ValidationError
from scripts.codegen.factor_generator import FactorCodeGenerator
from scripts.codegen.manifest import CodegenManifest
from scripts.codegen.rule_generator import RuleCodeGenerator
from scripts.codegen.semantic_generator import SemanticCodeGenerator

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)


def cmd_compile(args: argparse.Namespace) -> int:
    """编译命令"""
    gen_type = args.type
    source = Path(args.source)
    output_dir = Path(args.output) if args.output else None
    
    if not source.exists():
        logger.error(f"Source not found: {source}")
        return 1
    
    try:
        if gen_type == "rule":
            generator = RuleCodeGenerator(output_dir)
            return _compile_rules(generator, source, args)
        
        elif gen_type == "factor":
            generator = FactorCodeGenerator(output_dir)
            return _compile_factors(generator, source, args)
        
        elif gen_type == "semantic":
            generator = SemanticCodeGenerator(output_dir)
            return _compile_semantics(generator, source, args)
        
        else:
            logger.error(f"Unknown type: {gen_type}")
            return 1
    
    except CodegenError as e:
        logger.error(str(e))
        return 1


def _compile_rules(
    generator: RuleCodeGenerator,
    source: Path,
    args: argparse.Namespace
) -> int:
    """编译规则"""
    if source.is_file():
        # 单文件编译
        with open(source, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        if isinstance(data, list):
            # 批量编译
            for rule_data in data:
                _compile_single_rule(generator, rule_data, source)
        else:
            _compile_single_rule(generator, data, source)
    
    elif source.is_dir():
        # 目录编译
        for json_file in source.glob("*.json"):
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            if isinstance(data, list):
                for rule_data in data:
                    _compile_single_rule(generator, rule_data, json_file)
            else:
                _compile_single_rule(generator, data, json_file)
    
    logger.info("Rules compilation completed")
    return 0


def _compile_single_rule(
    generator: RuleCodeGenerator,
    data: dict,
    source_file: Path
) -> None:
    """编译单条规则"""
    rule_id = data.get("rule_id", "unknown")
    
    errors = generator.validate(data)
    if errors:
        raise ValidationError(
            f"Validation failed for rule {rule_id}",
            errors=errors,
            source_file=str(source_file)
        )
    
    code = generator.compile(data)
    code = generator.format_code(code)
    generator.verify_syntax(code)
    
    filename = f"{rule_id}.py"
    filepath = generator.save(code, filename)
    
    logger.info(f"Compiled rule: {rule_id} -> {filepath}")


def _compile_factors(
    generator: FactorCodeGenerator,
    source: Path,
    args: argparse.Namespace
) -> int:
    """编译因子"""
    engine_id = args.engine_id or source.stem
    version = args.version or "1.0.0"
    
    if source.suffix == ".jsonl":
        code = generator.compile_jsonl_file(source, engine_id, version)
    else:
        with open(source, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        if isinstance(data, list):
            code = generator.compile_batch(data, engine_id, version)
        else:
            raise ValidationError(
                "Factor source must be JSONL or JSON array",
                errors=["Invalid format"],
                source_file=str(source)
            )
    
    code = generator.format_code(code)
    generator.verify_syntax(code)
    
    filename = f"{engine_id}_factors_v{version.replace('.', '_')}.py"
    filepath = generator.save(code, filename)
    
    logger.info(f"Compiled factors: {engine_id} -> {filepath}")
    return 0


def _compile_semantics(
    generator: SemanticCodeGenerator,
    source: Path,
    args: argparse.Namespace
) -> int:
    """编译语义"""
    semantic_id = args.semantic_id or source.stem
    engine_id = args.engine_id or "unknown"
    version = args.version or "1.0.0"
    
    if source.suffix == ".md":
        code = generator.compile_markdown_file(source, semantic_id, engine_id, version)
    else:
        with open(source, "r", encoding="utf-8") as f:
            data = json.load(f)
        code = generator.compile(data)
    
    code = generator.format_code(code)
    generator.verify_syntax(code)
    
    filename = f"{semantic_id}_semantics_v{version.replace('.', '_')}.py"
    filepath = generator.save(code, filename)
    
    logger.info(f"Compiled semantics: {semantic_id} -> {filepath}")
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    """校验命令"""
    gen_type = args.type
    source = Path(args.source)
    
    if not source.exists():
        logger.error(f"Source not found: {source}")
        return 1
    
    try:
        if gen_type == "rule":
            generator = RuleCodeGenerator()
        elif gen_type == "factor":
            generator = FactorCodeGenerator()
        elif gen_type == "semantic":
            generator = SemanticCodeGenerator()
        else:
            logger.error(f"Unknown type: {gen_type}")
            return 1
        
        with open(source, "r", encoding="utf-8") as f:
            if source.suffix == ".jsonl":
                lines = f.readlines()
                for i, line in enumerate(lines, 1):
                    if not line.strip() or line.startswith("#"):
                        continue
                    data = json.loads(line)
                    errors = generator.validate(data)
                    if errors:
                        logger.error(f"Line {i}: {errors}")
                        return 1
            else:
                data = json.load(f)
                if isinstance(data, list):
                    for i, item in enumerate(data):
                        errors = generator.validate(item)
                        if errors:
                            logger.error(f"Item {i}: {errors}")
                            return 1
                else:
                    errors = generator.validate(data)
                    if errors:
                        logger.error(f"Validation errors: {errors}")
                        return 1
        
        logger.info("Validation passed")
        return 0
    
    except Exception as e:
        logger.error(f"Validation failed: {e}")
        return 1


def cmd_clean(args: argparse.Namespace) -> int:
    """清理命令"""
    output_dir = Path(args.output) if args.output else Path("backend/generated")
    dry_run = args.dry_run
    
    manifest = CodegenManifest(output_dir)
    orphans = manifest.clean_orphans(dry_run=dry_run)
    
    if orphans:
        action = "Would delete" if dry_run else "Deleted"
        for orphan in orphans:
            logger.info(f"{action}: {orphan}")
        logger.info(f"Total: {len(orphans)} orphan(s)")
    else:
        logger.info("No orphans found")
    
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    """状态命令"""
    output_dir = Path(args.output) if args.output else Path("backend/generated")
    
    manifest = CodegenManifest(output_dir)
    status = manifest.get_status()
    
    print(f"Manifest: {status['manifest_path']}")
    print(f"Total entries: {status['total_entries']}")
    print(f"  Rules: {status['by_type']['rule']}")
    print(f"  Factors: {status['by_type']['factor']}")
    print(f"  Semantics: {status['by_type']['semantic']}")
    print(f"Orphans: {status['orphans']}")
    
    return 0


def cmd_migrate(args: argparse.Namespace) -> int:
    """
    迁移命令 - Phase 2 语义层迁移
    
    对齐 tasks.md 1.5
    """
    from scripts.codegen.semantic_generator import SemanticMigrationTool
    
    tool = SemanticMigrationTool()
    dry_run = args.dry_run
    
    try:
        if args.book:
            # 迁移单本书籍
            logger.info(f"Migrating book: {args.book}")
            result = tool.migrate_book(args.book, dry_run=dry_run)
            logger.info(f"Result: {result.status.value}, {result.entries_success}/{result.entries_total} entries")
            
        elif args.engine:
            # 迁移整个体系
            logger.info(f"Migrating engine: {args.engine}")
            results = tool.migrate_engine(args.engine, dry_run=dry_run)
            for book_id, result in results.items():
                logger.info(f"  {book_id}: {result.status.value}, {result.entries_success}/{result.entries_total} entries")
            
        elif args.all:
            # 迁移所有 24 本典籍
            logger.info("Migrating all 24 books...")
            results = tool.migrate_all(dry_run=dry_run, parallel=args.parallel)
            for book_id, result in results.items():
                status_icon = "✅" if result.status.value == "success" else "⚠️" if result.status.value == "partial" else "❌"
                logger.info(f"  {status_icon} {book_id}: {result.entries_success}/{result.entries_total} entries")
        
        else:
            logger.error("Must specify --book, --engine, or --all")
            return 1
        
        # 打印报告
        if args.report:
            tool.print_report()
        else:
            # 简短摘要
            report = tool.get_report()
            print(f"\n=== Migration Summary ===")
            print(f"Books: {report.migrated_books}/{report.total_books}")
            print(f"Coverage: {report.coverage_percentage:.1f}%")
            print(f"Success Rate: {report.overall_success_rate:.1%}")
            if report.total_errors > 0:
                print(f"Errors: {report.total_errors}")
            if report.total_warnings > 0:
                print(f"Warnings: {report.total_warnings}")
        
        return 0
        
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        return 1


def main(argv: Optional[List[str]] = None) -> int:
    """CLI 入口"""
    parser = argparse.ArgumentParser(
        prog="codegen",
        description="LucidSelf Code Generation Pipeline"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # compile 命令
    compile_parser = subparsers.add_parser("compile", help="Compile config to Python")
    compile_parser.add_argument(
        "type",
        choices=["rule", "factor", "semantic"],
        help="Generator type"
    )
    compile_parser.add_argument("source", help="Source file or directory")
    compile_parser.add_argument("-o", "--output", help="Output directory")
    compile_parser.add_argument("--engine-id", help="Engine ID (for factors/semantics)")
    compile_parser.add_argument("--semantic-id", help="Semantic ID")
    compile_parser.add_argument("--version", default="1.0.0", help="Version")
    compile_parser.set_defaults(func=cmd_compile)
    
    # validate 命令
    validate_parser = subparsers.add_parser("validate", help="Validate config")
    validate_parser.add_argument(
        "type",
        choices=["rule", "factor", "semantic"],
        help="Generator type"
    )
    validate_parser.add_argument("source", help="Source file")
    validate_parser.set_defaults(func=cmd_validate)
    
    # clean 命令
    clean_parser = subparsers.add_parser("clean", help="Clean orphan files")
    clean_parser.add_argument("-o", "--output", help="Generated directory")
    clean_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only show what would be deleted"
    )
    clean_parser.set_defaults(func=cmd_clean)
    
    # status 命令
    status_parser = subparsers.add_parser("status", help="Show compilation status")
    status_parser.add_argument("-o", "--output", help="Generated directory")
    status_parser.set_defaults(func=cmd_status)
    
    # migrate 命令 (Phase 2 语义层迁移)
    migrate_parser = subparsers.add_parser(
        "migrate",
        help="Phase 2 semantic migration (24 books)"
    )
    migrate_parser.add_argument(
        "--book",
        help="Migrate single book by book_id (e.g., dts, sanming, waite_tarot)"
    )
    migrate_parser.add_argument(
        "--engine",
        choices=["bazi", "ziwei", "tarot", "astro", "dream", "yijing", "psych"],
        help="Migrate all books for an engine"
    )
    migrate_parser.add_argument(
        "--all",
        action="store_true",
        help="Migrate all 24 books"
    )
    migrate_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only validate, do not generate files"
    )
    migrate_parser.add_argument(
        "--parallel",
        type=int,
        default=1,
        help="Parallel compilation workers (default: 1)"
    )
    migrate_parser.add_argument(
        "--report",
        action="store_true",
        help="Print full migration report"
    )
    migrate_parser.set_defaults(func=cmd_migrate)
    
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
