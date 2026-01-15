"""
Module entry point for running as `python -m scripts.knowledge_graph_builder`

Feature: cross-book-knowledge-graph
Requirement Refs: Req 10.1
"""

import sys
from scripts.knowledge_graph_builder.cli import main

if __name__ == '__main__':
    sys.exit(main())
