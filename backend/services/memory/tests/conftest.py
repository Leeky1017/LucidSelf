"""
Memory Service Test Fixtures
"""

import base64
import secrets
import pytest

from backend.services.memory.models import PrivacyLevel, MemoryEvent, MemoryInsight
from backend.services.memory.encryption import EncryptionHelper
from backend.services.memory.service import MemoryService


@pytest.fixture
def test_key() -> bytes:
    """生成测试密钥"""
    return secrets.token_bytes(32)


@pytest.fixture
def encryption_helper(test_key) -> EncryptionHelper:
    """创建加密助手"""
    return EncryptionHelper(key=test_key)


@pytest.fixture
def memory_service(encryption_helper) -> MemoryService:
    """创建 MemoryService"""
    return MemoryService(encryption_helper=encryption_helper)


@pytest.fixture
def memory_service_no_encryption() -> MemoryService:
    """创建无加密的 MemoryService"""
    return MemoryService(encryption_helper=None)
