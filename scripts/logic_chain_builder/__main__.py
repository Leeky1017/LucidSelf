"""
Logic Chain Builder Entry Point

Usage:
    python -m scripts.logic_chain_builder build <book_id>
    python -m scripts.logic_chain_builder batch
    python -m scripts.logic_chain_builder validate <book_id>
    python -m scripts.logic_chain_builder list
"""

import sys

from scripts.logic_chain_builder.cli import main

if __name__ == "__main__":
    sys.exit(main())
