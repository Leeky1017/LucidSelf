"""
Rule Result Cache

规则结果缓存。

对照 design.md §6.1 三层缓存架构
对照 Requirements R-6-6-02, R-6-6-06
"""

from __future__ import annotations

import hashlib
import json
from typing import Any, Dict, List, Optional

from backend.core.cache.semantic_cache import SemanticCache


class RuleResultCache(SemanticCache[List[Any]]):
    """
    规则结果缓存
    
    对照 R-6-6-02, R-6-6-06
    
    使用因子组合哈希作为缓存键。
    """
    
    def __init__(
        self,
        max_size: int = 5000,
        ttl_seconds: Optional[float] = 1800,  # 30 分钟
    ):
        """
        初始化规则结果缓存
        
        Args:
            max_size: 最大缓存条目数
            ttl_seconds: TTL 秒数
        """
        super().__init__(
            max_size=max_size,
            ttl_seconds=ttl_seconds,
            cache_type="rule",
        )
    
    def compute_key(
        self,
        engine_id: str,
        factors: Dict[str, Any],
    ) -> str:
        """
        计算因子组合哈希
        
        对照 R-6-6-06
        
        Args:
            engine_id: 引擎ID
            factors: 因子字典
            
        Returns:
            缓存键
        """
        # 确保因子排序以保证一致性
        factors_str = json.dumps(factors, sort_keys=True, default=str)
        content = f"{engine_id}:{factors_str}"
        return hashlib.sha256(content.encode()).hexdigest()[:16]
    
    def get_by_factors(
        self,
        engine_id: str,
        factors: Dict[str, Any],
    ) -> Optional[List[Any]]:
        """
        通过因子获取缓存结果
        
        Args:
            engine_id: 引擎ID
            factors: 因子字典
            
        Returns:
            缓存的规则结果列表
        """
        key = self.compute_key(engine_id, factors)
        return self.get(key)
    
    def set_by_factors(
        self,
        engine_id: str,
        factors: Dict[str, Any],
        results: List[Any],
        ttl_seconds: Optional[float] = None,
    ) -> None:
        """
        通过因子设置缓存结果
        
        Args:
            engine_id: 引擎ID
            factors: 因子字典
            results: 规则结果列表
            ttl_seconds: TTL 秒数
        """
        key = self.compute_key(engine_id, factors)
        self.set(key, results, ttl_seconds)
    
    def invalidate_by_engine(self, engine_id: str) -> int:
        """
        失效指定引擎的所有缓存
        
        Args:
            engine_id: 引擎ID
            
        Returns:
            失效的条目数
        """
        # 由于我们的 key 是哈希值，无法直接按 engine_id 筛选
        # 需要存储额外的映射或清空全部
        # 这里采用简单方案：清空所有
        return self.clear()
