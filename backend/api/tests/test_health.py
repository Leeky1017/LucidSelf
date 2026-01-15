"""
Health Endpoint Tests

对照 tasks.md 13.5, 13.9:
- Requirements: 6.1.3, 6.1.4, 8.1.3
"""

import pytest


class TestHealthEndpoints:
    """健康检查端点测试"""
    
    def test_health_check(self, client):
        """测试 /health 端点"""
        response = client.get("/health")
        
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert "version" in data
        assert "timestamp" in data
    
    def test_version_info(self, client):
        """测试 /version 端点"""
        response = client.get("/version")
        
        assert response.status_code == 200
        data = response.json()
        assert "version" in data
        assert "api_version" in data
    
    def test_readiness_check(self, client):
        """测试 /ready 端点"""
        response = client.get("/ready")
        
        assert response.status_code == 200
        data = response.json()
        assert data["ready"] is True
    
    def test_liveness_check(self, client):
        """测试 /live 端点"""
        response = client.get("/live")
        
        assert response.status_code == 200
        data = response.json()
        assert data["alive"] is True


class TestRootEndpoint:
    """根端点测试"""
    
    def test_root(self, client):
        """测试根路由"""
        response = client.get("/")
        
        assert response.status_code == 200
        data = response.json()
        assert "name" in data
        assert "version" in data
        assert data["docs"] == "/docs"
