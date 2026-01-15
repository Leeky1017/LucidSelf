from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class CheckResult:
    ok: bool
    message: str


def contains_cjk(text: str) -> bool:
    return any("\u4e00" <= ch <= "\u9fff" for ch in text)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def count_tasks(path: Path) -> tuple[int, int]:
    if not path.exists():
        return (0, 0)
    done = 0
    total = 0
    for raw in read_text(path).splitlines():
        line = raw.strip().lower()
        if line.startswith("- [ ]"):
            total += 1
        elif line.startswith("- [x]"):
            total += 1
            done += 1
    return (done, total)


def validate_spec_structure(spec_md: Path) -> list[str]:
    errors: list[str] = []
    text = read_text(spec_md)
    if "## Purpose" not in text:
        errors.append("missing ## Purpose")
    if "## Requirements" not in text:
        errors.append("missing ## Requirements")

    # Requirement blocks
    lines = text.splitlines()
    req_indices = [i for i, ln in enumerate(lines) if ln.startswith("### Requirement:")]
    if not req_indices:
        errors.append("no requirements")
        return errors

    req_indices.append(len(lines))
    for start, end in zip(req_indices, req_indices[1:], strict=False):
        req_name = lines[start][len("### Requirement:") :].strip()
        body = [ln for ln in lines[start + 1 : end] if ln.strip()]
        if not body:
            errors.append(f"Requirement {req_name}: empty body")
            continue
        first = body[0]
        if "MUST" not in first and "SHALL" not in first:
            errors.append(f"Requirement {req_name}: first line missing MUST/SHALL")
        scenario_positions = [i for i, ln in enumerate(body) if ln.startswith("#### Scenario:")]
        if not scenario_positions:
            errors.append(f"Requirement {req_name}: missing scenario")
            continue
        for sidx, sstart in enumerate(scenario_positions):
            sname = body[sstart][len("#### Scenario:") :].strip()
            send = scenario_positions[sidx + 1] if sidx + 1 < len(scenario_positions) else len(body)
            scenario_body = [ln.strip() for ln in body[sstart + 1 : send] if ln.strip()]
            if not scenario_body:
                errors.append(f"Scenario {sname} in {req_name}: empty content")
    return errors


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


def parse_deps_from_index(index_text: str) -> dict[str, list[str]]:
    deps: dict[str, list[str]] = {}
    in_deps = False
    for raw in index_text.splitlines():
        line = raw.strip()
        if line.lower().startswith("## dependencies"):
            in_deps = True
            continue
        if in_deps and line.startswith("## "):
            in_deps = False
            continue
        if not in_deps:
            continue
        if not line.startswith("- "):
            continue
        payload = line[2:]
        if ":" not in payload:
            continue
        spec_id, dep_str = payload.split(":", 1)
        spec_id = spec_id.strip()
        dep_str = dep_str.strip()
        if dep_str.lower() in {"none", "无"}:
            deps[spec_id] = []
            continue
        deps[spec_id] = [d.strip() for d in dep_str.split(",") if d.strip()]
    return deps


def main() -> int:
    openspec_root = Path(__file__).resolve().parents[1]
    specs_root = openspec_root / "specs"
    changes_root = openspec_root / "changes"
    ops_root = openspec_root / "_ops"
    report_path = ops_root / "recheck_report.md"

    checks: list[tuple[str, CheckResult]] = []

    required_top = [
        openspec_root / "project.md",
        openspec_root / "SPECS_INDEX.md",
        openspec_root / "WORKFLOW.md",
        openspec_root / "QUALITY_GATES.md",
    ]
    missing_top = [p for p in required_top if not p.exists()]
    checks.append(
        (
            "Top-level docs",
            CheckResult(ok=not missing_top, message="missing: " + ", ".join(str(p) for p in missing_top) if missing_top else "ok"),
        )
    )

    spec_dirs = sorted([p for p in specs_root.iterdir() if p.is_dir()]) if specs_root.exists() else []
    checks.append(("Spec count", CheckResult(ok=len(spec_dirs) == 26, message=f"{len(spec_dirs)}")))

    # Per-spec file presence and structural validation
    file_errors: list[str] = []
    structure_errors: list[str] = []
    chinese_warnings: list[str] = []
    task_totals: list[int] = []

    required_spec_files = ["spec.md", "requirements.md", "tasks.md", "design.md", "acceptance.md"]
    for spec_dir in spec_dirs:
        for fname in required_spec_files:
            if not (spec_dir / fname).exists():
                file_errors.append(f"{spec_dir.name}: missing {fname}")

        spec_md = spec_dir / "spec.md"
        if spec_md.exists():
            errs = validate_spec_structure(spec_md)
            for e in errs:
                structure_errors.append(f"{spec_dir.name}: {e}")
            if not contains_cjk(read_text(spec_md)):
                chinese_warnings.append(f"{spec_dir.name}: spec.md has no CJK content")

        tasks_md = spec_dir / "tasks.md"
        _, total = count_tasks(tasks_md)
        task_totals.append(total)
        if total and not (12 <= total <= 30):
            file_errors.append(f"{spec_dir.name}: tasks.md checklist count {total} (expected 12~30)")

    checks.append(("Spec required files", CheckResult(ok=not file_errors, message=f"{len(file_errors)} issues")))
    checks.append(("Spec structure (Purpose/Requirements/Scenarios)", CheckResult(ok=not structure_errors, message=f"{len(structure_errors)} issues")))
    checks.append(("Chinese coverage (spec.md)", CheckResult(ok=not chinese_warnings, message=f"{len(chinese_warnings)} warnings")))
    checks.append(("Task checklist range", CheckResult(ok=all((t == 0) or (12 <= t <= 30) for t in task_totals), message=f"min={min(task_totals) if task_totals else 0}, max={max(task_totals) if task_totals else 0}")))

    # Dependency DAG check
    deps_errors: list[str] = []
    index_path = openspec_root / "SPECS_INDEX.md"
    if index_path.exists():
        index_text = read_text(index_path)
        deps = parse_deps_from_index(index_text)
        nodes = {p.name for p in spec_dirs}
        for src, ds in deps.items():
            if src not in nodes:
                continue
            for d in ds:
                if d not in nodes:
                    deps_errors.append(f"{src}: unknown dep {d}")
        for cycle in detect_cycles(nodes, deps):
            deps_errors.append("cycle: " + " -> ".join(cycle))
    checks.append(("Dependency DAG", CheckResult(ok=not deps_errors, message=f"{len(deps_errors)} issues")))

    # Change skeleton check
    change_dirs = sorted([p for p in changes_root.iterdir() if p.is_dir() and p.name not in {"archive", "_archive_"}]) if changes_root.exists() else []
    change_errors: list[str] = []
    for cd in change_dirs:
        for fname in ["proposal.md", "tasks.md"]:
            if not (cd / fname).exists():
                change_errors.append(f"{cd.name}: missing {fname}")
        if (cd / "proposal.md").exists() and not contains_cjk(read_text(cd / "proposal.md")):
            chinese_warnings.append(f"{cd.name}: proposal.md has no CJK content")
    checks.append(("Change count", CheckResult(ok=len(change_dirs) >= 1, message=f"{len(change_dirs)}")))
    checks.append(("Change required files", CheckResult(ok=not change_errors, message=f"{len(change_errors)} issues")))

    # Write report (facts-first)
    lines: list[str] = ["# OpenSpec Recheck Report（事实）", ""]
    for name, result in checks:
        status = "PASS" if result.ok else "FAIL"
        lines.append(f"- {name}: {status} | {result.message}")

    if file_errors:
        lines += ["", "## 文件问题", *[f"- {e}" for e in file_errors]]
    if structure_errors:
        lines += ["", "## 结构问题", *[f"- {e}" for e in structure_errors]]
    if deps_errors:
        lines += ["", "## 依赖问题", *[f"- {e}" for e in deps_errors]]
    if chinese_warnings:
        lines += ["", "## 中文覆盖警告", *[f"- {e}" for e in chinese_warnings]]

    report_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

