"""
Authentication Middleware

认证中间件。

对照 tasks.md 13.6:
- Requirements: 6.3.1
"""

import logging
import os
from typing import Optional

from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader

logger = logging.getLogger(__name__)

# API Key Header
API_KEY_HEADER = APIKeyHeader(name="X-API-Key", auto_error=False)

# 有效的 API Keys (生产环境应从安全存储获取)
def _get_valid_api_keys() -> set:
    """获取有效的 API Keys"""
    keys_str = os.getenv("API_KEYS", "")
    if keys_str:
        return set(k.strip() for k in keys_str.split(",") if k.strip())
    # 开发环境默认 key
    return {"dev-api-key-12345"}


async def api_key_auth(api_key: Optional[str] = Security(API_KEY_HEADER)) -> str:
    """
    API Key 认证依赖
    
    用法:
    ```python
    @router.get("/protected")
    async def protected_route(api_key: str = Depends(api_key_auth)):
        ...
    ```
    """
    if api_key is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing API Key",
            headers={"WWW-Authenticate": "API-Key"},
        )
    
    valid_keys = _get_valid_api_keys()
    if api_key not in valid_keys:
        logger.warning("Invalid API key attempt")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API Key",
        )
    
    return api_key


class AuthMiddleware:
    """
    认证中间件 (可选)
    
    用于全局 API Key 验证。
    对于需要更细粒度控制的场景，使用 api_key_auth 依赖。
    """
    
    # 不需要认证的路径
    EXEMPT_PATHS = {
        "/",
        "/health",
        "/ready",
        "/live",
        "/version",
        "/docs",
        "/openapi.json",
        "/redoc",
    }
    
    def __init__(self, app):
        self.app = app
    
    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        
        path = scope.get("path", "")
        
        # 豁免路径直接放行
        if path in self.EXEMPT_PATHS or path.startswith("/docs"):
            await self.app(scope, receive, send)
            return
        
        # 检查 API Key
        headers = dict(scope.get("headers", []))
        api_key = headers.get(b"x-api-key", b"").decode()
        
        valid_keys = _get_valid_api_keys()
        if api_key not in valid_keys:
            # 返回 401
            response = {
                "type": "http.response.start",
                "status": 401,
                "headers": [[b"content-type", b"application/json"]],
            }
            await send(response)
            await send({
                "type": "http.response.body",
                "body": b'{"error": "Unauthorized", "message": "Invalid or missing API key"}',
            })
            return
        
        await self.app(scope, receive, send)
