"""
Analyze Endpoint Tests

对照 tasks.md 13.3, 13.9:
- Requirements: 6.1.1, 6.2.1, 8.1.3
"""

import pytest


class TestAnalyzeEndpoint:
    """分析端点测试"""
    
    def test_analyze_with_birth_data(self, client):
        """测试带出生数据的分析"""
        response = client.post(
            "/api/v1/analyze",
            json={
                "user_id": "test_user_001",
                "birth_data": {
                    "year": 1990,
                    "month": 6,
                    "day": 15,
                    "hour": 10,
                },
                "include_narrative": True,
            },
        )
        
        assert response.status_code == 200
        data = response.json()
        
        assert "request_id" in data
        assert "fusion_id" in data
        assert "primary_themes" in data
        assert "cross_validation_score" in data
        assert "contributing_engines" in data
        assert "narrative" in data
        assert "processing_time_ms" in data
    
    def test_analyze_with_dream_text(self, client):
        """测试带梦境文本的分析"""
        response = client.post(
            "/api/v1/analyze",
            json={
                "user_id": "test_user_001",
                "dream_text": "我梦见自己在飞，飞过一片金色的麦田",
                "include_narrative": True,
            },
        )
        
        assert response.status_code == 200
        data = response.json()
        
        assert "dream" in data["contributing_engines"]
    
    def test_analyze_with_tarot(self, client):
        """测试带塔罗牌的分析"""
        response = client.post(
            "/api/v1/analyze",
            json={
                "user_id": "test_user_001",
                "tarot_spread": {
                    "cards": ["The Fool", "The Magician"],
                    "spread_type": "two_card",
                },
            },
        )
        
        assert response.status_code == 200
        data = response.json()
        
        assert "tarot" in data["contributing_engines"]
    
    def test_analyze_without_narrative(self, client):
        """测试不生成叙事的分析"""
        response = client.post(
            "/api/v1/analyze",
            json={
                "user_id": "test_user_001",
                "birth_data": {
                    "year": 1985,
                    "month": 3,
                    "day": 20,
                    "hour": 14,
                },
                "include_narrative": False,
            },
        )
        
        assert response.status_code == 200
        data = response.json()
        
        assert data["narrative"] is None
    
    def test_analyze_missing_user_id(self, client):
        """测试缺少用户 ID"""
        response = client.post(
            "/api/v1/analyze",
            json={
                "birth_data": {
                    "year": 1990,
                    "month": 1,
                    "day": 1,
                    "hour": 0,
                },
            },
        )
        
        assert response.status_code == 422  # Validation error


class TestAnalyzeValidation:
    """分析请求验证测试"""
    
    def test_invalid_birth_year(self, client):
        """测试无效的出生年份"""
        response = client.post(
            "/api/v1/analyze",
            json={
                "user_id": "test_user",
                "birth_data": {
                    "year": 1800,  # 太早
                    "month": 1,
                    "day": 1,
                    "hour": 0,
                },
            },
        )
        
        assert response.status_code == 422
    
    def test_invalid_birth_month(self, client):
        """测试无效的出生月份"""
        response = client.post(
            "/api/v1/analyze",
            json={
                "user_id": "test_user",
                "birth_data": {
                    "year": 1990,
                    "month": 13,  # 无效
                    "day": 1,
                    "hour": 0,
                },
            },
        )
        
        assert response.status_code == 422
