"""
CLI - 命令行接口

提供Logic Chain Builder的命令行入口。

Usage:
    python -m scripts.logic_chain_builder build <book_id>
    python -m scripts.logic_chain_builder batch
    python -m scripts.logic_chain_builder validate <book_id>
    python -m scripts.logic_chain_builder list
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import Optional

import yaml

from scripts.logic_chain_builder.constants import TARGET_BOOKS, OUTPUT_DIR
from scripts.logic_chain_builder.logging_config import setup_logging, get_logger
from scripts.logic_chain_builder.builder import LogicChainBuilder
from scripts.logic_chain_builder.validator import LogicChainValidator
from scripts.logic_chain_builder.writer import LogicChainWriter
from scripts.logic_chain_builder.loader import SchemaLoader, SchemaLoadError
from scripts.logic_chain_builder.models import LogicChain


def cmd_build(args) -> int:
    """
    构建单本书籍的逻辑链
    
    Wire up LogicChainBuilder, LogicChainValidator, and LogicChainWriter.
    Build logic chain for single book, validate and auto-repair if needed,
    then write output to YAML file.
    
    **Validates: Requirements 1.1, 1.2, 7.1**
    """
    logger = get_logger()
    book_id = args.book_id
    
    logger.info(f"📚 开始构建逻辑链: {book_id}")
    
    try:
        # 1. Build the logic chain
        builder = LogicChainBuilder(book_id)
        chain = builder.build()
        logger.info(f"✅ 构建完成: {len(chain.nodes)} 节点, {len(chain.edges)} 边")
        
        # 2. Validate the chain
        validator = LogicChainValidator()
        result = validator.validate(chain)
        
        if result.warnings:
            for warning in result.warnings:
                logger.warning(f"⚠️  {warning}")
        
        # 3. Auto-repair if validation failed
        if not result.valid:
            logger.warning(f"❌ 验证失败，发现 {len(result.errors)} 个错误，尝试自动修复...")
            for error in result.errors:
                logger.warning(f"   - {error.error_type}: {error.message}")
            
            chain, repairs = validator.auto_repair(chain, result.errors)
            
            if repairs:
                logger.info(f"🔧 自动修复完成，共 {len(repairs)} 项修复:")
                for repair in repairs:
                    logger.info(f"   - {repair}")
            
            # Re-validate after repair
            result = validator.validate(chain)
            if not result.valid:
                logger.error("❌ 自动修复后仍有验证错误:")
                for error in result.errors:
                    logger.error(f"   - {error.error_type}: {error.message}")
                return 1
            else:
                logger.info("✅ 自动修复后验证通过")
        else:
            logger.info("✅ 验证通过")
        
        # 4. Write output to YAML file
        writer = LogicChainWriter()
        output_path = writer.write(chain)
        logger.info(f"📝 已写入: {output_path}")
        
        # 5. Print summary
        print(f"\n{'='*60}")
        print(f"逻辑链构建完成: {book_id}")
        print(f"{'='*60}")
        print(f"  节点数: {len(chain.nodes)}")
        print(f"  边数: {len(chain.edges)}")
        print(f"  入口节点: {len(chain.entry_nodes)}")
        print(f"  终端节点: {len(chain.terminal_nodes)}")
        print(f"  输出文件: {output_path}")
        print(f"{'='*60}\n")
        
        return 0
        
    except FileNotFoundError as e:
        logger.error(f"❌ 文件未找到: {e}")
        return 1
    except SchemaLoadError as e:
        logger.error(f"❌ Schema加载错误: {e}")
        return 1
    except Exception as e:
        logger.error(f"❌ 构建失败: {e}")
        logger.exception("详细错误信息:")
        return 1


def cmd_batch(args) -> int:
    """
    批量构建所有书籍的逻辑链
    
    Batch orchestration for all 21 books:
    - Scan data/schema_staging/snippets/ for all book_ids
    - Verify each book has both snippets and relations files
    - Process all 21 books sequentially
    - Continue on individual book failure
    - Collect success/failure status for each book
    - Generate BuildReport with all statistics
    - Verify exactly 21 logic chain files exist after batch run
    
    **Validates: Requirements 8.1, 8.2, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6**
    """
    logger = get_logger()
    
    # Import report generator and quality scorer for batch processing
    from scripts.logic_chain_builder.report import BuildReportGenerator
    from scripts.logic_chain_builder.models import BookStats, BookQualityScores
    from scripts.logic_chain_builder.quality_scorer import LogicChainQualityScorer
    
    logger.info(f"📚 开始批量构建逻辑链，共 {len(TARGET_BOOKS)} 本书籍")
    
    # Initialize components
    loader = SchemaLoader()
    validator = LogicChainValidator()
    writer = LogicChainWriter()
    report_generator = BuildReportGenerator()
    quality_scorer = LogicChainQualityScorer()
    
    # Step 1: Discover all book_ids from snippets directory (Requirement 9.1)
    available_books = loader.list_available_books()
    logger.info(f"发现 {len(available_books)} 本可处理的书籍（同时拥有snippets和relations文件）")
    
    # Step 2: Verify each book_id has both snippets and relations files (Requirement 9.2)
    missing_books = []
    for book_id in TARGET_BOOKS:
        if book_id not in available_books:
            missing_books.append(book_id)
            logger.warning(f"书籍 {book_id} 缺少snippets或relations文件")
    
    if missing_books:
        logger.warning(f"共 {len(missing_books)} 本书籍缺少必要文件: {missing_books}")
    
    # Track statistics
    book_stats_list = []
    successful = 0
    failed = 0
    skipped = 0
    
    # Progress bar width
    bar_width = 40
    
    print(f"\n{'='*60}")
    print(f"批量构建逻辑链 - {len(TARGET_BOOKS)} 本书籍")
    print(f"{'='*60}")
    print(f"可处理书籍: {len(available_books)}/{len(TARGET_BOOKS)}")
    print(f"{'='*60}\n")
    
    # Step 3: Process all 21 books sequentially (Requirement 9.3)
    for i, book_id in enumerate(TARGET_BOOKS):
        # Progress bar
        progress = (i + 1) / len(TARGET_BOOKS)
        filled = int(bar_width * progress)
        bar = '█' * filled + '░' * (bar_width - filled)
        print(f"\r[{bar}] {i+1}/{len(TARGET_BOOKS)} - {book_id[:30]:<30}", end='', flush=True)
        
        # Step 4: Continue on individual book failure (Requirement 9.5)
        try:
            # Check if source files exist
            if book_id not in available_books:
                logger.warning(f"跳过 {book_id}: 缺少snippets或relations文件")
                book_stats = BookStats(
                    book_id=book_id,
                    snippet_count=0,
                    node_count=0,
                    edge_count=0,
                    coverage=0.0,
                    orphan_snippets=[],
                    status="skipped",
                    error_message="Missing snippets or relations file"
                )
                book_stats_list.append(book_stats)
                skipped += 1
                continue
            
            # Build logic chain
            builder = LogicChainBuilder(book_id)
            chain = builder.build()
            
            # Validate
            result = validator.validate(chain)
            
            # Auto-repair if needed
            if not result.valid:
                chain, repairs = validator.auto_repair(chain, result.errors)
                result = validator.validate(chain)
            
            if not result.valid:
                # Still invalid after repair
                error_msg = "; ".join([e.message for e in result.errors[:3]])
                book_stats = BookStats(
                    book_id=book_id,
                    snippet_count=chain.metadata.snippet_count,
                    node_count=len(chain.nodes),
                    edge_count=len(chain.edges),
                    coverage=0.0,
                    orphan_snippets=[],
                    status="failed",
                    error_message=f"Validation failed: {error_msg}"
                )
                book_stats_list.append(book_stats)
                failed += 1
                continue
            
            # Write output
            writer.write(chain)
            
            # Calculate coverage and quality scores
            snippets = loader.load_snippets(book_id)
            total_snippet_ids = {s.snippet_id for s in snippets}
            
            # Calculate quality scores (Requirement 12.5)
            quality_report = quality_scorer.score(chain, total_snippet_count=len(total_snippet_ids))
            quality_scores = BookQualityScores(
                connectivity=quality_report.connectivity,
                argument_completeness=quality_report.argument_completeness,
                orphan_ratio=quality_report.orphan_ratio,
                cycle_count=quality_report.cycle_count,
                connectivity_pass=quality_report.connectivity_pass,
                argument_completeness_pass=quality_report.argument_completeness_pass,
                orphan_ratio_pass=quality_report.orphan_ratio_pass,
                overall_pass=quality_report.passes_threshold(),
            )
            
            book_stats = report_generator.create_book_stats(
                book_id=book_id,
                chain=chain,
                total_snippet_ids=total_snippet_ids,
                status="success",
                quality_scores=quality_scores,
            )
            book_stats_list.append(book_stats)
            successful += 1
            
        except FileNotFoundError as e:
            book_stats = BookStats(
                book_id=book_id,
                snippet_count=0,
                node_count=0,
                edge_count=0,
                coverage=0.0,
                orphan_snippets=[],
                status="failed",
                error_message=str(e)
            )
            book_stats_list.append(book_stats)
            failed += 1
            
        except Exception as e:
            logger.error(f"处理 {book_id} 时出错: {e}")
            book_stats = BookStats(
                book_id=book_id,
                snippet_count=0,
                node_count=0,
                edge_count=0,
                coverage=0.0,
                orphan_snippets=[],
                status="failed",
                error_message=str(e)
            )
            book_stats_list.append(book_stats)
            failed += 1
    
    # Clear progress bar line
    print()
    
    # Step 5: Verify exactly 21 logic chain files exist (Requirement 9.4)
    output_dir = Path(OUTPUT_DIR)
    existing_chain_files = list(output_dir.glob("*.yaml")) if output_dir.exists() else []
    # Filter out build_report.md and other non-chain files
    chain_files = [f for f in existing_chain_files if not f.name.startswith("build_")]
    chain_file_count = len(chain_files)
    
    completeness_verified = chain_file_count == len(TARGET_BOOKS)
    if not completeness_verified:
        missing_count = len(TARGET_BOOKS) - chain_file_count
        report_generator.add_warning(
            f"Completeness verification failed: Expected {len(TARGET_BOOKS)} logic chain files, "
            f"found {chain_file_count} (missing {missing_count})"
        )
        logger.warning(f"完整性验证失败: 期望 {len(TARGET_BOOKS)} 个逻辑链文件，实际 {chain_file_count} 个")
    else:
        logger.info(f"完整性验证通过: {chain_file_count} 个逻辑链文件")
    
    # Step 6: Generate and write build report with per-book summary (Requirement 9.6)
    report = report_generator.generate(book_stats_list)
    report_path = report_generator.write(report)
    
    # Print summary statistics
    print(f"\n{'='*60}")
    print(f"批量构建完成")
    print(f"{'='*60}")
    print(f"  ✅ 成功: {successful}")
    print(f"  ❌ 失败: {failed}")
    print(f"  ⏭️  跳过: {skipped}")
    print(f"  📊 总计: {len(TARGET_BOOKS)}")
    print(f"\n  📁 逻辑链文件: {chain_file_count}/{len(TARGET_BOOKS)}")
    print(f"  {'✅' if completeness_verified else '❌'} 完整性验证: {'通过' if completeness_verified else '失败'}")
    print(f"\n  📝 构建报告: {report_path}")
    
    # Aggregate statistics
    total_nodes = sum(s.node_count for s in book_stats_list)
    total_edges = sum(s.edge_count for s in book_stats_list)
    total_snippets = sum(s.snippet_count for s in book_stats_list)
    avg_coverage = (
        sum(s.coverage for s in book_stats_list if s.status == "success") / successful
        if successful > 0 else 0.0
    )
    
    print(f"\n  📈 聚合统计:")
    print(f"     总节点数: {total_nodes}")
    print(f"     总边数: {total_edges}")
    print(f"     总素材数: {total_snippets}")
    print(f"     平均覆盖率: {avg_coverage:.1%}")
    
    # Quality score summary (Requirement 12.5)
    books_with_quality = [s for s in book_stats_list if s.quality_scores is not None]
    if books_with_quality:
        passing_quality = sum(1 for s in books_with_quality if s.quality_scores.overall_pass)
        print(f"\n  📊 质量评分:")
        print(f"     通过质量阈值: {passing_quality}/{len(books_with_quality)}")
        
        failing_books = [s for s in books_with_quality if not s.quality_scores.overall_pass]
        if failing_books:
            print(f"     ⚠️  未达标书籍: {', '.join(s.book_id for s in failing_books[:5])}")
            if len(failing_books) > 5:
                print(f"        ... 及其他 {len(failing_books) - 5} 本")
    
    print(f"{'='*60}\n")
    
    # Return non-zero if any failures or completeness check failed
    return 0 if (failed == 0 and completeness_verified) else 1


def cmd_validate(args) -> int:
    """
    验证逻辑链
    
    Load existing logic chain from YAML and run validation, report results.
    
    **Validates: Requirements 6.1, 6.2, 6.3, 6.4**
    """
    logger = get_logger()
    book_id = args.book_id
    
    logger.info(f"🔍 验证逻辑链: {book_id}")
    
    # 1. Load existing logic chain from YAML
    yaml_path = Path(OUTPUT_DIR) / f"{book_id}.yaml"
    
    if not yaml_path.exists():
        logger.error(f"❌ 逻辑链文件不存在: {yaml_path}")
        return 1
    
    try:
        with open(yaml_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        chain = LogicChain(**data)
        logger.info(f"✅ 已加载逻辑链: {len(chain.nodes)} 节点, {len(chain.edges)} 边")
        
    except yaml.YAMLError as e:
        logger.error(f"❌ YAML解析错误: {e}")
        return 1
    except Exception as e:
        logger.error(f"❌ 加载逻辑链失败: {e}")
        return 1
    
    # 2. Run validation
    validator = LogicChainValidator()
    result = validator.validate(chain)
    
    # 3. Report results
    print(f"\n{'='*60}")
    print(f"逻辑链验证结果: {book_id}")
    print(f"{'='*60}")
    
    if result.valid:
        print("✅ 验证通过")
    else:
        print(f"❌ 验证失败，发现 {len(result.errors)} 个错误:")
        for error in result.errors:
            print(f"   - [{error.error_type}] {error.message}")
    
    if result.warnings:
        print(f"\n⚠️  警告 ({len(result.warnings)}):")
        for warning in result.warnings:
            print(f"   - {warning}")
    
    # Print chain statistics
    print(f"\n📊 统计信息:")
    print(f"   节点数: {len(chain.nodes)}")
    print(f"   边数: {len(chain.edges)}")
    print(f"   入口节点: {len(chain.entry_nodes)}")
    print(f"   终端节点: {len(chain.terminal_nodes)}")
    print(f"   叙事顺序长度: {len(chain.narrative_order)}")
    print(f"{'='*60}\n")
    
    return 0 if result.valid else 1


def cmd_list(args) -> int:
    """列出所有目标书籍"""
    logger = get_logger()
    
    print("\n📚 目标书籍列表 (21本):\n")
    
    print("中文典籍 (8本):")
    for i, book in enumerate(TARGET_BOOKS[:8], 1):
        print(f"  {i:2d}. {book}")
    
    print("\n西方典籍 (13本):")
    for i, book in enumerate(TARGET_BOOKS[8:], 9):
        print(f"  {i:2d}. {book}")
    
    print()
    return 0


def cmd_refine(args) -> int:
    """
    自动优化低质量逻辑链
    
    Identify chains from build_report.md with quality < threshold,
    apply SemanticClusterRefiner and IntelligentSummaryGenerator,
    run IterativeRefinementEngine on each flagged chain,
    regenerate logic chains with refinements,
    and update build_report.md with final results.
    
    **Validates: Requirements 14.1-14.5, 15.1-15.5, 16.1-16.5**
    """
    logger = get_logger()
    
    # Import required components
    from scripts.logic_chain_builder.refinement_engine import (
        IterativeRefinementEngine, QUALITY_THRESHOLD_OVERALL
    )
    from scripts.logic_chain_builder.quality_scorer import LogicChainQualityScorer
    from scripts.logic_chain_builder.report import BuildReportGenerator
    from scripts.logic_chain_builder.models import BookStats, BookQualityScores
    
    # Get threshold from args or use default
    quality_threshold = args.threshold if hasattr(args, 'threshold') and args.threshold else QUALITY_THRESHOLD_OVERALL
    max_iterations = args.max_iterations if hasattr(args, 'max_iterations') and args.max_iterations else 5
    
    logger.info(f"🔧 开始自动优化逻辑链 (质量阈值: {quality_threshold:.2f}, 最大迭代: {max_iterations})")
    
    # Initialize components
    loader = SchemaLoader()
    validator = LogicChainValidator()
    writer = LogicChainWriter()
    quality_scorer = LogicChainQualityScorer()
    refinement_engine = IterativeRefinementEngine(
        max_iterations=max_iterations,
        quality_threshold=quality_threshold,
    )
    report_generator = BuildReportGenerator()
    
    # Step 1: Load all existing logic chains
    output_dir = Path(OUTPUT_DIR)
    if not output_dir.exists():
        logger.error(f"❌ 输出目录不存在: {output_dir}")
        print("请先运行 'batch' 命令生成逻辑链")
        return 1
    
    chain_files = list(output_dir.glob("*.yaml"))
    chain_files = [f for f in chain_files if not f.name.startswith("build_")]
    
    if not chain_files:
        logger.error("❌ 未找到任何逻辑链文件")
        return 1
    
    logger.info(f"📂 发现 {len(chain_files)} 个逻辑链文件")
    
    # Step 2: Load chains and identify low-quality ones
    chains_to_refine = []
    all_book_stats = []
    
    print(f"\n{'='*60}")
    print(f"自动优化逻辑链")
    print(f"{'='*60}")
    print(f"质量阈值: {quality_threshold:.2f}")
    print(f"最大迭代次数: {max_iterations}")
    print(f"{'='*60}\n")
    
    print("📊 分析现有逻辑链质量...")
    
    for chain_file in chain_files:
        book_id = chain_file.stem
        
        try:
            # Load chain
            with open(chain_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            chain = LogicChain(**data)
            
            # Load snippets for this book
            try:
                snippets = loader.load_snippets(book_id)
            except FileNotFoundError:
                logger.warning(f"⚠️  无法加载 {book_id} 的snippets，跳过")
                continue
            
            total_snippet_count = len(snippets)
            
            # Calculate quality score
            quality = quality_scorer.score(chain, total_snippet_count)
            overall_score = quality.overall_score()
            
            if overall_score < quality_threshold:
                chains_to_refine.append((chain, snippets, quality))
                logger.info(f"  ⚠️  {book_id}: 质量分数 {overall_score:.3f} < {quality_threshold:.2f}")
            else:
                logger.debug(f"  ✅ {book_id}: 质量分数 {overall_score:.3f} >= {quality_threshold:.2f}")
                
        except Exception as e:
            logger.error(f"❌ 加载 {book_id} 失败: {e}")
            continue
    
    if not chains_to_refine:
        print("\n✅ 所有逻辑链质量均达标，无需优化")
        return 0
    
    print(f"\n📋 发现 {len(chains_to_refine)} 个低质量逻辑链需要优化:")
    for chain, _, quality in chains_to_refine:
        print(f"   - {chain.book_id}: {quality.overall_score():.3f}")
    
    # Step 3: Apply refinement to each low-quality chain
    print(f"\n🔧 开始优化...")
    
    refined_count = 0
    improved_count = 0
    refinement_results = []
    
    bar_width = 40
    
    for i, (chain, snippets, initial_quality) in enumerate(chains_to_refine):
        book_id = chain.book_id
        
        # Progress bar
        progress = (i + 1) / len(chains_to_refine)
        filled = int(bar_width * progress)
        bar = '█' * filled + '░' * (bar_width - filled)
        print(f"\r[{bar}] {i+1}/{len(chains_to_refine)} - {book_id[:30]:<30}", end='', flush=True)
        
        try:
            # Run refinement engine
            result = refinement_engine.refine_until_threshold(
                chain=chain,
                snippets=snippets,
                total_snippet_count=len(snippets),
            )
            
            refined_count += 1
            
            # Check if quality improved
            if result.final_score > result.initial_score:
                improved_count += 1
            
            # Validate refined chain
            validation_result = validator.validate(result.chain)
            
            if not validation_result.valid:
                # Auto-repair if needed
                result.chain, repairs = validator.auto_repair(result.chain, validation_result.errors)
                validation_result = validator.validate(result.chain)
            
            if validation_result.valid:
                # Write refined chain
                writer.write(result.chain)
                
                refinement_results.append({
                    'book_id': book_id,
                    'initial_score': result.initial_score,
                    'final_score': result.final_score,
                    'iterations': result.iterations_performed,
                    'threshold_met': result.threshold_met,
                    'improvements': result.improvements_made,
                    'status': 'success',
                })
            else:
                refinement_results.append({
                    'book_id': book_id,
                    'initial_score': result.initial_score,
                    'final_score': result.final_score,
                    'iterations': result.iterations_performed,
                    'threshold_met': False,
                    'improvements': result.improvements_made,
                    'status': 'validation_failed',
                    'errors': [e.message for e in validation_result.errors],
                })
                
        except Exception as e:
            logger.error(f"优化 {book_id} 时出错: {e}")
            refinement_results.append({
                'book_id': book_id,
                'initial_score': initial_quality.overall_score(),
                'final_score': initial_quality.overall_score(),
                'iterations': 0,
                'threshold_met': False,
                'improvements': [],
                'status': 'error',
                'error_message': str(e),
            })
    
    # Clear progress bar
    print()
    
    # Step 4: Regenerate build report with updated statistics
    print("\n📝 更新构建报告...")
    
    # Reload all chains and regenerate report
    book_stats_list = []
    
    for book_id in TARGET_BOOKS:
        chain_path = output_dir / f"{book_id}.yaml"
        
        if not chain_path.exists():
            book_stats = BookStats(
                book_id=book_id,
                snippet_count=0,
                node_count=0,
                edge_count=0,
                coverage=0.0,
                orphan_snippets=[],
                status="skipped",
                error_message="Logic chain file not found"
            )
            book_stats_list.append(book_stats)
            continue
        
        try:
            with open(chain_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            chain = LogicChain(**data)
            
            # Load snippets
            try:
                snippets = loader.load_snippets(book_id)
                total_snippet_ids = {s.snippet_id for s in snippets}
            except FileNotFoundError:
                total_snippet_ids = set()
            
            # Calculate quality scores
            quality_report = quality_scorer.score(chain, total_snippet_count=len(total_snippet_ids))
            quality_scores = BookQualityScores(
                connectivity=quality_report.connectivity,
                argument_completeness=quality_report.argument_completeness,
                orphan_ratio=quality_report.orphan_ratio,
                cycle_count=quality_report.cycle_count,
                connectivity_pass=quality_report.connectivity_pass,
                argument_completeness_pass=quality_report.argument_completeness_pass,
                orphan_ratio_pass=quality_report.orphan_ratio_pass,
                overall_pass=quality_report.passes_threshold(),
            )
            
            book_stats = report_generator.create_book_stats(
                book_id=book_id,
                chain=chain,
                total_snippet_ids=total_snippet_ids,
                status="success",
                quality_scores=quality_scores,
            )
            book_stats_list.append(book_stats)
            
        except Exception as e:
            book_stats = BookStats(
                book_id=book_id,
                snippet_count=0,
                node_count=0,
                edge_count=0,
                coverage=0.0,
                orphan_snippets=[],
                status="failed",
                error_message=str(e)
            )
            book_stats_list.append(book_stats)
    
    # Generate and write updated report
    report = report_generator.generate(book_stats_list)
    report_path = report_generator.write(report)
    
    # Step 5: Print summary
    print(f"\n{'='*60}")
    print(f"优化完成")
    print(f"{'='*60}")
    print(f"  📊 处理的低质量链: {len(chains_to_refine)}")
    print(f"  ✅ 成功优化: {refined_count}")
    print(f"  📈 质量提升: {improved_count}")
    
    # Count how many now meet threshold
    threshold_met = sum(1 for r in refinement_results if r.get('threshold_met', False))
    print(f"  🎯 达到阈值: {threshold_met}/{len(chains_to_refine)}")
    
    print(f"\n  📝 构建报告已更新: {report_path}")
    
    # Print detailed results
    if refinement_results:
        print(f"\n📋 详细结果:")
        for result in refinement_results:
            status_emoji = "✅" if result['status'] == 'success' else "❌"
            score_change = result['final_score'] - result['initial_score']
            score_indicator = "↑" if score_change > 0 else ("↓" if score_change < 0 else "→")
            threshold_indicator = "🎯" if result.get('threshold_met', False) else ""
            
            print(f"   {status_emoji} {result['book_id']}: "
                  f"{result['initial_score']:.3f} {score_indicator} {result['final_score']:.3f} "
                  f"({result['iterations']} iterations) {threshold_indicator}")
            
            if result.get('improvements'):
                for improvement in result['improvements'][:3]:  # Show first 3 improvements
                    print(f"      - {improvement[:60]}...")
                if len(result.get('improvements', [])) > 3:
                    print(f"      ... and {len(result['improvements']) - 3} more")
    
    print(f"{'='*60}\n")
    
    # Return success if at least some chains were improved
    return 0 if improved_count > 0 or len(chains_to_refine) == 0 else 1


def cmd_build_v2(args) -> int:
    """
    V2版本：构建单本书籍的逻辑链
    
    使用V2组件：三级聚类、优先级边推断、语义质量评估。
    """
    logger = get_logger()
    book_id = args.book_id
    
    logger.info(f"📚 开始构建逻辑链 (V2): {book_id}")
    
    try:
        from scripts.logic_chain_builder.v2.builder import LogicChainBuilderV2
        
        builder = LogicChainBuilderV2(
            auto_backup=not args.no_backup,
            auto_rollback=not args.no_rollback,
        )
        result = builder.build(book_id)
        
        if result.success:
            chain = result.chain
            qr = result.quality_report
            
            print(f"\n{'='*60}")
            print(f"逻辑链构建完成 (V2): {book_id}")
            print(f"{'='*60}")
            print(f"  节点数: {len(chain.nodes)}")
            print(f"  边数: {len(chain.edges)}")
            print(f"  入口节点: {len(chain.entry_nodes)}")
            print(f"  终端节点: {len(chain.terminal_nodes)}")
            
            if qr:
                print(f"\n  📊 质量指标:")
                print(f"     连通性: {qr.connectivity:.2f}")
                print(f"     孤立比例: {qr.orphan_ratio:.2f}")
                print(f"     推理连贯性: {qr.reasoning_coherence:.2f}")
                print(f"     条件覆盖度: {qr.condition_coverage:.2f}")
                print(f"     论证完整性: {qr.argument_completeness:.2f}")
                print(f"     节点同质性: {qr.node_homogeneity:.2f}")
            
            print(f"{'='*60}\n")
            return 0
        else:
            logger.error(f"❌ 构建失败: {result.error_message}")
            return 1
            
    except Exception as e:
        logger.error(f"❌ 构建失败: {e}")
        logger.exception("详细错误信息:")
        return 1


def cmd_batch_v2(args) -> int:
    """
    V2版本：批量构建所有书籍的逻辑链
    """
    logger = get_logger()
    
    logger.info(f"📚 开始批量构建逻辑链 (V2)")
    
    try:
        from scripts.logic_chain_builder.v2.builder import LogicChainBuilderV2
        
        builder = LogicChainBuilderV2(
            auto_backup=not args.no_backup,
            auto_rollback=not args.no_rollback,
        )
        
        results = builder.build_batch()
        
        # 统计
        successful = sum(1 for r in results.values() if r.success)
        failed = sum(1 for r in results.values() if not r.success)
        
        print(f"\n{'='*60}")
        print(f"批量构建完成 (V2)")
        print(f"{'='*60}")
        print(f"  ✅ 成功: {successful}")
        print(f"  ❌ 失败: {failed}")
        print(f"  📊 总计: {len(results)}")
        print(f"\n  📝 报告已生成: data/logic_chains/build_report_v2.md")
        print(f"{'='*60}\n")
        
        return 0 if failed == 0 else 1
        
    except Exception as e:
        logger.error(f"❌ 批量构建失败: {e}")
        logger.exception("详细错误信息:")
        return 1


def cmd_validate_v2(args) -> int:
    """
    V2版本：验证书籍数据完整性
    """
    logger = get_logger()
    book_id = args.book_id
    
    logger.info(f"🔍 验证数据完整性 (V2): {book_id}")
    
    try:
        from scripts.logic_chain_builder.v2.builder import LogicChainBuilderV2
        
        builder = LogicChainBuilderV2()
        report = builder.validate(book_id)
        
        print(f"\n{'='*60}")
        print(f"数据验证结果 (V2): {book_id}")
        print(f"{'='*60}")
        print(f"  完整性: {'✅ 完整' if report.is_complete else '❌ 不完整'}")
        print(f"  Snippet数量: {report.snippet_count}")
        print(f"  Relation数量: {report.relation_count}")
        
        if report.missing_chapters:
            print(f"\n  ⚠️  缺失章节 ({len(report.missing_chapters)}):")
            for ch in report.missing_chapters[:5]:
                print(f"     - {ch}")
            if len(report.missing_chapters) > 5:
                print(f"     ... 及其他 {len(report.missing_chapters) - 5} 个")
        
        if report.orphan_relations:
            print(f"\n  ⚠️  孤儿关系 ({len(report.orphan_relations)}):")
            for rel in report.orphan_relations[:5]:
                print(f"     - {rel}")
            if len(report.orphan_relations) > 5:
                print(f"     ... 及其他 {len(report.orphan_relations) - 5} 个")
        
        if report.issues:
            print(f"\n  📋 问题列表 ({len(report.issues)}):")
            for issue in report.issues:
                print(f"     - [{issue.type}] {issue.description}")
                if issue.remediation:
                    print(f"       建议: {issue.remediation}")
        
        print(f"{'='*60}\n")
        
        return 0 if report.is_complete else 1
        
    except Exception as e:
        logger.error(f"❌ 验证失败: {e}")
        return 1


def cmd_cleanup_backups(args) -> int:
    """清理旧备份文件"""
    logger = get_logger()
    
    logger.info("🗑️  清理旧备份文件...")
    
    try:
        from scripts.logic_chain_builder.v2.backup import BackupManager
        
        manager = BackupManager()
        count = manager.cleanup_all_old_backups()
        
        print(f"\n✅ 已归档 {count} 个备份文件到 data/logic_chains/archive/\n")
        return 0
        
    except Exception as e:
        logger.error(f"❌ 清理失败: {e}")
        return 1


def main() -> int:
    """主入口"""
    parser = argparse.ArgumentParser(
        description="Logic Chain Builder - 从Schema数据构建逻辑链",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # V1 命令
  python -m scripts.logic_chain_builder build 滴天髓
  python -m scripts.logic_chain_builder batch
  python -m scripts.logic_chain_builder validate 滴天髓
  python -m scripts.logic_chain_builder list
  
  # V2 命令 (推荐)
  python -m scripts.logic_chain_builder build-v2 滴天髓
  python -m scripts.logic_chain_builder batch-v2
  python -m scripts.logic_chain_builder validate-v2 滴天髓
  python -m scripts.logic_chain_builder cleanup-backups
        """
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="启用详细日志输出"
    )
    
    parser.add_argument(
        "--log-file",
        type=str,
        help="日志文件路径"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="子命令")
    
    # build 命令
    build_parser = subparsers.add_parser("build", help="构建单本书籍的逻辑链")
    build_parser.add_argument("book_id", help="书籍ID")
    build_parser.set_defaults(func=cmd_build)
    
    # batch 命令
    batch_parser = subparsers.add_parser("batch", help="批量构建所有书籍的逻辑链")
    batch_parser.set_defaults(func=cmd_batch)
    
    # validate 命令
    validate_parser = subparsers.add_parser("validate", help="验证逻辑链")
    validate_parser.add_argument("book_id", help="书籍ID")
    validate_parser.set_defaults(func=cmd_validate)
    
    # list 命令
    list_parser = subparsers.add_parser("list", help="列出所有目标书籍")
    list_parser.set_defaults(func=cmd_list)
    
    # refine 命令
    refine_parser = subparsers.add_parser("refine", help="自动优化低质量逻辑链")
    refine_parser.add_argument(
        "--threshold",
        type=float,
        default=0.6,
        help="质量阈值 (默认: 0.6)"
    )
    refine_parser.add_argument(
        "--max-iterations",
        type=int,
        default=5,
        help="最大迭代次数 (默认: 5)"
    )
    refine_parser.set_defaults(func=cmd_refine)
    
    # V2 命令
    # build-v2 命令
    build_v2_parser = subparsers.add_parser("build-v2", help="[V2] 构建单本书籍的逻辑链")
    build_v2_parser.add_argument("book_id", help="书籍ID")
    build_v2_parser.add_argument(
        "--no-backup",
        action="store_true",
        help="禁用自动备份"
    )
    build_v2_parser.add_argument(
        "--no-rollback",
        action="store_true",
        help="禁用失败时自动回滚"
    )
    build_v2_parser.set_defaults(func=cmd_build_v2)
    
    # batch-v2 命令
    batch_v2_parser = subparsers.add_parser("batch-v2", help="[V2] 批量构建所有书籍的逻辑链")
    batch_v2_parser.add_argument(
        "--no-backup",
        action="store_true",
        help="禁用自动备份"
    )
    batch_v2_parser.add_argument(
        "--no-rollback",
        action="store_true",
        help="禁用失败时自动回滚"
    )
    batch_v2_parser.set_defaults(func=cmd_batch_v2)
    
    # validate-v2 命令
    validate_v2_parser = subparsers.add_parser("validate-v2", help="[V2] 验证书籍数据完整性")
    validate_v2_parser.add_argument("book_id", help="书籍ID")
    validate_v2_parser.set_defaults(func=cmd_validate_v2)
    
    # cleanup-backups 命令
    cleanup_parser = subparsers.add_parser("cleanup-backups", help="清理旧备份文件")
    cleanup_parser.set_defaults(func=cmd_cleanup_backups)
    
    args = parser.parse_args()
    
    # 配置日志
    log_level = logging.DEBUG if args.verbose else logging.INFO
    setup_logging(level=log_level, log_file=args.log_file)
    
    if args.command is None:
        parser.print_help()
        return 0
    
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
