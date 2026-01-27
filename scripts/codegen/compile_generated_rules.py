#!/usr/bin/env python3
"""
Compile generated JSONL rules into importable Python modules.

Why:
- Gate-1 integration/regression tests expect compiled rule modules under:
  backend/generated/rules/
- Source-of-truth rule definitions live under:
  data/rules/**/*.jsonl
  (includes curated rules + generated conversion outputs)

This script is CI-friendly:
- Does not require black (formatting is skipped if black is absent)
- Fails fast if any compile errors are detected
"""

from __future__ import annotations

from pathlib import Path

from scripts.codegen.rule_generator import RuleCodeGenerator


def main() -> int:
    source_root = Path("data/rules")
    output_dir = Path("backend/generated/rules")
    output_dir.mkdir(parents=True, exist_ok=True)

    # CI/本地一致性：清理旧的生成物，避免残留模块被误导入
    for p in output_dir.glob("*.py"):
        if p.name == "__init__.py":
            continue
        p.unlink()

    rule_files = sorted(source_root.rglob("*.jsonl"))
    if not rule_files:
        print(f"ERROR: no rule jsonl files found under: {source_root}")
        return 2

    generator = RuleCodeGenerator(output_dir=output_dir)

    total_compiled = 0
    total_errors = 0
    for p in rule_files:
        report = generator.compile_jsonl(p, output_dir=output_dir)
        total_compiled += int(report.get("rules_compiled", 0))
        total_errors += len(report.get("errors", []))

    print(
        f"OK: compiled_rules={total_compiled} files={len(rule_files)} output_dir={output_dir}"
    )

    if total_errors:
        print(f"ERROR: rule codegen failures detected: errors={total_errors}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

