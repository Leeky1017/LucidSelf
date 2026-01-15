"""
Rule ID Generator

生成唯一的规则 ID。

Feature: rule-converter
Requirement Refs: Req 7.1-7.5
"""

import logging
import re
from typing import Dict, Set

logger = logging.getLogger(__name__)


# 规则ID正则（来自 backend/core/contracts/base.py）
RULE_ID_PATTERN = re.compile(r"^[a-z][a-z0-9_]*$")


class RuleIdGenerator:
    """
    规则ID生成器
    
    生成唯一的规则 ID，格式：{system}_{book_abbr}_{category}_{seq:03d}
    
    例如：
    - bazi_dts_career_001
    - ziwei_zwds_palace_012
    - tarot_78d_major_005
    
    Requirement Refs: Req 7.1-7.5
    """
    
    # 书籍缩写映射
    BOOK_ABBR_MAP: Dict[str, str] = {
        "ditianshui": "dts",
        "zipingzhenquan": "zpzq",
        "sanminghui": "smth",
        "yuanhaiziping": "yhzp",
        "qiongtongbaojian": "qtbj",
        "ziweidoushu": "zwds",
        "zhouyi": "zy",
        "zhougongjiemeng": "zgjm",
        "menglinxuanjie": "mlxj",
        "inner_sky": "tis",
        "christian_astrology": "ca",
        "tetrabiblos": "ttb",
        "planets_transit": "pit",
        "astro_houses": "tah",
        "astro_personality": "aop",
        "78_degrees": "78d",
        "waite_key": "wpk",
        "learning_tarot": "ltt",
        "book_thoth": "bot",
        "jung_archetypes": "jacu",
    }
    
    # 书籍到体系的映射
    BOOK_SYSTEM_MAP: Dict[str, str] = {
        "ditianshui": "bazi",
        "zipingzhenquan": "bazi",
        "sanminghui": "bazi",
        "yuanhaiziping": "bazi",
        "qiongtongbaojian": "bazi",
        "ziweidoushu": "ziwei",
        "zhouyi": "yijing",
        "zhougongjiemeng": "dream",
        "menglinxuanjie": "dream",
        "inner_sky": "astro",
        "christian_astrology": "astro",
        "tetrabiblos": "astro",
        "planets_transit": "astro",
        "astro_houses": "astro",
        "astro_personality": "astro",
        "78_degrees": "tarot",
        "waite_key": "tarot",
        "learning_tarot": "tarot",
        "book_thoth": "tarot",
        "jung_archetypes": "psychology",
    }
    
    def __init__(self):
        self._registry: Set[str] = set()
        self._counters: Dict[str, int] = {}  # {prefix: current_count}
    
    def generate(
        self,
        book_id: str,
        category: str,
        system: str = None,
    ) -> str:
        """
        生成唯一的规则 ID
        
        Args:
            book_id: 书籍ID（如 "ditianshui"）
            category: 规则类别（如 "career", "wealth"）
            system: 体系（如果不提供，从 book_id 推断）
            
        Returns:
            唯一的规则ID
        """
        # 确定体系
        if not system:
            system = self._get_system(book_id)
        
        # 获取书籍缩写
        book_abbr = self._get_book_abbr(book_id)
        
        # 规范化 category
        category = self._normalize_id(category)
        
        # 构建前缀
        prefix = f"{system}_{book_abbr}_{category}"
        
        # 获取序号
        seq = self._get_next_seq(prefix)
        
        # 生成 ID
        rule_id = f"{prefix}_{seq:03d}"
        
        # 确保唯一性
        while rule_id in self._registry:
            seq = self._get_next_seq(prefix)
            rule_id = f"{prefix}_{seq:03d}"
        
        # 注册
        self._registry.add(rule_id)
        
        # 验证格式
        if not RULE_ID_PATTERN.match(rule_id):
            logger.warning(f"Generated rule_id doesn't match pattern: {rule_id}")
        
        return rule_id
    
    def _get_system(self, book_id: str) -> str:
        """从 book_id 推断体系"""
        normalized = self._normalize_id(book_id)
        return self.BOOK_SYSTEM_MAP.get(normalized, "unknown")
    
    def _get_book_abbr(self, book_id: str) -> str:
        """获取书籍缩写"""
        normalized = self._normalize_id(book_id)
        return self.BOOK_ABBR_MAP.get(normalized, normalized[:4])
    
    def _normalize_id(self, s: str) -> str:
        """规范化为小写下划线格式"""
        result = s.lower()
        result = re.sub(r"[^a-z0-9]", "_", result)
        result = re.sub(r"_+", "_", result)
        return result.strip("_")
    
    def _get_next_seq(self, prefix: str) -> int:
        """获取下一个序号"""
        if prefix not in self._counters:
            self._counters[prefix] = 0
        self._counters[prefix] += 1
        return self._counters[prefix]
    
    def is_unique(self, rule_id: str) -> bool:
        """检查规则ID是否唯一"""
        return rule_id not in self._registry
    
    def register(self, rule_id: str) -> bool:
        """
        注册已有的规则ID
        
        用于导入已存在的规则时保持唯一性
        
        Returns:
            True if registered successfully, False if already exists
        """
        if rule_id in self._registry:
            return False
        self._registry.add(rule_id)
        return True
    
    def reset(self):
        """重置生成器状态"""
        self._registry.clear()
        self._counters.clear()
    
    @property
    def count(self) -> int:
        """已生成的规则ID数量"""
        return len(self._registry)
    
    def get_stats(self) -> Dict[str, int]:
        """获取统计信息"""
        stats = {
            "total_generated": len(self._registry),
            "by_prefix": dict(self._counters),
        }
        return stats
