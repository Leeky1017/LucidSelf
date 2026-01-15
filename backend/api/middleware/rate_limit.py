"""
Rate Limiting Middleware

限流中间件。

对照 tasks.md 13.7:
- Requirements: 6.3.3
"""

import logging
import time
from collections import defaultdict
from dataclasses import dataclass, field
from threading import Lock
from typing import Dict, Optional

from fastapi import HTTPException, Request, status

logger = logging.getLogger(__name__)


@dataclass
class RateLimitBucket:
    """令牌桶"""
    tokens: float
    last_update: float
    
    def refill(self, rate: float, capacity: float) -> None:
        """补充令牌"""
        now = time.time()
        elapsed = now - self.last_update
        self.tokens = min(capacity, self.tokens + elapsed * rate)
        self.last_update = now
    
    def consume(self, tokens: int = 1) -> bool:
        """消费令牌"""
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False


class RateLimiter:
    """
    令牌桶限流器
    
    支持:
    - Per-user 限流
    - 突发允许 (burst)
    """
    
    def __init__(
        self,
        rate: float = 10.0,      # 每秒请求数
        capacity: float = 20.0,  # 最大突发量
    ):
        self.rate = rate
        self.capacity = capacity
        self._buckets: Dict[str, RateLimitBucket] = {}
        self._lock = Lock()
    
    def is_allowed(self, key: str) -> bool:
        """检查是否允许请求"""
        with self._lock:
            if key not in self._buckets:
                self._buckets[key] = RateLimitBucket(
                    tokens=self.capacity,
                    last_update=time.time(),
                )
            
            bucket = self._buckets[key]
            bucket.refill(self.rate, self.capacity)
            return bucket.consume()
    
    def get_remaining(self, key: str) -> int:
        """获取剩余令牌数"""
        with self._lock:
            bucket = self._buckets.get(key)
            if bucket:
                bucket.refill(self.rate, self.capacity)
                return int(bucket.tokens)
            return int(self.capacity)
    
    def cleanup(self, max_age: float = 3600.0) -> int:
        """清理过期的桶"""
        now = time.time()
        removed = 0
        with self._lock:
            expired_keys = [
                k for k, v in self._buckets.items()
                if now - v.last_update > max_age
            ]
            for key in expired_keys:
                del self._buckets[key]
                removed += 1
        return removed


# 全局限流器
_global_limiter = RateLimiter(rate=10.0, capacity=20.0)
_user_limiters: Dict[str, RateLimiter] = defaultdict(
    lambda: RateLimiter(rate=5.0, capacity=10.0)
)


async def rate_limit_dependency(request: Request) -> None:
    """
    限流依赖
    
    用法:
    ```python
    @router.get("/api")
    async def api_route(
        _: None = Depends(rate_limit_dependency)
    ):
        ...
    ```
    """
    # 获取客户端标识
    client_ip = request.client.host if request.client else "unknown"
    user_id = request.headers.get("X-User-ID", client_ip)
    
    # 检查全局限流
    if not _global_limiter.is_allowed("global"):
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many requests (global limit)",
            headers={"Retry-After": "1"},
        )
    
    # 检查用户限流
    user_limiter = _user_limiters[user_id]
    if not user_limiter.is_allowed(user_id):
        remaining = user_limiter.get_remaining(user_id)
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many requests (user limit)",
            headers={
                "Retry-After": "1",
                "X-RateLimit-Remaining": str(remaining),
            },
        )


class RateLimitMiddleware:
    """
    限流中间件
    
    全局限流，适用于简单场景。
    复杂场景建议使用 rate_limit_dependency。
    """
    
    EXEMPT_PATHS = {"/health", "/ready", "/live", "/version"}
    
    def __init__(self, app, rate: float = 100.0, capacity: float = 200.0):
        self.app = app
        self.limiter = RateLimiter(rate=rate, capacity=capacity)
    
    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        
        path = scope.get("path", "")
        if path in self.EXEMPT_PATHS:
            await self.app(scope, receive, send)
            return
        
        client = scope.get("client", ("unknown", 0))
        client_ip = client[0] if client else "unknown"
        
        if not self.limiter.is_allowed(client_ip):
            response = {
                "type": "http.response.start",
                "status": 429,
                "headers": [
                    [b"content-type", b"application/json"],
                    [b"retry-after", b"1"],
                ],
            }
            await send(response)
            await send({
                "type": "http.response.body",
                "body": b'{"error": "Too Many Requests"}',
            })
            return
        
        await self.app(scope, receive, send)
