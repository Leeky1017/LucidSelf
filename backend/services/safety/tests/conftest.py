"""
Safety Moderation Test Fixtures
"""

import pytest

from backend.services.safety.moderator import SafetyModerator
from backend.services.safety.crisis_handler import CrisisHandler


@pytest.fixture
def moderator_zh():
    """中文审核器"""
    return SafetyModerator(language="zh")


@pytest.fixture
def moderator_en():
    """英文审核器"""
    return SafetyModerator(language="en")


@pytest.fixture
def crisis_handler_zh():
    """中文危机处理器"""
    return CrisisHandler(language="zh")


@pytest.fixture
def crisis_handler_en():
    """英文危机处理器"""
    return CrisisHandler(language="en")
