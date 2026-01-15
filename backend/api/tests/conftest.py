"""
API Test Fixtures
"""

import pytest
from fastapi.testclient import TestClient

from backend.api.main import create_app


@pytest.fixture
def app():
    """创建测试应用"""
    return create_app(
        debug=True,
        enable_auth=False,
        enable_rate_limit=False,
    )


@pytest.fixture
def client(app):
    """创建测试客户端"""
    return TestClient(app)


@pytest.fixture
def client_with_auth():
    """创建带认证的测试客户端"""
    app = create_app(
        debug=True,
        enable_auth=True,
        enable_rate_limit=False,
    )
    return TestClient(app)


@pytest.fixture
def api_key():
    """测试用 API Key"""
    return "dev-api-key-12345"
