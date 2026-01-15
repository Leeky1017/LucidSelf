"""
Playbook Generator Tests

对照 tasks.md 15:
- Requirements: 7.1.1-7.1.3, 8.1.1
"""

import pytest
from datetime import date

from backend.services.playbook.generator import (
    PlaybookGenerator,
    Playbook,
    PlaybookType,
    PlaybookSection,
)
from backend.services.playbook.cache import PlaybookCache


class TestPlaybookGeneratorBasic:
    """基础测试"""
    
    def test_generate_daily(self):
        """测试生成日报"""
        generator = PlaybookGenerator()
        
        playbook = generator.generate(
            user_id="user_001",
            playbook_type=PlaybookType.DAILY,
            use_cache=False,
        )
        
        assert playbook.playbook_id.startswith("pb_")
        assert playbook.user_id == "user_001"
        assert playbook.playbook_type == PlaybookType.DAILY
        assert len(playbook.sections) == 4  # 4 个维度
    
    def test_generate_weekly(self):
        """测试生成周报"""
        generator = PlaybookGenerator()
        
        playbook = generator.generate(
            user_id="user_001",
            playbook_type=PlaybookType.WEEKLY,
            use_cache=False,
        )
        
        assert playbook.playbook_type == PlaybookType.WEEKLY
        assert "-W" in playbook.date_range
    
    def test_generate_monthly(self):
        """测试生成月报"""
        generator = PlaybookGenerator()
        
        playbook = generator.generate(
            user_id="user_001",
            playbook_type=PlaybookType.MONTHLY,
            use_cache=False,
        )
        
        assert playbook.playbook_type == PlaybookType.MONTHLY


class TestPlaybookContent:
    """内容测试"""
    
    def test_has_all_dimensions(self):
        """测试包含所有维度"""
        generator = PlaybookGenerator()
        
        playbook = generator.generate(
            user_id="user_001",
            playbook_type=PlaybookType.DAILY,
            use_cache=False,
        )
        
        dimensions = {s.dimension for s in playbook.sections}
        assert dimensions == {"事业", "财富", "感情", "健康"}
    
    def test_has_summary(self):
        """测试有总结"""
        generator = PlaybookGenerator()
        
        playbook = generator.generate(
            user_id="user_001",
            playbook_type=PlaybookType.DAILY,
            use_cache=False,
        )
        
        assert len(playbook.summary) > 0
        assert "运势" in playbook.summary
    
    def test_has_advice(self):
        """测试有建议"""
        generator = PlaybookGenerator()
        
        playbook = generator.generate(
            user_id="user_001",
            playbook_type=PlaybookType.DAILY,
            use_cache=False,
        )
        
        assert len(playbook.advice) > 0
    
    def test_has_lucky_elements(self):
        """测试有幸运元素"""
        generator = PlaybookGenerator()
        
        playbook = generator.generate(
            user_id="user_001",
            playbook_type=PlaybookType.DAILY,
            use_cache=False,
        )
        
        assert len(playbook.lucky_elements) > 0
    
    def test_overall_score(self):
        """测试综合分数"""
        generator = PlaybookGenerator()
        
        playbook = generator.generate(
            user_id="user_001",
            playbook_type=PlaybookType.DAILY,
            use_cache=False,
        )
        
        assert 0 <= playbook.overall_score <= 100


class TestPlaybookCache:
    """缓存测试"""
    
    def test_cache_hit(self):
        """测试缓存命中"""
        cache = PlaybookCache()
        generator = PlaybookGenerator(cache=cache)
        
        # 第一次生成
        playbook1 = generator.generate(
            user_id="user_001",
            playbook_type=PlaybookType.DAILY,
            use_cache=True,
        )
        
        # 第二次应该从缓存获取
        playbook2 = generator.generate(
            user_id="user_001",
            playbook_type=PlaybookType.DAILY,
            use_cache=True,
        )
        
        assert playbook1.playbook_id == playbook2.playbook_id
    
    def test_cache_bypass(self):
        """测试绕过缓存"""
        cache = PlaybookCache()
        generator = PlaybookGenerator(cache=cache)
        
        # 第一次生成
        playbook1 = generator.generate(
            user_id="user_001",
            playbook_type=PlaybookType.DAILY,
            use_cache=True,
        )
        
        # 绕过缓存
        playbook2 = generator.generate(
            user_id="user_001",
            playbook_type=PlaybookType.DAILY,
            use_cache=False,
        )
        
        assert playbook1.playbook_id != playbook2.playbook_id
    
    def test_invalidate_cache(self):
        """测试使缓存失效"""
        cache = PlaybookCache()
        generator = PlaybookGenerator(cache=cache)
        
        # 生成并缓存
        playbook1 = generator.generate(
            user_id="user_001",
            playbook_type=PlaybookType.DAILY,
            use_cache=True,
        )
        
        # 使缓存失效
        generator.invalidate_cache("user_001")
        
        # 重新生成
        playbook2 = generator.generate(
            user_id="user_001",
            playbook_type=PlaybookType.DAILY,
            use_cache=True,
        )
        
        assert playbook1.playbook_id != playbook2.playbook_id


class TestPlaybookModel:
    """Playbook 模型测试"""
    
    def test_playbook_creation(self):
        """测试 Playbook 创建"""
        playbook = Playbook(
            playbook_id="pb_test123",
            user_id="user_001",
            playbook_type=PlaybookType.DAILY,
            date_range="2024-12-06",
            title="测试日报",
            summary="测试总结",
        )
        
        assert playbook.playbook_id == "pb_test123"
        assert playbook.user_id == "user_001"
    
    def test_playbook_section_creation(self):
        """测试 PlaybookSection 创建"""
        section = PlaybookSection(
            title="事业运势",
            content="事业运势良好",
            dimension="事业",
            score=85.0,
        )
        
        assert section.dimension == "事业"
        assert section.score == 85.0
