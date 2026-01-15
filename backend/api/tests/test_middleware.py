"""
Middleware Tests

对照 tasks.md 13.6-13.8:
- Requirements: 6.3.1-6.3.3
"""

import pytest
from fastapi.testclient import TestClient

from backend.api.main import create_app
from backend.api.middleware.rate_limit import RateLimiter


class TestRateLimiter:
    """限流器测试"""
    
    def test_basic_rate_limit(self):
        """测试基本限流"""
        limiter = RateLimiter(rate=2.0, capacity=3.0)
        
        # 前三个请求应该通过 (capacity=3)
        assert limiter.is_allowed("test") is True
        assert limiter.is_allowed("test") is True
        assert limiter.is_allowed("test") is True
        
        # 第四个请求应该被限流
        assert limiter.is_allowed("test") is False
    
    def test_different_keys(self):
        """测试不同 key 独立限流"""
        limiter = RateLimiter(rate=1.0, capacity=1.0)
        
        assert limiter.is_allowed("user1") is True
        assert limiter.is_allowed("user2") is True
        
        # user1 被限流，user2 仍然可以
        assert limiter.is_allowed("user1") is False
    
    def test_get_remaining(self):
        """测试获取剩余令牌"""
        limiter = RateLimiter(rate=1.0, capacity=5.0)
        
        assert limiter.get_remaining("test") == 5
        
        limiter.is_allowed("test")
        assert limiter.get_remaining("test") == 4


class TestRequestLogging:
    """请求日志测试"""
    
    def test_request_id_header(self, client):
        """测试响应包含请求 ID"""
        # 使用非豁免路径 (health 在 SKIP_PATHS 中)
        response = client.get("/")
        
        assert "x-request-id" in response.headers
        assert response.headers["x-request-id"].startswith("req_")
    
    def test_response_time_header(self, client):
        """测试响应包含处理时间"""
        response = client.get("/")
        
        assert "x-response-time" in response.headers
        assert "ms" in response.headers["x-response-time"]


class TestRateLimitMiddleware:
    """限流中间件测试"""
    
    def test_rate_limit_exempt_paths(self):
        """测试豁免路径不受限流"""
        app = create_app(
            debug=True,
            enable_auth=False,
            enable_rate_limit=True,
        )
        client = TestClient(app)
        
        # 健康检查应该不受限流
        for _ in range(10):
            response = client.get("/health")
            assert response.status_code == 200
