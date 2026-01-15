"""
Cache Invalidator

缓存失效器。

对照 design.md §6.2 缓存失效
对照 Requirements R-6-6-07, R-6-6-08
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import TYPE_CHECKING, Callable, List, Optional

if TYPE_CHECKING:
    from backend.core.cache.semantic_cache import SemanticCache
    from backend.core.cache.rule_cache import RuleResultCache

logger = logging.getLogger(__name__)


class CacheInvalidator:
    """
    缓存失效器
    
    对照 R-6-6-07, R-6-6-08
    
    监听热重载事件并触发缓存失效。
    """
    
    def __init__(
        self,
        semantic_cache: Optional["SemanticCache"] = None,
        rule_cache: Optional["RuleResultCache"] = None,
        auto_subscribe: bool = True,
    ):
        """
        初始化缓存失效器
        
        Args:
            semantic_cache: 语义缓存实例
            rule_cache: 规则缓存实例
            auto_subscribe: 是否自动订阅热重载事件
        """
        self.semantic_cache = semantic_cache
        self.rule_cache = rule_cache
        self._subscribed = False
        
        if auto_subscribe:
            self.subscribe_to_reload()
    
    def subscribe_to_reload(self) -> None:
        """订阅热重载事件"""
        if self._subscribed:
            return
        
        try:
            from scripts.codegen.hot_reload import register_reload_listener
            register_reload_listener(self._on_reload)
            self._subscribed = True
            logger.info("CacheInvalidator subscribed to reload events")
        except ImportError:
            logger.warning("hot_reload module not available, cache invalidation disabled")
    
    def unsubscribe_from_reload(self) -> None:
        """取消订阅热重载事件"""
        if not self._subscribed:
            return
        
        try:
            from scripts.codegen.hot_reload import unregister_reload_listener
            unregister_reload_listener(self._on_reload)
            self._subscribed = False
        except ImportError:
            pass
    
    def _on_reload(self, file_path: Path) -> None:
        """
        热重载回调
        
        对照 R-6-6-07
        """
        file_path_str = str(file_path)
        
        # 根据文件类型决定失效策略
        if "rules" in file_path_str or file_path_str.endswith(".jsonl"):
            self.invalidate_rule_cache()
        elif "semantic" in file_path_str:
            self.invalidate_semantic_cache_by_file(file_path)
        else:
            # 保守策略：全部失效
            logger.debug(f"Unknown file type, invalidating all caches: {file_path}")
            self.invalidate_all()
    
    def invalidate_rule_cache(self) -> int:
        """
        失效规则缓存
        
        Returns:
            失效的条目数
        """
        if self.rule_cache:
            count = self.rule_cache.clear()
            logger.info(f"Rule cache invalidated: {count} entries cleared")
            return count
        return 0
    
    def invalidate_semantic_cache(self) -> int:
        """
        失效语义缓存
        
        Returns:
            失效的条目数
        """
        if self.semantic_cache:
            count = self.semantic_cache.clear()
            logger.info(f"Semantic cache invalidated: {count} entries cleared")
            return count
        return 0
    
    def invalidate_semantic_cache_by_file(self, file_path: Path) -> int:
        """
        根据文件失效相关语义缓存
        
        目前简化实现：清空全部语义缓存。
        未来可根据文件路径推断需要失效的特定条目。
        """
        return self.invalidate_semantic_cache()
    
    def invalidate_all(self) -> int:
        """
        失效所有缓存
        
        Returns:
            失效的条目数
        """
        total = 0
        total += self.invalidate_semantic_cache()
        total += self.invalidate_rule_cache()
        return total
    
    def invalidate_by_key(self, key: str) -> bool:
        """
        手动失效指定键
        
        对照 R-6-6-08
        
        Args:
            key: 缓存键
            
        Returns:
            True 如果删除成功
        """
        deleted = False
        
        if self.semantic_cache and self.semantic_cache.delete(key):
            deleted = True
        
        if self.rule_cache and self.rule_cache.delete(key):
            deleted = True
        
        return deleted
    
    def get_stats(self) -> dict:
        """获取缓存统计"""
        stats = {}
        
        if self.semantic_cache:
            s = self.semantic_cache.stats
            stats["semantic"] = {
                "hits": s.hits,
                "misses": s.misses,
                "hit_ratio": s.hit_ratio,
                "size": s.size,
                "evictions": s.evictions,
            }
        
        if self.rule_cache:
            s = self.rule_cache.stats
            stats["rule"] = {
                "hits": s.hits,
                "misses": s.misses,
                "hit_ratio": s.hit_ratio,
                "size": s.size,
                "evictions": s.evictions,
            }
        
        return stats
