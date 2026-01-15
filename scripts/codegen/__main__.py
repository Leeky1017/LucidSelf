"""
Codegen Pipeline Entry Point

Usage:
    python -m scripts.codegen compile rule <source.json>
    python -m scripts.codegen compile factor <source.jsonl> --engine-id bazi
    python -m scripts.codegen compile semantic <source.md> --engine-id bazi
    python -m scripts.codegen validate rule <source.json>
    python -m scripts.codegen clean
    python -m scripts.codegen status
"""

import sys

from scripts.codegen.cli import main

if __name__ == "__main__":
    sys.exit(main())
