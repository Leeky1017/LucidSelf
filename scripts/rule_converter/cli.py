"""
Rule Converter CLI

命令行接口，支持转换、验证、统计等操作。

Feature: rule-converter
Requirement Refs: Req 13.1-13.8
"""

import json
import logging
import sys
from pathlib import Path
from typing import Optional

try:
    import typer
    from rich.console import Console
    from rich.table import Table
    from rich.progress import Progress, SpinnerColumn, TextColumn
    HAS_RICH = True
except ImportError:
    HAS_RICH = False
    typer = None

# 设置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# 如果没有 typer，提供简单的 argparse 替代
if typer is None:
    import argparse
    
    def main():
        parser = argparse.ArgumentParser(description="Rule Converter CLI")
        parser.add_argument("command", choices=["convert", "stats", "validate", "diff", "review"])
        parser.add_argument("--input-dir", type=str, default="data/logic_chains")
        parser.add_argument("--output-dir", type=str, default="data/rules")
        parser.add_argument("--dry-run", action="store_true")
        parser.add_argument("--verbose", action="store_true")
        
        args = parser.parse_args()
        
        if args.verbose:
            logging.getLogger().setLevel(logging.DEBUG)
        
        if args.command == "convert":
            _convert_simple(args.input_dir, args.output_dir, args.dry_run)
        elif args.command == "stats":
            _stats_simple(args.input_dir)
        else:
            print(f"Command {args.command} requires typer. Install with: pip install typer rich")
    
    def _convert_simple(input_dir, output_dir, dry_run):
        from scripts.rule_converter.orchestrator import ConversionOrchestrator
        
        print("Starting conversion...")
        orchestrator = ConversionOrchestrator(
            logic_chain_dir=Path(input_dir),
            output_dir=Path(output_dir),
        )
        
        report = orchestrator.convert_all(dry_run=dry_run)
        
        print(f"\n=== Conversion Report ===")
        print(f"Duration: {report.duration_seconds:.2f}s")
        print(f"Total nodes: {report.total_nodes}")
        print(f"Convertible: {report.convertible_nodes}")
        print(f"Converted: {report.converted}")
        print(f"Auto-approved: {report.auto_approved}")
        print(f"Human-review: {report.human_review}")
        print(f"Rejected: {report.rejected}")
        print(f"Failed: {report.failed}")
    
    def _stats_simple(input_dir):
        from scripts.rule_converter.loaders.logic_chain_loader import LogicChainLoader
        
        loader = LogicChainLoader(Path(input_dir))
        loader.load_all()
        
        stats = loader.stats
        print(f"\n=== LogicChain Stats ===")
        for key, value in stats.items():
            print(f"{key}: {value}")

else:
    # 使用 typer 的完整 CLI
    app = typer.Typer(
        name="rule-converter",
        help="LogicChain → Rule Converter CLI",
        add_completion=False,
    )
    console = Console() if HAS_RICH else None
    
    @app.command()
    def convert(
        input_dir: str = typer.Option("data/logic_chains", "--input-dir", "-i", help="LogicChain 目录"),
        output_dir: str = typer.Option("data/rules", "--output-dir", "-o", help="输出目录"),
        dry_run: bool = typer.Option(False, "--dry-run", "-n", help="只生成报告不写入文件"),
        verbose: bool = typer.Option(False, "--verbose", "-v", help="详细输出"),
    ):
        """转换 LogicChain 节点为规则"""
        if verbose:
            logging.getLogger().setLevel(logging.DEBUG)
        
        from scripts.rule_converter.orchestrator import ConversionOrchestrator
        from scripts.rule_converter.outputs.jsonl_writer import JSONLWriter, WriteMode
        
        console.print("[bold blue]Starting conversion...[/bold blue]")
        
        orchestrator = ConversionOrchestrator(
            logic_chain_dir=Path(input_dir),
            output_dir=Path(output_dir),
        )
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            progress.add_task("Loading data...", total=None)
            orchestrator.load()
        
        report = orchestrator.convert_all(dry_run=dry_run)
        
        # 输出结果
        if not dry_run:
            # 写入规则文件
            writer = JSONLWriter(Path(output_dir))
            auto_rules = orchestrator.get_all_approved_rules()
            
            if auto_rules:
                grouped = writer.group_rules_by_system_category(auto_rules)
                results = writer.write_batch(grouped, WriteMode.OVERWRITE)
                writer.write_manifest()
                
                console.print(f"[green]Written {len(auto_rules)} rules to {output_dir}[/green]")
        
        # 显示报告
        _print_report(report)
    
    @app.command()
    def stats(
        input_dir: str = typer.Option("data/logic_chains", "--input-dir", "-i", help="LogicChain 目录"),
    ):
        """显示 LogicChain 统计信息"""
        from scripts.rule_converter.loaders.logic_chain_loader import LogicChainLoader
        from scripts.rule_converter.loaders.factor_ontology import FactorOntology
        from scripts.rule_converter.loaders.snippet_store import SnippetStore
        
        console.print("[bold blue]Loading data sources...[/bold blue]")
        
        # 加载 LogicChain
        loader = LogicChainLoader(Path(input_dir))
        loader.load_all()
        
        # 加载因子本体
        ontology = FactorOntology()
        ontology.load()
        
        # 加载 Snippets
        snippet_store = SnippetStore(lazy_load=False)
        snippet_store.load_from_dir()
        
        # 显示表格
        table = Table(title="Data Sources Statistics")
        table.add_column("Source", style="cyan")
        table.add_column("Count", style="green")
        
        table.add_row("LogicChain Files", str(loader.stats["loaded_files"]))
        table.add_row("Total Nodes", str(loader.stats["total_nodes"]))
        table.add_row("Convertible Nodes", str(loader.stats["convertible_nodes"]))
        table.add_row("Nodes with factor_refs", str(loader.stats["nodes_with_factor_refs"]))
        table.add_row("Total Edges", str(loader.stats["total_edges"]))
        table.add_row("", "")
        table.add_row("Certified Factors", str(ontology.stats["certified_factors"]))
        table.add_row("Base Factors", str(ontology.stats["base_factors"]))
        table.add_row("Total Factors", str(len(ontology)))
        table.add_row("", "")
        table.add_row("Total Snippets", str(len(snippet_store)))
        table.add_row("Snippets with factor_trigger", str(snippet_store.stats["snippets_with_factor_trigger"]))
        
        console.print(table)
        
        # 显示体系分布
        console.print("\n[bold]Factors by System:[/bold]")
        for system, count in sorted(ontology.stats["factors_by_system"].items()):
            console.print(f"  {system}: {count}")
    
    @app.command()
    def validate(
        rules_dir: str = typer.Option("data/rules", "--rules-dir", "-r", help="规则目录"),
    ):
        """验证规则文件"""
        from scripts.rule_converter.validators.schema_validator import SchemaValidator
        import json
        
        console.print("[bold blue]Validating rules...[/bold blue]")
        
        validator = SchemaValidator()
        rules_path = Path(rules_dir)
        
        if not rules_path.exists():
            console.print(f"[red]Directory not found: {rules_dir}[/red]")
            raise typer.Exit(1)
        
        total_rules = 0
        valid_rules = 0
        invalid_rules = 0
        errors = []
        
        for jsonl_file in rules_path.rglob("*.jsonl"):
            with open(jsonl_file, "r", encoding="utf-8") as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if not line:
                        continue
                    
                    try:
                        rule = json.loads(line)
                        total_rules += 1
                        
                        result = validator.validate(rule)
                        if result.is_valid:
                            valid_rules += 1
                        else:
                            invalid_rules += 1
                            errors.append({
                                "file": str(jsonl_file),
                                "line": line_num,
                                "rule_id": rule.get("rule_id", "unknown"),
                                "errors": [e.message for e in result.errors],
                            })
                    except json.JSONDecodeError as e:
                        invalid_rules += 1
                        errors.append({
                            "file": str(jsonl_file),
                            "line": line_num,
                            "error": f"JSON parse error: {e}",
                        })
        
        # 显示结果
        table = Table(title="Validation Results")
        table.add_column("Metric", style="cyan")
        table.add_column("Count", style="green")
        
        table.add_row("Total Rules", str(total_rules))
        table.add_row("Valid", str(valid_rules))
        table.add_row("Invalid", str(invalid_rules))
        
        console.print(table)
        
        if errors:
            console.print(f"\n[red]Found {len(errors)} validation errors:[/red]")
            for err in errors[:10]:
                console.print(f"  {err.get('file')}:{err.get('line')} - {err.get('rule_id', 'unknown')}")
                for e in err.get("errors", [])[:3]:
                    console.print(f"    - {e}")
    
    @app.command()
    def diff(
        old_dir: str = typer.Argument(..., help="旧规则目录"),
        new_dir: str = typer.Argument(..., help="新规则目录"),
        output: Optional[str] = typer.Option(None, "--output", "-o", help="输出报告路径"),
    ):
        """比较两次转换的差异"""
        from scripts.rule_converter.outputs.diff_reporter import DiffReporter
        
        console.print("[bold blue]Comparing rule sets...[/bold blue]")
        
        reporter = DiffReporter()
        report = reporter.compare_directories(Path(old_dir), Path(new_dir))
        
        # 显示摘要
        table = Table(title="Diff Summary")
        table.add_column("Change Type", style="cyan")
        table.add_column("Count", style="green")
        
        table.add_row("Added", str(report.added_count))
        table.add_row("Modified", str(report.modified_count))
        table.add_row("Removed", str(report.removed_count))
        table.add_row("Total Changes", str(report.total_changes))
        
        console.print(table)
        
        # 保存报告
        if output:
            output_path = Path(output)
            format = "markdown" if output_path.suffix == ".md" else "json"
            reporter.save_report(report, output_path, format)
            console.print(f"[green]Report saved to {output}[/green]")
    
    @app.command()
    def review(
        queue_path: str = typer.Option("data/rules/review_queue.json", "--queue", "-q", help="审核队列路径"),
        action: str = typer.Argument("list", help="操作: list, approve, reject"),
        rule_id: Optional[str] = typer.Option(None, "--rule-id", "-r", help="规则ID"),
    ):
        """管理审核队列"""
        from scripts.rule_converter.outputs.review_queue import ReviewQueue
        
        queue = ReviewQueue(Path(queue_path))
        queue.load()
        
        if action == "list":
            # 显示统计
            stats = queue.stats
            
            table = Table(title="Review Queue")
            table.add_column("Status", style="cyan")
            table.add_column("Count", style="green")
            
            table.add_row("Pending", str(stats["pending"]))
            table.add_row("Approved", str(stats["approved"]))
            table.add_row("Rejected", str(stats["rejected"]))
            table.add_row("Modified", str(stats["modified"]))
            table.add_row("Total", str(stats["total"]))
            
            console.print(table)
            
            # 显示待审核项
            pending = queue.get_pending()
            if pending:
                console.print("\n[bold]Pending Items:[/bold]")
                for item in pending[:10]:
                    console.print(f"  - {item.rule_id} (score: {item.classification_score:.2f})")
                if len(pending) > 10:
                    console.print(f"  ... and {len(pending) - 10} more")
        
        elif action == "approve":
            if not rule_id:
                console.print("[red]--rule-id is required for approve[/red]")
                raise typer.Exit(1)
            
            if queue.approve(rule_id):
                queue.save()
                console.print(f"[green]Approved: {rule_id}[/green]")
            else:
                console.print(f"[red]Rule not found: {rule_id}[/red]")
        
        elif action == "reject":
            if not rule_id:
                console.print("[red]--rule-id is required for reject[/red]")
                raise typer.Exit(1)
            
            if queue.reject(rule_id):
                queue.save()
                console.print(f"[yellow]Rejected: {rule_id}[/yellow]")
            else:
                console.print(f"[red]Rule not found: {rule_id}[/red]")
    
    def _print_report(report):
        """打印转换报告"""
        table = Table(title="Conversion Report")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")
        
        table.add_row("Duration", f"{report.duration_seconds:.2f}s")
        table.add_row("", "")
        table.add_row("Total Chains", str(report.total_chains))
        table.add_row("Total Nodes", str(report.total_nodes))
        table.add_row("Convertible Nodes", str(report.convertible_nodes))
        table.add_row("", "")
        table.add_row("Converted", str(report.converted))
        table.add_row("Auto-Approved", str(report.auto_approved))
        table.add_row("Human-Review", str(report.human_review))
        table.add_row("Rejected", str(report.rejected))
        table.add_row("Failed", str(report.failed))
        
        console.print(table)
        
        if report.by_system:
            console.print("\n[bold]By System:[/bold]")
            for system, count in sorted(report.by_system.items()):
                console.print(f"  {system}: {count}")
        
        if report.errors:
            console.print(f"\n[red]Errors ({len(report.errors)}):[/red]")
            for err in report.errors[:5]:
                console.print(f"  - {err['node_id']}: {err['error']}")
    
    def main():
        app()


if __name__ == "__main__":
    main()
