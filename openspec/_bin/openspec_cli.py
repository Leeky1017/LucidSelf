#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
from dataclasses import dataclass
from pathlib import Path


VERSION = "openspec-local 0.1.0"


@dataclass
class RequirementCheck:
    name: str
    ok: bool
    message: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def try_read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return read_text(path)


def list_spec_dirs(root: Path) -> list[Path]:
    specs_root = root / "openspec" / "specs"
    if not specs_root.exists():
        return []
    return sorted([p for p in specs_root.iterdir() if p.is_dir()])


def list_change_dirs(root: Path) -> list[Path]:
    changes_root = root / "openspec" / "changes"
    if not changes_root.exists():
        return []
    return sorted(
        [
            p
            for p in changes_root.iterdir()
            if p.is_dir() and p.name not in {"archive", "_archive_"}
        ]
    )


def count_tasks_from_file(path: Path) -> tuple[int, int]:
    if not path.exists():
        return (0, 0)
    text = read_text(path)
    total = 0
    done = 0
    for line in text.splitlines():
        line = line.strip().lower()
        if line.startswith("- [ ]"):
            total += 1
        elif line.startswith("- [x]"):
            total += 1
            done += 1
    return (done, total)


def count_tasks_in_dir(path: Path) -> tuple[int, int]:
    done_total = 0
    total_total = 0
    for task_file in path.glob("**/tasks.md"):
        done, total = count_tasks_from_file(task_file)
        done_total += done
        total_total += total
    return (done_total, total_total)


def parse_requirements(spec_text: str) -> list[tuple[str, list[str]]]:
    reqs: list[tuple[str, list[str]]] = []
    current_name = None
    current_lines: list[str] = []
    for line in spec_text.splitlines():
        if line.startswith("### Requirement:"):
            if current_name is not None:
                reqs.append((current_name, current_lines))
            current_name = line[len("### Requirement:") :].strip()
            current_lines = []
        else:
            if current_name is not None:
                current_lines.append(line)
    if current_name is not None:
        reqs.append((current_name, current_lines))
    return reqs


def spec_title_from_markdown(spec_text: str) -> str:
    for line in spec_text.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def requirement_checks(spec_text: str) -> list[RequirementCheck]:
    checks: list[RequirementCheck] = []
    if "## Purpose" not in spec_text:
        checks.append(RequirementCheck("Purpose section", False, "Missing ## Purpose"))
    if "## Requirements" not in spec_text:
        checks.append(
            RequirementCheck("Requirements section", False, "Missing ## Requirements")
        )
    for name, lines in parse_requirements(spec_text):
        non_empty = [ln.strip() for ln in lines if ln.strip()]
        if not non_empty:
            checks.append(
                RequirementCheck(
                    f"Requirement {name}",
                    False,
                    "Requirement content is empty",
                )
            )
            continue
        first = non_empty[0]
        if "SHALL" not in first and "MUST" not in first:
            checks.append(
                RequirementCheck(
                    f"Requirement {name}",
                    False,
                    "First line must contain SHALL or MUST",
                )
            )
        scenarios = [ln for ln in lines if ln.startswith("#### Scenario:")]
        if not scenarios:
            checks.append(
                RequirementCheck(
                    f"Requirement {name}",
                    False,
                    "Missing scenario",
                )
            )
            continue
        # Check scenario content
        lines_iter = list(lines)
        for i, line in enumerate(lines_iter):
            if line.startswith("#### Scenario:"):
                j = i + 1
                content_lines = []
                while j < len(lines_iter) and not lines_iter[j].startswith(
                    "#### Scenario:"
                ):
                    content_lines.append(lines_iter[j].strip())
                    j += 1
                if not [c for c in content_lines if c]:
                    checks.append(
                        RequirementCheck(
                            f"Scenario in {name}",
                            False,
                            "Scenario content is empty",
                        )
                    )
    return checks


def count_requirements_and_scenarios(spec_text: str) -> tuple[int, int]:
    reqs = parse_requirements(spec_text)
    req_count = len(reqs)
    scenario_count = 0
    for _, lines in reqs:
        scenario_count += len([ln for ln in lines if ln.startswith("#### Scenario:")])
    return req_count, scenario_count


def parse_specs_index_table(index_text: str) -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    for raw in index_text.splitlines():
        line = raw.strip()
        if not line or "|" not in line:
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 6:
            continue
        spec_id = parts[0]
        if spec_id == "ID" or set(spec_id) == {"-"}:
            continue
        if not all(ch.islower() or ch.isdigit() or ch == "-" for ch in spec_id):
            continue
        rows[spec_id] = {
            "name": parts[1],
            "priority": parts[2],
            "owner": parts[3],
            "status": parts[4],
            "gate": parts[5],
        }
    return rows


def parse_specs_index_deps(index_text: str) -> dict[str, list[str]]:
    deps: dict[str, list[str]] = {}
    in_deps = False
    for raw in index_text.splitlines():
        line = raw.rstrip()
        if line.strip().lower().startswith("## dependencies"):
            in_deps = True
            continue
        if in_deps and line.strip().startswith("## "):
            in_deps = False
            continue
        if not in_deps:
            continue
        if not line.strip().startswith("- "):
            continue
        payload = line.strip()[2:]
        if ":" not in payload:
            continue
        spec_id, dep_str = payload.split(":", 1)
        spec_id = spec_id.strip()
        dep_str = dep_str.strip()
        if dep_str.lower() in {"none", "无", "n/a"}:
            deps[spec_id] = []
            continue
        dep_list = [d.strip() for d in dep_str.split(",") if d.strip()]
        deps[spec_id] = dep_list
    return deps


def detect_cycles(nodes: set[str], edges: dict[str, list[str]]) -> list[list[str]]:
    visiting: set[str] = set()
    visited: set[str] = set()
    stack: list[str] = []
    cycles: list[list[str]] = []

    def visit(n: str) -> None:
        if n in visited:
            return
        if n in visiting:
            if n in stack:
                idx = stack.index(n)
                cycles.append(stack[idx:] + [n])
            return
        visiting.add(n)
        stack.append(n)
        for m in edges.get(n, []):
            if m in nodes:
                visit(m)
        stack.pop()
        visiting.remove(n)
        visited.add(n)

    for node in sorted(nodes):
        if node not in visited:
            visit(node)
    return cycles


def command_list(args: argparse.Namespace, root: Path) -> int:
    specs = list_spec_dirs(root)
    changes = list_change_dirs(root)
    index_path = root / "openspec" / "SPECS_INDEX.md"
    index_text = try_read_text(index_path)
    index_rows = parse_specs_index_table(index_text) if index_text else {}

    if args.specs:
        print(f"SPECS ({len(specs)})")
        for spec in specs:
            spec_path = spec / "spec.md"
            text = try_read_text(spec_path)
            title = spec_title_from_markdown(text) or spec.name
            reqs, scenarios = count_requirements_and_scenarios(text)
            done, total = count_tasks_in_dir(spec)
            pct = 0 if total == 0 else int((done / total) * 100)
            meta = index_rows.get(spec.name, {})
            prio = meta.get("priority")
            gate = meta.get("gate")
            suffix = ""
            if prio or gate:
                suffix = f" [{prio or '-'} {gate or '-'}]"
            print(
                f"- {spec.name}: {title}{suffix} | requirements {reqs}, scenarios {scenarios}, tasks {done}/{total} ({pct}%)"
            )
        return 0

    if args.changes:
        print(f"CHANGES ({len(changes)})")
        for change in changes:
            done, total = count_tasks_in_dir(change)
            pct = 0 if total == 0 else int((done / total) * 100)
            print(f"- {change.name}: tasks {done}/{total} ({pct}%)")
        return 0

    # Summary view
    req_total = 0
    scenario_total = 0
    for spec in specs:
        spec_path = spec / "spec.md"
        if not spec_path.exists():
            continue
        text = read_text(spec_path)
        reqs, scenarios = count_requirements_and_scenarios(text)
        req_total += reqs
        scenario_total += scenarios

    spec_done, spec_total = count_tasks_in_dir(root / "openspec" / "specs")
    change_done, change_total = count_tasks_in_dir(root / "openspec" / "changes")
    all_done = spec_done + change_done
    all_total = spec_total + change_total
    pct = 0 if all_total == 0 else int((all_done / all_total) * 100)

    print("OPENSPEC DASHBOARD (仪表盘)")
    print(f"- specs: {len(specs)}")
    print(f"- requirements: {req_total}")
    print(f"- scenarios: {scenario_total}")
    print(f"- changes: {len(changes)}")
    print(f"- tasks: {all_done}/{all_total} ({pct}%)")
    return 0


def command_validate(args: argparse.Namespace, root: Path) -> int:
    specs = list_spec_dirs(root)
    index_path = root / "openspec" / "SPECS_INDEX.md"
    index_text = try_read_text(index_path)
    index_rows = parse_specs_index_table(index_text) if index_text else {}
    deps_map = parse_specs_index_deps(index_text) if index_text else {}
    errors: list[str] = []

    # Validate index vs directory listing when index exists
    if index_rows:
        spec_dir_names = {p.name for p in specs}
        index_ids = set(index_rows.keys())
        missing_in_dir = sorted(index_ids - spec_dir_names)
        if missing_in_dir:
            errors.append(
                f"SPECS_INDEX.md: listed specs missing from openspec/specs/: {', '.join(missing_in_dir)}"
            )
        missing_in_index = sorted(spec_dir_names - index_ids)
        if missing_in_index:
            errors.append(
                f"SPECS_INDEX.md: spec dirs missing from table: {', '.join(missing_in_index)}"
            )

    # Validate dependency graph when deps section exists
    if deps_map:
        nodes = set(index_rows.keys()) if index_rows else {p.name for p in specs}
        for src, deps in deps_map.items():
            if src not in nodes:
                continue
            for dep in deps:
                if dep not in nodes:
                    errors.append(f"SPECS_INDEX.md: {src} depends on unknown spec: {dep}")
        cycles = detect_cycles(nodes, deps_map)
        for cycle in cycles:
            errors.append(f"SPECS_INDEX.md: dependency cycle: {' -> '.join(cycle)}")

    for spec in specs:
        spec_path = spec / "spec.md"
        if not spec_path.exists():
            errors.append(f"{spec.name}: missing spec.md")
            continue
        text = read_text(spec_path)
        checks = requirement_checks(text)
        for check in checks:
            if not check.ok:
                errors.append(f"{spec.name}: {check.message}")

        if args.strict:
            required = ["requirements.md", "tasks.md", "design.md", "acceptance.md"]
            for fname in required:
                if not (spec / fname).exists():
                    errors.append(f"{spec.name}: missing {fname}")

            tasks_path = spec / "tasks.md"
            done, total = count_tasks_from_file(tasks_path)
            if total and (total < 12 or total > 30):
                errors.append(
                    f"{spec.name}: tasks.md must have 12~30 checklist items (found {total})"
                )
            required_sections = [
                "Contracts & Interfaces",
                "Data & Integrity",
                "Runtime Behavior",
                "Observability & Metrics",
                "Security/Compliance",
                "Performance/Cost",
                "Tests/Validation",
                "Rollout/Risks",
            ]
            tasks_text = try_read_text(tasks_path)
            for sec in required_sections:
                if sec not in tasks_text:
                    errors.append(f"{spec.name}: tasks.md missing section: {sec}")

    # Validate change skeletons
    for change in list_change_dirs(root):
        if not (change / "proposal.md").exists():
            errors.append(f"{change.name}: missing proposal.md")
        if not (change / "tasks.md").exists():
            errors.append(f"{change.name}: missing tasks.md")

    if errors:
        print("INVALID")
        for err in errors:
            print(f"- {err}")
        return 1
    print("VALID")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="openspec", add_help=True)
    parser.add_argument("--version", action="store_true")
    subparsers = parser.add_subparsers(dest="command")

    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("--specs", action="store_true")
    list_parser.add_argument("--changes", action="store_true")

    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("--strict", action="store_true")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.version:
        print(VERSION)
        return 0
    root = Path(os.getcwd())
    if args.command == "list":
        return command_list(args, root)
    if args.command == "validate":
        return command_validate(args, root)
    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
