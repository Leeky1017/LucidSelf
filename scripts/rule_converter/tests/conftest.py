"""
Pytest configuration for rule_converter tests
"""

import pytest


def pytest_configure(config):
    """Configure pytest"""
    config.addinivalue_line(
        "markers", "integration: mark test as integration test (uses real data)"
    )


# Hypothesis settings (optional)
try:
    from hypothesis import settings, Verbosity
    settings.register_profile("fast", max_examples=10)
    settings.register_profile("ci", max_examples=50)
    settings.register_profile("full", max_examples=100)
    settings.load_profile("fast")
except ImportError:
    pass  # hypothesis not installed
