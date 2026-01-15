"""
Interpret Endpoint Tests

对照 tasks.md 13.4, 13.9:
- Requirements: 6.1.2, 8.1.3
"""

import pytest


class TestInterpretEndpoint:
    """解读端点测试"""
    
    def test_interpret_with_fusion_id(self, client):
        """测试使用 fusion_id 的解读"""
        response = client.post(
            "/api/v1/interpret",
            json={
                "user_id": "test_user_001",
                "fusion_id": "fus_abc123456789",
            },
        )
        
        assert response.status_code == 200
        data = response.json()
        
        assert "request_id" in data
        assert "fusion_id" in data
        assert "narrative" in data
        assert "processing_time_ms" in data
    
    def test_interpret_with_question(self, client):
        """测试带问题的解读"""
        response = client.post(
            "/api/v1/interpret",
            json={
                "user_id": "test_user_001",
                "fusion_id": "fus_abc123456789",
                "question": "我今年适合换工作吗？",
            },
        )
        
        assert response.status_code == 200
        data = response.json()
        
        # 叙事应该包含问题相关内容
        assert "换工作" in data["narrative"]
    
    def test_interpret_english(self, client):
        """测试英文解读"""
        response = client.post(
            "/api/v1/interpret",
            json={
                "user_id": "test_user_001",
                "fusion_id": "fus_abc123456789",
                "language": "en",
            },
        )
        
        assert response.status_code == 200
        data = response.json()
        
        # 英文叙事
        assert "Analysis" in data["narrative"] or "Interpretation" in data["narrative"]
    
    def test_interpret_missing_ids(self, client):
        """测试缺少 ID"""
        response = client.post(
            "/api/v1/interpret",
            json={
                "user_id": "test_user_001",
                # 没有 fusion_id 或 request_id
            },
        )
        
        assert response.status_code == 400
        assert "fusion_id or request_id" in response.json()["detail"]
