"""
CLI框架 - 知识图谱构建命令行工具

Feature: cross-book-knowledge-graph
Requirement Refs: Req 8.1, Req 8.2, Req 8.3
Design Refs: Design.md#模块结构

Commands:
- build: 构建知识图谱
- validate: 验证图谱完整性
- export: 导出图谱
- stats: 生成统计报告
- snapshot: 快照管理
"""

import argparse
import json
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Optional

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def cmd_build(args: argparse.Namespace) -> int:
    """构建knowledge graph"""
    from pathlib import Path
    from scripts.knowledge_graph_builder.builders import GraphBuilder
    from scripts.knowledge_graph_builder.persistence import GraphSerializer
    
    logger.info(f"Building knowledge graph from {args.input_dir}")
    
    try:
        builder = GraphBuilder(
            logic_chains_dir=Path(args.input_dir),
            knowledge_graph_dir=Path(args.output_dir),
        )
        
        # 构建图谱 - use build_full or build_incremental (not build)
        if args.incremental:
            graph = builder.build_incremental(dry_run=args.dry_run)
        else:
            graph = builder.build_full(dry_run=args.dry_run)
        
        if args.dry_run:
            logger.info("[DRY RUN] No changes applied")
            return 0
        
        # 保存
        serializer = GraphSerializer()
        serializer.serialize(graph, Path(args.output_dir))
        
        logger.info(f"Built graph with {len(graph.concepts)} concepts, {len(graph.edges)} edges")
        logger.info(f"Saved to {args.output_dir}")
        return 0
    except Exception as e:
        logger.error(f"Build failed: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


def cmd_validate(args: argparse.Namespace) -> int:
    """验证图谱"""
    from scripts.knowledge_graph_builder.persistence import GraphSerializer
    from scripts.knowledge_graph_builder.validation import GraphValidator
    
    logger.info(f"Validating graph from {args.graph_dir}")
    
    try:
        # 加载图谱
        serializer = GraphSerializer()
        graph = serializer.deserialize(args.graph_dir)
        
        # 验证
        validator = GraphValidator(
            logic_chains_dir=args.logic_chains_dir,
            factor_namespace_path=args.factor_namespace,
        )
        report = validator.validate(graph)
        
        # 保存报告
        if args.output:
            validator.save_report(report, args.output)
        
        # 输出结果
        print(f"\nValidation Result: {report.graph_status.upper()}")
        print(f"  Errors: {report.error_count}")
        print(f"  Warnings: {report.warning_count}")
        print(f"  Info: {report.info_count}")
        
        if args.verbose and report.issues:
            print("\nIssues:")
            for issue in report.issues[:20]:
                print(f"  [{issue.severity.value}] {issue.issue_type.value}: {issue.message}")
        
        return 0 if report.is_valid() else 1
    except Exception as e:
        logger.error(f"Validation failed: {e}")
        return 1


def cmd_export(args: argparse.Namespace) -> int:
    """导出图谱"""
    from scripts.knowledge_graph_builder.persistence import GraphSerializer
    from scripts.knowledge_graph_builder.export import (
        GraphMLExporter,
        JSONLDExporter,
        MermaidExporter,
    )
    from scripts.knowledge_graph_builder.models.concept import DivinationSystem
    
    logger.info(f"Exporting graph from {args.graph_dir} to {args.format}")
    
    try:
        # 加载图谱
        serializer = GraphSerializer()
        graph = serializer.deserialize(args.graph_dir)
        
        # 解析过滤参数
        systems = None
        if args.systems:
            systems = [DivinationSystem(s) for s in args.systems.split(',')]
        
        # 选择导出器
        exporters = {
            'graphml': GraphMLExporter,
            'mermaid': MermaidExporter,
            'jsonld': JSONLDExporter,
        }
        
        exporter_cls = exporters.get(args.format)
        if not exporter_cls:
            logger.error(f"Unknown format: {args.format}")
            return 1
        
        exporter = exporter_cls(max_nodes=args.max_nodes)
        exporter.export(
            graph,
            output_path=args.output,
            divination_systems=systems,
            authority_threshold=args.min_authority,
        )
        
        logger.info(f"Exported to {args.output}")
        return 0
    except Exception as e:
        logger.error(f"Export failed: {e}")
        return 1


def cmd_stats(args: argparse.Namespace) -> int:
    """生成统计报告"""
    from scripts.knowledge_graph_builder.persistence import GraphSerializer
    from scripts.knowledge_graph_builder.export import StatsGenerator
    
    logger.info(f"Generating stats for {args.graph_dir}")
    
    try:
        # 加载图谱
        serializer = GraphSerializer()
        graph = serializer.deserialize(args.graph_dir)
        
        # 生成统计
        generator = StatsGenerator()
        stats = generator.generate_stats(graph)
        
        # 保存JSON
        if args.json_output:
            generator.save_stats(stats, args.json_output)
        
        # 生成并保存摘要
        if args.summary_output:
            summary = generator.generate_summary(graph, stats)
            generator.save_summary(summary, args.summary_output)
        
        # 输出基本统计
        print(f"\nGraph Statistics:")
        print(f"  Concepts: {stats.total_concepts:,}")
        print(f"  Edges: {stats.total_edges:,}")
        print(f"  Books: {stats.total_books}")
        print(f"  Systems: {stats.total_systems}")
        print(f"  Avg Authority: {stats.average_authority_score:.2%}")
        
        return 0
    except Exception as e:
        logger.error(f"Stats generation failed: {e}")
        return 1


def cmd_snapshot(args: argparse.Namespace) -> int:
    """快照管理"""
    from scripts.knowledge_graph_builder.persistence import GraphSerializer, SnapshotManager
    
    try:
        manager = SnapshotManager(
            snapshots_dir=args.snapshots_dir,
            retention_days=args.retention_days,
        )
        
        if args.action == 'create':
            serializer = GraphSerializer()
            graph = serializer.deserialize(args.graph_dir)
            info = manager.create_snapshot(graph, description=args.description)
            print(f"Created snapshot: {info.version}")
            
        elif args.action == 'list':
            snapshots = manager.list_snapshots()
            if snapshots:
                print("Snapshots:")
                for snap in snapshots:
                    desc = f" - {snap.description}" if snap.description else ""
                    print(f"  {snap.version} ({snap.created_at.strftime('%Y-%m-%d %H:%M')}){desc}")
            else:
                print("No snapshots found")
                
        elif args.action == 'rollback':
            graph = manager.rollback(version=args.version)
            serializer = GraphSerializer()
            serializer.serialize(graph, args.graph_dir)
            print(f"Rolled back to {args.version}")
            
        elif args.action == 'delete':
            manager.delete_snapshot(args.version)
            print(f"Deleted snapshot: {args.version}")
            
        elif args.action == 'cleanup':
            deleted = manager.cleanup_old_snapshots()
            print(f"Cleaned up {deleted} old snapshots")
        
        return 0
    except Exception as e:
        logger.error(f"Snapshot operation failed: {e}")
        return 1


def cmd_query(args: argparse.Namespace) -> int:
    """查询图谱"""
    from scripts.knowledge_graph_builder.persistence import GraphSerializer
    from scripts.knowledge_graph_builder.query import SemanticQueryService
    from scripts.knowledge_graph_builder.models import SemanticQuery
    
    try:
        serializer = GraphSerializer()
        graph = serializer.deserialize(args.graph_dir)
        
        service = SemanticQueryService(graph)
        
        # Parse factor IDs
        factor_ids = args.factors.split(',') if args.factors else []
        
        query = SemanticQuery(
            factor_ids=factor_ids,
            traversal_depth=args.depth,
            page_size=args.limit,
        )
        
        result = service.query(query)
        
        print(f"\nQuery Results: {result.total_count} total, showing {len(result.items)}")
        print(f"Query time: {result.query_time_ms:.2f}ms")
        print()
        
        for item in result.items:
            concept = item.concept
            print(f"- {concept.canonical_label_zh} [{concept.divination_system.value}]")
            print(f"  ID: {concept.concept_id}")
            print(f"  Authority: {concept.authority_score:.2f}")
            if item.conflict_warnings:
                print(f"  Conflicts: {len(item.conflict_warnings)}")
            print()
        
        return 0
    except Exception as e:
        logger.error(f"Query failed: {e}")
        return 1


def cmd_rollback(args: argparse.Namespace) -> int:
    """回滚到指定版本"""
    from scripts.knowledge_graph_builder.persistence import GraphSerializer, SnapshotManager
    
    try:
        manager = SnapshotManager(
            snapshots_dir=args.snapshots_dir,
        )
        
        if not args.version:
            # List available versions
            snapshots = manager.list_snapshots()
            if not snapshots:
                print("No snapshots available for rollback")
                return 1
            print("Available versions:")
            for snap in snapshots:
                print(f"  {snap.version}")
            return 0
        
        graph = manager.rollback(version=args.version)
        serializer = GraphSerializer()
        serializer.serialize(graph, args.graph_dir)
        
        print(f"Successfully rolled back to version {args.version}")
        return 0
    except Exception as e:
        logger.error(f"Rollback failed: {e}")
        return 1


def cmd_align(args: argparse.Namespace) -> int:
    """生成对齐报告"""
    from scripts.knowledge_graph_builder.persistence import GraphSerializer
    from scripts.knowledge_graph_builder.builders import ConceptAligner, AlignmentThresholds
    
    try:
        serializer = GraphSerializer()
        graph = serializer.deserialize(args.graph_dir)
        
        aligner = ConceptAligner(thresholds=AlignmentThresholds())
        alignments = aligner.find_alignments(graph.concepts)
        
        # Generate report
        output_path = Path(args.output) if args.output else Path(args.graph_dir) / 'alignment_report.md'
        aligner.generate_alignment_report(alignments, output_path)
        
        print(f"Found {len(alignments)} alignment candidates")
        print(f"Report saved to {output_path}")
        
        return 0
    except Exception as e:
        logger.error(f"Alignment report failed: {e}")
        return 1


def create_parser() -> argparse.ArgumentParser:
    """创建命令行解析器"""
    parser = argparse.ArgumentParser(
        prog='kg-builder',
        description='Knowledge Graph Builder CLI',
    )
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # build命令
    build_parser = subparsers.add_parser('build', help='Build knowledge graph')
    build_parser.add_argument('--input-dir', default='data/logic_chains', help='LogicChain directory')
    build_parser.add_argument('--output-dir', default='data/knowledge_graph', help='Output directory')
    build_parser.add_argument('--incremental', action='store_true', help='Incremental build')
    build_parser.add_argument('--dry-run', action='store_true', help='Report changes without applying')
    build_parser.set_defaults(func=cmd_build)
    
    # validate命令
    validate_parser = subparsers.add_parser('validate', help='Validate graph')
    validate_parser.add_argument('--graph-dir', default='data/knowledge_graph', help='Graph directory')
    validate_parser.add_argument('--logic-chains-dir', default='data/logic_chains', help='LogicChain directory')
    validate_parser.add_argument('--factor-namespace', default='data/factor_ontology/namespace.yaml')
    validate_parser.add_argument('--output', help='Output report path')
    validate_parser.set_defaults(func=cmd_validate)
    
    # export命令
    export_parser = subparsers.add_parser('export', help='Export graph')
    export_parser.add_argument('--graph-dir', default='data/knowledge_graph', help='Graph directory')
    export_parser.add_argument('--format', choices=['graphml', 'mermaid', 'jsonld'], default='graphml')
    export_parser.add_argument('--output', required=True, help='Output file path')
    export_parser.add_argument('--max-nodes', type=int, default=100, help='Max nodes to export')
    export_parser.add_argument('--systems', help='Comma-separated divination systems')
    export_parser.add_argument('--min-authority', type=float, default=0.0, help='Min authority threshold')
    export_parser.set_defaults(func=cmd_export)
    
    # stats命令
    stats_parser = subparsers.add_parser('stats', help='Generate statistics')
    stats_parser.add_argument('--graph-dir', default='data/knowledge_graph', help='Graph directory')
    stats_parser.add_argument('--json-output', help='JSON output path')
    stats_parser.add_argument('--summary-output', help='Summary markdown output path')
    stats_parser.set_defaults(func=cmd_stats)
    
    # snapshot命令
    snapshot_parser = subparsers.add_parser('snapshot', help='Snapshot management')
    snapshot_parser.add_argument('action', choices=['create', 'list', 'rollback', 'delete', 'cleanup'])
    snapshot_parser.add_argument('--graph-dir', default='data/knowledge_graph', help='Graph directory')
    snapshot_parser.add_argument('--snapshots-dir', default='data/knowledge_graph/snapshots')
    snapshot_parser.add_argument('--version', help='Snapshot version')
    snapshot_parser.add_argument('--description', help='Snapshot description')
    snapshot_parser.add_argument('--retention-days', type=int, default=30)
    snapshot_parser.set_defaults(func=cmd_snapshot)
    
    # query命令
    query_parser = subparsers.add_parser('query', help='Query knowledge graph')
    query_parser.add_argument('--graph-dir', default='data/knowledge_graph', help='Graph directory')
    query_parser.add_argument('--factors', help='Comma-separated factor IDs to query')
    query_parser.add_argument('--depth', type=int, default=1, help='Traversal depth (0-3)')
    query_parser.add_argument('--limit', type=int, default=20, help='Max results')
    query_parser.set_defaults(func=cmd_query)
    
    # rollback命令
    rollback_parser = subparsers.add_parser('rollback', help='Rollback to previous version')
    rollback_parser.add_argument('--graph-dir', default='data/knowledge_graph', help='Graph directory')
    rollback_parser.add_argument('--snapshots-dir', default='data/knowledge_graph/snapshots')
    rollback_parser.add_argument('--version', help='Version to rollback to (omit to list versions)')
    rollback_parser.set_defaults(func=cmd_rollback)
    
    # align命令
    align_parser = subparsers.add_parser('align', help='Generate alignment report')
    align_parser.add_argument('--graph-dir', default='data/knowledge_graph', help='Graph directory')
    align_parser.add_argument('--output', help='Output report path')
    align_parser.set_defaults(func=cmd_align)
    
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    """主入口"""
    parser = create_parser()
    args = parser.parse_args(argv)
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    if not args.command:
        parser.print_help()
        return 0
    
    return args.func(args)


if __name__ == '__main__':
    sys.exit(main())
